# Aggregate Findings

Text-based rereview summary. This is not final paper evidence.

Warnings:
- This is text-based rereview; image-visible helper verification is not performed.
- Strong decomposition prompt may have label noise; see `label_inconsistency_audit.md` when available.
- Parse failures are separate from planning failures.

## Context usage warnings

- High risk rows: 0
- Medium risk rows: 0
- Unknown risk rows: 198
- Rows with negative prompt+generation headroom: 198

### Highest context usage ratio top 10

| Task | Model | Prompt | Usage ratio | Prompt eval | Num ctx | Headroom after prompt+generation | Risk |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| task_009 | ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | 0.502197 | 4114 | 8192 | 2542 | low |
| task_010 | ollama_qwen3_5_35b | strong_decomposition_free_plan_humanoid_dual_arm | 0.496338 | 4066 | 8192 | 2590 | low |
| task_006 | ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan | 0.494995 | 4055 | 8192 | 2601 | low |
| task_005 | ollama_qwen3_5_35b | strong_decomposition_free_plan_humanoid_dual_arm | 0.493164 | 4040 | 8192 | 2616 | low |
| task_002 | ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan | 0.488159 | 3999 | 8192 | 2657 | low |
| task_003 | ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | 0.481689 | 3946 | 8192 | 2710 | low |
| task_002 | ollama_qwen3_5_35b | strong_decomposition_free_plan | 0.477905 | 3915 | 8192 | 2741 | low |
| task_003 | ollama_qwen3_5_35b | strong_decomposition_free_plan | 0.474365 | 3886 | 8192 | 2770 | low |
| task_007 | ollama_qwen3_5_35b | efficient_safe_free_plan_quadruped_single_arm | 0.473877 | 3882 | 8192 | 2774 | low |
| task_006 | ollama_qwen3_5_35b | tool_prior_free_plan | 0.471924 | 3866 | 8192 | 2790 | low |

### Prompt eval count by model

| Name | Rows with prompt eval | Avg prompt eval | Max prompt eval |
| --- | ---: | ---: | ---: |
| ollama_gemma3_27b_it_q8_0 | 198 | 659.11 | 921 |
| ollama_minicpm_v4_5_q8_0 | 198 | 997.25 | 1261 |
| ollama_qwen3_5_35b | 198 | 2951.6 | 4114 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 198 | 2388.7 | 2718 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 198 | 2388.7 | 2718 |

### Prompt eval count by prompt

| Name | Rows with prompt eval | Avg prompt eval | Max prompt eval |
| --- | ---: | ---: | ---: |
| efficient_safe_free_plan | 55 | 1717.78 | 3554 |
| efficient_safe_free_plan_humanoid_dual_arm | 55 | 1771.45 | 3737 |
| efficient_safe_free_plan_quadruped_single_arm | 55 | 1783.64 | 3882 |
| natural_free_plan | 55 | 1759.73 | 3643 |
| natural_free_plan_humanoid_dual_arm | 55 | 1810.36 | 3838 |
| natural_free_plan_quadruped_single_arm | 55 | 1752.11 | 3706 |
| search_explicit_strong_decomposition_free_plan | 55 | 2058.25 | 4055 |
| search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | 55 | 2121.44 | 4114 |
| search_explicit_strong_decomposition_free_plan_quadruped_single_arm | 55 | 2090.6 | 3767 |
| strong_decomposition_free_plan | 55 | 1983.95 | 3915 |
| strong_decomposition_free_plan_humanoid_dual_arm | 55 | 2028.02 | 4066 |
| strong_decomposition_free_plan_quadruped_single_arm | 55 | 1975.45 | 3845 |
| structured_tool_action_chain_probe_humanoid_dual_arm | 55 | 1868.47 | 3067 |
| structured_tool_action_chain_probe_quadruped_single_arm | 55 | 1918.71 | 3804 |
| structured_tool_probe | 55 | 1793.8 | 3796 |
| tool_prior_free_plan | 55 | 1818.75 | 3866 |
| tool_prior_free_plan_humanoid_dual_arm | 55 | 1769.35 | 3594 |
| tool_prior_free_plan_quadruped_single_arm | 55 | 1765.44 | 3231 |

## By prompt category

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| diagnostic_probe | 198 | 92 | 65 | 0 | 41 | 0 | 0.414 | 0.5096 | 0 | helper_mention_without_use:62; parse_failure:41; helper_search_failure:14; physical_capacity_hallucination:4; field_plan_inconsistency:4 |
| embodiment_clean | 264 | 97 | 105 | 0 | 62 | 0 | 0.5198 | 0.396 | 28 | aggregation_failure:74; container_affordance_miss:74; parse_failure:62; helper_mention_without_use:29; visual_uncertainty:28 |
| generic_clean | 132 | 55 | 49 | 0 | 28 | 0 | 0.4712 | 0.4327 | 17 | aggregation_failure:32; container_affordance_miss:32; parse_failure:28; helper_mention_without_use:17; visual_uncertainty:17 |
| search_explicit_strong_decomposition_intervention | 198 | 104 | 48 | 0 | 46 | 0 | 0.3158 | 0.5921 | 44 | parse_failure:46; helper_mention_without_use:45; visual_uncertainty:44; tool_necessity_miss:18; helper_search_failure:10 |
| strong_decomposition_intervention | 198 | 96 | 58 | 0 | 44 | 0 | 0.3766 | 0.5455 | 48 | helper_mention_without_use:50; visual_uncertainty:48; parse_failure:44; tool_necessity_miss:22; helper_search_failure:14 |
| tool_prior_intervention | 198 | 85 | 61 | 0 | 52 | 0 | 0.4178 | 0.4863 | 42 | parse_failure:52; helper_mention_without_use:43; visual_uncertainty:42; aggregation_failure:18; container_affordance_miss:18 |

## By prompt ID

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| efficient_safe_free_plan | 66 | 24 | 27 | 0 | 15 | 0 | 0.5294 | 0.3725 | 11 | aggregation_failure:16; container_affordance_miss:16; parse_failure:15; helper_mention_without_use:11; visual_uncertainty:11 |
| efficient_safe_free_plan_humanoid_dual_arm | 66 | 26 | 24 | 0 | 16 | 0 | 0.48 | 0.42 | 6 | aggregation_failure:18; container_affordance_miss:18; parse_failure:16; helper_mention_without_use:6; visual_uncertainty:6 |
| efficient_safe_free_plan_quadruped_single_arm | 66 | 26 | 23 | 0 | 17 | 0 | 0.4694 | 0.449 | 4 | aggregation_failure:18; container_affordance_miss:18; parse_failure:17; helper_mention_without_use:4; visual_uncertainty:4 |
| natural_free_plan | 66 | 31 | 22 | 0 | 13 | 0 | 0.4151 | 0.4906 | 6 | aggregation_failure:16; container_affordance_miss:16; parse_failure:13; helper_mention_without_use:6; visual_uncertainty:6 |
| natural_free_plan_humanoid_dual_arm | 66 | 25 | 28 | 0 | 13 | 0 | 0.5283 | 0.3962 | 11 | aggregation_failure:16; container_affordance_miss:16; parse_failure:13; helper_mention_without_use:11; visual_uncertainty:11 |
| natural_free_plan_quadruped_single_arm | 66 | 20 | 30 | 0 | 16 | 0 | 0.6 | 0.32 | 7 | aggregation_failure:22; container_affordance_miss:22; parse_failure:16; helper_mention_without_use:8; visual_uncertainty:7 |
| search_explicit_strong_decomposition_free_plan | 66 | 39 | 12 | 0 | 15 | 0 | 0.2353 | 0.6667 | 12 | parse_failure:15; helper_mention_without_use:12; visual_uncertainty:12; helper_search_failure:4; tool_necessity_miss:4 |
| search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | 66 | 35 | 17 | 0 | 14 | 0 | 0.3269 | 0.5962 | 15 | helper_mention_without_use:16; visual_uncertainty:15; parse_failure:14; tool_necessity_miss:6; helper_search_failure:4 |
| search_explicit_strong_decomposition_free_plan_quadruped_single_arm | 66 | 30 | 19 | 0 | 17 | 0 | 0.3878 | 0.5102 | 17 | helper_mention_without_use:17; visual_uncertainty:17; parse_failure:17; tool_necessity_miss:8; helper_search_failure:2 |
| strong_decomposition_free_plan | 66 | 34 | 19 | 0 | 13 | 0 | 0.3585 | 0.5472 | 18 | helper_mention_without_use:18; visual_uncertainty:18; parse_failure:13; tool_necessity_miss:7; helper_search_failure:5 |
| strong_decomposition_free_plan_humanoid_dual_arm | 66 | 29 | 23 | 0 | 14 | 0 | 0.4423 | 0.5192 | 18 | helper_mention_without_use:20; visual_uncertainty:18; parse_failure:14; tool_necessity_miss:8; helper_search_failure:5 |
| strong_decomposition_free_plan_quadruped_single_arm | 66 | 33 | 16 | 0 | 17 | 0 | 0.3265 | 0.5714 | 12 | parse_failure:17; helper_mention_without_use:12; visual_uncertainty:12; tool_necessity_miss:7; aggregation_failure:4 |
| structured_tool_action_chain_probe_humanoid_dual_arm | 66 | 30 | 22 | 0 | 14 | 0 | 0.4231 | 0.5 | 0 | helper_mention_without_use:21; parse_failure:14; helper_search_failure:5; field_plan_inconsistency:2; physical_capacity_hallucination:1 |
| structured_tool_action_chain_probe_quadruped_single_arm | 66 | 28 | 26 | 0 | 12 | 0 | 0.4815 | 0.4444 | 0 | helper_mention_without_use:25; parse_failure:12; helper_search_failure:5; field_plan_inconsistency:2; physical_capacity_hallucination:1 |
| structured_tool_probe | 66 | 34 | 17 | 0 | 15 | 0 | 0.3333 | 0.5882 | 0 | helper_mention_without_use:16; parse_failure:15; helper_search_failure:4; physical_capacity_hallucination:2; wrong_helper_type:1 |
| tool_prior_free_plan | 66 | 34 | 19 | 0 | 13 | 0 | 0.3585 | 0.5472 | 16 | helper_mention_without_use:16; visual_uncertainty:16; parse_failure:13; tool_necessity_miss:6; helper_search_failure:5 |
| tool_prior_free_plan_humanoid_dual_arm | 66 | 28 | 19 | 0 | 19 | 0 | 0.4043 | 0.5106 | 9 | parse_failure:19; helper_mention_without_use:10; aggregation_failure:9; container_affordance_miss:9; visual_uncertainty:9 |
| tool_prior_free_plan_quadruped_single_arm | 66 | 23 | 23 | 0 | 20 | 0 | 0.5 | 0.3913 | 17 | parse_failure:20; helper_mention_without_use:17; visual_uncertainty:17; tool_necessity_miss:7; aggregation_failure:6 |

## By model

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ollama_gemma3_27b_it_q8_0 | 198 | 94 | 104 | 0 | 0 | 0 | 0.5253 | 0.3838 | 47 | helper_mention_without_use:65; visual_uncertainty:47; aggregation_failure:39; container_affordance_miss:39; tool_necessity_miss:27 |
| ollama_llama3_2_vision_11b_instruct_q8_0 | 198 | 0 | 0 | 0 | 198 | 0 | 0 | 0 | 0 | parse_failure:198 |
| ollama_minicpm_v4_5_q8_0 | 198 | 104 | 94 | 0 | 0 | 0 | 0.4747 | 0.4596 | 41 | helper_mention_without_use:58; visual_uncertainty:41; aggregation_failure:33; container_affordance_miss:33; tool_necessity_miss:19 |
| ollama_qwen3_5_35b | 198 | 79 | 44 | 0 | 75 | 0 | 0.3577 | 0.5203 | 26 | parse_failure:75; helper_mention_without_use:36; visual_uncertainty:26; helper_search_failure:11; aggregation_failure:7 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 198 | 117 | 81 | 0 | 0 | 0 | 0.4091 | 0.5 | 37 | helper_mention_without_use:49; visual_uncertainty:37; aggregation_failure:32; container_affordance_miss:32; helper_search_failure:18 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 198 | 135 | 63 | 0 | 0 | 0 | 0.3182 | 0.6061 | 28 | helper_mention_without_use:38; visual_uncertainty:28; aggregation_failure:23; container_affordance_miss:23; helper_search_failure:16 |

## By task

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| task_001 | 108 | 16 | 69 | 0 | 23 | 0 | 0.8118 | 0.1882 | 29 | helper_mention_without_use:39; aggregation_failure:30; container_affordance_miss:30; visual_uncertainty:29; parse_failure:23 |
| task_002 | 108 | 8 | 77 | 0 | 23 | 0 | 0.9059 | 0.0941 | 32 | helper_search_failure:77; helper_mention_without_use:46; visual_uncertainty:32; aggregation_failure:31; container_affordance_miss:31 |
| task_003 | 108 | 74 | 6 | 0 | 28 | 0 | 0.075 | 0.925 | 6 | parse_failure:28; helper_mention_without_use:6; visual_uncertainty:6; tool_necessity_miss:1 |
| task_004 | 108 | 16 | 65 | 0 | 27 | 0 | 0.8025 | 0.1975 | 22 | helper_mention_without_use:34; aggregation_failure:31; container_affordance_miss:31; parse_failure:27; visual_uncertainty:22 |
| task_005 | 108 | 44 | 34 | 0 | 30 | 0 | 0.4359 | 0.5641 | 22 | parse_failure:30; helper_mention_without_use:26; visual_uncertainty:22; aggregation_failure:8; container_affordance_miss:8 |
| task_006 | 108 | 70 | 14 | 0 | 24 | 0 | 0.1667 | 0.8333 | 9 | parse_failure:24; helper_mention_without_use:11; visual_uncertainty:9; tool_necessity_miss:4; aggregation_failure:3 |
| task_007 | 108 | 66 | 19 | 0 | 23 | 0 | 0.2235 | 0.7765 | 16 | parse_failure:23; helper_mention_without_use:18; visual_uncertainty:16; tool_necessity_miss:6; physical_capacity_hallucination:1 |
| task_008 | 108 | 38 | 49 | 0 | 21 | 0 | 0.5632 | 0.4368 | 22 | helper_mention_without_use:33; visual_uncertainty:22; parse_failure:21; aggregation_failure:16; container_affordance_miss:16 |
| task_009 | 108 | 53 | 29 | 0 | 26 | 0 | 0.3537 | 0.7195 | 9 | parse_failure:26; helper_mention_without_use:12; aggregation_failure:11; container_affordance_miss:11; visual_uncertainty:9 |
| task_010 | 108 | 59 | 19 | 0 | 30 | 0 | 0.2436 | 0.7564 | 12 | parse_failure:30; helper_mention_without_use:16; visual_uncertainty:12; aggregation_failure:3; container_affordance_miss:3 |
| task_011 | 108 | 85 | 5 | 0 | 18 | 0 | 0.0556 | 0.0 | 0 | parse_failure:18; helper_mention_without_use:5 |

## By embodiment

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| generic | 396 | 196 | 116 | 0 | 84 | 0 | 0.3718 | 0.5353 | 63 | parse_failure:84; helper_mention_without_use:79; visual_uncertainty:63; aggregation_failure:36; container_affordance_miss:36 |
| humanoid_dual_arm | 396 | 173 | 133 | 0 | 90 | 0 | 0.4346 | 0.4902 | 59 | parse_failure:90; helper_mention_without_use:84; visual_uncertainty:59; aggregation_failure:46; container_affordance_miss:46 |
| quadruped_single_arm | 396 | 160 | 137 | 0 | 99 | 0 | 0.4613 | 0.4478 | 57 | parse_failure:99; helper_mention_without_use:83; visual_uncertainty:57; aggregation_failure:52; container_affordance_miss:52 |

