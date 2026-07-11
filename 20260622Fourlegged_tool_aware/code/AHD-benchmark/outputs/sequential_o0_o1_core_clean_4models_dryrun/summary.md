# Sequential O0/O1 Evaluation Summary

- evaluated rows: 384
- ok evaluations: 0
- generation budget exhausted: 0
- schema echoes: 0
- non-empty parse errors: 0
- provider errors: 0
- clean protocols do not explicitly name task-specific helper types.
- generation/provider failures are not counted as task-capability failures.

## Response Execution Status

| response_status | count |
| --- | ---: |
| dry_run | 384 |

## By Model

| model | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| ollama_qwen3_5_35b | 0 | 0 | 96 | 0 | 0 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 0 | 0 | 96 | 0 | 0 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 0 | 0 | 96 | 0 | 0 |
| ollama_qwen3_vl_8b | 0 | 0 | 96 | 0 | 0 |

## By Protocol

| protocol | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| single_turn_multi_image | 0 | 0 | 192 | 0 | 0 |
| two_turn_sequential | 0 | 0 | 192 | 0 | 0 |

## By Sample Type

| sample_type | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| no_tool_control | 0 | 0 | 48 | 0 | 0 |
| positive_aggregate | 0 | 0 | 48 | 0 | 0 |
| positive_reach | 0 | 0 | 48 | 0 | 0 |
| same_o1_different_o0 | 0 | 0 | 144 | 0 | 0 |
| wrong_helper_negative | 0 | 0 | 96 | 0 | 0 |

## Same O1 Different O0 Consistency

| model | prompt | group | consistency |
| --- | --- | --- | --- |
| ollama_qwen3_5_35b | multi_image__efficient_safe_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | multi_image__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | multi_image__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | multi_image__natural_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | multi_image__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | multi_image__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | two_turn__efficient_safe_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | two_turn__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | two_turn__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | two_turn__natural_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | two_turn__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | two_turn__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__efficient_safe_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__natural_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__efficient_safe_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__natural_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__efficient_safe_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__natural_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__efficient_safe_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__natural_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | multi_image__efficient_safe_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | multi_image__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | multi_image__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | multi_image__natural_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | multi_image__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | multi_image__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | two_turn__efficient_safe_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | two_turn__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | two_turn__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | two_turn__natural_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | two_turn__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_vl_8b | two_turn__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
