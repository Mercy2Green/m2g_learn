# Repeat Consistency Summary

## Data Scope

- Total groups: 198
- Expected groups: 198 (11 tasks x 18 prompts)
- Total rows: 1980
- Expected rows: 1980
- Missing/duplicate repeat groups: 0

## Overall Consistency

| consistency_type | groups | percent |
| --- | ---: | ---: |
| stable_all_pass | 36 | 18.2% |
| stable_all_fail | 15 | 7.6% |
| stable_all_parse | 13 | 6.6% |
| stable_nonparse_pass_with_parse | 65 | 32.8% |
| stable_nonparse_fail_with_parse | 33 | 16.7% |
| mixed_pass_fail_no_parse | 10 | 5.1% |
| mixed_pass_fail_with_parse | 26 | 13.1% |
| uncertain_or_other | 0 | 0.0% |

## Key Judgments

- Completely stable groups: 64
- Groups with pass/fail flip: 36
- Groups with helper-chain yes/no flip: 38
- Groups with parse instability: 124

## By Task

| task_id | total_prompt_groups | stable_all_pass_groups | stable_all_fail_groups | stable_all_parse_groups | mixed_pass_fail_groups | helper_chain_flip_groups | groups_with_parse_error | avg_pass_rate_non_parse | avg_helper_chain_yes_rate_non_parse | avg_volatility_score | max_volatility_score | representative_unstable_prompt_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| task_001 | 18 | 3 | 2 | 1 | 4 | 4 | 12 | 0.467747 | 0.467747 | 0.216667 | 0.5 | structured_tool_probe \| structured_tool_action_chain_probe_humanoid_dual_arm \| efficient_safe_free_plan \| natural_free_plan \| tool_prior_free_plan_humanoid_dual_arm \| efficient_safe_free_plan_humanoid_dual_arm \| efficient_safe_free_plan_quadruped_single_arm \| natural_free_plan_quadruped_single_arm |
| task_002 | 18 | 0 | 7 | 0 | 1 | 1 | 11 | 0.015873 | 0.015873 | 0.144444 | 0.5 | search_explicit_strong_decomposition_free_plan \| efficient_safe_free_plan_quadruped_single_arm \| search_explicit_strong_decomposition_free_plan_quadruped_single_arm \| tool_prior_free_plan_humanoid_dual_arm \| tool_prior_free_plan_quadruped_single_arm \| strong_decomposition_free_plan \| efficient_safe_free_plan_humanoid_dual_arm \| natural_free_plan |
| task_003 | 18 | 3 | 0 | 1 | 6 | 6 | 15 | 0.815388 | 0.815388 | 0.322222 | 0.5 | structured_tool_action_chain_probe_quadruped_single_arm \| structured_tool_probe \| tool_prior_free_plan_quadruped_single_arm \| search_explicit_strong_decomposition_free_plan_quadruped_single_arm \| strong_decomposition_free_plan_humanoid_dual_arm \| natural_free_plan \| efficient_safe_free_plan_humanoid_dual_arm \| natural_free_plan_humanoid_dual_arm |
| task_004 | 18 | 0 | 1 | 1 | 5 | 5 | 16 | 0.457231 | 0.457231 | 0.261111 | 0.5 | efficient_safe_free_plan \| strong_decomposition_free_plan_humanoid_dual_arm \| structured_tool_action_chain_probe_quadruped_single_arm \| search_explicit_strong_decomposition_free_plan \| structured_tool_action_chain_probe_humanoid_dual_arm \| natural_free_plan_humanoid_dual_arm \| strong_decomposition_free_plan \| strong_decomposition_free_plan_quadruped_single_arm |
| task_005 | 18 | 0 | 0 | 2 | 1 | 1 | 17 | 0.45 | 0.45 | 0.216667 | 0.4 | structured_tool_action_chain_probe_quadruped_single_arm \| natural_free_plan \| search_explicit_strong_decomposition_free_plan_humanoid_dual_arm \| search_explicit_strong_decomposition_free_plan_quadruped_single_arm \| strong_decomposition_free_plan_humanoid_dual_arm \| natural_free_plan_quadruped_single_arm \| strong_decomposition_free_plan \| structured_tool_probe |
| task_006 | 18 | 3 | 0 | 2 | 5 | 5 | 13 | 0.837346 | 0.837346 | 0.216667 | 0.5 | tool_prior_free_plan_humanoid_dual_arm \| tool_prior_free_plan_quadruped_single_arm \| structured_tool_action_chain_probe_quadruped_single_arm \| natural_free_plan_humanoid_dual_arm \| structured_tool_action_chain_probe_humanoid_dual_arm \| efficient_safe_free_plan \| strong_decomposition_free_plan_humanoid_dual_arm \| strong_decomposition_free_plan_quadruped_single_arm |
| task_007 | 18 | 3 | 0 | 0 | 3 | 3 | 14 | 0.946296 | 0.951852 | 0.233333 | 0.5 | natural_free_plan_humanoid_dual_arm \| structured_tool_probe \| efficient_safe_free_plan_humanoid_dual_arm \| structured_tool_action_chain_probe_quadruped_single_arm \| tool_prior_free_plan_quadruped_single_arm \| search_explicit_strong_decomposition_free_plan_humanoid_dual_arm \| tool_prior_free_plan_humanoid_dual_arm \| efficient_safe_free_plan |
| task_008 | 18 | 4 | 4 | 0 | 6 | 6 | 8 | 0.387191 | 0.387191 | 0.211111 | 0.6 | tool_prior_free_plan \| natural_free_plan_humanoid_dual_arm \| search_explicit_strong_decomposition_free_plan_quadruped_single_arm \| tool_prior_free_plan_quadruped_single_arm \| efficient_safe_free_plan_humanoid_dual_arm \| structured_tool_action_chain_probe_humanoid_dual_arm \| strong_decomposition_free_plan_quadruped_single_arm \| natural_free_plan |
| task_009 | 18 | 3 | 0 | 1 | 3 | 3 | 14 | 0.718519 | 0.718519 | 0.166667 | 0.6 | natural_free_plan_humanoid_dual_arm \| natural_free_plan \| natural_free_plan_quadruped_single_arm \| strong_decomposition_free_plan_quadruped_single_arm \| efficient_safe_free_plan_quadruped_single_arm \| search_explicit_strong_decomposition_free_plan_humanoid_dual_arm \| search_explicit_strong_decomposition_free_plan_quadruped_single_arm \| strong_decomposition_free_plan_humanoid_dual_arm |
| task_010 | 18 | 0 | 1 | 5 | 2 | 2 | 16 | 0.538095 | 0.546032 | 0.155556 | 0.5 | structured_tool_action_chain_probe_humanoid_dual_arm \| structured_tool_action_chain_probe_quadruped_single_arm \| tool_prior_free_plan_humanoid_dual_arm \| search_explicit_strong_decomposition_free_plan_quadruped_single_arm \| tool_prior_free_plan \| natural_free_plan \| search_explicit_strong_decomposition_free_plan_humanoid_dual_arm \| efficient_safe_free_plan |
| task_011 | 18 | 17 | 0 | 0 | 0 | 2 | 1 | 1 | 0.016667 | 0.022222 | 0.4 | structured_tool_action_chain_probe_humanoid_dual_arm \| structured_tool_probe \| tool_prior_free_plan_humanoid_dual_arm |

## By Prompt

| prompt_id | prompt_category | embodiment_profile | total_task_groups | stable_all_pass_groups | stable_all_fail_groups | stable_all_parse_groups | mixed_pass_fail_groups | helper_chain_flip_groups | groups_with_parse_error | avg_pass_rate_non_parse | avg_helper_chain_yes_rate_non_parse | avg_volatility_score | max_volatility_score | representative_unstable_task_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| efficient_safe_free_plan | generic_clean | generic | 11 | 2 | 1 | 1 | 2 | 2 | 8 | 0.500722 | 0.409812 | 0.172727 | 0.5 | task_004 \| task_001 \| task_006 \| task_007 \| task_008 \| task_009 \| task_010 |
| efficient_safe_free_plan_humanoid_dual_arm | embodiment_clean | humanoid_dual_arm | 11 | 1 | 0 | 3 | 2 | 2 | 10 | 0.238636 | 0.147727 | 0.172727 | 0.5 | task_008 \| task_007 \| task_003 \| task_001 \| task_004 \| task_005 \| task_002 |
| efficient_safe_free_plan_quadruped_single_arm | embodiment_clean | quadruped_single_arm | 11 | 1 | 1 | 3 | 0 | 0 | 9 | 0.272727 | 0.181818 | 0.118182 | 0.4 | task_002 \| task_001 \| task_009 \| task_004 \| task_007 \| task_010 |
| natural_free_plan | generic_clean | generic | 11 | 2 | 0 | 0 | 3 | 3 | 9 | 0.494949 | 0.40404 | 0.209091 | 0.4 | task_001 \| task_009 \| task_003 \| task_005 \| task_007 \| task_008 \| task_004 \| task_010 |
| natural_free_plan_humanoid_dual_arm | embodiment_clean | humanoid_dual_arm | 11 | 1 | 2 | 0 | 4 | 4 | 8 | 0.515152 | 0.424242 | 0.272727 | 0.6 | task_009 \| task_007 \| task_008 \| task_006 \| task_003 \| task_004 \| task_005 \| task_010 |
| natural_free_plan_quadruped_single_arm | embodiment_clean | quadruped_single_arm | 11 | 1 | 2 | 0 | 1 | 1 | 7 | 0.463636 | 0.372727 | 0.163636 | 0.3 | task_009 \| task_001 \| task_003 \| task_005 \| task_006 \| task_004 \| task_007 \| task_010 |
| search_explicit_strong_decomposition_free_plan | search_explicit_strong_decomposition_intervention | generic | 11 | 5 | 0 | 0 | 2 | 2 | 6 | 0.834055 | 0.743146 | 0.145455 | 0.5 | task_002 \| task_004 \| task_003 \| task_008 \| task_005 \| task_010 |
| search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | search_explicit_strong_decomposition_intervention | humanoid_dual_arm | 11 | 4 | 1 | 0 | 0 | 0 | 6 | 0.909091 | 0.818182 | 0.163636 | 0.4 | task_005 \| task_007 \| task_003 \| task_004 \| task_009 \| task_010 |
| search_explicit_strong_decomposition_free_plan_quadruped_single_arm | search_explicit_strong_decomposition_intervention | quadruped_single_arm | 11 | 1 | 0 | 1 | 2 | 2 | 10 | 0.777273 | 0.686364 | 0.245455 | 0.5 | task_008 \| task_003 \| task_002 \| task_005 \| task_001 \| task_010 \| task_009 \| task_006 |
| strong_decomposition_free_plan | strong_decomposition_intervention | generic | 11 | 4 | 0 | 1 | 0 | 0 | 7 | 0.818182 | 0.727273 | 0.154545 | 0.5 | task_003 \| task_004 \| task_005 \| task_002 \| task_006 \| task_009 |
| strong_decomposition_free_plan_humanoid_dual_arm | strong_decomposition_intervention | humanoid_dual_arm | 11 | 3 | 0 | 1 | 2 | 2 | 8 | 0.737374 | 0.646465 | 0.190909 | 0.5 | task_004 \| task_003 \| task_005 \| task_006 \| task_001 \| task_009 \| task_002 |
| strong_decomposition_free_plan_quadruped_single_arm | strong_decomposition_intervention | quadruped_single_arm | 11 | 2 | 0 | 1 | 0 | 0 | 9 | 0.727273 | 0.636364 | 0.209091 | 0.4 | task_004 \| task_006 \| task_008 \| task_009 \| task_001 \| task_005 \| task_002 \| task_007 |
| structured_tool_action_chain_probe_humanoid_dual_arm | diagnostic_probe | humanoid_dual_arm | 11 | 2 | 1 | 0 | 5 | 6 | 5 | 0.599711 | 0.539971 | 0.2 | 0.5 | task_010 \| task_001 \| task_008 \| task_004 \| task_006 \| task_011 \| task_003 \| task_007 |
| structured_tool_action_chain_probe_quadruped_single_arm | diagnostic_probe | quadruped_single_arm | 11 | 1 | 3 | 0 | 5 | 5 | 3 | 0.453247 | 0.362338 | 0.218182 | 0.5 | task_003 \| task_004 \| task_010 \| task_006 \| task_005 \| task_007 \| task_009 |
| structured_tool_probe | diagnostic_probe | generic | 11 | 2 | 3 | 0 | 3 | 4 | 5 | 0.396429 | 0.323701 | 0.181818 | 0.5 | task_001 \| task_003 \| task_007 \| task_011 \| task_005 \| task_006 \| task_002 |
| tool_prior_free_plan | tool_prior_intervention | generic | 11 | 2 | 1 | 0 | 1 | 1 | 8 | 0.863636 | 0.772727 | 0.172727 | 0.6 | task_008 \| task_006 \| task_010 \| task_001 \| task_005 \| task_004 \| task_007 \| task_009 |
| tool_prior_free_plan_humanoid_dual_arm | tool_prior_intervention | humanoid_dual_arm | 11 | 1 | 0 | 0 | 1 | 1 | 10 | 0.80303 | 0.712121 | 0.327273 | 0.5 | task_006 \| task_001 \| task_003 \| task_007 \| task_010 \| task_011 \| task_002 \| task_005 |
| tool_prior_free_plan_quadruped_single_arm | tool_prior_intervention | quadruped_single_arm | 11 | 1 | 0 | 2 | 3 | 3 | 9 | 0.45 | 0.359091 | 0.227273 | 0.5 | task_003 \| task_006 \| task_008 \| task_007 \| task_002 \| task_004 \| task_005 \| task_009 |

## Input Integrity Audit

- Groups audited: 198
- Groups with non-identical inputs or repeat-count issues: 0
- Groups with changed system/user/image/task fields: 0
