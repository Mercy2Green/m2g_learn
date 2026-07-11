# Strict VLM Judge V2 Summary

## Overall

- judge model: qwen3-vl:32b-instruct-q4_K_M
- source rows: 384
- eligible ok_eval rows: 338
- selected rows: 338
- judged rows: 337
- judge errors: 1
- pass: 151
- fail: 179
- needs_review: 7
- pass rate: 0.448
- failure rate: 0.542
- needs_review rate: 0.021
- non-independent rows: 96

## By Model

| model_id | judged | pass | fail | review | pass rate | failure rate | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ollama_qwen3_5_35b | 91 | 34 | 55 | 2 | 0.374 | 0.618 | 0 | 0.000 | 12 | 0.132 | 24 | 0.264 | 9 | 0.099 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 96 | 41 | 53 | 2 | 0.427 | 0.564 | 0 | 0.000 | 13 | 0.135 | 28 | 0.292 | 4 | 0.042 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 96 | 49 | 44 | 3 | 0.510 | 0.473 | 4 | 0.042 | 12 | 0.125 | 24 | 0.250 | 1 | 0.010 |
| ollama_qwen3_vl_8b | 54 | 27 | 27 | 0 | 0.500 | 0.500 | 0 | 0.000 | 5 | 0.093 | 13 | 0.241 | 0 | 0.000 |

## By Protocol

| protocol | judged | pass | fail | review | pass rate | failure rate | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| single_turn_multi_image | 161 | 64 | 95 | 2 | 0.398 | 0.597 | 0 | 0.000 | 27 | 0.168 | 55 | 0.342 | 0 | 0.000 |
| two_turn_sequential | 176 | 87 | 84 | 5 | 0.494 | 0.491 | 4 | 0.023 | 15 | 0.085 | 34 | 0.193 | 14 | 0.080 |

## By Sample Type

| sample_type | judged | pass | fail | review | pass rate | failure rate | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| no_tool_control | 43 | 39 | 4 | 0 | 0.907 | 0.093 | 0 | 0.000 | 0 | 0.000 | 1 | 0.023 | 0 | 0.000 |
| positive_aggregate | 45 | 2 | 42 | 1 | 0.044 | 0.955 | 2 | 0.044 | 14 | 0.311 | 29 | 0.644 | 7 | 0.156 |
| positive_reach | 40 | 0 | 40 | 0 | 0.000 | 1.000 | 0 | 0.000 | 2 | 0.050 | 7 | 0.175 | 0 | 0.000 |
| same_o1_different_o0 | 127 | 81 | 40 | 6 | 0.638 | 0.331 | 2 | 0.016 | 10 | 0.079 | 25 | 0.197 | 7 | 0.055 |
| wrong_helper_negative | 82 | 29 | 53 | 0 | 0.354 | 0.646 | 0 | 0.000 | 16 | 0.195 | 27 | 0.329 | 0 | 0.000 |

## Physical O1 Helper Chain

| model_id | judged | physical chains | rate |
| --- | ---: | ---: | ---: |
| ollama_qwen3_5_35b | 91 | 0 | 0.000 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 96 | 0 | 0.000 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 96 | 4 | 0.042 |
| ollama_qwen3_vl_8b | 54 | 0 | 0.000 |

| protocol | judged | physical chains | rate |
| --- | ---: | ---: | ---: |
| single_turn_multi_image | 161 | 0 | 0.000 |
| two_turn_sequential | 176 | 4 | 0.023 |

| sample_type | judged | physical chains | rate |
| --- | ---: | ---: | ---: |
| no_tool_control | 43 | 0 | 0.000 |
| positive_aggregate | 45 | 2 | 0.044 |
| positive_reach | 40 | 0 | 0.000 |
| same_o1_different_o0 | 127 | 2 | 0.016 |
| wrong_helper_negative | 82 | 0 | 0.000 |

## Same-O1 Consistency

- groups evaluated: 38
- consistency pass: 0
- consistency fail: 38
- not available: 9
- consistency pass rate: 0.000

| model | prompt | group | consistency |
| --- | --- | --- | --- |
| ollama_qwen3_5_35b | multi_image__efficient_safe_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | multi_image__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | multi_image__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | multi_image__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | multi_image__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | multi_image__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__efficient_safe_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | two_turn__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__efficient_safe_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__efficient_safe_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__efficient_safe_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__efficient_safe_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_8b | multi_image__efficient_safe_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_8b | multi_image__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | multi_image__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_8b | multi_image__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | multi_image__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | two_turn__efficient_safe_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_8b | two_turn__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | two_turn__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | two_turn__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_8b | two_turn__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | two_turn__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
