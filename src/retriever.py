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
import pypdf

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


# ---------------- DOCUMENT PARSER ----------------

def parse_file(file_path: Path) -> str:
    """Extracts text content from Markdown, Text, or PDF files."""
    suffix = file_path.suffix.lower()
    if suffix in [".md", ".txt"]:
        return file_path.read_text(encoding="utf-8")
    elif suffix == ".pdf":
        reader = pypdf.PdfReader(str(file_path))
        pages_text = [page.extract_text() or "" for page in reader.pages]
        return "\n\n".join(pages_text)
    return ""


def infer_category(filename: str) -> str:
    """Classifies document category based on filename prefixes and naming."""
    fn = filename.lower()
    if any(k in fn for k in ["sec", "password", "vulnerability", "access", "byod", "incident", "odc", "surveillance"]):
        return "Security & Infrastructure"
    elif any(k in fn for k in ["leave", "parental", "bereavement", "holiday", "posh", "grievance", "whistleblower", "handbook", "onboarding", "dress", "wellness", "eap"]):
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


# ---------------- INGESTION PIPELINE (PHASE 1) ----------------

def ingest_all_documents(docs_dir: str = "docs", recreate: bool = True) -> Dict[str, int]:
    """
    Parses all .md, .txt, and .pdf documents from docs_dir, chunks them with
    ~800 chars and 100 overlap, embeds with sentence-transformers/all-MiniLM-L6-v2,
    and uploads points to Qdrant.
    """
    global _bm25_index, _corpus_chunks
    base_path = Path(docs_dir)
    if not base_path.exists():
        raise FileNotFoundError(f"Documentation directory '{docs_dir}' not found!")

    files = sorted(
        list(base_path.rglob("*.md"))
        + list(base_path.rglob("*.txt"))
        + list(base_path.rglob("*.pdf"))
    )

    doc_count = len(files)
    print(f"\n[Ingestion] Found {doc_count} documents in '{docs_dir}' for parsing.")

    all_chunks: List[str] = []
    all_payloads: List[Dict[str, Any]] = []
    all_ids: List[str] = []

    for file_path in files:
        try:
            content = parse_file(file_path)
        except Exception as e:
            print(f"[Parser Error] Could not parse {file_path.name}: {e}")
            continue

        if not content.strip():
            continue

        category = infer_category(file_path.name)
        chunks = text_splitter.split_text(content)

        for idx, chunk in enumerate(chunks):
            chunk_clean = chunk.strip()
            if not chunk_clean:
                continue

            all_chunks.append(chunk_clean)
            chunk_id = f"{file_path.stem}_{idx}"
            stable_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f"{file_path.name}::{idx}"))
            all_ids.append(stable_id)       

            all_payloads.append({
                "chunk_id": chunk_id,
                "source": file_path.name,
                "category": category,
                "char_length": len(chunk_clean),
                "text": chunk_clean,
                "file_path": file_path.as_posix()
            })

    total_chunks = len(all_chunks)
    print(f"[Ingestion] Generated {total_chunks} chunks from {doc_count} documents (~800 chars, 100 overlap).")

    if total_chunks == 0:
        print("[Ingestion Warning] No chunks to index.")
        return {"documents": doc_count, "chunks": 0}

    ensure_collection(recreate=recreate)

    print(f"[Embeddings] Generating {total_chunks} dense embeddings via {EMBEDDING_MODEL_NAME}...")
    embeddings = embedding_model.encode(
        all_chunks,
        batch_size=64,
        show_progress_bar=True,
        normalize_embeddings=True
    )

    points = [
        models.PointStruct(
            id=all_ids[i],
            vector=embeddings[i].tolist(),
            payload=all_payloads[i]
        )
        for i in range(total_chunks)
    ]

    batch_size = 100
    print(f"[Qdrant] Uploading {total_chunks} points in batches of {batch_size}...")
    for i in range(0, total_chunks, batch_size):
        batch = points[i:i + batch_size]
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=batch
        )

    # Invalidate BM25 cache so it reloads fresh points
    _bm25_index = None
    _corpus_chunks = []

    print("\n" + "=" * 65)
    print(">>> INGESTION COMPLETE")
    print(f"Total Documents Ingested: {doc_count}")
    print(f"Total Chunks Stored:      {total_chunks}")
    print(f"Target Collection:        {COLLECTION_NAME}")
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
