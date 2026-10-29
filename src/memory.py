import os
import sys
from datetime import datetime
from typing import List, Dict, Any, Optional

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from dotenv import load_dotenv

load_dotenv()

# MongoDB Configuration
MONGODB_URI = os.getenv("MONGODB_URI", "").strip()
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "drona_db")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "chat_history")

_mongo_client = None
_collection = None
_mongo_available = False

# In-memory fallback cache when MONGODB_URI is not set or unavailable
_in_memory_cache: Dict[str, List[Dict[str, Any]]] = {}


def _init_mongodb():
    """Initializes MongoDB client if MONGODB_URI is configured."""
    global _mongo_client, _collection, _mongo_available
    if not MONGODB_URI:
        print("[Memory] MONGODB_URI is not set. Using resilient in-memory session cache.")
        _mongo_available = False
        return

    try:
        from pymongo import MongoClient, ASCENDING
        _mongo_client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=4000)
        # Ping the server to verify connectivity
        _mongo_client.admin.command("ping")
        db = _mongo_client[MONGODB_DB_NAME]
        _collection = db[MONGODB_COLLECTION]
        # Ensure fast index on thread_id
        _collection.create_index([("thread_id", ASCENDING)], unique=True)
        _mongo_available = True
        print(f"[Memory] Successfully connected to MongoDB Database: '{MONGODB_DB_NAME}' -> Collection: '{MONGODB_COLLECTION}'")
    except Exception as e:
        print(f"[Memory Warning] MongoDB connection failed ({e}). Falling back to in-memory session cache.")
        _mongo_available = False


# Initialize on import
_init_mongodb()


def save_message(
    thread_id: str,
    role: str,
    content: str,
    metadata: Optional[Dict[str, Any]] = None
) -> None:
    """
    Saves a message turn (user or assistant) to MongoDB or in-memory fallback.
    
    Args:
        thread_id: Slack thread_ts or conversation ID.
        role: 'user' or 'assistant'.
        content: The message text.
        metadata: Optional dictionary with user_id, channel_id, intent, etc.
    """
    global _collection, _mongo_available

    msg_doc = {
        "role": role,
        "content": content,
        "timestamp": datetime.utcnow().isoformat(),
        "metadata": metadata or {}
    }

    # 1. Try MongoDB
    if _mongo_available and _collection is not None:
        try:
            _collection.update_one(
                {"thread_id": thread_id},
                {
                    "$push": {"messages": msg_doc},
                    "$set": {"updated_at": datetime.utcnow()},
                    "$setOnInsert": {
                        "created_at": datetime.utcnow(),
                        "channel_id": (metadata or {}).get("channel_id"),
                        "user_id": (metadata or {}).get("user_id")
                    }
                },
                upsert=True
            )
            return
        except Exception as e:
            print(f"[Memory Error] Failed to write to MongoDB ({e}). Falling back to memory cache.")

    # 2. In-memory fallback
    if thread_id not in _in_memory_cache:
        _in_memory_cache[thread_id] = []
    _in_memory_cache[thread_id].append(msg_doc)


def get_chat_history(thread_id: str, limit: int = 10) -> List[Dict[str, Any]]:
    """
    Retrieves the most recent message turns for a given thread_id.
    
    Returns:
        List of dicts: [{"role": "user"|"assistant", "content": "...", "timestamp": "..."}]
    """
    global _collection, _mongo_available

    if _mongo_available and _collection is not None:
        try:
            doc = _collection.find_one({"thread_id": thread_id}, {"messages": {"$slice": -limit}})
            if doc and "messages" in doc:
                return doc["messages"]
        except Exception as e:
            print(f"[Memory Error] Failed to read from MongoDB ({e}). Using memory cache.")

    # Fallback to in-memory cache
    history = _in_memory_cache.get(thread_id, [])
    return history[-limit:]


def format_history_for_llm(thread_id: str, max_turns: int = 4) -> str:
    """
    Formats recent conversation turns into a clean dialogue string for LLM prompts.
    
    Example:
        User: What is the clinical credentialing policy?
        Assistant: Clinical staff must verify licenses upon hire and every three years.
    """
    history = get_chat_history(thread_id, limit=max_turns * 2)
    if not history:
        return ""

    lines = []
    for turn in history:
        role_label = "User" if turn.get("role") == "user" else "Assistant"
        content = turn.get("content", "").strip()
        if content:
            # Truncate very long answers in history to keep token usage lean
            if role_label == "Assistant" and len(content) > 400:
                content = content[:397] + "..."
            lines.append(f"{role_label}: {content}")

    return "\n".join(lines)


def is_known_thread(thread_id: str) -> bool:
    """
    Checks if Drona has previously participated in this Slack thread.
    Used by Slack message listener to respond to follow-up questions without re-mentioning.
    """
    global _collection, _mongo_available

    if thread_id in _in_memory_cache and len(_in_memory_cache[thread_id]) > 0:
        return True

    if _mongo_available and _collection is not None:
        try:
            count = _collection.count_documents({"thread_id": thread_id}, limit=1)
            return count > 0
        except Exception:
            pass

    return False


def clear_thread_history(thread_id: str) -> bool:
    """Clears history for a specific thread."""
    global _collection, _mongo_available

    if thread_id in _in_memory_cache:
        del _in_memory_cache[thread_id]

    if _mongo_available and _collection is not None:
        try:
            _collection.delete_one({"thread_id": thread_id})
            return True
        except Exception:
            return False

    return True
