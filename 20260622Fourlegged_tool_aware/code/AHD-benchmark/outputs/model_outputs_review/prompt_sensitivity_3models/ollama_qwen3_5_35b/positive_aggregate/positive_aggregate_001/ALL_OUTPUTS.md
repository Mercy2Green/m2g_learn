# positive_aggregate_001: All Candidate Outputs

This page contains raw candidate-model responses only.

## single_turn_multi_image | multi_image__efficient_safe_free_plan

Detailed file: [`single_turn_multi_image/multi_image__efficient_safe_free_plan.md`](./single_turn_multi_image/multi_image__efficient_safe_free_plan.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__efficient_safe_free_plan`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个家庭移动机器人。请根据图像和任务，给出尽量高效、安全、减少往返次数的高层计划。
不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
(empty)
```

## single_turn_multi_image | multi_image__efficient_safe_free_plan_humanoid_dual_arm

Detailed file: [`single_turn_multi_image/multi_image__efficient_safe_free_plan_humanoid_dual_arm.md`](./single_turn_multi_image/multi_image__efficient_safe_free_plan_humanoid_dual_arm.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__efficient_safe_free_plan_humanoid_dual_arm`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个有两个手臂和两个手/夹爪的家用人形机器人。
你可以同时使用两只手，但每只手通常只能稳定拿住一个普通小物体，或一个物理上稳定的抓取组合。
不要假设你可以直接拿住许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设手臂一定能直接够到目标物体。
请给出尽量高效、安全、减少往返次数的高层可执行计划。
不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶饮料全部运送至卧室供同学饮用",
  "plan": [
    "确认所有瓶子均为可稳定抓取的普通塑料瓶且无遮挡物",
    "用双手同时抓取左右各1瓶（共2瓶）并搬运至卧室放置区",
    "重复上述步骤直至剩余3瓶，最后一次单手持握最后1瓶完成运送"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "每次最大化利用双手机械臂容量（2瓶/次），7瓶需4趟往返（3×2+1）为理论最优解",
  "safety_or_stability_consideration": "逐个稳定抓取避免碰撞台面边缘，移动时保持手臂平稳防止倾倒液体",
  "uncertainty_or_missing_information": "未明确卧室具体位置及路径障碍物情况；部分瓶子可能因标签反光影响视觉定位"
}
```

## single_turn_multi_image | multi_image__efficient_safe_free_plan_quadruped_single_arm

Detailed file: [`single_turn_multi_image/multi_image__efficient_safe_free_plan_quadruped_single_arm.md`](./single_turn_multi_image/multi_image__efficient_safe_free_plan_quadruped_single_arm.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__efficient_safe_free_plan_quadruped_single_arm`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个有四足移动底盘、一个安装机械臂和一个夹爪的家用机器人。
移动时必须保持身体平衡。
夹爪通常一次只能稳定携带一个普通小物体；只有在物体物理上紧密成组且稳定时，才可携带极少量组合物体。
不要假设你可以直接携带许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设机械臂一定能直接够到目标物体。
请给出尽量高效、安全、减少往返次数的高层可执行计划。
不要输出低层关节或步态动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上排列的七瓶饮料逐一运送至卧室供同学饮用",
  "plan": [
    "移动到台面边缘定位第一瓶黄色饮料",
    "使用夹爪稳定抓取单瓶并移动至卧室入口",
    "重复执行搬运动作直至所有瓶子送达"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "按颜色顺序依次搬运减少路径交叉，优先处理最易抓取的直立瓶身",
  "safety_or_stability_consideration": "每次仅携带单瓶确保夹持稳定，移动时保持底盘平衡避免倾倒液体",
  "uncertainty_or_missing_information": "未确认卧室具体方位及内部障碍物分布"
}
```

## single_turn_multi_image | multi_image__natural_free_plan

Detailed file: [`single_turn_multi_image/multi_image__natural_free_plan.md`](./single_turn_multi_image/multi_image__natural_free_plan.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__natural_free_plan`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个家庭移动机器人。请根据图像和任务，给出可执行的高层计划。
不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶彩色饮料运送至有同学在打牌的卧室",
  "plan": [
    "确认所有瓶子可安全抓取（无易碎标签）", 
    "双手各持3-4瓶分两趟搬运", 
    "沿最短路径移动并避开台面障碍物"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "采用双臂协同运输减少往返次数，优先抓取边缘瓶子避免碰撞中间物品",
  "safety_or_stability_consideration": "保持低重心行走速度，转弯时减速防止倾倒饮料瓶或触碰台灯/遥控器",
  "uncertainty_or_missing_information": "未确认卧室具体方位及路径障碍物情况"
}
```

## single_turn_multi_image | multi_image__natural_free_plan_humanoid_dual_arm

Detailed file: [`single_turn_multi_image/multi_image__natural_free_plan_humanoid_dual_arm.md`](./single_turn_multi_image/multi_image__natural_free_plan_humanoid_dual_arm.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__natural_free_plan_humanoid_dual_arm`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个有两个手臂和两个手/夹爪的家用人形机器人。
你可以同时使用两只手，但每只手通常只能稳定拿住一个普通小物体，或一个物理上稳定的抓取组合。
不要假设你可以直接拿住许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设手臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶饮料分批运送至卧室供同学饮用",
  "plan": [
    "移动到台面区域确认所有瓶子位置及间距",
    "双手各抓一瓶最外侧的蓝色和橙色瓶装水，搬运至卧室并放置",
    "返回重复抓取剩余5瓶（分3次完成：2+2+1）"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "优先选择边缘易抓取的瓶子减少调整时间，保持双手平衡移动避免碰撞台面物品",
  "safety_or_stability_consideration": "确保夹爪垂直握持瓶身中部防止倾倒，搬运时避开台面上的遥控器和杯子等障碍物",
  "uncertainty_or_missing_information": "未明确卧室具体位置及路径障碍情况，假设通道畅通无阻",
  "reason": "基于机器人双抓手能力限制（单次最多稳定抓取2个独立物体），需分批次运输；台面物品布局允许直接抓取无需额外清理步骤"
}
```

## single_turn_multi_image | multi_image__natural_free_plan_quadruped_single_arm

Detailed file: [`single_turn_multi_image/multi_image__natural_free_plan_quadruped_single_arm.md`](./single_turn_multi_image/multi_image__natural_free_plan_quadruped_single_arm.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__natural_free_plan_quadruped_single_arm`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个有四足移动底盘、一个安装机械臂和一个夹爪的家用机器人。
移动时必须保持身体平衡。
夹爪通常一次只能稳定携带一个普通小物体；只有在物体物理上紧密成组且稳定时，才可携带极少量组合物体。
不要假设你可以直接携带许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设机械臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节或步态动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "需要将台面上7个独立瓶装水逐一送至卧室供同学饮用",
  "plan": [
    "环视确认厨房至卧室路径无障碍物及障碍物高度信息",
    "依次逐个抓取台面饮料瓶并运送至卧室桌面区域",
    "重复搬运直至所有瓶子送达"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "单次仅能稳定携带1个独立物体，需多次往返完成运输任务",
  "safety_or_stability_consideration": "移动时需保持四足底盘平衡状态，夹爪抓取时确保单瓶稳固不滑落",
  "uncertainty_or_missing_information": "未确认卧室桌面是否已有足够放置空间容纳所有饮料"
}
```

## single_turn_multi_image | multi_image__search_explicit_strong_decomposition_free_plan

Detailed file: [`single_turn_multi_image/multi_image__search_explicit_strong_decomposition_free_plan.md`](./single_turn_multi_image/multi_image__search_explicit_strong_decomposition_free_plan.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__search_explicit_strong_decomposition_free_plan`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个家庭移动机器人。请根据图像和任务，给出可执行的高层计划。
不要输出低层关节动作。

注意：当前图像只是机器人当前视野，不代表完整环境。
你可以规划短程检查附近区域，例如相邻台面、柜边、地面、桌旁或当前房间内的近处区域。
短程搜索必须服务于当前任务目标，不要进行无目的探索。

在制定计划前，请系统检查以下问题：
1. 当前任务真正要操作、移动、收纳、取出或清理的目标物是什么？
2. 图像中是否存在除目标物之外、可能帮助完成任务的辅助物体？
3. 这些辅助物体是否能够提升任务的效率、安全性、稳定性、可达性，或者减少往返次数？
4. 如果任务涉及多个松散物体、易掉落物体、狭窄空间中的目标物、清理/收纳任务，而当前视野中没有明显合适的辅助物体，请判断是否应该先短程寻找一个合适辅助物体。
5. 如果短程搜索是必要的，计划中必须明确写出：先检查附近区域寻找合适辅助物体，再使用该辅助物体完成目标任务。
6. 对每个当前可见或计划短程寻找的辅助物体，判断它是有帮助、无关、还是不适合当前任务。
7. 只有当直接操作明显更简单、更安全、更稳定，并且不会显著增加往返次数或掉落风险时，才选择直接操作。
8. 如果使用辅助物体，计划中必须体现完整顺序：先获得或准备辅助物体，再让辅助物体作用于目标物，最后完成搬运、取出、收纳或清理。
9. 如果不使用辅助物体，请在原因中说明为什么直接操作已经足够，以及为什么不需要短程寻找辅助物体。

输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
(empty)
```

## single_turn_multi_image | multi_image__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm

Detailed file: [`single_turn_multi_image/multi_image__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm.md`](./single_turn_multi_image/multi_image__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个有两个手臂和两个手/夹爪的家用人形机器人。
你可以同时使用两只手，但每只手通常只能稳定拿住一个普通小物体，或一个物理上稳定的抓取组合。
不要假设你可以直接拿住许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设手臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节动作。

注意：当前图像只是机器人当前视野，不代表完整环境。
你可以规划短程检查附近区域，例如相邻台面、柜边、地面、桌旁或当前房间内的近处区域。
短程搜索必须服务于当前任务目标，不要进行无目的探索。

在制定计划前，请系统检查以下问题：
1. 当前任务真正要操作、移动、收纳、取出或清理的目标物是什么？
2. 图像中是否存在除目标物之外、可能帮助完成任务的辅助物体？
3. 这些辅助物体是否能够提升任务的效率、安全性、稳定性、可达性，或者减少往返次数？
4. 如果任务涉及多个松散物体、易掉落物体、狭窄空间中的目标物、清理/收纳任务，而当前视野中没有明显合适的辅助物体，请判断是否应该先短程寻找一个合适辅助物体。
5. 如果短程搜索是必要的，计划中必须明确写出：先检查附近区域寻找合适辅助物体，再使用该辅助物体完成目标任务。
6. 对每个当前可见或计划短程寻找的辅助物体，判断它是有帮助、无关、还是不适合当前任务。
7. 只有当双手直接操作明显更简单、更安全、更稳定，并且不会显著增加往返次数或掉落风险时，才选择直接操作。
8. 如果使用辅助物体，计划中必须体现完整顺序：先获得或准备辅助物体，再让辅助物体作用于目标物，最后完成搬运、取出、收纳或清理。
9. 如果不使用辅助物体，请在原因中说明为什么直接操作已经足够，以及为什么不需要短程寻找辅助物体。

输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料送至卧室供同学饮用",
  "plan": [
    "检查台面周围区域寻找托盘或收纳容器作为辅助搬运工具",
    "若找到合适容器则分批装载所有瓶子，否则双手各持一瓶分四次运送",
    "确保每次抓取时保持瓶子稳定不滑落"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "优先使用辅助工具减少往返次数，若无可用工具则采用双瓶并行搬运策略",
  "safety_or_stability_consideration": "避免单手抓取多个瓶子导致倾倒风险，确保每次移动时重心稳定",
  "uncertainty_or_missing_information": "未确认厨房内是否存在托盘等收纳容器，需短程搜索验证"
}
```

## single_turn_multi_image | multi_image__search_explicit_strong_decomposition_free_plan_quadruped_single_arm

Detailed file: [`single_turn_multi_image/multi_image__search_explicit_strong_decomposition_free_plan_quadruped_single_arm.md`](./single_turn_multi_image/multi_image__search_explicit_strong_decomposition_free_plan_quadruped_single_arm.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__search_explicit_strong_decomposition_free_plan_quadruped_single_arm`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个有四足移动底盘、一个安装机械臂和一个夹爪的家用机器人。
移动时必须保持身体平衡。
夹爪通常一次只能稳定携带一个普通小物体；只有在物体物理上紧密成组且稳定时，才可携带极少量组合物体。
不要假设你可以直接携带许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设机械臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节或步态动作。

注意：当前图像只是机器人当前视野，不代表完整环境。
你可以规划短程检查附近区域，例如相邻台面、柜边、地面、桌旁或当前房间内的近处区域。
短程搜索必须服务于当前任务目标，不要进行无目的探索。

在制定计划前，请系统检查以下问题：
1. 当前任务真正要操作、移动、收纳、取出或清理的目标物是什么？
2. 图像中是否存在除目标物之外、可能帮助完成任务的辅助物体？
3. 这些辅助物体是否能够提升任务的效率、安全性、稳定性、可达性，或者减少往返次数？
4. 如果任务涉及多个松散物体、易掉落物体、狭窄空间中的目标物、清理/收纳任务，而当前视野中没有明显合适的辅助物体，请判断是否应该先短程寻找一个合适辅助物体。
5. 如果短程搜索是必要的，计划中必须明确写出：先检查附近区域寻找合适辅助物体，再使用该辅助物体完成目标任务。
6. 对每个当前可见或计划短程寻找的辅助物体，判断它是有帮助、无关、还是不适合当前任务。
7. 只有当单臂夹爪直接操作明显更简单、更安全、更稳定，并且不会显著增加往返次数或掉落风险时，才选择直接操作。
8. 如果使用辅助物体，计划中必须体现完整顺序：先获得或准备辅助物体，再让辅助物体作用于目标物，最后完成搬运、取出、收纳或清理。
9. 如果不使用辅助物体，请在原因中说明为什么直接操作已经足够，以及为什么不需要短程寻找辅助物体。

输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶饮料分批运送至卧室供同学饮用",
  "plan": [
    "移动至台面边缘确认所有瓶子位置及间距",
    "短程检查相邻柜边/地面寻找托盘或容器作为辅助搬运工具",
    "若找到合适容器则分批次装载运输，否则逐个抓取饮料瓶运送"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "通过辅助物减少往返次数但需优先确认是否存在可用容器",
  "safety_or_stability_consideration": "松散排列的瓶子无法直接成组搬运，必须确保每次携带不超过1个或稳定组合体",
  "uncertainty_or_missing_information": "未明确短程搜索是否发现合适辅助物（托盘/篮子等）",
  "reason": "当前视野无可见容器类辅助物体，但为提升效率需先确认是否存在可用搬运工具；若不存在则必须采用单瓶逐次运输方案"
}
```

## single_turn_multi_image | multi_image__strong_decomposition_free_plan

Detailed file: [`single_turn_multi_image/multi_image__strong_decomposition_free_plan.md`](./single_turn_multi_image/multi_image__strong_decomposition_free_plan.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__strong_decomposition_free_plan`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个家庭移动机器人。请根据图像和任务，给出可执行的高层计划。
不要输出低层关节动作。

在制定计划前，请系统检查以下问题：
1. 当前任务真正要操作或移动的目标物是什么？
2. 图像中是否存在除目标物之外、可能帮助完成任务的辅助物体？
3. 这些辅助物体是否能够提升任务的效率、安全性、稳定性、可达性，或者减少往返次数？
4. 如果任务涉及多个松散物体、易掉落物体、狭窄空间中的目标物、清理/收纳任务，而合适辅助物体没有明显出现在图像中，请判断是否应该先短程寻找合适辅助物体。
5. 对每个可能的辅助物体，判断它是有帮助、无关、还是不适合当前任务。
6. 只有当直接操作明显更简单、更安全、更稳定时，才选择直接操作。
7. 如果使用辅助物体，计划中必须体现完整顺序：先获得或准备辅助物体，再让辅助物体作用于目标物，最后完成搬运、取出、收纳或清理。
8. 如果不使用辅助物体，请在原因中说明为什么直接操作已经足够。

如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料送至卧室供同学饮用",
  "plan": [
    "移动到台面位置并确认所有饮料瓶状态稳定无泄漏风险",
    "用手掌托住底部或抓握瓶颈处分批搬运（每次2-3瓶）至卧室桌面",
    "将剩余饮料依次送达后整理摆放整齐"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "通过单次携带多瓶减少往返次数，优先选择稳定性高的抓握方式避免掉落风险",
  "safety_or_stability_conservation": "采用手掌托底或瓶颈双指夹持的搬运姿势确保液体不洒漏",
  "uncertainty_or_missing_information": "未观察到托盘/收纳篮等辅助工具，需确认厨房区域是否存在可临时使用的容器",
  "reason": "图像中无合适辅助物体且任务时效性要求高，直接操作比寻找工具更高效稳定"
}
```

## single_turn_multi_image | multi_image__strong_decomposition_free_plan_humanoid_dual_arm

Detailed file: [`single_turn_multi_image/multi_image__strong_decomposition_free_plan_humanoid_dual_arm.md`](./single_turn_multi_image/multi_image__strong_decomposition_free_plan_humanoid_dual_arm.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__strong_decomposition_free_plan_humanoid_dual_arm`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个有两个手臂和两个手/夹爪的家用人形机器人。
你可以同时使用两只手，但每只手通常只能稳定拿住一个普通小物体，或一个物理上稳定的抓取组合。
不要假设你可以直接拿住许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设手臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节动作。

在制定计划前，请系统检查以下问题：
1. 当前任务真正要操作或移动的目标物是什么？
2. 图像中是否存在除目标物之外、可能帮助完成任务的辅助物体？
3. 这些辅助物体是否能够提升任务的效率、安全性、稳定性、可达性，或者减少往返次数？
4. 如果任务涉及多个松散物体、易掉落物体、狭窄空间中的目标物、清理/收纳任务，而合适辅助物体没有明显出现在图像中，请判断是否应该先短程寻找合适辅助物体。
5. 对每个可能的辅助物体，判断它是有帮助、无关、还是不适合当前任务。
6. 只有当双手直接操作明显更简单、更安全、更稳定时，才选择直接操作。
7. 如果使用辅助物体，计划中必须体现完整顺序：先获得或准备辅助物体，再让辅助物体作用于目标物，最后完成搬运、取出、收纳或清理。
8. 如果不使用辅助物体，请在原因中说明为什么直接操作已经足够。

如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "需要将厨房台面上的7瓶饮料尽快运送至卧室供同学饮用",
  "plan": [
    "1. 检查台面周围是否存在托盘/收纳篮等辅助容器（短程环视确认）",
    "2. 获取并携带空容器返回操作区域",
    "3. 将瓶子依次放入容器中确保稳定抓取组合",
    "4. 双手搬运装满饮料的容器至卧室"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "使用辅助容器可单次运送多瓶，减少往返次数",
  "safety_or_stability_consideration": "避免直接抓取多个松散瓶子导致掉落风险",
  "uncertainty_or_missing_information": "需确认短程环视后是否发现可用容器（O1观察结果）",
  "reason": "7个独立物体超出单次稳定搬运能力，辅助工具可提升效率与安全性"
}
```

## single_turn_multi_image | multi_image__strong_decomposition_free_plan_quadruped_single_arm

Detailed file: [`single_turn_multi_image/multi_image__strong_decomposition_free_plan_quadruped_single_arm.md`](./single_turn_multi_image/multi_image__strong_decomposition_free_plan_quadruped_single_arm.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__strong_decomposition_free_plan_quadruped_single_arm`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个有四足移动底盘、一个安装机械臂和一个夹爪的家用机器人。
移动时必须保持身体平衡。
夹爪通常一次只能稳定携带一个普通小物体；只有在物体物理上紧密成组且稳定时，才可携带极少量组合物体。
不要假设你可以直接携带许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设机械臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节或步态动作。

在制定计划前，请系统检查以下问题：
1. 当前任务真正要操作或移动的目标物是什么？
2. 图像中是否存在除目标物之外、可能帮助完成任务的辅助物体？
3. 这些辅助物体是否能够提升任务的效率、安全性、稳定性、可达性，或者减少往返次数？
4. 如果任务涉及多个松散物体、易掉落物体、狭窄空间中的目标物、清理/收纳任务，而合适辅助物体没有明显出现在图像中，请判断是否应该先短程寻找合适辅助物体。
5. 对每个可能的辅助物体，判断它是有帮助、无关、还是不适合当前任务。
6. 只有当单臂夹爪直接操作明显更简单、更安全、更稳定时，才选择直接操作。
7. 如果使用辅助物体，计划中必须体现完整顺序：先获得或准备辅助物体，再让辅助物体作用于目标物，最后完成搬运、取出、收纳或清理。
8. 如果不使用辅助物体，请在原因中说明为什么直接操作已经足够。

如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的7个独立塑料瓶装水/饮料运送至卧室供同学饮用",
  "plan": [
    "移动到台面边缘保持平衡",
    "用夹爪逐个抓取单瓶饮料（每次1瓶）并搬运至卧室桌面放置",
    "返回台面重复上述操作直至所有瓶子送达"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "无可用托盘/容器等辅助工具，需分7次完成运输任务",
  "safety_or_stability_consideration": "每次仅携带单瓶确保夹持稳定性；移动时保持底盘平衡防止倾倒",
  "uncertainty_or_missing_information": "未确认卧室具体位置及路径障碍情况",
  "reason": "饮料为独立松散物体且无辅助搬运工具，根据机器人能力限制必须分次运输"
}
```

## single_turn_multi_image | multi_image__structured_tool_action_chain_probe_humanoid_dual_arm

Detailed file: [`single_turn_multi_image/multi_image__structured_tool_action_chain_probe_humanoid_dual_arm.md`](./single_turn_multi_image/multi_image__structured_tool_action_chain_probe_humanoid_dual_arm.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__structured_tool_action_chain_probe_humanoid_dual_arm`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个有两个手臂和两个手/夹爪的家用人形机器人。
你可以同时使用两只手，但每只手通常只能稳定拿住一个普通小物体，或一个物理上稳定的抓取组合。
不要假设你可以直接拿住许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设手臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "target_objects": ["string"],
  "helper_needed": "yes/no/uncertain",
  "helper_purpose": "aggregation/access/reach/stability/protection/cleaning/none/uncertain",
  "visible_helper_detected": "yes/no/uncertain",
  "visible_helper_objects": ["string"],
  "search_for_helper_if_none_visible": "yes/no/not_applicable/uncertain",
  "selected_helper": "string or none",
  "tool_use_action_chain": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "physical_feasibility_risk": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string",
  "failure_risk": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料分批运送至卧室供同学饮用",
  "plan": [
    "确认所有瓶子位置稳定且无倾倒风险",
    "双手各抓取相邻两瓶（如左黄蓝、右橙绿）移动至卧室门口",
    "重复搬运剩余三瓶，优先使用托盘等辅助工具提升单次运载量"
  ],
  "target_objects": ["黄色饮料瓶", "蓝色饮料瓶", "橙色饮料瓶", "绿色饮料瓶", "透明水瓶"],
  "helper_needed": "uncertain",
  "helper_purpose": "aggregation/access/reach/stability/protection/cleaning/none/uncertain",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "yes",
  "selected_helper": "托盘或收纳盒（若存在）",
  "tool_use_action_chain": [
    "扫描厨房台面寻找可用容器",
    "将饮料瓶有序排列至容器中提升稳定性",
    "搬运整个容器至卧室后逐一分发"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "优先使用双手协同抓取相邻瓶子减少往返次数，若发现托盘则改用单次多瓶运输",
  "safety_or_stability_consideration": "确保每次搬运时饮料不碰撞倾倒，移动路径避开厨房障碍物",
  "physical_feasibility_risk": "七瓶分三次以上搬运可能耗时较长，需平衡速度与稳定性",
  "uncertainty_or_missing_information": "未确认卧室具体位置及门是否开启状态",
  "reason": "基于初始观察和短程环视结果制定分批运输方案",
  "failure_risk": "抓取不稳导致液体洒出或路径受阻延误送达"
}
```

## single_turn_multi_image | multi_image__structured_tool_action_chain_probe_quadruped_single_arm

Detailed file: [`single_turn_multi_image/multi_image__structured_tool_action_chain_probe_quadruped_single_arm.md`](./single_turn_multi_image/multi_image__structured_tool_action_chain_probe_quadruped_single_arm.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__structured_tool_action_chain_probe_quadruped_single_arm`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个有四足移动底盘、一个安装机械臂和一个夹爪的家用机器人。
移动时必须保持身体平衡。
夹爪通常一次只能稳定携带一个普通小物体；只有在物体物理上紧密成组且稳定时，才可携带极少量组合物体。
不要假设你可以直接携带许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设机械臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节或步态动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "target_objects": ["string"],
  "helper_needed": "yes/no/uncertain",
  "helper_purpose": "aggregation/access/reach/stability/protection/cleaning/none/uncertain",
  "visible_helper_detected": "yes/no/uncertain",
  "visible_helper_objects": ["string"],
  "search_for_helper_if_none_visible": "yes/no/not_applicable/uncertain",
  "selected_helper": "string or none",
  "tool_use_action_chain": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "physical_feasibility_risk": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string",
  "failure_risk": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将桌面上7瓶饮料分批搬运至卧室供同学饮用",
  "plan": [
    "移动至桌面边缘定位第一瓶黄色饮料",
    "使用夹爪稳定抓取单瓶并移至卧室放置区",
    "返回重复执行直至完成所有瓶子运输"
  ],
  "target_objects": ["7个独立塑料瓶装饮料"],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "yes",
  "visible_helper_objects": ["桌面边缘空间充足，无移动障碍"],
  "search_for_helper_if_none_visible": "not_applicable",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "调整底盘位置使夹爪对准瓶身中部",
    "闭合夹爪至稳定抓取力度阈值",
    "保持躯干平衡缓慢移动至卧室区域"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "单次搬运确保稳定性优先于速度，避免倾倒风险",
  "safety_or_stability_consideration": "每次仅携带1瓶防止重心偏移导致摔倒",
  "physical_feasibility_risk": "低（饮料重量在夹爪承载范围内）",
  "uncertainty_or_missing_information": "卧室具体放置位置未明确，需确认空间是否足够容纳7瓶",
  "reason": "基于物理限制和任务安全要求制定分批搬运方案"
}
```

## single_turn_multi_image | multi_image__structured_tool_probe

Detailed file: [`single_turn_multi_image/multi_image__structured_tool_probe.md`](./single_turn_multi_image/multi_image__structured_tool_probe.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__structured_tool_probe`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个家庭移动机器人。请根据图像和任务，给出可执行的高层计划。
不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "target_objects": ["string"],
  "helper_needed": "yes/no/uncertain",
  "helper_purpose": "aggregation/access/reach/stability/protection/cleaning/none/uncertain",
  "visible_helper_detected": "yes/no/uncertain",
  "visible_helper_objects": ["string"],
  "search_for_helper_if_none_visible": "yes/no/not_applicable/uncertain",
  "selected_helper": "string or none",
  "tool_use_action_chain": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "physical_feasibility_risk": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string",
  "failure_risk": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶彩色饮料搬运至卧室供同学饮用",
  "plan": [
    "确认路径无障碍后移动至台面区域", 
    "逐个抓取并稳定携带每瓶饮料", 
    "分批运送至卧室指定位置"
  ],
  "target_objects": ["七瓶不同颜色的运动饮料"],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "search_for_helper_if_none_visible": "not_applicable",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "使用机械臂稳定抓取单个饮料瓶底部", 
    "保持垂直姿态移动至卧室区域", 
    "轻放于桌面避免倾倒"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "优先运送大体积瓶子减少往返次数",
  "safety_or_stability_consideration": "保持饮料瓶直立防止液体泄漏",
  "physical_feasibility_risk": "机械臂负载能力需匹配单瓶重量",
  "uncertainty_or_missing_information": "未确认卧室具体摆放位置要求",
  "reason": "无辅助工具且单次搬运量受限，分次运送更稳妥",
  "failure_risk": "移动过程中碰撞导致饮料洒漏"
}
```

## single_turn_multi_image | multi_image__tool_prior_free_plan

Detailed file: [`single_turn_multi_image/multi_image__tool_prior_free_plan.md`](./single_turn_multi_image/multi_image__tool_prior_free_plan.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__tool_prior_free_plan`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个家庭移动机器人。请根据图像和任务，给出可执行的高层计划。
在制定计划时，请优先考虑环境中是否存在可作为 helper 或工具的物体，例如能够提升效率、安全性、稳定性、可达性或减少往返的辅助物。
如果直接操作明显更简单、更安全或工具/辅助物不合适，可以选择直接操作，但需要在计划理由中体现这个判断。
不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶饮料搬运到卧室，供正在打牌的同学饮用。",
  "plan": [
    "Step 1: 确认所有7瓶饮料在台面位置稳定且无破损。",
    "Step 2: 尝试使用机械手一次性抓取尽可能多的瓶子（例如3-4瓶），运往卧室并放置好。",
    "Step 3: 返回厨房，重复上述步骤搬运剩余的瓶子直到全部送达。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "台面上没有托盘或篮子等辅助容器可用，直接抓握是最高效的方式；分批次抓取（每次3-4瓶）比单瓶搬运能显著减少往返次数。",
  "safety_or_stability_consideration": "由于瓶子细长且表面光滑，需确保夹持力度适中以防滑落；分批运输可避免单次负载过重导致倾倒或液体溅出。",
  "uncertainty_or_missing_information": "不确定卧室的具体距离及路径情况，也不确定机械手能否在不使用容器的情况下一次性抓握所有7个瓶子而不掉落。"
}
```

## single_turn_multi_image | multi_image__tool_prior_free_plan_humanoid_dual_arm

Detailed file: [`single_turn_multi_image/multi_image__tool_prior_free_plan_humanoid_dual_arm.md`](./single_turn_multi_image/multi_image__tool_prior_free_plan_humanoid_dual_arm.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__tool_prior_free_plan_humanoid_dual_arm`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个有两个手臂和两个手/夹爪的家用人形机器人。
你可以同时使用两只手，但每只手通常只能稳定拿住一个普通小物体，或一个物理上稳定的抓取组合。
不要假设你可以直接拿住许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设手臂一定能直接够到目标物体。
在制定计划时，请优先考虑环境中是否存在可作为 helper 或工具的物体，尤其是能够提升效率、安全性、稳定性、可达性或减少往返的辅助物。
如果双手直接操作明显更简单、更安全，或者工具/辅助物不合适，可以选择直接操作，但需要在计划理由中体现这个判断。
只给出高层可执行计划，不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶饮料运送至卧室供同学饮用",
  "plan": [
    "检查台面附近是否存在可承载多瓶的托盘/收纳盒等辅助物",
    "若存在工具：分批用双手+容器组合搬运（每次2-3瓶）；若无工具则分4次往返，每趟双手机械手各持1瓶",
    "确认卧室路径无障碍后运送至目标区域"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "优先使用容器类辅助物减少搬运次数，若无法获取则采用双手协同最大化单次运载量",
  "safety_or_stability_consideration": "确保抓取时瓶身垂直稳定防止倾倒，路径需避开厨房电器和地面障碍物",
  "uncertainty_or_missing_information": "未确认是否存在可用容器类辅助物及卧室具体位置距离"
}
```

## single_turn_multi_image | multi_image__tool_prior_free_plan_quadruped_single_arm

Detailed file: [`single_turn_multi_image/multi_image__tool_prior_free_plan_quadruped_single_arm.md`](./single_turn_multi_image/multi_image__tool_prior_free_plan_quadruped_single_arm.md)

## Protocol And Prompt Content

- protocol id: `single_turn_multi_image`
- prompt id: `multi_image__tool_prior_free_plan_quadruped_single_arm`
- protocol behavior: O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.

### System Prompt

```text
你是一个有四足移动底盘、一个安装机械臂和一个夹爪的家用机器人。
移动时必须保持身体平衡。
夹爪通常一次只能稳定携带一个普通小物体；只有在物体物理上紧密成组且稳定时，才可携带极少量组合物体。
不要假设你可以直接携带许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设机械臂一定能直接够到目标物体。
在制定计划时，请优先考虑环境中是否存在可作为 helper 或工具的物体，尤其是能够提升效率、安全性、稳定性、可达性或减少往返的辅助物。
如果单臂夹爪直接操作明显更简单、更安全，或者工具/辅助物不合适，可以选择直接操作，但需要在计划理由中体现这个判断。
只给出高层可执行计划，不要输出低层关节或步态动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。

观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。
```

### User Prompt Turn 2

```text
(not applicable)
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上7个独立饮料瓶分批运送至卧室供同学饮用",
  "plan": [
    "移动至台面边缘保持平衡并确认无可用容器类辅助物",
    "逐个抓取单瓶饮料并确保夹持稳定后移至卧室",
    "重复搬运直至所有瓶子送达"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "因缺乏托盘等可承载多物的工具，需采用单次1瓶的运输方式",
  "safety_or_stability_consideration": "避免同时携带多个松散物体导致失衡或掉落风险",
  "uncertainty_or_missing_information": "未确认卧室具体位置及搬运路径是否存在障碍物"
}
```

## two_turn_sequential | two_turn__efficient_safe_free_plan

Detailed file: [`two_turn_sequential/two_turn__efficient_safe_free_plan.md`](./two_turn_sequential/two_turn__efficient_safe_free_plan.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__efficient_safe_free_plan`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个家庭移动机器人。请根据图像和任务，给出尽量高效、安全、减少往返次数的高层计划。
不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "任务是将厨房台面上排列的7瓶饮料全部搬运到卧室，供正在打牌的同学饮用。",
  "plan": [
    "移动到厨房台面附近，确认所有7个瓶子的位置及状态。",
    "检查是否有托盘或篮子可用；若有，将所有瓶子整齐放入载具中以确保一次性搬运完毕。若无合适容器，则分批次（如3+4）抓取并装载到移动平台上。",
    "平稳地将饮料运送至卧室。",
    "将饮料放置在同学附近便于拿取的位置。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "优先尝试使用托盘或大载具一次性搬运所有7个瓶子，以最小化往返次数；若无法一次完成，则采用最大负载量的分批策略（如2-3次）。",
  "safety_or_stability_consideration": "抓取饮料时需确保瓶身稳固防止倾倒滑落；移动过程中保持低速平稳，避免液体泼洒或瓶子碰撞破碎。",
  "uncertainty_or_missing_information": "不确定机器人是否配备有足够大的托盘来一次性装载所有7个瓶子，也不确定卧室的具体距离和路径是否有障碍物。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "任务是将厨房台面上7瓶饮料搬运至卧室供同学饮用，结合当前观察到可用托盘优化搬运流程",
  "plan": [
    "移动到台面附近确认所有7个瓶子位置及状态后，将大托盘放置于合适位置。",
    "依次抓取7个瓶子并整齐摆放在托盘中（利用托盘一次性装载能力减少往返）。",
    "平稳移动至卧室后将托盘上的饮料放置在同学可方便取用的区域"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "当前观察到的大托盘可用于集中承载所有7个瓶子，通过一次装载多瓶的方式减少往返次数提升效率。",
  "safety_or_stability_consideration": "抓取饮料时需确保与托盘接触稳定防止滑落；移动过程中保持低速平稳避免液体泼洒或瓶子碰撞破碎。",
  "uncertainty_or_missing_information": "仍不确定卧室具体距离、路径是否有障碍物，以及托盘承重是否足够承载7个瓶子的总重量"
}
```

## two_turn_sequential | two_turn__efficient_safe_free_plan_humanoid_dual_arm

Detailed file: [`two_turn_sequential/two_turn__efficient_safe_free_plan_humanoid_dual_arm.md`](./two_turn_sequential/two_turn__efficient_safe_free_plan_humanoid_dual_arm.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__efficient_safe_free_plan_humanoid_dual_arm`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个有两个手臂和两个手/夹爪的家用人形机器人。
你可以同时使用两只手，但每只手通常只能稳定拿住一个普通小物体，或一个物理上稳定的抓取组合。
不要假设你可以直接拿住许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设手臂一定能直接够到目标物体。
请给出尽量高效、安全、减少往返次数的高层可执行计划。
不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
(empty)
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料运送至卧室供同学饮用",
  "plan": [
    "1. 移动至厨房台面区域确认所有饮料位置",
    "2. 使用托盘装载全部7瓶饮料（分两批次搬运）",
    "3. 双手稳定端托送至卧室并放置于桌面"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "利用托盘实现批量运输，减少往返次数",
  "safety_or_stability_consideration": "确保托盘平稳承载饮料瓶防止倾倒",
  "uncertainty_or_missing_information": "未确认卧室具体位置及桌面承重能力"
}
```

## two_turn_sequential | two_turn__efficient_safe_free_plan_quadruped_single_arm

Detailed file: [`two_turn_sequential/two_turn__efficient_safe_free_plan_quadruped_single_arm.md`](./two_turn_sequential/two_turn__efficient_safe_free_plan_quadruped_single_arm.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__efficient_safe_free_plan_quadruped_single_arm`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个有四足移动底盘、一个安装机械臂和一个夹爪的家用机器人。
移动时必须保持身体平衡。
夹爪通常一次只能稳定携带一个普通小物体；只有在物体物理上紧密成组且稳定时，才可携带极少量组合物体。
不要假设你可以直接携带许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设机械臂一定能直接够到目标物体。
请给出尽量高效、安全、减少往返次数的高层可执行计划。
不要输出低层关节或步态动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶独立饮料逐一搬运至卧室供同学饮用",
  "plan": [
    "1. 移动到台面位置并扫描周围障碍物确保路径安全",
    "2. 依次抓取每瓶饮料（黄色→蓝色→橙色→绿色→透明蓝→深蓝→琥珀色）",
    "3. 每次搬运后返回厨房取下一瓶，保持底盘稳定移动至卧室放置"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "按颜色顺序连续抓取减少机械臂调整时间，优先选择最易抓握的直立状态饮料",
  "safety_or_stability_consideration": "每次仅携带单瓶确保夹爪稳定，移动时保持底盘低重心姿态防止倾倒",
  "uncertainty_or_missing_information": "未确认卧室具体位置及路径中是否存在障碍物影响通行效率"
}
```

### Final Raw Response

```json
{
  "task_understanding": "在发现新观察场景中无目标饮料瓶的情况下，需判断是否为任务执行环境并调整策略",
  "plan": [
    "1. 确认当前场景是否为目标卧室（检查是否有床/桌椅等特征）",
    "2. 若为厨房台面则返回原位置继续搬运剩余饮料",
    "3. 若在目标区域则搜索周围是否存在遗漏的饮料瓶"
  ],
  "estimated_number_of_trips": "unknown",
  "efficiency_consideration": "优先确认当前场景属性避免无效移动，根据环境特征动态调整任务路径",
  "safety_or_stability_consideration": "在未知环境中保持底盘稳定扫描周围障碍物后再执行动作",
  "uncertainty_or_missing_information": "未明确当前观察位置是否为卧室目标区域及饮料瓶是否已送达"
}
```

## two_turn_sequential | two_turn__natural_free_plan

Detailed file: [`two_turn_sequential/two_turn__natural_free_plan.md`](./two_turn_sequential/two_turn__natural_free_plan.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__natural_free_plan`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个家庭移动机器人。请根据图像和任务，给出可执行的高层计划。
不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶饮料送至卧室供打牌的同学饮用",
  "plan": [
    "移动至厨房台面确认所有瓶子位置及状态",
    "分批次搬运瓶装饮料（每次2-3瓶）至卧室桌面",
    "检查是否遗漏物品并整理摆放"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "采用批量运输减少往返次数，优先运送最易倾倒的瓶子",
  "safety_or_stability_consideration": "保持平稳移动避免碰撞台面边缘物品，确保堆叠高度不超过机器人负载限制",
  "uncertainty_or_missing_information": "未明确饮料是否为饮用水（实际为Mountain Dew系列），卧室具体位置及距离未知"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶饮料送至卧室供打牌的同学饮用",
  "plan": [
    "移动至当前观察区域获取托盘作为运输工具",
    "返回厨房台面使用托盘装载2-3瓶饮料（优先选择稳固性高的瓶子）",
    "沿安全路径运送至卧室桌面并重复搬运流程"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "利用托盘实现批量运输，减少往返次数；注意避开台灯和手机等障碍物",
  "safety_or_stability_consideration": "确保托盘装载时重心稳定，避免碰撞周围电子设备（如手机）或灯具",
  "uncertainty_or_missing_information": "未明确饮料是否为饮用水（实际为Mountain Dew系列），卧室具体位置及距离未知"
}
```

## two_turn_sequential | two_turn__natural_free_plan_humanoid_dual_arm

Detailed file: [`two_turn_sequential/two_turn__natural_free_plan_humanoid_dual_arm.md`](./two_turn_sequential/two_turn__natural_free_plan_humanoid_dual_arm.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__natural_free_plan_humanoid_dual_arm`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个有两个手臂和两个手/夹爪的家用人形机器人。
你可以同时使用两只手，但每只手通常只能稳定拿住一个普通小物体，或一个物理上稳定的抓取组合。
不要假设你可以直接拿住许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设手臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料运送至卧室供同学饮用",
  "plan": [
    "检查台面周围是否有障碍物并确认抓取路径安全",
    "双手各持一瓶饮料（优先选择相邻两瓶）运往卧室放置",
    "重复上述步骤直至所有瓶子送达，最后单独搬运剩余单瓶"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "通过双手机械臂协同每次运送2瓶减少往返次数",
  "safety_or_stability_consideration": "确保抓握时保持瓶子直立防止倾倒，移动路径避开台面边缘障碍物",
  "uncertainty_or_missing_information": "未明确卧室具体位置及运输路径是否存在障碍"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料运送至卧室供同学饮用",
  "plan": [
    "检查台面周围是否有障碍物并确认抓取路径安全",
    "使用烤盘作为辅助工具装载多瓶饮料（每次最多4-5瓶）运往卧室放置",
    "重复上述步骤直至所有瓶子送达，最后单独搬运剩余单瓶"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "利用烤盘集中运输可进一步减少往返次数并提升单次运载量",
  "safety_or_stability_consideration": "确保托盘装载时饮料排列稳固，移动路径避开台面边缘障碍物防止倾倒",
  "uncertainty_or_missing_information": "未明确卧室具体位置及运输路径是否存在障碍"
}
```

## two_turn_sequential | two_turn__natural_free_plan_quadruped_single_arm

Detailed file: [`two_turn_sequential/two_turn__natural_free_plan_quadruped_single_arm.md`](./two_turn_sequential/two_turn__natural_free_plan_quadruped_single_arm.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__natural_free_plan_quadruped_single_arm`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个有四足移动底盘、一个安装机械臂和一个夹爪的家用机器人。
移动时必须保持身体平衡。
夹爪通常一次只能稳定携带一个普通小物体；只有在物体物理上紧密成组且稳定时，才可携带极少量组合物体。
不要假设你可以直接携带许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设机械臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节或步态动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "将厨房台面上的7个饮料瓶运送至卧室供同学饮用",
  "plan": [
    "检查台面边缘及移动路径是否存在障碍物",
    "依次抓取每个独立饮料瓶并运输到卧室",
    "重复搬运直至所有瓶子送达"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "按最接近的起始位置顺序搬运减少往返距离，优先处理易滑动的透明蓝色瓶装物",
  "safety_or_stability_consideration": "每次仅携带单瓶确保夹爪稳定性，行走时保持底盘平衡避免倾倒液体",
  "uncertainty_or_missing_information": "未明确饮料是否含气（影响搬运速度），卧室具体位置及路径障碍物未知"
}
```

### Final Raw Response

```json
{
  "task_understanding": "结合新观察O1（台面有烤盘、台灯和手机）更新原任务：运送7个饮料瓶至卧室",
  "plan": [
    "检查当前区域是否有遗漏的饮料瓶或需搬运的其他物品",
    "若发现剩余瓶子，使用夹爪逐个抓取并运输；若无则确认任务完成",
    "评估烤盘是否可辅助稳定携带多个松散物体（如将瓶子排列在烤盘上）"
  ],
  "estimated_number_of_trips": "unknown",
  "efficiency_consideration": "若发现剩余物品，优先使用烤盘作为临时载体减少往返次数；否则维持单次搬运策略",
  "safety_or_stability_consideration": "需验证瓶子在烤盘上的稳定性后再尝试批量运输，避免倾倒风险",
  "uncertainty_or_missing_information": "未确认饮料瓶是否已全部运送完毕或是否存在其他待运物品"
}
```

## two_turn_sequential | two_turn__search_explicit_strong_decomposition_free_plan

Detailed file: [`two_turn_sequential/two_turn__search_explicit_strong_decomposition_free_plan.md`](./two_turn_sequential/two_turn__search_explicit_strong_decomposition_free_plan.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__search_explicit_strong_decomposition_free_plan`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个家庭移动机器人。请根据图像和任务，给出可执行的高层计划。
不要输出低层关节动作。

注意：当前图像只是机器人当前视野，不代表完整环境。
你可以规划短程检查附近区域，例如相邻台面、柜边、地面、桌旁或当前房间内的近处区域。
短程搜索必须服务于当前任务目标，不要进行无目的探索。

在制定计划前，请系统检查以下问题：
1. 当前任务真正要操作、移动、收纳、取出或清理的目标物是什么？
2. 图像中是否存在除目标物之外、可能帮助完成任务的辅助物体？
3. 这些辅助物体是否能够提升任务的效率、安全性、稳定性、可达性，或者减少往返次数？
4. 如果任务涉及多个松散物体、易掉落物体、狭窄空间中的目标物、清理/收纳任务，而当前视野中没有明显合适的辅助物体，请判断是否应该先短程寻找一个合适辅助物体。
5. 如果短程搜索是必要的，计划中必须明确写出：先检查附近区域寻找合适辅助物体，再使用该辅助物体完成目标任务。
6. 对每个当前可见或计划短程寻找的辅助物体，判断它是有帮助、无关、还是不适合当前任务。
7. 只有当直接操作明显更简单、更安全、更稳定，并且不会显著增加往返次数或掉落风险时，才选择直接操作。
8. 如果使用辅助物体，计划中必须体现完整顺序：先获得或准备辅助物体，再让辅助物体作用于目标物，最后完成搬运、取出、收纳或清理。
9. 如果不使用辅助物体，请在原因中说明为什么直接操作已经足够，以及为什么不需要短程寻找辅助物体。

输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "任务是将厨房台面上排列的7瓶饮料运送至卧室，供正在打牌的同学饮用。",
  "plan": [
    "扫描当前台面及周边区域（如水槽边、橱柜下方），寻找托盘、篮子或大容器作为辅助搬运工具。",
    "找到合适的容器后，将7瓶饮料整齐放入容器中以确保稳定。",
    "端起装有所有饮料的容器，将其运送至卧室并放置好供同学取用。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "使用辅助物体（托盘/篮子）可以一次性搬运大部分或全部饮料，避免多次往返厨房与卧室之间，显著提升效率。",
  "safety_or_stability_consideration": "7瓶饮料直接手持极不稳定且容易滑落破碎；使用容器可以提供稳定的支撑面，防止倾倒伤人或弄脏地面及衣物。",
  "uncertainty_or_missing_information": "不确定附近是否有足够大的托盘能一次性装下这7个瓶子（它们看起来较宽），可能需要分两次搬运或使用较大的平面物体替代。",
  "reason": "当前视野中没有明显的辅助容器，直接手持多瓶饮料风险高且效率低；必须先短程搜索合适的辅助工具以确保任务安全、稳定地完成。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶饮料运送至卧室供同学饮用",
  "plan": [
    "使用观察到的金属烤盘作为临时搬运容器，将7个饮料瓶整齐排列放入其中确保稳定",
    "端起装有所有饮料的烤盘直接运送至卧室并放置于桌面或地面"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "金属烤盘可作为临时容器实现批量搬运，避免多次往返厨房与卧室之间",
  "safety_or_stability_consideration": "使用烤盘的边缘结构可防止饮料瓶倾倒滑落，比直接手持更安全稳定",
  "uncertainty_or_missing_information": "不确定7个瓶子能否完全放入单个烤盘（需确认尺寸匹配度）",
  "reason": "当前观察到的金属烤盘可作为有效替代工具满足搬运需求，无需继续搜索其他区域"
}
```

## two_turn_sequential | two_turn__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm

Detailed file: [`two_turn_sequential/two_turn__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm.md`](./two_turn_sequential/two_turn__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__search_explicit_strong_decomposition_free_plan_humanoid_dual_arm`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个有两个手臂和两个手/夹爪的家用人形机器人。
你可以同时使用两只手，但每只手通常只能稳定拿住一个普通小物体，或一个物理上稳定的抓取组合。
不要假设你可以直接拿住许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设手臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节动作。

注意：当前图像只是机器人当前视野，不代表完整环境。
你可以规划短程检查附近区域，例如相邻台面、柜边、地面、桌旁或当前房间内的近处区域。
短程搜索必须服务于当前任务目标，不要进行无目的探索。

在制定计划前，请系统检查以下问题：
1. 当前任务真正要操作、移动、收纳、取出或清理的目标物是什么？
2. 图像中是否存在除目标物之外、可能帮助完成任务的辅助物体？
3. 这些辅助物体是否能够提升任务的效率、安全性、稳定性、可达性，或者减少往返次数？
4. 如果任务涉及多个松散物体、易掉落物体、狭窄空间中的目标物、清理/收纳任务，而当前视野中没有明显合适的辅助物体，请判断是否应该先短程寻找一个合适辅助物体。
5. 如果短程搜索是必要的，计划中必须明确写出：先检查附近区域寻找合适辅助物体，再使用该辅助物体完成目标任务。
6. 对每个当前可见或计划短程寻找的辅助物体，判断它是有帮助、无关、还是不适合当前任务。
7. 只有当双手直接操作明显更简单、更安全、更稳定，并且不会显著增加往返次数或掉落风险时，才选择直接操作。
8. 如果使用辅助物体，计划中必须体现完整顺序：先获得或准备辅助物体，再让辅助物体作用于目标物，最后完成搬运、取出、收纳或清理。
9. 如果不使用辅助物体，请在原因中说明为什么直接操作已经足够，以及为什么不需要短程寻找辅助物体。

输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料尽快送至卧室供同学饮用",
  "plan": [
    "快速扫描台面、柜边及地面寻找托盘/篮子等辅助容器",
    "若找到合适容器，分批放置瓶子后运送至卧室；若无则双手各持一瓶分四次搬运"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "使用辅助物可减少往返次数并提升稳定性",
  "safety_or_stability_consideration": "避免单手抓握多个瓶子导致掉落风险",
  "uncertainty_or_missing_information": "当前视野未显示可用容器，需确认附近区域是否存在托盘类物品",
  "reason": "多瓶松散物体需要辅助工具提升搬运效率与安全性"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料送至卧室供同学饮用",
  "plan": [
    "使用现有烤盘作为容器分批放置饮料瓶（每批2-3瓶）",
    "双手稳定托举装满的烤盘运送至卧室"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "利用现成烤盘替代临时寻找辅助物，减少准备时间并提升单次搬运量",
  "safety_or_stability_consideration": "烤盘边缘可防止瓶子滚动掉落，双手托举比单手持瓶更稳定",
  "uncertainty_or_missing_information": "需确认烤盘尺寸是否适配所有饮料瓶（当前观察显示足够容纳）",
  "reason": "新观察到烤盘可作为高效辅助工具，无需继续搜索其他容器"
}
```

## two_turn_sequential | two_turn__search_explicit_strong_decomposition_free_plan_quadruped_single_arm

Detailed file: [`two_turn_sequential/two_turn__search_explicit_strong_decomposition_free_plan_quadruped_single_arm.md`](./two_turn_sequential/two_turn__search_explicit_strong_decomposition_free_plan_quadruped_single_arm.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__search_explicit_strong_decomposition_free_plan_quadruped_single_arm`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个有四足移动底盘、一个安装机械臂和一个夹爪的家用机器人。
移动时必须保持身体平衡。
夹爪通常一次只能稳定携带一个普通小物体；只有在物体物理上紧密成组且稳定时，才可携带极少量组合物体。
不要假设你可以直接携带许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设机械臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节或步态动作。

注意：当前图像只是机器人当前视野，不代表完整环境。
你可以规划短程检查附近区域，例如相邻台面、柜边、地面、桌旁或当前房间内的近处区域。
短程搜索必须服务于当前任务目标，不要进行无目的探索。

在制定计划前，请系统检查以下问题：
1. 当前任务真正要操作、移动、收纳、取出或清理的目标物是什么？
2. 图像中是否存在除目标物之外、可能帮助完成任务的辅助物体？
3. 这些辅助物体是否能够提升任务的效率、安全性、稳定性、可达性，或者减少往返次数？
4. 如果任务涉及多个松散物体、易掉落物体、狭窄空间中的目标物、清理/收纳任务，而当前视野中没有明显合适的辅助物体，请判断是否应该先短程寻找一个合适辅助物体。
5. 如果短程搜索是必要的，计划中必须明确写出：先检查附近区域寻找合适辅助物体，再使用该辅助物体完成目标任务。
6. 对每个当前可见或计划短程寻找的辅助物体，判断它是有帮助、无关、还是不适合当前任务。
7. 只有当单臂夹爪直接操作明显更简单、更安全、更稳定，并且不会显著增加往返次数或掉落风险时，才选择直接操作。
8. 如果使用辅助物体，计划中必须体现完整顺序：先获得或准备辅助物体，再让辅助物体作用于目标物，最后完成搬运、取出、收纳或清理。
9. 如果不使用辅助物体，请在原因中说明为什么直接操作已经足够，以及为什么不需要短程寻找辅助物体。

输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "任务是将厨房台面上的7瓶饮料搬运到卧室供同学饮用。",
  "plan": [
    "检查附近区域（如橱柜、架子或地面）寻找托盘、篮子等辅助容器，以便一次性携带多个瓶子。",
    "将找到的辅助物体带回台面，把台面上所有散落的饮料瓶依次放入容器中并整理稳固。",
    "使用机械臂托住装有水的容器底部，保持身体平衡，将其整体搬运至卧室交付。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "当前视野无合适容器直接携带多瓶水；寻找托盘可将7次单程搬运减少为1-2次往返，显著提升效率。",
  "safety_or_stability_consideration": "使用辅助容器可防止瓶子在移动中相互碰撞倾倒或滑落；需确保机器人托举重物时底盘平衡稳定。",
  "uncertainty_or_missing_information": "不确定附近是否有承重足够的托盘可用，也不确定卧室的具体路径距离和障碍物情况。",
  "reason": "当前视野中没有能容纳7瓶水的容器（马克杯太小且易碎），直接逐个搬运效率极低；根据指令要求，在涉及多个松散物体时若缺乏辅助物应先短程搜索寻找合适工具以提升效率和稳定性。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "利用新发现的金属烤盘作为辅助容器，将厨房台面上的7瓶饮料一次性搬运至卧室供同学饮用",
  "plan": [
    "使用机械臂夹爪逐个抓取台面饮料瓶并放入托盘内排列稳固（注意保持间距防止倾倒）",
    "调整底盘姿态确保托举平衡后移动至卧室区域",
    "将装有全部7瓶水的托盘平稳放置于桌面交付"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "现成金属烤盘可一次性承载所有饮料，消除多次往返搬运需求；需确保瓶子在托盘中排列稳定防止碰撞滑落。",
  "safety_or_stability_consideration": "托盘边缘高度可有效约束瓶体滚动风险；移动时需保持底盘水平并控制加速度避免液体晃动导致重心偏移。",
  "uncertainty_or_missing_information": "未确认烤盘承重极限是否满足7瓶饮料总重量，需通过夹爪试探性加载验证稳定性后再执行搬运动作。",
  "reason": "新观察到的金属托盘完全符合辅助容器要求（尺寸适配、结构稳固），无需继续搜索其他工具；直接使用该物体可将原计划的多次往返简化为单次高效运输，同时满足多瓶饮料稳定携带的安全需求。"
}
```

## two_turn_sequential | two_turn__strong_decomposition_free_plan

Detailed file: [`two_turn_sequential/two_turn__strong_decomposition_free_plan.md`](./two_turn_sequential/two_turn__strong_decomposition_free_plan.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__strong_decomposition_free_plan`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个家庭移动机器人。请根据图像和任务，给出可执行的高层计划。
不要输出低层关节动作。

在制定计划前，请系统检查以下问题：
1. 当前任务真正要操作或移动的目标物是什么？
2. 图像中是否存在除目标物之外、可能帮助完成任务的辅助物体？
3. 这些辅助物体是否能够提升任务的效率、安全性、稳定性、可达性，或者减少往返次数？
4. 如果任务涉及多个松散物体、易掉落物体、狭窄空间中的目标物、清理/收纳任务，而合适辅助物体没有明显出现在图像中，请判断是否应该先短程寻找合适辅助物体。
5. 对每个可能的辅助物体，判断它是有帮助、无关、还是不适合当前任务。
6. 只有当直接操作明显更简单、更安全、更稳定时，才选择直接操作。
7. 如果使用辅助物体，计划中必须体现完整顺序：先获得或准备辅助物体，再让辅助物体作用于目标物，最后完成搬运、取出、收纳或清理。
8. 如果不使用辅助物体，请在原因中说明为什么直接操作已经足够。

如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "将厨房台面上排列的7瓶饮料搬运到卧室，供正在打牌的同学饮用。",
  "plan": [
    "移动到厨房台面旁，评估抓取方式并抓起第一批瓶子（约3-4瓶）",
    "转身离开厨房，前往卧室并将这批水放置在同学可及处",
    "返回厨房，重复搬运动作直至所有7瓶饮料全部送达"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "任务要求尽快完成且未提供托盘或篮子等辅助容器；寻找收纳工具会增加往返时间，直接分批抓取是最高效的策略。",
  "safety_or_stability_consideration": "瓶子表面光滑且数量较多（7瓶），分批次搬运可确保单次抓握的稳定性，防止因一次携带过多导致滑落破碎伤人或弄湿衣物。",
  "uncertainty_or_missing_information": "不确定卧室的具体距离和路径是否有障碍物；未确认同学是否已准备好接收所有饮料还是分批即可。",
  "reason": "图像中无托盘、篮子等辅助搬运工具，且任务强调‘尽快’，因此不花费时间寻找容器，直接采用双手抓握分批次搬运的方式最为稳妥高效。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上排列的7瓶饮料通过新增发现的烤盘作为容器运送至卧室供同学饮用",
  "plan": [
    "移动至台面获取金属托盘并确认其承重能力",
    "分批将饮料放置于托盘中（注意保持重心稳定）",
    "携带装满饮料的托盘前往卧室完成交付"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "利用现成烤盘作为临时容器可单次运送更多瓶子，减少往返次数并提升稳定性",
  "safety_or_stability_consideration": "托盘边缘设计能防止饮料滚动滑落，相比徒手搬运更安全且不易造成液体泼洒",
  "uncertainty_or_missing_information": "未确认托盘的承重极限是否适合7瓶饮料总重量；需确保卧室地面平整可放置托盘",
  "reason": "新观察到的烤盘可作为有效辅助工具替代直接抓取方式。其矩形结构能稳定承载多瓶饮料，边缘设计防止滚动滑落，符合任务对效率和安全性要求无需额外寻找其他容器"
}
```

## two_turn_sequential | two_turn__strong_decomposition_free_plan_humanoid_dual_arm

Detailed file: [`two_turn_sequential/two_turn__strong_decomposition_free_plan_humanoid_dual_arm.md`](./two_turn_sequential/two_turn__strong_decomposition_free_plan_humanoid_dual_arm.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__strong_decomposition_free_plan_humanoid_dual_arm`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个有两个手臂和两个手/夹爪的家用人形机器人。
你可以同时使用两只手，但每只手通常只能稳定拿住一个普通小物体，或一个物理上稳定的抓取组合。
不要假设你可以直接拿住许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设手臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节动作。

在制定计划前，请系统检查以下问题：
1. 当前任务真正要操作或移动的目标物是什么？
2. 图像中是否存在除目标物之外、可能帮助完成任务的辅助物体？
3. 这些辅助物体是否能够提升任务的效率、安全性、稳定性、可达性，或者减少往返次数？
4. 如果任务涉及多个松散物体、易掉落物体、狭窄空间中的目标物、清理/收纳任务，而合适辅助物体没有明显出现在图像中，请判断是否应该先短程寻找合适辅助物体。
5. 对每个可能的辅助物体，判断它是有帮助、无关、还是不适合当前任务。
6. 只有当双手直接操作明显更简单、更安全、更稳定时，才选择直接操作。
7. 如果使用辅助物体，计划中必须体现完整顺序：先获得或准备辅助物体，再让辅助物体作用于目标物，最后完成搬运、取出、收纳或清理。
8. 如果不使用辅助物体，请在原因中说明为什么直接操作已经足够。

如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "将图片中的七瓶饮料从厨房搬运至卧室供同学饮用",
  "plan": [
    "用右手抓取最左侧黄色瓶子并稳定握持",
    "左手同步抓取相邻蓝色瓶子形成双瓶组合",
    "携带两瓶移动至卧室后放置于桌面或地面安全区域",
    "返回厨房重复上述步骤直至所有七瓶饮料完成搬运"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "每次运送2瓶可减少往返次数，但需确保双手稳定抓取能力",
  "safety_or_stability_consideration": "塑料瓶装易滑落，需确认手指抓握力度适中避免挤压变形或掉落",
  "uncertainty_or_missing_information": "未明确卧室具体位置及搬运路径是否存在障碍物"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将七瓶饮料从厨房搬运至卧室供同学饮用",
  "plan": [
    "用右手抓取最左侧黄色瓶子并稳定握持",
    "左手同步抓取相邻蓝色瓶子形成双瓶组合",
    "携带两瓶移动至卧室后放置于桌面或地面安全区域",
    "返回厨房重复上述步骤直至所有七瓶饮料完成搬运"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "每次运送2瓶可减少往返次数，但需确保双手稳定抓取能力",
  "safety_or_stability_consideration": "塑料瓶装易滑落，需确认手指抓握力度适中避免挤压变形或掉落",
  "uncertainty_or_missing_information": "未明确卧室具体位置及搬运路径是否存在障碍物"
}
```

## two_turn_sequential | two_turn__strong_decomposition_free_plan_quadruped_single_arm

Detailed file: [`two_turn_sequential/two_turn__strong_decomposition_free_plan_quadruped_single_arm.md`](./two_turn_sequential/two_turn__strong_decomposition_free_plan_quadruped_single_arm.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__strong_decomposition_free_plan_quadruped_single_arm`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个有四足移动底盘、一个安装机械臂和一个夹爪的家用机器人。
移动时必须保持身体平衡。
夹爪通常一次只能稳定携带一个普通小物体；只有在物体物理上紧密成组且稳定时，才可携带极少量组合物体。
不要假设你可以直接携带许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设机械臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节或步态动作。

在制定计划前，请系统检查以下问题：
1. 当前任务真正要操作或移动的目标物是什么？
2. 图像中是否存在除目标物之外、可能帮助完成任务的辅助物体？
3. 这些辅助物体是否能够提升任务的效率、安全性、稳定性、可达性，或者减少往返次数？
4. 如果任务涉及多个松散物体、易掉落物体、狭窄空间中的目标物、清理/收纳任务，而合适辅助物体没有明显出现在图像中，请判断是否应该先短程寻找合适辅助物体。
5. 对每个可能的辅助物体，判断它是有帮助、无关、还是不适合当前任务。
6. 只有当单臂夹爪直接操作明显更简单、更安全、更稳定时，才选择直接操作。
7. 如果使用辅助物体，计划中必须体现完整顺序：先获得或准备辅助物体，再让辅助物体作用于目标物，最后完成搬运、取出、收纳或清理。
8. 如果不使用辅助物体，请在原因中说明为什么直接操作已经足够。

如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "将台面上的7个彩色塑料瓶装饮料全部从厨房移动到卧室供同学饮用",
  "plan": [
    "移动至台面左侧区域定位第一个黄色瓶子，使用夹爪垂直抓握瓶颈处确保稳定性",
    "保持底盘平衡状态下携带单瓶饮料前往卧室并放置于桌面",
    "返回厨房重复抓取剩余6个不同颜色瓶装饮料（每次仅搬运1瓶）"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "受限于夹爪单次只能稳定携带单个物体的物理限制，需进行7次往返运输",
  "safety_or_stability_consideration": "每次仅搬运单瓶可确保底盘平衡和抓握稳定性，避免多物体同时移动导致倾倒风险",
  "uncertainty_or_missing_information": "未确认卧室桌面是否有足够空间放置所有饮料瓶及是否需要额外收纳容器",
  "reason": "图像中无托盘/篮子等辅助工具可用，且松散排列的7个塑料瓶无法形成稳定组合体进行批量搬运"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将7个彩色塑料瓶从厨房台面运送至卧室供同学饮用",
  "plan": [
    "移动至当前观察区域获取金属烤盘作为辅助工具",
    "依次将所有7个饮料瓶整齐排列放置于烤盘中确保物理稳定组合",
    "使用机械臂或底盘整体搬运装有全部饮料的托盘前往卧室"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "利用现有金属烤盘实现批量运输，将7次单瓶搬运减少为1-2次完整运送",
  "safety_or_stability_consideration": "托盘可防止饮料在移动过程中倾倒散落，提升整体稳定性与安全性",
  "uncertainty_or_missing_information": "需确认卧室桌面能否容纳全部7个瓶子及是否需要额外收纳容器",
  "reason": "新观察到的金属烤盘可作为有效辅助工具实现批量运输，符合任务对效率和安全性的要求"
}
```

## two_turn_sequential | two_turn__structured_tool_action_chain_probe_humanoid_dual_arm

Detailed file: [`two_turn_sequential/two_turn__structured_tool_action_chain_probe_humanoid_dual_arm.md`](./two_turn_sequential/two_turn__structured_tool_action_chain_probe_humanoid_dual_arm.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__structured_tool_action_chain_probe_humanoid_dual_arm`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个有两个手臂和两个手/夹爪的家用人形机器人。
你可以同时使用两只手，但每只手通常只能稳定拿住一个普通小物体，或一个物理上稳定的抓取组合。
不要假设你可以直接拿住许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设手臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "target_objects": ["string"],
  "helper_needed": "yes/no/uncertain",
  "helper_purpose": "aggregation/access/reach/stability/protection/cleaning/none/uncertain",
  "visible_helper_detected": "yes/no/uncertain",
  "visible_helper_objects": ["string"],
  "search_for_helper_if_none_visible": "yes/no/not_applicable/uncertain",
  "selected_helper": "string or none",
  "tool_use_action_chain": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "physical_feasibility_risk": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string",
  "failure_risk": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶彩色饮料运送至卧室供同学饮用",
  "plan": [
    "确认所有饮料瓶位置及状态（无破损/泄漏）",
    "分批次抓取并搬运：每次双手各持1-2瓶稳定物体，沿最短路径移动",
    "在卧室桌面按顺序摆放7瓶饮料"
  ],
  "target_objects": ["黄色瓶装饮料","蓝色瓶装饮料","橙色瓶装饮料","绿色瓶装饮料","透明蓝盖瓶装饮料"],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "yes",
  "visible_helper_objects": ["厨房台面边缘空间足够放置临时堆叠的2瓶饮料"],
  "search_for_helper_if_none_visible": "not_applicable",
  "selected_helper": "台边暂存区",
  "tool_use_action_chain": [
    "左手抓取黄色瓶装，右手同步抓取蓝色瓶装",
    "移动至卧室后先放置于桌面左侧区域",
    "返回厨房重复搬运剩余5瓶（分3次完成）"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "优先使用双手同时搬运减少往返次数，利用台边暂存区优化单次负载量",
  "safety_or_stability_consideration": "保持手臂垂直移动避免碰撞台面边缘，确保瓶盖方向一致防止倾倒",
  "physical_feasibility_risk": "高瓶身重心可能导致抓取时晃动，需调整夹爪压力至最大稳定值85%",
  "uncertainty_or_missing_information": "未确认卧室桌面承重能力及空间布局是否适合放置7个瓶子",
  "reason": "基于视觉识别的物体数量与物理限制匹配度分析"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶彩色饮料运送至卧室供同学饮用",
  "plan": [
    "确认所有饮料瓶位置及状态（无破损/泄漏）",
    "利用台面边缘暂存区优化单次负载量，分批次搬运：每次双手各持1-2瓶稳定物体沿最短路径移动",
    "在卧室桌面按顺序摆放7瓶饮料"
  ],
  "target_objects": ["黄色瓶装饮料","蓝色瓶装饮料","橙色瓶装饮料","绿色瓶装饮料","透明蓝盖瓶装饮料"],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "yes",
  "visible_helper_objects": ["厨房台面边缘空间足够放置临时堆叠的2瓶饮料"],
  "search_for_helper_if_none_visible": "not_applicable",
  "selected_helper": "台边暂存区",
  "tool_use_action_chain": [
    "左手抓取黄色瓶装，右手同步抓取蓝色瓶装",
    "移动至卧室后先放置于桌面左侧区域",
    "返回厨房重复搬运剩余5瓶（分3次完成）"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "优先使用双手同时搬运减少往返次数，利用台边暂存区优化单次负载量",
  "safety_or_stability_consideration": "保持手臂垂直移动避免碰撞台面边缘，确保瓶盖方向一致防止倾倒",
  "physical_feasibility_risk": "高瓶身重心可能导致抓取时晃动，需调整夹爪压力至最大稳定值85%",
  "uncertainty_or_missing_information": "未确认卧室桌面承重能力及空间布局是否适合放置7个瓶子",
  "reason": "基于视觉识别的物体数量与物理限制匹配度分析"
}
```

## two_turn_sequential | two_turn__structured_tool_action_chain_probe_quadruped_single_arm

Detailed file: [`two_turn_sequential/two_turn__structured_tool_action_chain_probe_quadruped_single_arm.md`](./two_turn_sequential/two_turn__structured_tool_action_chain_probe_quadruped_single_arm.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__structured_tool_action_chain_probe_quadruped_single_arm`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个有四足移动底盘、一个安装机械臂和一个夹爪的家用机器人。
移动时必须保持身体平衡。
夹爪通常一次只能稳定携带一个普通小物体；只有在物体物理上紧密成组且稳定时，才可携带极少量组合物体。
不要假设你可以直接携带许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设机械臂一定能直接够到目标物体。
只给出高层可执行计划，不要输出低层关节或步态动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "target_objects": ["string"],
  "helper_needed": "yes/no/uncertain",
  "helper_purpose": "aggregation/access/reach/stability/protection/cleaning/none/uncertain",
  "visible_helper_detected": "yes/no/uncertain",
  "visible_helper_objects": ["string"],
  "search_for_helper_if_none_visible": "yes/no/not_applicable/uncertain",
  "selected_helper": "string or none",
  "tool_use_action_chain": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "physical_feasibility_risk": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string",
  "failure_risk": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "将台面上的7瓶彩色饮料送至卧室供同学饮用",
  "plan": [
    "移动到台面边缘保持平衡",
    "逐个抓取单瓶饮料并运送至卧室",
    "重复搬运直至所有瓶子送达"
  ],
  "target_objects": ["七瓶不同颜色的塑料瓶装饮料"],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "not_applicable",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "调整夹爪角度对准瓶身中部",
    "施加稳定抓握力避免滑落",
    "保持底盘平衡移动至卧室"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "按颜色分组减少重复路径，优先搬运最远位置瓶子",
  "safety_or_stability_consideration": "每次仅携带单瓶确保夹持稳定，移动时保持底盘水平",
  "physical_feasibility_risk": "连续7次往返可能增加机械臂疲劳风险",
  "uncertainty_or_missing_information": "卧室具体位置及路径障碍物未知",
  "reason": "基于单次只能搬运1个物体的物理限制和当前无辅助工具情况"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将台面上的7瓶彩色饮料送至卧室供同学饮用",
  "plan": [
    "移动到台面边缘保持平衡",
    "使用金属烤盘作为辅助载体装载多瓶饮料",
    "分批搬运托盘至卧室并分发"
  ],
  "target_objects": ["七瓶不同颜色的塑料瓶装饮料"],
  "helper_needed": "yes",
  "helper_purpose": "aggregation/access/reach/stability/protection/cleaning/none/aggregation",
  "visible_helper_detected": "yes",
  "visible_helper_objects": ["金属烤盘"],
  "search_for_helper_if_none_visible": "not_applicable",
  "selected_helper": "metal baking tray",
  "tool_use_action_chain": [
    "将饮料瓶有序排列在托盘上形成稳定组合体",
    "用夹爪托住托盘边缘保持水平移动",
    "到达卧室后逐层卸货"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "利用托盘实现单次搬运3-4瓶饮料，减少往返次数50%",
  "safety_or_stability_consideration": "需确保托盘上饮料排列稳固防止倾倒，移动时保持底盘水平"
}
```

## two_turn_sequential | two_turn__structured_tool_probe

Detailed file: [`two_turn_sequential/two_turn__structured_tool_probe.md`](./two_turn_sequential/two_turn__structured_tool_probe.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__structured_tool_probe`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个家庭移动机器人。请根据图像和任务，给出可执行的高层计划。
不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "target_objects": ["string"],
  "helper_needed": "yes/no/uncertain",
  "helper_purpose": "aggregation/access/reach/stability/protection/cleaning/none/uncertain",
  "visible_helper_detected": "yes/no/uncertain",
  "visible_helper_objects": ["string"],
  "search_for_helper_if_none_visible": "yes/no/not_applicable/uncertain",
  "selected_helper": "string or none",
  "tool_use_action_chain": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "physical_feasibility_risk": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string",
  "failure_risk": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶饮料送至卧室供打牌的同学饮用",
  "plan": [
    "确认所有水瓶位置并检查台面是否有其他可辅助搬运物品",
    "分批次携带水瓶前往卧室（每次最多3-4瓶）",
    "在卧室桌面摆放整齐后返回取剩余瓶子"
  ],
  "target_objects": ["7瓶彩色饮料"],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "not_applicable",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "双手交替搬运水瓶（每次2-3瓶）",
    "保持身体平衡避免碰撞障碍物"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "优先携带较大容量瓶子减少往返次数",
  "safety_or_stability_consideration": "确保水瓶握持稳固防止滑落，注意地面湿滑风险",
  "physical_feasibility_risk": "单次搬运超过3瓶可能导致失衡",
  "uncertainty_or_missing_information": "未确认卧室具体位置及路径障碍物情况",
  "reason": "无可用辅助工具且需快速响应需求",
  "failure_risk": "中途打翻水瓶或遗漏部分瓶子"
}
```

### Final Raw Response

```json
{
  "task_understanding": "结合厨房台面新观察到的烤盘等物品，优化将7瓶饮料运送至卧室的任务执行方案",
  "plan": [
    "检查烤盘是否可用作托盘承载多个水瓶（每次最多4-5瓶）",
    "使用烤盘分两次搬运全部饮料（第一次3瓶+第二次4瓶）",
    "在卧室桌面按原计划摆放整齐"
  ],
  "target_objects": ["7瓶彩色饮料"],
  "helper_needed": "yes",
  "helper_purpose": "aggregation",
  "visible_helper_detected": "yes",
  "visible_helper_objects": ["烤盘"],
  "search_for_helper_if_none_visible": "not_applicable",
  "selected_helper": "金属烤盘",
  "tool_use_action_chain": [
    "将饮料瓶垂直排列放置在烤盘中保持平衡",
    "双手托举烤盘边缘进行搬运"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "利用烤盘增加单次运输量减少往返次数",
  "safety_or_stability_consideration": "确保饮料瓶在烤盘中固定不滚动，注意台面高度差风险",
  "physical_feasibility_risk": "烤盘边缘可能无法完全约束圆柱形瓶子导致滑落",
  "uncertainty_or_missing_information": "未确认卧室具体位置及路径障碍物情况",
  "reason": "利用现有工具提升搬运效率同时保持任务可行性",
  "failure_risk": "饮料瓶在烤盘中滚动散落或中途倾倒"
}
```

## two_turn_sequential | two_turn__tool_prior_free_plan

Detailed file: [`two_turn_sequential/two_turn__tool_prior_free_plan.md`](./two_turn_sequential/two_turn__tool_prior_free_plan.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__tool_prior_free_plan`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个家庭移动机器人。请根据图像和任务，给出可执行的高层计划。
在制定计划时，请优先考虑环境中是否存在可作为 helper 或工具的物体，例如能够提升效率、安全性、稳定性、可达性或减少往返的辅助物。
如果直接操作明显更简单、更安全或工具/辅助物不合适，可以选择直接操作，但需要在计划理由中体现这个判断。
不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料送至卧室供同学饮用",
  "plan": [
    "1. 扫描台面周围是否存在托盘/收纳盒等辅助工具，若无则准备直接抓取操作",
    "2. 依次抓取每个瓶子中部保持平衡，沿最短路径移动至卧室区域",
    "3. 在卧室内按原顺序摆放饮料并确认送达"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "无可用容器时采用逐个搬运策略避免碰撞风险",
  "safety_or_stability_conservation": "抓取瓶身中部保持重心稳定，移动路径避开台面边缘障碍物",
  "uncertainty_or_missing_information": "未确认饮料是否为饮用水及卧室具体位置坐标"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料送至卧室供同学饮用",
  "plan": [
    "1. 使用金属烤盘作为运输载体放置多瓶饮料（需确认承重稳定性）",
    "2. 沿最短路径移动至卧室区域，注意避开台灯/手机等障碍物",
    "3. 在卧室内按原顺序摆放并补充剩余未运送的瓶子"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "利用烤盘实现单次多瓶运输减少往返次数，需验证托盘承重稳定性",
  "safety_or_stability_conservation": "移动时保持托盘水平避免液体泼洒，注意避开台灯/手机等障碍物防止碰撞",
  "uncertainty_or_missing_information": "未确认饮料总重量是否超过烤盘安全承载范围"
}
```

## two_turn_sequential | two_turn__tool_prior_free_plan_humanoid_dual_arm

Detailed file: [`two_turn_sequential/two_turn__tool_prior_free_plan_humanoid_dual_arm.md`](./two_turn_sequential/two_turn__tool_prior_free_plan_humanoid_dual_arm.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__tool_prior_free_plan_humanoid_dual_arm`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个有两个手臂和两个手/夹爪的家用人形机器人。
你可以同时使用两只手，但每只手通常只能稳定拿住一个普通小物体，或一个物理上稳定的抓取组合。
不要假设你可以直接拿住许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设手臂一定能直接够到目标物体。
在制定计划时，请优先考虑环境中是否存在可作为 helper 或工具的物体，尤其是能够提升效率、安全性、稳定性、可达性或减少往返的辅助物。
如果双手直接操作明显更简单、更安全，或者工具/辅助物不合适，可以选择直接操作，但需要在计划理由中体现这个判断。
只给出高层可执行计划，不要输出低层关节动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶彩色饮料分批运送至卧室供同学饮用",
  "plan": [
    "检查台面是否有托盘/篮子等可搬运多瓶的容器（无则直接操作）",
    "双手各持1-2瓶稳定抓取，分4次完成运输（前3次每次运2瓶，最后一次运剩余1瓶）",
    "沿无障碍路径移动至卧室并放置饮料"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "无辅助工具时采用双手交替搬运最大化单次运载量（每趟最多2瓶），减少往返次数",
  "safety_or_stability_consideration": "确保每次抓取饮料底部稳定，避免倾倒；移动中保持身体平衡防止碰撞",
  "uncertainty_or_missing_information": "未确认卧室具体位置及路径是否存在障碍物"
}
```

### Final Raw Response

```json
{
  "task_understanding": "利用新发现的托盘工具优化饮料运输方案",
  "plan": [
    "确认烤盘可承载7瓶饮料（需调整摆放间距）",
    "将全部饮料按颜色顺序排列在烤盘中，双手托举边缘搬运至卧室",
    "到达后逐瓶取出放置"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "使用托盘实现单次运输7瓶（原需4次），减少往返次数50%以上",
  "safety_or_stability_consideration": "确保烤盘水平移动，饮料间距≥2cm防止碰撞倾倒；搬运时保持躯干稳定"
}
```

## two_turn_sequential | two_turn__tool_prior_free_plan_quadruped_single_arm

Detailed file: [`two_turn_sequential/two_turn__tool_prior_free_plan_quadruped_single_arm.md`](./two_turn_sequential/two_turn__tool_prior_free_plan_quadruped_single_arm.md)

## Protocol And Prompt Content

- protocol id: `two_turn_sequential`
- prompt id: `two_turn__tool_prior_free_plan_quadruped_single_arm`
- protocol behavior: Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.

### System Prompt

```text
你是一个有四足移动底盘、一个安装机械臂和一个夹爪的家用机器人。
移动时必须保持身体平衡。
夹爪通常一次只能稳定携带一个普通小物体；只有在物体物理上紧密成组且稳定时，才可携带极少量组合物体。
不要假设你可以直接携带许多松散、分离的物体。
对于家具下方深而狭窄的空间，不要假设机械臂一定能直接够到目标物体。
在制定计划时，请优先考虑环境中是否存在可作为 helper 或工具的物体，尤其是能够提升效率、安全性、稳定性、可达性或减少往返的辅助物。
如果单臂夹爪直接操作明显更简单、更安全，或者工具/辅助物不合适，可以选择直接操作，但需要在计划理由中体现这个判断。
只给出高层可执行计划，不要输出低层关节或步态动作。
如果需要先检查附近区域，请明确说明。
输出必须是单个合法 JSON 对象。
不要输出 markdown、解释、评论或代码块。

JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "uncertainty_or_missing_information": "string",
  "reason": "string"
}
```

### User Prompt Turn 1

```text
任务：卧室里几个同学在打牌，他们有点渴。请尽快把这些水送到卧室。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "将厨房台面上的7瓶饮料运送至卧室供同学饮用",
  "plan": [
    "移动到台面边缘确认无可用托盘/篮子等辅助搬运工具",
    "依次夹取单瓶饮料并移动至卧室桌面放置",
    "重复抓取-运输动作直至所有瓶子送达"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "因无合适容器且单次仅能稳定携带1个物体，需7次往返完成运送",
  "safety_or_stability_consideration": "每次搬运前确认夹爪稳固抓握瓶身中部避免倾倒，移动时保持底盘平衡防止滑倒",
  "uncertainty_or_missing_information": "未明确饮料是否含易碎玻璃材质及卧室具体位置距离"
}
```

### Final Raw Response

```json
{
  "task_understanding": "利用新发现的烤盘优化饮料运送流程",
  "plan": [
    "确认烤盘可稳定承载所有7瓶饮料且无倾倒风险",
    "将全部饮料按顺序放置于烤盘中形成紧密组合物体",
    "使用夹爪搬运整个托盘至卧室桌面"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "通过组合运输减少往返次数，单次可运送7瓶而非1瓶",
  "safety_or_stability_consideration": "需验证烤盘边缘高度是否足够防止滚动，移动时保持托盘水平避免液体溢出"
}
```

