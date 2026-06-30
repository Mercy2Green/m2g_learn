# Visual Review Cases

These cases are selected for human image-level verification. Text rereview is not final evidence.

## task_001 / aggregation_container

### VR006 - clean_counterexample

- Task instruction: 卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_001_multi_bottles_visible_container/Weixin Image_20260629231738_395_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'bag', 'box', 'basket']; search=False
- Model/prompt: ollama_qwen3_5_35b / efficient_safe_free_plan / generic
- Model output excerpt: Pick up a stable batch of water bottles from the table.; Navigate to the bedroom and place them down for the students.; Return to the table to grasp the remaining water bottles.; Deliver the second batch to the bedroom. Grouping multiple...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR007 - clean_counterexample

- Task instruction: 卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_001_multi_bottles_visible_container/Weixin Image_20260629231738_395_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'bag', 'box', 'basket']; search=False
- Model/prompt: ollama_qwen3_vl_30b_a3b_instruct_q4_K_M / natural_free_plan / generic
- Model output excerpt: 检查周围环境以确保路径畅通无阻。; 拿起最靠近自己的那瓶矿泉水。; 沿着规划的路线前往卧室。; 在卧室内找到同学并递送水瓶。 由于有多个水瓶需要运送，且目的地为卧室，需多次往返以完成任务。 优先搬运所有水瓶，以减少往返次数，提高效率。 搬运时保持平稳，避免水瓶倾倒或掉落造成滑倒风险。 不清楚卧室的具体位置和路径细节。 { "task_understanding": "将桌上的矿泉水瓶从当前位置运送到卧室，供正在打牌的同学解渴。", "plan": [ "检查周围环境以确...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR008 - clean_counterexample

- Task instruction: 卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_001_multi_bottles_visible_container/Weixin Image_20260629231738_395_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'bag', 'box', 'basket']; search=False
- Model/prompt: ollama_qwen3_vl_30b_a3b_instruct_q4_K_M / efficient_safe_free_plan / generic
- Model output excerpt: 检查周围环境，确认路径无障碍物。; 拿起最靠近自己的那瓶水。; 沿直线路径前往卧室。; 在卧室内找到同学并递送水瓶。; 返回原处，重复上述步骤，直到所有水瓶送达。 为了高效完成任务并确保安全，应分批搬运，并优先处理易取的物品。由于不确定具体路径，需在途中根据实际情况调整路线。 优先搬运距离近、易于抓取的物品，并规划最短路径以减少往返次数。 在移动过程中保持平稳，避免水瓶倾斜或掉落造成滑倒风险。 不清楚卧室的具体位置和路径细节，以及同学是否需要一次性全部送达。 { "ta...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_001 / physical_capacity

### VR016 - clean_counterexample

- Task instruction: 卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_001_multi_bottles_visible_container/Weixin Image_20260629231738_395_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'bag', 'box', 'basket']; search=False
- Model/prompt: ollama_gemma3_27b_it_q8_0 / natural_free_plan / generic
- Model output excerpt: Navigate to the table with the water bottles.; Grasp and lift one or more water bottles (depending on carrying capacity).; Navigate to the bedroom where the students are playing cards.; Place the water bottles within reach of the student...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss;physical_capacity_hallucination

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR017 - clean_counterexample

- Task instruction: 卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_001_multi_bottles_visible_container/Weixin Image_20260629231738_395_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'bag', 'box', 'basket']; search=False
- Model/prompt: ollama_gemma3_27b_it_q8_0 / efficient_safe_free_plan / generic
- Model output excerpt: Navigate to the table with the water bottles.; Grasp and lift all the water bottles.; Navigate to the bedroom where the students are playing cards.; Place the water bottles on a stable surface near the students. The image shows several b...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss;physical_capacity_hallucination

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR018 - clean_counterexample

- Task instruction: 卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_001_multi_bottles_visible_container/Weixin Image_20260629231738_395_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'bag', 'box', 'basket']; search=False
- Model/prompt: ollama_minicpm_v4_5_q8_0 / efficient_safe_free_plan / generic
- Model output excerpt: 识别并定位桌面上的矿泉水瓶（共7瓶）; 拿起所有矿泉水瓶，确保不遗漏任何一瓶; 前往卧室位置 任务要求尽快送水，一次性拿取所有矿泉水可以提高效率。 一次性拿取所有矿泉水以减少往返次数。 小心搬运，避免瓶子倾倒或掉落。 未明确卧室的具体位置和距离；未说明是否需要其他物品伴随。 { "task_understanding": "将桌上的矿泉水送到卧室给正在打牌的同学。", "plan": [ "识别并定位桌面上的矿泉水瓶（共7瓶）", "拿起所有矿泉水瓶，确保不遗漏任何一瓶...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss;physical_capacity_hallucination

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_002 / helper_search

### VR001 - clean_counterexample

- Task instruction: 卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_002_multi_bottles_no_visible_container/Weixin Image_20260629231739_396_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'bag', 'box', 'basket']; search=True
- Model/prompt: ollama_gemma3_27b_it_q8_0 / natural_free_plan / generic
- Model output excerpt: Navigate to the table with the water bottles.; Grasp and lift all the water bottles.; Navigate to the bedroom where the students are playing cards.; Place the water bottles within reach of the students. The image shows several water bott...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss;helper_search_failure;physical_capacity_hallucination

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR002 - clean_counterexample

- Task instruction: 卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_002_multi_bottles_no_visible_container/Weixin Image_20260629231739_396_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'bag', 'box', 'basket']; search=True
- Model/prompt: ollama_gemma3_27b_it_q8_0 / efficient_safe_free_plan / generic
- Model output excerpt: Navigate to the table with water bottles; Grasp and lift all water bottles simultaneously or sequentially, ensuring stable carrying.; Navigate to the bedroom where the students are playing cards.; Release the water bottles in a safe loca...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss;helper_search_failure;physical_capacity_hallucination

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR005 - clean_counterexample

- Task instruction: 卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_002_multi_bottles_no_visible_container/Weixin Image_20260629231739_396_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'bag', 'box', 'basket']; search=True
- Model/prompt: ollama_minicpm_v4_5_q8_0 / natural_free_plan / generic
- Model output excerpt: 拿起桌子右侧的矿泉水瓶; 前往卧室 尽量一次性拿够数量，减少往返次数。 确保瓶子稳固，避免倾倒或洒漏。 未明确卧室具体位置及同学人数和需求量。 { "task_understanding": "需要将桌上的矿泉水送到卧室给正在打牌的同学。", "plan": [ "拿起桌子右侧的矿泉水瓶", "前往卧室" ], "estimated_number_of_trips": "few", "efficiency_consideration": "尽量一次性拿够数量，减少往返次...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss;helper_search_failure

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_002 / reach_extension

### VR039 - uncertain_visual

- Task instruction: 卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_002_multi_bottles_no_visible_container/Weixin Image_20260629231739_396_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'bag', 'box', 'basket']; search=True
- Model/prompt: ollama_minicpm_v4_5_q8_0 / tool_prior_free_plan / generic
- Model output excerpt: 拿起桌子右侧的几瓶矿泉水; 前往卧室 直接从桌上拿取矿泉水是最高效、最安全的方式，因为物品摆放稳定且无需额外工具辅助。一次拿多瓶可以减少往返次数，提高效率。 直接拿取桌面上的水，避免额外移动或寻找工具的时间。桌上有多瓶水，一次可以拿多瓶以减少往返次数。 桌子上的物品摆放稳定，可以直接拿起矿泉水而无需借助其他工具。 未明确卧室的具体位置和距离，但假设在可步行范围内。未说明需要运送的水的确切数量，但从图片上看至少有六瓶。 { "task_understanding": "需...
- Rereview judgment: true_fail (medium); modes=helper_mention_without_use;tool_necessity_miss;visual_uncertainty

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_004 / aggregation_container

### VR010 - clean_counterexample

- Task instruction: 客厅里有几个人在聊天，请拿些喝的和吃的过去。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_004_snacks_drinks_tray/Weixin Image_20260629231742_398_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'basket', 'box']; search=False
- Model/prompt: ollama_gemma3_27b_it_q8_0 / natural_free_plan / generic
- Model output excerpt: Locate drink options (water bottle, potentially others not visible).; Locate snack options (variety of packaged snacks and an apple).; Select a reasonable quantity of both drinks and snacks considering the number of people chatting (assu...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR013 - clean_counterexample

- Task instruction: 客厅里有几个人在聊天，请拿些喝的和吃的过去。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_004_snacks_drinks_tray/Weixin Image_20260629231742_398_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'basket', 'box']; search=False
- Model/prompt: ollama_minicpm_v4_5_q8_0 / natural_free_plan / generic
- Model output excerpt: 识别桌面上的食物和饮料。 一次性拿够数量以减少往返次数。 确保所选物品在移动过程中不会掉落或损坏。 未明确客厅的具体位置和聊天的人数，需要根据实际情况调整携带的物品量。 { "task_understanding": "需要从这张桌子上的物品中选择一些食物和饮料，然后带到客厅给正在聊天的人们。", "plan": [ "识别桌面上的食物和饮料。" ], "estimated_number_of_trips": "single", "efficiency_consider...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR014 - clean_counterexample

- Task instruction: 客厅里有几个人在聊天，请拿些喝的和吃的过去。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_004_snacks_drinks_tray/Weixin Image_20260629231742_398_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'basket', 'box']; search=False
- Model/prompt: ollama_minicpm_v4_5_q8_0 / efficient_safe_free_plan / generic
- Model output excerpt: 检查桌子周围是否有其他可拿的食物或饮品，确保收集齐全。; 拿起桌面上的零食、苹果和矿泉水瓶。 桌面上有多种零食、一个苹果和一瓶矿泉水，这些是任务中提到的‘喝的’和‘吃的’。 一次性拿齐所有物品以减少往返次数。 确保物品稳固，避免在搬运过程中掉落。 未明确客厅的具体位置和聊天的人们的位置，需要先确认。 { "task_understanding": "需要将桌上的食物（零食、苹果）和饮料（矿泉水瓶）带到客厅给聊天的人们。", "plan": [ "检查桌子周围是否有其他可...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_004 / helper_mention_without_use

### VR022 - clean_counterexample

- Task instruction: 客厅里有几个人在聊天，请拿些喝的和吃的过去。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_004_snacks_drinks_tray/Weixin Image_20260629231742_398_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'basket', 'box']; search=False
- Model/prompt: ollama_gemma3_27b_it_q8_0 / efficient_safe_free_plan / generic
- Model output excerpt: Scan nearby area for obstacles before moving.; Locate and grasp a water bottle and an apple.; Navigate to the living room while carrying both items.; Place the water bottle and apple near the people chatting. Prioritizing a single trip w...
- Rereview judgment: true_fail (medium); modes=helper_mention_without_use;visual_uncertainty

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR023 - clean_counterexample

- Task instruction: 客厅里有几个人在聊天，请拿些喝的和吃的过去。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_004_snacks_drinks_tray/Weixin Image_20260629231742_398_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'basket', 'box']; search=False
- Model/prompt: ollama_qwen3_5_35b / efficient_safe_free_plan / generic
- Model output excerpt: 检查桌面物品摆放情况并确认抓取点; 拿起桌上的矿泉水瓶和红苹果; 抓起绿色包装盒及几包散落的零食; 携带所有物品前往客厅人群处 一次性拿走桌上所有的食物和水，避免多次往返。 抓取零食时注意不要碰倒旁边的水瓶或书本；手持物品需保持平衡以防掉落。 不确定绿色盒子里的具体内容（可能是饮料也可能是固体），也不确定人群具体位置，但默认在客厅方向。 { "task_understanding": "识别出桌面上有矿泉水、苹果和多种零食，任务是将这些食物和水带给客厅聊天的人群。",...
- Rereview judgment: true_fail (medium); modes=helper_mention_without_use;visual_uncertainty

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR024 - clean_counterexample

- Task instruction: 客厅里有几个人在聊天，请拿些喝的和吃的过去。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_004_snacks_drinks_tray/Weixin Image_20260629231742_398_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'basket', 'box']; search=False
- Model/prompt: ollama_qwen3_5_35b / efficient_safe_free_plan_humanoid_dual_arm / humanoid_dual_arm
- Model output excerpt: Step 1: Scan table to identify stable items suitable for transport, specifically the water bottle and apple.; Step 2: Grasp the water bottle with one hand (e.g., right) while simultaneously grasping the red apple or green box with the ot...
- Rereview judgment: true_fail (medium); modes=helper_mention_without_use;visual_uncertainty

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_005 / aggregation_container

### VR011 - clean_counterexample

- Task instruction: 请把这些用过的杯子和盘子收回厨房。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_005_used_cups_dishes/Weixin Image_20260629231743_399_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'basin', 'basket']; search=False
- Model/prompt: ollama_gemma3_27b_it_q8_0 / natural_free_plan / generic
- Model output excerpt: Locate all used cups and dishes on the table.; Pick up each cup/dish one by one.; Transport each item to the kitchen.; Repeat until all items are moved. The task requires moving multiple objects from one location (the table) to another (...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR012 - clean_counterexample

- Task instruction: 请把这些用过的杯子和盘子收回厨房。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_005_used_cups_dishes/Weixin Image_20260629231743_399_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'basin', 'basket']; search=False
- Model/prompt: ollama_gemma3_27b_it_q8_0 / efficient_safe_free_plan / generic
- Model output excerpt: 1. Scan the table to confirm the locations of all dirty dishes (cups, bowls).; 2. Grasp and lift each dish individually.; 3. Transport all grasped dishes to the kitchen.; 4. Release the dishes in the designated area within the kitchen. M...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR015 - clean_counterexample

- Task instruction: 请把这些用过的杯子和盘子收回厨房。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_005_used_cups_dishes/Weixin Image_20260629231743_399_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'basin', 'basket']; search=False
- Model/prompt: ollama_qwen3_vl_30b_a3b_instruct_q4_K_M / natural_free_plan / generic
- Model output excerpt: 检查桌子上的所有物品，确认哪些是用过的杯子和盘子。; 从桌子上拿起用过的白色碗、不锈钢碗和杯子。; 将这些餐具移出当前区域，前往厨房。; 在厨房内找到合适的存放位置（如水槽或橱柜）并放置好餐具。 为了高效完成任务并保证安全，需要先确认所有待收拾的餐具，并在搬运过程中保持稳定。 一次性尽可能多地收集所有用过的餐具，减少往返次数。 搬运时确保物品稳定，避免掉落或打翻。 不清楚厨房的具体位置和存放区域是否已明确。 { "task_understanding": "将桌上的用过...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_005 / helper_mention_without_use

### VR028 - robust_failure

- Task instruction: 请把这些用过的杯子和盘子收回厨房。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_005_used_cups_dishes/Weixin Image_20260629231743_399_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'basin', 'basket']; search=False
- Model/prompt: ollama_qwen3_vl_32b_instruct_q4_K_M / natural_free_plan / generic
- Model output excerpt: 检查桌面所有餐具（包括白色瓷碗、不锈钢碗、带勺子的小杯、金属保温杯等）是否为待回收物品; 将这些餐具小心地集中放置在便于搬运的位置（如靠近桌边）; 携带收集好的餐具前往厨房区域; 将餐具放入厨房水槽或指定清洗区 根据图像可见桌面有多件使用过的碗、杯和盘子，任务目标是收回厨房。一次性搬运可提升效率，但需注意安全性和稳定性。由于未提供厨房位置及物品分类要求，存在部分不确定性。 一次性收集所有物品可减少往返次数，提高效率；需确保搬运过程中不掉落或碰撞。 金属保温杯内可能有残留...
- Rereview judgment: true_fail (medium); modes=helper_mention_without_use;visual_uncertainty

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR029 - robust_failure

- Task instruction: 请把这些用过的杯子和盘子收回厨房。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_005_used_cups_dishes/Weixin Image_20260629231743_399_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'basin', 'basket']; search=False
- Model/prompt: ollama_qwen3_vl_32b_instruct_q4_K_M / natural_free_plan_humanoid_dual_arm / humanoid_dual_arm
- Model output excerpt: 检查桌面所有餐具，确认需要回收的物品：白色带勺小杯、两个白色瓷碗、一个不锈钢碗、一个金属保温杯。; 使用双手分别抓取两组物品（例如左手拿小杯和一个白碗，右手拿另一个白碗和不锈钢碗），避免一次携带过多导致不稳定。; 将收集到的餐具移至厨房区域，放置在水槽或指定清洗区。; 若金属保温杯内有液体残留，需先倾倒再回收；如无法一次性完成，则分批处理。 桌面存在多个可回收餐具，部分为易滑或带液体的容器，需分批安全搬运。同时考虑效率与稳定性，避免一次携带过多导致掉落风险。 优先组合轻...
- Rereview judgment: true_fail (medium); modes=helper_mention_without_use;visual_uncertainty

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_005 / physical_capacity

### VR030 - robust_failure

- Task instruction: 请把这些用过的杯子和盘子收回厨房。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_005_used_cups_dishes/Weixin Image_20260629231743_399_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'basin', 'basket']; search=False
- Model/prompt: ollama_qwen3_vl_30b_a3b_instruct_q4_K_M / natural_free_plan_humanoid_dual_arm / humanoid_dual_arm
- Model output excerpt: 检查桌上所有可用的杯子和盘子，确认哪些是需要回收的。; 先拿起金属碗和白色瓷碗，确保它们稳定抓取。; 同时拿起带勺子的白色杯子和不锈钢保温杯。; 将这些物品集中放置在桌面一侧，准备一次性搬运。; 从桌面上拿起所有收集好的用过的杯子和盘子，离开当前区域前往厨房。; 进入厨房后，将物品放入水槽或指定收纳区。 桌面上的杯子和盘子数量有限且集中，可通过一次搬运完成任务；同时使用双臂可提高效率，并确保物品在移动过程中稳定。 尽量一次性搬运所有可用的杯子和盘子，减少往返次数以提高效...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss;physical_capacity_hallucination

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_006 / other

### VR033 - prompted_improvement

- Task instruction: 请把地上的小东西收起来。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_006_scattered_small_objects/Weixin Image_20260629231745_400_27.jpg
- Expected helper/tool behavior: use=True; types=['box', 'dustpan', 'broom', 'basket']; search=False
- Model/prompt: ollama_gemma3_27b_it_q8_0 / tool_prior_free_plan_humanoid_dual_arm / humanoid_dual_arm
- Model output excerpt: 1. Scan the area to identify all small objects needing collection.; 2. Pick up the blister packs of pills (two sets) with one hand each, and place them into the trash can.; 3. Pick up the snack packages (three items) with one hand each,...
- Rereview judgment: true_pass (high); modes=

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR034 - prompted_improvement

- Task instruction: 请把地上的小东西收起来。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_006_scattered_small_objects/Weixin Image_20260629231745_400_27.jpg
- Expected helper/tool behavior: use=True; types=['box', 'dustpan', 'broom', 'basket']; search=False
- Model/prompt: ollama_minicpm_v4_5_q8_0 / tool_prior_free_plan_quadruped_single_arm / quadruped_single_arm
- Model output excerpt: 检查地面所有小物件的位置，确认哪些是需要收集的目标物体。; 使用机械臂和夹爪逐一拾取每个目标物体，并将其放入篮子中。 任务目标是将所有散落的小物件收集起来。由于物品分散且数量较多，需要逐一拾取并放入篮子中。考虑到机械臂和夹爪的操作限制以及环境中的可达性问题，计划优先检查每个物体的位置，并根据实际情况选择直接操作或使用辅助工具（如篮子本身作为容器）以提高效率和安全性。 由于物品分散且数量较多，可能需要多次往返以完成任务；优先考虑直接操作简单、安全的物件。 保持身体平衡，在...
- Rereview judgment: true_pass (high); modes=

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_006 / reach_extension

### VR038 - uncertain_visual

- Task instruction: 请把地上的小东西收起来。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_006_scattered_small_objects/Weixin Image_20260629231745_400_27.jpg
- Expected helper/tool behavior: use=True; types=['box', 'dustpan', 'broom', 'basket']; search=False
- Model/prompt: ollama_gemma3_27b_it_q8_0 / tool_prior_free_plan_quadruped_single_arm / quadruped_single_arm
- Model output excerpt: 1. Approach the area with scattered items and perform a visual scan to confirm object locations and identify potential obstacles.; 2. Pick up each individual item one by one using the gripper and transport it to the trash can.; 3. Deposi...
- Rereview judgment: true_fail (medium); modes=helper_mention_without_use;tool_necessity_miss;visual_uncertainty

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_007 / aggregation_container

### VR019 - clean_counterexample

- Task instruction: 请把这些衣服收起来，拿到洗衣区。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_007_laundry_basket/Weixin Image_20260629231746_401_27.jpg
- Expected helper/tool behavior: use=True; types=['laundry basket', 'storage box', 'basket']; search=False
- Model/prompt: ollama_minicpm_v4_5_q8_0 / natural_free_plan / generic
- Model output excerpt: 识别并收集椅子上悬挂和放置的所有衣物，包括绿色条纹衫、深蓝色T恤以及椅背上的衣物。确认所有衣物已被取下。; 将这些衣物放入旁边的白色洗衣篮中。 任务要求将所有衣物收拾到洗衣篮中，因此需先收集并确认衣物数量后进行转移操作。 一次性收集并转移所有衣物以提高效率，避免多次往返。 确保在移动过程中不会掉落或损坏衣物，并注意周围环境的安全。 未明确洗衣区的具体位置和距离。需要根据现有信息判断是否能直接到达。 { "task_understanding": "将椅子上的衣物和地面上...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR020 - clean_counterexample

- Task instruction: 请把这些衣服收起来，拿到洗衣区。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_007_laundry_basket/Weixin Image_20260629231746_401_27.jpg
- Expected helper/tool behavior: use=True; types=['laundry basket', 'storage box', 'basket']; search=False
- Model/prompt: ollama_minicpm_v4_5_q8_0 / efficient_safe_free_plan / generic
- Model output excerpt: 检查椅子上是否有更多需要整理的衣物，确保所有衣物都被识别并准备收起。; 逐一取下椅子上的衣物（包括挂在椅背、椅座上的），并将它们叠放整齐或直接放入洗衣篮。注意避免衣物掉落和缠绕。; 将地面上的衣物拾起，并与椅子上收集到的衣物一起放入洗衣篮中，确保所有衣物都被收纳进洗衣篮内。 一次性完成所有衣物的整理和转移，减少往返次数。 在取下椅背上的衣物时注意平衡，避免椅子倾倒或衣物掉落。 { "task_understanding": "将椅子上的衣物和地面上的衣物收集起来，并移动...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR021 - clean_counterexample

- Task instruction: 请把这些衣服收起来，拿到洗衣区。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_007_laundry_basket/Weixin Image_20260629231746_401_27.jpg
- Expected helper/tool behavior: use=True; types=['laundry basket', 'storage box', 'basket']; search=False
- Model/prompt: ollama_qwen3_vl_30b_a3b_instruct_q4_K_M / efficient_safe_free_plan / generic
- Model output excerpt: 检查周围环境以确保路径无障碍; 拿起椅子上悬挂的绿色条纹短袖和深蓝色长袖; 拿起椅子上堆放的绿色条纹裤子和深蓝色T恤; 确认所有衣物已从椅子上取下; 将收集到的衣物放入洗衣篮中; 携带装有衣物的洗衣篮前往洗衣区 所有衣物均位于同一区域且数量适中，可一次性收集并运送至洗衣区，无需多次往返。 一次性完成所有衣物的收集与运送，减少往返次数以提高效率 搬运过程中保持平衡，避免衣物掉落或碰撞到其他物体 洗衣区的具体位置未明确，需根据环境判断最佳路径 {"task_understa...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_007 / other

### VR035 - prompted_improvement

- Task instruction: 请把这些衣服收起来，拿到洗衣区。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_007_laundry_basket/Weixin Image_20260629231746_401_27.jpg
- Expected helper/tool behavior: use=True; types=['laundry basket', 'storage box', 'basket']; search=False
- Model/prompt: ollama_gemma3_27b_it_q8_0 / tool_prior_free_plan / generic
- Model output excerpt: Locate and grasp the green striped shirt.; Locate and grasp the blue hoodie.; Locate and grasp the black t-shirt.; Locate and grasp the clothes in the white basket.; Transport all collected clothes to the laundry area. Direct manipulatio...
- Rereview judgment: true_pass (high); modes=

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_007 / physical_capacity

### VR031 - robust_failure

- Task instruction: 请把这些衣服收起来，拿到洗衣区。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_007_laundry_basket/Weixin Image_20260629231746_401_27.jpg
- Expected helper/tool behavior: use=True; types=['laundry basket', 'storage box', 'basket']; search=False
- Model/prompt: ollama_qwen3_vl_30b_a3b_instruct_q4_K_M / natural_free_plan / generic
- Model output excerpt: 检查周围环境以确保路径畅通无阻。; 从椅子上拿起所有衣物（包括条纹衫和深蓝色T恤）。; 确认所有衣物都已拾取后，前往洗衣区。; 将衣物放入洗衣区的指定位置。 图像显示所有衣物都集中在椅子上，且距离洗衣篮较近，因此可以一次性完成收集和运送任务。 一次性完成任务以减少移动次数。 确保在搬运过程中衣物不会掉落，保持平稳移动。 洗衣区的具体位置未知，需根据环境判断方向。 { "task_understanding": "将椅子上的衣物收集并运送到洗衣区。", "plan": [...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss;physical_capacity_hallucination

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR037 - uncertain_visual

- Task instruction: 请把这些衣服收起来，拿到洗衣区。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_007_laundry_basket/Weixin Image_20260629231746_401_27.jpg
- Expected helper/tool behavior: use=True; types=['laundry basket', 'storage box', 'basket']; search=False
- Model/prompt: ollama_qwen3_vl_30b_a3b_instruct_q4_K_M / tool_prior_free_plan / generic
- Model output excerpt: 检查周围环境以确认路径无障碍物。; 从椅子上拿起所有衣物，包括条纹短袖、深蓝色T恤和裤子。; 将收集的衣物放入旁边的白色塑料篮中。; 提起装有衣物的塑料篮，前往洗衣区。 直接操作是最佳选择，因为椅子上的衣物可以一次性收集并装入现成的塑料篮中。该篮子作为工具可提升效率和安全性，无需额外辅助物或多次往返。 使用旁边的塑料篮作为容器可以一次性携带所有衣物，减少往返次数，提高效率。 将衣物放入篮中可防止掉落，并确保搬运过程中的稳定性。 洗衣区的具体位置未知，但假设其在机器人可达...
- Rereview judgment: true_fail (medium); modes=helper_mention_without_use;physical_capacity_hallucination;visual_uncertainty

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_008 / reach_extension

### VR003 - clean_counterexample

- Task instruction: 请把沙发下面的遥控器拿出来。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_008_remote_under_sofa/af09e19db8fd93d51875f3e63c5fea96.jpg
- Expected helper/tool behavior: use=True; types=['broom', 'stick', 'rod']; search=False
- Model/prompt: ollama_gemma3_27b_it_q8_0 / natural_free_plan / generic
- Model output excerpt: Approach the sofa.; Check for obstacles around the sofa legs.; Reach under the sofa to grasp the remote control.; Withdraw the remote control from under the sofa.; Present the remote control. The task requires navigating to the sofa, ide...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR004 - clean_counterexample

- Task instruction: 请把沙发下面的遥控器拿出来。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_008_remote_under_sofa/af09e19db8fd93d51875f3e63c5fea96.jpg
- Expected helper/tool behavior: use=True; types=['broom', 'stick', 'rod']; search=False
- Model/prompt: ollama_gemma3_27b_it_q8_0 / efficient_safe_free_plan / generic
- Model output excerpt: Approach the sofa from a clear angle.; Extend arm/manipulator to reach under the sofa and grasp the remote control.; Retract arm/manipulator with the remote control.; Present the remote control. A single, direct approach with a careful e...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR009 - clean_counterexample

- Task instruction: 请把沙发下面的遥控器拿出来。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_008_remote_under_sofa/af09e19db8fd93d51875f3e63c5fea96.jpg
- Expected helper/tool behavior: use=True; types=['broom', 'stick', 'rod']; search=False
- Model/prompt: ollama_qwen3_vl_30b_a3b_instruct_q4_K_M / natural_free_plan / generic
- Model output excerpt: 检查沙发下方区域，确认遥控器的位置和周围环境。; 将身体或机械臂移动到靠近遥控器的位置。; 伸出机械臂并小心地抓取遥控器。; 平稳地将遥控器从沙发下拉出。 由于任务明确且环境相对简单，机器人可以一次性完成任务。但需要确保动作平稳以避免损坏家具或物品。 优先使用最短路径接近目标，避免不必要的移动以节省时间。 在操作过程中保持稳定，防止碰撞或翻倒沙发。 无法确定遥控器是否被其他物体遮挡，需先检查清楚。 { "task_understanding": "从沙发下方取出遥控器。...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_009 / aggregation_container

### VR025 - clean_counterexample

- Task instruction: 这里有点脏，请清理一下。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_009_dirty_floor_or_table/Weixin Image_20260629231751_404_27.jpg
- Expected helper/tool behavior: use=True; types=['tissue', 'cloth', 'broom', 'dustpan']; search=False
- Model/prompt: ollama_gemma3_27b_it_q8_0 / natural_free_plan / generic
- Model output excerpt: Scan the area to confirm all debris locations and identify any obstacles.; Navigate to each piece of crumpled paper.; Pick up each piece of crumpled paper.; Navigate to the trash can (visible in the image).; Deposit the crumpled paper in...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

### VR026 - clean_counterexample

- Task instruction: 这里有点脏，请清理一下。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_009_dirty_floor_or_table/Weixin Image_20260629231751_404_27.jpg
- Expected helper/tool behavior: use=True; types=['tissue', 'cloth', 'broom', 'dustpan']; search=False
- Model/prompt: ollama_gemma3_27b_it_q8_0 / efficient_safe_free_plan / generic
- Model output excerpt: 1. Scan the area for any obstacles or hazards before starting cleaning.; 2. Navigate to the location of the crumpled papers.; 3. Collect all visible crumpled papers and store them in the trash can (located near the toilet).; 4. Re-scan t...
- Rereview judgment: true_fail (high); modes=aggregation_failure;container_affordance_miss

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_009 / other

### VR036 - prompted_improvement

- Task instruction: 这里有点脏，请清理一下。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_009_dirty_floor_or_table/Weixin Image_20260629231751_404_27.jpg
- Expected helper/tool behavior: use=True; types=['tissue', 'cloth', 'broom', 'dustpan']; search=False
- Model/prompt: ollama_minicpm_v4_5_q8_0 / tool_prior_free_plan_humanoid_dual_arm / humanoid_dual_arm
- Model output excerpt: 检查附近是否有可以作为工具或辅助物的物体; 如果存在合适的工具（如扫帚、簸箕），使用它们来收集和处理纸屑；如果没有，则直接用手捡起并丢弃到垃圾桶中 根据环境中的物体判断是否使用工具，以提高效率并确保操作安全。 优先考虑是否可以利用现有工具提高清理效率，减少往返次数。 确保在操作过程中不会因弯腰或伸手而造成身体不适或物品掉落。 需要确认附近是否有合适的清洁工具（如扫帚、簸箕）以及垃圾桶的位置和可接近性。 { "task_understanding": "需要清理地面上的纸...
- Rereview judgment: true_pass (high); modes=

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_009 / reach_extension

### VR040 - uncertain_visual

- Task instruction: 这里有点脏，请清理一下。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_009_dirty_floor_or_table/Weixin Image_20260629231751_404_27.jpg
- Expected helper/tool behavior: use=True; types=['tissue', 'cloth', 'broom', 'dustpan']; search=False
- Model/prompt: ollama_gemma3_27b_it_q8_0 / tool_prior_free_plan / generic
- Model output excerpt: Locate and approach the nearest piece of crumpled paper.; Pick up the crumpled paper and move it towards the trash can.; Repeat steps 1 and 2 for all visible pieces of crumpled paper.; Confirm that all visible debris has been removed. Di...
- Rereview judgment: true_fail (medium); modes=helper_mention_without_use;tool_necessity_miss;visual_uncertainty

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_009 / wrong_helper_type

### VR027 - clean_counterexample

- Task instruction: 这里有点脏，请清理一下。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_009_dirty_floor_or_table/Weixin Image_20260629231751_404_27.jpg
- Expected helper/tool behavior: use=True; types=['tissue', 'cloth', 'broom', 'dustpan']; search=False
- Model/prompt: ollama_minicpm_v4_5_q8_0 / natural_free_plan_humanoid_dual_arm / humanoid_dual_arm
- Model output excerpt: 检查附近是否有合适的容器或垃圾袋来收集纸屑; 使用夹爪逐一拾取地上的纸屑并放入容器中; 重复上述步骤直到所有可见纸屑都被清理完毕 通过逐一拾取并集中处理，可以有效避免遗漏和混乱。 尽量减少移动次数，提高清洁效率。 确保在拾取过程中不会因地面湿滑或不稳定而摔倒。 需要确认附近是否有足够的容器来容纳所有纸屑；如果容器不足，则可能需要多次往返。 { "task_understanding": "需要清理地面上的纸屑，使地面干净。", "plan": [ "检查附近是否有合适的...
- Rereview judgment: true_fail (high); modes=wrong_helper_type

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?

## task_010 / helper_mention_without_use

### VR032 - robust_failure

- Task instruction: 请把这些东西安全拿到餐桌上。
- Image path: /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark/images/task_010_fragile_objects/Weixin Image_20260629231750_403_27.jpg
- Expected helper/tool behavior: use=True; types=['tray', 'box', 'padded box']; search=False
- Model/prompt: ollama_qwen3_vl_30b_a3b_instruct_q4_K_M / natural_free_plan / generic
- Model output excerpt: 检查周围环境，确认餐桌位置和路径无障碍物。; 逐一拾取鸡蛋，并小心放置在餐桌上。; 将塑料蛋托拿起并放在餐桌上。; 拿起金属碗并移动到餐桌上。; 将遥控器、JBL音箱和纸巾盒依次搬到餐桌上。; 整理桌面上的物品，确保摆放整齐且安全。 为了确保所有物品安全、有序地转移到餐桌上，同时减少不必要的移动次数以提高效率。 优先搬运易碎品（如鸡蛋），减少移动次数以提高效率。 搬运过程中避免碰撞或掉落，特别是鸡蛋和金属碗等易碎物品。 未明确餐桌的具体位置和大小，需根据实际情况调整搬运...
- Rereview judgment: true_fail (medium); modes=helper_mention_without_use;visual_uncertainty

Human checks:
- [ ] Is the target object visible?
- [ ] Is the expected helper visible?
- [ ] If helper is not visible, is searching for one reasonable?
- [ ] Is the expected helper/tool type reasonable for this task?
- [ ] Is the model plan physically feasible for the stated embodiment?
- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?
- [ ] Can this case be safely used as paper evidence?
