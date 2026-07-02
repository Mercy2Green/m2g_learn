# Aggregate Findings

Text-based rereview summary. This is not final paper evidence.

Warnings:
- This is text-based rereview; image-visible helper verification is not performed.
- Strong decomposition prompt may have label noise; see `label_inconsistency_audit.md` when available.
- Parse failures are separate from planning failures.

## By prompt category

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| strong_decomposition_intervention | 198 | 97 | 55 | 0 | 46 | 0 | 0.3618 | 0.5526 | 49 | helper_mention_without_use:51; visual_uncertainty:49; parse_failure:46; helper_search_failure:14; tool_necessity_miss:14 |

## By prompt ID

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| strong_decomposition_free_plan | 66 | 31 | 20 | 0 | 15 | 0 | 0.3922 | 0.5098 | 18 | helper_mention_without_use:18; visual_uncertainty:18; parse_failure:15; tool_necessity_miss:7; helper_search_failure:5 |
| strong_decomposition_free_plan_humanoid_dual_arm | 66 | 33 | 18 | 0 | 15 | 0 | 0.3529 | 0.5882 | 16 | helper_mention_without_use:18; visual_uncertainty:16; parse_failure:15; helper_search_failure:4; tool_necessity_miss:3 |
| strong_decomposition_free_plan_quadruped_single_arm | 66 | 33 | 17 | 0 | 16 | 0 | 0.34 | 0.56 | 15 | parse_failure:16; helper_mention_without_use:15; visual_uncertainty:15; helper_search_failure:5; tool_necessity_miss:4 |

## By model

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ollama_gemma3_27b_it_q8_0 | 33 | 21 | 12 | 0 | 0 | 0 | 0.3636 | 0.5455 | 9 | helper_mention_without_use:9; visual_uncertainty:9; tool_necessity_miss:7; aggregation_failure:3; container_affordance_miss:3 |
| ollama_llama3_2_vision_11b_instruct_q8_0 | 33 | 0 | 0 | 0 | 33 | 0 | 0 | 0 | 0 | parse_failure:33 |
| ollama_minicpm_v4_5_q8_0 | 33 | 19 | 14 | 0 | 0 | 0 | 0.4242 | 0.5152 | 12 | helper_mention_without_use:13; visual_uncertainty:12; tool_necessity_miss:3; helper_search_failure:2; aggregation_failure:1 |
| ollama_qwen3_5_35b | 33 | 13 | 7 | 0 | 13 | 0 | 0.35 | 0.55 | 6 | parse_failure:13; helper_mention_without_use:7; visual_uncertainty:6; helper_search_failure:3; tool_necessity_miss:1 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 33 | 19 | 14 | 0 | 0 | 0 | 0.4242 | 0.4848 | 14 | helper_mention_without_use:14; visual_uncertainty:14; helper_search_failure:3 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 33 | 25 | 8 | 0 | 0 | 0 | 0.2424 | 0.6667 | 8 | helper_mention_without_use:8; visual_uncertainty:8; helper_search_failure:3; tool_necessity_miss:3 |

## By task

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| task_001 | 18 | 4 | 11 | 0 | 3 | 0 | 0.7333 | 0.2667 | 9 | helper_mention_without_use:9; visual_uncertainty:9; parse_failure:3; aggregation_failure:2; container_affordance_miss:2 |
| task_002 | 18 | 1 | 14 | 0 | 3 | 0 | 0.9333 | 0.0667 | 14 | helper_mention_without_use:14; helper_search_failure:14; visual_uncertainty:14; tool_necessity_miss:4; parse_failure:3 |
| task_003 | 18 | 13 | 0 | 0 | 5 | 0 | 0.0 | 1.0 | 0 | parse_failure:5 |
| task_004 | 18 | 6 | 8 | 0 | 4 | 0 | 0.5714 | 0.4286 | 8 | helper_mention_without_use:8; visual_uncertainty:8; parse_failure:4; tool_necessity_miss:3 |
| task_005 | 18 | 9 | 4 | 0 | 5 | 0 | 0.3077 | 0.6923 | 4 | parse_failure:5; helper_mention_without_use:4; visual_uncertainty:4 |
| task_006 | 18 | 11 | 3 | 0 | 4 | 0 | 0.2143 | 0.7857 | 2 | parse_failure:4; helper_mention_without_use:2; visual_uncertainty:2; aggregation_failure:1; container_affordance_miss:1 |
| task_007 | 18 | 13 | 2 | 0 | 3 | 0 | 0.1333 | 0.8667 | 2 | parse_failure:3; helper_mention_without_use:2; visual_uncertainty:2; physical_capacity_hallucination:1 |
| task_008 | 18 | 9 | 4 | 0 | 5 | 0 | 0.3077 | 0.6923 | 4 | parse_failure:5; helper_mention_without_use:4; visual_uncertainty:4; tool_necessity_miss:1 |
| task_009 | 18 | 9 | 4 | 0 | 5 | 0 | 0.3077 | 0.6923 | 3 | parse_failure:5; helper_mention_without_use:3; tool_necessity_miss:3; visual_uncertainty:3; aggregation_failure:1 |
| task_010 | 18 | 9 | 3 | 0 | 6 | 0 | 0.25 | 0.75 | 3 | parse_failure:6; helper_mention_without_use:3; visual_uncertainty:3 |
| task_011 | 18 | 13 | 2 | 0 | 3 | 0 | 0.1333 | 0.0 | 0 | parse_failure:3; helper_mention_without_use:2 |

## By embodiment

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| generic | 66 | 31 | 20 | 0 | 15 | 0 | 0.3922 | 0.5098 | 18 | helper_mention_without_use:18; visual_uncertainty:18; parse_failure:15; tool_necessity_miss:7; helper_search_failure:5 |
| humanoid_dual_arm | 66 | 33 | 18 | 0 | 15 | 0 | 0.3529 | 0.5882 | 16 | helper_mention_without_use:18; visual_uncertainty:16; parse_failure:15; helper_search_failure:4; tool_necessity_miss:3 |
| quadruped_single_arm | 66 | 33 | 17 | 0 | 16 | 0 | 0.34 | 0.56 | 15 | parse_failure:16; helper_mention_without_use:15; visual_uncertainty:15; helper_search_failure:5; tool_necessity_miss:4 |

