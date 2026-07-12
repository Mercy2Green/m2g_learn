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
{
  "task_understanding": "将七瓶不同颜色的饮料从厨房快速、安全地送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "拿起最左边的黄色瓶子",
    "离开厨房，前往卧室",
    "在卧室放下黄色瓶子",
    "返回厨房，拿起蓝色瓶子",
    "前往卧室",
    "在卧室放下蓝色瓶子",
    "返回厨房，拿起橙色瓶子",
    "前往卧室",
    "在卧室放下橙色瓶子",
    "返回厨房，拿起绿色瓶子",
    "前往卧室",
    "在卧室放下绿色瓶子",
    "返回厨房，拿起透明瓶子",
    "前往卧室",
    "在卧室放下透明瓶子",
    "返回厨房，拿起蓝色瓶子",
    "前往卧室",
    "在卧室放下蓝色瓶子",
    "返回厨房，拿起橙色瓶子",
    "前往卧室",
    "在卧室放下橙色瓶子"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "为了减少总行程时间，计划采用单次搬运一瓶的方式，尽管需要多次往返，但避免了因一次携带过多而可能发生的掉落或碰撞风险。",
  "safety_or_stability_consideration": "每次只携带一瓶饮料，确保机器人在移动过程中的稳定性和安全性，防止液体洒出。",
  "uncertainty_or_missing_information": "无法确定卧室的具体位置和路径，也无法确认是否有障碍物。此外，未明确说明是否需要将所有瓶子一次性送达或可以分批送达。",
  "reason": "根据两个观察，机器人从厨房出发，目标是将饮料送到卧室。由于任务要求“尽快”，且考虑到单次搬运的稳定性和安全性，决定采用多次往返的方式逐一运送。虽然效率较低，但能确保安全和准确送达。"
}
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
  "task_understanding": "将七瓶饮料从厨房台面运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查当前环境，确认所有七瓶饮料均在厨房台面上且状态稳定。",
    "使用右手抓取最左侧的黄色瓶子，同时用左手抓取其右侧的蓝色瓶子。",
    "将两瓶饮料移至中间位置，准备进行下一次抓取。",
    "重复上述动作，分批将剩余五瓶饮料从厨房台面运送到卧室。",
    "在运送过程中确保每只手最多携带两个瓶子，并保持平衡以防止倾倒。",
    "到达卧室后，将所有饮料放置在靠近打牌区域的桌面上。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "通过同时使用双手并分批运送，减少往返次数，提高效率。",
  "safety_or_stability_consideration": "确保每次抓取时瓶子稳定，避免因单手或双手负载过重导致掉落或倾倒。",
  "uncertainty_or_missing_information": "无法确认卧室的具体位置和路径是否畅通，需在移动过程中实时调整路线。",
  "reason": "基于两个观察，机器人需要高效、安全地完成任务。通过分批运送并利用双臂协同工作，可以减少往返次数，同时确保运输过程中的稳定性。"
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
  "task_understanding": "将七瓶饮料从厨房运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查当前环境，确认所有饮料瓶均在厨房台面上且未被移动。",
    "使用机械臂逐一抓取每瓶饮料，确保每次只携带一瓶以保持稳定。",
    "从厨房出发，沿最短路径前往卧室，途中避免碰撞家具或障碍物。",
    "将第一瓶饮料放入卧室指定位置后返回厨房，重复此过程直至所有饮料送达。",
    "在运送过程中，若发现任何异常（如饮料被移动、路径受阻），立即暂停并重新评估。"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "优先完成运输任务，减少往返次数以提高效率；确保每次搬运的稳定性。",
  "safety_or_stability_consideration": "保持身体平衡，避免在移动中倾倒；夹爪仅携带单个物体或物理上紧密成组的少量物体，防止掉落。",
  "uncertainty_or_missing_information": "未明确卧室的具体位置和路径细节，需依赖环境感知导航；无法确认是否有其他障碍物影响通行。",
  "reason": "根据观察O0和O1，所有饮料瓶均在厨房台面上且状态稳定，任务目标清晰。为确保高效安全地完成运输，计划采用逐次搬运方式，并结合实时环境反馈调整路径与动作。"
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
  "task_understanding": "将七瓶饮料从厨房送达卧室，供正在打牌的同学解渴。",
  "plan": [
    "确认所有七瓶饮料都在厨房的台面上。",
    "拿起最左边的一瓶黄色饮料。",
    "离开厨房，前往卧室。",
    "在卧室内找到正在打牌的同学，并将饮料交给他们。",
    "返回厨房，重复上述步骤，直到所有饮料都送达。"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "为了减少往返次数并提高效率，应一次性携带尽可能多的瓶子，但需确保在移动过程中的稳定性和安全性。",
  "safety_or_stability_consideration": "在搬运过程中要保持平稳，避免饮料瓶倾倒或掉落。由于有多个瓶子，需要评估一次携带的数量以保证机器人平衡和路径安全。",
  "uncertainty_or_missing_information": "无法确定卧室的具体位置以及从厨房到卧室的路径是否畅通；不清楚同学的确切人数和他们所在的位置。",
  "reason": "根据O0和O1的观察，确认了饮料在厨房台面上且数量为七瓶。由于任务要求尽快送达，因此需要规划多次往返以确保所有饮料都能被安全送达。同时，考虑到机器人可能无法一次性携带全部瓶子，必须分批运输。"
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
  "task_understanding": "将七瓶饮料从厨房台面运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查当前环境，确认所有饮料瓶均在厨房台面上且未被移动。",
    "使用两只手同时抓取两组饮料（每只手最多两个），确保抓握稳定。",
    "从厨房离开，前往卧室方向。",
    "进入卧室后，将饮料放置于可接近的表面（如床头柜或桌子）。",
    "返回厨房，重复搬运剩余饮料，直至全部送达。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "优先使用双臂并行抓取以减少往返次数，提高运输效率。",
  "safety_or_stability_consideration": "确保每次抓取的瓶子组合稳定，避免因晃动或掉落造成损坏或安全隐患。",
  "uncertainty_or_missing_information": "无法确认卧室的具体位置和路径是否畅通，需在移动过程中实时感知环境变化。",
  "reason": "基于O0和O1的观察，确认饮料瓶未被移动且环境无异常，因此维持原计划并优化搬运策略以提高效率。"
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
  "task_understanding": "将七瓶饮料从厨房送达卧室，供正在打牌的同学饮用。",
  "plan": [
    "移动至厨房台面，确认所有饮料瓶的位置和状态。",
    "逐一检查每瓶饮料是否可被夹爪稳定抓取，确保无泄漏或不稳定情况。",
    "使用机械臂逐个拾取饮料瓶，并保持身体平衡以避免倾倒。",
    "将第一瓶饮料运送到卧室，放置在合适位置后返回厨房。",
    "重复上述过程，直到所有饮料瓶全部送达卧室。"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "优先确保每次运输的稳定性与安全性，避免因携带过多导致掉落或倾倒；若条件允许，可尝试一次携带两瓶紧密排列且稳定的瓶子以提高效率。",
  "safety_or_stability_consideration": "移动过程中必须保持身体平衡，夹爪仅能稳定携带一个普通小物体，除非多个物体物理上紧密成组且稳定。运输时需避免碰撞或晃动。",
  "uncertainty_or_missing_information": "无法确认卧室的具体位置和路径是否畅通；未明确说明饮料瓶在厨房中的确切排列方式及是否有障碍物影响取用。",
  "reason": "基于观察O0，机器人初始位于厨房台面附近，可直接看到所有饮料瓶。观察O1显示机器人已短程环视，但未提供新信息，因此计划维持原方案，仅需确认环境无变化即可执行。"
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
{
  "task_understanding": "将七瓶饮料从厨房台面运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "识别并确认所有七瓶饮料在当前视野中。",
    "检查附近区域（如相邻的地面或柜边）以寻找一个合适的容器或托盘来一次性搬运多瓶饮料。",
    "使用找到的容器或托盘，将所有饮料瓶安全地装入其中。",
    "从厨房出发，前往卧室。",
    "在卧室内，将饮料瓶从容器中取出并放置在合适的位置。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "使用托盘或容器可以一次性搬运多瓶饮料，减少往返次数，提高效率。",
  "safety_or_stability_consideration": "使用托盘或容器可以防止饮料瓶在移动过程中倾倒或掉落，确保安全和稳定。",
  "uncertainty_or_missing_information": "无法确定卧室的具体位置以及从厨房到卧室的路径是否畅通。",
  "reason": "直接搬运多瓶饮料存在掉落风险且效率低。通过短程寻找托盘等辅助物体，可以一次性运输所有饮料，减少往返次数，并提高搬运的安全性和稳定性。"
}
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
  "task_understanding": "将七瓶饮料从厨房台面运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查附近区域以确认是否有合适的容器或托盘来一次性搬运多瓶饮料。",
    "使用找到的托盘或容器，逐个拾取饮料瓶并放置于其上。",
    "将装有饮料瓶的托盘从厨房运送到卧室。",
    "在卧室中将饮料瓶从托盘上取出，并整齐摆放在桌上。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "使用托盘或容器可以一次性搬运多瓶饮料，减少往返次数，提高效率。",
  "safety_or_stability_consideration": "单手拿多个松散的瓶子容易掉落，使用托盘可确保运输过程中的稳定性与安全性。",
  "uncertainty_or_missing_information": "无法确定卧室的具体位置和路径是否畅通，但根据任务要求应尽快送达。",
  "reason": "由于饮料瓶数量较多且为松散物体，直接用手搬运易导致掉落或需要多次往返。通过短程检查寻找托盘等辅助工具，可以一次性稳定运输所有瓶子，减少操作次数并提高效率与安全性。"
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
  "task_understanding": "将七瓶饮料从厨房台面运送到卧室，供打牌的同学饮用。",
  "plan": [
    "检查附近区域以确认是否有合适的容器或托盘来一次性携带多瓶饮料。",
    "若发现合适辅助物体（如托盘），则使用机械臂和夹爪将所有饮料瓶集中并安全放置于该辅助物体上。",
    "移动至卧室，将饮料送达指定位置。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "为减少往返次数并提高效率，应优先寻找可承载多瓶饮料的辅助物体（如托盘），避免单次仅携带一瓶。",
  "safety_or_stability_consideration": "夹爪一次只能稳定携带一个普通小物体；若直接逐个搬运，易因频繁移动导致掉落或不稳定。使用托盘可提升整体稳定性与安全性。",
  "uncertainty_or_missing_information": "当前视野中未见明显可用于承载多瓶饮料的辅助物体（如托盘），需通过短程检查确认附近区域是否存在合适物品。",
  "reason": "目标物为多个松散、易掉落的塑料瓶，直接逐个搬运效率低且风险高。虽然图像中无明确辅助物体，但根据任务需求和机器人能力，应先短程搜索是否有托盘或类似容器可用；若找到，则使用该物体集中运输以减少往返次数并提升稳定性。"
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
  "task_understanding": "将七瓶饮料从厨房台面运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "在厨房台面上识别并定位七瓶饮料。",
    "使用机械臂逐一抓取每瓶饮料，并将其放入储物箱或托盘中以确保稳定运输。",
    "离开厨房，前往卧室方向。",
    "进入卧室，将饮料从储物箱/托盘中取出并放置在同学可及的位置。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "使用储物箱或托盘一次性运输所有饮料，减少往返次数，提高效率。",
  "safety_or_stability_consideration": "将饮料放入储物箱/托盘中可防止在移动过程中倾倒或掉落，确保安全和稳定性。",
  "uncertainty_or_missing_information": "未明确说明卧室的具体位置及路径是否畅通，需在行进中实时调整。",
  "reason": "直接操作目标物（饮料瓶）是可行的，但为了提高效率、减少往返次数并保证运输过程中的稳定性和安全性，应使用储物箱或托盘作为辅助物体。"
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
  "task_understanding": "将七瓶饮料从厨房台面运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查周围环境以确认是否有合适的容器或托盘来一次性搬运多瓶饮料。",
    "如果发现合适辅助物体（如托盘），使用它同时携带所有饮料；否则，分批运送。",
    "从厨房台面拿起第一组饮料（最多两只手各拿一瓶）。",
    "移动到卧室并放下饮料。",
    "返回厨房取剩余的饮料。",
    "重复上述步骤直到所有饮料送达。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "使用托盘或类似辅助物体可以减少往返次数，提高效率。",
  "safety_or_stability_consideration": "单手拿一瓶更稳定；若尝试同时拿多瓶且无稳固支撑，则可能因晃动导致液体洒出。",
  "uncertainty_or_missing_information": "未明确说明卧室与厨房之间的路径是否畅通或是否有障碍物，也未确认是否存在托盘等辅助工具。",
  "reason": "由于饮料瓶为松散物体、易掉落，且需搬运多个，直接操作存在风险。虽然图像中未显示托盘，但根据任务需求和常见家居物品推断，应优先寻找并使用辅助物体以提升效率与稳定性。若无法找到，则分批运送是合理选择。"
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
  "task_understanding": "将七瓶饮料从厨房台面运送到卧室，供打牌的同学饮用。",
  "plan": [
    "移动到厨房台面，确认所有七瓶饮料的位置和状态。",
    "使用机械臂逐一抓取每瓶饮料，并确保夹爪稳定持握。",
    "保持身体平衡，从厨房移动至卧室。",
    "在卧室内将饮料放置于合适位置（如床头柜或桌面）。",
    "重复上述步骤直至所有饮料送达。"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "由于夹爪一次只能稳定携带一个物体，且饮料瓶为独立、易掉落的松散物品，无法通过组合方式一次性搬运多个，因此必须多次往返以确保安全和稳定性。",
  "safety_or_stability_consideration": "单个瓶子在移动过程中可能因振动或倾斜而滑落；每次仅携带一瓶可最大限度降低掉落风险，并保证机器人在行走时的平衡性。",
  "uncertainty_or_missing_information": "未观察到可用于辅助搬运的容器（如托盘）或其他工具，且图像中无明显障碍物影响路径。若存在合适容器，应优先使用以减少往返次数。",
  "reason": "直接操作是唯一可行方案，因为夹爪无法稳定携带多个松散物体；同时，目标物为独立、轻质的塑料瓶，适合单次搬运；未发现可提升效率的辅助工具，因此不进行额外寻找。"
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
  "task_understanding": "将七瓶饮料从厨房台面运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查当前环境以确认所有目标物体（七瓶饮料）的位置和状态。",
    "使用两只手同时抓取两组饮料（每只手最多两个），并确保抓握稳定。",
    "从厨房台面拿起饮料，沿最短路径前往卧室。",
    "在卧室放下饮料，并将它们放置在易于拿取的区域。"
  ],
  "target_objects": [
    "七瓶饮料"
  ],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "no",
  "selected_helper": "none",
  "tool_use_action_chain": [],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "使用双臂并行抓取以减少运输次数。",
  "safety_or_stability_consideration": "确保每只手的饮料组合稳定，避免掉落或倾倒。",
  "physical_feasibility_risk": "无显著风险，所有物体均在可操作范围内。",
  "uncertainty_or_missing_information": "未明确卧室的具体位置和路径障碍。",
  "reason": "从O0到O1的观察变化表明机器人已确认目标物的位置，并且环境允许直接执行任务。无需额外工具或帮助。",
  "failure_risk": "低，主要风险为运输过程中饮料倾倒，但可通过稳定抓取降低。"
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
  "task_understanding": "将七瓶饮料从厨房运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "移动到厨房的桌子旁，确认所有饮料瓶的位置和状态。",
    "逐一拾取每瓶饮料，并在保持平衡的前提下将其运送至卧室。",
    "将每瓶饮料放置在卧室中易于同学取用的位置。"
  ],
  "target_objects": [
    "饮料瓶"
  ],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "no",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "确认饮料瓶位置",
    "拾取并运送每瓶饮料"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "每次携带一瓶以确保稳定性和安全性。",
  "safety_or_stability_consideration": "移动时保持身体平衡，避免因单次携带过多导致倾倒或掉落。",
  "physical_feasibility_risk": "无显著风险，但需注意路径中可能存在的障碍物。",
  "uncertainty_or_missing_information": "未明确卧室的具体位置和路径细节。",
  "reason": "任务目标清晰，但环境信息有限，需依赖机器人自主导航完成任务。",
  "failure_risk": "低，主要风险为路径受阻或饮料瓶在运输中掉落。"
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
  "task_understanding": "将七瓶不同颜色的饮料从厨房运送到卧室，供正在打牌的同学解渴。",
  "plan": [
    "检查厨房台面上的七瓶饮料是否全部可见且可接近。",
    "逐一拿起每瓶饮料，并将其安全地携带到卧室。",
    "在卧室中将所有饮料放置在方便同学取用的位置。"
  ],
  "target_objects": [
    "饮料瓶"
  ],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "no",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "确认所有饮料瓶都在厨房台面上。",
    "从左到右依次拿起每瓶饮料。",
    "将每瓶饮料运送到卧室。"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "一次性携带尽可能多的瓶子以减少往返次数，但需确保每次搬运的安全性。",
  "safety_or_stability_consideration": "在移动过程中保持平衡，避免饮料瓶倾倒或液体洒出。",
  "physical_feasibility_risk": "如果一次携带过多瓶子，可能导致机器人失去平衡或无法稳定行走。",
  "uncertainty_or_missing_information": "不清楚卧室的具体位置和路径，需要导航至目标地点。",
  "reason": "任务要求将多瓶饮料从厨房运送到卧室，需分多次搬运以确保安全性和效率。",
  "failure_risk": "在运输过程中发生碰撞或瓶子掉落可能导致液体洒出或机器人损坏。"
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
  "task_understanding": "将七瓶饮料从厨房送达卧室，供正在打牌的同学饮用。",
  "plan": [
    "确认所有七瓶饮料都在厨房的台面上。",
    "一次性拿起全部七瓶饮料。",
    "离开厨房，前往卧室。",
    "在卧室内找到正在打牌的同学，并将饮料交给他们。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "所有饮料都位于同一位置且数量适中，一次性搬运可减少往返次数，提高效率。",
  "safety_or_stability_consideration": "使用双手或稳定方式同时携带多瓶饮料以防止掉落和打翻。",
  "uncertainty_or_missing_information": "无法确定卧室的具体位置、路径上是否有障碍物以及同学的确切人数和位置。",
  "reason": "根据O0和O1的观察，所有饮料均在厨房台面上且未被移动。由于任务要求尽快送达，一次性搬运全部饮料是最佳选择，既减少了往返次数又保证了效率。"
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
  "task_understanding": "将七瓶饮料从厨房送达卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查当前环境，确认所有饮料瓶均在厨房台面上且未被移动。",
    "使用双手同时抓取两组饮料（每只手最多两个），优先拿取最靠近边缘的瓶子以减少手臂伸展距离。",
    "从厨房出发，沿最短路径前往卧室，途中避开障碍物。",
    "进入卧室后，将饮料放置在打牌区域附近的稳定表面（如床头柜或小桌）上。",
    "返回厨房，重复上述步骤直至所有饮料送达。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "利用双手同时搬运以减少往返次数；优先取放靠近路径起点的瓶子以提高效率。",
  "safety_or_stability_consideration": "确保每次抓取时瓶身稳定，避免液体晃动或倾倒；搬运过程中保持低重心以防跌落。",
  "uncertainty_or_missing_information": "无法确认卧室的具体布局和打牌区域的位置，需根据实际路径调整最终放置点。",
  "reason": "基于O0和O1的观察，所有饮料瓶均在厨房台面上且位置稳定。机器人具备双手协同操作能力，可高效完成多件物品搬运任务。通过分批运输并优化取放顺序，可在保证安全的前提下快速完成任务。"
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
  "task_understanding": "将七瓶饮料从厨房运送到卧室，供打牌的同学饮用。",
  "plan": [
    "检查当前环境，确认所有饮料瓶均在厨房台面上且未被移动。",
    "使用机械臂逐一抓取每瓶饮料，确保每次只携带一瓶以保持稳定。",
    "从厨房出发，沿最短路径前往卧室，途中避开障碍物并保持身体平衡。",
    "将第一瓶饮料放入卧室指定位置后返回厨房，重复此过程直至所有饮料运送完毕。"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "由于夹爪一次只能稳定携带一瓶饮料，且需往返于厨房与卧室之间，因此需要多次往返以完成任务。",
  "safety_or_stability_consideration": "每次仅携带一瓶饮料可确保运输过程中的稳定性，避免因负载不均导致机器人失衡或饮料洒出。",
  "uncertainty_or_missing_information": "无法确定卧室的具体位置和路径是否畅通，需在移动过程中实时调整路线。",
  "reason": "基于两个观察，确认所有饮料瓶仍在厨房台面上且未被移动。由于夹爪的承载限制和环境不确定性，选择分次运送以确保安全与效率。"
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
{"task_understanding": "将厨房台面上的七瓶饮料快速、安全地送达卧室，供正在打牌的同学饮用。", "plan": ["检查周围环境以确保路径无障碍物。", "从厨房台面拿起所有七瓶饮料。", "沿最短路径前往卧室。", "在卧室中将饮料交给同学。"], "estimated_number_of_trips": "single", "efficiency_consideration": "一次性搬运全部饮料，减少往返次数，提高效率。", "safety_or_stability_consideration": "搬运时保持平稳，避免液体晃动或溢出，确保路径安全无绊倒风险。", "uncertainty_or_missing_information": "未明确卧室的具体位置和路径细节，但假设为室内常规布局。", "reason": "一次性完成任务可最大限度减少时间消耗，并降低因多次移动带来的潜在风险。"}
```

### Final Raw Response

```json
{"task_understanding": "将饮料从厨房送达卧室供打牌的同学饮用，当前机器人位于一个类似书桌或床头柜的区域，可能靠近卧室。", "plan": ["确认当前位置是否为卧室，若不确定则检查周围区域以确定位置。", "如果确认在卧室，则执行送水任务；否则返回厨房取饮料并前往卧室。"], "estimated_number_of_trips": "unknown", "efficiency_consideration": "避免盲目移动，先确认位置可减少无效行程。", "safety_or_stability_consideration": "检查环境时保持平稳，避免碰撞或倾倒物品。", "uncertainty_or_missing_information": "无法确定当前是否在卧室，且未看到饮料瓶，需进一步确认任务起点和终点。", "reason": "O1 显示的场景与 O0 的厨房不同，说明机器人已移动，但尚未到达目标地点，因此需要先定位再决定下一步行动。"}
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
{
  "task_understanding": "将厨房台面上的七瓶饮料（每瓶为独立包装）安全、高效地运送至卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查厨房台面，确认所有七瓶饮料的位置和状态，并评估是否可以一次性抓取。",
    "使用两只手同时抓取三到四瓶饮料，确保抓握稳定且不倾倒。",
    "从厨房出发，前往卧室，途中避免碰撞家具或障碍物。",
    "将第一批次的饮料放置在卧室内的安全位置（如床头柜或桌子）。",
    "返回厨房，重复上述步骤，运送剩余的饮料。",
    "确认所有饮料均已送达，并确保它们被妥善放置。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "通过一次抓取多瓶饮料（最多四瓶），减少往返次数，提高效率。",
  "safety_or_stability_consideration": "在搬运过程中保持瓶子稳定，避免液体溢出或掉落；确保路径畅通无阻。",
  "uncertainty_or_missing_information": "未明确卧室的具体布局和是否有足够的空间放置所有饮料。",
  "reason": "由于每只手最多能稳定抓取一个物体，且需考虑搬运过程中的稳定性与安全性，因此需要分批运送。通过优化每次搬运的数量，可以在保证安全的前提下减少总行程次数。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料（每瓶为独立包装）安全、高效地运送至卧室，供正在打牌的同学饮用。",
  "plan": [
    "确认当前观察到的托盘可用于承载多瓶饮料，提高单次搬运效率。",
    "返回厨房，使用两只手抓取三到四瓶饮料，并将它们放置在托盘上以形成稳定组合。",
    "利用托盘作为载体，一次性运送最多四瓶饮料至卧室，减少往返次数。",
    "重复上述步骤，运送剩余的饮料，确保每次搬运都保持稳定性。",
    "确认所有饮料均已送达，并将托盘和空瓶妥善处理或归位。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "利用托盘作为承载工具，单次可运送多瓶饮料，显著减少往返次数。",
  "safety_or_stability_consideration": "将饮料放置在托盘上可以增加搬运过程中的稳定性，避免液体溢出或瓶子掉落。",
  "uncertainty_or_missing_information": "未明确卧室的具体布局和是否有足够的空间放置所有饮料及托盘。",
  "reason": "当前观察到的托盘是一个适合用于承载多瓶饮料的物体，能够有效提升单次搬运效率。因此，更新计划以利用该工具，并继续执行任务。"
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
{"task_understanding": "将厨房台面上的七瓶饮料（每瓶为独立包装）安全、高效地运送至卧室，供正在打牌的同学饮用。", "plan": ["检查并确认所有饮料瓶均在厨房台面且未被遮挡或固定。", "使用机械臂逐一抓取饮料瓶，并确保每次仅携带一瓶以保证稳定性和安全性。", "从厨房出发，沿最短路径移动至卧室，途中保持身体平衡，避免碰撞家具。", "将第一瓶饮料放置于卧室指定位置（如床头柜或桌面），返回厨房继续搬运下一瓶。", "重复上述步骤，直至所有七瓶饮料全部送达卧室。"], "estimated_number_of_trips": "multiple", "efficiency_consideration": "为减少往返次数并提高效率，应优先确保每次运输的稳定性与安全性；若条件允许且物体紧密成组（如用托盘固定），可考虑一次携带多瓶，但需评估夹爪承载能力及移动过程中的平衡风险。", "safety_or_stability_consideration": "在搬运过程中必须保持身体平衡，避免因负载不均或路径障碍导致倾倒；每次仅携带一瓶饮料以确保抓取和运输的稳定性。", "uncertainty_or_missing_information": "未明确卧室的具体位置、路径中是否存在障碍物或狭窄通道，以及是否允许使用辅助工具（如托盘）一次性搬运多瓶饮料。", "reason": "由于任务要求尽快送达且需保证安全，因此采用分次单瓶运输以确保稳定性；同时考虑到可能存在的环境不确定性，优先选择低风险、高可控性的执行策略。"}
```

### Final Raw Response

```json
{"task_understanding": "将七瓶饮料从厨房运送至卧室，供打牌的同学饮用。", "plan": ["确认当前观察区域内无可用的承载工具（如托盘）用于一次性搬运多瓶饮料；检查附近区域以寻找可能适合固定或携带多个瓶子的辅助物体（如托盘、盒子等）。", "若未发现合适载体，则继续采用单瓶运输策略，确保每次搬运的安全与稳定。", "返回厨房取第一瓶饮料，沿最短路径前往卧室，途中保持身体平衡并避开障碍物。", "在卧室放置第一瓶后返回厨房，重复此过程直至所有饮料送达。"], "estimated_number_of_trips": "multiple", "efficiency_consideration": "当前观察未提供可用于批量运输的物体，因此无法提高单次搬运效率；继续采用分批运输以确保任务安全完成。", "safety_or_stability_consideration": "在无辅助工具的情况下，坚持每次仅携带一瓶饮料，避免因负载不均导致移动不稳定或倾倒风险。", "uncertainty_or_missing_information": "未明确卧室与厨房之间的路径是否畅通、是否存在其他潜在承载物（如托盘）可被利用；当前观察区域未发现可用物体。", "reason": "新观察中未出现适合用于批量运输的物体，且原任务要求尽快送达，因此继续执行原有计划并优先确保安全性和稳定性，同时持续检查附近区域以寻找可能提升效率的机会。"}
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
  "task_understanding": "将厨房台面上的七瓶饮料快速送达卧室，供正在打牌的同学解渴。",
  "plan": [
    "检查周围环境以确保路径畅通无阻。",
    "一次性拿起所有七瓶饮料，避免多次往返。",
    "从厨房出发，沿最短路径前往卧室。",
    "将饮料平稳地放在卧室的桌子上或指定位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "为了尽快送达，应一次性携带所有饮料，减少运输次数。",
  "safety_or_stability_consideration": "在搬运过程中需保持平衡，避免液体晃动或洒出，确保路径上没有障碍物以防绊倒。",
  "uncertainty_or_missing_information": "不清楚卧室的具体位置和房间内是否有合适的放置空间。",
  "reason": "一次性运送所有饮料可以最大化效率，减少时间消耗。同时，需要在移动中保持稳定以防止意外发生。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料快速送达卧室，供正在打牌的同学解渴。",
  "plan": [
    "确认当前观察到的托盘可以用于一次性承载所有饮料，提高运输效率。",
    "返回厨房，使用托盘收集所有七瓶饮料。",
    "从厨房出发，沿最短路径前往卧室。",
    "将装有饮料的托盘平稳地放在卧室的桌子上或指定位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "利用托盘一次性运输所有饮料，避免多次搬运，提高效率。",
  "safety_or_stability_consideration": "在移动过程中确保托盘上的饮料稳定，防止倾倒或洒出。",
  "uncertainty_or_missing_information": "不清楚卧室的具体位置和房间内是否有合适的放置空间。",
  "reason": "当前观察到的托盘是一个适合承载多瓶饮料的工具，可以显著提高运输效率。因此，计划调整为使用该托盘进行一次性运送。"
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
{"task_understanding": "将七瓶饮料从厨房台面运送到卧室，供正在打牌的同学饮用。", "plan": ["检查所有饮料瓶是否都在台面上且可安全抓取。", "用右手拿起最左边的黄色瓶子，同时用左手拿起旁边的蓝色瓶子。", "确认两只手各持一瓶后，离开厨房前往卧室。", "在卧室放下第一组两瓶饮料，并准备返回取剩余的。", "重复上述步骤，分批将所有七瓶饮料运送到卧室。"], "estimated_number_of_trips": "few", "efficiency_consideration": "由于每只手最多能稳定拿两个瓶子，且总共有七个瓶子，需至少三次往返才能全部送达；优先确保运输过程中的稳定性以避免洒出。", "safety_or_stability_consideration": "搬运过程中保持双手平衡，防止饮料瓶滑落或倾倒，尤其注意在移动中避开障碍物。", "uncertainty_or_missing_information": "无法确认卧室的具体位置和路径是否畅通；未明确是否有其他人在场可能影响通行。", "reason": "基于当前环境布局和机器人能力限制，需分批运输以保证安全与效率，同时考虑潜在的路径不确定性。"}
```

### Final Raw Response

```json
{"task_understanding": "将七瓶饮料从厨房台面运送到卧室，供正在打牌的同学饮用。", "plan": ["确认当前观察中未发现任何饮料瓶，因此需返回原位置继续任务。", "检查厨房区域以重新定位所有饮料瓶的位置。", "若在附近区域（如橱柜下方或台面边缘）发现遗漏的瓶子，则立即抓取并准备运输。", "若未发现新物体，继续前往卧室运送已有的饮料瓶，并规划后续返回路径。"], "estimated_number_of_trips": "few", "efficiency_consideration": "由于当前观察中无可用物品，应尽快完成剩余运输任务以减少延迟；优先确保已完成的瓶子送达目标区域。", "safety_or_stability_consideration": "在移动过程中保持平稳，避免因路径不熟悉导致碰撞或掉落。", "uncertainty_or_missing_information": "无法确认饮料瓶是否被移动或隐藏，需进一步检查厨房台面及周边区域。", "reason": "当前观察未提供与任务直接相关的物体信息，因此继续执行原计划并补充对周围环境的检查以确保完整性。"}
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
{"task_understanding": "将厨房台面上的七瓶饮料（每瓶为独立包装）安全、快速地运送至卧室，供正在打牌的同学饮用。", "plan": ["移动到厨房台面附近并确认所有饮料的位置和状态。", "逐个用夹爪拾取饮料瓶，并确保每次只携带一个以保持平衡与稳定。", "从厨房出发，沿最短路径前往卧室，途中注意避障并保持身体平衡。", "在卧室中将每瓶饮料放置于同学可轻松拿到的区域（如床边或桌面上）。", "确认所有饮料均已送达且无掉落或损坏。"], "estimated_number_of_trips": "multiple", "efficiency_consideration": "由于夹爪一次只能稳定携带一个物体，需多次往返以完成全部运送任务；优先选择最短路径并避免不必要的移动以节省时间。", "safety_or_stability_consideration": "搬运过程中必须保持身体平衡，防止因负载不均或地面湿滑导致倾倒；每次仅携带一瓶饮料以确保夹爪抓握稳定。", "uncertainty_or_missing_information": "未明确卧室的具体位置和路径上的障碍物分布情况，需在移动前进行环境感知确认。", "reason": "夹爪承载能力有限且为单次搬运设计，无法一次性携带多个松散物体；同时需确保机器人在移动过程中的稳定性与安全性，因此需要多次往返完成任务。"}
```

### Final Raw Response

```json
{"task_understanding": "将七瓶饮料从厨房运送至卧室，供打牌的同学饮用。", "plan": ["确认当前所在位置为厨房台面附近，并识别出托盘、手机等物体的位置和状态。", "检查托盘是否可用于一次性携带多个饮料瓶以提高运输效率；若可行，则规划使用托盘进行批量搬运。", "若托盘不适合或无法稳定承载多瓶饮料，则继续逐个用夹爪拾取并运送每瓶饮料。", "沿最短路径前往卧室，途中注意避障并保持身体平衡。", "在卧室中将所有饮料放置于同学可轻松拿到的区域（如床边或桌面上）。", "确认所有饮料均已送达且无掉落或损坏。"], "estimated_number_of_trips": "few", "efficiency_consideration": "托盘可能用于批量运输，减少往返次数；若使用托盘需确保其稳定性与负载能力，否则仍采用单瓶搬运以保证安全。", "safety_or_stability_consideration": "无论是否使用托盘，均需保持身体平衡，避免因负载不均或路径障碍导致倾倒。", "uncertainty_or_missing_information": "未明确托盘的承重能力和稳定性，也未确认其是否适合用于搬运饮料瓶；需进一步评估后决定是否采用批量运输方案。", "reason": "新观察中出现的托盘可能提升效率，但需验证其适用性；若不可用则继续单瓶搬运，同时持续检查周围环境以优化路径和任务执行。"}
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
  "task_understanding": "将厨房台面上的七瓶饮料（水）运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "拿起最左边的第一瓶饮料。",
    "转身离开厨房区域，前往卧室方向。",
    "进入卧室，将第一瓶饮料放在床边或桌子上。",
    "返回厨房，拿起第二瓶饮料。",
    "重复上述过程，依次将剩余的六瓶饮料运送到卧室。",
    "在卧室中整理好所有饮料，确保它们方便取用。"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "由于每瓶饮料体积小、重量轻，且厨房与卧室距离较近，单次搬运一瓶是可行的。虽然需要多次往返，但避免了因一次携带过多而增加掉落或倾倒的风险。",
  "safety_or_stability_consideration": "直接逐瓶运送可以确保每瓶都稳定放置，防止液体泄漏或瓶子滚动造成安全隐患。",
  "uncertainty_or_missing_information": "无法确定卧室的具体位置和路径是否畅通，也无法确认是否有其他障碍物。此外，未说明是否需要将所有饮料一次性送达，还是分批送达。",
  "reason": "当前视野中没有辅助物体可以用于批量搬运这些饮料，且任务要求是‘尽快’送达。直接逐瓶运送虽然次数多，但操作简单、安全可靠，无需额外准备工具或进行复杂规划。因此选择直接操作，不进行短程寻找辅助物体。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料（水）运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "拿起金属托盘。",
    "返回厨房，依次将七瓶饮料放入托盘中。",
    "端起装有所有饮料的托盘。",
    "前往卧室，将托盘中的饮料放在床边或桌子上。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "利用金属托盘可以一次性搬运所有饮料，显著减少往返次数，提高任务效率。",
  "safety_or_stability_consideration": "使用托盘可以稳定地承载多瓶饮料，避免单手搬运时因不平衡导致的掉落或倾倒风险。",
  "uncertainty_or_missing_information": "无法确认托盘是否足够大以容纳所有七瓶饮料，也无法确定从厨房到卧室的路径上是否有障碍物影响托盘的移动。",
  "reason": "当前观察中发现的金属托盘是一个非常适合用于批量搬运饮料的辅助物体。相比逐瓶运送，使用托盘能大幅提高效率并增强稳定性。因此，计划更新为先获取托盘，再利用其一次性完成所有饮料的运输任务。"
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
  "task_understanding": "将厨房台面上的七瓶饮料（水）安全、快速地运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查双手是否能稳定抓取两瓶饮料，确认可以同时搬运最多两瓶。",
    "从台面左侧开始，用左手拿起第一瓶黄色饮料和第二瓶蓝色饮料。",
    "将手中的两瓶饮料平稳地移出厨房区域，进入走廊并前往卧室。",
    "在卧室内放下第一组两瓶饮料。",
    "返回厨房，用右手拿起第三瓶橙色饮料和第四瓶绿色饮料。",
    "将这第二组两瓶饮料运送到卧室，并放在已放置的饮料旁边。",
    "再次返回厨房，用左手拿起第五瓶透明蓝色饮料和第六瓶深蓝色饮料。",
    "将这第三组两瓶饮料运送到卧室并摆放整齐。",
    "最后返回厨房，用右手拿起第七瓶橙色饮料。",
    "将最后一瓶饮料运送到卧室，并与其他饮料集中放置。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "通过每次搬运两瓶饮料，减少往返次数，提高效率；所有饮料均在台面可见且易于抓取，无需额外辅助工具。",
  "safety_or_stability_consideration": "每只手仅携带一瓶或两瓶稳定、不易滑落的塑料瓶，确保运输过程中的稳定性与安全性。",
  "uncertainty_or_missing_information": "无法确认卧室的具体位置和路径是否畅通，但根据常识判断为短距离移动；未提供饮料重量信息，假设在机器人承载范围内。",
  "reason": "目标物明确且可见，所有饮料均放置于台面，易于抓取。每只手可稳定携带一个或两个瓶子，无需辅助物体。通过分批搬运（每次两瓶）可在最少往返次数内完成任务，效率高、风险低。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料（水）安全、快速地运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "确认当前视野中未见任何饮料瓶，但观察到一个金属烤盘，可作为临时承载工具以提高单次搬运效率。",
    "检查双手是否能稳定抓取两瓶饮料，并评估使用烤盘的可行性：将多瓶饮料集中放置于烤盘上，一次运载更多数量。",
    "返回厨房台面，用左手拿起第一瓶黄色饮料和第二瓶蓝色饮料，放入烤盘中。",
    "用右手拿起第三瓶橙色饮料、第四瓶绿色饮料，并将其整齐摆放在烤盘内。",
    "确认烤盘上的六瓶饮料稳定放置，无倾倒风险。",
    "双手稳持烤盘边缘，从厨房移出并前往卧室。",
    "在卧室内放下烤盘及所有饮料。",
    "返回厨房，取回剩余的一瓶橙色饮料，并运送到卧室。",
    "将最后一瓶饮料与其余饮料集中摆放。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "利用金属烤盘作为承载工具，可一次性搬运最多六瓶饮料，显著减少往返次数，提升整体效率。",
  "safety_or_stability_consideration": "烤盘提供稳定平面，避免单手或双手直接持握多瓶时的滑落风险；所有瓶子在烤盘内排列整齐，运输过程更安全。",
  "uncertainty_or_missing_information": "无法确认烤盘是否足够大以容纳六瓶饮料且保持平衡，但根据其尺寸和常见设计判断可行；未提供卧室路径信息，假设为短距离移动。",
  "reason": "当前观察中发现的金属烤盘是适合任务的辅助物体，可提升单次搬运量与稳定性。因此调整计划，利用烤盘集中运输大部分饮料，仅需一次额外往返处理剩余一瓶，整体效率更高且风险更低。"
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
  "task_understanding": "将厨房台面上的七瓶饮料（每瓶为单个独立物体）安全、快速地运送至卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查当前视野中是否有可辅助搬运的容器或托盘以提高效率和稳定性。",
    "确认无合适辅助物后，使用机械臂夹爪逐瓶抓取饮料。",
    "将第一瓶饮料移至移动底盘上并保持平衡，然后前往卧室。",
    "在卧室放下第一瓶饮料，并返回厨房继续运送下一瓶。",
    "重复上述步骤直至所有七瓶饮料全部送达。"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "由于夹爪一次只能稳定携带一个物体，且无合适辅助物可一次性搬运多瓶，因此需多次往返以完成任务。",
  "safety_or_stability_consideration": "单次仅携带一瓶饮料可确保运输过程中的稳定性与安全性，避免因负载过重或重心不稳导致掉落。",
  "uncertainty_or_missing_information": "无法确认卧室的具体位置及路径是否畅通；未提供房间布局图以判断是否存在障碍物。",
  "reason": "目标物体为多个独立、易滑落的塑料瓶，且当前视野中无明显可用于批量搬运的辅助工具（如托盘或容器），因此必须采用逐个运输的方式。直接操作虽效率较低但安全可靠，无需短程寻找辅助物以避免增加任务复杂度和时间成本。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料（每瓶为单个独立物体）安全、快速地运送至卧室，供正在打牌的同学饮用。",
  "plan": [
    "识别到当前区域存在一个金属托盘，可用于一次性承载多瓶饮料以减少往返次数。",
    "使用机械臂夹爪将第一瓶饮料放置于托盘上，并依次继续放置其余六瓶饮料，确保每瓶稳固不滑动。",
    "确认所有七瓶饮料均安全置于托盘后，移动底盘平稳抬起托盘并保持平衡。",
    "前往卧室，途中避免路径障碍物以保证运输稳定。",
    "在卧室放下托盘并将饮料逐一取出或整体放置于合适位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "利用金属托盘可一次性搬运多瓶饮料，显著减少往返次数，提高任务效率。",
  "safety_or_stability_consideration": "托盘提供稳定承载面，配合机械臂精准放置和底盘平稳移动，降低单个物体掉落风险。",
  "uncertainty_or_missing_information": "无法确认托盘是否足够大以容纳全部七瓶饮料且保持平衡；未明确卧室路径是否存在限制。",
  "reason": "当前观察中发现的金属托盘是适合本任务的辅助物体，能够提升搬运效率并增强稳定性。因此调整原计划为使用托盘一次性运输所有饮料，无需再逐个搬运或短程寻找其他工具。"
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
  "task_understanding": "将厨房台面上的七瓶饮料（水）安全、快速地运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "识别并确认所有七瓶饮料的位置和状态。",
    "从厨房台面拿起最左侧的一瓶饮料。",
    "转身离开厨房，前往卧室方向。",
    "进入卧室，将手中的饮料放在床边的桌子上。",
    "返回厨房，重复上述步骤，依次取回剩余六瓶饮料，并逐一送至卧室。"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "为了减少往返次数并提高效率，应一次性搬运尽可能多的瓶子。然而，由于瓶子是独立的、易掉落的物体且可能较重，单次搬运过多会增加倾倒或掉落的风险，因此采用分批运输的方式更为安全和稳定。",
  "safety_or_stability_consideration": "饮料瓶为塑料材质，但装满液体后重心较高，在移动过程中容易因晃动而倾倒。为了确保安全和稳定性，每次只搬运一瓶，避免同时携带多瓶导致失衡或掉落。",
  "uncertainty_or_missing_information": "无法确定卧室的具体位置、路径上是否有障碍物以及床边桌子是否足够大以容纳所有饮料。此外，未提供机器人当前的负载能力信息。",
  "reason": "直接操作是唯一可行的方式，因为没有其他辅助物体（如推车或托盘）出现在图像中，且任务要求‘尽快’送达，因此必须通过多次往返来完成搬运。使用辅助工具会增加准备时间，而直接搬运虽然需要更多次数，但能更快启动并持续进行。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料（水）安全、快速地运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "识别并确认所有七瓶饮料的位置和状态。",
    "在当前观察中发现一个金属烤盘，该物体可用于一次性承载多瓶饮料，从而减少往返次数。",
    "返回厨房台面，将七瓶饮料全部放入烤盘中，确保其稳定放置。",
    "抬起装有饮料的烤盘，转身离开厨房，前往卧室方向。",
    "进入卧室，将整个烤盘放在床边的桌子上，并将饮料分发给同学。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "利用金属烤盘作为承载工具，可以一次性搬运所有七瓶饮料，显著减少往返次数，提高整体效率。",
  "safety_or_stability_consideration": "将多瓶饮料集中放置在烤盘中，并确保其重心居中、平稳，可有效防止运输过程中的倾倒风险。同时，避免单手提握多个瓶子带来的不稳定性。",
  "uncertainty_or_missing_information": "无法确定烤盘的尺寸是否足以容纳所有七瓶饮料且保持稳定；也无法确认从厨房到卧室的路径上是否存在障碍物或需要避让的人。",
  "reason": "当前观察中发现的金属烤盘是一个有效的辅助物体，能够提升任务效率和稳定性。因此，计划已更新为使用该烤盘进行一次性搬运，而非分批运输。无需继续检查附近区域，因为已有明确可用的工具。"
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
  "task_understanding": "将厨房台面上的七瓶饮料（每瓶为独立小物体）搬运至卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查双手是否能同时稳定抓取两个瓶子，确认可安全携带最多两瓶。",
    "从左到右依次用左手和右手各拿两瓶，共四瓶，前往卧室。",
    "返回厨房，再次拿起剩余三瓶（一手两瓶，另一手一瓶），前往卧室。",
    "将所有饮料放置在卧室的合适位置。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "使用双手并行搬运可减少往返次数，提高效率；无需额外辅助物体，因瓶子为独立且稳定的小型容器。",
  "safety_or_stability_consideration": "每只手最多拿两瓶，确保抓握稳固，避免液体洒出或掉落。",
  "uncertainty_or_missing_information": "未明确卧室与厨房之间的路径是否畅通、是否有障碍物；但假设为常规室内环境，无障碍。",
  "reason": "目标物体为多个独立且稳定的瓶子，双手可同时操作，无需辅助工具。搬运过程可通过分批完成，效率高且安全。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料搬运至卧室，供正在打牌的同学饮用。",
  "plan": [
    "确认当前场景中未见任何饮料瓶，说明它们可能位于其他位置或已被移动。",
    "利用烤盘作为辅助工具，将其用于集中承载多瓶饮料以减少单次搬运数量。",
    "返回厨房台面，将七瓶饮料全部放入烤盘中，确保稳定放置。",
    "双手抓取装有饮料的烤盘（一手托底，一手扶边），前往卧室。",
    "在卧室放下烤盘并取出饮料供同学使用。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "利用烤盘一次性搬运所有饮料，显著减少往返次数，提升效率。",
  "safety_or_stability_consideration": "烤盘提供稳定承载面，避免单手拿多瓶导致滑落或倾倒，提高搬运安全性。",
  "uncertainty_or_missing_information": "未明确烤盘是否足够大以容纳所有饮料瓶；但假设其尺寸合适。若不可用，则需重新评估。",
  "reason": "当前观察中出现的烤盘可作为有效辅助物体，用于集中运输多瓶饮料，优于分批搬运。因此更新计划以利用该物体，并继续执行任务。"
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
  "task_understanding": "将七瓶饮料从厨房台面运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "移动到厨房台面前方，确保身体平衡。",
    "使用机械臂和夹爪逐一抓取每瓶饮料，每次携带一瓶以保证稳定。",
    "返回卧室，将第一瓶饮料放置在合适位置。",
    "重复上述步骤，直到所有七瓶饮料全部运送到卧室。"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "由于夹爪一次只能稳定携带一个物体，且为确保安全和稳定性，必须分多次运输，因此无法通过单次搬运完成任务。",
  "safety_or_stability_consideration": "饮料瓶为独立个体，松散放置在台面上，直接抓取并逐个运送可避免掉落或倾倒风险。",
  "uncertainty_or_missing_information": "未提供卧室的具体位置和路径信息，但假设厨房与卧室之间无障碍物且路径清晰。",
  "reason": "目标物体是七瓶独立的饮料瓶，无明显辅助工具可用。夹爪一次只能稳定携带一个物体，因此必须分多次运输。直接操作是最简单、最安全的方式，无需额外准备或使用辅助物体。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将七瓶饮料从厨房台面运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "移动到厨房台面前方，确保身体平衡。",
    "使用机械臂和夹爪逐一抓取每瓶饮料，每次携带一瓶以保证稳定。",
    "返回卧室，将第一瓶饮料放置在合适位置。",
    "重复上述步骤，直到所有七瓶饮料全部运送到卧室。"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "当前观察中未发现可用于辅助搬运的物体（如托盘或容器），且原任务目标物为独立瓶子，无法通过组合方式提升效率。",
  "safety_or_stability_consideration": "夹爪一次只能稳定携带一个物体，直接操作是唯一安全的方式。使用托盘等工具在此场景中不适用，因为当前未发现可用的辅助物体。",
  "uncertainty_or_missing_information": "未提供卧室的具体位置和路径信息，但假设厨房与卧室之间无障碍物且路径清晰。",
  "reason": "新观察 O1 中存在一个烤盘，理论上可用于一次性携带多个饮料瓶以减少往返次数。然而，该烤盘为长方形、无防滑设计，且夹爪无法稳定抓取其边缘进行搬运，因此不适合用于辅助运输。此外，当前任务目标物为独立瓶子，无需组合操作。故继续执行原计划，不改变高层策略。"
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
{"task_understanding": "将厨房台面上的七瓶饮料快速送达卧室，供正在打牌的同学饮用", "plan": ["从厨房台面拿起一瓶饮料", "转身离开厨房前往卧室", "在卧室内放下饮料", "重复上述步骤直到所有饮料都被送至卧室"], "target_objects": ["饮料瓶"], "helper_needed": "no", "helper_purpose": "none", "visible_helper_detected": "no", "visible_helper_objects": [], "search_for_helper_if_none_visible": "no", "selected_helper": "none", "tool_use_action_chain": [], "estimated_number_of_trips": "multiple", "efficiency_consideration": "每次运送一瓶以确保稳定性和安全性", "safety_or_stability_consideration": "避免在移动过程中饮料瓶倾倒或掉落", "physical_feasibility_risk": "无明显风险，但需注意路径中是否有障碍物", "uncertainty_or_missing_information": "未明确说明卧室的具体位置和路径是否畅通", "reason": "由于每只手只能稳定拿住一个物体，且需要确保饮料瓶不倾倒，因此每次运送一瓶是最佳选择。同时，考虑到任务的紧急性，应尽快完成所有运输任务。", "failure_risk": "如果路径中有障碍物或地面湿滑，可能导致摔倒或饮料洒出"}
```

### Final Raw Response

```json
{"task_understanding": "将厨房台面上的七瓶饮料快速送达卧室，供正在打牌的同学饮用", "plan": ["确认当前环境中的可用空间和路径", "使用托盘作为承载工具一次性运送多瓶饮料", "从厨房台面拿起托盘并放置饮料瓶于其上", "转身离开厨房前往卧室", "在卧室内放下托盘及饮料"], "target_objects": ["饮料瓶"], "helper_needed": "yes", "helper_purpose": "aggregation", "visible_helper_detected": "yes", "visible_helper_objects": ["托盘"], "search_for_helper_if_none_visible": "no", "selected_helper": "托盘", "tool_use_action_chain": ["拿起托盘", "将饮料瓶放入托盘中", "搬运托盘至卧室"], "estimated_number_of_trips": "few", "efficiency_consideration": "使用托盘可一次性运送多瓶饮料，减少往返次数", "safety_or_stability_consideration": "确保托盘上的饮料瓶稳定放置，避免倾倒", "physical_feasibility_risk": "无明显风险，但需注意托盘的承重能力", "uncertainty_or_missing_information": "未明确说明托盘是否足够大以容纳所有饮料瓶", "reason": "当前观察中发现了一个托盘，可以用于一次性运送多瓶饮料，提高效率。因此，更新计划以利用该工具进行任务执行。", "failure_risk": "如果托盘无法承载所有饮料瓶或在搬运过程中不稳定，可能导致部分饮料洒出"}
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
  "task_understanding": "将七瓶饮料从厨房台面运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "移动到厨房台面附近，确认所有饮料瓶的位置和状态。",
    "逐一用夹爪抓取每瓶饮料，并将其安全地携带至卧室。",
    "在卧室中将饮料放置在方便同学拿取的区域。"
  ],
  "target_objects": [
    "黄色饮料瓶",
    "蓝色饮料瓶",
    "橙色饮料瓶",
    "绿色饮料瓶",
    "透明饮料瓶",
    "深蓝色饮料瓶",
    "棕色饮料瓶"
  ],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "no",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "使用夹爪抓取第一瓶饮料。",
    "移动到卧室方向，保持身体平衡。",
    "放下第一瓶饮料。"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "由于每次只能携带一瓶饮料，需要多次往返以提高效率。",
  "safety_or_stability_consideration": "在移动过程中需确保夹爪稳定抓取瓶子，避免掉落或倾倒。",
  "physical_feasibility_risk": "单次携带多瓶饮料可能导致平衡问题或物体不稳定。",
  "uncertainty_or_missing_information": "未明确卧室的具体位置和路径障碍。",
  "reason": "任务要求快速送达，但受限于夹爪一次只能稳定携带一个物体的物理限制。",
  "failure_risk": "在运输过程中可能因移动不稳导致饮料瓶掉落或洒出。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将七瓶饮料从厨房台面运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "确认当前环境为厨房台面，未发现目标饮料瓶，需继续检查附近区域以定位所有饮料瓶。",
    "在移动过程中保持对周围环境的扫描，确保路径畅通且无障碍物。",
    "一旦找到饮料瓶，使用夹爪逐一抓取并运送到卧室。"
  ],
  "target_objects": [
    "黄色饮料瓶",
    "蓝色饮料瓶",
    "橙色饮料瓶",
    "绿色饮料瓶",
    "透明饮料瓶",
    "深蓝色饮料瓶",
    "棕色饮料瓶"
  ],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "yes",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "检查台面及周围区域，确认饮料瓶位置。",
    "若发现目标物体，则使用夹爪抓取并移动至卧室。"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "需多次往返以完成全部运输任务。",
  "safety_or_stability_consideration": "在搬运过程中确保夹爪稳定，避免饮料瓶倾倒或掉落。",
  "physical_feasibility_risk": "当前未发现目标物体，可能需要更长时间搜索。",
  "uncertainty_or_missing_information": "不确定饮料瓶是否已被移动或隐藏。",
  "reason": "新观察中未发现任何饮料瓶，需继续检查附近区域以完成任务。",
  "failure_risk": "因未能及时定位所有饮料瓶而导致任务延迟。"
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
{"task_understanding": "将七瓶不同颜色的饮料从厨房台面运送到卧室，供正在打牌的同学饮用。", "plan": ["检查周围环境以确认路径无障碍", "拿起最左边的黄色瓶子", "沿着安全路径前往卧室", "放下黄色瓶子", "返回厨房", "重复上述步骤直到所有瓶子都被运送至卧室"], "target_objects": ["饮料瓶"], "helper_needed": "no", "helper_purpose": "none", "visible_helper_detected": "no", "visible_helper_objects": [], "search_for_helper_if_none_visible": "no", "selected_helper": "none", "tool_use_action_chain": [], "estimated_number_of_trips": "multiple", "efficiency_consideration": "尽量减少往返次数，优先运送易碎或重的瓶子", "safety_or_stability_consideration": "确保在搬运过程中瓶子不会掉落或倾倒", "physical_feasibility_risk": "无明显风险，路径清晰且物体可移动", "uncertainty_or_missing_information": "未明确说明卧室的具体位置和路径细节", "reason": "任务目标是快速运送饮料，但需注意避免碰撞或洒出液体。由于没有其他辅助工具或人员协助，机器人需要独立完成多次往返运输。", "failure_risk": "低，只要保持平稳移动并避开障碍物即可成功完成任务"}
```

### Final Raw Response

```json
{"task_understanding": "将七瓶不同颜色的饮料从厨房台面运送到卧室，供正在打牌的同学饮用。", "plan": ["确认当前环境中的托盘可用于一次性运送多瓶饮料", "返回厨房取走所有饮料瓶并放置在托盘上", "沿安全路径前往卧室", "将托盘上的所有饮料瓶一次性送达卧室"], "target_objects": ["饮料瓶"], "helper_needed": "no", "helper_purpose": "none", "visible_helper_detected": "yes", "visible_helper_objects": ["托盘"], "search_for_helper_if_none_visible": "no", "selected_helper": "托盘", "tool_use_action_chain": ["使用托盘装载所有饮料瓶", "一次性运送至卧室"], "estimated_number_of_trips": "single", "efficiency_consideration": "利用托盘减少运输次数，提高效率", "safety_or_stability_consideration": "确保托盘上的瓶子在移动过程中保持稳定，避免倾倒或碰撞", "physical_feasibility_risk": "无明显风险，托盘可承载多瓶饮料且路径清晰", "uncertainty_or_missing_information": "未明确说明卧室的具体位置和路径细节", "reason": "当前观察到的托盘可用于一次性运送所有饮料瓶，显著提高效率并减少运输次数。因此调整计划以利用该工具完成任务。", "failure_risk": "低，只要确保托盘稳定且路径无障碍即可成功完成任务"}
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
  "task_understanding": "将厨房台面上的七瓶饮料快速送达卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查周围环境，确认路径无障碍物。",
    "一次性拿起所有七瓶饮料。",
    "从厨房出发，沿最短路径前往卧室。",
    "在卧室门口放下所有饮料。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "由于所有饮料都位于同一台面上且数量有限，一次性全部取走可以最大限度地减少往返次数，提高效率。",
  "safety_or_stability_consideration": "为确保运输过程中的稳定性，将瓶子并排握持，避免单手拿取导致倾倒或掉落。",
  "uncertainty_or_missing_information": "无法确定卧室的具体位置和路径细节，但根据常识推断厨房与卧室相邻，路径应较为直接。",
  "reason": "所有饮料集中放置在台面上，且数量不多，一次性搬运是最快、最高效的方案。无需使用辅助工具或分次运输。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料快速送达卧室，供正在打牌的同学饮用。",
  "plan": [
    "确认当前观察中未发现任何可作为辅助工具的物体。",
    "检查周围区域以寻找可能影响路径或任务执行的障碍物。",
    "根据上一轮观察，确定所有饮料位于厨房台面。",
    "一次性拿起所有七瓶饮料。",
    "从厨房出发，沿最短路径前往卧室。",
    "在卧室门口放下所有饮料。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "尽管当前观察中未发现可用的辅助工具，但根据上一轮信息，所有饮料已集中放置，一次性搬运仍是最高效的方式。",
  "safety_or_stability_consideration": "为确保运输过程中的稳定性，将瓶子并排握持，避免单手拿取导致倾倒或掉落。",
  "uncertainty_or_missing_information": "无法确定卧室的具体位置和路径细节，但根据常识推断厨房与卧室相邻，路径应较为直接。",
  "reason": "当前观察中未发现对任务有帮助的物体，且上一轮已明确饮料的位置。因此，无需改变原计划，继续执行一次性搬运并前往卧室的任务。"
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
  "task_understanding": "将厨房台面上的七瓶饮料（水）安全、快速地运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查厨房台面，确认所有7瓶饮料的位置和状态。",
    "用右手拿起最左边的一瓶黄色饮料，同时用左手拿起最右边的一瓶橙色饮料。",
    "将两瓶饮料从厨房台面移至地面或临时放置点（如餐桌），以腾出空间。",
    "使用双手分别拿起剩余的5瓶饮料，确保每只手稳定抓握1-2瓶，形成一个稳定的组合负载。",
    "从厨房出发，沿最短路径前往卧室，途中避免碰撞家具。",
    "进入卧室后，将所有饮料放置在同学可轻松取用的位置（如床头柜或地面）。",
    "确认所有饮料已送达，并检查是否有遗漏。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "通过同时使用双手并合理分配负载，减少往返次数，提高运输效率。",
  "safety_or_stability_consideration": "确保每只手抓握的饮料数量在稳定范围内，避免因失衡导致掉落或损坏。",
  "uncertainty_or_missing_information": "不清楚卧室的具体布局和同学的位置，但假设路径畅通且目标区域可访问。",
  "reason": "使用双手并行运输可以显著减少总行程次数，同时通过合理分配负载确保操作安全与稳定。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料（水）安全、快速地运送到卧室，供正在打牌的同学饮用。",
  "plan": [
    "确认当前观察到的托盘可用于承载多瓶饮料，提高单次运输效率。",
    "返回厨房台面，使用双手拾取所有7瓶饮料，并将它们整齐放置在托盘上以形成稳定负载。",
    "从厨房拿起装有饮料的托盘，沿最短路径前往卧室。",
    "进入卧室后，将托盘上的饮料放置在同学可轻松取用的位置（如床头柜或地面）。",
    "确认所有饮料已送达，并检查是否有遗漏。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "利用托盘作为承载工具，实现一次性运输全部饮料，减少往返次数并提升效率。",
  "safety_or_stability_consideration": "将饮料置于托盘上可增强整体负载的稳定性，降低单手或双手直接搬运时因失衡导致掉落的风险。",
  "uncertainty_or_missing_information": "不清楚卧室的具体布局和同学的位置，但假设路径畅通且目标区域可访问。",
  "reason": "当前观察到的托盘是一个适合承载多瓶饮料的工具，能够显著提升运输效率并增强负载稳定性。因此，调整计划以利用该物体，并继续执行任务。"
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
  "task_understanding": "将厨房台面上的七瓶饮料（每瓶为单个独立物体）安全、快速地运送至卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查周围环境，确认路径无障碍物，并确保移动底盘稳定。",
    "逐个使用机械臂和夹爪抓取饮料瓶，从厨房台面移出。",
    "将每瓶饮料运送到卧室，放置在易于拿取的位置。",
    "重复上述步骤直至所有饮料送达。"
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "由于夹爪一次只能稳定携带一个物体，且需确保移动过程中的稳定性，因此需要多次往返以完成全部运送任务。",
  "safety_or_stability_consideration": "在搬运过程中保持身体平衡，避免因单臂负载不均导致倾倒；每次仅携带一瓶饮料以保证抓取和运输的稳定性。",
  "uncertainty_or_missing_information": "未明确卧室的具体位置及路径细节，需根据实际环境调整移动路线。",
  "reason": "夹爪设计限制决定了无法一次性搬运多个松散物体，且为确保安全与稳定，必须逐个运送。同时，考虑到任务紧急性，应优先保证效率和可靠性。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "将厨房台面上的七瓶饮料（每瓶为单个独立物体）安全、快速地运送至卧室，供正在打牌的同学饮用。",
  "plan": [
    "检查当前区域是否包含可用于辅助搬运的工具或容器，例如托盘。",
    "发现金属烤盘可作为临时承载平台，用于一次性携带多瓶饮料以减少往返次数。",
    "返回厨房台面，使用机械臂将七瓶饮料依次放置于烤盘上，确保排列稳定。",
    "利用移动底盘将装有饮料的烤盘整体运送至卧室，避免多次搬运。",
    "在卧室中将烤盘平稳放下，并确认所有饮料易于取用。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "通过使用金属烤盘作为承载工具，可一次性运输多瓶饮料，显著减少往返次数，提升整体效率。",
  "safety_or_stability_consideration": "在将饮料放入烤盘时需确保排列紧凑且重心稳定；移动过程中保持底盘平衡以防止倾覆。",
  "uncertainty_or_missing_information": "未明确卧室的具体位置及路径细节，需根据实际环境调整移动路线。",
  "reason": "新观察中发现的金属烤盘可作为有效辅助工具，用于集中搬运多个饮料瓶，从而优化任务执行效率。因此更新计划以利用该物体，并继续推进任务。"
}
```

