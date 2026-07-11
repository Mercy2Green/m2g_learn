# Sequential O0/O1 Offline Analysis V2

- evaluator version: sequential_heuristic_v2
- total raw rows: 384
- ok_eval: 338
- generation_budget_exhausted: 45
- schema_echo: 1
- parse_error_nonempty: 0
- provider_error: 0

V2 distinguishes physical O1 helper use from embodiment batching and direct multi-trip behavior.

## By Model

| model_id | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| ollama_qwen3_5_35b | 15 | 30 | 46 | 0 | 5 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 21 | 32 | 43 | 0 | 0 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 18 | 30 | 48 | 0 | 0 |
| ollama_qwen3_vl_8b | 14 | 21 | 21 | 0 | 40 |

## By Protocol

| protocol | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| single_turn_multi_image | 17 | 61 | 85 | 0 | 29 |
| two_turn_sequential | 51 | 52 | 73 | 0 | 16 |

## By Sample Type

| sample_type | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| no_tool_control | 10 | 0 | 33 | 0 | 5 |
| positive_aggregate | 9 | 37 | 0 | 0 | 2 |
| positive_reach | 0 | 40 | 0 | 0 | 8 |
| same_o1_different_o0 | 29 | 34 | 65 | 0 | 16 |
| wrong_helper_negative | 20 | 2 | 60 | 0 | 14 |

## Physical O1 Helper Chain Success

| model_id | physical chains | passing chains |
| --- | ---: | ---: |
| ollama_qwen3_5_35b | 6 | 5 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 4 | 4 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 6 | 6 |
| ollama_qwen3_vl_8b | 0 | 0 |

| protocol | physical chains | passing chains |
| --- | ---: | ---: |
| single_turn_multi_image | 1 | 0 |
| two_turn_sequential | 15 | 15 |

| sample_type | physical chains | passing chains |
| --- | ---: | ---: |
| no_tool_control | 0 | 0 |
| positive_aggregate | 9 | 9 |
| positive_reach | 0 | 0 |
| same_o1_different_o0 | 6 | 6 |
| wrong_helper_negative | 1 | 0 |

## Action Mode Counts

- embodiment_batching: 50
- direct_multi_trip: 95
- wrong_helper_use: 4
- physical_o1_helper_chain: 16
- no_tool_overuse: 0

## Same O1 Different O0 Consistency

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
| ollama_qwen3_vl_8b | multi_image__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
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
