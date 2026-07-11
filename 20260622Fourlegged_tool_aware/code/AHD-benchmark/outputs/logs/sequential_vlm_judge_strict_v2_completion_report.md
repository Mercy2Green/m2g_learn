# Sequential Strict VLM Judge V2 Completion Report

- Candidate VLM experiments were not rerun.
- Only the response-level strict VLM judge v2 was run.
- Judge model: qwen3-vl:32b-instruct-q4_K_M
- Limit: 5
- Core manual review pack: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/AHD-benchmark/outputs/test_o0o1_v2/sequential_o0_o1_core_clean_4models_v2/response_judge_qwen32_strict_v2/manual_review_pack_vlm_strict_v2.md
- Sensitivity manual review pack: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/AHD-benchmark/outputs/test_o0o1_v2/sequential_o0_o1_prompt_sensitivity_3models_v2/response_judge_qwen32_strict_v2/manual_review_pack_vlm_strict_v2.md

## Core Strict V2 Summary

# Strict VLM Judge V2 Summary

## Overall

- judge model: qwen3-vl:32b-instruct-q4_K_M
- source rows: 384
- eligible ok_eval rows: 338
- selected rows: 5
- judged rows: 5
- judge errors: 0
- pass: 0
- fail: 5
- needs_review: 0
- pass rate: 0.000
- failure rate: 1.000
- needs_review rate: 0.000
- non-independent rows: 3

## By Model

| model_id | judged | pass | fail | review | pass rate | failure rate | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 3 | 0 | 3 | 0 | 0.000 | 1.000 | 0 | 0.000 | 1 | 0.333 | 2 | 0.667 | 1 | 0.333 |
| ollama_qwen3_vl_8b | 2 | 0 | 2 | 0 | 0.000 | 1.000 | 0 | 0.000 | 0 | 0.000 | 1 | 0.500 | 0 | 0.000 |

## By Protocol

| protocol | judged | pass | fail | review | pass rate | failure rate | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| single_turn_multi_image | 3 | 0 | 3 | 0 | 0.000 | 1.000 | 0 | 0.000 | 1 | 0.333 | 3 | 1.000 | 0 | 0.000 |
| two_turn_sequential | 2 | 0 | 2 | 0 | 0.000 | 1.000 | 0 | 0.000 | 0 | 0.000 | 0 | 0.000 | 1 | 0.500 |

## By Sample Type

| sample_type | judged | pass | fail | review | pass rate | failure rate | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| positive_aggregate | 5 | 0 | 5 | 0 | 0.000 | 1.000 | 0 | 0.000 | 1 | 0.200 | 3 | 0.600 | 1 | 0.200 |

## Physical O1 Helper Chain

| model_id | judged | physical chains | rate |
| --- | ---: | ---: | ---: |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 3 | 0 | 0.000 |
| ollama_qwen3_vl_8b | 2 | 0 | 0.000 |

| protocol | judged | physical chains | rate |
| --- | ---: | ---: | ---: |
| single_turn_multi_image | 3 | 0 | 0.000 |
| two_turn_sequential | 2 | 0 | 0.000 |

| sample_type | judged | physical chains | rate |
| --- | ---: | ---: | ---: |
| positive_aggregate | 5 | 0 | 0.000 |

## Same-O1 Consistency

- groups evaluated: 0
- consistency pass: 0
- consistency fail: 0
- not available: 0
- consistency pass rate: n/a

| model | prompt | group | consistency |
| --- | --- | --- | --- |

## Core VLM vs Heuristic V2

# Strict VLM Judge V2 vs Heuristic V2

| group by | value | comparable | both pass | both fail | VLM pass / v2 fail | v2 pass / VLM fail | VLM pass / v2 review | v2 pass / VLM review | exact agreement | rate |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| overall | all | 5 | 0 | 4 | 0 | 1 | 0 | 0 | 4 | 0.800 |
| model_id | ollama_qwen3_vl_32b_instruct_q4_K_M | 3 | 0 | 2 | 0 | 1 | 0 | 0 | 2 | 0.667 |
| model_id | ollama_qwen3_vl_8b | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 1.000 |
| protocol | single_turn_multi_image | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 3 | 1.000 |
| protocol | two_turn_sequential | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0.500 |
| sample_type | positive_aggregate | 5 | 0 | 4 | 0 | 1 | 0 | 0 | 4 | 0.800 |
