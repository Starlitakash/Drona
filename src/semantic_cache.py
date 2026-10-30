import os
import sys
import json
import time
import threading
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import numpy as np

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from dotenv import load_dotenv

load_dotenv()

# Configuration
DEFAULT_THRESHOLD = float(os.getenv("SEMANTIC_CACHE_THRESHOLD", "0.85"))
DEFAULT_TTL_SECONDS = int(os.getenv("SEMANTIC_CACHE_TTL_SECONDS", "86400"))  # 24 hours default
CACHE_FILE_PATH = Path(__file__).resolve().parent.parent / "data" / "semantic_cache.json"

# Lazy-loaded embedding model reference (shared from retriever to save RAM)
_cached_encoder = None


def _get_encoder():
    """Lazily retrieves the shared embedding model from src.retriever."""
    global _cached_encoder
    if _cached_encoder is None:
        try:
            from src.retriever import embedding_model
            _cached_encoder = embedding_model
        except Exception:
            from sentence_transformers import SentenceTransformer
            _cached_encoder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return _cached_encoder


class SemanticCache:
    """
    High-performance Semantic Cache for enterprise RAG.
    
    Uses dense vector similarity (cosine similarity >= threshold) to detect semantically
    equivalent queries (e.g. 'How many sick leaves?' vs 'What is the sick leave policy?').
    Serves answers instantaneously in ~15ms at $0 token cost, bypassing vector search and LLM calls.
    """

    def __init__(
        self,
        threshold: float = DEFAULT_THRESHOLD,
        default_ttl: int = DEFAULT_TTL_SECONDS,
        persist_path: Optional[Path] = CACHE_FILE_PATH
    ):
        self.threshold = threshold
        self.default_ttl = default_ttl
        self.persist_path = persist_path
        self._lock = threading.Lock()
        
        # In-memory storage: list of entries
        # Each entry: {
        #   "query": str,
        #   "embedding": np.ndarray (normalized, 384-dim),
        #   "answer": str,
        #   "intent": str,
        #   "metadata": dict,
        #   "created_at": float (timestamp),
        #   "ttl": int (seconds),
        #   "hit_count": int
        # }
        self._entries: List[Dict[str, Any]] = []
        
        # Telemetry
        self._hits = 0
        self._misses = 0

        # Load persisted cache if exists
        self._load_from_disk()

    def _load_from_disk(self):
        """Loads previously cached entries from disk if available."""
        if not self.persist_path or not self.persist_path.exists():
            return

        try:
            with open(self.persist_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            now = time.time()
            loaded_entries = []
            for item in data.get("entries", []):
                created_at = item.get("created_at", now)
                ttl = item.get("ttl", self.default_ttl)
                # Check expiration
                if now - created_at < ttl:
                    emb = np.array(item["embedding"], dtype=np.float32)
                    norm = np.linalg.norm(emb)
                    if norm > 0:
                        emb = emb / norm
                    item["embedding"] = emb
                    loaded_entries.append(item)

            self._entries = loaded_entries
            print(f"[Semantic Cache] Restored {len(self._entries)} warm entries from {self.persist_path.name}")
        except Exception as e:
            print(f"[Semantic Cache Warning] Could not load persisted cache: {e}")

    def _save_to_disk(self):
        """Persists current valid cache entries to disk asynchronously or on change."""
        if not self.persist_path:
            return

        try:
            self.persist_path.parent.mkdir(parents=True, exist_ok=True)
            now = time.time()
            serializable_entries = []
            for item in self._entries:
                if now - item["created_at"] < item["ttl"]:
                    serializable_entries.append({
                        "query": item["query"],
                        "embedding": item["embedding"].tolist(),
                        "answer": item["answer"],
                        "intent": item.get("intent", "RAG"),
                        "metadata": item.get("metadata", {}),
                        "created_at": item["created_at"],
                        "ttl": item["ttl"],
                        "hit_count": item.get("hit_count", 0)
                    })

            with open(self.persist_path, "w", encoding="utf-8") as f:
                json.dump({"entries": serializable_entries, "updated_at": now}, f, indent=2)
        except Exception as e:
            print(f"[Semantic Cache Warning] Failed to persist cache to disk: {e}")

    def get(self, query: str, threshold: Optional[float] = None) -> Optional[Dict[str, Any]]:
        """
        Searches the semantic cache for a question with cosine similarity >= threshold.
        Returns the matching entry or None if cache miss.
        """
        threshold = threshold or self.threshold
        clean_q = query.strip()
        if not clean_q or not self._entries:
            with self._lock:
                self._misses += 1
            return None

        # 1. Encode user query (normalized vector)
        encoder = _get_encoder()
        query_emb = encoder.encode(clean_q, normalize_embeddings=True)
        query_vec = np.array(query_emb, dtype=np.float32)

        now = time.time()
        best_score = -1.0
        best_entry = None
        best_idx = -1

        with self._lock:
            # Clean expired items & calculate cosine similarities
            valid_entries = []
            for i, entry in enumerate(self._entries):
                if now - entry["created_at"] >= entry["ttl"]:
                    continue  # Expired
                valid_entries.append(entry)

                # Dot product of normalized vectors == Cosine Similarity
                sim = float(np.dot(query_vec, entry["embedding"]))
                if sim > best_score:
                    best_score = sim
                    best_entry = entry
                    best_idx = i

            self._entries = valid_entries

            if best_entry and best_score >= threshold:
                self._hits += 1
                best_entry["hit_count"] = best_entry.get("hit_count", 0) + 1
                print(
                    f"\n[Semantic Cache HIT] (Similarity: {best_score:.4f} >= {threshold:.2f})\n"
                    f"   Incoming: '{clean_q}'\n"
                    f"   Matched:  '{best_entry['query']}'\n"
                    f"   Saved ~2,500ms and 100% LLM token costs!"
                )
                return {
                    "answer": best_entry["answer"],
                    "intent": best_entry.get("intent", "RAG"),
                    "matched_query": best_entry["query"],
                    "similarity": round(best_score, 4),
                    "created_at": best_entry["created_at"],
                    "metadata": best_entry.get("metadata", {})
                }

            self._misses += 1
            return None

    def set(
        self,
        query: str,
        answer: str,
        intent: str = "RAG",
        metadata: Optional[Dict[str, Any]] = None,
        ttl_seconds: Optional[int] = None
    ):
        """Stores a new (query, answer) pair in the semantic cache."""
        clean_q = query.strip()
        if not clean_q or not answer:
            return

        encoder = _get_encoder()
        query_emb = encoder.encode(clean_q, normalize_embeddings=True)
        query_vec = np.array(query_emb, dtype=np.float32)

        entry = {
            "query": clean_q,
            "embedding": query_vec,
            "answer": answer.strip(),
            "intent": intent,
            "metadata": metadata or {},
            "created_at": time.time(),
            "ttl": ttl_seconds or self.default_ttl,
            "hit_count": 0
        }

        with self._lock:
            # Check if this exact query or a very close variant (>= 0.98) is already cached; if so, update answer
            updated = False
            for existing in self._entries:
                sim = float(np.dot(query_vec, existing["embedding"]))
                if sim >= 0.98:
                    existing["answer"] = answer.strip()
                    existing["created_at"] = time.time()
                    existing["metadata"] = metadata or {}
                    updated = True
                    break

            if not updated:
                self._entries.append(entry)

            self._save_to_disk()

    def clear(self):
        """Clears all entries from in-memory cache and persisted storage."""
        with self._lock:
            self._entries.clear()
            self._hits = 0
            self._misses = 0
            if self.persist_path and self.persist_path.exists():
                try:
                    self.persist_path.unlink()
                except Exception:
                    pass
        print("[Semantic Cache] In-memory and persisted cache cleared.")

    def get_stats(self) -> Dict[str, Any]:
        """Returns performance metrics and hit-rate telemetry."""
        with self._lock:
            total_requests = self._hits + self._misses
            hit_rate = (self._hits / total_requests * 100.0) if total_requests > 0 else 0.0
            now = time.time()
            active_entries = sum(1 for e in self._entries if now - e["created_at"] < e["ttl"])
            
            # Estimate savings: assume ~2.2s latency and ~$0.003 per LLM call saved
            est_latency_saved_sec = round(self._hits * 2.2, 2)
            est_tokens_saved = self._hits * 850  # average ~850 tokens per RAG turn

            return {
                "hits": self._hits,
                "misses": self._misses,
                "total_requests": total_requests,
                "hit_rate_pct": round(hit_rate, 2),
                "active_entries": active_entries,
                "threshold": self.threshold,
                "est_latency_saved_sec": est_latency_saved_sec,
                "est_tokens_saved": est_tokens_saved
            }


# Global singleton instance
semantic_cache = SemanticCache()
