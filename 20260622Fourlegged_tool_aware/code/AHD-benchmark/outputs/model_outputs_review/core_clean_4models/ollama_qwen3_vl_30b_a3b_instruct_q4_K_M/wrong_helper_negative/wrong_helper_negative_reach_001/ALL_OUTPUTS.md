# wrong_helper_negative_reach_001: All Candidate Outputs

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
  "task_understanding": "The robot needs to retrieve a remote control located under the sofa. The initial observation shows a bedroom with a bed and a remote on the floor, but no visible sofa. After a short scan, the second observation reveals a living area with a sofa and a cup on a table, indicating that the robot has moved or scanned to a different location where the sofa is present.",
  "plan": [
    "Move to the living area where the sofa is located.",
    "Check under the sofa for the remote control.",
    "Retrieve the remote control from under the sofa."
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "The robot should move directly to the living area and perform a thorough search under the sofa in one trip to minimize unnecessary movements.",
  "safety_or_stability_consideration": "Ensure stable movement when reaching under the sofa to avoid tipping or collision with furniture.",
  "uncertainty_or_missing_information": "It is unclear if the remote control is visible or fully accessible under the sofa, and whether there are obstacles that might impede retrieval.",
  "reason": "The initial observation does not show a sofa, but the second observation confirms its presence in a different area. Therefore, the robot must reorient to the correct location before attempting to retrieve the remote."
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
    "检查沙发下方区域以确认遥控器的位置和可接近性",
    "使用右手或左手（选择更方便的一侧）伸入沙发下方，抓取遥控器",
    "平稳地将遥控器从沙发下抽出",
    "确保在移动过程中不碰倒其他物品"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "优先使用单次动作完成任务，避免不必要的往返。",
  "safety_or_stability_consideration": "保持身体平衡，避免因伸展过远导致不稳定；确保抓取牢固，防止遥控器掉落或损坏。",
  "uncertainty_or_missing_information": "无法确定沙发下方是否有障碍物或其他物品阻碍取出遥控器。",
  "reason": "根据观察O0和O1，机器人需要确认遥控器的具体位置，并评估是否可以直接取出。由于任务要求高效完成，应尽量减少移动次数并确保操作安全。"
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
    "移动到沙发附近，检查沙发下方空间是否可见且可接近",
    "如果可见且无障碍，使用机械臂伸入沙发下方，夹取遥控器并平稳取出",
    "确认遥控器已成功抓取后，将机器人移至目标位置"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "优先选择最短路径接近目标区域，并在首次尝试中完成任务以减少移动次数。",
  "safety_or_stability_consideration": "保持底盘平衡，避免因机械臂伸展过远导致重心偏移；夹爪动作需平稳，防止遥控器掉落或损坏。",
  "uncertainty_or_missing_information": "无法确认沙发下方是否有障碍物遮挡遥控器，也无法确定遥控器是否被其他物体覆盖。",
  "reason": "基于观察O0和O1，机器人需要先评估环境并判断操作可行性。由于任务目标明确且空间相对开放，计划应聚焦于高效、安全地完成单次取物任务。"
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
    "Move towards the sofa area.",
    "Inspect the space underneath the sofa to locate the remote control.",
    "Extend the robotic arm and grasp the remote control.",
    "Lift the remote control out from under the sofa."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The robot should move directly to the sofa area without unnecessary detours, as the task is straightforward and requires only one trip.",
  "safety_or_stability_consideration": "Ensure the robotic arm moves smoothly and avoids any sudden movements that could disturb objects or cause instability in the environment.",
  "uncertainty_or_missing_information": "The exact position of the remote control under the sofa is not visible, so a careful inspection may be needed to locate it accurately.",
  "reason": "Based on the initial observation (O0), the robot identified the need to retrieve an object from under the bed. After a short re-evaluation (O1), the task remains consistent: retrieving a remote control from beneath a piece of furniture. The plan is updated to reflect the correct location and ensure efficient execution."
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
    "检查沙发下方区域以确认遥控器的位置和可接近性",
    "使用右手或左手（选择更合适的一侧）伸入沙发下方，抓取遥控器",
    "平稳地将遥控器从沙发下抽出并移至安全位置"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "优先使用单次动作完成任务以减少移动次数和时间",
  "safety_or_stability_consideration": "确保在抓取过程中不触碰或扰动沙发或其他家具，避免造成不稳定或掉落物品",
  "uncertainty_or_missing_information": "无法确认遥控器是否被其他物体遮挡或卡住，需谨慎操作以防止损坏设备或自身部件",
  "reason": "根据观察O0和O1，机器人需要先定位遥控器并评估其可接近性。由于沙发下方空间有限且可能存在障碍物，计划中强调了检查与谨慎抓取的步骤，确保任务安全高效完成。"
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
  "task_understanding": "从沙发下方取出遥控器",
  "plan": [
    "移动到床边，检查床下空间以确认目标物体位置",
    "使用机械臂伸入床下，定位并夹取遥控器",
    "缓慢收回机械臂，确保携带稳定",
    "移动至指定放置区域，释放遥控器"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "优先选择最短路径接近目标，并在一次操作中完成任务以减少能耗和时间。",
  "safety_or_stability_consideration": "保持移动底盘平衡，避免因机械臂伸展过远导致倾倒；夹取时确保遥控器被牢固抓握以防掉落。",
  "uncertainty_or_missing_information": "无法确认沙发的具体位置及遥控器是否被遮挡或卡住，需在接近后进一步判断。",
  "reason": "根据观察O0和O1，机器人最初看到的是床下场景而非沙发，说明任务描述中的‘沙发’可能为误述；结合实际视觉信息，应以床下为目标区域执行操作。"
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
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The image shows a bedroom with a bed, but no visible sofa or remote control in the scene.",
  "plan": [
    "Move to the area where the sofa is located.",
    "Check underneath the sofa for the remote control.",
    "Pick up the remote control from under the sofa."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The robot should move directly to the sofa and perform the task in one trip to minimize time and energy usage.",
  "safety_or_stability_consideration": "Ensure stable movement when reaching under the sofa to avoid tipping or collision with furniture.",
  "uncertainty_or_missing_information": "The exact location of the sofa is not visible in the provided image, so the robot must rely on prior knowledge or additional sensory input to locate it.",
  "reason": "The task requires retrieving an object from a specific location (under the sofa), and since no other objects are mentioned, the focus is on locating and accessing the remote control efficiently while ensuring safety during movement."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The previous observation (O0) showed a bedroom with a bed and some objects on the floor, but no clear view of a sofa or remote control. The current observation (O1) shows a different part of the room with a table, window, and bed, but still no visible sofa or remote control.",
  "plan": [
    "Continue searching for the sofa in the surrounding area since it is not visible in the current observation.",
    "Check under any furniture that might be similar to a sofa, such as a bench or low seating area.",
    "If the remote control is found under any object, pick it up."
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "Since the sofa and remote control are not visible in either observation, the robot should systematically search nearby areas to locate them efficiently.",
  "safety_or_stability_consideration": "Ensure stable movement while searching under furniture to avoid tipping or damaging objects.",
  "uncertainty_or_missing_information": "The exact location of the sofa remains unknown, and no useful objects related to the task are visible in the current observation.",
  "reason": "The current observation does not provide any new information about the remote control or the sofa. Therefore, the robot should continue searching nearby areas to locate the object."
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The image shows a bed, not a sofa, so there may be a mismatch between the described object and the visual context.",
  "plan": [
    "Move towards the area where the sofa is located.",
    "Check if the remote control is visible or accessible under the sofa.",
    "If visible, use both hands to carefully retrieve the remote control from under the sofa.",
    "Ensure the remote control is securely held before moving it."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The plan minimizes trips by directly accessing the remote control in one go and using both arms for a stable grip if needed.",
  "safety_or_stability_consideration": "Ensure that the movement does not disturb any other objects under the sofa, and maintain balance while reaching underneath.",
  "uncertainty_or_missing_information": "The image shows a bed instead of a sofa, so it is unclear where the actual sofa is located or if the remote control is indeed under it. The presence of a remote control on the floor near the bed suggests it might not be under a sofa at all.",
  "reason": "The task assumes the remote control is under a sofa, but the image shows a bed with a remote on the floor nearby. This discrepancy makes it uncertain whether the remote is actually under a sofa or just on the floor. The plan proceeds based on the assumption that the remote is under a sofa, but this may need verification."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control from under the sofa. The previous observation (O0) showed a remote on the floor near a bed, while the current observation (O1) shows a different area with a table and no visible sofa or remote.",
  "plan": [
    "Since the current observation does not show a sofa or a remote control, continue checking nearby areas for the sofa and the remote control.",
    "Move to the area near the bed where the remote was previously seen under the bed frame.",
    "Check if the remote is still present in that location or has been moved."
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "The plan avoids unnecessary movements by prioritizing areas where the remote was last observed, reducing the number of trips needed to locate it.",
  "safety_or_stability_consideration": "Ensure stable movement while navigating between rooms and avoid bumping into furniture during the search.",
  "uncertainty_or_missing_information": "It is unclear whether the sofa is in this room or if the remote control has been moved. The current observation does not provide useful information about the remote's location.",
  "reason": "The current observation (O1) does not show a sofa or a remote, so it is necessary to continue searching nearby areas where the remote was previously seen under the bed frame."
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
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The robot has a mobile base, an arm with a gripper, and must maintain balance while moving. The remote is not visible in the image but is assumed to be accessible under the sofa.",
  "plan": [
    "Move towards the sofa area from the current position.",
    "Position the robot so that the mechanical arm can reach under the sofa.",
    "Extend the arm and use the gripper to grasp the remote control.",
    "Lift the remote control out from under the sofa.",
    "Retract the arm and move away from the sofa."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The robot should minimize unnecessary movements by directly approaching the target area and using precise arm positioning to avoid multiple attempts at grasping.",
  "safety_or_stability_consideration": "Maintain balance during movement, especially when extending the arm under the sofa. Avoid sudden motions that could destabilize the robot.",
  "uncertainty_or_missing_information": "The exact location of the remote control under the sofa is not visible; it may be partially obscured or require slight adjustments to access.",
  "reason": "The task requires a single trip as the remote is likely within reach, and the robot can perform all necessary actions in one sequence without needing additional items or repositioning."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The previous observation (O0) showed the remote under the bed, but this new observation (O1) shows a different room layout with no visible sofa or remote. This suggests the robot may have moved or the target location has changed.",
  "plan": [
    "Verify if the current room contains a sofa by scanning the area around the table and near the bed.",
    "If a sofa is found, proceed to check under it for the remote control using the mechanical arm.",
    "If no sofa is visible in the vicinity, continue searching nearby areas or re-evaluate the task location based on prior knowledge."
  ],
  "estimated_number_of_trips": "unknown",
  "efficiency_consideration": "The robot should prioritize checking areas near the current position before moving to new zones to avoid unnecessary travel.",
  "safety_or_stability_consideration": "Maintain balance while scanning and extending the arm, especially in a dimly lit environment with potential obstacles.",
  "uncertainty_or_missing_information": "The remote's location is uncertain due to conflicting observations; it may have been moved or the robot may be in a different room.",
  "reason": "The new observation does not confirm the presence of a sofa or remote, so further exploration is needed. The plan must adapt to potential environmental changes while ensuring safety and efficiency."
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "The robot needs to retrieve a remote control located under the sofa. The image shows a bedroom with a bed, but no visible sofa or remote control in the immediate view.",
  "plan": [
    "Move towards the area where the sofa is located.",
    "Check underneath the sofa to locate the remote control.",
    "Retrieve the remote control from under the sofa."
  ],
  "estimated_number_of_trips": "unknown",
  "efficiency_consideration": "The robot should move directly to the sofa and use its sensors to locate the remote control efficiently without unnecessary movements.",
  "safety_or_stability_consideration": "Ensure that the robot does not bump into furniture or cause any disturbance while retrieving the remote control.",
  "uncertainty_or_missing_information": "The exact location of the sofa is not visible in the current image, and it is unclear if there are obstacles around the sofa.",
  "reason": "The task requires locating and retrieving a remote control from under a sofa. The robot must navigate to the correct area, which may require additional exploration due to missing visual information about the sofa's location."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The robot needs to retrieve a remote control located under the sofa. The previous observation (O0) showed a bed and some objects on the floor, but no clear view of a sofa. The current observation (O1) shows a different part of the room with a table, window, and bed, but still no visible sofa or remote control.",
  "plan": [
    "Continue searching for the sofa in the surrounding area since it is not visible in the current observation.",
    "Check under furniture such as tables or beds if necessary, though these are less likely to have a remote control underneath.",
    "Move to another section of the room to locate the sofa and retrieve the remote control."
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "The robot should systematically scan different areas of the room to find the sofa, prioritizing locations where a sofa is likely to be placed.",
  "safety_or_stability_consideration": "Ensure that the robot avoids obstacles and does not disturb any objects while searching for the sofa.",
  "uncertainty_or_missing_information": "The exact location of the sofa remains unknown, and it may be in another part of the room not currently visible.",
  "reason": "Since neither observation shows a clear view of the sofa or remote control, the robot must continue exploring other areas to locate the sofa and complete the task."
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
  "task_understanding": "The task is to retrieve a remote control located under the sofa. The image shows a bed, not a sofa, so there may be a mismatch between the described object and the visual context.",
  "plan": [
    "Move towards the area beneath the furniture where the remote control is believed to be located.",
    "Use one hand to reach into the space under the furniture and grasp the remote control.",
    "Lift the remote control out of the space and bring it back to a stable position."
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "The task requires only one trip since the remote is likely within reach and no additional objects need to be moved.",
  "safety_or_stability_consideration": "Ensure that the movement does not disturb any other items under the furniture, which could cause instability or damage.",
  "uncertainty_or_missing_information": "The image shows a bed instead of a sofa, so it is unclear if the remote control is actually under a sofa. The exact location and accessibility of the remote are uncertain based on the visual context.",
  "reason": "The task assumes the presence of a sofa with a remote underneath, but the image depicts a bed. This discrepancy makes it difficult to confirm the actual setup, potentially affecting the ability to locate and retrieve the remote."
}
```

### Final Raw Response

```json
{
  "task_understanding": "The task is to retrieve a remote control from under the sofa. The previous observation (O0) showed a bed with a remote under it, but this new observation (O1) shows a different room setup with no visible sofa or remote.",
  "plan": [
    "Since the current observation does not show a sofa or any remote control, continue to check nearby areas for the presence of a sofa and the remote control.",
    "Move systematically around the room to locate the sofa and confirm if the remote is under it."
  ],
  "estimated_number_of_trips": "multiple",
  "efficiency_consideration": "The task may require multiple trips as the current observation does not provide sufficient information about the location of the remote control.",
  "safety_or_stability_consideration": "Ensure that movements are stable and do not disturb any objects in the room, especially near windows or furniture.",
  "uncertainty_or_missing_information": "The exact location of the sofa and the remote control is unknown. The current observation does not confirm their presence, so further exploration is needed.",
  "reason": "The new observation (O1) does not show a sofa or remote control, indicating that the task cannot be completed based on this view alone. Therefore, it is necessary to continue searching for the correct location."
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
{"task_understanding": "The task is to retrieve a remote control located under the sofa. The image shows a bed, not a sofa, so there may be a mismatch between the described location and the visual scene.", "plan": ["Move to the area where the sofa is located.", "Check if the remote control is visible or accessible under the sofa.", "Use the mechanical arm to grasp the remote control securely.", "Lift the remote control out from under the sofa.", "Carry the remote control to the designated destination."], "estimated_number_of_trips": "single", "efficiency_consideration": "Minimize movement by directly accessing the remote control without unnecessary detours.", "safety_or_stability_consideration": "Ensure stable movement of the robot and avoid tipping while reaching under the sofa.", "uncertainty_or_missing_information": "The image does not show a sofa; it shows a bed. The exact location of the sofa is unknown, so the initial search may require adjustment.", "reason": "The task requires retrieving an object from under a piece of furniture, but the visual context does not match the described scenario (sofa vs. bed). Therefore, the robot must first locate the correct furniture before attempting retrieval."}
```

### Final Raw Response

```json
{"task_understanding": "The task is to retrieve a remote control from under the sofa. The previous observation (O0) showed a bed with objects under it, but no sofa was visible. The current observation (O1) shows a different room setup with a table and lamp, but still no clear view of a sofa.", "plan": ["Confirm that the current location does not contain the sofa mentioned in the task.", "Proceed to scan the surrounding area for the presence of a sofa.", "If a sofa is found, approach it and check underneath for the remote control.", "Use the mechanical arm to retrieve the remote control if visible or accessible.", "Carry the remote control to the designated destination."], "estimated_number_of_trips": "multiple", "efficiency_consideration": "Prioritize scanning areas likely to contain a sofa based on room layout and previous observations.", "safety_or_stability_consideration": "Maintain balance while moving between locations; avoid obstacles during navigation.", "uncertainty_or_missing_information": "The exact location of the sofa remains unknown, and no direct evidence of it is present in either observation.", "reason": "Since neither O0 nor O1 shows a sofa, further exploration is needed to locate it. The robot should continue searching nearby areas until the sofa is found."}
```

