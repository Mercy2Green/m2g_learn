# Sequential O0/O1 Analysis V2 Completion Report

- Candidate VLM experiments were not rerun; analysis used existing raw_responses.jsonl files only.
- The response-level VLM judge was not rerun.
- Core manual review pack: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/outputs/sequential_o0_o1_core_clean_4models/analysis_v2/manual_review_pack_v2.md
- Sensitivity manual review pack: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/outputs/sequential_o0_o1_prompt_sensitivity_3models/analysis_v2/manual_review_pack_v2.md
- Review images: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/AHD-benchmark/outputs/sequential_analysis_v2_review_images

## Core Analysis V2

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

## Prompt Sensitivity Analysis V2

# Sequential O0/O1 Offline Analysis V2

- evaluator version: sequential_heuristic_v2
- total raw rows: 540
- ok_eval: 526
- generation_budget_exhausted: 14
- schema_echo: 0
- parse_error_nonempty: 0
- provider_error: 0

V2 distinguishes physical O1 helper use from embodiment batching and direct multi-trip behavior.

## By Model

| model_id | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| ollama_qwen3_5_35b | 47 | 43 | 76 | 0 | 14 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 60 | 41 | 79 | 0 | 0 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 70 | 40 | 70 | 0 | 0 |

## By Protocol

| protocol | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| single_turn_multi_image | 50 | 79 | 132 | 0 | 9 |
| two_turn_sequential | 127 | 45 | 93 | 0 | 5 |

## By Sample Type

| sample_type | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| positive_aggregate | 46 | 60 | 0 | 0 | 2 |
| same_o1_different_o0 | 94 | 58 | 162 | 0 | 10 |
| wrong_helper_negative | 37 | 6 | 63 | 0 | 2 |

## Physical O1 Helper Chain Success

| model_id | physical chains | passing chains |
| --- | ---: | ---: |
| ollama_qwen3_5_35b | 32 | 27 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 40 | 36 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 43 | 42 |

| protocol | physical chains | passing chains |
| --- | ---: | ---: |
| single_turn_multi_image | 37 | 30 |
| two_turn_sequential | 78 | 75 |

| sample_type | physical chains | passing chains |
| --- | ---: | ---: |
| positive_aggregate | 46 | 46 |
| same_o1_different_o0 | 48 | 47 |
| wrong_helper_negative | 21 | 12 |

## Action Mode Counts

- embodiment_batching: 92
- direct_multi_trip: 123
- wrong_helper_use: 12
- physical_o1_helper_chain: 115
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
| ollama_qwen3_5_35b | multi_image__search_explicit_strong_decomposition_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | multi_image__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | multi_image__search_explicit_strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | multi_image__strong_decomposition_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | multi_image__strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | multi_image__strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | multi_image__structured_tool_action_chain_probe_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | multi_image__structured_tool_action_chain_probe_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | multi_image__structured_tool_probe | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | multi_image__tool_prior_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | multi_image__tool_prior_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | multi_image__tool_prior_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__efficient_safe_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__search_explicit_strong_decomposition_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | two_turn__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__search_explicit_strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | two_turn__strong_decomposition_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__structured_tool_action_chain_probe_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__structured_tool_action_chain_probe_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__structured_tool_probe | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | two_turn__tool_prior_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | two_turn__tool_prior_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__tool_prior_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__efficient_safe_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__search_explicit_strong_decomposition_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__search_explicit_strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__strong_decomposition_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__structured_tool_action_chain_probe_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__structured_tool_action_chain_probe_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__structured_tool_probe | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__tool_prior_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__tool_prior_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | multi_image__tool_prior_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__efficient_safe_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__search_explicit_strong_decomposition_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__search_explicit_strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__strong_decomposition_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__structured_tool_action_chain_probe_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__structured_tool_action_chain_probe_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__structured_tool_probe | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__tool_prior_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__tool_prior_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__tool_prior_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__efficient_safe_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__search_explicit_strong_decomposition_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__search_explicit_strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__strong_decomposition_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__structured_tool_action_chain_probe_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__structured_tool_action_chain_probe_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__structured_tool_probe | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__tool_prior_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__tool_prior_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | multi_image__tool_prior_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__efficient_safe_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__search_explicit_strong_decomposition_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__search_explicit_strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__strong_decomposition_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__structured_tool_action_chain_probe_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__structured_tool_action_chain_probe_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__structured_tool_probe | same_o1_container_000001 | pass |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__tool_prior_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__tool_prior_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__tool_prior_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
