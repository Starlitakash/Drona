import os
import sys
import json
import time
from pathlib import Path
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

load_dotenv(PROJECT_ROOT / ".env")

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from src.retriever import hybrid_search_and_rerank
from src.agent import ask_agent

GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
judge_llm = ChatGroq(
    model=GROQ_MODEL,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.0
)

LLM_JUDGE_PROMPT = """You are an expert, impartial evaluation judge assessing an enterprise AI assistant ('Drona') for NexaTech Solutions.
Evaluate the Candidate Answer against the Ground Truth Answer and the User Question.

Question: {question}
Question Type: {question_type}
Ground Truth Reference: {ground_truth}
Candidate Answer to Evaluate: {candidate_answer}

Evaluation Criteria:
1. For 'single_doc' and 'multi_doc' questions:
   - Does the candidate answer provide the key facts, specific figures (INR amounts, days, percentages, ratios), and policy conditions required by the ground truth?
   - Score 1.0 if fully accurate and comprehensive.
   - Score 0.5 if partially accurate or minor detail missing.
   - Score 0.0 if factually wrong, contradicts ground truth, or hallucinates.

2. For 'unanswerable' questions (topics not covered in company records, e.g., pet insurance, space flights, crypto payroll):
   - The candidate answer MUST correctly decline or state that the information is not available in company records.
   - Score 1.0 if it properly declines to answer and avoids hallucinating.
   - Score 0.0 if it makes up fake policy terms or claims company coverage exists.

Output ONLY a valid JSON object with:
{{
  "score": 1.0 or 0.5 or 0.0,
  "reason": "1-sentence concise reason for the assigned score"
}}"""


def evaluate_llm_judge(
    question: str,
    ground_truth: str,
    candidate_answer: str,
    question_type: str,
    expected_keywords: List[str]
) -> Dict[str, Any]:
    """Evaluates answer correctness using LLM-as-a-judge with keyword matching fallback."""
    # Try LLM judging
    try:
        prompt = LLM_JUDGE_PROMPT.format(
            question=question,
            question_type=question_type,
            ground_truth=ground_truth,
            candidate_answer=candidate_answer
        )
        response = judge_llm.invoke([
            SystemMessage(content="You are a strict, objective AI evaluation judge. Output valid JSON only."),
            HumanMessage(content=prompt)
        ])
        content = response.content.strip()
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        parsed = json.loads(content)
        return {
            "score": float(parsed.get("score", 0.0)),
            "reason": parsed.get("reason", "Evaluated by LLM Judge"),
            "method": "llm_judge"
        }
    except Exception as e:
        # Fallback to keyword matching
        print(f"[Judge Fallback due to: {e}] Using keyword matching fallback.")
        cand_lower = candidate_answer.lower()
        
        if question_type == "unanswerable":
            # For unanswerable, check for declining phrases
            decline_phrases = ["don't have", "do not have", "not found", "no information", "company records", "not covered"]
            is_declined = any(phrase in cand_lower for phrase in decline_phrases)
            score = 1.0 if is_declined else 0.0
            return {
                "score": score,
                "reason": "Keyword fallback: checked for non-hallucination declining statement",
                "method": "keyword_fallback"
            }
        
        if not expected_keywords:
            return {"score": 1.0, "reason": "No keywords defined", "method": "keyword_fallback"}

        matches = sum(1 for kw in expected_keywords if kw.lower() in cand_lower)
        fraction = matches / len(expected_keywords)
        score = 1.0 if fraction >= 0.70 else (0.5 if fraction >= 0.40 else 0.0)
        return {
            "score": score,
            "reason": f"Keyword fallback: matched {matches}/{len(expected_keywords)} keywords ({fraction:.1%})",
            "method": "keyword_fallback"
        }


def run_evaluation(dataset_path: Optional[Path] = None, max_samples: Optional[int] = None) -> Dict[str, Any]:
    """Runs full evaluation over the golden dataset and computes Hit Rate, MRR, and Correctness."""
    if dataset_path is None:
        dataset_path = PROJECT_ROOT / "evals" / "golden_dataset.json"

    with open(dataset_path, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    if max_samples:
        dataset = dataset[:max_samples]

    output_path = PROJECT_ROOT / "evals" / "eval_results.json"
    existing_results = {}
    if output_path.exists():
        try:
            with open(output_path, "r", encoding="utf-8") as f:
                old_data = json.load(f)
                for r in old_data.get("results", []):
                    existing_results[r["id"]] = r
        except Exception:
            pass

    print("\n" + "=" * 80)
    print(f"STARTING DRONA EVALUATION HARNESS ({len(dataset)} Golden Test Cases)")
    if existing_results:
        print(f"[Resume Enabled] Found {len(existing_results)} previously completed evaluation items.")
    print("=" * 80 + "\n")

    eval_results = []
    category_stats: Dict[str, Dict[str, Any]] = {}

    for idx, item in enumerate(dataset, 1):
        q_id = item["id"]
        cat = item["category"]
        q_type = item["question_type"]
        question = item["question"]
        ground_truth = item["ground_truth_answer"]
        expected_sources = item.get("expected_sources", [])
        expected_keywords = item.get("expected_keywords", [])

        if cat not in category_stats:
            category_stats[cat] = {
                "total": 0,
                "answerable_total": 0,
                "hits": 0,
                "rr_sum": 0.0,
                "correctness_sum": 0.0
            }

        category_stats[cat]["total"] += 1

        # Check if already evaluated in previous run
        if q_id in existing_results:
            cached = existing_results[q_id]
            print(f"[{idx}/{len(dataset)}] [CACHED] [{cat}] ({q_type}) {question[:65]}...")
            if q_type != "unanswerable" and expected_sources:
                category_stats[cat]["answerable_total"] += 1
                if cached.get("hit") == 1:
                    category_stats[cat]["hits"] += 1
                category_stats[cat]["rr_sum"] += (cached.get("mrr") or 0.0)
            category_stats[cat]["correctness_sum"] += (cached.get("correctness_score") or 0.0)
            eval_results.append(cached)
            continue

        print(f"[{idx}/{len(dataset)}] [{cat}] ({q_type}) {question[:75]}...")

        # 1. Retrieval Evaluation
        retrieved_docs = hybrid_search_and_rerank(question, top_final=5, log_scores=False)
        retrieved_sources = [d.get("source", "") for d in retrieved_docs]

        hit = None
        rr = None

        if q_type != "unanswerable" and expected_sources:
            category_stats[cat]["answerable_total"] += 1
            # Check if at least one expected source is in top-5
            is_hit = any(src in retrieved_sources for src in expected_sources)
            hit = 1 if is_hit else 0
            if is_hit:
                category_stats[cat]["hits"] += 1

            # Compute Reciprocal Rank (1 / rank of first matching doc)
            matching_ranks = [r + 1 for r, src in enumerate(retrieved_sources) if src in expected_sources]
            if matching_ranks:
                rr = 1.0 / min(matching_ranks)
                category_stats[cat]["rr_sum"] += rr
            else:
                rr = 0.0

        # 2. Generation & Answer Correctness Evaluation
        agent_res = ask_agent(question, thread_id=f"eval_thread_{q_id}")
        candidate_answer = agent_res.get("answer", "")

        judge_res = evaluate_llm_judge(
            question=question,
            ground_truth=ground_truth,
            candidate_answer=candidate_answer,
            question_type=q_type,
            expected_keywords=expected_keywords
        )
        correctness_score = judge_res["score"]
        category_stats[cat]["correctness_sum"] += correctness_score

        eval_results.append({
            "id": q_id,
            "category": cat,
            "question_type": q_type,
            "question": question,
            "ground_truth": ground_truth,
            "retrieved_sources": retrieved_sources,
            "expected_sources": expected_sources,
            "hit": hit,
            "mrr": rr,
            "candidate_answer": candidate_answer,
            "correctness_score": correctness_score,
            "judge_reason": judge_res["reason"],
            "judge_method": judge_res["method"]
        })

        # Progressively save checkpoint to disk
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump({"results": eval_results}, f, indent=2)
        except Exception:
            pass

        # Avoid aggressive LLM rate limits
        time.sleep(0.5)

    # Compute Summary Table
    total_samples = len(dataset)
    total_answerable = sum(s["answerable_total"] for s in category_stats.values())
    total_hits = sum(s["hits"] for s in category_stats.values())
    total_rr = sum(s["rr_sum"] for s in category_stats.values())
    total_correctness = sum(s["correctness_sum"] for s in category_stats.values())

    overall_hit_rate = (total_hits / total_answerable) if total_answerable > 0 else 0.0
    overall_mrr = (total_rr / total_answerable) if total_answerable > 0 else 0.0
    overall_correctness = (total_correctness / total_samples) if total_samples > 0 else 0.0

    print("\n" + "=" * 92)
    print(f"{'CATEGORY':<28} {'COUNT':<7} {'HIT RATE @ 5':<16} {'MRR @ 5':<12} {'CORRECTNESS':<14}")
    print("-" * 92)

    category_breakdown = {}
    for cat, s in category_stats.items():
        ans_total = s["answerable_total"]
        c_hit_rate = (s["hits"] / ans_total * 100) if ans_total > 0 else "N/A"
        c_mrr = (s["rr_sum"] / ans_total) if ans_total > 0 else "N/A"
        c_correctness = (s["correctness_sum"] / s["total"] * 100) if s["total"] > 0 else 0.0

        hit_str = f"{c_hit_rate:.1f}%" if isinstance(c_hit_rate, float) else "N/A"
        mrr_str = f"{c_mrr:.4f}" if isinstance(c_mrr, float) else "N/A"
        cor_str = f"{c_correctness:.1f}%"

        print(f"{cat:<28} {s['total']:<7} {hit_str:<16} {mrr_str:<12} {cor_str:<14}")
        category_breakdown[cat] = {
            "total": s["total"],
            "hit_rate": c_hit_rate,
            "mrr": c_mrr,
            "correctness": round(c_correctness, 2)
        }

    print("-" * 92)
    print(f"{'OVERALL SUMMARY':<28} {total_samples:<7} {overall_hit_rate * 100:.1f}%{'':<10} {overall_mrr:.4f}{'':<6} {overall_correctness * 100:.1f}%")
    print("=" * 92 + "\n")

    summary_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_samples": total_samples,
        "total_answerable": total_answerable,
        "overall_hit_rate": round(overall_hit_rate, 4),
        "overall_mrr": round(overall_mrr, 4),
        "overall_correctness": round(overall_correctness, 4),
        "category_breakdown": category_breakdown,
        "results": eval_results
    }

    # Save output to evals/eval_results.json
    output_path = PROJECT_ROOT / "evals" / "eval_results.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2)

    print(f"[Results Saved] Comprehensive report written to: {output_path}")
    return summary_data


if __name__ == "__main__":
    run_evaluation()
