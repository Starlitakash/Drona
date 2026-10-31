import os
import sys
import json
import time
import random
from pathlib import Path
from typing import List, Dict, Any
import numpy as np

# Ensure root in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from src.agent import ask_agent
from src.semantic_cache import semantic_cache


# ---------------------------------------------------------------------------
# 1. 20 Enterprise Policy Topics with Natural Semantic Paraphrases
# ---------------------------------------------------------------------------
ENTERPRISE_TOPICS = [
    {
        "id": "T01",
        "rank": 1,
        "name": "Personnel File Checklist Frequency",
        "queries": [
            "How often must the Employee Personnel File Checklist be updated?",
            "How frequently is the personnel file checklist reviewed?",
            "What is the required update frequency for personnel files?",
            "Personnel file checklist update requirement annually?"
        ]
    },
    {
        "id": "T02",
        "rank": 2,
        "name": "At-Will Employment Nature",
        "queries": [
            "What type of employment relationship does TriageLogic establish with employees?",
            "Is employment at TriageLogic at-will or under contract?",
            "Can you explain the at-will employment policy?",
            "Does the policy manual create an employment contract?"
        ]
    },
    {
        "id": "T03",
        "rank": 3,
        "name": "Performance Appraisals Frequency",
        "queries": [
            "How often are employee performance appraisals conducted?",
            "What is the schedule for annual performance evaluations?",
            "When do employee reviews happen at the company?",
            "Frequency of performance evaluations for staff"
        ]
    },
    {
        "id": "T04",
        "rank": 4,
        "name": "Mandatory Personnel Documents",
        "queries": [
            "What mandatory documents must be maintained in each employee personnel file?",
            "Which documents are required in the staff personnel folder?",
            "Mandatory paperwork needed for employee personnel file",
            "What forms must be kept in the personnel file according to Core 25?"
        ]
    },
    {
        "id": "T05",
        "rank": 5,
        "name": "Telecommute Eligibility",
        "queries": [
            "What positions are eligible for telecommuting or remote work?",
            "Who is allowed to work remotely from home?",
            "Telecommute eligibility criteria for employees"
        ]
    },
    {
        "id": "T06",
        "rank": 6,
        "name": "Background Checks Requirements",
        "queries": [
            "What background checks are required for newly hired employees?",
            "Are criminal background checks mandatory before hiring?",
            "What pre-employment screening is conducted on candidates?"
        ]
    },
    {
        "id": "T07",
        "rank": 7,
        "name": "HIPAA and Confidentiality Statement",
        "queries": [
            "Is signing a HIPAA compliance policy mandatory for all staff?",
            "What confidentiality agreements must employees sign?",
            "HIPAA compliance training and signed statement requirement"
        ]
    },
    {
        "id": "T08",
        "rank": 8,
        "name": "Overtime and Hours Tracking",
        "queries": [
            "How must non-exempt employees track and record their working hours?",
            "What is the overtime approval policy for hourly staff?",
            "Time card submission and overtime rules for non-exempt workers"
        ]
    },
    {
        "id": "T09",
        "rank": 9,
        "name": "Paid Time Off Accrual",
        "queries": [
            "How is paid time off accrued and requested by employees?",
            "What is the procedure for requesting PTO in advance?",
            "Vacation and PTO accrual schedule for full-time staff"
        ]
    },
    {
        "id": "T10",
        "rank": 10,
        "name": "Equal Employment Opportunity Policy",
        "queries": [
            "What is the company policy on Equal Employment Opportunity and non-discrimination?",
            "Does the company have a formal anti-discrimination policy in hiring?",
            "EEO guidelines and non-harassment commitment"
        ]
    },
    {
        "id": "T11",
        "rank": 11,
        "name": "Termination and Notice Period",
        "queries": [
            "What is the notice period required for voluntary resignation?",
            "How does voluntary termination and resignation procedure work?"
        ]
    },
    {
        "id": "T12",
        "rank": 12,
        "name": "Nurse Licensure Verification",
        "queries": [
            "How often is nursing licensure verified for clinical triage staff?",
            "Verification requirement for professional licenses of clinical staff"
        ]
    },
    {
        "id": "T13",
        "rank": 13,
        "name": "Orientation and Training Period",
        "queries": [
            "What training must new employees complete during orientation?",
            "Mandatory URAC and regulatory training upon hire"
        ]
    },
    {
        "id": "T14",
        "rank": 14,
        "name": "Drug and Alcohol Policy",
        "queries": [
            "What is the substance abuse and drug-free workplace policy?",
            "Are drugs or alcohol prohibited on company premises?"
        ]
    },
    {
        "id": "T15",
        "rank": 15,
        "name": "Equipment and Laptop Security",
        "queries": [
            "What security measures are required for company laptops and remote devices?",
            "Company-provided equipment maintenance and return policy upon exit"
        ]
    },
    {
        "id": "T16",
        "rank": 16,
        "name": "Disciplinary Procedures",
        "queries": [
            "What progressive discipline steps does management follow for policy violations?"
        ]
    },
    {
        "id": "T17",
        "rank": 17,
        "name": "Expense Reimbursement",
        "queries": [
            "What business expenses are eligible for reimbursement and what documentation is required?"
        ]
    },
    {
        "id": "T18",
        "rank": 18,
        "name": "Grievance and Dispute Resolution",
        "queries": [
            "How can an employee file a grievance regarding workplace conflict?"
        ]
    },
    {
        "id": "T19",
        "rank": 19,
        "name": "Dress Code and Professional Conduct",
        "queries": [
            "What is the dress code for client meetings and virtual calls?"
        ]
    },
    {
        "id": "T20",
        "rank": 20,
        "name": "Whistleblower Protection",
        "queries": [
            "How does the company protect employees who report regulatory or ethical violations?"
        ]
    }
]


# ---------------------------------------------------------------------------
# 2. Generate 100 Queries Following Zipf's Law (s = 1.15)
# ---------------------------------------------------------------------------
def generate_zipfian_workload(num_requests: int = 100, s: float = 1.15) -> List[Dict[str, Any]]:
    """
    Computes exact probabilities using Zipf's Law: P(k) = (1 / k^s) / sum(1 / i^s)
    and samples queries accordingly across the 20 topics.
    """
    num_topics = len(ENTERPRISE_TOPICS)
    ranks = np.arange(1, num_topics + 1)
    weights = 1.0 / (ranks ** s)
    probabilities = weights / weights.sum()

    np.random.seed(42)  # Deterministic repeatability
    random.seed(42)

    workload = []
    sampled_indices = np.random.choice(num_topics, size=num_requests, p=probabilities)

    for i, idx in enumerate(sampled_indices):
        topic = ENTERPRISE_TOPICS[idx]
        # Pick one paraphrase for this topic
        query_text = random.choice(topic["queries"])
        workload.append({
            "request_id": i + 1,
            "topic_id": topic["id"],
            "topic_name": topic["name"],
            "rank": topic["rank"],
            "query": query_text
        })

    return workload


# ---------------------------------------------------------------------------
# 3. Main Load Simulation Engine
# ---------------------------------------------------------------------------
def run_simulation(num_requests: int = 100, clear_cache_first: bool = True):
    print("=" * 80)
    print(f"  DRONA ENTERPRISE LOAD BENCHMARK (100 REAL REQUESTS)")
    print(f"  Traffic Model: Zipfian Power-Law (Pareto 80/20 Distribution)")
    print("=" * 80)

    if clear_cache_first:
        print("\n[Setup] Clearing Semantic Cache to start from cold baseline...")
        semantic_cache.clear()
        print("  Cache emptied.")

    workload = generate_zipfian_workload(num_requests=num_requests)
    
    # Print Zipfian distribution preview
    from collections import Counter
    topic_counts = Counter(item["topic_name"] for item in workload)
    print("\n[Traffic Distribution Preview - Top 5 Topics by Frequency]")
    for name, count in topic_counts.most_common(5):
        pct = (count / num_requests) * 100
        bar = "█" * int(pct // 2)
        print(f"  {count:2d} reqs ({pct:4.1f}%) | {bar:<15} | {name}")
    print(f"  ... plus {len(topic_counts) - 5} other topics in the long tail.")
    print("-" * 80)

    results = []
    print(f"\n[Execution] Firing {num_requests} requests through Drona agent pipeline...\n")

    for item in workload:
        req_id = item["request_id"]
        query = item["query"]
        t_name = item["topic_name"]
        
        # Unique session per user simulation
        session_id = f"load_test_req_{req_id}"

        t_start = time.perf_counter()
        response = ask_agent(query, thread_id=session_id)
        t_end = time.perf_counter()

        latency_ms = (t_end - t_start) * 1000.0
        cache_hit = bool(response.get("cache_hit", False))

        record = {
            "request_id": req_id,
            "query": query,
            "topic_name": t_name,
            "latency_ms": round(latency_ms, 2),
            "cache_hit": cache_hit,
            "answer_length": len(response.get("answer", ""))
        }
        results.append(record)

        tag = "⚡ CACHE HIT " if cache_hit else "❄️ COLD MISS "
        print(f"[{req_id:03d}/{num_requests}] [{tag}] {latency_ms:7.1f}ms | {t_name[:32]:<32} | '{query[:45]}...'")

        # Pace cold LLM calls slightly to keep Groq API RPM/TPM well within limits
        if not cache_hit:
            time.sleep(1.2)

    # ---------------------------------------------------------------------------
    # 4. Compute Statistical Percentiles
    # ---------------------------------------------------------------------------
    latencies = [r["latency_ms"] for r in results]
    cache_hits = [r for r in results if r["cache_hit"]]
    cold_misses = [r for r in results if not r["cache_hit"]]

    hit_count = len(cache_hits)
    miss_count = len(cold_misses)
    hit_rate_pct = (hit_count / num_requests) * 100.0

    p50 = float(np.percentile(latencies, 50))
    p90 = float(np.percentile(latencies, 90))
    p95 = float(np.percentile(latencies, 95))
    p99 = float(np.percentile(latencies, 99))
    avg_latency = float(np.mean(latencies))
    min_latency = float(np.min(latencies))
    max_latency = float(np.max(latencies))

    cache_latencies = [r["latency_ms"] for r in cache_hits] if cache_hits else [0]
    cold_latencies = [r["latency_ms"] for r in cold_misses] if cold_misses else [0]

    cache_p50 = float(np.percentile(cache_latencies, 50)) if cache_hits else 0.0
    cold_p50 = float(np.percentile(cold_latencies, 50)) if cold_misses else 0.0

    speedup = cold_p50 / max(cache_p50, 1.0) if cache_hits else 1.0

    # Token & cost estimates
    baseline_tokens = num_requests * 850
    actual_tokens = miss_count * 850
    token_savings_pct = ((baseline_tokens - actual_tokens) / baseline_tokens) * 100.0

    # ---------------------------------------------------------------------------
    # 5. Output Results Table
    # ---------------------------------------------------------------------------
    print("\n" + "=" * 80)
    print("  🏆 FINAL 100-REQUEST BENCHMARK RESULTS")
    print("=" * 80)
    print(f"  • Total Requests Processed : {num_requests}")
    print(f"  • Semantic Cache Hits      : {hit_count} ({hit_rate_pct:.1f}%)")
    print(f"  • Cold RAG Executions      : {miss_count} ({100 - hit_rate_pct:.1f}%)")
    print(f"  • Speedup on Cache Hits    : {speedup:.1f}x faster")
    print("-" * 80)
    print("  LATENCY PERCENTILES (Overall System):")
    print(f"  • Min Latency              : {min_latency:7.1f} ms")
    print(f"  • p50 (Median) Latency     : {p50:7.1f} ms  (Typical user experience)")
    print(f"  • p90 Latency              : {p90:7.1f} ms  (Slow requests)")
    print(f"  • p95 Latency              : {p95:7.1f} ms")
    print(f"  • p99 Latency              : {p99:7.1f} ms  (Worst-case tail)")
    print(f"  • Max Latency              : {max_latency:7.1f} ms")
    print(f"  • Mean Latency             : {avg_latency:7.1f} ms")
    print("-" * 80)
    print("  PATH-SPECIFIC LATENCY BREAKDOWN:")
    print(f"  • Semantic Cache Path p50  : {cache_p50:7.1f} ms  (In-memory dot-product + save)")
    print(f"  • Cold RAG Path p50        : {cold_p50:7.1f} ms  (Qdrant + Cross-Encoder + Groq)")
    print("-" * 80)
    print("  TOKEN CONSUMPTION & COST IMPACT:")
    print(f"  • Tokens without Cache     : ~{baseline_tokens:,} tokens")
    print(f"  • Tokens with Drona Cache  : ~{actual_tokens:,} tokens")
    print(f"  • Total Tokens Saved       : ~{baseline_tokens - actual_tokens:,} tokens ({token_savings_pct:.1f}% savings)")
    print(f"  • Est. Cost without Cache  : ${baseline_tokens * 0.000001:0.4f}")
    print(f"  • Est. Cost with Cache     : ${actual_tokens * 0.000001:0.4f}")
    print("=" * 80)

    # Save to JSON
    output_file = PROJECT_ROOT / "evals" / "load_test_results.json"
    summary_data = {
        "benchmark_timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_requests": num_requests,
        "distribution": "Zipfian (s=1.15)",
        "hit_count": hit_count,
        "miss_count": miss_count,
        "hit_rate_pct": round(hit_rate_pct, 2),
        "percentiles": {
            "min_ms": round(min_latency, 2),
            "p50_ms": round(p50, 2),
            "p90_ms": round(p90, 2),
            "p95_ms": round(p95, 2),
            "p99_ms": round(p99, 2),
            "max_ms": round(max_latency, 2),
            "mean_ms": round(avg_latency, 2)
        },
        "breakdown": {
            "cache_hit_p50_ms": round(cache_p50, 2),
            "cold_rag_p50_ms": round(cold_p50, 2),
            "cache_speedup": round(speedup, 2)
        },
        "tokens": {
            "baseline": baseline_tokens,
            "actual": actual_tokens,
            "savings_pct": round(token_savings_pct, 2)
        },
        "individual_runs": results
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2)

    print(f"\n[Saved] Detailed raw benchmark data written to {output_file.relative_to(PROJECT_ROOT)}\n")
    return summary_data


if __name__ == "__main__":
    run_simulation(num_requests=100)

