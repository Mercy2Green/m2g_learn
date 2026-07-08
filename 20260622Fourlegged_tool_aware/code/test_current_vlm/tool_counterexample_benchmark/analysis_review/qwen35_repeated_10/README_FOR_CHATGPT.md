# README For ChatGPT

This is an automatic text-based rereview handoff. It suggests analysis directions but is not final paper evidence.

## Data Scope
- Rows: 1980
- Models: 1 (ollama_qwen3_5_35b)
- Tasks: 11 (task_001, task_002, task_003, task_004, task_005, task_006, task_007, task_008, task_009, task_010, task_011)
- Prompt categories: {'generic_clean': 220, 'tool_prior_intervention': 330, 'strong_decomposition_intervention': 330, 'search_explicit_strong_decomposition_intervention': 330, 'diagnostic_probe': 330, 'embodiment_clean': 440}
- Rereview labels: {'true_pass': 866, 'true_fail': 415, 'parse_error': 699}
- Context risk labels: {'low': 1980}

## Rereview Rubric Summary
- Valid helper use requires a committed action chain, not just helper mention.
- Conditional helper-only plans are not counted as valid helper use.
- Tool-prior prompts are intervention checks, not clean evidence.
- Visual uncertainty remains unresolved until image-level review.

## Top 10 Findings
- parse_failure: 699 text-based labels
- helper_mention_without_use: 330 text-based labels
- visual_uncertainty: 226 text-based labels
- helper_search_failure: 109 text-based labels
- aggregation_failure: 77 text-based labels
- container_affordance_miss: 77 text-based labels
- tool_necessity_miss: 48 text-based labels
- field_plan_inconsistency: 12 text-based labels
- wrong_helper_type: 8 text-based labels
- target_as_helper: 6 text-based labels

## Top Clean Counterexample Candidates
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_qwen3_5_35b / natural_free_plan_humanoid_dual_arm: helper_mention_without_use;visual_uncertainty | 使用双手机械臂分别抓取桌上的农夫山泉矿泉水瓶; 将抓取的矿泉水搬运至卧室区域; 重复上述步骤直至所有需要的水送达 基于机器人双手机械臂可同时稳定抓取单个物体的能力，结合桌上矿泉水分布情况制定分批运送计划，兼顾效率与稳定性。 利用双手机械臂同时抓取水瓶以减少往返次数，提升运送效率 未明确卧室具体位置及距离，需先确认路径；同时不确定水瓶总数是否超过单次可搬运量（假设多瓶但分批次） { "task_understanding": "识别桌上农夫山泉矿泉水瓶为需运送至卧室的饮用...
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_qwen3_5_35b / natural_free_plan: aggregation_failure;container_affordance_miss;helper_search_failure | Scan the table surface to identify all water bottle locations and check for obstacles like cables or books that might block access.; Grasp multiple water bottles securely in one batch, ensuring stability near nearby electronics (laptop/c...
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_qwen3_5_35b / efficient_safe_free_plan: aggregation_failure;container_affordance_miss;helper_search_failure | 检查桌面环境，确认水瓶位置及周围障碍物（如笔记本电脑、书籍）以确保安全抓取路径。; 尝试一次抓取多瓶水（例如左侧或右侧的一簇），移动至卧室并放置好。; 返回原处抓取剩余的水瓶，再次移动到卧室完成交付。 尽量在一次行程中携带尽可能多的水瓶以减少往返次数；优先处理最显眼、易抓取的瓶子组。 抓取时注意不要碰倒旁边的笔记本电脑和书籍，确保握持稳固防止水洒出或掉落。 不确定卧室的具体位置（虽然任务说是卧室），以及机器人一次最多能抓几瓶水的物理限制。 { "task_underst...
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_qwen3_5_35b / natural_free_plan_humanoid_dual_arm: aggregation_failure;container_affordance_miss;helper_search_failure | 检查桌面周围是否有障碍物（如电线、笔记本电脑）影响抓取路径; 用双手各持1-2瓶水，分3次搬运至卧室; 确保每次搬运时手臂稳定不碰撞其他物品 利用双手机械臂同时抓取水瓶减少往返次数 避免触碰笔记本电脑和电线，保持身体平衡防止倾倒 未明确卧室具体位置及搬运路径是否存在障碍 { "task_understanding": "将桌上的6瓶农夫山泉矿泉水送至有同学在打牌的卧室", "plan": [ "检查桌面周围是否有障碍物（如电线、笔记本电脑）影响抓取路径", "用双手各持...
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_qwen3_5_35b / efficient_safe_free_plan_humanoid_dual_arm: aggregation_failure;container_affordance_miss;helper_search_failure | 确认桌面无阻碍物后双手各持一瓶水（共两瓶）运送至卧室; 返回取剩余四瓶中相邻的两瓶再次搬运; 最后两次分别搬运剩余水瓶 采用双手机械臂协同抓取策略最大化单次运载量，避免单手持物导致的频繁往返 每次仅搬运两瓶水确保抓握稳定性，防止倾倒造成液体泄漏或物品损坏 未确认卧室具体位置及路径是否存在障碍物需绕行 { "task_understanding": "将桌上六瓶农夫山泉矿泉水送至卧室供同学饮用", "plan": [ "确认桌面无阻碍物后双手各持一瓶水（共两瓶）运送至卧室...
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_qwen3_5_35b / natural_free_plan_quadruped_single_arm: aggregation_failure;container_affordance_miss;helper_search_failure | 确认水瓶组合物体稳定性并尝试抓取3-4瓶紧密排列的水; 保持平衡移动至卧室门口检查通行条件; 重复搬运剩余水直至全部送达 优先选择能稳定携带的最大数量水瓶减少往返次数 移动时保持底盘平衡，避免夹爪负载不均导致倾倒 未确认卧室具体位置及通行路径是否存在障碍物 { "task_understanding": "将桌上的农夫山泉矿泉水搬运至有同学在打牌的卧室", "plan": [ "确认水瓶组合物体稳定性并尝试抓取3-4瓶紧密排列的水", "保持平衡移动至卧室门口检查通行条...
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_qwen3_5_35b / efficient_safe_free_plan_quadruped_single_arm: aggregation_failure;container_affordance_miss;helper_search_failure | 移动到桌边，扫描并确认水瓶的具体排列位置及周围障碍物（如笔记本电脑、书本）。; 尝试一次抓取相邻的2-3瓶水作为一组（若物理上稳定），或分批次每次携带1-2瓶靠近边缘的水。; 将这批水搬运至卧室指定区域放下，然后返回桌子重复上述步骤直到所有水瓶被运走。 尝试在夹爪稳定范围内最大化单次携带数量（例如一次抓取相邻的2-3瓶水），以减少往返次数，尽快满足需求。 水瓶为圆柱体易滚动且散落摆放，需确保抓握稳固防止掉落；搬运过程中保持底盘平衡，避免碰撞桌边物品导致倾倒或夹爪失稳。...
- task_003 / 372f92c1ce9c87231d199c1102dcf7b4.jpg / ollama_qwen3_5_35b / efficient_safe_free_plan_humanoid_dual_arm: aggregation_failure;container_affordance_miss | 1. 检查并合上中间的笔记本电脑屏幕，确保设备处于安全状态。; 2. 将右侧椅子上的黑色电脑包移至桌面上或调整其位置以便操作拉链和放入物品。; 3. 依次将笔记本电脑、桌上的水杯及其他必要小件物品装入电脑包中。 优先处理核心电子设备（笔记本电脑）的收纳，忽略报纸等无需带走的杂物，减少不必要的移动和整理步骤。 在操作电脑包时注意保持平衡，避免碰倒桌上的显示器或水杯；合上笔记本时需小心屏幕与键盘之间的线缆。 不确定用户是否需要带走左侧的报纸或其他杂物瓶罐，计划中仅针对明显的...
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_qwen3_5_35b / natural_free_plan: aggregation_failure;container_affordance_miss | Move closer to the table to clearly identify specific edible snacks among the scattered packets and locate the water bottle.; Pick up the water bottle first to ensure it is secure before handling loose items.; Gather a handful of snack p...
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_qwen3_5_35b / natural_free_plan_humanoid_dual_arm: helper_mention_without_use;tool_necessity_miss;visual_uncertainty | 检查桌面布局，确认目标物品的具体位置：右侧有一瓶农夫山泉矿泉水，中间偏右有一个红苹果，左侧有白色盘子及散落零食。; 右手稳定抓取桌上的矿泉水瓶身或瓶颈处。; 左手同时抓起桌上的红苹果（作为食物），或者绿色小盒子；随后携带这两样物品前往客厅交付给聊天的人群。 利用双臂协同能力，在一次行程中分别拿取液体和固体食品，避免多次往返搬运零散的小包装零食（因难以稳定抓取）。 确保水瓶握持稳固以防泼洒；苹果作为独立物体易于抓握且不易滚动掉落。不尝试直接抓取电脑上一堆松散分离的零食包装...

## Top Prompted Improvement Cases
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_qwen3_5_35b: natural_free_plan fail -> tool_prior_free_plan pass
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_qwen3_5_35b: natural_free_plan fail -> tool_prior_free_plan pass
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_qwen3_5_35b: natural_free_plan fail -> tool_prior_free_plan pass
- task_005 / Weixin Image_20260629231743_399_27.jpg / ollama_qwen3_5_35b: natural_free_plan fail -> tool_prior_free_plan pass
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_qwen3_5_35b: natural_free_plan fail -> tool_prior_free_plan pass
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_qwen3_5_35b: natural_free_plan fail -> tool_prior_free_plan pass
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_qwen3_5_35b: natural_free_plan fail -> tool_prior_free_plan pass
- task_005 / Weixin Image_20260629231743_399_27.jpg / ollama_qwen3_5_35b: natural_free_plan fail -> tool_prior_free_plan pass
- task_007 / Weixin Image_20260629231746_401_27.jpg / ollama_qwen3_5_35b: natural_free_plan_humanoid_dual_arm fail -> tool_prior_free_plan_humanoid_dual_arm pass
- task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / ollama_qwen3_5_35b: natural_free_plan_humanoid_dual_arm fail -> tool_prior_free_plan_humanoid_dual_arm pass

## Top Robust Failures Across Clean/Tool-Prior
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_qwen3_5_35b: clean and tool-prior both true_fail
- task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / ollama_qwen3_5_35b: clean and tool-prior both true_fail
- task_007 / Weixin Image_20260629231746_401_27.jpg / ollama_qwen3_5_35b: clean and tool-prior both true_fail
- task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / ollama_qwen3_5_35b: clean and tool-prior both true_fail
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_qwen3_5_35b: clean and tool-prior both true_fail
- task_003 / 372f92c1ce9c87231d199c1102dcf7b4.jpg / ollama_qwen3_5_35b: clean and tool-prior both true_fail
- task_007 / Weixin Image_20260629231746_401_27.jpg / ollama_qwen3_5_35b: clean and tool-prior both true_fail
- task_003 / 372f92c1ce9c87231d199c1102dcf7b4.jpg / ollama_qwen3_5_35b: clean and tool-prior both true_fail
- task_007 / Weixin Image_20260629231746_401_27.jpg / ollama_qwen3_5_35b: clean and tool-prior both true_fail
- task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / ollama_qwen3_5_35b: clean and tool-prior both true_fail

## Main Uncertainty Sources
- Image visibility of helpers/targets was not checked.
- Parse-recoverable outputs need manual interpretation.
- Some helper mentions may be background or conditional rather than committed use.
- Strong decomposition prompt rows may still need targeted label audit; see `label_inconsistency_audit.md` when available.
- Check `aggregate_findings.md` context usage warnings before interpreting long-prompt runs.

## Generated Files
- `aggregate_findings.md`: aggregate text-rereview metrics.
- `task_family_summary.csv`: per-task metrics.
- `model_prompt_matrix.csv`: per-model/prompt matrix.
- `prompt_intervention_delta.md`: clean vs tool-prior comparisons.
- `counterexample_candidates_ranked.md`: ranked clean failure candidates.
- `label_inconsistency_audit.md`: high-risk label consistency audit when generated by rereview.

## Warning
Automatic text rereview is not final paper evidence. Selected claims require image-level human review.
