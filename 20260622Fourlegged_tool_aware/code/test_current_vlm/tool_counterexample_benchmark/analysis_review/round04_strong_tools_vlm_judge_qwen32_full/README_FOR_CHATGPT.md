# README For ChatGPT

This is a local image-aware VLM judge rereview handoff. It is not final paper evidence.

## Scope
- Rows judged: 198
- Tested models: ollama_gemma3_27b_it_q8_0, ollama_llama3_2_vision_11b_instruct_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Tasks: task_001, task_002, task_003, task_004, task_005, task_006, task_007, task_008, task_009, task_010, task_011
- VLM labels: {'true_fail': 69, 'true_pass': 83, 'parse_error': 46}
- Rule comparison types: {'consistent_or_other': 151, 'task002_search_agreement': 14, 'rule_true_pass_vlm_true_fail': 21, 'task002_search_review': 3, 'rule_true_fail_vlm_true_pass': 7, 'rule_fail_vlm_committed_helper_use': 2}

## How To Read
- `vlm_case_rereview.csv/jsonl` contains row-level judge decisions.
- `vlm_rule_disagreements.md` highlights where VLM judge and rule rereview disagree.
- Image-aware judge output can still be wrong and requires human review for claims.

## Key Warnings
- Judge is another VLM, not ground truth.
- Image visibility and physical feasibility should still be human verified.
- Parse failures of tested models and judge parse failures are separate from planning failures.
- This workflow is intended to reduce keyword-rule mistakes, not replace final manual review.
