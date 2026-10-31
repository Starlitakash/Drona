import os
import sys
import time
from pathlib import Path

# Ensure root in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from src.agent import ask_agent, decompose_multi_hop_query


def test_multi_hop_pipeline():
    print("\n" + "=" * 80)
    print("🚀 TESTING MULTI-HOP QUERY DECOMPOSITION & RAG RETRIEVAL")
    print("=" * 80)

    # 1. Test Query Decomposition directly
    compound_query = (
        "What type of employment relationship does TriageLogic establish with employees, "
        "and how often must the employee personnel file checklist be updated?"
    )

    print(f"\n[TEST 1: Query Decomposition Unit Test]")
    print(f"Original Compound Query: '{compound_query}'")
    is_multi, sub_queries = decompose_multi_hop_query(compound_query)
    print(f"  -> Is Multi-Hop Detected : {is_multi}")
    print(f"  -> Decomposed Sub-Queries:")
    for i, sq in enumerate(sub_queries):
        print(f"     Hop {i+1}: {sq}")

    assert is_multi is True, "Expected query to be detected as multi-hop"
    assert len(sub_queries) >= 2, "Expected at least 2 sub-queries"

    # 2. Test Full Agent Execution
    print(f"\n[TEST 2: End-to-End Agent Execution on Compound Query]")
    t0 = time.time()
    result = ask_agent(compound_query, thread_id="test_multi_hop_session")
    t1 = time.time()

    answer = result.get("answer", "")
    print(f"\nElapsed Time: {(t1 - t0) * 1000:.1f}ms")
    print("\n" + "-" * 50 + " SYNTHESIZED ANSWER " + "-" * 50)
    print(answer)
    print("-" * 120)

    # 3. Assertions
    # Must mention at-will (from Hop 1)
    assert "at-will" in answer.lower(), "Answer should address at-will employment relationship"
    # Must mention annually / update (from Hop 2)
    assert any(w in answer.lower() for w in ["annual", "annually", "year", "checklist", "update"]), "Answer should address checklist update frequency"
    # Zero asterisks rule
    assert "*" not in answer, "Answer must not contain any asterisks"

    print("\n✅ Multi-hop query decomposition, parallel retrieval, and synthesis ALL PASSED!\n")


if __name__ == "__main__":
    test_multi_hop_pipeline()

