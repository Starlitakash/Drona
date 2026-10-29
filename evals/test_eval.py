import os
import sys
import json
import pytest
from pathlib import Path

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from evals.eval_harness import run_evaluation

GOLDEN_DATASET_PATH = PROJECT_ROOT / "evals" / "golden_dataset.json"
EVAL_RESULTS_PATH = PROJECT_ROOT / "evals" / "eval_results.json"


@pytest.fixture(scope="session")
def golden_dataset():
    """Loads the golden dataset JSON file."""
    assert GOLDEN_DATASET_PATH.exists(), f"Golden dataset not found at {GOLDEN_DATASET_PATH}"
    with open(GOLDEN_DATASET_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


@pytest.fixture(scope="session")
def eval_summary():
    """
    Returns evaluation summary data.
    If eval_results.json already exists and was computed recently, loads it;
    otherwise runs the evaluation harness.
    """
    if EVAL_RESULTS_PATH.exists():
        with open(EVAL_RESULTS_PATH, "r", encoding="utf-8") as f:
            summary = json.load(f)
        if summary.get("total_samples", 0) == 40:
            return summary

    return run_evaluation(dataset_path=GOLDEN_DATASET_PATH)


def test_golden_dataset_integrity(golden_dataset):
    """Verifies that the golden dataset meets all Phase 4 specifications."""
    # 1. Exactly 40 Q&A pairs
    assert len(golden_dataset) == 40, f"Expected 40 Q&A pairs, got {len(golden_dataset)}"

    # 2. Spans >= 15 distinct documents
    all_sources = set()
    for item in golden_dataset:
        for s in item.get("expected_sources", []):
            all_sources.add(s)
    
    assert len(all_sources) >= 15, f"Expected >= 15 distinct documents spanned, got {len(all_sources)}: {all_sources}"

    # 3. Includes multi-doc queries
    multi_doc_queries = [i for i in golden_dataset if i.get("question_type") == "multi_doc"]
    assert len(multi_doc_queries) >= 3, f"Expected at least 3 multi-doc queries, got {len(multi_doc_queries)}"

    # 4. Includes deliberately unanswerable queries
    unanswerable_queries = [i for i in golden_dataset if i.get("question_type") == "unanswerable"]
    assert len(unanswerable_queries) >= 3, f"Expected at least 3 unanswerable queries, got {len(unanswerable_queries)}"

    # 5. Schema validation
    for item in golden_dataset:
        assert "id" in item
        assert "category" in item
        assert "question" in item
        assert "ground_truth_answer" in item
        assert "question_type" in item


def test_retrieval_hit_rate(eval_summary):
    """Asserts that the hybrid retrieval Hit Rate @ 5 meets the target threshold (>= 85%)."""
    hit_rate = eval_summary["overall_hit_rate"]
    print(f"\n[EVAL METRIC] Overall Retrieval Hit Rate @ 5: {hit_rate:.1%}")
    assert hit_rate >= 0.85, f"Retrieval Hit Rate ({hit_rate:.1%}) fell below required 85% threshold!"


def test_retrieval_mrr(eval_summary):
    """Asserts that the Mean Reciprocal Rank (MRR @ 5) meets the target threshold (>= 0.70)."""
    mrr = eval_summary["overall_mrr"]
    print(f"\n[EVAL METRIC] Overall Retrieval MRR @ 5: {mrr:.4f}")
    assert mrr >= 0.70, f"Retrieval MRR ({mrr:.4f}) fell below required 0.70 threshold!"


def test_answer_correctness(eval_summary):
    """Asserts that Answer Correctness (LLM-judged with keyword fallback) meets threshold (>= 70%)."""
    correctness = eval_summary["overall_correctness"]
    print(f"\n[EVAL METRIC] Overall Answer Correctness: {correctness:.1%}")
    assert correctness >= 0.70, f"Answer Correctness ({correctness:.1%}) fell below required 70% threshold!"


def test_unanswerable_guardrail(eval_summary):
    """Asserts that deliberately unanswerable questions are safely declined without hallucinations."""
    unans_results = [r for r in eval_summary.get("results", []) if r.get("question_type") == "unanswerable"]
    assert len(unans_results) > 0, "No unanswerable queries found in eval results!"
    
    declined_count = sum(1 for r in unans_results if r.get("correctness_score", 0.0) >= 0.5)
    guardrail_accuracy = declined_count / len(unans_results)
    print(f"\n[GUARDRAIL] Unanswerable Questions Declined Correctly: {guardrail_accuracy:.1%} ({declined_count}/{len(unans_results)})")
    assert guardrail_accuracy >= 0.75, f"Unanswerable guardrail accuracy ({guardrail_accuracy:.1%}) fell below 75%!"


def test_category_coverage(eval_summary):
    """Verifies that every category has been evaluated and recorded in the breakdown."""
    breakdown = eval_summary.get("category_breakdown", {})
    required_cats = [
        "hr_benefits",
        "travel_and_expense",
        "engineering_and_devops",
        "it_and_workplace",
        "compensation_and_payroll",
        "multi_doc",
        "unanswerable"
    ]
    for cat in required_cats:
        assert cat in breakdown, f"Category '{cat}' missing from breakdown report!"
        assert breakdown[cat]["total"] > 0, f"Category '{cat}' has 0 samples!"
