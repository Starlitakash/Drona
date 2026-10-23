
import os
import uuid
from pathlib import Path

from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# ---------------- CONFIGURATION ----------------

STORAGE_PATH = os.getenv("QDRANT_STORAGE_PATH", "./qdrant_data")
COLLECTION_NAME = "enterprise_knowledge"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Local Qdrant database; no Docker required
client = QdrantClient(path=STORAGE_PATH)

# Text chunking configuration
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=100,
    separators=["\n## ", "\n### ", "\n- ", "\n\n", "\n", " "]
)


# ---------------- COLLECTION SETUP ----------------

def ensure_collection():
    """Create the collection if it does not already exist."""

    if client.collection_exists(COLLECTION_NAME):
        return

    vector_size = client.get_embedding_size(EMBEDDING_MODEL)

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE
        )
    )

    print(f"Created collection: {COLLECTION_NAME}")


# ---------------- DOCUMENT INGESTION ----------------

def ingest_all_documents(data_dir: str = "data"):
    """Read Markdown/text files, split them and store them in Qdrant."""

    base_path = Path(data_dir)

    if not base_path.exists():
        print(f"Directory '{data_dir}' not found!")
        return

    files = sorted(
        list(base_path.rglob("*.md"))
        + list(base_path.rglob("*.txt"))
    )

    print(f"Found {len(files)} knowledge files.")

    if not files:
        print("No Markdown or text files to ingest.")
        return

    documents = []
    metadata = []
    point_ids = []

    for file_path in files:
        category = (
            file_path.parent.name
            if file_path.parent != base_path
            else "general"
        )

        try:
            content = file_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            print(f"Could not read {file_path}: {error}")
            continue

        chunks = text_splitter.split_text(content)

        for idx, chunk in enumerate(chunks):
            if not chunk.strip():
                continue

            documents.append(chunk)

            metadata.append({
                "text": chunk,
                "source": file_path.name,
                "category": category,
                "chunk_id": f"{file_path.stem}_{idx}",
                "file_path": file_path.as_posix()
            })

            # Deterministic ID: rerunning ingestion updates
            # existing points instead of duplicating them.
            stable_id = str(
                uuid.uuid5(
                    uuid.NAMESPACE_URL,
                    f"{file_path.resolve()}::{idx}"
                )
            )
            point_ids.append(stable_id)

    if not documents:
        print("No readable document chunks found.")
        return

    ensure_collection()

    print(f"Ingesting {len(documents)} chunks into Qdrant...")

    # The client generates embeddings from the documents
    # using the configured FastEmbed model.
    client.upload_collection(
        collection_name=COLLECTION_NAME,
        vectors=[
            models.Document(
                text=doc,
                model=EMBEDDING_MODEL
            )
            for doc in documents
        ],
        ids=point_ids,
        payload=metadata,
        batch_size=32
    )

    print("Ingestion complete!")


# ---------------- SEMANTIC SEARCH ----------------

def search_knowledge_base(
    query: str,
    limit: int = 3
) -> list[dict]:
    """Return the most relevant document chunks."""

    if not client.collection_exists(COLLECTION_NAME):
        print("Collection does not exist. Ingest documents first.")
        return []

    if not query.strip():
        return []

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=models.Document(
            text=query,
            model=EMBEDDING_MODEL
        ),
        limit=limit,
        with_payload=True
    )

    matched = []

    for hit in response.points:
        payload = hit.payload or {}

        matched.append({
            "text": payload.get("text", ""),
            "source": payload.get("source", "Unknown"),
            "category": payload.get("category", "general"),
            "chunk_id": payload.get("chunk_id"),
            "score": round(hit.score, 4)
        })

    return matched


# ---------------- TESTING ----------------

if __name__ == "__main__":

    try:
        ingest_all_documents()

        test_queries = [
            "What is error PG-ERR-53300 and how to fix it?",
            "How many weeks of parental leave do I get?",
            "What is the maximum hotel allowance in London?"
        ]

        for query in test_queries:
            print("\n" + "=" * 55)
            print(f"QUERY: {query}")
            print("=" * 55)

            hits = search_knowledge_base(query, limit=1)

            if not hits:
                print("No matching documents found.")
                continue

            for hit in hits:
                print(f"Source: {hit['source']}")
                print(f"Category: {hit['category']}")
                print(f"Score: {hit['score']}")
                print(f"Content:\n{hit['text']}")

    finally:
        client.close()
