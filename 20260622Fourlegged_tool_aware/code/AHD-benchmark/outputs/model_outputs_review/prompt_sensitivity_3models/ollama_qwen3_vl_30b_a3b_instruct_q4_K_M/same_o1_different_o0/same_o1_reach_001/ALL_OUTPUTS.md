# same_o1_reach_001: All Candidate Outputs

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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "从沙发下面取出遥控器",
  "plan": [
    "移动到沙发前，靠近遥控器所在的位置。",
    "使用机械臂伸入沙发下方，小心地抓取遥控器。",
    "将遥控器平稳地从沙发下取出并移至安全位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接移动到目标区域进行操作，避免不必要的路径规划以提高效率。",
  "safety_or_stability_consideration": "在伸入沙发下方时需注意机械臂的运动范围，确保不碰撞沙发或损坏遥控器。同时保持机器人自身稳定。",
  "uncertainty_or_missing_information": "无法确认遥控器的具体位置和形状，可能需要通过视觉辅助进行定位。",
  "reason": "根据观察O0和O1，机器人已确定遥控器位于沙发下方，且环境清晰，因此计划直接执行取物任务。"
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "从沙发下方取出遥控器",
  "plan": [
    "检查沙发下方区域，确认遥控器的位置和可接近性",
    "使用右手或左手（选择更合适的一只）伸入沙发下方，抓取遥控器",
    "将遥控器平稳地拿出，并确保不掉落",
    "完成任务"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "优先使用单次动作完成任务，避免不必要的移动和重复检查。",
  "safety_or_stability_consideration": "在伸入沙发下方时注意手臂与周围物体的碰撞风险，确保抓取稳定以防止遥控器掉落。",
  "uncertainty_or_missing_information": "无法确定遥控器是否被其他物品遮挡或卡住，需谨慎操作。",
  "reason": "根据两个观察，机器人已确认目标位置和环境，计划应聚焦于高效、安全地完成单次取出动作。"
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "从沙发下方取出遥控器",
  "plan": [
    "移动到沙发前方，确保身体平衡并留出足够的机械臂操作空间。",
    "使用机械臂伸入沙发下方，检查遥控器的位置和可抓取性。",
    "如果遥控器可见且无障碍物阻挡，用夹爪小心地将其取出。",
    "将遥控器放置在附近的稳定表面上。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "通过一次移动和操作完成任务，避免不必要的往返以提高效率。",
  "safety_or_stability_consideration": "保持底盘平衡，确保机械臂动作平稳，防止夹爪误伤或掉落物体。",
  "uncertainty_or_missing_information": "无法确定遥控器是否被其他物品遮挡或卡住，需在操作中实时判断。",
  "reason": "根据O0和O1的观察，机器人已确认沙发下方存在目标物且环境无明显障碍。计划聚焦于安全、高效地完成单次取物任务，并预留应对突发情况的空间。"
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "The robot needs to retrieve a remote control located under the sofa.",
  "plan": [
    "Move towards the sofa.",
    "Crawl or lower the body to reach underneath the sofa.",
    "Locate the remote control on the floor beneath the sofa.",
    "Pick up the remote control."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The robot should move directly towards the sofa and use its lowest possible profile to access the area underneath without needing to reposition multiple times.",
  "safety_or_stability_consideration": "Ensure stable movement when lowering the body to avoid tipping or damaging the furniture.",
  "uncertainty_or_missing_information": "It is unclear if there are any obstacles under the sofa that might impede access, such as other objects or uneven flooring.",
  "reason": "The robot must first approach the sofa and then lower itself to reach the remote control. The plan assumes a direct path based on the initial observation of the object's location."
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "从沙发下方取出遥控器",
  "plan": [
    "检查沙发下方区域以确认遥控器的位置和可接近性。",
    "使用右手或左手（选择更合适的一侧）伸入沙发下方，尝试抓取遥控器。",
    "如果遥控器被遮挡或难以直接接触，移动沙发或调整自身位置以获得更好的操作角度。",
    "成功抓取遥控器后，将其平稳移出沙发下方区域。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "优先使用单次动作完成任务，避免不必要的重复移动。",
  "safety_or_stability_consideration": "确保在伸入沙发下方时保持机器人平衡，避免因过度倾斜导致不稳定。",
  "uncertainty_or_missing_information": "无法确定遥控器是否被完全遮挡或是否有障碍物阻碍抓取。",
  "reason": "基于两个观察，任务目标一致但环境细节可能变化。计划需适应潜在的视野限制和物理障碍，确保操作安全且高效。"
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "The robot needs to retrieve a remote control located under the sofa. The initial observation shows the general area, but the exact position of the remote is not visible. A second observation provides a closer view of the space under the sofa, revealing a tray and other objects, which may obstruct access.",
  "plan": [
    "Move closer to the sofa to get a better view of the area underneath it.",
    "Assess whether the remote control is accessible or blocked by other objects (e.g., the tray).",
    "If accessible, extend the mechanical arm and use the gripper to grasp the remote control.",
    "Lift the remote control out from under the sofa while maintaining balance."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The robot should minimize unnecessary movements by directly approaching the target area after confirming its location. The plan prioritizes direct access to avoid repeated repositioning.",
  "safety_or_stability_consideration": "Maintain body balance while extending the arm under the sofa, ensuring no tipping occurs due to uneven weight distribution or obstruction.",
  "uncertainty_or_missing_information": "The exact position and orientation of the remote control are not clearly visible in O0. It is uncertain whether it is fully accessible or partially blocked by other objects like the tray seen in O1.",
  "reason": "The second observation provides critical details about the environment under the sofa, indicating potential obstacles that could hinder access to the remote. The plan must account for these findings to ensure successful retrieval."
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The initial observation (O0) shows the sofa and part of the surrounding area, but no clear view of the remote or any tools. The second observation (O1) reveals a tray on a table, which could potentially be used as an aid for retrieving the object from beneath the sofa.",
  "plan": [
    "Check the area under the sofa to confirm the location and accessibility of the remote control.",
    "If the remote is visible but out of reach, use the tray as a tool by placing it under the sofa to create a surface or leverage point to slide the remote out.",
    "Retrieve the remote from the tray or directly from under the sofa."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "Using the tray reduces the need for complex manipulation and allows for a more stable retrieval of the remote without requiring additional tools or multiple attempts.",
  "safety_or_stability_consideration": "The tray provides a stable surface to interact with the remote, minimizing the risk of dropping it or damaging the sofa during retrieval.",
  "uncertainty_or_missing_information": "It is uncertain whether the remote is visible in O0 or if it requires manipulation to be retrieved. The exact position and orientation of the remote under the sofa are not clear from either observation.",
  "reason": "The tray observed in O1 can serve as a useful auxiliary object for retrieving the remote without requiring additional tools or complex movements. Using the tray increases stability and reduces the risk of dropping the remote, making it more efficient than attempting direct retrieval."
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The initial observation (O0) shows the remote under the sofa, but it's not clearly visible or accessible from that angle. The second observation (O1) provides a closer view of the area beneath the sofa, revealing a tray and other objects on the floor, which may help in accessing the remote.",
  "plan": [
    "Check the area under the sofa to locate the remote control.",
    "Use the tray as a tool to slide or push the remote out from under the sofa.",
    "Retrieve the remote control using one hand while stabilizing the tray with the other."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "Using the tray as an auxiliary object allows for efficient retrieval without needing to move or reposition the sofa, reducing effort and time.",
  "safety_or_stability_consideration": "The tray provides a stable surface to push against, minimizing the risk of dropping the remote or losing balance during retrieval.",
  "uncertainty_or_missing_information": "It is unclear if the remote is fully visible in O1 or if it requires additional manipulation. The exact position and orientation of the remote under the sofa are uncertain.",
  "reason": "The tray observed in O1 can serve as a useful auxiliary object to help push the remote out from under the sofa, making retrieval easier and more stable than attempting direct hand access."
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The initial observation (O0) shows the remote under the sofa, but it's not clearly visible or accessible from that angle. The second observation (O1) provides a closer view of the area beneath the sofa and confirms the presence of the remote, along with other objects like a tray and cloth.",
  "plan": [
    "Move to a position where the remote under the sofa is clearly visible and reachable.",
    "Use the mechanical arm to grasp the remote control from under the sofa.",
    "Lift the remote out from under the sofa and move it to a safe location."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The remote is clearly visible in O1, allowing for direct retrieval without needing additional tools or objects. The proximity of other items (tray, cloth) does not obstruct access and may even provide stability during the operation.",
  "safety_or_stability_consideration": "The remote is a small object that can be securely held by the gripper. No complex manipulation or stabilization is required as it's directly accessible under the sofa without risk of falling or tipping.",
  "uncertainty_or_missing_information": "It is unclear if the remote is fully visible in O0, but O1 confirms its location and accessibility. There are no indications that additional objects are needed to retrieve it safely.",
  "reason": "The remote control is clearly visible under the sofa in O1, and there are no obstacles or risks preventing direct retrieval with the gripper. No auxiliary tools or objects are required, making a single trip sufficient."
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "从沙发下方取出遥控器",
  "plan": [
    "检查沙发下方区域，确认遥控器的位置和状态。",
    "使用机械臂伸入沙发下方，小心地抓取遥控器。",
    "将遥控器平稳地从沙发下移出并放置在安全位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作目标物，无需额外辅助物体，提高效率。",
  "safety_or_stability_consideration": "确保机械臂动作平稳，避免碰撞沙发或损坏遥控器。",
  "uncertainty_or_missing_information": "无法确定遥控器是否被其他物品遮挡，需谨慎操作。",
  "reason": "目标物（遥控器）清晰可见且位于可直接操作的范围内，无需借助辅助物体。"
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The initial observation (O0) shows the remote under the sofa, but it's not clearly visible or accessible due to the sofa's design and low lighting. The second observation (O1) reveals that there is a tray on a table nearby, which could be used as an auxiliary object to assist in retrieving the remote.",
  "plan": [
    "Move to the table where the tray is located.",
    "Pick up the tray from the table.",
    "Position the tray under the sofa, aligning it with the area where the remote control is located.",
    "Use the tray to slide or push the remote control out from under the sofa.",
    "Retrieve the remote control from the floor."
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "Using the tray as a tool allows for indirect retrieval of the remote without requiring direct access with hands, which would be difficult due to the narrow space under the sofa. This reduces the need for multiple attempts or repositioning.",
  "safety_or_stability_consideration": "The tray provides a stable surface that can safely slide objects out from tight spaces, minimizing the risk of dropping the remote or damaging it during retrieval.",
  "uncertainty_or_missing_information": "It is unclear whether the remote control is visible in O1 or if it has already been moved. However, based on the task context and O0, we assume the remote remains under the sofa.",
  "reason": "The remote control is located in a narrow space beneath the sofa that cannot be directly accessed with hands. The tray serves as an auxiliary object to safely and efficiently retrieve the remote without requiring complex manipulation or multiple trips."
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The initial observation (O0) shows the remote under the sofa, but it may be difficult to access directly due to limited space and potential instability of the robot's posture. A tray has been identified in O1 as a possible auxiliary object that could help in retrieving the remote without requiring direct arm reach into tight spaces.",
  "plan": [
    "Move toward the area under the sofa where the remote is located.",
    "Use the mechanical arm to pick up the tray from its current position on the table.",
    "Position the tray beneath the sofa, aligning it with the space where the remote is located.",
    "Slide the tray under the sofa so that the remote can be pushed onto it.",
    "Retrieve the tray with the remote on it by using the mechanical arm to grasp and lift it."
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "Using the tray as an auxiliary object allows for indirect retrieval of the remote, reducing the need for precise manipulation in a confined space. This approach minimizes risk of dropping the remote or destabilizing the robot.",
  "safety_or_stability_consideration": "Direct arm reach into the narrow space under the sofa may compromise balance and increase the chance of collision or object drop. Using the tray provides a stable platform for transferring the remote, enhancing safety and stability during retrieval.",
  "uncertainty_or_missing_information": "The exact size and position of the remote relative to the sofa's underside are not fully clear from O0; however, the presence of the tray in O1 suggests it can be used effectively. The robot must ensure the tray is large enough to support the remote without tipping.",
  "reason": "While direct retrieval might seem simpler, the confined space under the sofa makes using a tray more efficient and safer. The tray acts as an intermediary tool to push or slide the remote onto its surface for easy pickup, avoiding risky movements."
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "The robot needs to retrieve a remote control located under the sofa. The initial observation shows the sofa and a small object underneath, but the exact nature of the object is unclear. After a short scan, the second observation confirms that the object under the sofa is indeed a remote control.",
  "plan": [
    "Move closer to the sofa to get a better view of the area beneath it.",
    "Use both hands to reach under the sofa and grasp the remote control.",
    "Lift the remote control out from under the sofa."
  ],
  "target_objects": [
    "remote control"
  ],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "no",
  "selected_helper": "none",
  "tool_use_action_chain": [],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The robot should use both hands to ensure a stable grip on the remote control and avoid dropping it during retrieval.",
  "safety_or_stability_consideration": "Ensure that the robot's movements do not cause any instability in the sofa or result in the remote control being dropped.",
  "physical_feasibility_risk": "The narrow space under the sofa may limit the robot's ability to fully extend its arms, potentially making it difficult to grasp the remote control securely.",
  "uncertainty_or_missing_information": "It is uncertain whether the remote control is easily accessible or if there are any obstacles (e.g., a blanket) that might impede retrieval.",
  "reason": "The second observation confirms the presence of the remote control under the sofa, but its exact position and potential obstructions remain unclear. The robot must proceed cautiously to avoid dropping the object or causing instability.",
  "failure_risk": "The risk of failure is moderate due to the limited space and potential for misjudging the remote's position."
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "The robot needs to retrieve a remote control located under the sofa. The initial observation shows the general area, but the exact location of the remote is not visible. After a short scan, the second observation confirms that the remote is on the floor near the right side of the sofa.",
  "plan": [
    "Move closer to the right side of the sofa to get a better view of the area under it.",
    "Use the mechanical arm to reach under the sofa and grasp the remote control.",
    "Lift the remote control out from under the sofa and move it to a safe location."
  ],
  "target_objects": [
    "remote control"
  ],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "no",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "Extend the mechanical arm towards the area under the sofa.",
    "Open the gripper and position it above the remote control.",
    "Close the gripper to grasp the remote control."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The robot should minimize movement by directly approaching the target area after confirming its location.",
  "safety_or_stability_consideration": "Ensure the robot maintains balance while extending the arm under the sofa to avoid tipping over.",
  "physical_feasibility_risk": "The remote control might be partially obstructed or difficult to grasp due to limited space under the sofa.",
  "uncertainty_or_missing_information": "The exact position and orientation of the remote control are not fully known, requiring careful manipulation.",
  "reason": "The second observation confirms the remote is on the floor near the right side of the sofa, allowing for a more precise approach. The robot must ensure stability while reaching under the furniture.",
  "failure_risk": "The gripper might fail to grasp the remote due to its small size or awkward positioning."
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "The robot needs to retrieve a remote control located under the sofa. The initial observation shows the sofa and surrounding area, but the remote is not clearly visible. After a short scan, the second observation reveals a tray-like object on a table, which may be related to the task or an intermediate step.",
  "plan": [
    "Move closer to the sofa to inspect the area underneath it for the remote control.",
    "Use a reaching motion to retrieve the remote control from under the sofa.",
    "Place the remote control on a stable surface."
  ],
  "target_objects": [
    "remote control",
    "sofa"
  ],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "no",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "Inspect the area under the sofa.",
    "Reach under the sofa to grasp the remote control.",
    "Lift the remote control out from under the sofa."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "Minimize movement by directly accessing the remote control without unnecessary detours.",
  "safety_or_stability_consideration": "Ensure stable positioning to avoid tipping or damaging objects while reaching under the sofa.",
  "physical_feasibility_risk": "The remote might be difficult to grasp due to limited visibility and space under the sofa.",
  "uncertainty_or_missing_information": "The exact location of the remote control is uncertain, and it may not be visible in the initial view.",
  "reason": "The task requires retrieving an object from a confined space. The robot must first locate the remote and then use precise movements to extract it without causing disturbance or damage.",
  "failure_risk": "Risk of failing to locate or retrieve the remote due to poor visibility or incorrect positioning."
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "The robot needs to retrieve a remote control located under the sofa. The initial observation (O0) shows the general environment, while the second observation (O1) provides a closer view of the area beneath the sofa, revealing a tray and other objects that may obstruct access.",
  "plan": [
    "Move towards the sofa to get a closer view of the area underneath it.",
    "Check if there are any obstacles, such as the tray or cloth, blocking access to the remote control.",
    "If an obstacle is present, reposition it (e.g., move the tray) to create clear access to the remote control.",
    "Reach under the sofa and retrieve the remote control."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The robot should first assess the area under the sofa for obstacles before attempting retrieval. Repositioning a small tray or cloth is more efficient than multiple trips to fetch tools.",
  "safety_or_stability_consideration": "Ensure stable movement when reaching under the sofa and avoid tipping over by maintaining balance while extending its arm.",
  "uncertainty_or_missing_information": "The exact location of the remote control under the sofa is not visible, and it may be partially hidden or obstructed by other objects.",
  "reason": "The second observation (O1) reveals a tray and cloth near the area where the remote might be located. Repositioning these items will provide clear access to the remote without requiring multiple trips or external tools."
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "The robot needs to retrieve a remote control located under the sofa. The initial observation (O0) shows the general environment, while the second observation (O1) provides a closer view of the area beneath the sofa and reveals that the remote is not directly visible but may be accessible.",
  "plan": [
    "Move closer to the sofa to get a better view of the space underneath it.",
    "Use both hands to carefully reach under the sofa, ensuring stability and avoiding knocking over any objects.",
    "Locate the remote control by feeling or visually inspecting the area beneath the sofa.",
    "Gently grasp the remote control with one hand while stabilizing the other hand if needed.",
    "Slowly pull the remote control out from under the sofa."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "Using both hands allows for better stability and precision when reaching into tight spaces, reducing the risk of dropping or misplacing objects. The plan avoids unnecessary movements by focusing directly on retrieving the remote.",
  "safety_or_stability_consideration": "The robot must ensure that its arms do not collide with the sofa legs or other obstacles while reaching under it. It should maintain balance and avoid sudden movements to prevent tipping or damaging nearby items.",
  "uncertainty_or_missing_information": "It is unclear whether the remote control is visible in O1 or if additional tools (e.g., a long-handled grabber) are needed. However, since the robot has two arms and can use them simultaneously, direct retrieval is feasible unless further constraints arise.",
  "reason": "The updated plan leverages the closer view from O1 to refine the approach, ensuring that the robot can safely and efficiently reach under the sofa without requiring multiple trips or additional tools."
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
任务：请把沙发下面的遥控器拿出来。

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
  "task_understanding": "The robot needs to retrieve a remote control located under the sofa. The initial observation shows the general environment, while the second observation provides a closer view of the area beneath the sofa, revealing a tray and other objects that may obstruct access.",
  "plan": [
    "Move closer to the sofa to get a better view of the space underneath it.",
    "Assess whether the remote control is visible or accessible from the current position.",
    "If the remote control is not directly reachable, use the tray as a tool to gently push aside any obstructing objects.",
    "Extend the mechanical arm and use the gripper to grasp the remote control securely.",
    "Lift the remote control out from under the sofa while maintaining balance."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "Using the tray as a tool reduces the need for multiple movements, allowing the robot to clear obstacles efficiently and retrieve the remote in one attempt.",
  "safety_or_stability_consideration": "The robot must maintain balance while extending its arm under the sofa. The gripper should be used carefully to avoid dropping or damaging the remote control.",
  "uncertainty_or_missing_information": "It is unclear if the remote control is visible or how tightly it is wedged under the sofa. Additionally, the exact size and shape of the remote are not specified.",
  "reason": "The second observation reveals that a tray may be obstructing access to the remote control. By using the tray as a tool to move obstacles, the robot can improve its reach and avoid unnecessary movements, making the retrieval process more efficient while ensuring stability."
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{"task_understanding": "The robot needs to retrieve a remote control located under the sofa. The image shows a living room with a sofa, and there is an object that could be a remote control visible on the floor near the sofa's base.", "plan": ["Move towards the sofa.", "Check the area underneath the sofa to locate the remote control.", "Extend the robot's arm or use a grasping mechanism to pick up the remote control from under the sofa.", "Retract the arm and move away from the sofa."], "estimated_number_of_trips": "single", "efficiency_consideration": "The robot should directly approach the sofa and perform the task in one trip to minimize movement time and energy consumption.", "safety_or_stability_consideration": "Ensure that the robot maintains stability while extending its arm under the sofa, avoiding any collisions with furniture or objects on the floor.", "uncertainty_or_missing_information": "The exact location of the remote control is not clearly visible in the image; it may require a closer inspection to confirm its position.", "reason": "The task requires retrieving an object from under the sofa. The robot must move close enough to access the area, locate the remote, and retrieve it efficiently while ensuring safety and stability during the operation."}
```

### Final Raw Response

```json
{"task_understanding": "The robot's original task is to retrieve a remote control from under the sofa. The current observation shows a different area of the room, including a countertop with various objects such as a lamp, a baking tray, and a smartphone. This location does not contain the remote control or any relevant items for the task.", "plan": ["Continue checking nearby areas to locate the sofa and the remote control under it.", "Move towards the area where the sofa is located based on prior knowledge or previous observations.", "Inspect the space beneath the sofa to find the remote control."], "estimated_number_of_trips": "multiple", "efficiency_consideration": "Since the current location does not provide any useful information for retrieving the remote control, the robot should proceed directly to the area where the sofa is located to avoid unnecessary movements.", "safety_or_stability_consideration": "Ensure that the robot navigates safely around obstacles such as furniture and electrical outlets while moving towards the sofa.", "uncertainty_or_missing_information": "The exact location of the sofa is not confirmed in this observation, so further exploration may be needed to locate it.", "reason": "The current observation does not contain any objects relevant to the task of retrieving the remote control. Therefore, the robot should continue searching for the sofa and the remote control under it by moving to the appropriate area."}
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The object appears to be small and may be partially obscured by the sofa's structure or other items on the floor.",
  "plan": [
    "Move closer to the sofa to get a better view of the area underneath it.",
    "Check if the remote control is visible and accessible from the current position.",
    "If visible, use one hand to reach under the sofa and grasp the remote control.",
    "Lift the remote control out from under the sofa carefully.",
    "Move away from the sofa with the remote control."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The plan minimizes movement by directly approaching the target area and retrieving the object in one attempt, reducing unnecessary trips.",
  "safety_or_stability_consideration": "Ensure that the robot's arms do not collide with the sofa or other objects while reaching under it. Maintain a stable posture to avoid tipping over during the retrieval process.",
  "uncertainty_or_missing_information": "The exact location and orientation of the remote control are unknown, which may require slight adjustments in hand positioning. The presence of other items (e.g., cloth) near the target area could affect accessibility.",
  "reason": "The plan is designed to efficiently locate and retrieve the remote control while ensuring safety and stability during the operation."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The task remains to retrieve the remote control from under the sofa. The new observation (O1) shows a countertop with various objects, including a baking tray, a lamp, and a smartphone, but no visible connection to the remote control or the sofa.",
  "plan": [
    "Confirm that the current location does not contain the remote control or any relevant items related to the task.",
    "Return to the area near the sofa to continue searching for the remote control under it.",
    "Check if the remote control is now visible or accessible after repositioning."
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "Since O1 does not provide any useful information about the remote control's location, returning to the original search area ensures focus on the task without unnecessary detours.",
  "safety_or_stability_consideration": "Ensure smooth navigation back to the sofa area while avoiding obstacles such as the lamp or other objects on the countertop.",
  "uncertainty_or_missing_information": "The exact position of the remote control remains unknown, and O1 does not offer any new clues. The robot must continue searching in the vicinity of the sofa.",
  "reason": "O1 is unrelated to the task, so the plan reverts to the original search strategy near the sofa, prioritizing efficiency by avoiding irrelevant areas."
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{"task_understanding": "The task is to retrieve a remote control located under the sofa. The robot has a mobile base, an arm with a gripper, and must maintain balance while moving. The remote is small and likely accessible from beneath the sofa.", "plan": ["Move the robot close to the sofa, ensuring stable positioning.", "Extend the mechanical arm under the sofa to locate the remote control.", "Use the gripper to securely grasp the remote control.", "Retract the arm and move the robot away from the sofa.", "Place the remote control on a stable surface or hold it for delivery."], "estimated_number_of_trips": "single", "efficiency_consideration": "The plan minimizes movement by directly approaching the target area, using the arm to reach under the sofa without repositioning the base unnecessarily.", "safety_or_stability_consideration": "Maintain balance during movement and ensure the arm does not cause instability when extended under the furniture.", "uncertainty_or_missing_information": "The exact location of the remote control under the sofa is unknown; visual confirmation may be needed to locate it. The size and shape of the remote are also uncertain, which could affect grip reliability.", "reason": "The robot must first approach the sofa safely, then use its arm to reach into a confined space where visibility might be limited. A single trip is sufficient if the remote is found on the first attempt; otherwise, minor repositioning may be needed without additional trips."}
```

### Final Raw Response

```json
{"task_understanding": "The original task is to retrieve a remote control from under the sofa. The new observation shows a countertop with various objects, including a baking tray, a lamp, a smartphone, and a book. None of these items are relevant to retrieving the remote control.", "plan": ["Continue searching for the remote control under the sofa as previously planned.", "If no progress is made after initial attempts, reposition the robot to check other areas near the sofa or beneath it from different angles."], "estimated_number_of_trips": "unknown", "efficiency_consideration": "The current observation does not provide useful information for completing the task. Therefore, the focus remains on efficiently locating and retrieving the remote control under the sofa.", "safety_or_stability_consideration": "Maintain balance while moving and ensure that arm movements do not cause instability when reaching into confined spaces.", "uncertainty_or_missing_information": "The exact location of the remote control is still unknown, and there is no visual confirmation from this observation. The robot may need to recheck areas around the sofa if initial attempts fail.", "reason": "Since the current observation does not contain any objects related to the task or provide new information about the remote's location, the plan remains focused on continuing the search under the sofa."}
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa.",
  "plan": [
    "Move towards the area beneath the sofa where the remote control is located.",
    "Extend the robot's arm or gripper to reach the remote control.",
    "Grasp the remote control securely.",
    "Lift the remote control out from under the sofa."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The robot should move directly to the target area and perform the retrieval in one continuous motion to minimize time and energy consumption.",
  "safety_or_stability_consideration": "Ensure that the robot maintains stability while extending its arm under the sofa, avoiding any collisions with furniture or objects on the floor.",
  "uncertainty_or_missing_information": "The exact location of the remote control under the sofa is not specified; it may require a brief search. The size and shape of the remote are unknown, which could affect grasping."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The previous observation (O0) showed the area beneath the sofa, and the current observation (O1) shows a different location with a tray, lamp, and phone on a counter.",
  "plan": [
    "Since the current observation (O1) does not show the sofa or the remote control, it is not relevant to the task. The robot should return to the area near the sofa to continue searching for the remote control."
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "The robot should prioritize returning to the original search area (near the sofa) rather than exploring unrelated locations, as this will increase efficiency in finding the remote control.",
  "safety_or_stability_consideration": "While moving between areas, the robot must ensure safe navigation and avoid obstacles such as the lamp or tray on the counter.",
  "uncertainty_or_missing_information": "The exact location of the remote control under the sofa remains uncertain. The robot may need to perform a more thorough search in that area."
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The object appears to be small and may be partially obscured by the sofa's structure or other items on the floor.",
  "plan": [
    "Move closer to the sofa to get a better view of the area underneath it.",
    "Check if the remote control is visible or accessible from the current position.",
    "If visible, use one hand to carefully reach under the sofa and grasp the remote control.",
    "Lift the remote control out from under the sofa and move it to a safe location."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The task requires minimal movement since the remote is already in close proximity. The robot should use its arms efficiently to avoid unnecessary repositioning.",
  "safety_or_stability_consideration": "Ensure that the robot maintains balance while reaching under the sofa and does not tip over due to uneven weight distribution or unstable positioning.",
  "uncertainty_or_missing_information": "The exact location of the remote control is unclear, and it may be partially hidden by other objects such as a cloth. The size and shape of the remote are also uncertain.",
  "reason": "The robot must first assess the visibility and accessibility of the remote under the sofa before attempting retrieval to ensure successful grasping without causing disturbance or instability."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The task remains to retrieve the remote control from under the sofa. The new observation (O1) shows a countertop with various objects, including a baking tray, a lamp, and a smartphone, but no visible connection to the remote or the sofa area.",
  "plan": [
    "Continue searching for the remote control under the sofa as previously planned.",
    "Since O1 does not provide any relevant information about the remote's location, do not divert attention from the original task.",
    "Check if there are other nearby areas that might contain the remote, but prioritize returning to the sofa area."
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "The robot should avoid unnecessary movements to unrelated areas. Focus on completing the primary task efficiently without getting distracted by irrelevant observations.",
  "safety_or_stability_consideration": "Maintain stability while moving between locations, especially when transitioning from the countertop area back to the sofa.",
  "uncertainty_or_missing_information": "The remote control's exact location remains unknown, and O1 does not offer any new clues. The robot must continue relying on visual inspection of the sofa area.",
  "reason": "O1 is unrelated to the task of retrieving the remote from under the sofa, so the plan should remain focused on the original objective without deviation."
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{"task_understanding": "The robot needs to retrieve a remote control located under the sofa. The remote is not visible in the image, but there is an object (possibly a toy or small item) under the sofa that may be mistaken for it. The robot must navigate to the area beneath the sofa and use its mechanical arm and gripper to extract the remote.", "plan": ["Move towards the sofa to position the robot's base close enough to reach underneath.", "Extend the mechanical arm downward into the space under the sofa, ensuring stability during movement.", "Use the gripper to locate and grasp the remote control, confirming it is securely held before lifting.", "Retract the arm and move away from the sofa to avoid obstruction or imbalance."], "estimated_number_of_trips": "single", "efficiency_consideration": "The robot should minimize unnecessary movements by directly approaching the target area and using precise arm motion to reduce time and energy consumption.", "safety_or_stability_consideration": "Maintain balance while extending the arm under the sofa; avoid sudden movements that could cause tipping or collision with furniture.", "uncertainty_or_missing_information": "The exact location of the remote control is not visible, so the robot may need to scan the area under the sofa to locate it. The size and shape of the remote are unknown, which affects grip strategy.", "reason": "The task requires careful navigation due to limited visibility under the sofa and potential instability from reaching into confined spaces. A single trip is sufficient if the remote is found immediately; otherwise, additional scanning may be needed."}
```

### Final Raw Response

```json
{"task_understanding": "The robot's original task is to retrieve a remote control from under the sofa. The current observation (O1) shows a countertop with various objects, including a baking tray, a lamp, and a smartphone, but no visible connection to the remote or the sofa. This scene does not provide any direct information about the remote's location.", "plan": ["Continue searching for the remote control by revisiting the area under the sofa as previously planned.", "If no progress is made in locating the remote after rechecking the initial area, expand the search to nearby regions such as tables or shelves where remotes are commonly placed."], "estimated_number_of_trips": "multiple", "efficiency_consideration": "Since O1 does not provide relevant information about the remote's location, the robot should prioritize returning to the original task area rather than exploring unrelated zones.", "safety_or_stability_consideration": "Ensure stable movement when transitioning between areas; avoid abrupt changes in direction that could compromise balance.", "uncertainty_or_missing_information": "The exact location of the remote remains unknown. The current observation does not confirm its presence or absence, so further investigation is required.", "reason": "O1 does not contain any useful objects for retrieving the remote control and appears unrelated to the task. Therefore, the robot should continue checking nearby areas around the sofa or other likely locations where a remote might be found."}
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The current view shows the sofa and the floor beneath it, where a small object resembling a remote control is visible.",
  "plan": [
    "Move towards the area under the sofa.",
    "Extend the arm to reach the remote control on the floor.",
    "Gently grasp the remote control.",
    "Lift the remote control out from under the sofa."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The remote is clearly visible and within immediate reach, so no additional tools or objects are needed. Direct retrieval minimizes movement and time.",
  "safety_or_stability_consideration": "The object is small and stable on the floor; there is minimal risk of dropping it during retrieval as long as the arm moves steadily.",
  "uncertainty_or_missing_information": "It cannot be definitively confirmed that the visible object is a remote control without closer inspection, but its size and shape are consistent with one. The exact location under the sofa may require slight adjustment to ensure full access.",
  "reason": "The remote control is clearly visible on the floor directly beneath the sofa, making direct retrieval straightforward and efficient. No auxiliary objects or additional searches are required as the target is already in a reachable position."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The previous observation (O0) showed the remote under the sofa, while the current observation (O1) shows a countertop with various objects, including a baking tray and a lamp.",
  "plan": [
    "Proceed to the area where the sofa is located based on prior knowledge.",
    "Move towards the space beneath the sofa.",
    "Extend the arm to reach the remote control on the floor.",
    "Gently grasp the remote control.",
    "Lift the remote control out from under the sofa."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The current observation (O1) does not contain any objects that assist in retrieving the remote control. The baking tray and lamp are unrelated to the task, so no auxiliary use is possible.",
  "safety_or_stability_consideration": "No safety concerns arise from the current observation as it does not involve handling fragile or unstable items relevant to the task.",
  "uncertainty_or_missing_information": "The remote control's exact location under the sofa may require fine adjustments, but no additional information is needed since its presence was confirmed in O0.",
  "reason": "The current observation (O1) provides no useful objects for retrieving the remote. Therefore, the plan remains unchanged: directly proceed to retrieve the remote from under the sofa without any intermediate steps or searches."
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The object is visible in the image, but it is partially obscured and may be difficult to reach directly due to the low clearance.",
  "plan": [
    "Check if there are any tools or objects nearby that can assist in retrieving the remote (e.g., a long stick or a grabber tool).",
    "If no suitable tool is available, use one hand to stabilize the sofa while using the other hand to reach under it and retrieve the remote.",
    "Ensure both hands are used safely to avoid dropping the remote or causing instability."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "Using a tool would increase efficiency by reducing the need for precise hand movements. However, since no tools are visible in the immediate vicinity, direct retrieval is necessary.",
  "safety_or_stability_consideration": "The sofa may shift if too much force is applied. Stabilizing it with one hand while retrieving the remote with the other ensures safety and prevents accidental tipping.",
  "uncertainty_or_missing_information": "It is unclear whether a tool is available nearby, but none are visible in the current view. The exact position of the remote under the sofa may also affect reachability.",
  "reason": "The remote is clearly visible under the sofa, so direct retrieval is feasible. No auxiliary objects are present to assist, and short-range searching for tools would not significantly improve efficiency given the proximity of the target."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The previous observation (O0) showed the remote partially visible under the sofa, while the current observation (O1) shows a different scene with a countertop, lamp, and tray. This indicates that the robot has moved to a new location, possibly after completing or pausing the task.",
  "plan": [
    "Since the current view does not show the sofa or the remote control, check nearby areas for the sofa or any objects that might help retrieve the remote.",
    "If the sofa is within reach in an adjacent area, proceed to retrieve the remote directly using both hands to ensure stability and safety.",
    "If no immediate access to the sofa is available, continue searching nearby regions (e.g., under furniture, on tables) for the remote control."
  ],
  "estimated_number_of_trips": "unknown",
  "efficiency_consideration": "The current scene does not provide any tools or objects that can assist in retrieving the remote. Therefore, efficiency depends on locating the sofa and accessing it directly.",
  "safety_or_stability_consideration": "Direct retrieval under the sofa requires careful movement to avoid knocking over furniture or dropping the remote. Stabilizing actions may be necessary if the sofa is unstable.",
  "uncertainty_or_missing_information": "The exact location of the sofa relative to the current position is unknown, and it is unclear whether the remote has been moved or remains in place.",
  "reason": "The current observation (O1) does not contain any objects relevant to retrieving the remote under the sofa. Therefore, the robot must continue searching nearby areas for the sofa or use indirect methods if necessary."
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The remote is not visible in the current image, but there is a small object (possibly the remote) on the floor near the sofa's base. The robot must navigate to the area under the sofa and extract the remote.",
  "plan": [
    "Move closer to the sofa to inspect the space beneath it for the remote control.",
    "If the remote is visible, use the mechanical arm to grasp it with the gripper.",
    "Lift the remote out from under the sofa and move it to a safe location."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The task can be completed in one trip since the remote is likely within reach of the robot's arm without requiring additional tools or objects.",
  "safety_or_stability_consideration": "The robot must maintain balance while extending its arm under the sofa. The gripper should securely grasp the remote to prevent dropping it during retrieval.",
  "uncertainty_or_missing_information": "The exact location and visibility of the remote control are uncertain, as it is not clearly visible in the image. It may be partially hidden or require repositioning of nearby objects (e.g., a cloth) for access.",
  "reason": "Direct operation is feasible because the remote appears to be within reach under the sofa, and no auxiliary tools are needed. The robot can use its mechanical arm to retrieve it without requiring additional items or multiple trips."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The previous observation (O0) showed a small object near the sofa's base, possibly the remote. The current observation (O1) shows a countertop with various objects, including a baking tray, a lamp, and a smartphone, but no direct connection to the sofa or the remote.",
  "plan": [
    "The current observation does not provide any useful auxiliary object for retrieving the remote from under the sofa.",
    "Return to the area near the sofa to continue searching for the remote control under it."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "Since no helpful objects are present in the current observation, there is no efficiency gain by using them. The task must be completed directly at the original location.",
  "safety_or_stability_consideration": "The robot should maintain balance while moving back to the sofa area and ensure stable arm movement when retrieving the remote from under it.",
  "uncertainty_or_missing_information": "It is still unclear whether the small object near the sofa in O0 is the remote control. The exact location of the remote remains uncertain, requiring further inspection.",
  "reason": "The current observation does not contain any objects that can assist with retrieving the remote from under the sofa. Therefore, no auxiliary actions are needed, and the robot should return to the original task area to continue searching."
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The image shows a small colorful object, likely the remote, on the floor beneath the sofa. There are no visible obstacles or tools that could assist in this retrieval.",
  "plan": [
    "Move towards the area under the sofa where the remote control is located.",
    "Extend the robot's arm and grasp the remote control from the floor.",
    "Lift the remote control out from under the sofa."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The remote control is directly accessible, so no additional tools or steps are needed. The task can be completed in one trip without requiring intermediate actions.",
  "safety_or_stability_consideration": "No safety risks are apparent as the object is small and stable on the floor. No complex movements are required to avoid tipping or dropping objects.",
  "uncertainty_or_missing_information": "The exact location of the remote control under the sofa cannot be confirmed from the image, but its presence is indicated by a visible object in that area.",
  "reason": "Direct access to the remote control allows for immediate retrieval without requiring auxiliary tools. The task does not involve fragile or heavy objects, nor does it require navigating complex environments."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The previous observation (O0) showed the remote under the sofa, while the current observation (O1) shows a countertop with various objects but no direct connection to the remote or the sofa.",
  "plan": [
    "Confirm that the remote control has not been moved from its original location under the sofa.",
    "Return to the area near the sofa and proceed to retrieve the remote control."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The current observation does not provide any useful objects or tools for retrieving the remote. The task remains unchanged, so no additional steps are needed.",
  "safety_or_stability_consideration": "No safety concerns arise from the current observation as it is unrelated to the retrieval process.",
  "uncertainty_or_missing_information": "The location of the remote control under the sofa cannot be confirmed without revisiting that area. The current observation does not provide any new information about its status or position.",
  "reason": "Since the current observation (O1) does not contain any objects relevant to retrieving the remote, it is necessary to return to the original task location. No auxiliary tools are available in this scene, so direct retrieval remains the only option."
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "目标是取出位于沙发下方的遥控器。从图像中可见，遥控器位于沙发底部前方的地面上，处于一个相对开阔的空间内，没有被其他物体明显阻挡。",
  "plan": [
    "移动到沙发前，确保双手可以伸入沙发下方。",
    "使用右手或左手直接抓取地上的遥控器。",
    "将遥控器从沙发下取出并移至安全位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "无需额外辅助物体，直接操作即可完成任务，效率高。",
  "safety_or_stability_consideration": "遥控器为单个稳定小物体，无掉落或滑动风险，直接抓取安全可靠。",
  "uncertainty_or_missing_information": "图像中未显示遥控器的具体位置是否完全在手臂可及范围内，但根据其外观和位置判断，应在可达范围之内。",
  "reason": "目标物（遥控器）为单个、稳定的小物体，且位于沙发下方的开阔区域，无需借助辅助工具即可直接抓取。因此选择直接操作，既高效又安全。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "目标是取出沙发下的遥控器，但当前观察 O1 显示的是一个不同的场景（桌面区域），与原始任务无关。",
  "plan": [
    "忽略当前观察 O1 中的物体，因为它们不涉及沙发或遥控器。",
    "返回原任务环境，继续执行从沙发下取出遥控器的任务。"
  ],
  "estimated_number_of_trips": "unknown",
  "efficiency_consideration": "O1 中无对任务有用的辅助物体，无法提升效率。",
  "safety_or_stability_consideration": "当前观察未提供任何影响安全或稳定性的信息。",
  "uncertainty_or_missing_information": "不确定 O0 和 O1 是否属于同一空间，需确认机器人是否已移动位置。",
  "reason": "O1 所示场景与原始任务无关，无可用辅助物体。因此继续执行原计划，并可能需要检查附近区域以确认当前位置和目标物的相对关系。"
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The remote is not visible, but its location is inferred from the context of the image and the task description.",
  "plan": [
    "Move toward the sofa to approach the area beneath it.",
    "Extend the mechanical arm to reach under the sofa where the remote is located.",
    "Use the gripper to grasp the remote control securely.",
    "Lift the remote out from under the sofa and retract the arm."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The task can be completed in one trip since the remote is directly accessible under the sofa without requiring additional tools or objects.",
  "safety_or_stability_consideration": "The remote control is small and likely stable, so direct retrieval with the gripper poses no risk of dropping or instability.",
  "uncertainty_or_missing_information": "The exact position of the remote under the sofa is not visible in the image, but its location is assumed to be within reach of the mechanical arm. No auxiliary objects are present that could assist in retrieving it.",
  "reason": "Direct retrieval is feasible because the remote control is small and likely accessible without needing additional tools or assistance. The environment appears clear enough for safe manipulation."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The task remains to retrieve a remote control located under the sofa. The previous observation (O0) showed the remote's location beneath the sofa, and this new observation (O1) shows a countertop with various objects but no direct relevance to the remote or its retrieval.",
  "plan": [
    "Proceed to the area under the sofa as previously planned.",
    "Use the mechanical arm to reach under the sofa and retrieve the remote control."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The current observation (O1) does not provide any objects or tools that can assist in retrieving the remote. Therefore, no changes are needed to the original plan.",
  "safety_or_stability_consideration": "No new safety concerns arise from O1; the retrieval process remains stable and straightforward.",
  "uncertainty_or_missing_information": "The exact position of the remote under the sofa is still uncertain due to limited visibility. However, no additional information from O1 helps resolve this uncertainty.",
  "reason": "O1 does not contain any objects that can assist in retrieving the remote control. The original plan remains valid as it directly addresses the task without requiring auxiliary tools or actions."
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{"task_understanding": "The robot needs to retrieve a remote control located under the sofa. The object is visible and appears to be within reach, but the space is narrow and may require careful maneuvering.", "plan": ["Move towards the sofa.", "Extend one arm under the sofa to locate the remote control.", "Use both hands to grasp and extract the remote control from under the sofa."], "target_objects": ["remote control"], "helper_needed": "no", "helper_purpose": "none", "visible_helper_detected": "no", "visible_helper_objects": [], "search_for_helper_if_none_visible": "no", "selected_helper": "none", "tool_use_action_chain": [], "estimated_number_of_trips": "single", "efficiency_consideration": "The remote control is visible and close to the edge of the sofa, so a single attempt should suffice.", "safety_or_stability_consideration": "Ensure that the robot's movements do not cause it to lose balance or damage the furniture.", "physical_feasibility_risk": "The narrow space under the sofa may limit arm movement, but the object is within reach and stable.", "uncertainty_or_missing_information": "It is unclear if the remote control is fully accessible without obstruction from other objects.", "reason": "The remote control appears to be a single, small object that can be grasped with one hand. The robot's arms are capable of reaching under the sofa, but careful positioning may be required due to limited space.", "failure_risk": "Low risk if the robot successfully extends its arm and locates the remote; higher risk if the remote is obstructed or the robot misjudges the position."}
```

### Final Raw Response

```json
{"task_understanding": "The robot's original task is to retrieve a remote control from under the sofa. The new observation shows a different scene, likely a kitchen or desk area, with no visible connection to the sofa or the remote control.", "plan": ["Continue searching for the sofa and the remote control as per the original plan.", "Check if the remote control might have been moved to this location by verifying nearby objects.", "If the remote is not found here, return to the previous area under the sofa."], "target_objects": ["remote control"], "helper_needed": "no", "helper_purpose": "none", "visible_helper_detected": "no", "visible_helper_objects": [], "search_for_helper_if_none_visible": "no", "selected_helper": "none", "tool_use_action_chain": [], "estimated_number_of_trips": "unknown", "efficiency_consideration": "The robot should prioritize returning to the original location under the sofa where the remote was last seen.", "safety_or_stability_consideration": "Ensure that movements do not cause any objects on the counter to fall or create hazards.", "physical_feasibility_risk": "No significant risk, as this area is open and accessible.", "uncertainty_or_missing_information": "It is unclear if the remote control has been moved; further verification is needed.", "reason": "The current observation does not show any relevant objects related to the task. The robot must continue its search based on prior knowledge of the remote's location.", "failure_risk": "Low risk, but potential for delay if the robot spends time checking irrelevant areas."}
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "The robot needs to retrieve a remote control located under the sofa. The object is small and likely accessible, but the space beneath the sofa may be narrow or obstructed.",
  "plan": [
    "Move towards the sofa to approach the area underneath it.",
    "Extend the mechanical arm to reach under the sofa and locate the remote control.",
    "Use the gripper to pick up the remote control carefully.",
    "Retract the arm and move away from the sofa."
  ],
  "target_objects": [
    "remote control"
  ],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "no",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "Extend mechanical arm towards the space under the sofa.",
    "Use gripper to grasp the remote control.",
    "Lift and retract the arm."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The robot should move directly to the target area without unnecessary detours to minimize time and energy usage.",
  "safety_or_stability_consideration": "Ensure the robot maintains balance while extending its arm under the sofa, avoiding any tipping or collision with furniture.",
  "physical_feasibility_risk": "The remote control might be difficult to locate due to limited visibility or obstructed access; however, the object is small and likely within reach of the gripper.",
  "uncertainty_or_missing_information": "It is uncertain whether the remote control is visible or if there are obstacles blocking direct access under the sofa.",
  "reason": "The robot has a mechanical arm and gripper capable of reaching into tight spaces. The task does not require additional tools or assistance, but careful movement is needed to avoid instability.",
  "failure_risk": "Failure could occur if the remote control is out of reach due to obstruction or if the robot loses balance during the operation."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The robot's original task is to retrieve a remote control from under the sofa. The current observation shows a countertop with various objects, including a baking tray, lamp, smartphone, and book. This area does not contain the remote control or any relevant items for the task.",
  "plan": [
    "Continue searching for the remote control by moving back to the area near the sofa.",
    "Check under the sofa again if necessary, ensuring the robot maintains balance while extending its arm."
  ],
  "target_objects": [
    "remote control"
  ],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "no",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "Move back to the sofa area.",
    "Extend mechanical arm under the sofa to locate and retrieve the remote control."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The robot should return directly to the original task location without deviating, as no relevant objects are present in the current observation.",
  "safety_or_stability_consideration": "Maintain balance while moving and extending the arm under the sofa; avoid collisions with furniture or other objects.",
  "physical_feasibility_risk": "The remote control may still be hidden under the sofa, requiring careful manipulation to retrieve it without causing instability.",
  "uncertainty_or_missing_information": "It is unclear whether the remote control has been moved or if there are any changes in its location since the last observation.",
  "reason": "The current observation does not provide useful information for retrieving the remote control. The robot must return to the original task area to continue the search.",
  "failure_risk": "Failure could occur if the robot fails to locate the remote control due to misjudgment of its position or obstruction."
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{"task_understanding": "The robot needs to retrieve a remote control located under the sofa. The object is not clearly visible, but there is a small colorful cube-like item under the sofa that might be the remote or related to it.", "plan": ["Move towards the sofa.", "Crawl or lower the body to inspect underneath the sofa.", "Locate the remote control under the sofa.", "Retrieve the remote control from under the sofa."], "target_objects": ["remote control"], "helper_needed": "no", "helper_purpose": "none", "visible_helper_detected": "no", "visible_helper_objects": [], "search_for_helper_if_none_visible": "no", "selected_helper": "none", "tool_use_action_chain": [], "estimated_number_of_trips": "single", "efficiency_consideration": "Minimize movement by directly accessing the area under the sofa.", "safety_or_stability_consideration": "Ensure stable positioning while lowering to avoid tipping or collision with furniture.", "physical_feasibility_risk": "Low risk, as the task involves standard mobility and manipulation within a clear space.", "uncertainty_or_missing_information": "The exact location of the remote control is unknown; it may be partially hidden under the sofa.", "reason": "The robot must navigate to the sofa and inspect underneath it to locate the remote control. The absence of visible obstacles or hazards suggests a straightforward retrieval process.", "failure_risk": "Low risk, as long as the robot can successfully lower itself and detect the object."}
```

### Final Raw Response

```json
{"task_understanding": "The robot's original task is to retrieve a remote control from under the sofa. The current observation shows a countertop with various objects, including a baking tray, a lamp, and a smartphone. This location does not appear to be near the sofa or relevant to the task.", "plan": ["Continue searching for the sofa in the surrounding area.", "Check nearby regions for the sofa and any objects underneath it.", "Once the sofa is located, proceed with retrieving the remote control from under it."], "target_objects": ["remote control"], "helper_needed": "no", "helper_purpose": "none", "visible_helper_detected": "no", "visible_helper_objects": [], "search_for_helper_if_none_visible": "yes", "selected_helper": "none", "tool_use_action_chain": [], "estimated_number_of_trips": "unknown", "efficiency_consideration": "Prioritize checking areas near the sofa to avoid unnecessary movement.", "safety_or_stability_consideration": "Ensure stable navigation while searching for the sofa.", "physical_feasibility_risk": "Low risk, as the environment appears clear and accessible.", "uncertainty_or_missing_information": "The exact location of the sofa is unknown; further exploration is needed.", "reason": "The current observation does not provide any relevant information about the remote control or the sofa. Therefore, the robot should continue searching for the sofa in nearby areas.", "failure_risk": "Low risk if the robot continues to search systematically."}
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The image shows a living room with a sofa, and there appears to be an object (possibly the remote) on the floor near the front of the sofa.",
  "plan": [
    "Move towards the area beneath the sofa where the remote control is located.",
    "Extend the robot's arm or gripper to reach under the sofa.",
    "Grasp the remote control carefully without disturbing other objects.",
    "Lift the remote control out from under the sofa."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The task requires only one trip as the remote is directly accessible under the sofa. No additional tools or helpers are needed since the robot can reach it with its arm.",
  "safety_or_stability_consideration": "Ensure that the robot maintains stability while extending its arm under the sofa to avoid tipping over. Avoid knocking over any nearby objects like the cloth on the floor.",
  "uncertainty_or_missing_information": "The exact location and orientation of the remote control are not clearly visible, so precise positioning may require slight adjustments during retrieval.",
  "reason": "The robot can directly access the remote under the sofa without needing additional tools or assistance. The environment appears clear enough to allow safe movement and grasping."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The previous observation (O0) showed the remote near the front of the sofa, while the current observation (O1) shows a different area with a countertop, lamp, and tray.",
  "plan": [
    "Confirm that the current location does not contain the remote control.",
    "Return to the original area under the sofa where the remote was previously observed.",
    "Proceed to retrieve the remote control from beneath the sofa."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The new observation (O1) does not contain any objects relevant to retrieving the remote. Therefore, it is more efficient to return directly to the original location rather than exploring further.",
  "safety_or_stability_consideration": "No safety concerns are introduced in the current area; however, the robot should maintain awareness of its surroundings when moving back to the sofa area.",
  "uncertainty_or_missing_information": "The exact position of the remote control is uncertain due to limited visibility. The robot may need to adjust its approach upon returning to the sofa.",
  "reason": "Since O1 does not provide any useful information or tools for retrieving the remote, the robot should disregard this area and return to the original location under the sofa."
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The object appears small and may be difficult to reach due to limited visibility and space.",
  "plan": [
    "Move closer to the sofa to get a better view of the area underneath it.",
    "Use one hand to carefully probe under the sofa to locate the remote control.",
    "Once located, use both hands if necessary to grasp and extract the remote control safely."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "Using both hands allows for better stability and precision when retrieving an object from a confined space. No additional tools are needed as the task can be completed with direct manipulation.",
  "safety_or_stability_consideration": "Ensure that movements are slow and controlled to avoid knocking over nearby objects or damaging the sofa. Avoid applying excessive force under the sofa.",
  "uncertainty_or_missing_information": "The exact position of the remote control is not visible, so initial probing may be required. The size and shape of the remote control are unknown but assumed to fit within a single hand's grasp.",
  "reason": "Direct retrieval using both hands provides better control and reduces the risk of dropping or losing the object in the confined space under the sofa."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The task remains to retrieve a remote control from under the sofa. The current observation shows a countertop with various objects, but no direct connection to the sofa or the remote's location.",
  "plan": [
    "Continue searching for the remote control under the sofa as previously planned.",
    "Check if any nearby objects (e.g., tray, lamp) can be used to assist in retrieving the remote, but none appear relevant.",
    "Proceed with direct manipulation using both hands to locate and extract the remote from under the sofa."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "No new tools or objects are available that would improve efficiency for this task. The original plan remains optimal.",
  "safety_or_stability_consideration": "The current environment does not introduce additional hazards, so the safety considerations remain unchanged.",
  "uncertainty_or_missing_information": "The remote control's exact location under the sofa is still unknown, and no new information from O1 helps locate it.",
  "reason": "O1 does not provide any useful objects or insights for retrieving the remote. The task must proceed as originally planned since the relevant area (under the sofa) has not been fully explored."
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "从沙发下方取出遥控器。",
  "plan": [
    "移动到沙发前方，确保身体平衡并保持稳定姿态。",
    "检查沙发下方空间，确认遥控器的位置和可接近性。",
    "使用机械臂伸入沙发下方，调整夹爪角度以对准遥控器。",
    "用夹爪小心抓取遥控器，确保其被牢固握持且不会掉落。",
    "将遥控器从沙发下平稳取出并移至安全位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接使用机械臂操作是最高效的方式，无需额外工具或辅助物。",
  "safety_or_stability_consideration": "移动时保持身体平衡，避免因重心不稳导致倾倒；夹爪抓取动作需轻柔以防止遥控器损坏或掉落。",
  "uncertainty_or_missing_information": "无法确认沙发下方是否有障碍物影响机械臂伸入，但根据图像判断空间足够。",
  "reason": "基于当前环境和机器人能力，直接操作是最佳选择。无需借助辅助工具，且单次移动即可完成任务，效率高、风险低。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "从沙发下方取出遥控器。",
  "plan": [
    "确认当前环境未提供与原始任务相关的有用辅助物，因此不改变原计划。",
    "继续检查周围区域以确保无其他潜在障碍或工具可提升效率。",
    "保持移动至沙发前方的路径清晰，并准备执行机械臂操作。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "当前观察未提供可用辅助物，原计划已是最优方案，无需调整。",
  "safety_or_stability_consideration": "保持身体平衡和稳定姿态是首要任务，避免因环境变化导致操作风险增加。",
  "uncertainty_or_missing_information": "无法确认沙发下方是否有新障碍物，需在接近时进一步检查。",
  "reason": "O1 中未发现对取出遥控器有帮助的物体或工具，因此继续执行原计划。当前观察区域与任务无关，无需调整策略。"
}
```

