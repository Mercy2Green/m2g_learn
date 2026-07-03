# VLM Judge Aggregate Findings

Image-aware local VLM judge summary. This is still not final paper evidence.

## Overall

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| overall | 1188 | 397 | 518 | 0 | 273 | 0 | 915 | 0 | 0 | 0.5661 | 0.3366 | direct_operation_without_helper:503; tested_model_parse_error:273; helper_mention_without_use:86; helper_search_failure:84; conditional_helper_only:43; aggregation_failure:30 |

## By task

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| task_001 | 108 | 15 | 70 | 0 | 23 | 0 | 85 | 0 | 0 | 0.8235 | 0.1765 | direct_operation_without_helper:69; tested_model_parse_error:23; aggregation_failure:18; helper_mention_without_use:7; conditional_helper_only:3 |
| task_002 | 108 | 0 | 85 | 0 | 23 | 0 | 85 | 0 | 0 | 1.0 | 0.0 | helper_search_failure:84; direct_operation_without_helper:84; tested_model_parse_error:23; conditional_helper_only:3; helper_mention_without_use:2 |
| task_003 | 108 | 66 | 14 | 0 | 28 | 0 | 80 | 0 | 0 | 0.175 | 0.825 | tested_model_parse_error:28; direct_operation_without_helper:14; helper_mention_without_use:7 |
| task_004 | 108 | 9 | 72 | 0 | 27 | 0 | 81 | 0 | 0 | 0.8889 | 0.1111 | direct_operation_without_helper:71; tested_model_parse_error:27; helper_mention_without_use:9; conditional_helper_only:8; aggregation_failure:1 |
| task_005 | 108 | 9 | 69 | 0 | 30 | 0 | 78 | 0 | 0 | 0.8846 | 0.1154 | direct_operation_without_helper:68; tested_model_parse_error:30; helper_mention_without_use:17; aggregation_failure:5; conditional_helper_only:1; tool_necessity_miss:1 |
| task_006 | 108 | 62 | 22 | 0 | 24 | 0 | 84 | 0 | 0 | 0.2619 | 0.7381 | tested_model_parse_error:24; direct_operation_without_helper:21; container_affordance_miss:17 |
| task_007 | 108 | 45 | 40 | 0 | 23 | 0 | 85 | 0 | 0 | 0.4706 | 0.5294 | direct_operation_without_helper:40; tested_model_parse_error:23; helper_mention_without_use:5; aggregation_failure:2; conditional_helper_only:1; container_affordance_miss:1 |
| task_008 | 108 | 25 | 62 | 0 | 21 | 0 | 87 | 0 | 0 | 0.7126 | 0.2874 | direct_operation_without_helper:61; tested_model_parse_error:21; conditional_helper_only:19; helper_mention_without_use:2; physical_capacity_hallucination:1 |
| task_009 | 108 | 50 | 32 | 0 | 26 | 0 | 82 | 0 | 0 | 0.3902 | 0.6098 | direct_operation_without_helper:32; tested_model_parse_error:26; conditional_helper_only:2 |
| task_010 | 108 | 26 | 52 | 0 | 30 | 0 | 78 | 0 | 0 | 0.6667 | 0.3462 | direct_operation_without_helper:43; helper_mention_without_use:37; tested_model_parse_error:30; conditional_helper_only:6; container_affordance_miss:4; aggregation_failure:4 |
| task_011 | 108 | 90 | 0 | 0 | 18 | 0 | 90 | 0 | 0 | 0.0 | 0.0 | tested_model_parse_error:18 |

## By model

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ollama_gemma3_27b_it_q8_0 | 198 | 43 | 155 | 0 | 0 | 0 | 198 | 0 | 0 | 0.7828 | 0.1263 | direct_operation_without_helper:149; helper_mention_without_use:23; container_affordance_miss:19; helper_search_failure:18; aggregation_failure:15; conditional_helper_only:4 |
| ollama_llama3_2_vision_11b_instruct_q8_0 | 198 | 0 | 0 | 0 | 198 | 0 | 0 | 0 | 0 | 0 | 0 | tested_model_parse_error:198 |
| ollama_minicpm_v4_5_q8_0 | 198 | 67 | 131 | 0 | 0 | 0 | 198 | 0 | 0 | 0.6616 | 0.2475 | direct_operation_without_helper:127; helper_mention_without_use:24; conditional_helper_only:18; helper_search_failure:17; aggregation_failure:2; tool_necessity_miss:1 |
| ollama_qwen3_5_35b | 198 | 75 | 48 | 0 | 75 | 0 | 123 | 0 | 0 | 0.3902 | 0.4634 | tested_model_parse_error:75; direct_operation_without_helper:48; helper_search_failure:13; helper_mention_without_use:8; aggregation_failure:1; conditional_helper_only:1 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 198 | 99 | 99 | 0 | 0 | 0 | 198 | 0 | 0 | 0.5 | 0.4141 | direct_operation_without_helper:97; helper_search_failure:18; helper_mention_without_use:17; aggregation_failure:7; conditional_helper_only:2; container_affordance_miss:1 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 198 | 113 | 85 | 0 | 0 | 0 | 198 | 0 | 0 | 0.4293 | 0.4798 | direct_operation_without_helper:82; helper_search_failure:18; conditional_helper_only:18; helper_mention_without_use:14; aggregation_failure:5; container_affordance_miss:1 |

## By prompt

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| efficient_safe_free_plan | 66 | 19 | 32 | 0 | 15 | 0 | 51 | 0 | 0 | 0.6275 | 0.2745 | direct_operation_without_helper:30; tested_model_parse_error:15; helper_search_failure:5; helper_mention_without_use:4; conditional_helper_only:1; container_affordance_miss:1 |
| efficient_safe_free_plan_humanoid_dual_arm | 66 | 17 | 33 | 0 | 16 | 0 | 50 | 0 | 0 | 0.66 | 0.24 | direct_operation_without_helper:33; tested_model_parse_error:16; helper_search_failure:4; helper_mention_without_use:3; container_affordance_miss:1; conditional_helper_only:1 |
| efficient_safe_free_plan_quadruped_single_arm | 66 | 16 | 33 | 0 | 17 | 0 | 49 | 0 | 0 | 0.6735 | 0.2245 | direct_operation_without_helper:32; tested_model_parse_error:17; helper_search_failure:4; helper_mention_without_use:4; aggregation_failure:3; conditional_helper_only:2 |
| natural_free_plan | 66 | 22 | 31 | 0 | 13 | 0 | 53 | 0 | 0 | 0.5849 | 0.3208 | direct_operation_without_helper:30; tested_model_parse_error:13; helper_mention_without_use:6; helper_search_failure:5; conditional_helper_only:2; aggregation_failure:1 |
| natural_free_plan_humanoid_dual_arm | 66 | 18 | 35 | 0 | 13 | 0 | 53 | 0 | 0 | 0.6604 | 0.2453 | direct_operation_without_helper:35; tested_model_parse_error:13; helper_search_failure:5; helper_mention_without_use:4; conditional_helper_only:3; aggregation_failure:1 |
| natural_free_plan_quadruped_single_arm | 66 | 14 | 36 | 0 | 16 | 0 | 50 | 0 | 0 | 0.72 | 0.18 | direct_operation_without_helper:36; tested_model_parse_error:16; helper_search_failure:5; conditional_helper_only:5; aggregation_failure:4; container_affordance_miss:2 |
| search_explicit_strong_decomposition_free_plan | 66 | 30 | 21 | 0 | 15 | 0 | 51 | 0 | 0 | 0.4118 | 0.4902 | direct_operation_without_helper:18; tested_model_parse_error:15; helper_search_failure:5; helper_mention_without_use:4; conditional_helper_only:3; aggregation_failure:2 |
| search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | 66 | 28 | 24 | 0 | 14 | 0 | 52 | 0 | 0 | 0.4615 | 0.4615 | direct_operation_without_helper:21; tested_model_parse_error:14; helper_search_failure:5; conditional_helper_only:3; container_affordance_miss:2; aggregation_failure:1 |
| search_explicit_strong_decomposition_free_plan_quadruped_single_arm | 66 | 23 | 26 | 0 | 17 | 0 | 49 | 0 | 0 | 0.5306 | 0.3673 | direct_operation_without_helper:24; tested_model_parse_error:17; conditional_helper_only:6; aggregation_failure:5; helper_search_failure:3; container_affordance_miss:2 |
| strong_decomposition_free_plan | 66 | 32 | 21 | 0 | 13 | 0 | 53 | 0 | 0 | 0.3962 | 0.5094 | direct_operation_without_helper:20; tested_model_parse_error:13; helper_search_failure:5; conditional_helper_only:2; helper_mention_without_use:2; aggregation_failure:1 |
| strong_decomposition_free_plan_humanoid_dual_arm | 66 | 27 | 25 | 0 | 14 | 0 | 52 | 0 | 0 | 0.4808 | 0.4231 | direct_operation_without_helper:25; tested_model_parse_error:14; helper_search_failure:5; conditional_helper_only:2; helper_mention_without_use:2; tool_necessity_miss:1 |
| strong_decomposition_free_plan_quadruped_single_arm | 66 | 26 | 23 | 0 | 17 | 0 | 49 | 0 | 0 | 0.4694 | 0.4286 | direct_operation_without_helper:22; tested_model_parse_error:17; helper_search_failure:5; aggregation_failure:2; helper_mention_without_use:2; conditional_helper_only:2 |
| structured_tool_action_chain_probe_humanoid_dual_arm | 66 | 20 | 32 | 0 | 14 | 0 | 52 | 0 | 0 | 0.6154 | 0.2885 | direct_operation_without_helper:32; tested_model_parse_error:14; helper_mention_without_use:11; helper_search_failure:5; aggregation_failure:2; conditional_helper_only:2 |
| structured_tool_action_chain_probe_quadruped_single_arm | 66 | 17 | 37 | 0 | 12 | 0 | 54 | 0 | 0 | 0.6852 | 0.2222 | direct_operation_without_helper:37; helper_mention_without_use:17; tested_model_parse_error:12; helper_search_failure:5; aggregation_failure:3; container_affordance_miss:1 |
| structured_tool_probe | 66 | 20 | 31 | 0 | 15 | 0 | 51 | 0 | 0 | 0.6078 | 0.2941 | direct_operation_without_helper:30; tested_model_parse_error:15; helper_mention_without_use:14; helper_search_failure:4; conditional_helper_only:2; container_affordance_miss:2 |
| tool_prior_free_plan | 66 | 32 | 21 | 0 | 13 | 0 | 53 | 0 | 0 | 0.3962 | 0.5094 | direct_operation_without_helper:21; tested_model_parse_error:13; helper_search_failure:5; helper_mention_without_use:3; aggregation_failure:1; container_affordance_miss:1 |
| tool_prior_free_plan_humanoid_dual_arm | 66 | 19 | 28 | 0 | 19 | 0 | 47 | 0 | 0 | 0.5957 | 0.2979 | direct_operation_without_helper:28; tested_model_parse_error:19; helper_search_failure:5; conditional_helper_only:4; helper_mention_without_use:4; container_affordance_miss:1 |
| tool_prior_free_plan_quadruped_single_arm | 66 | 17 | 29 | 0 | 20 | 0 | 46 | 0 | 0 | 0.6304 | 0.2609 | direct_operation_without_helper:29; tested_model_parse_error:20; helper_search_failure:4; aggregation_failure:3; helper_mention_without_use:3; container_affordance_miss:1 |

## By task family

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| aggregation_transport | 540 | 104 | 303 | 0 | 133 | 0 | 407 | 0 | 0 | 0.7445 | 0.258 | direct_operation_without_helper:291; tested_model_parse_error:133; helper_mention_without_use:75; aggregation_failure:30; conditional_helper_only:19; container_affordance_miss:5 |
| cleanup_collection | 216 | 112 | 54 | 0 | 50 | 0 | 166 | 0 | 0 | 0.3253 | 0.6747 | direct_operation_without_helper:53; tested_model_parse_error:50; container_affordance_miss:17; conditional_helper_only:2 |
| control_no_tool | 108 | 90 | 0 | 0 | 18 | 0 | 90 | 0 | 0 | 0.0 | 0.0 | tested_model_parse_error:18 |
| helper_search | 108 | 0 | 85 | 0 | 23 | 0 | 85 | 0 | 0 | 1.0 | 0.0 | helper_search_failure:84; direct_operation_without_helper:84; tested_model_parse_error:23; conditional_helper_only:3; helper_mention_without_use:2 |
| other | 108 | 66 | 14 | 0 | 28 | 0 | 80 | 0 | 0 | 0.175 | 0.825 | tested_model_parse_error:28; direct_operation_without_helper:14; helper_mention_without_use:7 |
| reach_extension | 108 | 25 | 62 | 0 | 21 | 0 | 87 | 0 | 0 | 0.7126 | 0.2874 | direct_operation_without_helper:61; tested_model_parse_error:21; conditional_helper_only:19; helper_mention_without_use:2; physical_capacity_hallucination:1 |
