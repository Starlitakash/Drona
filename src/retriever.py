import os
import sys
import uuid
import re
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer, CrossEncoder
from rank_bm25 import BM25Okapi
import pdfplumber

load_dotenv()

# ---------------- CONFIGURATION ----------------

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
STORAGE_PATH = os.getenv("QDRANT_STORAGE_PATH", "./qdrant_data")
COLLECTION_NAME = "enterprise_knowledge"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
RERANKER_MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"
VECTOR_DIM = 384


def get_qdrant_client() -> QdrantClient:
    """Connects to Qdrant Cloud if credentials exist, otherwise falls back to local storage."""
    if QDRANT_URL:
        print(f"[Qdrant] Connecting to Qdrant Cloud: {QDRANT_URL}")
        return QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, timeout=60.0)
    return QdrantClient(path=STORAGE_PATH, timeout=60.0)


client = get_qdrant_client()
_collection_verified = False

# Text chunking configuration (~800 characters with 100 character overlap)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100,
    separators=["\n## ", "\n### ", "\n\n", "\n", " "]
)

# Initialize models locally
print(f"[Models] Loading Bi-Encoder: {EMBEDDING_MODEL_NAME}...")
embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)

print(f"[Models] Loading Cross-Encoder Reranker: {RERANKER_MODEL_NAME}...")
reranker_model = CrossEncoder(RERANKER_MODEL_NAME)

# In-memory BM25 index and chunk cache
_bm25_index: Optional[BM25Okapi] = None
_corpus_chunks: List[Dict[str, Any]] = []


# ---------------- COLLECTION SETUP ----------------

def ensure_collection(recreate: bool = False):
    """Create or recreate the Qdrant collection for 384-dimensional cosine embeddings."""
    if client.collection_exists(COLLECTION_NAME):
        if recreate:
            client.delete_collection(COLLECTION_NAME)
            print(f"[Qdrant] Deleted existing collection: {COLLECTION_NAME}")
        else:
            return

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=VECTOR_DIM,
            distance=models.Distance.COSINE
        )
    )
    print(f"[Qdrant] Created collection: {COLLECTION_NAME} (vector_dim={VECTOR_DIM}, metric=Cosine)")


# ================================================================
# DOCUMENT PARSING
# ================================================================
# This section handles reading different file types and converting
# them into clean text + structured elements (tables, headings).
# We use pdfplumber instead of pypdf because pdfplumber understands
# the LAYOUT of a PDF — it can detect tables and read columns in
# the correct order. pypdf just dumps raw text and destroys structure.


def _looks_like_section_heading(text: str) -> bool:
    """
    Checks if a short text line looks like a section heading.

    Examples that return True:
      "4.1 Leave Entitlements"
      "CHAPTER 3: TRAVEL POLICY"
      "Section 2 – Code of Conduct"

    We use this while parsing PDF text blocks to track which
    section each chunk belongs to — so we can store it as metadata.
    """
    text = text.strip()
    # Must be short enough to be a heading (not a full paragraph)
    if len(text) > 120:
        return False
    # Matches patterns like "4.", "4.1", "4.1.2" at the start
    import re as _re
    numbered = bool(_re.match(r'^\d+(\.\d+)*[\s\.:–-]', text))
    # Matches ALL CAPS headings like "CHAPTER 4: BENEFITS"
    all_caps = text.isupper() and len(text.split()) >= 2
    # Matches "Section X" or "Chapter X" style
    keyword = text.lower().startswith(("section", "chapter", "part ", "appendix"))
    return numbered or all_caps or keyword


def _table_to_chunks(
    table: List[List],
    file_name: str,
    page_num: int,
    section: str,
    category: str,
    chunk_counter: int
) -> Tuple[List[str], List[Dict[str, Any]], List[str]]:
    """
    Converts a PDF table (a list of rows, each row a list of cells)
    into one clean text chunk PER DATA ROW.

    Why one chunk per row?
    → If we dump the whole table as one chunk, the AI sees:
      "Annual Leave 21 days Sick Leave 12 days Maternity 26 weeks"
      and can't tell which value belongs to which leave type.

    → If we give it one row at a time like:
      "Leave Type: Annual Leave | Days: 21 | Carry Forward: Yes"
      the AI can perfectly answer "how many annual leave days do I get?"

    Args:
        table:         The raw table data from pdfplumber.
        file_name:     Source PDF filename (stored in metadata).
        page_num:      Page number where this table was found.
        section:       The last section heading seen before this table.
        category:      HR / Finance / etc. (inferred from filename).
        chunk_counter: Running counter to generate unique chunk IDs.

    Returns:
        (texts, payloads, ids) — parallel lists ready for embedding.
    """
    texts, payloads, ids = [], [], []

    if not table or len(table) < 2:
        # A table with only 1 row (just headers, no data) — skip it.
        return texts, payloads, ids

    # The first row is treated as the header (column names).
    # Clean each cell: strip whitespace and replace None with empty string.
    raw_headers = table[0]
    headers = [str(h).strip() if h else "" for h in raw_headers]

    # Process each subsequent row as one data record.
    for row in table[1:]:
        if row is None:
            continue

        # Build "Header: Value" pairs for all cells in this row.
        # Skip pairs where either the header or value is blank.
        pairs = []
        for col_idx, cell in enumerate(row):
            header = headers[col_idx] if col_idx < len(headers) else ""
            value  = str(cell).strip() if cell else ""
            if header and value:
                pairs.append(f"{header}: {value}")

        # If the row had no usable data, skip it.
        if not pairs:
            continue

        # Join all pairs with " | " separator — easy to read, easy to search.
        # Example: "Leave Type: Maternity Leave | Days: 26 weeks | Carry Forward: No"
        row_text = " | ".join(pairs)

        chunk_id   = f"{Path(file_name).stem}_table_{chunk_counter}"
        stable_id  = str(uuid.uuid5(uuid.NAMESPACE_URL, f"{file_name}::table::{chunk_counter}"))

        texts.append(row_text)
        payloads.append({
            "chunk_id":     chunk_id,
            "source":       file_name,
            "page":         page_num,                # Which page this table was on
            "section":      section,                 # e.g. "4.1 Leave Entitlements"
            "element_type": "table",                 # Tells the AI this came from a table
            "category":     category,
            "char_length":  len(row_text),
            "text":         row_text,
        })
        ids.append(stable_id)
        chunk_counter += 1

    return texts, payloads, ids


def _text_to_chunks(
    text_block: str,
    file_name: str,
    page_num: int,
    section: str,
    category: str,
    element_type: str,
    chunk_counter: int
) -> Tuple[List[str], List[Dict[str, Any]], List[str]]:
    """
    Splits a plain text block into chunks using section-aware splitting.

    Splitting priority (we try the least destructive option first):
      1. Split on paragraph breaks (\n\n) — keeps paragraphs together.
      2. Split on newlines (\n) — keeps lines together.
      3. Split on sentence endings (. ) — keeps sentences together.
      4. Last resort: cut at CHUNK_SIZE characters on a word boundary.

    Each chunk gets: source file, page number, section heading, element_type.

    Args:
        element_type: "text" for normal paragraphs, "figure_context" for
                      text surrounding a flowchart or image page.
    """
    texts, payloads, ids = [], [], []

    # Split this text block into pieces no larger than CHUNK_SIZE.
    # Overlap is CHUNK_OVERLAP characters so sentences cut at a boundary
    # still appear fully in at least one chunk.
    raw_chunks = text_splitter.split_text(text_block)

    for piece in raw_chunks:
        piece = piece.strip()
        if len(piece) < 30:  # Skip fragments that are too short to be meaningful
            continue

        chunk_id  = f"{Path(file_name).stem}_text_{chunk_counter}"
        stable_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f"{file_name}::text::{chunk_counter}"))

        texts.append(piece)
        payloads.append({
            "chunk_id":     chunk_id,
            "source":       file_name,
            "page":         page_num,      # Page this text appeared on
            "section":      section,       # Section heading above this text
            "element_type": element_type,  # "text" or "figure_context"
            "category":     category,
            "char_length":  len(piece),
            "text":         piece,
        })
        ids.append(stable_id)
        chunk_counter += 1

    return texts, payloads, ids


def parse_pdf_smart(file_path: Path) -> Tuple[List[str], List[Dict[str, Any]], List[str]]:
    """
    The main PDF parsing function — uses pdfplumber to extract content
    in a layout-aware way.

    What it does, page by page:
      1. Detect and extract TABLES → convert each row to a text chunk.
      2. Extract TEXT BLOCKS → split into paragraph/sentence chunks.
      3. Track the SECTION HEADING above each block (e.g. "4.1 Leave Policy").
      4. Detect IMAGE-ONLY PAGES (flowcharts) → capture surrounding text as context.

    Every chunk gets rich metadata:
      - source:       filename
      - page:         page number (1-indexed)
      - section:      last heading seen before this chunk
      - element_type: "table", "text", or "figure_context"
      - category:     HR / Finance / Engineering / etc.

    Returns:
        (texts, payloads, ids) — three parallel lists ready for embedding.
    """
    all_texts:    List[str]           = []
    all_payloads: List[Dict[str, Any]] = []
    all_ids:      List[str]           = []

    category      = infer_category(file_path.name)
    chunk_counter = 0                  # Running index for unique chunk IDs
    current_section = "Introduction"   # Default section until we detect a heading

    with pdfplumber.open(str(file_path)) as pdf:
        total_pages = len(pdf.pages)
        print(f"  [PDF Parser] {file_path.name} — {total_pages} pages")

        for page_num, page in enumerate(pdf.pages, start=1):

            # ── STEP 1: Extract tables from this page ───────────────────
            # pdfplumber returns tables as List[List[Optional[str]]].
            # Example: [["Leave Type", "Days"], ["Maternity", "26 weeks"], ...]
            tables_on_page = page.extract_tables() or []

            # Collect the bounding boxes of all tables so we can exclude
            # their area from the plain text extraction below.
            # (Without this, table cell text would appear twice — once as
            #  a table row and again in the raw text dump.)
            table_bboxes = []
            for table_obj in page.find_tables():
                table_bboxes.append(table_obj.bbox)  # (x0, top, x1, bottom)

            # Convert each table into one chunk per data row.
            for table in tables_on_page:
                t_texts, t_payloads, t_ids = _table_to_chunks(
                    table, file_path.name, page_num, current_section, category, chunk_counter
                )
                all_texts    += t_texts
                all_payloads += t_payloads
                all_ids      += t_ids
                chunk_counter += len(t_texts)

            # ── STEP 2: Extract plain text, excluding table areas ────────
            # We crop out table bounding boxes so their text isn't duplicated.
            remaining_page = page
            for bbox in table_bboxes:
                try:
                    # outside_bbox returns the page with that rectangle removed
                    remaining_page = remaining_page.outside_bbox(bbox)
                except Exception:
                    pass  # If crop fails for any reason, just use the full page

            page_text = remaining_page.extract_text() or ""

            # ── STEP 3: Detect section headings in the extracted text ────
            # We scan each line of text. If a line looks like a section
            # heading (numbered or ALL CAPS), we update current_section.
            # All chunks created AFTER this point will carry this section tag.
            text_lines  = page_text.split("\n")
            usable_lines: List[str] = []

            for line in text_lines:
                line_stripped = line.strip()
                if not line_stripped:
                    continue

                if _looks_like_section_heading(line_stripped):
                    # Save this heading for all subsequent chunks
                    current_section = line_stripped
                    # Also include it as a line in the text block so
                    # the chunk knows its own section context.
                usable_lines.append(line_stripped)

            # Rejoin lines into a clean text block for splitting.
            clean_text = "\n".join(usable_lines).strip()

            # ── STEP 4: Handle image-only / flowchart pages ─────────────
            # If a page has no extractable text AND no tables,
            # it's probably an image (flowchart, org chart, photo).
            # We can't read the image, but the surrounding pages usually
            # describe what it shows — so we tag the neighboring text
            # as "figure_context" to signal approximate context.
            if not clean_text and not tables_on_page:
                # Nothing to extract from this page — mark as figure page.
                # The previous page's text (already stored) and the next
                # page's text (stored next iteration) serve as context.
                print(f"    [Page {page_num}] Image/flowchart page — no text extracted. Using surrounding context.")
                # Update section so next page inherits the right heading.
                continue

            if not clean_text:
                continue  # Tables were found but no additional text — that's fine.

            # ── STEP 5: Split text into chunks ──────────────────────────
            # Determine element type: if the page had no tables, it's pure text.
            # We'll use the default "text" type for normal content.
            elem_type = "text"

            p_texts, p_payloads, p_ids = _text_to_chunks(
                clean_text, file_path.name, page_num, current_section, category, elem_type, chunk_counter
            )
            all_texts    += p_texts
            all_payloads += p_payloads
            all_ids      += p_ids
            chunk_counter += len(p_texts)

    return all_texts, all_payloads, all_ids


def parse_markdown_or_text(file_path: Path) -> Tuple[List[str], List[Dict[str, Any]], List[str]]:
    """
    Parses Markdown (.md) and plain text (.txt) files.

    These files have predictable structure — headings start with '#',
    so we split on heading boundaries first, then further split any
    section that's too long using the standard text splitter.
    """
    texts, payloads, ids = [], [], []
    category      = infer_category(file_path.name)
    chunk_counter = 0

    content = file_path.read_text(encoding="utf-8")
    chunks  = text_splitter.split_text(content)

    for piece in chunks:
        piece = piece.strip()
        if len(piece) < 30:
            continue

        chunk_id  = f"{file_path.stem}_{chunk_counter}"
        stable_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f"{file_path.name}::{chunk_counter}"))

        texts.append(piece)
        payloads.append({
            "chunk_id":     chunk_id,
            "source":       file_path.name,
            "page":         None,       # Markdown has no page numbers
            "section":      None,
            "element_type": "text",
            "category":     category,
            "char_length":  len(piece),
            "text":         piece,
        })
        ids.append(stable_id)
        chunk_counter += 1

    return texts, payloads, ids


def infer_category(filename: str) -> str:
    """
    Guesses the document category from the filename.
    This is stored as metadata on every chunk so users can
    filter searches by department (e.g. only HR policies).
    """
    fn = filename.lower()
    if any(k in fn for k in ["sec", "password", "vulnerability", "access", "byod", "incident", "odc", "surveillance"]):
        return "Security & Infrastructure"
    elif any(k in fn for k in ["leave", "parental", "bereavement", "holiday", "posh", "grievance", "whistleblower", "handbook", "onboarding", "dress", "wellness", "eap", "policy", "procedure"]):
        return "People Operations & HR"
    elif any(k in fn for k in ["travel", "expense", "payroll", "salary", "pf", "gratuity", "bonus", "card", "tax", "esop", "lease"]):
        return "Finance & Payroll"
    elif any(k in fn for k in ["sde", "api", "git", "ci_cd", "database", "observability", "testing", "ai", "cloud", "sre"]):
        return "Engineering & Cloud"
    elif any(k in fn for k in ["sales", "commission", "client", "nda", "msa", "procurement", "vendor"]):
        return "Sales & Commercial"
    elif any(k in fn for k in ["facility", "visitor", "lost", "seat", "meeting", "ehs", "emergency"]):
        return "Workplace Solutions"
    return "Corporate Governance"


# ================================================================
# INGESTION PIPELINE
# ================================================================
# This is the main entry point called by `python main.py --ingest`.
# It orchestrates: Parse → Chunk → Embed → Upload to Qdrant.


def ingest_all_documents(docs_dir: str = "docs", recreate: bool = True) -> Dict[str, int]:
    """
    Full ingestion pipeline for all documents in the docs/ folder.

    Steps:
      1. Find all .pdf, .md, and .txt files.
      2. Parse each file using the appropriate parser:
           - PDFs  → parse_pdf_smart()    (pdfplumber, layout-aware)
           - Text/MD → parse_markdown_or_text() (standard splitter)
      3. Collect all chunks with rich metadata.
      4. Generate 384-dimensional embeddings for all chunks in bulk.
      5. Upload everything to Qdrant Cloud in batches of 100.

    Args:
        docs_dir: Folder to scan for documents (default: "docs").
        recreate: If True, deletes and recreates the Qdrant collection
                  (use when re-ingesting from scratch).

    Returns:
        Dict with {"documents": count, "chunks": count}.
    """
    global _bm25_index, _corpus_chunks

    base_path = Path(docs_dir)
    if not base_path.exists():
        raise FileNotFoundError(
            f"Documentation directory '{docs_dir}' not found! "
            f"Create it and add your PDF/Markdown files."
        )

    # Find all supported file types recursively.
    files = sorted(
        list(base_path.rglob("*.pdf"))
        + list(base_path.rglob("*.md"))
        + list(base_path.rglob("*.txt"))
    )

    doc_count = len(files)
    print(f"\n[Ingestion] Found {doc_count} document(s) in '{docs_dir}'.")
    print(f"[Ingestion] Chunking strategy: pdfplumber layout-aware (tables row-by-row, text section-aware)\n")

    # These three lists stay in sync: texts[i], payloads[i], ids[i]
    # all describe the same chunk.
    all_texts:    List[str]            = []
    all_payloads: List[Dict[str, Any]] = []
    all_ids:      List[str]            = []

    for file_path in files:
        print(f"  → Parsing: {file_path.name}")
        try:
            suffix = file_path.suffix.lower()

            if suffix == ".pdf":
                # Smart layout-aware parsing — handles tables, sections, flowcharts
                t, p, i = parse_pdf_smart(file_path)
            elif suffix in [".md", ".txt"]:
                # Simple text splitting for flat documents
                t, p, i = parse_markdown_or_text(file_path)
            else:
                print(f"    [Skip] Unsupported file type: {suffix}")
                continue

            all_texts    += t
            all_payloads += p
            all_ids      += i

            # Count element types for the summary log
            table_chunks = sum(1 for x in p if x.get("element_type") == "table")
            text_chunks  = len(p) - table_chunks
            print(f"    → {len(t)} chunks ({text_chunks} text, {table_chunks} table rows)")

        except Exception as e:
            print(f"    [Parser Error] Could not parse {file_path.name}: {e}")
            continue

    total_chunks = len(all_texts)
    print(f"\n[Ingestion] Total chunks generated: {total_chunks}")

    if total_chunks == 0:
        print("[Ingestion Warning] No chunks to index. Check that your docs/ folder has readable PDFs.")
        return {"documents": doc_count, "chunks": 0}

    # ── Create / recreate the Qdrant collection ──────────────────────────
    ensure_collection(recreate=recreate)

    # ── Generate embeddings for all chunks in one batch ──────────────────
    # encode() handles batching internally (batch_size=64).
    # normalize_embeddings=True ensures cosine similarity works correctly.
    print(f"\n[Embeddings] Encoding {total_chunks} chunks with {EMBEDDING_MODEL_NAME}...")
    embeddings = embedding_model.encode(
        all_texts,
        batch_size=64,
        show_progress_bar=True,
        normalize_embeddings=True
    )

    # ── Build Qdrant point objects ───────────────────────────────────────
    # Each PointStruct = one chunk with its vector + all metadata.
    points = [
        models.PointStruct(
            id=all_ids[i],
            vector=embeddings[i].tolist(),
            payload=all_payloads[i]   # source, page, section, element_type, text, ...
        )
        for i in range(total_chunks)
    ]

    # ── Upload to Qdrant in batches of 100 ──────────────────────────────
    # Uploading in batches avoids hitting request size limits.
    UPLOAD_BATCH_SIZE = 100
    print(f"[Qdrant] Uploading {total_chunks} points in batches of {UPLOAD_BATCH_SIZE}...")
    for i in range(0, total_chunks, UPLOAD_BATCH_SIZE):
        batch = points[i : i + UPLOAD_BATCH_SIZE]
        client.upsert(collection_name=COLLECTION_NAME, points=batch)
        print(f"  Uploaded batch {i // UPLOAD_BATCH_SIZE + 1}/{-(-total_chunks // UPLOAD_BATCH_SIZE)}")

    # ── Invalidate the in-memory BM25 cache ─────────────────────────────
    # BM25 is rebuilt lazily on the next query, using the fresh Qdrant data.
    _bm25_index   = None
    _corpus_chunks = []

    # ── Summary ──────────────────────────────────────────────────────────
    table_total = sum(1 for p in all_payloads if p.get("element_type") == "table")
    text_total  = total_chunks - table_total
    print("\n" + "=" * 65)
    print(">>> INGESTION COMPLETE")
    print(f"  Documents Ingested : {doc_count}")
    print(f"  Total Chunks       : {total_chunks}")
    print(f"    ├─ Text chunks   : {text_total}")
    print(f"    └─ Table rows    : {table_total}")
    print(f"  Qdrant Collection  : {COLLECTION_NAME}")
    print("=" * 65 + "\n")

    return {"documents": doc_count, "chunks": total_chunks}


# ---------------- BM25 KEYWORD SEARCH ENGINE ----------------

def _tokenize(text: str) -> List[str]:
    """Simple alphanumeric tokenizer for BM25."""
    return re.findall(r"\w+", text.lower())


def ensure_bm25_index():
    """Lazily loads all chunks from Qdrant to build the in-memory BM25 index."""
    global _bm25_index, _corpus_chunks
    if _bm25_index is not None and _corpus_chunks:
        return

    if not client.collection_exists(COLLECTION_NAME):
        return

    # Scroll all points from collection
    records, _ = client.scroll(
        collection_name=COLLECTION_NAME,
        limit=5000,
        with_payload=True,
        with_vectors=False
    )

    _corpus_chunks = [record.payload for record in records if record.payload]
    tokenized_corpus = [_tokenize(chunk.get("text", "")) for chunk in _corpus_chunks]
    _bm25_index = BM25Okapi(tokenized_corpus)
    print(f"[BM25] Built in-memory index over {len(_corpus_chunks)} document chunks.")


def search_bm25(query: str, limit: int = 20) -> List[Dict[str, Any]]:
    """Returns top keyword matches using BM25."""
    ensure_bm25_index()
    if not _bm25_index or not _corpus_chunks or not query.strip():
        return []

    tokens = _tokenize(query)
    if not tokens:
        return []

    scores = _bm25_index.get_scores(tokens)
    top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:limit]

    results = []
    for idx in top_indices:
        score = float(scores[idx])
        if score <= 0.0:
            continue
        chunk = _corpus_chunks[idx]
        results.append({
            "text": chunk.get("text", ""),
            "source": chunk.get("source", "Unknown"),
            "category": chunk.get("category", "General"),
            "chunk_id": chunk.get("chunk_id", ""),
            "bm25_score": round(score, 4)
        })
    return results


# ---------------- VECTOR DENSE SEARCH ----------------

def search_dense_vectors(query: str, limit: int = 20) -> List[Dict[str, Any]]:
    """Returns top semantic matches from Qdrant vector space with automatic retry on network blips."""
    global _collection_verified
    if not query.strip():
        return []

    if not _collection_verified:
        try:
            if not client.collection_exists(COLLECTION_NAME):
                return []
            _collection_verified = True
        except Exception as e:
            print(f"[Qdrant Connection Warning]: {e}")

    query_vector = embedding_model.encode(query, normalize_embeddings=True).tolist()
    
    # Retry with exponential backoff on intermittent SSL/connection drops
    response = None
    for attempt in range(1, 4):
        try:
            response = client.query_points(
                collection_name=COLLECTION_NAME,
                query=query_vector,
                limit=limit,
                with_payload=True
            )
            break
        except Exception as e:
            print(f"[Qdrant query_points attempt {attempt} failed]: {e}")
            if attempt < 3:
                import time
                time.sleep(1.5 * attempt)
            else:
                return []

    if not response:
        return []

    matches = []
    for hit in response.points:
        payload = hit.payload or {}
        matches.append({
            "text": payload.get("text", ""),
            "source": payload.get("source", "Unknown"),
            "category": payload.get("category", "General"),
            "chunk_id": payload.get("chunk_id", ""),
            "vector_score": round(hit.score, 4)
        })
    return matches


# ---------------- HYBRID RETRIEVAL + RERANKING (PHASE 2) ----------------

def hybrid_search_and_rerank(
    query: str,
    top_candidates: int = 20,
    top_final: int = 5,
    log_scores: bool = True
) -> List[Dict[str, Any]]:
    """
    Phase 2 Pipeline:
    1. Retrieve top 20 via Qdrant dense vector search.
    2. Retrieve top 20 via BM25 keyword search.
    3. Fuse candidates using Reciprocal Rank Fusion (RRF).
    4. Rerank top 20 candidates down to top 5 with Cross-Encoder (ms-marco-MiniLM-L-6-v2).
    5. Log all retrieval & rerank scores.
    """
    if not query.strip():
        return []

    # 1. Retrieve dense vectors & BM25
    vector_hits = search_dense_vectors(query, limit=top_candidates)
    bm25_hits = search_bm25(query, limit=top_candidates)

    # 2. Merge candidates via Reciprocal Rank Fusion (RRF constant k=60)
    candidate_dict: Dict[str, Dict[str, Any]] = {}
    rrf_scores: Dict[str, float] = {}

    for rank, hit in enumerate(vector_hits):
        cid = hit["chunk_id"]
        candidate_dict[cid] = hit
        rrf_scores[cid] = rrf_scores.get(cid, 0.0) + (1.0 / (60.0 + rank + 1.0))

    for rank, hit in enumerate(bm25_hits):
        cid = hit["chunk_id"]
        if cid not in candidate_dict:
            candidate_dict[cid] = hit
        else:
            candidate_dict[cid]["bm25_score"] = hit.get("bm25_score", 0.0)
        rrf_scores[cid] = rrf_scores.get(cid, 0.0) + (1.0 / (60.0 + rank + 1.0))

    # Sort merged candidate pool by RRF score and take top_candidates (default 20)
    sorted_candidate_ids = sorted(rrf_scores.keys(), key=lambda k: rrf_scores[k], reverse=True)[:top_candidates]
    top_candidates_list = [candidate_dict[cid] for cid in sorted_candidate_ids]

    if not top_candidates_list:
        return []

    # 3. Cross-Encoder Reranking
    pairs = [(query, cand["text"]) for cand in top_candidates_list]
    cross_scores = reranker_model.predict(pairs)

    for i, score in enumerate(cross_scores):
        top_candidates_list[i]["rerank_score"] = round(float(score), 4)
        top_candidates_list[i]["score"] = round(float(score), 4)

    # Sort descending by cross-encoder score and take top_final (default 5)
    final_ranked = sorted(top_candidates_list, key=lambda c: c["rerank_score"], reverse=True)[:top_final]

    # 4. Log retrieval scores
    if log_scores:
        print("\n" + "=" * 75)
        print(f"[Hybrid Retrieval & Reranker] Query: '{query}'")
        print(f"Candidates Fused: {len(top_candidates_list)} | Final Top: {len(final_ranked)}")
        print("-" * 75)
        for rank, doc in enumerate(final_ranked, 1):
            v_score = doc.get("vector_score", 0.0)
            b_score = doc.get("bm25_score", 0.0)
            r_score = doc.get("rerank_score", 0.0)
            src = doc.get("source", "Unknown")
            cid = doc.get("chunk_id", "")
            print(f"#{rank} [Rerank: {r_score:+.4f} | Vector: {v_score:.4f} | BM25: {b_score:.2f}] -> {src} ({cid})")
        print("=" * 75 + "\n")

    return final_ranked


# Backwards compatibility helper for existing agent.py
def search_knowledge_base(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    """Hybrid search with cross-encoder reranking."""
    return hybrid_search_and_rerank(query=query, top_candidates=20, top_final=limit)


def is_ready() -> bool:
    """Readiness probe checking that client and models are initialized."""
    return bool(client is not None and embedding_model is not None and reranker_model is not None)


# ---------------- TESTING ----------------

if __name__ == "__main__":
    test_queries = [
        "How many days of paid maternity leave are female employees entitled to?",
        "What is the daily meal per diem and hotel limit in London?",
        "What are the immediate steps for incident commander during a SEV-1 outage?",
        "What is the maximum laptop budget for software engineers?"
    ]

    print("\nRunning Phase 2 Hybrid Retrieval & Reranking Tests...")
    for q in test_queries:
        hybrid_search_and_rerank(q, top_candidates=20, top_final=3)
