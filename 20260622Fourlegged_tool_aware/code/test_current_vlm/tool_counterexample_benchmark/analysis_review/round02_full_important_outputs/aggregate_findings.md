# Aggregate Findings

Text-based rereview summary. This is not final paper evidence.

## By prompt category

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| diagnostic_probe | 198 | 59 | 96 | 2 | 41 | 0 | 0.6115 | 0.3758 | 0 | helper_mention_without_use:81; parse_failure:43; helper_search_failure:12; wrong_helper_type:10; field_plan_inconsistency:8 |
| embodiment_clean | 264 | 68 | 129 | 0 | 67 | 0 | 0.6548 | 0.2893 | 24 | aggregation_failure:96; container_affordance_miss:96; parse_failure:67; helper_mention_without_use:24; visual_uncertainty:24 |
| generic_clean | 132 | 31 | 68 | 0 | 33 | 0 | 0.6869 | 0.2828 | 15 | aggregation_failure:46; container_affordance_miss:46; parse_failure:33; helper_mention_without_use:15; visual_uncertainty:15 |
| tool_prior_intervention | 198 | 49 | 99 | 0 | 50 | 0 | 0.6689 | 0.3311 | 59 | helper_mention_without_use:59; visual_uncertainty:59; parse_failure:50; aggregation_failure:25; container_affordance_miss:25 |

## By prompt ID

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| efficient_safe_free_plan | 66 | 15 | 34 | 0 | 17 | 0 | 0.6939 | 0.2857 | 6 | aggregation_failure:24; container_affordance_miss:24; parse_failure:17; physical_capacity_hallucination:6; helper_mention_without_use:6 |
| efficient_safe_free_plan_humanoid_dual_arm | 66 | 19 | 29 | 0 | 18 | 0 | 0.6042 | 0.3333 | 4 | aggregation_failure:23; container_affordance_miss:23; parse_failure:18; helper_search_failure:5; helper_mention_without_use:4 |
| efficient_safe_free_plan_quadruped_single_arm | 66 | 16 | 31 | 0 | 19 | 0 | 0.6596 | 0.3191 | 4 | aggregation_failure:23; container_affordance_miss:23; parse_failure:19; helper_search_failure:4; helper_mention_without_use:4 |
| natural_free_plan | 66 | 16 | 34 | 0 | 16 | 0 | 0.68 | 0.28 | 9 | aggregation_failure:22; container_affordance_miss:22; parse_failure:16; helper_mention_without_use:9; visual_uncertainty:9 |
| natural_free_plan_humanoid_dual_arm | 66 | 16 | 37 | 0 | 13 | 0 | 0.6981 | 0.2453 | 9 | aggregation_failure:26; container_affordance_miss:26; parse_failure:13; helper_mention_without_use:9; visual_uncertainty:9 |
| natural_free_plan_quadruped_single_arm | 66 | 17 | 32 | 0 | 17 | 0 | 0.6531 | 0.2653 | 7 | aggregation_failure:24; container_affordance_miss:24; parse_failure:17; helper_mention_without_use:7; visual_uncertainty:7 |
| structured_tool_action_chain_probe_humanoid_dual_arm | 66 | 21 | 30 | 0 | 15 | 0 | 0.5882 | 0.4118 | 0 | helper_mention_without_use:25; parse_failure:15; helper_search_failure:4; wrong_helper_type:4; field_plan_inconsistency:3 |
| structured_tool_action_chain_probe_quadruped_single_arm | 66 | 19 | 33 | 2 | 12 | 0 | 0.6111 | 0.3704 | 0 | helper_mention_without_use:27; parse_failure:14; helper_search_failure:4; wrong_helper_type:3; tool_necessity_miss:2 |
| structured_tool_probe | 66 | 19 | 33 | 0 | 14 | 0 | 0.6346 | 0.3462 | 0 | helper_mention_without_use:29; parse_failure:14; helper_search_failure:4; wrong_helper_type:3; field_plan_inconsistency:3 |
| tool_prior_free_plan | 66 | 16 | 37 | 0 | 13 | 0 | 0.6981 | 0.3019 | 31 | helper_mention_without_use:31; visual_uncertainty:31; parse_failure:13; tool_necessity_miss:7; helper_search_failure:4 |
| tool_prior_free_plan_humanoid_dual_arm | 66 | 17 | 32 | 0 | 17 | 0 | 0.6531 | 0.3673 | 14 | parse_failure:17; helper_mention_without_use:14; visual_uncertainty:14; aggregation_failure:12; container_affordance_miss:12 |
| tool_prior_free_plan_quadruped_single_arm | 66 | 16 | 30 | 0 | 20 | 0 | 0.6522 | 0.3261 | 14 | parse_failure:20; helper_mention_without_use:14; visual_uncertainty:14; aggregation_failure:12; container_affordance_miss:12 |

## By model

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ollama_gemma3_27b_it_q8_0 | 132 | 41 | 91 | 0 | 0 | 0 | 0.6894 | 0.2576 | 24 | helper_mention_without_use:46; aggregation_failure:40; container_affordance_miss:40; visual_uncertainty:24; helper_search_failure:12 |
| ollama_llama3_2_vision_11b_instruct_q8_0 | 132 | 0 | 0 | 0 | 132 | 0 | 0 | 0 | 0 | parse_failure:132 |
| ollama_minicpm_v4_5_q8_0 | 132 | 41 | 89 | 2 | 0 | 0 | 0.6742 | 0.2955 | 23 | helper_mention_without_use:41; aggregation_failure:38; container_affordance_miss:38; visual_uncertainty:23; wrong_helper_type:10 |
| ollama_qwen3_5_35b | 132 | 27 | 46 | 0 | 59 | 0 | 0.6301 | 0.3288 | 18 | parse_failure:59; helper_mention_without_use:29; visual_uncertainty:18; aggregation_failure:8; container_affordance_miss:8 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 132 | 48 | 84 | 0 | 0 | 0 | 0.6364 | 0.3409 | 15 | aggregation_failure:42; container_affordance_miss:42; helper_mention_without_use:33; visual_uncertainty:15; helper_search_failure:12 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 132 | 50 | 82 | 0 | 0 | 0 | 0.6212 | 0.3864 | 18 | aggregation_failure:39; container_affordance_miss:39; helper_mention_without_use:30; visual_uncertainty:18; helper_search_failure:12 |

## By task

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| task_001 | 72 | 3 | 53 | 0 | 16 | 0 | 0.9464 | 0.0714 | 12 | aggregation_failure:28; container_affordance_miss:28; helper_mention_without_use:24; parse_failure:16; visual_uncertainty:12 |
| task_002 | 72 | 2 | 54 | 1 | 15 | 0 | 0.9474 | 0.0702 | 7 | helper_search_failure:50; aggregation_failure:33; container_affordance_miss:33; helper_mention_without_use:19; parse_failure:16 |
| task_003 | 72 | 50 | 3 | 1 | 18 | 0 | 0.0556 | 0.9259 | 3 | parse_failure:19; helper_mention_without_use:3; visual_uncertainty:3 |
| task_004 | 72 | 1 | 52 | 0 | 19 | 0 | 0.9811 | 0.0189 | 9 | aggregation_failure:29; container_affordance_miss:29; helper_mention_without_use:23; parse_failure:19; visual_uncertainty:9 |
| task_005 | 72 | 4 | 48 | 0 | 20 | 0 | 0.9231 | 0.0769 | 10 | aggregation_failure:24; container_affordance_miss:24; helper_mention_without_use:24; parse_failure:20; visual_uncertainty:10 |
| task_006 | 72 | 5 | 50 | 0 | 17 | 0 | 0.9091 | 0.6364 | 12 | wrong_helper_type:30; parse_failure:17; helper_mention_without_use:16; visual_uncertainty:12; aggregation_failure:4 |
| task_007 | 72 | 10 | 40 | 0 | 22 | 0 | 0.8 | 0.2 | 16 | helper_mention_without_use:22; parse_failure:22; aggregation_failure:18; container_affordance_miss:18; visual_uncertainty:16 |
| task_008 | 72 | 10 | 48 | 0 | 14 | 0 | 0.8276 | 0.2759 | 12 | helper_mention_without_use:22; aggregation_failure:20; container_affordance_miss:20; parse_failure:14; visual_uncertainty:12 |
| task_009 | 72 | 31 | 23 | 0 | 18 | 0 | 0.4259 | 0.6667 | 6 | parse_failure:18; helper_mention_without_use:10; aggregation_failure:8; container_affordance_miss:8; visual_uncertainty:6 |
| task_010 | 72 | 31 | 21 | 0 | 20 | 0 | 0.4038 | 0.6346 | 11 | parse_failure:20; helper_mention_without_use:16; visual_uncertainty:11; aggregation_failure:3; container_affordance_miss:3 |
| task_011 | 72 | 60 | 0 | 0 | 12 | 0 | 0.0 | 0.0 | 0 | parse_failure:12 |

## By embodiment

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| generic | 264 | 66 | 138 | 0 | 60 | 0 | 0.6765 | 0.3039 | 46 | helper_mention_without_use:75; parse_failure:60; aggregation_failure:47; container_affordance_miss:47; visual_uncertainty:46 |
| humanoid_dual_arm | 264 | 73 | 128 | 0 | 63 | 0 | 0.6368 | 0.3383 | 27 | parse_failure:63; aggregation_failure:61; container_affordance_miss:61; helper_mention_without_use:52; visual_uncertainty:27 |
| quadruped_single_arm | 264 | 68 | 126 | 2 | 68 | 0 | 0.6429 | 0.3214 | 25 | parse_failure:70; aggregation_failure:59; container_affordance_miss:59; helper_mention_without_use:52; visual_uncertainty:25 |

