# README For ChatGPT

This is a local image-aware VLM judge rereview handoff. It is not final paper evidence.

## Scope
- Rows judged: 5
- Tested models: ollama_gemma3_27b_it_q8_0
- Tasks: task_001, task_002
- VLM labels: {'true_fail': 5}
- Rule comparison types: {'consistent_or_other': 3, 'task002_search_agreement': 2}

## How To Read
- `vlm_case_rereview.csv/jsonl` contains row-level judge decisions.
- `vlm_rule_disagreements.md` highlights where VLM judge and rule rereview disagree.
- Image-aware judge output can still be wrong and requires human review for claims.

## Key Warnings
- Judge is another VLM, not ground truth.
- Image visibility and physical feasibility should still be human verified.
- Parse failures of tested models and judge parse failures are separate from planning failures.
- This workflow is intended to reduce keyword-rule mistakes, not replace final manual review.
