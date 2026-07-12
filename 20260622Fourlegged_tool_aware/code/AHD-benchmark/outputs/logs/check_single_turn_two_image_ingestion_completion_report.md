# Single-Turn Two-Image Ingestion Completion Report

- Original helper-chain candidate experiments were not rerun.
- Original task prompts were not strengthened or modified.
- This run only checks image ingestion and image-order perception.
- Models: ollama_qwen3_5_35b
- Sample limit: none

# Single-Turn Two-Image Ingestion Diagnostic

- samples source: `/home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/sequential_o0_o1/data/sequential_core_eval_samples.jsonl`
- total test cases: 25
- image_count_total values: {1: 10, 2: 15}
- expected two-image cases with image_count_total=2: 15/15
- expected one-image cases with image_count_total=1: 10/10
- missing files: 0
- unexpected O0/O1 duplicate SHA patterns: 0
- mismatched O0/O0 SHA patterns: 0

No base64 or data URL payload content is stored in this manifest.

## By Model

| model_id | O0_O1 | O1_O0 | O0_only | O1_only | O0_O0 | two-image perceived | order distinguish |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ollama_qwen3_5_35b | 0/5 (0.0%) | 0/5 (0.0%) | 5/5 (100.0%) | 5/5 (100.0%) | 0/5 (0.0%) | 0/15 (0.0%) | 0/15 (0.0%) |

## By Sample

| sample_id | O0_O1 | O1_O0 | O0_only | O1_only | O0_O0 | two-image perceived | order distinguish |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| no_tool_control_001 | 0/1 (0.0%) | 0/1 (0.0%) | 1/1 (100.0%) | 1/1 (100.0%) | 0/1 (0.0%) | 0/3 (0.0%) | 0/3 (0.0%) |
| positive_aggregate_001 | 0/1 (0.0%) | 0/1 (0.0%) | 1/1 (100.0%) | 1/1 (100.0%) | 0/1 (0.0%) | 0/3 (0.0%) | 0/3 (0.0%) |
| same_o1_aggregate_001 | 0/1 (0.0%) | 0/1 (0.0%) | 1/1 (100.0%) | 1/1 (100.0%) | 0/1 (0.0%) | 0/3 (0.0%) | 0/3 (0.0%) |
| same_o1_direct_001 | 0/1 (0.0%) | 0/1 (0.0%) | 1/1 (100.0%) | 1/1 (100.0%) | 0/1 (0.0%) | 0/3 (0.0%) | 0/3 (0.0%) |
| wrong_helper_negative_aggregate_001 | 0/1 (0.0%) | 0/1 (0.0%) | 1/1 (100.0%) | 1/1 (100.0%) | 0/1 (0.0%) | 0/3 (0.0%) | 0/3 (0.0%) |

This diagnostic only tests image ingestion and image-order perception.
It does not rerun or replace the helper-chain benchmark and does not strengthen the original task prompt.

Manual review: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/AHD-benchmark/outputs/sanity_check_single_turn_two_images/diagnostic_manual_review.md
Payload manifest: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/AHD-benchmark/outputs/sanity_check_single_turn_two_images/payload_manifest.jsonl
