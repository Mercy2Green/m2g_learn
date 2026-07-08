# VLM vs Text Repeat Consistency Comparison

- Groups compared: 198
- Consistency type agreements: 136
- Text-only pass/fail flip groups: 48
- VLM-only pass/fail flip groups: 10

## Text-Only Flip Groups

| task_id | prompt_id | vlm_consistency_type | text_consistency_type | vlm_nonparse_flip | text_nonparse_flip |
| --- | --- | --- | --- | --- | --- |
| task_001 | efficient_safe_free_plan_quadruped_single_arm | stable_nonparse_fail_with_parse | mixed_pass_fail_with_parse | false | true |
| task_001 | search_explicit_strong_decomposition_free_plan | stable_all_pass | mixed_pass_fail_no_parse | false | true |
| task_001 | search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | stable_all_pass | mixed_pass_fail_no_parse | false | true |
| task_001 | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_001 | strong_decomposition_free_plan | stable_all_pass | mixed_pass_fail_no_parse | false | true |
| task_001 | strong_decomposition_free_plan_quadruped_single_arm | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_001 | tool_prior_free_plan | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_002 | natural_free_plan | stable_nonparse_fail_with_parse | mixed_pass_fail_with_parse | false | true |
| task_002 | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | stable_nonparse_fail_with_parse | mixed_pass_fail_with_parse | false | true |
| task_002 | strong_decomposition_free_plan_humanoid_dual_arm | stable_nonparse_fail_with_parse | mixed_pass_fail_with_parse | false | true |
| task_002 | structured_tool_action_chain_probe_humanoid_dual_arm | stable_all_fail | mixed_pass_fail_no_parse | false | true |
| task_002 | tool_prior_free_plan | stable_all_fail | mixed_pass_fail_no_parse | false | true |
| task_002 | tool_prior_free_plan_humanoid_dual_arm | stable_nonparse_fail_with_parse | mixed_pass_fail_with_parse | false | true |
| task_002 | tool_prior_free_plan_quadruped_single_arm | stable_nonparse_fail_with_parse | mixed_pass_fail_with_parse | false | true |
| task_003 | efficient_safe_free_plan | stable_all_pass | mixed_pass_fail_no_parse | false | true |
| task_003 | efficient_safe_free_plan_humanoid_dual_arm | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_003 | search_explicit_strong_decomposition_free_plan | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_003 | tool_prior_free_plan | stable_all_pass | mixed_pass_fail_no_parse | false | true |
| task_004 | natural_free_plan | stable_nonparse_fail_with_parse | mixed_pass_fail_with_parse | false | true |
| task_004 | natural_free_plan_humanoid_dual_arm | stable_nonparse_fail_with_parse | mixed_pass_fail_with_parse | false | true |
| task_004 | strong_decomposition_free_plan_quadruped_single_arm | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_004 | structured_tool_probe | stable_all_fail | mixed_pass_fail_no_parse | false | true |
| task_004 | tool_prior_free_plan_quadruped_single_arm | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_005 | efficient_safe_free_plan_humanoid_dual_arm | stable_nonparse_fail_with_parse | mixed_pass_fail_with_parse | false | true |
| task_005 | natural_free_plan | stable_nonparse_fail_with_parse | mixed_pass_fail_with_parse | false | true |
| task_005 | natural_free_plan_humanoid_dual_arm | stable_nonparse_fail_with_parse | mixed_pass_fail_with_parse | false | true |
| task_005 | structured_tool_probe | stable_nonparse_fail_with_parse | mixed_pass_fail_with_parse | false | true |
| task_006 | natural_free_plan | stable_all_pass | mixed_pass_fail_no_parse | false | true |
| task_007 | natural_free_plan | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_007 | strong_decomposition_free_plan | stable_all_pass | mixed_pass_fail_no_parse | false | true |
| task_007 | structured_tool_action_chain_probe_humanoid_dual_arm | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_007 | structured_tool_action_chain_probe_quadruped_single_arm | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_007 | tool_prior_free_plan | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_008 | efficient_safe_free_plan | stable_nonparse_fail_with_parse | mixed_pass_fail_with_parse | false | true |
| task_008 | efficient_safe_free_plan_quadruped_single_arm | stable_all_fail | mixed_pass_fail_no_parse | false | true |
| task_008 | natural_free_plan | stable_nonparse_fail_with_parse | mixed_pass_fail_with_parse | false | true |
| task_008 | structured_tool_action_chain_probe_quadruped_single_arm | stable_all_fail | mixed_pass_fail_no_parse | false | true |
| task_008 | structured_tool_probe | stable_all_fail | mixed_pass_fail_no_parse | false | true |
| task_009 | search_explicit_strong_decomposition_free_plan | stable_all_pass | mixed_pass_fail_no_parse | false | true |
| task_009 | search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_009 | strong_decomposition_free_plan | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_009 | tool_prior_free_plan | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_010 | structured_tool_probe | stable_all_fail | mixed_pass_fail_no_parse | false | true |
| task_011 | search_explicit_strong_decomposition_free_plan | stable_all_pass | mixed_pass_fail_no_parse | false | true |
| task_011 | strong_decomposition_free_plan | stable_all_pass | mixed_pass_fail_no_parse | false | true |
| task_011 | strong_decomposition_free_plan_humanoid_dual_arm | stable_all_pass | mixed_pass_fail_no_parse | false | true |
| task_011 | tool_prior_free_plan_humanoid_dual_arm | stable_nonparse_pass_with_parse | mixed_pass_fail_with_parse | false | true |
| task_011 | tool_prior_free_plan_quadruped_single_arm | stable_all_pass | mixed_pass_fail_no_parse | false | true |

## VLM-Only Flip Groups

| task_id | prompt_id | vlm_consistency_type | text_consistency_type | vlm_nonparse_flip | text_nonparse_flip |
| --- | --- | --- | --- | --- | --- |
| task_003 | strong_decomposition_free_plan_humanoid_dual_arm | mixed_pass_fail_with_parse | stable_nonparse_pass_with_parse | true | false |
| task_003 | structured_tool_probe | mixed_pass_fail_with_parse | stable_nonparse_pass_with_parse | true | false |
| task_003 | tool_prior_free_plan_quadruped_single_arm | mixed_pass_fail_with_parse | stable_nonparse_pass_with_parse | true | false |
| task_006 | natural_free_plan_humanoid_dual_arm | mixed_pass_fail_with_parse | stable_nonparse_pass_with_parse | true | false |
| task_006 | structured_tool_action_chain_probe_humanoid_dual_arm | mixed_pass_fail_no_parse | stable_all_pass | true | false |
| task_006 | structured_tool_action_chain_probe_quadruped_single_arm | mixed_pass_fail_no_parse | stable_all_pass | true | false |
| task_006 | tool_prior_free_plan_humanoid_dual_arm | mixed_pass_fail_with_parse | stable_nonparse_pass_with_parse | true | false |
| task_006 | tool_prior_free_plan_quadruped_single_arm | mixed_pass_fail_with_parse | stable_nonparse_pass_with_parse | true | false |
| task_007 | efficient_safe_free_plan_humanoid_dual_arm | mixed_pass_fail_with_parse | stable_nonparse_pass_with_parse | true | false |
| task_008 | structured_tool_action_chain_probe_humanoid_dual_arm | mixed_pass_fail_no_parse | stable_all_pass | true | false |
