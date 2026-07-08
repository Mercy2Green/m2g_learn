# Aggregate Findings

Text-based rereview summary. This is not final paper evidence.

Warnings:
- This is text-based rereview; image-visible helper verification is not performed.
- Strong decomposition prompt may have label noise; see `label_inconsistency_audit.md` when available.
- Parse failures are separate from planning failures.

## Context usage warnings

- High risk rows: 0
- Medium risk rows: 0
- Unknown risk rows: 0
- Rows with negative prompt+generation headroom: 0

### Highest context usage ratio top 10

| Task | Model | Prompt | Usage ratio | Prompt eval | Num ctx | Headroom after prompt+generation | Risk |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| task_002 | ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | 0.519531 | 4256 | 8192 | 2400 | low |
| task_007 | ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | 0.517456 | 4239 | 8192 | 2417 | low |
| task_002 | ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | 0.51709 | 4236 | 8192 | 2420 | low |
| task_006 | ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | 0.516113 | 4228 | 8192 | 2428 | low |
| task_003 | ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | 0.515991 | 4227 | 8192 | 2429 | low |
| task_005 | ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | 0.514771 | 4217 | 8192 | 2439 | low |
| task_001 | ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | 0.514648 | 4216 | 8192 | 2440 | low |
| task_005 | ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | 0.513062 | 4203 | 8192 | 2453 | low |
| task_002 | ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | 0.510986 | 4186 | 8192 | 2470 | low |
| task_002 | ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | 0.510376 | 4181 | 8192 | 2475 | low |

### Prompt eval count by model

| Name | Rows with prompt eval | Avg prompt eval | Max prompt eval |
| --- | ---: | ---: | ---: |
| ollama_qwen3_5_35b | 1980 | 2977.7 | 4256 |

### Prompt eval count by prompt

| Name | Rows with prompt eval | Avg prompt eval | Max prompt eval |
| --- | ---: | ---: | ---: |
| efficient_safe_free_plan | 110 | 2864.56 | 3826 |
| efficient_safe_free_plan_humanoid_dual_arm | 110 | 2742.32 | 3913 |
| efficient_safe_free_plan_quadruped_single_arm | 110 | 2570.63 | 3931 |
| natural_free_plan | 110 | 2948.4 | 3836 |
| natural_free_plan_humanoid_dual_arm | 110 | 2903.9 | 3893 |
| natural_free_plan_quadruped_single_arm | 110 | 2758.08 | 3853 |
| search_explicit_strong_decomposition_free_plan | 110 | 3349.77 | 4110 |
| search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | 110 | 3272.15 | 4239 |
| search_explicit_strong_decomposition_free_plan_quadruped_single_arm | 110 | 3208.91 | 4256 |
| strong_decomposition_free_plan | 110 | 3233.66 | 4057 |
| strong_decomposition_free_plan_humanoid_dual_arm | 110 | 3042.7 | 4096 |
| strong_decomposition_free_plan_quadruped_single_arm | 110 | 3140.67 | 4137 |
| structured_tool_action_chain_probe_humanoid_dual_arm | 110 | 2867.53 | 3893 |
| structured_tool_action_chain_probe_quadruped_single_arm | 110 | 3016.5 | 4053 |
| structured_tool_probe | 110 | 2828.95 | 3986 |
| tool_prior_free_plan | 110 | 3144.96 | 3891 |
| tool_prior_free_plan_humanoid_dual_arm | 110 | 2978.81 | 3950 |
| tool_prior_free_plan_quadruped_single_arm | 110 | 2726.02 | 3995 |

## By prompt category

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| diagnostic_probe | 330 | 177 | 89 | 0 | 64 | 0 | 0.3346 | 0.5526 | 0 | helper_mention_without_use:89; parse_failure:64; helper_search_failure:12; field_plan_inconsistency:12; tool_necessity_miss:9 |
| embodiment_clean | 440 | 115 | 117 | 0 | 208 | 0 | 0.5043 | 0.3319 | 61 | parse_failure:208; helper_mention_without_use:61; visual_uncertainty:61; aggregation_failure:54; container_affordance_miss:54 |
| generic_clean | 220 | 80 | 67 | 0 | 73 | 0 | 0.4558 | 0.4082 | 46 | parse_failure:73; helper_mention_without_use:46; visual_uncertainty:46; aggregation_failure:21; container_affordance_miss:21 |
| search_explicit_strong_decomposition_intervention | 330 | 192 | 34 | 0 | 104 | 0 | 0.1504 | 0.7301 | 31 | parse_failure:104; helper_mention_without_use:32; visual_uncertainty:31; helper_search_failure:14; tool_necessity_miss:7 |
| strong_decomposition_intervention | 330 | 153 | 60 | 0 | 117 | 0 | 0.2817 | 0.6338 | 48 | parse_failure:117; helper_mention_without_use:57; visual_uncertainty:48; helper_search_failure:21; tool_necessity_miss:17 |
| tool_prior_intervention | 330 | 149 | 48 | 0 | 133 | 0 | 0.2437 | 0.6548 | 40 | parse_failure:133; helper_mention_without_use:45; visual_uncertainty:40; helper_search_failure:14; tool_necessity_miss:7 |

## By prompt ID

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| efficient_safe_free_plan | 110 | 39 | 30 | 0 | 41 | 0 | 0.4348 | 0.4203 | 15 | parse_failure:41; aggregation_failure:15; container_affordance_miss:15; helper_mention_without_use:15; visual_uncertainty:15 |
| efficient_safe_free_plan_humanoid_dual_arm | 110 | 21 | 31 | 0 | 58 | 0 | 0.5962 | 0.2115 | 19 | parse_failure:58; helper_mention_without_use:19; visual_uncertainty:19; aggregation_failure:12; container_affordance_miss:12 |
| efficient_safe_free_plan_quadruped_single_arm | 110 | 14 | 19 | 0 | 77 | 0 | 0.5758 | 0.1212 | 10 | parse_failure:77; helper_mention_without_use:10; visual_uncertainty:10; aggregation_failure:9; container_affordance_miss:9 |
| natural_free_plan | 110 | 41 | 37 | 0 | 32 | 0 | 0.4744 | 0.3974 | 31 | parse_failure:32; helper_mention_without_use:31; visual_uncertainty:31; aggregation_failure:6; container_affordance_miss:6 |
| natural_free_plan_humanoid_dual_arm | 110 | 49 | 31 | 0 | 30 | 0 | 0.3875 | 0.5 | 13 | parse_failure:30; aggregation_failure:17; container_affordance_miss:17; helper_mention_without_use:13; visual_uncertainty:13 |
| natural_free_plan_quadruped_single_arm | 110 | 31 | 36 | 0 | 43 | 0 | 0.5373 | 0.3284 | 19 | parse_failure:43; helper_mention_without_use:19; visual_uncertainty:19; aggregation_failure:16; container_affordance_miss:16 |
| search_explicit_strong_decomposition_free_plan | 110 | 73 | 14 | 0 | 23 | 0 | 0.1609 | 0.7471 | 12 | parse_failure:23; helper_mention_without_use:13; visual_uncertainty:12; tool_necessity_miss:3; helper_search_failure:1 |
| search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | 110 | 64 | 14 | 0 | 32 | 0 | 0.1795 | 0.7051 | 13 | parse_failure:32; helper_mention_without_use:13; visual_uncertainty:13; helper_search_failure:10; tool_necessity_miss:2 |
| search_explicit_strong_decomposition_free_plan_quadruped_single_arm | 110 | 55 | 6 | 0 | 49 | 0 | 0.0984 | 0.7377 | 6 | parse_failure:49; helper_mention_without_use:6; visual_uncertainty:6; helper_search_failure:3; tool_necessity_miss:2 |
| strong_decomposition_free_plan | 110 | 58 | 25 | 0 | 27 | 0 | 0.3012 | 0.6506 | 19 | parse_failure:27; helper_mention_without_use:22; visual_uncertainty:19; helper_search_failure:6; tool_necessity_miss:4 |
| strong_decomposition_free_plan_humanoid_dual_arm | 110 | 50 | 15 | 0 | 45 | 0 | 0.2308 | 0.7077 | 9 | parse_failure:45; helper_mention_without_use:15; visual_uncertainty:9; helper_search_failure:6; tool_necessity_miss:4 |
| strong_decomposition_free_plan_quadruped_single_arm | 110 | 45 | 20 | 0 | 45 | 0 | 0.3077 | 0.5385 | 20 | parse_failure:45; helper_mention_without_use:20; visual_uncertainty:20; helper_search_failure:9; tool_necessity_miss:9 |
| structured_tool_action_chain_probe_humanoid_dual_arm | 110 | 68 | 15 | 0 | 27 | 0 | 0.1807 | 0.6988 | 0 | parse_failure:27; helper_mention_without_use:15; field_plan_inconsistency:4; target_as_helper:4; helper_search_failure:2 |
| structured_tool_action_chain_probe_quadruped_single_arm | 110 | 56 | 45 | 0 | 9 | 0 | 0.4455 | 0.4554 | 0 | helper_mention_without_use:45; helper_search_failure:10; parse_failure:9; tool_necessity_miss:8; field_plan_inconsistency:5 |
| structured_tool_probe | 110 | 53 | 29 | 0 | 28 | 0 | 0.3537 | 0.5244 | 0 | helper_mention_without_use:29; parse_failure:28; field_plan_inconsistency:3 |
| tool_prior_free_plan | 110 | 68 | 27 | 0 | 15 | 0 | 0.2842 | 0.6211 | 26 | helper_mention_without_use:26; visual_uncertainty:26; parse_failure:15; helper_search_failure:9; tool_necessity_miss:6 |
| tool_prior_free_plan_humanoid_dual_arm | 110 | 48 | 13 | 0 | 49 | 0 | 0.2131 | 0.7541 | 7 | parse_failure:49; helper_mention_without_use:11; visual_uncertainty:7; helper_search_failure:3; aggregation_failure:2 |
| tool_prior_free_plan_quadruped_single_arm | 110 | 33 | 8 | 0 | 69 | 0 | 0.1951 | 0.5854 | 7 | parse_failure:69; helper_mention_without_use:8; visual_uncertainty:7; helper_search_failure:2 |

## By model

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ollama_qwen3_5_35b | 1980 | 866 | 415 | 0 | 699 | 0 | 0.324 | 0.5566 | 226 | parse_failure:699; helper_mention_without_use:330; visual_uncertainty:226; helper_search_failure:109; aggregation_failure:77 |

## By task

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| task_001 | 180 | 49 | 75 | 0 | 56 | 0 | 0.6048 | 0.3952 | 50 | helper_mention_without_use:67; parse_failure:56; visual_uncertainty:50; aggregation_failure:8; container_affordance_miss:8 |
| task_002 | 180 | 27 | 113 | 0 | 40 | 0 | 0.8071 | 0.1929 | 55 | helper_search_failure:109; helper_mention_without_use:68; visual_uncertainty:55; aggregation_failure:45; container_affordance_miss:45 |
| task_003 | 180 | 85 | 18 | 0 | 77 | 0 | 0.1748 | 0.8252 | 14 | parse_failure:77; helper_mention_without_use:16; visual_uncertainty:14; aggregation_failure:2; container_affordance_miss:2 |
| task_004 | 180 | 54 | 54 | 0 | 72 | 0 | 0.5 | 0.5 | 30 | parse_failure:72; helper_mention_without_use:48; visual_uncertainty:30; tool_necessity_miss:11; aggregation_failure:6 |
| task_005 | 180 | 63 | 19 | 0 | 98 | 0 | 0.2317 | 0.7683 | 13 | parse_failure:98; helper_mention_without_use:17; visual_uncertainty:13; aggregation_failure:2; container_affordance_miss:2 |
| task_006 | 180 | 118 | 1 | 0 | 61 | 0 | 0.0084 | 0.9916 | 1 | parse_failure:61; helper_mention_without_use:1; visual_uncertainty:1 |
| task_007 | 180 | 98 | 16 | 0 | 66 | 0 | 0.1404 | 0.8596 | 9 | parse_failure:66; helper_mention_without_use:16; visual_uncertainty:9; field_plan_inconsistency:2; target_as_helper:2 |
| task_008 | 180 | 79 | 77 | 0 | 24 | 0 | 0.4936 | 0.5064 | 46 | helper_mention_without_use:63; visual_uncertainty:46; parse_failure:24; aggregation_failure:14; container_affordance_miss:14 |
| task_009 | 180 | 90 | 15 | 0 | 75 | 0 | 0.1429 | 0.9333 | 7 | parse_failure:75; wrong_helper_type:8; helper_mention_without_use:7; visual_uncertainty:7 |
| task_010 | 180 | 42 | 12 | 0 | 126 | 0 | 0.2222 | 0.7778 | 1 | parse_failure:126; helper_mention_without_use:12; field_plan_inconsistency:6; target_as_helper:4; visual_uncertainty:1 |
| task_011 | 180 | 161 | 15 | 0 | 4 | 0 | 0.0852 | 0.0 | 0 | helper_mention_without_use:15; parse_failure:4 |

## By embodiment

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| generic | 660 | 332 | 162 | 0 | 166 | 0 | 0.3279 | 0.5688 | 103 | parse_failure:166; helper_mention_without_use:136; visual_uncertainty:103; helper_search_failure:31; aggregation_failure:21 |
| humanoid_dual_arm | 660 | 300 | 119 | 0 | 241 | 0 | 0.284 | 0.611 | 61 | parse_failure:241; helper_mention_without_use:86; visual_uncertainty:61; helper_search_failure:40; aggregation_failure:31 |
| quadruped_single_arm | 660 | 234 | 134 | 0 | 292 | 0 | 0.3641 | 0.4783 | 62 | parse_failure:292; helper_mention_without_use:108; visual_uncertainty:62; helper_search_failure:38; aggregation_failure:25 |

