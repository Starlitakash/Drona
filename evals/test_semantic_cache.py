import time
import sys
from pathlib import Path

# Ensure root in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.agent import ask_agent
from src.semantic_cache import semantic_cache


def run_cache_benchmark():
    print("\n" + "=" * 70)
    print("🚀 DRONA SEMANTIC CACHE BENCHMARK TEST")
    print("=" * 70)

    # Clear cache before benchmark
    semantic_cache.clear()

    # Test Question 1: Original Query
    q1 = "How often are employee performance appraisals conducted?"
    print(f"\n[TURN 1 - Cold Cache Miss]")
    print(f"Query: '{q1}'")
    t0 = time.time()
    res1 = ask_agent(q1, thread_id="cache_bench_1")
    t1 = time.time()
    latency_1 = (t1 - t0) * 1000
    print(f"Latency: {latency_1:.1f}ms | Cache Hit: {res1.get('cache_hit')} | Answer Preview: {res1['answer'][:120]}...")

    # Test Question 2: Exact Repeat
    print(f"\n[TURN 2 - Exact Repeat Cache Hit]")
    print(f"Query: '{q1}'")
    t0 = time.time()
    res2 = ask_agent(q1, thread_id="cache_bench_2")
    t1 = time.time()
    latency_2 = (t1 - t0) * 1000
    print(f"Latency: {latency_2:.1f}ms | Cache Hit: {res2.get('cache_hit')}")
    speedup_exact = latency_1 / max(latency_2, 1)
    print(f"⚡ Speedup: {speedup_exact:.1f}x faster! (LLM bypassed completely)")

    # Test Question 3: Paraphrase / Semantic Variant
    q3 = "Can you tell me how often employee appraisals are conducted?"
    print(f"\n[TURN 3 - Semantic Paraphrase Cache Hit]")
    print(f"Query: '{q3}'")
    t0 = time.time()
    res3 = ask_agent(q3, thread_id="cache_bench_3")
    t1 = time.time()
    latency_3 = (t1 - t0) * 1000
    print(f"Latency: {latency_3:.1f}ms | Cache Hit: {res3.get('cache_hit')}")
    speedup_para = latency_1 / max(latency_3, 1)
    print(f"⚡ Speedup: {speedup_para:.1f}x faster! (Cosine similarity match)")

    # Print Cache Stats
    stats = semantic_cache.get_stats()
    print("\n" + "=" * 70)
    print("📊 SEMANTIC CACHE TELEMETRY & SAVINGS")
    print("=" * 70)
    for k, v in stats.items():
        print(f"• {k:<25}: {v}")
    print("=" * 70)

    # Verification assertions
    assert res1.get("cache_hit") is False, "Turn 1 must be a cold cache miss"
    assert res2.get("cache_hit") is True, "Turn 2 must be an exact cache hit"
    assert res3.get("cache_hit") is True, "Turn 3 must be a semantic paraphrase cache hit"
    # Latency includes network round-trip to remote MongoDB Atlas cluster for thread history persistence
    assert latency_2 < 350.0, f"Cache hit latency must be sub-350ms including cloud DB write, got {latency_2:.1f}ms"
    assert latency_3 < 350.0, f"Cache hit latency must be sub-350ms including cloud DB write, got {latency_3:.1f}ms"
    print("\n✅ ALL SEMANTIC CACHE VERIFICATIONS PASSED SUCCESSFULLY!\n")


if __name__ == "__main__":
    run_cache_benchmark()
