# Aggregate Findings

Text-based rereview summary. This is not final paper evidence.

## By prompt category

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| diagnostic_probe | 198 | 73 | 82 | 2 | 41 | 0 | 0.5223 | 0.4076 | 0 | helper_mention_without_use:76; parse_failure:43; helper_search_failure:12; field_plan_inconsistency:7; tool_necessity_miss:4 |
| embodiment_clean | 264 | 81 | 116 | 0 | 67 | 0 | 0.5888 | 0.335 | 25 | aggregation_failure:86; container_affordance_miss:86; parse_failure:67; helper_mention_without_use:25; visual_uncertainty:25 |
| generic_clean | 132 | 42 | 57 | 0 | 33 | 0 | 0.5758 | 0.3232 | 16 | aggregation_failure:41; container_affordance_miss:41; parse_failure:33; helper_mention_without_use:16; visual_uncertainty:16 |
| tool_prior_intervention | 198 | 65 | 83 | 0 | 50 | 0 | 0.5608 | 0.4122 | 56 | helper_mention_without_use:56; visual_uncertainty:56; parse_failure:50; aggregation_failure:16; container_affordance_miss:16 |

## By prompt ID

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| efficient_safe_free_plan | 66 | 20 | 29 | 0 | 17 | 0 | 0.5918 | 0.3061 | 8 | aggregation_failure:21; container_affordance_miss:21; parse_failure:17; helper_mention_without_use:8; visual_uncertainty:8 |
| efficient_safe_free_plan_humanoid_dual_arm | 66 | 20 | 28 | 0 | 18 | 0 | 0.5833 | 0.3542 | 4 | aggregation_failure:22; container_affordance_miss:22; parse_failure:18; helper_search_failure:5; helper_mention_without_use:4 |
| efficient_safe_free_plan_quadruped_single_arm | 66 | 19 | 28 | 0 | 19 | 0 | 0.5957 | 0.3404 | 6 | aggregation_failure:20; container_affordance_miss:20; parse_failure:19; helper_mention_without_use:6; visual_uncertainty:6 |
| natural_free_plan | 66 | 22 | 28 | 0 | 16 | 0 | 0.56 | 0.34 | 8 | aggregation_failure:20; container_affordance_miss:20; parse_failure:16; helper_mention_without_use:8; visual_uncertainty:8 |
| natural_free_plan_humanoid_dual_arm | 66 | 21 | 32 | 0 | 13 | 0 | 0.6038 | 0.3208 | 10 | aggregation_failure:21; container_affordance_miss:21; parse_failure:13; helper_mention_without_use:10; visual_uncertainty:10 |
| natural_free_plan_quadruped_single_arm | 66 | 21 | 28 | 0 | 17 | 0 | 0.5714 | 0.3265 | 5 | aggregation_failure:23; container_affordance_miss:23; parse_failure:17; helper_search_failure:5; helper_mention_without_use:5 |
| structured_tool_action_chain_probe_humanoid_dual_arm | 66 | 25 | 26 | 0 | 15 | 0 | 0.5098 | 0.4314 | 0 | helper_mention_without_use:24; parse_failure:15; helper_search_failure:4; field_plan_inconsistency:2; tool_necessity_miss:1 |
| structured_tool_action_chain_probe_quadruped_single_arm | 66 | 23 | 29 | 2 | 12 | 0 | 0.537 | 0.3889 | 0 | helper_mention_without_use:26; parse_failure:14; helper_search_failure:4; tool_necessity_miss:2; field_plan_inconsistency:2 |
| structured_tool_probe | 66 | 25 | 27 | 0 | 14 | 0 | 0.5192 | 0.4038 | 0 | helper_mention_without_use:26; parse_failure:14; helper_search_failure:4; field_plan_inconsistency:3; target_as_helper:2 |
| tool_prior_free_plan | 66 | 22 | 31 | 0 | 13 | 0 | 0.5849 | 0.4151 | 26 | helper_mention_without_use:26; visual_uncertainty:26; parse_failure:13; tool_necessity_miss:6; helper_search_failure:4 |
| tool_prior_free_plan_humanoid_dual_arm | 66 | 22 | 27 | 0 | 17 | 0 | 0.551 | 0.4286 | 16 | parse_failure:17; helper_mention_without_use:16; visual_uncertainty:16; aggregation_failure:7; container_affordance_miss:7 |
| tool_prior_free_plan_quadruped_single_arm | 66 | 21 | 25 | 0 | 20 | 0 | 0.5435 | 0.3913 | 14 | parse_failure:20; helper_mention_without_use:14; visual_uncertainty:14; aggregation_failure:9; container_affordance_miss:9 |

## By model

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ollama_gemma3_27b_it_q8_0 | 132 | 47 | 85 | 0 | 0 | 0 | 0.6439 | 0.2727 | 25 | helper_mention_without_use:46; aggregation_failure:38; container_affordance_miss:38; visual_uncertainty:25; helper_search_failure:12 |
| ollama_llama3_2_vision_11b_instruct_q8_0 | 132 | 0 | 0 | 0 | 132 | 0 | 0 | 0 | 0 | parse_failure:132 |
| ollama_minicpm_v4_5_q8_0 | 132 | 56 | 74 | 2 | 0 | 0 | 0.5606 | 0.3712 | 19 | helper_mention_without_use:36; aggregation_failure:33; container_affordance_miss:33; visual_uncertainty:19; helper_search_failure:9 |
| ollama_qwen3_5_35b | 132 | 36 | 37 | 0 | 59 | 0 | 0.5068 | 0.411 | 15 | parse_failure:59; helper_mention_without_use:25; visual_uncertainty:15; aggregation_failure:6; container_affordance_miss:6 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 132 | 62 | 70 | 0 | 0 | 0 | 0.5303 | 0.3788 | 16 | aggregation_failure:37; container_affordance_miss:37; helper_mention_without_use:33; visual_uncertainty:16; helper_search_failure:12 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 132 | 60 | 72 | 0 | 0 | 0 | 0.5455 | 0.4394 | 22 | helper_mention_without_use:33; aggregation_failure:29; container_affordance_miss:29; visual_uncertainty:22; helper_search_failure:12 |

## By task

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| task_001 | 72 | 5 | 51 | 0 | 16 | 0 | 0.9107 | 0.1071 | 11 | aggregation_failure:28; container_affordance_miss:28; helper_mention_without_use:22; parse_failure:16; visual_uncertainty:11 |
| task_002 | 72 | 3 | 53 | 1 | 15 | 0 | 0.9298 | 0.0702 | 7 | helper_search_failure:50; aggregation_failure:33; container_affordance_miss:33; helper_mention_without_use:19; parse_failure:16 |
| task_003 | 72 | 50 | 3 | 1 | 18 | 0 | 0.0556 | 0.9259 | 3 | parse_failure:19; helper_mention_without_use:3; visual_uncertainty:3 |
| task_004 | 72 | 5 | 48 | 0 | 19 | 0 | 0.9057 | 0.0943 | 12 | helper_mention_without_use:25; aggregation_failure:23; container_affordance_miss:23; parse_failure:19; visual_uncertainty:12 |
| task_005 | 72 | 12 | 40 | 0 | 20 | 0 | 0.7692 | 0.2308 | 10 | helper_mention_without_use:23; parse_failure:20; aggregation_failure:17; container_affordance_miss:17; visual_uncertainty:10 |
| task_006 | 72 | 43 | 12 | 0 | 17 | 0 | 0.2182 | 0.8364 | 4 | parse_failure:17; helper_mention_without_use:6; visual_uncertainty:4; aggregation_failure:3; container_affordance_miss:3 |
| task_007 | 72 | 10 | 40 | 0 | 22 | 0 | 0.8 | 0.22 | 20 | helper_mention_without_use:26; parse_failure:22; visual_uncertainty:20; aggregation_failure:13; container_affordance_miss:13 |
| task_008 | 72 | 11 | 47 | 0 | 14 | 0 | 0.8103 | 0.3103 | 12 | helper_mention_without_use:22; aggregation_failure:18; container_affordance_miss:18; parse_failure:14; visual_uncertainty:12 |
| task_009 | 72 | 29 | 25 | 0 | 18 | 0 | 0.463 | 0.6852 | 6 | parse_failure:18; helper_mention_without_use:10; aggregation_failure:7; container_affordance_miss:7; visual_uncertainty:6 |
| task_010 | 72 | 33 | 19 | 0 | 20 | 0 | 0.3654 | 0.6538 | 12 | parse_failure:20; helper_mention_without_use:17; visual_uncertainty:12; aggregation_failure:1; container_affordance_miss:1 |
| task_011 | 72 | 60 | 0 | 0 | 12 | 0 | 0.0 | 0.0 | 0 | parse_failure:12 |

## By embodiment

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| generic | 264 | 89 | 115 | 0 | 60 | 0 | 0.5637 | 0.3676 | 42 | helper_mention_without_use:68; parse_failure:60; visual_uncertainty:42; aggregation_failure:41; container_affordance_miss:41 |
| humanoid_dual_arm | 264 | 88 | 113 | 0 | 63 | 0 | 0.5622 | 0.3831 | 30 | parse_failure:63; helper_mention_without_use:54; aggregation_failure:50; container_affordance_miss:50; visual_uncertainty:30 |
| quadruped_single_arm | 264 | 84 | 110 | 2 | 68 | 0 | 0.5612 | 0.3622 | 25 | parse_failure:70; aggregation_failure:52; container_affordance_miss:52; helper_mention_without_use:51; visual_uncertainty:25 |

