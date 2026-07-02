# Aggregate Findings

Text-based rereview summary. This is not final paper evidence.

## By prompt category

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| strong_decomposition_intervention | 198 | 73 | 79 | 0 | 46 | 0 | 0.5197 | 0.4934 | 58 | helper_mention_without_use:58; visual_uncertainty:58; parse_failure:46; tool_necessity_miss:17; helper_search_failure:10 |

## By prompt ID

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| strong_decomposition_free_plan | 66 | 23 | 28 | 0 | 15 | 0 | 0.549 | 0.451 | 21 | helper_mention_without_use:21; visual_uncertainty:21; parse_failure:15; tool_necessity_miss:8; helper_search_failure:3 |
| strong_decomposition_free_plan_humanoid_dual_arm | 66 | 26 | 25 | 0 | 15 | 0 | 0.4902 | 0.549 | 18 | helper_mention_without_use:18; visual_uncertainty:18; parse_failure:15; helper_search_failure:4; tool_necessity_miss:3 |
| strong_decomposition_free_plan_quadruped_single_arm | 66 | 24 | 26 | 0 | 16 | 0 | 0.52 | 0.48 | 19 | helper_mention_without_use:19; visual_uncertainty:19; parse_failure:16; tool_necessity_miss:6; helper_search_failure:3 |

## By model

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ollama_gemma3_27b_it_q8_0 | 33 | 16 | 17 | 0 | 0 | 0 | 0.5152 | 0.4848 | 11 | helper_mention_without_use:11; visual_uncertainty:11; tool_necessity_miss:9; aggregation_failure:3; container_affordance_miss:3 |
| ollama_llama3_2_vision_11b_instruct_q8_0 | 33 | 0 | 0 | 0 | 33 | 0 | 0 | 0 | 0 | parse_failure:33 |
| ollama_minicpm_v4_5_q8_0 | 33 | 13 | 20 | 0 | 0 | 0 | 0.6061 | 0.4242 | 15 | helper_mention_without_use:15; visual_uncertainty:15; tool_necessity_miss:3; aggregation_failure:1; container_affordance_miss:1 |
| ollama_qwen3_5_35b | 33 | 13 | 7 | 0 | 13 | 0 | 0.35 | 0.55 | 6 | parse_failure:13; helper_mention_without_use:6; visual_uncertainty:6; helper_search_failure:2; tool_necessity_miss:1 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 33 | 16 | 17 | 0 | 0 | 0 | 0.5152 | 0.4545 | 15 | helper_mention_without_use:15; visual_uncertainty:15; helper_search_failure:3 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 33 | 15 | 18 | 0 | 0 | 0 | 0.5455 | 0.5758 | 11 | helper_mention_without_use:11; visual_uncertainty:11; tool_necessity_miss:4; helper_search_failure:2 |

## By task

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| task_001 | 18 | 4 | 11 | 0 | 3 | 0 | 0.7333 | 0.2667 | 9 | helper_mention_without_use:9; visual_uncertainty:9; parse_failure:3; aggregation_failure:2; container_affordance_miss:2 |
| task_002 | 18 | 1 | 14 | 0 | 3 | 0 | 0.9333 | 0.0667 | 14 | helper_mention_without_use:14; visual_uncertainty:14; helper_search_failure:10; tool_necessity_miss:4; parse_failure:3 |
| task_003 | 18 | 11 | 2 | 0 | 5 | 0 | 0.1538 | 1.0 | 0 | parse_failure:5 |
| task_004 | 18 | 3 | 11 | 0 | 4 | 0 | 0.7857 | 0.3571 | 9 | helper_mention_without_use:9; visual_uncertainty:9; parse_failure:4; tool_necessity_miss:3 |
| task_005 | 18 | 3 | 10 | 0 | 5 | 0 | 0.7692 | 0.5385 | 6 | helper_mention_without_use:6; visual_uncertainty:6; parse_failure:5; tool_necessity_miss:2 |
| task_006 | 18 | 7 | 7 | 0 | 4 | 0 | 0.5 | 0.7857 | 2 | parse_failure:4; helper_mention_without_use:2; visual_uncertainty:2; aggregation_failure:1; container_affordance_miss:1 |
| task_007 | 18 | 6 | 9 | 0 | 3 | 0 | 0.6 | 0.4667 | 8 | helper_mention_without_use:8; visual_uncertainty:8; parse_failure:3; physical_capacity_hallucination:1; tool_necessity_miss:1 |
| task_008 | 18 | 7 | 6 | 0 | 5 | 0 | 0.4615 | 0.6923 | 4 | parse_failure:5; helper_mention_without_use:4; visual_uncertainty:4; tool_necessity_miss:1 |
| task_009 | 18 | 9 | 4 | 0 | 5 | 0 | 0.3077 | 0.6923 | 3 | parse_failure:5; helper_mention_without_use:3; tool_necessity_miss:3; visual_uncertainty:3; aggregation_failure:1 |
| task_010 | 18 | 7 | 5 | 0 | 6 | 0 | 0.4167 | 0.75 | 3 | parse_failure:6; helper_mention_without_use:3; visual_uncertainty:3 |
| task_011 | 18 | 15 | 0 | 0 | 3 | 0 | 0.0 | 0.0 | 0 | parse_failure:3 |

## By embodiment

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| generic | 66 | 23 | 28 | 0 | 15 | 0 | 0.549 | 0.451 | 21 | helper_mention_without_use:21; visual_uncertainty:21; parse_failure:15; tool_necessity_miss:8; helper_search_failure:3 |
| humanoid_dual_arm | 66 | 26 | 25 | 0 | 15 | 0 | 0.4902 | 0.549 | 18 | helper_mention_without_use:18; visual_uncertainty:18; parse_failure:15; helper_search_failure:4; tool_necessity_miss:3 |
| quadruped_single_arm | 66 | 24 | 26 | 0 | 16 | 0 | 0.52 | 0.48 | 19 | helper_mention_without_use:19; visual_uncertainty:19; parse_failure:16; tool_necessity_miss:6; helper_search_failure:3 |

