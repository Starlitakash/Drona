import os
import sys
import uuid
from pathlib import Path
from typing import List, Dict, Any, Optional

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import pypdf

load_dotenv()

# ---------------- CONFIGURATION ----------------

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
STORAGE_PATH = os.getenv("QDRANT_STORAGE_PATH", "./qdrant_data")
COLLECTION_NAME = "enterprise_knowledge"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
VECTOR_DIM = 384


def get_qdrant_client() -> QdrantClient:
    """Connects to Qdrant Cloud if credentials exist, otherwise falls back to local storage."""
    if QDRANT_URL:
        print(f"[Qdrant] Connecting to Qdrant Cloud: {QDRANT_URL}")
        return QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
    print(f"[Qdrant] Using local storage path: {STORAGE_PATH}")
    return QdrantClient(path=STORAGE_PATH)


client = get_qdrant_client()

# Text chunking configuration (~800 characters with 100 character overlap)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100,
    separators=["\n## ", "\n### ", "\n\n", "\n", " "]
)

# Initialize SentenceTransformer locally
print(f"[Embeddings] Loading local model: {EMBEDDING_MODEL_NAME}...")
embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)


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
    base_path = Path(docs_dir)
    if not base_path.exists():
        raise FileNotFoundError(f"Documentation directory '{docs_dir}' not found!")

    # Discover all supported documents
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
            
            # Deterministic UUIDv5 for deduplication and idempotent updates
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

    # Ensure collection exists
    ensure_collection(recreate=recreate)

    # Compute dense embeddings locally using sentence-transformers
    print(f"[Embeddings] Generating {total_chunks} dense embeddings via {EMBEDDING_MODEL_NAME}...")
    embeddings = embedding_model.encode(
        all_chunks,
        batch_size=64,
        show_progress_bar=True,
        normalize_embeddings=True
    )

    # Construct Qdrant points
    points = [
        models.PointStruct(
            id=all_ids[i],
            vector=embeddings[i].tolist(),
            payload=all_payloads[i]
        )
        for i in range(total_chunks)
    ]

    # Upload to Qdrant in batches
    batch_size = 100
    print(f"[Qdrant] Uploading {total_chunks} points in batches of {batch_size}...")
    for i in range(0, total_chunks, batch_size):
        batch = points[i:i + batch_size]
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=batch
        )

    print("\n" + "=" * 65)
    print(">>> INGESTION COMPLETE")
    print(f"Total Documents Ingested: {doc_count}")
    print(f"Total Chunks Stored:      {total_chunks}")
    print(f"Target Collection:        {COLLECTION_NAME}")
    print("=" * 65 + "\n")

    return {"documents": doc_count, "chunks": total_chunks}


# ---------------- VECTOR SEARCH HELPER ----------------

def search_knowledge_base(query: str, limit: int = 3) -> List[Dict[str, Any]]:
    """Returns top semantic matches from Qdrant."""
    if not client.collection_exists(COLLECTION_NAME) or not query.strip():
        return []

    query_vector = embedding_model.encode(query, normalize_embeddings=True).tolist()
    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=limit,
        with_payload=True
    )

    matches = []
    for hit in response.points:
        payload = hit.payload or {}
        matches.append({
            "text": payload.get("text", ""),
            "source": payload.get("source", "Unknown"),
            "category": payload.get("category", "General"),
            "chunk_id": payload.get("chunk_id", ""),
            "score": round(hit.score, 4)
        })
    return matches


if __name__ == "__main__":
    ingest_all_documents(docs_dir="docs", recreate=True)
