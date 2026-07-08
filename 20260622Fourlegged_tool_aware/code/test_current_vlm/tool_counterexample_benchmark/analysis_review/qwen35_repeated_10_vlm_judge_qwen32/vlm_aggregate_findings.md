# VLM Judge Aggregate Findings

Image-aware local VLM judge summary. This is still not final paper evidence.

## Overall

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| overall | 1980 | 827 | 454 | 0 | 699 | 0 | 1281 | 0 | 0 | 0.3544 | 0.5121 | tested_model_parse_error:699; direct_operation_without_helper:441; helper_search_failure:128; helper_mention_without_use:90; conditional_helper_only:15; aggregation_failure:13 |

## By task

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| task_001 | 180 | 67 | 57 | 0 | 56 | 0 | 124 | 0 | 0 | 0.4597 | 0.5403 | direct_operation_without_helper:57; tested_model_parse_error:56; helper_mention_without_use:21; aggregation_failure:4; conditional_helper_only:1 |
| task_002 | 180 | 2 | 138 | 0 | 40 | 0 | 140 | 0 | 0 | 0.9857 | 0.0143 | direct_operation_without_helper:137; helper_search_failure:128; tested_model_parse_error:40; helper_mention_without_use:12; conditional_helper_only:4 |
| task_003 | 180 | 89 | 14 | 0 | 77 | 0 | 103 | 0 | 0 | 0.1359 | 0.8641 | tested_model_parse_error:77; direct_operation_without_helper:14; helper_mention_without_use:8; conditional_helper_only:1 |
| task_004 | 180 | 45 | 63 | 0 | 72 | 0 | 108 | 0 | 0 | 0.5833 | 0.4167 | tested_model_parse_error:72; direct_operation_without_helper:57; helper_mention_without_use:11; container_affordance_miss:5; aggregation_failure:4; conditional_helper_only:3 |
| task_005 | 180 | 44 | 38 | 0 | 98 | 0 | 82 | 0 | 0 | 0.4634 | 0.5366 | tested_model_parse_error:98; direct_operation_without_helper:38; helper_mention_without_use:14; aggregation_failure:1 |
| task_006 | 180 | 112 | 7 | 0 | 61 | 0 | 119 | 0 | 0 | 0.0588 | 0.9412 | tested_model_parse_error:61; direct_operation_without_helper:7; helper_mention_without_use:2 |
| task_007 | 180 | 109 | 5 | 0 | 66 | 0 | 114 | 0 | 0 | 0.0439 | 0.9649 | tested_model_parse_error:66; direct_operation_without_helper:4; helper_mention_without_use:3 |
| task_008 | 180 | 64 | 92 | 0 | 24 | 0 | 156 | 0 | 0 | 0.5897 | 0.4103 | direct_operation_without_helper:92; tested_model_parse_error:24; conditional_helper_only:5; helper_mention_without_use:1 |
| task_009 | 180 | 87 | 18 | 0 | 75 | 0 | 105 | 0 | 0 | 0.1714 | 0.8286 | tested_model_parse_error:75; direct_operation_without_helper:18; helper_mention_without_use:2; conditional_helper_only:1 |
| task_010 | 180 | 32 | 22 | 0 | 126 | 0 | 54 | 0 | 0 | 0.4074 | 0.6111 | tested_model_parse_error:126; direct_operation_without_helper:17; helper_mention_without_use:16; aggregation_failure:4; container_affordance_miss:1 |
| task_011 | 180 | 176 | 0 | 0 | 4 | 0 | 176 | 0 | 0 | 0.0 | 0.017 | tested_model_parse_error:4 |

## By model

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ollama_qwen3_5_35b | 1980 | 827 | 454 | 0 | 699 | 0 | 1281 | 0 | 0 | 0.3544 | 0.5121 | tested_model_parse_error:699; direct_operation_without_helper:441; helper_search_failure:128; helper_mention_without_use:90; conditional_helper_only:15; aggregation_failure:13 |

## By prompt

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| efficient_safe_free_plan | 110 | 38 | 31 | 0 | 41 | 0 | 69 | 0 | 0 | 0.4493 | 0.4058 | tested_model_parse_error:41; direct_operation_without_helper:29; helper_search_failure:9; helper_mention_without_use:2; container_affordance_miss:1; aggregation_failure:1 |
| efficient_safe_free_plan_humanoid_dual_arm | 110 | 17 | 35 | 0 | 58 | 0 | 52 | 0 | 0 | 0.6731 | 0.1346 | tested_model_parse_error:58; direct_operation_without_helper:35; helper_search_failure:9; aggregation_failure:4; conditional_helper_only:1 |
| efficient_safe_free_plan_quadruped_single_arm | 110 | 12 | 21 | 0 | 77 | 0 | 33 | 0 | 0 | 0.6364 | 0.0606 | tested_model_parse_error:77; direct_operation_without_helper:21; helper_search_failure:4 |
| natural_free_plan | 110 | 40 | 38 | 0 | 32 | 0 | 78 | 0 | 0 | 0.4872 | 0.3846 | direct_operation_without_helper:37; tested_model_parse_error:32; helper_mention_without_use:9; helper_search_failure:9; conditional_helper_only:3; aggregation_failure:1 |
| natural_free_plan_humanoid_dual_arm | 110 | 36 | 44 | 0 | 30 | 0 | 80 | 0 | 0 | 0.55 | 0.325 | direct_operation_without_helper:44; tested_model_parse_error:30; helper_search_failure:10 |
| natural_free_plan_quadruped_single_arm | 110 | 24 | 43 | 0 | 43 | 0 | 67 | 0 | 0 | 0.6418 | 0.209 | tested_model_parse_error:43; direct_operation_without_helper:43; helper_search_failure:10; aggregation_failure:2; conditional_helper_only:2; helper_mention_without_use:2 |
| search_explicit_strong_decomposition_free_plan | 110 | 74 | 13 | 0 | 23 | 0 | 87 | 0 | 0 | 0.1494 | 0.7356 | tested_model_parse_error:23; direct_operation_without_helper:13; helper_search_failure:4; helper_mention_without_use:1; conditional_helper_only:1 |
| search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | 110 | 68 | 10 | 0 | 32 | 0 | 78 | 0 | 0 | 0.1282 | 0.7436 | tested_model_parse_error:32; helper_search_failure:10; direct_operation_without_helper:10 |
| search_explicit_strong_decomposition_free_plan_quadruped_single_arm | 110 | 55 | 6 | 0 | 49 | 0 | 61 | 0 | 0 | 0.0984 | 0.7377 | tested_model_parse_error:49; direct_operation_without_helper:6; helper_search_failure:2; conditional_helper_only:2; helper_mention_without_use:1 |
| strong_decomposition_free_plan | 110 | 75 | 8 | 0 | 27 | 0 | 83 | 0 | 0 | 0.0964 | 0.7831 | tested_model_parse_error:27; direct_operation_without_helper:8; helper_search_failure:7; helper_mention_without_use:1 |
| strong_decomposition_free_plan_humanoid_dual_arm | 110 | 50 | 15 | 0 | 45 | 0 | 65 | 0 | 0 | 0.2308 | 0.6154 | tested_model_parse_error:45; direct_operation_without_helper:12; helper_search_failure:9; container_affordance_miss:3 |
| strong_decomposition_free_plan_quadruped_single_arm | 110 | 52 | 13 | 0 | 45 | 0 | 65 | 0 | 0 | 0.2 | 0.6462 | tested_model_parse_error:45; direct_operation_without_helper:13; helper_search_failure:9 |
| structured_tool_action_chain_probe_humanoid_dual_arm | 110 | 51 | 32 | 0 | 27 | 0 | 83 | 0 | 0 | 0.3855 | 0.5301 | direct_operation_without_helper:28; tested_model_parse_error:27; helper_mention_without_use:12; helper_search_failure:7; aggregation_failure:2; container_affordance_miss:1 |
| structured_tool_action_chain_probe_quadruped_single_arm | 110 | 43 | 58 | 0 | 9 | 0 | 101 | 0 | 0 | 0.5743 | 0.3267 | direct_operation_without_helper:58; helper_mention_without_use:31; helper_search_failure:10; tested_model_parse_error:9; conditional_helper_only:2 |
| structured_tool_probe | 110 | 35 | 47 | 0 | 28 | 0 | 82 | 0 | 0 | 0.5732 | 0.3293 | direct_operation_without_helper:44; helper_mention_without_use:29; tested_model_parse_error:28; container_affordance_miss:1; aggregation_failure:1; helper_search_failure:1 |
| tool_prior_free_plan | 110 | 81 | 14 | 0 | 15 | 0 | 95 | 0 | 0 | 0.1474 | 0.7474 | tested_model_parse_error:15; direct_operation_without_helper:14; helper_search_failure:9; helper_mention_without_use:1 |
| tool_prior_free_plan_humanoid_dual_arm | 110 | 48 | 13 | 0 | 49 | 0 | 61 | 0 | 0 | 0.2131 | 0.6885 | tested_model_parse_error:49; direct_operation_without_helper:13; helper_search_failure:6; aggregation_failure:2; helper_mention_without_use:1 |
| tool_prior_free_plan_quadruped_single_arm | 110 | 28 | 13 | 0 | 69 | 0 | 41 | 0 | 0 | 0.3171 | 0.439 | tested_model_parse_error:69; direct_operation_without_helper:13; helper_search_failure:3; conditional_helper_only:2 |

## By task family

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| aggregation_transport | 900 | 297 | 185 | 0 | 418 | 0 | 482 | 0 | 0 | 0.3838 | 0.6203 | tested_model_parse_error:418; direct_operation_without_helper:173; helper_mention_without_use:65; aggregation_failure:13; container_affordance_miss:6; conditional_helper_only:4 |
| cleanup_collection | 360 | 199 | 25 | 0 | 136 | 0 | 224 | 0 | 0 | 0.1116 | 0.8884 | tested_model_parse_error:136; direct_operation_without_helper:25; helper_mention_without_use:4; conditional_helper_only:1 |
| control_no_tool | 180 | 176 | 0 | 0 | 4 | 0 | 176 | 0 | 0 | 0.0 | 0.017 | tested_model_parse_error:4 |
| helper_search | 180 | 2 | 138 | 0 | 40 | 0 | 140 | 0 | 0 | 0.9857 | 0.0143 | direct_operation_without_helper:137; helper_search_failure:128; tested_model_parse_error:40; helper_mention_without_use:12; conditional_helper_only:4 |
| other | 180 | 89 | 14 | 0 | 77 | 0 | 103 | 0 | 0 | 0.1359 | 0.8641 | tested_model_parse_error:77; direct_operation_without_helper:14; helper_mention_without_use:8; conditional_helper_only:1 |
| reach_extension | 180 | 64 | 92 | 0 | 24 | 0 | 156 | 0 | 0 | 0.5897 | 0.4103 | direct_operation_without_helper:92; tested_model_parse_error:24; conditional_helper_only:5; helper_mention_without_use:1 |
