# Strict VLM Judge V3 Image-Audit-Aware Summary

## Overall

- judge model: qwen3-vl:32b-instruct-q4_K_M
- source rows: 384
- eligible rows: 338
- selected rows: 338
- judged rows: 337
- judge errors: 1
- pass/fail/needs_review: 145/171/21
- physical_o1_helper_chain: 10 (0.030)
- embodiment_batching: 24 (0.071)
- direct_multi_trip: 46 (0.136)
- hallucinated_helper: 7 (0.021)
- visual_conflict: 249 (0.739)
- image_audit_overridden rows: 215

## By Model

| model_id | judged | pass | fail | review | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate | visual conflict | conflict rate | overridden |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ollama_qwen3_5_35b | 91 | 40 | 45 | 6 | 4 | 0.044 | 6 | 0.066 | 10 | 0.110 | 5 | 0.055 | 67 | 0.736 | 57 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 96 | 42 | 51 | 3 | 2 | 0.021 | 9 | 0.094 | 18 | 0.188 | 2 | 0.021 | 70 | 0.729 | 60 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 96 | 40 | 49 | 7 | 4 | 0.042 | 7 | 0.073 | 12 | 0.125 | 0 | 0.000 | 69 | 0.719 | 60 |
| ollama_qwen3_vl_8b | 54 | 23 | 26 | 5 | 0 | 0.000 | 2 | 0.037 | 6 | 0.111 | 0 | 0.000 | 43 | 0.796 | 38 |

## By Protocol

| protocol | judged | pass | fail | review | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate | visual conflict | conflict rate | overridden |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| single_turn_multi_image | 161 | 74 | 83 | 4 | 1 | 0.006 | 17 | 0.106 | 31 | 0.193 | 1 | 0.006 | 122 | 0.758 | 104 |
| two_turn_sequential | 176 | 71 | 88 | 17 | 9 | 0.051 | 7 | 0.040 | 15 | 0.085 | 6 | 0.034 | 127 | 0.722 | 111 |

## By Sample Type

| sample_type | judged | pass | fail | review | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate | visual conflict | conflict rate | overridden |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| no_tool_control | 43 | 22 | 21 | 0 | 0 | 0.000 | 2 | 0.047 | 1 | 0.023 | 0 | 0.000 | 43 | 1.000 | 43 |
| positive_aggregate | 45 | 3 | 30 | 12 | 5 | 0.111 | 9 | 0.200 | 16 | 0.356 | 2 | 0.044 | 42 | 0.933 | 45 |
| positive_reach | 40 | 0 | 40 | 0 | 0 | 0.000 | 2 | 0.050 | 4 | 0.100 | 0 | 0.000 | 40 | 1.000 | 0 |
| same_o1_different_o0 | 127 | 41 | 77 | 9 | 4 | 0.031 | 11 | 0.087 | 17 | 0.134 | 4 | 0.031 | 124 | 0.976 | 127 |
| wrong_helper_negative | 82 | 79 | 3 | 0 | 1 | 0.012 | 0 | 0.000 | 8 | 0.098 | 1 | 0.012 | 0 | 0.000 | 0 |

## Critical Strict V2 vs Strict V3

| group by | value | comparable | physical v2 | physical v3 | hallucinated v2 | hallucinated v3 | review v2 | review v3 | same-O1 pass v2 | same-O1 pass v3 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| overall | all | 337 | 4 | 10 | 14 | 7 | 7 | 21 | 0 | 2 |
| model_id | ollama_qwen3_5_35b | 91 | 0 | 4 | 9 | 5 | 2 | 6 | 0 | 0 |
| model_id | ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 96 | 0 | 2 | 4 | 2 | 2 | 3 | 0 | 1 |
| model_id | ollama_qwen3_vl_32b_instruct_q4_K_M | 96 | 4 | 4 | 1 | 0 | 3 | 7 | 0 | 1 |
| model_id | ollama_qwen3_vl_8b | 54 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 |
| protocol | single_turn_multi_image | 161 | 0 | 1 | 0 | 1 | 2 | 4 | 0 | 0 |
| protocol | two_turn_sequential | 176 | 4 | 9 | 14 | 6 | 5 | 17 | 0 | 2 |
| sample_type | no_tool_control | 43 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| sample_type | positive_aggregate | 45 | 2 | 5 | 7 | 2 | 1 | 12 | 0 | 0 |
| sample_type | positive_reach | 40 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| sample_type | same_o1_different_o0 | 127 | 2 | 4 | 7 | 4 | 6 | 9 | 0 | 2 |
| sample_type | wrong_helper_negative | 82 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |

## Same-O1 Consistency V3

- groups evaluated: 38
- consistency pass: 2
- consistency fail: 36
- not available: 9
- consistency pass rate: 0.053

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
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | pass |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__efficient_safe_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__efficient_safe_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | pass |
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
