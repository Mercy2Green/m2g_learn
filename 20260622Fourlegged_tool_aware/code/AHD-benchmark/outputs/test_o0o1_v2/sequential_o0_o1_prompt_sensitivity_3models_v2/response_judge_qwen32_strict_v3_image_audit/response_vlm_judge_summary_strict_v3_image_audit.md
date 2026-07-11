# Strict VLM Judge V3 Image-Audit-Aware Summary

## Overall

- judge model: qwen3-vl:32b-instruct-q4_K_M
- source rows: 540
- eligible rows: 526
- selected rows: 526
- judged rows: 523
- judge errors: 3
- pass/fail/needs_review: 230/222/71
- physical_o1_helper_chain: 62 (0.119)
- embodiment_batching: 44 (0.084)
- direct_multi_trip: 90 (0.172)
- hallucinated_helper: 28 (0.054)
- visual_conflict: 376 (0.719)
- image_audit_overridden rows: 417

## By Model

| model_id | judged | pass | fail | review | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate | visual conflict | conflict rate | overridden |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ollama_qwen3_5_35b | 164 | 79 | 62 | 23 | 24 | 0.146 | 13 | 0.079 | 29 | 0.177 | 6 | 0.037 | 113 | 0.689 | 130 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 179 | 69 | 88 | 22 | 18 | 0.101 | 19 | 0.106 | 30 | 0.168 | 18 | 0.101 | 133 | 0.743 | 143 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 180 | 82 | 72 | 26 | 20 | 0.111 | 12 | 0.067 | 31 | 0.172 | 4 | 0.022 | 130 | 0.722 | 144 |

## By Protocol

| protocol | judged | pass | fail | review | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate | visual conflict | conflict rate | overridden |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| single_turn_multi_image | 259 | 98 | 135 | 26 | 10 | 0.039 | 33 | 0.127 | 73 | 0.282 | 12 | 0.046 | 203 | 0.784 | 207 |
| two_turn_sequential | 264 | 132 | 87 | 45 | 52 | 0.197 | 11 | 0.042 | 17 | 0.064 | 16 | 0.061 | 173 | 0.655 | 210 |

## By Sample Type

| sample_type | judged | pass | fail | review | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate | visual conflict | conflict rate | overridden |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| positive_aggregate | 105 | 22 | 52 | 31 | 30 | 0.286 | 15 | 0.143 | 32 | 0.305 | 3 | 0.029 | 81 | 0.771 | 105 |
| same_o1_different_o0 | 312 | 113 | 159 | 40 | 27 | 0.087 | 26 | 0.083 | 37 | 0.119 | 19 | 0.061 | 295 | 0.946 | 312 |
| wrong_helper_negative | 106 | 95 | 11 | 0 | 5 | 0.047 | 3 | 0.028 | 21 | 0.198 | 6 | 0.057 | 0 | 0.000 | 0 |

## Critical Strict V2 vs Strict V3

| group by | value | comparable | physical v2 | physical v3 | hallucinated v2 | hallucinated v3 | review v2 | review v3 | same-O1 pass v2 | same-O1 pass v3 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| overall | all | 521 | 29 | 62 | 63 | 28 | 46 | 71 | 7 | 7 |
| model_id | ollama_qwen3_5_35b | 163 | 7 | 24 | 23 | 6 | 19 | 23 | 2 | 4 |
| model_id | ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 179 | 5 | 18 | 31 | 18 | 11 | 22 | 1 | 0 |
| model_id | ollama_qwen3_vl_32b_instruct_q4_K_M | 179 | 17 | 20 | 9 | 4 | 16 | 26 | 4 | 3 |
| protocol | single_turn_multi_image | 258 | 1 | 10 | 10 | 12 | 33 | 26 | 0 | 0 |
| protocol | two_turn_sequential | 263 | 28 | 52 | 53 | 16 | 13 | 45 | 7 | 7 |
| sample_type | positive_aggregate | 105 | 11 | 30 | 28 | 3 | 17 | 31 | 0 | 0 |
| sample_type | same_o1_different_o0 | 311 | 16 | 27 | 29 | 19 | 29 | 40 | 7 | 7 |
| sample_type | wrong_helper_negative | 105 | 2 | 5 | 6 | 6 | 0 | 0 | 0 | 0 |

## Same-O1 Consistency V3

- groups evaluated: 99
- consistency pass: 7
- consistency fail: 92
- not available: 9
- consistency pass rate: 0.071

| model | prompt | group | consistency |
| --- | --- | --- | --- |
| ollama_qwen3_5_35b | multi_image__efficient_safe_free_plan | same_o1_container_000001 | not_available |
| ollama_qwen3_5_35b | multi_image__efficient_safe_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
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
| ollama_qwen3_5_35b | two_turn__strong_decomposition_free_plan | same_o1_container_000001 | pass |
| ollama_qwen3_5_35b | two_turn__strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_5_35b | two_turn__strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | pass |
| ollama_qwen3_5_35b | two_turn__structured_tool_action_chain_probe_humanoid_dual_arm | same_o1_container_000001 | pass |
| ollama_qwen3_5_35b | two_turn__structured_tool_action_chain_probe_quadruped_single_arm | same_o1_container_000001 | pass |
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
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | two_turn__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | not_available |
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
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__search_explicit_strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | pass |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__strong_decomposition_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__strong_decomposition_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__strong_decomposition_free_plan_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__structured_tool_action_chain_probe_humanoid_dual_arm | same_o1_container_000001 | pass |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__structured_tool_action_chain_probe_quadruped_single_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__structured_tool_probe | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__tool_prior_free_plan | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__tool_prior_free_plan_humanoid_dual_arm | same_o1_container_000001 | fail |
| ollama_qwen3_vl_32b_instruct_q4_K_M | two_turn__tool_prior_free_plan_quadruped_single_arm | same_o1_container_000001 | pass |
