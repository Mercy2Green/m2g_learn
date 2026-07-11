# Sequential O0/O1 Evaluation Summary

- evaluated rows: 540
- ok evaluations: 526
- generation budget exhausted: 14
- schema echoes: 0
- non-empty parse errors: 0
- provider errors: 0
- clean protocols do not explicitly name task-specific helper types.
- generation/provider failures are not counted as task-capability failures.

## Response Execution Status

| response_status | count |
| --- | ---: |
| generation_budget_exhausted | 14 |
| ok_eval | 526 |

## By Model

| model | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| ollama_qwen3_5_35b | 52 | 52 | 62 | 0 | 14 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 54 | 71 | 55 | 0 | 0 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 69 | 71 | 40 | 0 | 0 |

## By Protocol

| protocol | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| single_turn_multi_image | 63 | 94 | 104 | 0 | 9 |
| two_turn_sequential | 112 | 100 | 53 | 0 | 5 |

## By Sample Type

| sample_type | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| positive_aggregate | 38 | 68 | 0 | 0 | 2 |
| same_o1_different_o0 | 117 | 89 | 108 | 0 | 10 |
| wrong_helper_negative | 20 | 37 | 49 | 0 | 2 |

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
| ollama_qwen3_5_35b | two_turn__efficient_safe_free_plan_quadruped_single_arm | same_o1_container_000001 | pass |
| ollama_qwen3_5_35b | two_turn__natural_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | pass |
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
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | pass |
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
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__natural_free_plan_humanoid_dual_arm | same_o1_container_000001 | pass |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__natural_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__search_explicit_strong_decomposition_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__search_explicit_strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__strong_decomposition_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__structured_tool_action_chain_probe_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__structured_tool_action_chain_probe_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__structured_tool_probe | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__tool_prior_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__tool_prior_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__tool_prior_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
