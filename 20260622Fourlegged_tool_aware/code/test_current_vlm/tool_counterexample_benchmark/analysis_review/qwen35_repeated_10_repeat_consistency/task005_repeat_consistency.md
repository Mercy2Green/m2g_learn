# task_005 Repeat Consistency

- Stable pass prompts: 8 / 18
- Stable fail prompts: 7 / 18
- Pass/fail flip prompts: 1 / 18
- Successful rows mentioning visible tray/basin/basket-like helper: 44 / 44
- Failure modes top: direct_operation_without_helper:38 | helper_mention_without_use:14 | aggregation_failure:1

## Stable Pass Prompts

| prompt_id | consistency_type | vlm_true_pass_count | parse_error_count | helper_chain_yes_count |
| --- | --- | --- | --- | --- |
| search_explicit_strong_decomposition_free_plan | stable_nonparse_pass_with_parse | 9 | 1 | 9 |
| search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | stable_nonparse_pass_with_parse | 4 | 6 | 4 |
| search_explicit_strong_decomposition_free_plan_quadruped_single_arm | stable_nonparse_pass_with_parse | 4 | 6 | 4 |
| strong_decomposition_free_plan | stable_nonparse_pass_with_parse | 7 | 3 | 7 |
| strong_decomposition_free_plan_humanoid_dual_arm | stable_nonparse_pass_with_parse | 6 | 4 | 6 |
| strong_decomposition_free_plan_quadruped_single_arm | stable_nonparse_pass_with_parse | 2 | 8 | 2 |
| tool_prior_free_plan | stable_nonparse_pass_with_parse | 8 | 2 | 8 |
| tool_prior_free_plan_humanoid_dual_arm | stable_nonparse_pass_with_parse | 3 | 7 | 3 |

## Stable Fail Prompts

| prompt_id | consistency_type | vlm_true_fail_count | parse_error_count | failure_modes_top |
| --- | --- | --- | --- | --- |
| efficient_safe_free_plan_humanoid_dual_arm | stable_nonparse_fail_with_parse | 8 | 2 | direct_operation_without_helper:8 \| tested_model_parse_error:2 \| aggregation_failure:1 |
| natural_free_plan | stable_nonparse_fail_with_parse | 4 | 6 | tested_model_parse_error:6 \| direct_operation_without_helper:4 \| helper_mention_without_use:1 |
| natural_free_plan_humanoid_dual_arm | stable_nonparse_fail_with_parse | 9 | 1 | direct_operation_without_helper:9 \| tested_model_parse_error:1 |
| natural_free_plan_quadruped_single_arm | stable_nonparse_fail_with_parse | 3 | 7 | tested_model_parse_error:7 \| direct_operation_without_helper:3 \| helper_mention_without_use:1 |
| structured_tool_action_chain_probe_humanoid_dual_arm | stable_nonparse_fail_with_parse | 1 | 9 | tested_model_parse_error:9 \| direct_operation_without_helper:1 \| helper_mention_without_use:1 |
| structured_tool_probe | stable_nonparse_fail_with_parse | 3 | 7 | tested_model_parse_error:7 \| direct_operation_without_helper:3 \| helper_mention_without_use:2 |
| tool_prior_free_plan_quadruped_single_arm | stable_nonparse_fail_with_parse | 1 | 9 | tested_model_parse_error:9 \| direct_operation_without_helper:1 |

## Pass/Fail Flip Prompts

| prompt_id | vlm_true_pass_count | vlm_true_fail_count | label_sequence_by_repeat | helper_chain_sequence_by_repeat |
| --- | --- | --- | --- | --- |
| structured_tool_action_chain_probe_quadruped_single_arm | 1 | 9 | repeat_01:true_fail \| repeat_02:true_fail \| repeat_03:true_fail \| repeat_04:true_fail \| repeat_05:true_fail \| repeat_06:true_pass \| repeat_07:true_fail \| repeat_08:true_fail \| repeat_09:true_fail \| repeat_10:true_fail | repeat_01:no \| repeat_02:no \| repeat_03:no \| repeat_04:no \| repeat_05:no \| repeat_06:yes \| repeat_07:no \| repeat_08:no \| repeat_09:no \| repeat_10:no |

## Success/Failure Short Examples

| label | run_id | prompt_id | quote |
| --- | --- | --- | --- |
| success | repeat_01_ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan | 识别并利用位于桌面左侧的大号米色托盘作为辅助搬运工具，将其调整至便于装载的位置。; 依次抓取桌上的白色马克杯（含勺子）、不锈钢保温杯、白碗和金属盆，将它们有序地放置在米色托盘上；注意将较重的金属盆放在底部或中心位置以保持稳定，陶瓷碗可叠放或并排摆放以节省空间。; 双手稳固抓持装有所有餐具的托盘，将其从当前桌面搬运至厨房区域进行最终收纳。 |
| success | repeat_02_ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan | 识别并利用桌左侧的大号米色砧板/托盘作为临时搬运容器，将其调整至便于抓取的位置。; 依次将桌上的不锈钢大碗、堆叠的白色小碗以及杯子放置在托盘中（注意重物在下或居中以保持平衡）。; 端起装有所有餐具的托盘，一次性将它们运送到厨房指定位置并放下。 |
| success | repeat_03_ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan | 识别并利用桌左侧的大号米色托盘作为辅助搬运工具，将其调整至便于装载的位置。; 依次抓取桌上的所有餐具（白色马克杯、不锈钢保温杯、白碗组、金属盆），将它们有序地堆叠或放置在米色托盘上，确保重心稳定且不易滑落。; 双手抓握装有全部餐具的托盘边缘，将其平稳搬运至厨房区域并放置在水槽旁完成收纳任务。 |
| success | repeat_04_ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan | 识别并利用左侧的大号米色砧板/托盘作为临时搬运容器，将其调整至便于抓取的位置（如果它当前是平放的）。; 依次抓取桌上的不锈钢盆、白色小碗和马克杯，将它们放置在托盘中或堆叠在托盘上。注意将较重的物品放在底部以保持稳定。; 端起装有所有餐具的托盘，将其运送到厨房指定位置并放下完成收纳。 |
| success | repeat_06_ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan | 识别并利用位于桌面左侧的大号米色托盘作为辅助搬运工具，将其位置调整至便于装载物品的状态。; 依次抓取桌上的白色马克杯（含勺子）、不锈钢保温杯、白碗和金属盆，将它们有序地堆叠或放置在米色托盘上，确保重心稳定且不易滑落。; 双手稳固抓持装有所有餐具的托盘，将其从当前桌面搬运至厨房区域进行最终收纳。 |
| failure | repeat_01_ollama_qwen3_5_35b | efficient_safe_free_plan_humanoid_dual_arm | Grasp the stack of two white ceramic bowls with one hand and simultaneously grasp the stainless steel bowl with the other hand; move these items away from the table towards the kitchen direction.; Return to pick up the mug containing a s... |
| failure | repeat_03_ollama_qwen3_5_35b | efficient_safe_free_plan_humanoid_dual_arm | 双手同时抓取桌面上的主要餐具组合：左手抓握叠放的白色瓷碗和勺子作为一组稳定物体，右手抓握不锈钢大碗或灰色保温杯；或者分两次快速连续抓取剩余的小件（如马克杯）。; 将手中持有的所有餐具一次性搬运至厨房区域并放入水槽。 |
| failure | repeat_05_ollama_qwen3_5_35b | efficient_safe_free_plan_humanoid_dual_arm | 双手同时抓取主要餐具组合：左手抓握叠放的两个白色小碗，右手抓握不锈钢大碗; 转身离开桌子前往厨房放置物品 |
| failure | repeat_06_ollama_qwen3_5_35b | efficient_safe_free_plan_humanoid_dual_arm | 双手同时抓取桌面上的主要餐具组合：左手抓握叠放的白瓷碗和马克杯，右手抓握不锈钢大碗或保温杯。; 转身离开桌子前往厨房放置物品。 |
| failure | repeat_07_ollama_qwen3_5_35b | efficient_safe_free_plan_humanoid_dual_arm | 双手协同抓取：左手同时抓握两个白色瓷碗和马克杯组合，右手抓握不锈钢大碗或灰色水杯; 转身离开桌子前往厨房 |
