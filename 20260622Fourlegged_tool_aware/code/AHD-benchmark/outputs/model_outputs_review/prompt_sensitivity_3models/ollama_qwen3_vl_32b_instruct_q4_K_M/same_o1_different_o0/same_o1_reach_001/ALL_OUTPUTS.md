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
  "task_understanding": "从沙发下方取出遥控器，确保操作安全且高效。",
  "plan": [
    "检查沙发下方区域以确认遥控器的位置和周围环境是否无障碍物。",
    "伸入机械臂或移动身体进入沙发下方空间，抓取遥控器。",
    "将遥控器移出并放置在安全、可见的表面上（如茶几或桌面）。",
    "确认任务完成，返回初始位置或待命状态。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "通过一次进入沙发下方区域直接抓取遥控器，避免多次往返；若空间狭窄则需谨慎规划路径以减少调整次数。",
  "safety_or_stability_consideration": "确保在伸入或移动过程中不碰倒周围物品（如台灯、书籍），并保持自身平衡以防倾覆。同时注意地毯和障碍物可能影响移动稳定性。",
  "uncertainty_or_missing_information": "遥控器的具体位置未明确，沙发下方可能存在其他杂物（如玩具块）；需确认是否需要清理路径或避开障碍物才能抓取。",
  "reason": "基于O0和O1的观察，沙发下方可见一个彩色小方块（可能是玩具），但遥控器尚未被直接识别。因此，第一步应是环视并定位遥控器，再执行抓取动作。由于任务目标明确且空间相对开放，预计一次操作即可完成，无需多次往返。安全方面需注意周围物品的稳定性及移动路径中的障碍物。"
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
  "task_understanding": "从沙发下方取出遥控器，该遥控器位于沙发底部靠近地面的位置。",
  "plan": [
    "检查沙发下方区域以确认遥控器的具体位置和可访问性。",
    "若遥控器可见且易于抓取，则使用一只手伸入并拾取遥控器；若空间狭窄或遥控器被遮挡，则尝试调整姿态或移动沙发边缘以便接触。",
    "将遥控器安全取出后，放置在附近稳定表面（如茶几）上。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "优先直接抓取以减少动作次数；若需调整环境，则最小化移动幅度和时间。",
  "safety_or_stability_consideration": "避免在操作过程中碰撞沙发或造成自身不稳定，确保手臂伸入时不会卡住或损坏物体。",
  "uncertainty_or_missing_information": "遥控器是否被其他物品（如玩具、布料）遮挡；沙发下方空间深度和宽度是否允许手臂完全进入并稳定抓取。",
  "reason": "基于O0和O1的观察，遥控器位于沙发底部靠近地面处，但未明确可见。因此需先检查确认其位置与可访问性，再决定最安全高效的拾取方式。"
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
  "task_understanding": "从沙发下方取出遥控器，该区域光线较暗且空间狭窄，需谨慎操作以避免碰撞或掉落物品。",
  "plan": [
    "短程环视确认沙发下方是否有可见的遥控器或其他障碍物。",
    "若遥控器在视线范围内且可触及，则伸展机械臂并使用夹爪小心抓取；否则尝试调整位置以便更接近目标区域。",
    "成功拾取后，将遥控器移至安全高度，并返回指定放置点或交还给用户。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "通过环视减少不必要的移动和重复尝试；优先使用一次操作完成任务。",
  "safety_or_stability_consideration": "在狭窄空间中避免机械臂过度伸展导致失衡或碰撞沙发结构，确保夹爪抓取稳定后再提升物体。",
  "uncertainty_or_missing_information": "遥控器是否完全位于沙发下方、是否有遮挡物（如玩具块）影响获取路径尚不明确；需进一步确认其确切位置和可及性。",
  "reason": "基于O0与O1的观察，初步判断遥控器可能被部分遮挡或处于深部空间。环视后若仍不可见，则需调整姿态或尝试不同角度接近目标，以确保安全高效完成任务。"
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
  "task_understanding": "从沙发下方取出遥控器。",
  "plan": [
    "检查沙发下方区域以定位遥控器",
    "确认遥控器位置并规划抓取路径",
    "伸入或移动至沙发下方抓取遥控器",
    "将遥控器移出并放置在安全可见的位置"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接定位并取出遥控器，避免不必要的重复动作。",
  "safety_or_stability_consideration": "确保移动过程中不碰撞沙发或周围物体，保持稳定抓取以防掉落。",
  "uncertainty_or_missing_information": "遥控器在沙发下方的具体位置和可见性尚不确定；可能被遮挡或与其他物品混杂。",
  "reason": "根据初始观察O0，沙发下方有阴影区域且存在小物件（如积木），但未明确看到遥控器。短程环视后O1未提供新信息，因此需主动检查该区域以确认遥控器位置并安全取出。"
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
  "task_understanding": "从沙发下方取出遥控器。",
  "plan": [
    "检查沙发下方区域，确认遥控器的位置和可访问性。",
    "使用一只手或双手伸入沙发下方抓取遥控器（若空间允许）。",
    "将遥控器取出并放置在安全、可见的表面上。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接定位并取出遥控器，避免不必要的移动或重复操作。",
  "safety_or_stability_consideration": "确保手臂伸入沙发下方时不会损坏家具或自身结构；抓取时保持稳定以防止掉落。",
  "uncertainty_or_missing_information": "遥控器在沙发下的具体位置和周围是否有障碍物（如玩具、布料）尚不明确，可能影响抓取。",
  "reason": "基于初始观察O0，沙发下方可见一个彩色积木和一块布，但未见遥控器。短程环视后O1未提供新信息，因此需主动检查沙发下方以确认遥控器位置，并规划安全有效的取出方式。"
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
  "task_understanding": "从沙发下方取出遥控器，该区域光线较暗且空间狭窄，可能需要调整视角或移动位置以确认目标物体的位置。",
  "plan": [
    "短程环视周围环境，确认遥控器是否在沙发下方可见区域。",
    "若遥控器不可见，则尝试靠近沙发底部并伸展机械臂探入下方空间进行搜索。",
    "一旦定位到遥控器，使用夹爪稳定抓取后将其取出并放置于安全位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "避免不必要的移动；优先通过环视确认目标位置以减少操作次数。",
  "safety_or_stability_consideration": "在探入沙发下方时需确保机械臂动作平稳，防止因空间狭窄导致夹爪卡住或机器人失衡。",
  "uncertainty_or_missing_information": "遥控器是否完全被遮挡、其确切位置以及是否与其他物体（如玩具）混杂尚不明确。",
  "reason": "基于O0和O1的观察，沙发下方存在一个彩色小方块状物体（可能是玩具），但未见明显遥控器。因此需进一步确认目标是否存在及具体位置，再执行抓取操作。"
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
  "task_understanding": "目标是取出位于沙发下方的遥控器。当前视野中，沙发底部可见一个彩色小方块物体（疑似玩具或遥控器），但无法确认是否为目标物；同时地面有衣物和托盘等杂物，可能遮挡或干扰操作。",
  "plan": [
    "短程环视并检查沙发下方区域，确认遥控器的具体位置及周围障碍物情况。",
    "若遥控器被遮挡或难以直接抓取，则寻找附近可用的辅助工具（如托盘、纸巾盒等）用于推动或拨动遥控器至可触及范围。",
    "使用机械臂或辅助工具将遥控器取出并放置于安全可见位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作可能因空间狭窄或遮挡导致失败，短程寻找辅助物能提升一次成功率，避免多次往返。",
  "safety_or_stability_consideration": "沙发下方空间狭小，直接伸入可能导致机械臂卡滞或损坏；使用辅助工具可减少风险并提高稳定性。",
  "uncertainty_or_missing_information": "当前图像中彩色方块是否为遥控器尚不明确，且地面杂物可能影响操作路径和抓取成功率。",
  "reason": "由于目标物位置隐蔽、空间受限且存在遮挡物，直接操作效率低且有风险。短程检查可确认目标并寻找辅助工具（如托盘），提升任务完成的稳定性和一次性成功率。因此优先进行环境评估与辅助物准备。"
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
  "task_understanding": "目标是取出位于沙发下方的遥控器。当前视野中，沙发底部可见一个彩色小方块玩具和一块布料，但未见遥控器。需要确认遥控器是否在沙发下方，并规划如何安全、稳定地将其取出。",
  "plan": [
    "检查沙发下方区域，确认遥控器的具体位置及周围环境（如是否有障碍物或空间限制）。",
    "若遥控器位于狭窄或深部空间，短程寻找一个合适的辅助工具（如长柄夹子、细长棍状物等），以提升抓取的可达性和稳定性；否则直接使用手臂尝试取出。",
    "使用双手或辅助工具将遥控器从沙发下方取出，并放置于安全可见位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "若遥控器位置较浅且无遮挡，直接操作效率更高；否则需先寻找辅助工具以避免多次尝试或失败。",
  "safety_or_stability_consideration": "沙发下方空间可能狭窄，手臂伸入时存在卡住或掉落风险。使用辅助工具可提高稳定性并减少对家具的潜在损伤。",
  "uncertainty_or_missing_information": "当前图像未明确显示遥控器是否在沙发下方、具体位置及周围障碍物情况；需通过短程检查确认。",
  "reason": "由于初始视野中未直接看到遥控器，且沙发下方可能存在空间限制或遮挡物，因此需要先进行短程检查以定位目标。若无法直接触及，则应寻找辅助工具提升操作成功率和安全性。双手直接操作仅在目标可见、可达且无干扰时适用；当前情况存在不确定性，故优先考虑安全与稳定性的方案。"
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
  "task_understanding": "目标是取出位于沙发下方的遥控器。当前视野中可见沙发底部空间，但遥控器未直接暴露在视线内，可能被遮挡或处于较深位置。",
  "plan": [
    "短程环视确认沙发下方区域是否有其他障碍物或可辅助操作的物体（如托盘、工具等）。",
    "若无合适辅助物，则尝试伸展机械臂进入沙发底部空间，定位并夹取遥控器。",
    "若直接夹取困难或不稳定，则寻找附近可用的长柄工具或扁平物体作为辅助探入工具，用于拨动或推动遥控器至可抓取位置后取出。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "优先尝试直接操作以减少往返；若失败则寻找辅助物一次性解决，避免多次移动。",
  "safety_or_stability_consideration": "机械臂伸入狭窄空间时需保持身体平衡，避免因过度前倾导致失稳。夹爪抓取时确保遥控器稳定，防止掉落或损坏。",
  "uncertainty_or_missing_information": "遥控器在沙发下的具体位置、是否被其他物体遮挡、以及是否有足够空间让机械臂伸入并操作尚不明确。",
  "reason": "当前视野中未直接看到遥控器，且沙发下方为深而狭窄的空间，单靠夹爪可能难以稳定抓取。因此需先短程环视确认是否存在辅助工具（如托盘、长柄物体等），若无则尝试直接伸入操作；若有，则优先使用辅助物提升可达性和稳定性。此策略兼顾效率与安全性。"
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
  "task_understanding": "目标是取出位于沙发下方的遥控器。根据初始观察O0，遥控器被一个黑色托盘部分遮挡，且位置靠近沙发底部边缘，可能需要移动或抬起托盘才能触及。",
  "plan": [
    "短程环视以确认遥控器的确切位置和周围环境（如是否有障碍物、是否可直接伸手取出）",
    "若遥控器被托盘遮挡，则尝试小心地将黑色托盘向一侧滑动或抬起，以便暴露遥控器",
    "取出遥控器并放置在安全可见的位置"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作可能因空间狭窄而困难；使用托盘作为辅助工具可减少反复尝试和潜在碰撞。若托盘易于移动，则优先利用它提升效率。",
  "safety_or_stability_consideration": "在抬起或滑动托盘时需避免对沙发结构造成压力，同时防止遥控器掉落至更难触及的位置；操作应平稳、缓慢。",
  "uncertainty_or_missing_information": "当前图像未明确显示遥控器是否完全被遮挡，也未确认其与托盘的接触方式（如是否卡在下方）。需要环视以获取更多信息。",
  "reason": "直接伸手可能因空间受限而失败。黑色托盘是可见且可移动的辅助物体，能有效暴露目标物。因此计划优先尝试通过移动托盘来完成任务，而非强行伸入狭窄区域。"
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
  "task_understanding": "目标是取出位于沙发下方的遥控器。根据初始观察O0，沙发下方可见一个彩色小方块玩具和一块布料，但未见遥控器；短程环视后的新场景O1中也未明确显示遥控器位置，因此需要进一步确认其具体位置。",
  "plan": [
    "检查沙发下方区域以定位遥控器的具体位置。",
    "若遥控器位于狭窄或深部空间，考虑使用辅助工具（如长柄夹子、纸板等）将其取出；否则直接用手抓取。",
    "将遥控器从沙发下取出并放置在安全可见的位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "若遥控器位置浅且易于触及，直接操作效率最高；若位于深部或狭窄空间，则需使用辅助工具以避免多次尝试或损坏物品。",
  "safety_or_stability_consideration": "沙发下方可能存在障碍物（如玩具、布料），直接伸手可能造成手臂卡住或物体掉落。优先确认位置和环境后再操作，确保稳定抓取。",
  "uncertainty_or_missing_information": "遥控器在当前图像中未被明确识别，其确切位置未知；需进一步检查沙发下方区域以确认是否需要辅助工具。",
  "reason": "由于初始观察和短程环视均未清晰显示遥控器，必须先定位目标物。若直接伸手可及，则无需辅助工具；否则应寻找或使用合适的辅助物体（如长柄夹子、纸板等）提升可达性和稳定性。当前无明显可用的辅助物体在视野中，因此可能需要短程搜索或准备临时工具。"
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
  "task_understanding": "目标是取出位于沙发下方的遥控器。根据初始观察O0，沙发下方可见一个彩色小方块玩具和一块布料，但未见遥控器；短程环视后的新场景O1中也未明确显示遥控器位置，因此需要进一步确认其具体位置。",
  "plan": [
    "移动至沙发前方，降低高度并使用机械臂在沙发下方进行扫描或探测以定位遥控器。",
    "一旦确定遥控器位置，尝试用夹爪直接抓取；若空间狭窄或遥控器被遮挡，则考虑使用辅助工具（如长柄夹子）或调整姿态以便够到目标。",
    "成功取出后，将遥控器放置于安全可见的位置（如茶几上）。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作是首选方案；若无法直接抓取，则需寻找辅助工具以避免多次往返。当前未见明显可用的辅助物体，因此优先尝试直接操作。",
  "safety_or_stability_consideration": "在沙发下方操作时需确保机械臂稳定且不触碰家具造成损坏或自身失衡。移动过程中保持底盘平衡，避免碰撞。",
  "uncertainty_or_missing_information": "遥控器的具体位置和周围障碍物情况未明确；可能被玩具、布料或其他物体遮挡，需要近距离探测确认。",
  "reason": "由于初始观察中未直接看到遥控器，且沙发下方空间可能存在遮挡或狭窄限制，因此必须先进行定位。夹爪一次只能稳定携带一个物体，而遥控器是单个小型物品，适合直接抓取；若无法触及，则需考虑辅助工具，但当前场景中无明显可用的辅助物，故优先尝试直接操作并根据探测结果调整策略。"
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
  "task_understanding": "从沙发下方取出遥控器。",
  "plan": [
    "检查沙发下方区域以确认遥控器的位置和可访问性。",
    "若遥控器可见且可触及，使用一只手或双手将其取出。",
    "若遥控器被遮挡或难以直接抓取，则尝试移动障碍物（如玩具）或调整身体姿态以便够到。",
    "将遥控器安全放置在附近平坦表面（如茶几）。"
  ],
  "target_objects": ["遥控器"],
  "helper_needed": "uncertain",
  "helper_purpose": "reach",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "yes",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "定位遥控器在沙发下方的具体位置。",
    "伸展手臂尝试抓取遥控器。",
    "若失败，调整姿态或移动障碍物后重试。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "优先直接抓取以减少动作次数；如需辅助则快速评估可用工具。",
  "safety_or_stability_consideration": "避免在伸展过程中碰撞家具或导致自身失稳，尤其注意沙发边缘和地面障碍物。",
  "physical_feasibility_risk": "沙发下方空间狭窄且有玩具阻挡，可能无法直接触及遥控器；手臂长度或角度不足可能导致抓取失败。",
  "uncertainty_or_missing_information": "遥控器是否被完全遮挡、其确切位置以及是否有其他物体阻碍抓取尚不明确。",
  "reason": "基于初始观察，沙发下方可见一个彩色玩具和部分阴影区域，但未直接看到遥控器。短程环视后仍无新信息表明遥控器的位置或可及性，因此需先检查并确认其状态再执行抓取动作。",
  "failure_risk": "若遥控器被完全遮挡且无法移动障碍物，则可能需要人类协助；否则在多次尝试失败后可能导致任务超时或损坏周围物品。"
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
  "task_understanding": "从沙发下方取出遥控器。",
  "plan": [
    "移动至沙发前方，确认遥控器在沙发底部的可见位置。",
    "伸展机械臂尝试抓取遥控器；若空间狭窄或视线受阻，则调整姿态以获得更好角度。",
    "成功抓取后，将遥控器移出并放置于安全、易取的位置（如茶几）。",
    "确认任务完成。"
  ],
  "target_objects": ["遥控器"],
  "helper_needed": "uncertain",
  "helper_purpose": "reach",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "not_applicable",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "移动至沙发下方区域。",
    "使用机械臂伸入沙发底部尝试定位并抓取遥控器。",
    "若失败，调整位置或姿态后重试。",
    "成功取出后放置于指定位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作避免多次往返；优先使用机械臂伸入尝试一次完成任务。",
  "safety_or_stability_consideration": "在沙发下方操作时需确保身体平衡，防止因重心偏移导致倾倒或碰撞。",
  "physical_feasibility_risk": "沙发底部空间可能狭窄，机械臂无法完全伸入或夹爪难以稳定抓取；遥控器位置不确定可能导致多次尝试失败。",
  "uncertainty_or_missing_information": "遥控器在沙发下方的具体位置、是否被遮挡或与其他物体（如玩具）混杂未明确；当前视角下无法确认其确切可及性。",
  "reason": "基于O0和O1观察，遥控器位于沙发底部但未直接可见。需通过机械臂尝试抓取，可能需要调整姿态以获得更好操作角度。由于空间限制和物体位置不确定性，存在物理可行性风险，因此计划中包含多次尝试的容错步骤。",
  "failure_risk": "若遥控器被遮挡或夹爪无法稳定抓取，则可能导致任务失败；机械臂在狭窄空间内操作可能触发碰撞或卡住。"
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
  "task_understanding": "从沙发下方取出遥控器并将其带到指定位置（默认为安全可见区域）。",
  "plan": [
    "检查沙发下方区域以确认遥控器的位置和可访问性",
    "若遥控器可见且可触及，则伸入或移动至其位置进行拾取",
    "将遥控器移出沙发下方并放置在安全、可见的表面上"
  ],
  "target_objects": ["遥控器"],
  "helper_needed": "uncertain",
  "helper_purpose": "reach",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "not_applicable",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "定位遥控器在沙发下方的具体位置",
    "伸入或移动至遥控器所在处进行拾取",
    "将遥控器移出并放置于安全区域"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作，避免不必要的移动或重复尝试。",
  "safety_or_stability_consideration": "在伸入沙发下方时需确保自身稳定，防止倾倒或卡住；避免对家具造成损坏。",
  "physical_feasibility_risk": "遥控器可能被遮挡、位置过深或空间狭窄导致无法触及。",
  "uncertainty_or_missing_information": "当前图像中未明确显示遥控器的具体位置和是否完全可见，需进一步环视确认其可访问性。",
  "reason": "基于初始观察O0，沙发下方存在阴影区域且有小物件（如积木），但遥控器未被直接识别。短程环视后O1仍无明显变化，因此需要先确认遥控器是否在可见范围内及能否安全触及。若不可见或无法触及，则需调整策略。",
  "failure_risk": "遥控器可能不在沙发下方、位置过深导致无法拾取，或机器人因空间限制而卡住或损坏自身。"
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
  "task_understanding": "从沙发下方取出遥控器，该遥控器位于沙发底部靠近地面的位置。",
  "plan": [
    "移动到沙发前方，确认遥控器在沙发底座下的具体位置。",
    "降低高度或使用伸缩臂/机械手探入沙发下方，抓取遥控器。",
    "将遥控器从沙发下取出并放置于安全可见的表面（如茶几）。",
    "完成任务后返回初始位置或待命状态。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作无需往返，使用机械臂伸入即可高效取物；若空间狭窄可考虑调整姿态以减少移动次数。",
  "safety_or_stability_consideration": "在探入沙发下方时需确保动作平稳，避免碰撞或刮伤家具表面。同时注意地面杂物（如玩具、布料）可能影响移动路径。",
  "uncertainty_or_missing_information": "遥控器的具体位置和深度未知；沙发底座与地面间隙是否足够机械臂伸入尚不明确；周围是否有障碍物阻挡接近。",
  "reason": "基于O0和O1的观察，遥控器位于沙发下方且靠近地面。虽然未直接看到遥控器，但其存在已被任务确认。因此计划优先通过降低高度或使用可伸缩部件探入取物，避免不必要的移动。若空间受限，则需调整姿态以确保安全抓取。"
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
  "task_understanding": "从沙发下方取出遥控器，该区域光线较暗且空间狭窄，可能需要调整姿态或使用工具辅助抓取。",
  "plan": [
    "环视确认沙发下方是否有可见的遥控器或其他障碍物。",
    "若遥控器在视线范围内但难以直接触及，则尝试伸展手臂并利用夹爪稳定抓取；否则，考虑移动沙发边缘以扩大操作空间。",
    "成功取出后，将遥控器放置于安全、易取的位置（如茶几或沙发上）。",
    "确认任务完成。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "优先尝试直接抓取避免移动家具；若不可行，则最小化调整动作以减少操作时间。",
  "safety_or_stability_consideration": "在伸展手臂或移动沙发边缘时，需确保不会损坏地毯、家具或自身结构；夹爪应稳定抓握以防掉落。",
  "uncertainty_or_missing_information": "遥控器是否被其他物体遮挡（如玩具块）？其确切位置和朝向未知。若空间过窄，手臂可能无法完全伸入。",
  "reason": "基于O0与O1的观察，沙发下方存在一个彩色积木块，可能部分阻挡遥控器；同时，该区域光线不足且深度较大，直接抓取可能存在困难。因此计划优先检查可见性，再决定是否需要调整环境以提升可达性。"
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
  "task_understanding": "从沙发下方取出遥控器，该区域光线较暗且空间狭窄，可能需要调整视角或使用辅助工具以确保准确识别和抓取。",
  "plan": [
    "短程环视确认沙发下方是否有可见的遥控器或其他物体。",
    "若遥控器在视线范围内但位置偏深，尝试伸展机械臂并使用夹爪小心探入获取；否则需移动身体靠近或调整角度以获得更好可达性。",
    "成功抓取后，将遥控器移出至安全区域，并确认其状态完好。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "通过环视快速判断是否需要物理干预；若遥控器可见且位置浅，则可直接操作避免多余移动。",
  "safety_or_stability_consideration": "在伸入沙发下方时需确保机械臂动作平稳，防止夹爪卡住或损坏家具；同时保持底盘平衡以防倾覆。",
  "uncertainty_or_missing_information": "遥控器是否被其他物体遮挡、其确切位置及深度未知，可能需要多次微调抓取角度。",
  "reason": "基于O0和O1的观察，沙发下方存在一个彩色小方块（可能是玩具或误识别），但未明确看到遥控器。因此需先确认目标是否存在并定位，再决定是否直接操作或调整姿态以提高成功率。优先考虑单次高效完成任务，避免多次往返。"
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
  "task_understanding": "从沙发下方取出遥控器。",
  "plan": [
    "检查沙发下方区域，确认遥控器的位置和可访问性。",
    "伸入或移动至沙发下方，安全地拾取遥控器。",
    "将遥控器移出并放置在易于取用的表面（如茶几）上。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接定位目标物并一次性完成任务，避免不必要的往返或重复动作。",
  "safety_or_stability_consideration": "确保在伸入沙发下方时保持身体稳定，防止碰撞或绊倒；若空间狭窄，可使用机械臂或工具辅助以减少风险。",
  "uncertainty_or_missing_information": "遥控器的具体位置和是否被遮挡（如玩具、布料等）尚不明确，可能需要轻微移动障碍物。",
  "reason": "图像显示沙发下方有彩色积木和衣物，遥控器可能被部分遮挡。为安全高效完成任务，需先确认其确切位置并清除潜在障碍后再取出。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "从沙发下方取出遥控器。",
  "plan": [
    "回顾上一轮观察（O0）：沙发下方存在积木和衣物，遥控器可能被遮挡。",
    "当前观察（O1）显示的是厨房台面区域，包含烤盘、手机、书籍和台灯，未见遥控器或沙发相关物体。",
    "确认当前视野中无目标物，需返回至沙发附近区域继续搜索。",
    "在沙发下方重新检查并清除积木或衣物等障碍物后取出遥控器。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "避免在无关区域浪费时间；优先聚焦于已知目标位置（沙发下方），仅当必要时才扩展搜索范围。",
  "safety_or_stability_consideration": "移动过程中注意周围家具和地面障碍物，确保路径畅通且操作稳定。若需伸入狭窄空间，应使用可调节工具或机械臂以减少风险。",
  "uncertainty_or_missing_information": "遥控器是否仍在沙发下方、是否被完全遮挡仍不确定；当前观察未提供新线索。",
  "reason": "O1为厨房台面场景，与原始任务无关。结合O0中沙发下方存在障碍物的信息，应返回原区域继续搜索并清除障碍以完成取物任务。"
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
  "task_understanding": "从沙发下方取出一个遥控器，该遥控器位于沙发底部靠近地面的位置。",
  "plan": [
    "检查沙发下方区域以确认遥控器的具体位置和可及性。",
    "使用一只手伸入沙发下方抓取遥控器，同时保持身体稳定以防碰撞或倾倒。",
    "将遥控器取出并放置在安全、可见的表面上（如茶几或沙发扶手）。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "一次性完成任务，避免多次往返；优先使用单臂操作以减少动作复杂度。",
  "safety_or_stability_consideration": "在伸入沙发下方时需确保手臂和身体稳定，防止因空间狭窄导致意外碰撞或摔倒。同时注意不要拉扯或损坏沙发结构。",
  "uncertainty_or_missing_information": "遥控器是否被其他物体遮挡（如玩具、布料）尚未确认；沙发底部是否有足够空间让手臂伸入也存在不确定性。",
  "reason": "根据图像，遥控器位于沙发下方靠近地面的位置，且周围有小玩具和布料。为安全高效完成任务，需先检查环境再操作，避免因遮挡或空间不足导致失败或损坏物品。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "从沙发下方取出遥控器。根据最新观察，当前视野聚焦于台面区域（含烤盘、台灯、手机等），未显示沙发或其下方空间。",
  "plan": [
    "返回至沙发所在区域，重新定位并检查沙发下方以确认遥控器位置和可及性。",
    "使用一只手伸入沙发下方抓取遥控器，同时保持身体稳定以防碰撞或倾倒。",
    "将遥控器取出并放置在安全、可见的表面上（如茶几或沙发扶手）。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "避免在无关区域停留；直接返回目标位置执行任务，减少无效移动。",
  "safety_or_stability_consideration": "在伸入沙发下方时需确保手臂和身体稳定，防止因空间狭窄导致意外碰撞或摔倒。同时注意不要拉扯或损坏沙发结构。",
  "uncertainty_or_missing_information": "当前观察未显示沙发区域，无法确认遥控器是否仍位于原处或已被移动；沙发底部是否有足够空间让手臂伸入也存在不确定性。",
  "reason": "新观察O1聚焦于台面区域，与原始任务目标（沙发下方）无关。因此需返回至沙发所在位置继续执行任务。当前视野中无可用物体辅助完成该任务。"
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
  "task_understanding": "从沙发下方取出一个遥控器，该区域可能因空间狭窄或遮挡而难以直接触及。",
  "plan": [
    "移动至沙发前方，确认遥控器在沙发底部的具体位置和可及性。",
    "若机械臂能够伸入并稳定抓取遥控器，则直接使用夹爪将其取出；否则尝试调整姿态或轻微移动沙发以增加操作空间。",
    "将遥控器安全放置于附近平坦表面（如茶几）或指定交付点。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "优先尝试直接抓取，避免不必要的移动或调整；若需移动沙发，则评估是否影响其他物品或稳定性。",
  "safety_or_stability_consideration": "在伸入狭窄空间时确保机械臂动作平稳，防止夹爪卡住或损坏家具；如需移动沙发，应缓慢且保持底盘平衡。",
  "uncertainty_or_missing_information": "遥控器的具体位置、是否被遮挡（如玩具或其他物品）、以及沙发底部的可进入深度尚不明确。",
  "reason": "由于图像显示沙发下方有彩色积木等物体，可能阻碍直接访问遥控器；同时机械臂能否完全伸入需现场确认。因此计划中包含检查与调整步骤以确保成功取出而不造成损坏或多次往返。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "从沙发下方取出遥控器，但当前观察显示该区域已无可见物品（如积木），且环境为厨房台面，与原始任务场景不符；可能原目标位置已被清理或机器人定位偏移。",
  "plan": [
    "返回至原始沙发区域，重新确认遥控器是否仍在沙发下方。",
    "若遥控器仍存在，则尝试使用机械臂伸入并抓取；如空间受限则轻微调整沙发底部间隙以增加可及性。",
    "将取出的遥控器放置于附近安全平坦表面（如茶几或台面）。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "避免在无关区域停留，优先返回原始任务位置；若确认目标已移除，则可终止任务。",
  "safety_or_stability_consideration": "移动过程中保持底盘稳定，尤其在调整沙发时需缓慢操作以防倾倒或碰撞。",
  "uncertainty_or_missing_information": "当前观察场景为厨房台面，与原始沙发区域不一致；遥控器是否仍在原位、是否有遮挡物未被确认。",
  "reason": "新观察O1显示的是厨房环境，无遥控器迹象，而原始任务目标位于沙发下方。因此需返回原始位置重新检查，以确认目标是否存在或已被移除。"
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
  "task_understanding": "需要从沙发下方取出一个遥控器，当前图像显示沙发底部有一个彩色小方块物体（可能是遥控器或类似物品），但无法确认其具体身份。",
  "plan": [
    "靠近沙发并检查沙发下方的物体是否为遥控器",
    "如果确认是遥控器，则将其取出",
    "将遥控器放置在安全可见的位置"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接接近目标位置，避免不必要的移动或重复操作。",
  "safety_or_stability_consideration": "在沙发下方操作时需注意自身稳定性和周围环境，防止碰撞或绊倒。",
  "uncertainty_or_missing_information": "图像中物体外观不明确，无法100%确认是否为遥控器；可能需要近距离观察或触碰以确认。",
  "reason": "由于目标物品位于沙发下方且视觉上模糊，需先进行检查确认其身份再执行取出操作，确保任务准确完成。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "根据原始任务，需要从沙发下方取出遥控器。然而，在当前观察O1中，场景已切换至厨房台面区域，未显示沙发或其下方的物体。因此，无法在当前视野内完成任务。",
  "plan": [
    "返回上一轮观察中的沙发区域",
    "靠近沙发并检查沙发下方的物体是否为遥控器",
    "如果确认是遥控器，则将其取出",
    "将遥控器放置在安全可见的位置"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "避免在无关区域停留，直接返回目标位置以提高效率。",
  "safety_or_stability_consideration": "移动过程中注意周围障碍物，确保路径畅通并保持稳定。",
  "uncertainty_or_missing_information": "当前观察O1中未包含沙发或遥控器相关信息；无法确认遥控器是否已被取出或仍在原位。",
  "reason": "新观察O1与任务目标区域无关，因此需返回原始位置继续执行任务。"
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
  "task_understanding": "从沙发下方取出一个遥控器。",
  "plan": [
    "检查沙发下方区域，确认遥控器的位置和可及性。",
    "使用一只手或双手伸入沙发下方，抓取遥控器。",
    "将遥控器安全取出并放置在附近可见的平面上。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作即可完成任务，无需多次往返。",
  "safety_or_stability_consideration": "确保手臂伸入时不会损坏沙发或自身结构；取出遥控器时避免拉扯导致家具移位。",
  "uncertainty_or_missing_information": "遥控器是否被其他物体遮挡、位置深度及是否容易抓取尚不明确，需先检查确认。",
  "reason": "任务目标清晰，但执行前需要确认遥控器在沙发下的具体位置和可操作性。由于空间可能狭窄或有障碍物，直接伸手可能无法成功，因此第一步应为检查区域以评估可行性。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "从沙发下方取出遥控器。",
  "plan": [
    "回顾上一轮观察（O0）中沙发下方存在一个彩色小方块物体，但未确认是否为遥控器。",
    "当前观察（O1）显示的是厨房台面区域，无沙发或其下方空间的可见信息。",
    "返回至沙发所在区域，重新检查沙发下方以定位遥控器。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "避免在无关区域浪费时间；应优先回到任务相关位置执行操作。",
  "safety_or_stability_consideration": "移动过程中注意避开障碍物，确保手臂伸入沙发下方时保持稳定，防止碰撞或损坏家具。",
  "uncertainty_or_missing_information": "当前观察（O1）未提供关于遥控器位置的任何新信息；仍需确认沙发下方是否有遥控器及是否可抓取。",
  "reason": "新观察 O1 显示的是厨房台面环境，与原始任务无关。因此无法利用其中物体完成任务。必须返回至沙发区域继续检查并执行操作。"
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
{
  "task_understanding": "从沙发下方取出一个遥控器。",
  "plan": [
    "移动到沙发前方，确认遥控器在沙发下方的位置。",
    "伸展机械臂尝试够到遥控器；若空间狭窄或无法直接触及，则调整位置以获得更好的操作角度。",
    "夹取遥控器并将其安全移出至可见区域。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "尽量一次性完成任务，避免重复移动和尝试。",
  "safety_or_stability consideration": "在伸展机械臂时确保身体平衡，防止因过度前倾导致失稳；夹取过程中保持抓握稳定以防掉落。",
  "uncertainty_or_missing_information": "遥控器是否被其他物体遮挡或位于沙发下方过深位置尚不明确，可能需要调整姿态或多次尝试。",
  "reason": "根据图像可见，遥控器位于沙发底部靠近地面处，但具体深度和周围障碍物情况未知。机械臂需谨慎伸入并确保抓取稳定，同时保持整体平衡以避免意外倾倒。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "从沙发下方取出遥控器。",
  "plan": [
    "返回至沙发前方，确认遥控器在沙发下方的位置。",
    "伸展机械臂尝试够到遥控器；若空间狭窄或无法直接触及，则调整位置以获得更好的操作角度。",
    "夹取遥控器并将其安全移出至可见区域。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "当前观察未显示遥控器所在位置，因此需返回原任务地点继续执行；避免在无关区域浪费时间。",
  "safety_or_stability_consideration": "在伸展机械臂时确保身体平衡，防止因过度前倾导致失稳；夹取过程中保持抓握稳定以防掉落。",
  "uncertainty_or_missing_information": "当前观察O1显示的是厨房台面环境，与沙发位置无关。遥控器仍位于沙发下方，其具体深度和周围障碍物情况未知，可能需要调整姿态或多次尝试。",
  "reason": "新观察O1未提供关于遥控器的任何信息，且场景已切换至厨房区域。因此需忽略当前观察，返回原任务地点继续执行计划。"
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "目标是取出位于沙发下方的遥控器，当前视野中可见沙发底部区域，但遥控器未直接暴露在视线内。",
  "plan": [
    "检查沙发下方区域以定位遥控器的具体位置。",
    "若遥控器被遮挡或难以触及，尝试使用手或工具将其移出。",
    "将遥控器取出并放置于安全、可见的位置（如茶几或沙发上）。",
    "确认任务完成。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作即可完成任务，无需往返搬运辅助工具，因遥控器体积小且位置相对固定，短程检查后可立即取出。",
  "safety_or_stability_consideration": "沙发下方空间有限，操作时需注意避免碰撞或拉扯导致家具移位；若遥控器卡在角落，应轻柔移动以防止损坏。",
  "uncertainty_or_missing_information": "当前图像中未直接显示遥控器，仅可见一个彩色小方块（可能是玩具），不确定是否为遥控器。需要短程检查确认目标物身份及位置。",
  "reason": "任务明确要求取出沙发下的遥控器，但图像中未清晰展示该物体。因此需先进行短程检查以定位并确认目标物。由于遥控器体积小、重量轻，且无明显障碍物（如家具或杂物），直接操作即可完成，无需辅助工具。若发现非遥控器，则需进一步搜索；否则取出后放置于可见位置即告完成。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "目标是取出沙发下方的遥控器，但当前图像（O1）显示的是厨房台面区域，包含烤盘、台灯、手机和书籍等物品，并未展示沙发或其下方空间。",
  "plan": [
    "返回至之前观察到沙发的区域（基于O0），重新定位沙发下方空间。",
    "检查沙发下方以确认遥控器的位置并尝试取出。",
    "若遥控器被遮挡，使用手部操作将其移出，并放置于安全可见位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "当前图像（O1）与任务无关，未提供任何有助于完成目标的辅助物体或信息；因此无需在该区域停留或使用其物品。直接返回原区域执行操作更高效。",
  "safety_or_stability_consideration": "在沙发下方操作时需注意避免碰撞家具或拉扯导致不稳定；若遥控器卡住，应轻柔处理以防损坏。",
  "uncertainty_or_missing_information": "当前图像未显示沙发或遥控器，无法确认目标物状态。需要返回原区域进行短程检查以定位遥控器。",
  "reason": "O1展示的是厨房台面环境，与任务无关；而O0中可见沙发下方有彩色小方块（疑似遥控器），但未明确确认。因此需优先返回沙发区域执行短程搜索和操作。当前视野中的物体（如烤盘、手机）均不适合用于取出遥控器，无需使用或检查。直接返回原位置并完成任务是更合理的选择。"
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
  "task_understanding": "目标是取出位于沙发下方的遥控器，当前视野中可见沙发底部空间及部分地面物品，但遥控器未直接显示。",
  "plan": [
    "检查沙发下方区域以定位遥控器的具体位置。",
    "若遥控器在可触及范围内，则使用一只手或双手将其取出；若空间狭窄或难以直接抓取，则短程寻找辅助工具（如长柄夹子、棍状物）进行操作。",
    "将遥控器安全放置于附近台面或指定位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "优先尝试直接抓取以减少往返；若不可行，则寻找辅助工具一次完成任务，避免多次移动。",
  "safety_or_stability_consideration": "沙发下方空间可能狭窄或存在障碍物（如玩具、布料），需谨慎操作以防掉落或卡住；使用辅助工具可提升稳定性与安全性。",
  "uncertainty_or_missing_information": "遥控器在沙发下的具体位置和深度未知，且当前视野未直接显示其存在，需进一步检查确认。",
  "reason": "由于遥控器位于沙发下方且未直接可见，无法确定是否可以直接抓取。因此，首先应检查该区域以定位目标物；若空间受限或难以触及，则需要辅助工具提升操作成功率和安全性。目前无明显可用的辅助物体在视野中，故计划包含短程搜索步骤。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "目标是取出沙发下方的遥控器，但当前视野（O1）显示的是厨房台面区域，包含烤盘、台灯、手机和书籍等物品，未见沙发或遥控器。",
  "plan": [
    "返回至之前观察到沙发的区域（O0），重新检查沙发下方以定位遥控器。",
    "若遥控器在可触及范围内，则使用一只手或双手将其取出；若空间狭窄或难以直接抓取，则短程寻找辅助工具（如长柄夹子、棍状物）进行操作。",
    "将遥控器安全放置于附近台面或指定位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "当前视野中无与任务相关的物体，无法直接使用现有物品辅助取出遥控器；因此需返回原区域执行操作，避免无效停留。",
  "safety_or_stability_consideration": "在沙发下方操作时需注意空间狭窄和潜在障碍物（如玩具、布料），优先考虑稳定抓取或使用工具以减少掉落风险。",
  "uncertainty_or_missing_information": "遥控器的具体位置和深度仍未知，且当前视野未提供任何关于其存在的信息；需要返回原区域进行确认。",
  "reason": "新观察O1显示的是厨房台面环境，与任务目标（沙发下方的遥控器）无关。因此无法利用当前视野中的物体辅助完成任务。必须回到之前可见沙发的区域继续执行计划，并根据实际情况决定是否需要寻找辅助工具。"
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
  "task_understanding": "目标是取出位于沙发下方的遥控器，当前视野中可见沙发底部空间及部分地面物品，但遥控器未直接显示。",
  "plan": [
    "检查沙发下方区域以定位遥控器的具体位置。",
    "若遥控器在可触及范围内，则使用机械臂夹爪将其取出；否则评估是否需要辅助工具或调整姿态以便够到。",
    "将遥控器安全放置于附近台面或其他指定位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作是最高效方式，无需额外往返获取辅助物，除非遥控器被遮挡或空间过深导致机械臂无法触及。",
  "safety_or_stability consideration": "在伸入沙发下方时需确保身体平衡和机械臂稳定，避免因姿态不当造成倾覆或夹爪损坏。若空间狭窄，应缓慢操作以防止卡住或掉落。",
  "uncertainty_or_missing_information": "遥控器的具体位置、是否被其他物体遮挡（如玩具块）、以及沙发底部的深度和宽度未明确，可能影响机械臂可达性。",
  "reason": "当前视野中未直接看到遥控器，但其位于沙发下方是已知条件。由于夹爪一次可稳定携带一个普通小物体，且任务目标单一，优先尝试直接操作。若无法触及，则需短程检查附近是否有可用辅助工具（如长柄夹子），但目前无明显辅助物可见，因此先执行直接搜索与取出计划。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "目标是取出沙发下方的遥控器，但当前视野（O1）显示的是厨房台面区域，包含烤盘、台灯、手机和书籍等物品，未见沙发或遥控器。结合前一观察（O0），沙发位于另一区域，且遥控器在沙发下。",
  "plan": [
    "返回至沙发所在区域，重新定位并检查沙发下方以寻找遥控器。",
    "若遥控器可见且可触及，则使用机械臂夹爪将其取出；否则评估是否需要辅助工具或调整姿态以便够到。",
    "将遥控器安全放置于附近台面或其他指定位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "当前观察区域与任务无关，无需在厨房台面停留；直接返回沙发区是更高效路径。若后续发现辅助工具（如长柄夹子）位于该区域，则可考虑带回使用，但目前无此类物体可见。",
  "safety_or_stability_consideration": "移动过程中需保持身体平衡，尤其在转向或靠近家具时避免碰撞。伸入沙发下方操作时应缓慢、稳定以确保安全。",
  "uncertainty_or_missing_information": "遥控器的具体位置和是否被遮挡仍不确定；当前视野未提供关于沙发区域的任何新信息，因此无法确认其可达性。",
  "reason": "O1 中的物体（如烤盘、台灯）与任务无关，不能用于辅助取出遥控器。由于任务目标明确且位于前一观察中的沙发下方，应立即返回该区域继续执行原计划。无需在当前区域进行短程搜索或获取辅助物，因为无相关物品可见。"
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
  "task_understanding": "目标是取出位于沙发下方的遥控器，该遥控器被部分遮挡在沙发底座与地面之间。",
  "plan": [
    "移动到沙发前方，确认遥控器的具体位置和可及性。",
    "伸展机械臂或使用抓取工具从沙发底部小心地取出遥控器。",
    "将遥控器放置于安全、可见的位置（如茶几或桌面）。",
    "完成任务并返回原位。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作即可完成，无需额外工具或往返搬运，效率较高。",
  "safety_or_stability_consideration": "沙发底部空间狭窄，需确保机械臂动作平稳、避免碰撞家具或地面物体（如玩具块和布料），防止损坏遥控器或周围物品。",
  "uncertainty_or_missing_information": "图像中未明确显示遥控器的完整形态及是否被其他小物件卡住；若存在障碍物可能需要清理路径后再操作。",
  "reason": "直接操作已足够，因为遥控器位于沙发下方但可见且可触及，无需借助辅助工具。机械臂具备足够的灵活性和精度完成抓取任务，同时避免对周围环境造成干扰。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "目标是取出沙发下方的遥控器，但当前图像（O1）显示的是厨房台面场景，包含烤盘、台灯、手机和书籍等物品，未见沙发或遥控器。",
  "plan": [
    "返回上一轮观察位置（O0），重新定位至沙发区域。",
    "确认遥控器在沙发下方的具体位置及可及性。",
    "伸展机械臂从沙发底部小心取出遥控器。",
    "将遥控器放置于安全、可见的位置（如茶几或桌面）。",
    "完成任务并返回原位。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "当前观察区域与目标无关，需立即返回原始场景执行操作；直接前往目标位置效率更高。",
  "safety_or_stability_consideration": "在移动过程中避免碰撞厨房台面物品（如烤盘、手机），确保路径畅通。在沙发下方操作时注意机械臂动作平稳，防止刮伤地面或家具。",
  "uncertainty_or_missing_information": "当前图像未显示遥控器或沙发，无法确认其状态；需返回原始位置重新评估目标物的可达性。",
  "reason": "新观察O1与任务无关，未提供任何有助于取出遥控器的辅助物体。因此应立即返回上一轮观察区域（O0）继续执行原计划，直接操作即可完成任务。"
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
  "task_understanding": "目标是取出位于沙发下方的遥控器，该区域空间狭窄且光线不足，直接伸手可能难以稳定抓取。",
  "plan": [
    "检查沙发下方是否有其他障碍物或可见物品，确认遥控器的具体位置。",
    "尝试使用一只手伸入沙发下方，小心地定位并抓取遥控器；若无法触及，则寻找辅助工具（如长柄夹子、拖鞋等）以增加操作范围。",
    "成功取出遥控器后，将其放置在安全且易于访问的位置（如茶几或沙发上）。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接伸手是最高效的方式；若失败，则需寻找辅助工具，可能增加操作时间。",
  "safety_or_stability_consideration": "沙发下方空间狭窄，手臂伸入时需避免用力过猛导致身体失衡或损坏家具。使用辅助工具可提高稳定性并减少风险。",
  "uncertainty_or_missing_information": "图像中未明确显示遥控器的具体位置和周围环境（如是否有其他杂物阻挡），且无法确认是否需要辅助工具。",
  "reason": "虽然双手直接操作是首选，但沙发下方空间狭窄、光线不足，可能影响抓取稳定性。因此，在尝试直接伸手失败后，应考虑使用辅助工具以确保安全高效完成任务。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "目标是取出沙发下方的遥控器，但当前图像（O1）显示的是厨房台面场景，未包含沙发或其下方空间，因此无法直接观察到遥控器的位置。",
  "plan": [
    "返回至原始任务区域（即沙发所在位置），重新检查沙发下方以定位遥控器。",
    "尝试使用一只手伸入沙发下方抓取遥控器；若因空间狭窄或视线受阻而失败，则寻找附近可用的辅助工具（如长柄夹子、拖鞋等）进行操作。",
    "成功取出遥控器后，将其放置在安全且易于访问的位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "当前观察场景与任务无关，需返回原区域执行；若直接使用辅助工具可减少往返次数并提高效率。",
  "safety_or_stability_consideration": "沙发下方空间狭窄，手臂伸入时需避免用力过猛导致身体失衡或损坏家具。优先考虑使用辅助工具以提升操作稳定性。",
  "uncertainty_or_missing_information": "当前图像未显示沙发或遥控器位置，无法确认是否需要辅助工具；需返回原区域进一步检查。",
  "reason": "新观察O1与任务无关，未提供任何有助于取出遥控器的物体或信息。因此必须返回原始场景执行操作，并在必要时寻找附近可用的辅助工具以提高成功率和安全性。"
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
  "task_understanding": "目标是取出位于沙发下方的遥控器，该位置可能因空间狭窄而难以直接触及。",
  "plan": [
    "检查沙发下方区域以确认遥控器的位置和可及性。",
    "若机械臂无法直接够到遥控器，则寻找合适的辅助工具（如长柄夹子、细长棍状物等）来协助取出。",
    "使用辅助工具或直接操作将遥控器从沙发下取出并放置在安全可见位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "若能直接操作则无需额外往返；否则需一次短程寻找辅助工具，避免多次尝试失败。",
  "safety_or_stability_consideration": "沙发下方空间狭窄，直接伸入可能造成机械臂卡滞或损坏。使用辅助工具可提升操作稳定性并减少风险。",
  "uncertainty_or_missing_information": "图像中未明确显示遥控器的具体位置和周围障碍物情况；也未见明显可用的辅助工具。",
  "reason": "由于沙发下方空间狭窄，直接用夹爪可能无法稳定抓取或存在卡滞风险。因此优先考虑寻找辅助工具以提升操作成功率与安全性。若无合适工具，则需评估是否可调整姿态尝试直接取出。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "目标是取出沙发下方的遥控器，但当前图像（O1）显示的是厨房台面场景，未包含沙发或其下方空间，因此无法直接观察到遥控器位置。",
  "plan": [
    "返回至原始任务区域（即沙发附近），重新定位并检查沙发下方以确认遥控器的位置和可及性。",
    "若机械臂无法直接够到遥控器，则寻找合适的辅助工具（如长柄夹子、细长棍状物等）来协助取出。",
    "使用辅助工具或直接操作将遥控器从沙发下取出并放置在安全可见位置。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "当前观察区域与任务无关，需返回原区域执行任务；若能快速找到辅助工具可减少往返次数。",
  "safety_or_stability_consideration": "沙发下方空间狭窄，直接伸入可能造成机械臂卡滞或损坏。使用辅助工具可提升操作稳定性并减少风险。",
  "uncertainty_or_missing_information": "当前图像未显示沙发或遥控器位置；无法确认是否有可用的辅助物体在附近区域。",
  "reason": "新观察O1与任务无关，未提供任何有助于取出遥控器的信息或工具。因此必须返回原始任务区域，并根据实际情况决定是否需要寻找辅助工具以完成操作。"
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
{
  "task_understanding": "从沙发下方取出一个遥控器。",
  "plan": [
    "检查沙发下方区域以确认遥控器的位置和可及性。",
    "若遥控器可见且可触及，使用一只手或双手将其取出。",
    "若遥控器被遮挡或难以直接抓取，则尝试移动障碍物（如玩具）或调整身体姿态以便够到它。",
    "将遥控器安全放置在附近平坦表面（如茶几）。"
  ],
  "target_objects": ["遥控器"],
  "helper_needed": "uncertain",
  "helper_purpose": "reach",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "yes",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "伸展手臂尝试直接抓取遥控器。",
    "若失败，检查是否有可移动障碍物（如玩具）并移开它。",
    "再次尝试抓取遥控器。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "优先尝试直接操作以减少动作步骤；若不可行，则最小化干扰环境的调整。",
  "safety_or_stability_consideration": "避免在伸展手臂时失去平衡或碰撞家具；确保抓取稳定，防止掉落。",
  "physical_feasibility_risk": "沙发下方空间可能狭窄，手臂无法完全伸入或遥控器位置偏斜导致难以抓握。",
  "uncertainty_or_missing_information": "遥控器是否被玩具或其他物体遮挡、其确切位置和形状未知；沙发底部是否有足够空间供手臂进入。",
  "reason": "当前图像显示沙发下方有一个彩色小方块（可能是玩具），可能部分阻挡了遥控器。由于无法确认遥控器的精确位置和可及性，需先检查并尝试直接抓取，必要时移开障碍物。",
  "failure_risk": "若遥控器被完全遮挡或空间过窄导致手臂无法触及，则任务失败；也可能因操作不当造成物品损坏或自身失稳。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "从沙发下方取出一个遥控器。",
  "plan": [
    "回顾上一轮观察（O0）：沙发下方可见彩色玩具和疑似遥控器的物体，但当前图像（O1）未显示该区域。",
    "确认当前视野中无沙发或其下方区域，因此无法直接执行任务。",
    "返回至沙发附近区域进行重新检查，以定位遥控器并尝试抓取。"
  ],
  "target_objects": ["遥控器"],
  "helper_needed": "uncertain",
  "helper_purpose": "reach",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "yes",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "移动至沙发附近区域。",
    "检查沙发下方以确认遥控器位置和可及性。",
    "尝试直接抓取或移开障碍物后抓取遥控器。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "避免在无目标视野下盲目操作；优先返回原区域进行定位后再执行任务，减少无效动作。",
  "safety_or_stability_consideration": "移动过程中注意周围家具和地面障碍物，防止碰撞或失稳。",
  "physical_feasibility_risk": "沙发下方空间可能狭窄，手臂伸入受限；遥控器位置不确定可能导致抓取失败。",
  "uncertainty_or_missing_information": "当前图像未显示沙发区域，无法确认遥控器是否仍在原位、是否有新障碍物出现。需要重新定位目标区域。",
  "reason": "O1 显示的是厨房台面区域，与原始任务场景（沙发下方）无关；因此必须返回至沙发附近以继续执行任务。",
  "failure_risk": "若无法重新定位遥控器或空间过于狭窄导致抓取失败，则任务可能中断。"
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "从沙发下方取出一个遥控器。",
  "plan": [
    "移动到沙发前方，确认遥控器在沙发下方的位置。",
    "伸展机械臂尝试够到遥控器；若无法直接触及，则评估是否需要辅助工具或调整姿态。",
    "成功抓取后，将遥控器移出并放置于安全可见位置。"
  ],
  "target_objects": ["遥控器"],
  "helper_needed": "uncertain",
  "helper_purpose": "reach",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "yes",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "移动至沙发下方区域",
    "尝试用机械臂抓取遥控器",
    "若失败则检查是否有可用工具辅助伸展或调整姿态"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作优先，避免不必要的往返。",
  "safety_or_stability_consideration": "在沙发下方操作时需确保机械臂运动平稳，防止碰撞或倾覆。",
  "physical_feasibility_risk": "遥控器可能被遮挡或位于狭窄空间内，机械臂无法完全伸入或抓取不稳定。",
  "uncertainty_or_missing_information": "图像中未明确显示遥控器的具体位置和可见性；沙发下方可能存在障碍物影响操作。",
  "reason": "虽然目标物体（遥控器）在视觉上可能被部分遮挡，但基于任务描述其位于沙发下方。需先确认可及性再执行抓取动作。",
  "failure_risk": "若遥控器位置过深或被杂物阻挡，机械臂无法触及；或抓取后因空间狭小导致夹爪松脱。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "从沙发下方取出一个遥控器。",
  "plan": [
    "移动至沙发前方，确认遥控器在沙发下方的位置。",
    "伸展机械臂尝试够到遥控器；若无法直接触及，则评估是否需要辅助工具或调整姿态。",
    "成功抓取后，将遥控器移出并放置于安全可见位置。"
  ],
  "target_objects": ["遥控器"],
  "helper_needed": "uncertain",
  "helper_purpose": "reach",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "yes",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "移动至沙发下方区域",
    "尝试用机械臂抓取遥控器",
    "若失败则检查是否有可用工具辅助伸展或调整姿态"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作优先，避免不必要的往返。",
  "safety_or_stability_consideration": "在沙发下方操作时需确保机械臂运动平稳，防止碰撞或倾覆。",
  "physical_feasibility_risk": "遥控器可能被遮挡或位于狭窄空间内，机械臂无法完全伸入或抓取不稳定。",
  "uncertainty_or_missing_information": "当前观察O1显示的是厨房台面区域，与沙发下方无关；原任务目标位置未在新观察中出现。需继续检查沙发附近区域以确认遥控器位置。",
  "reason": "新观察O1并未提供关于沙发或其下方的任何信息，因此无法基于此更新计划。必须返回至沙发区域进行进一步探测。",
  "failure_risk": "若遥控器位置过深或被杂物阻挡，机械臂无法触及；或抓取后因空间狭小导致夹爪松脱。"
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
{
  "task_understanding": "从沙发下方取出遥控器。",
  "plan": [
    "检查沙发下方区域以确认遥控器的位置和可访问性。",
    "伸入或移动到沙发下方，抓取遥控器。",
    "将遥控器移出并放置在安全可见位置。"
  ],
  "target_objects": ["遥控器"],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "not_applicable",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "伸入沙发下方抓取遥控器。",
    "将遥控器取出并放置在安全位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作，无需额外工具或多次往返。",
  "safety_or_stability_consideration": "确保移动过程中不损坏沙发或自身结构；避免卡住或受阻。",
  "physical_feasibility_risk": "遥控器可能被遮挡或难以触及，需确认空间是否允许伸入。",
  "uncertainty_or_missing_information": "图像中未明确显示遥控器的具体位置和可见性，仅知其位于沙发下方。",
  "reason": "任务目标清晰，操作路径直接。无需外部协助，但需先确认遥控器的可访问性以避免无效尝试。",
  "failure_risk": "若遥控器被完全遮挡或空间过小导致无法抓取，则可能失败；建议先检查再执行。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "从沙发下方取出遥控器。",
  "plan": [
    "回顾上一轮观察（O0）中沙发下方存在遥控器的线索，但当前观察（O1）未显示沙发或其下方区域。",
    "确认当前视野内无目标物体，需重新定位至沙发附近区域进行检查。",
    "在沙发下方再次搜索并取出遥控器。"
  ],
  "target_objects": ["遥控器"],
  "helper_needed": "no",
  "helper_purpose": "none",
  "visible_helper_detected": "no",
  "visible_helper_objects": [],
  "search_for_helper_if_none_visible": "not_applicable",
  "selected_helper": "none",
  "tool_use_action_chain": [
    "移动至沙发区域。",
    "检查并伸入沙发下方抓取遥控器。",
    "将遥控器取出并放置在安全位置。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "当前观察未提供目标物体信息，需返回原任务区域以提高效率。",
  "safety_or_stability_consideration": "移动过程中避免碰撞家具或障碍物；确保在沙发下方操作时保持稳定。",
  "physical_feasibility_risk": "遥控器可能被遮挡或空间狭窄导致抓取困难，需确认可访问性。",
  "uncertainty_or_missing_information": "当前观察（O1）未包含沙发或其下方区域，无法验证遥控器位置；需重新定位至原任务区域。",
  "reason": "新观察（O1）与原始任务无关，未提供目标物体信息。必须返回沙发附近区域以继续执行任务。",
  "failure_risk": "若未能准确回到沙发区域或遥控器被遮挡，则可能导致任务失败。"
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
任务：请把沙发下面的遥控器拿出来。
```

### User Prompt Turn 2

```text
机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。仍然只输出同一 JSON schema。
```

### Turn 1 Raw Response

```json
{
  "task_understanding": "需要从沙发下方取出一个遥控器，该遥控器位于沙发底部与地面之间的空间内。",
  "plan": [
    "移动到沙发前方，确认遥控器在沙发底下的具体位置。",
    "伸入或使用工具（如长柄夹子）从沙发下方取出遥控器。",
    "将遥控器放置于安全、易取的位置（例如茶几上）。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作可能因空间狭窄而困难，但若无合适工具，则需尝试伸入或调整姿态以完成任务。无需往返。",
  "safety_or_stability_consideration": "沙发下方可能存在障碍物（如玩具、布料），操作时应避免碰撞或拉扯导致物品损坏或自身不稳定。",
  "uncertainty_or_missing_information": "遥控器的具体位置和是否被遮挡不明确，可能需要轻微移动或调整视角确认。",
  "reason": "由于遥控器位于沙发下方且空间有限，直接伸手可能受限。但考虑到任务简单、无需多次往返，优先尝试直接操作；若无法触及，则考虑使用工具辅助。当前环境中未见明显可用的长柄工具，因此计划以伸入为主，并在必要时调整姿态或轻微移动障碍物（如玩具）以确保安全取出。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "需要从沙发下方取出遥控器，但当前图像（O1）显示的是厨房台面区域，包含烤盘、台灯和手机等物品，并未展示沙发或其下方空间。",
  "plan": [
    "返回至沙发所在区域，确认遥控器在沙发底下的具体位置。",
    "伸入或使用工具从沙发下方取出遥控器。",
    "将遥控器放置于安全、易取的位置（例如茶几上）。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "当前观察区域与任务无关，无法利用现有物体辅助完成任务。需返回原位置执行操作，无效率提升工具可用。",
  "safety_or_stability_consideration": "在移动过程中应避免碰撞家具或电器（如台灯、烤盘），确保路径安全。",
  "uncertainty_or_missing_information": "遥控器的具体位置和是否被遮挡仍不明确；当前图像未提供沙发区域信息，需重新定位目标区域。",
  "reason": "新观察O1显示的是厨房台面环境，与原始任务（从沙发下取遥控器）无关。因此无法利用当前可见物体作为工具或辅助。必须返回至沙发所在区域继续执行原计划。由于任务未完成且无可用工具，需直接前往目标位置并尝试伸入取出遥控器。"
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
  "task_understanding": "需要从沙发下方取出一个遥控器，该区域可能因空间狭窄或遮挡而难以直接触及。",
  "plan": [
    "检查沙发下方是否有可见的遥控器，并评估其位置和可及性。",
    "若遥控器在伸手可及范围内，则使用一只手将其取出；否则尝试用另一只手辅助或调整姿势以够到它。",
    "如果无法直接取出，考虑使用工具（如长柄夹子）或移动沙发一角来获取访问权限。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "优先尝试直接操作以减少动作复杂度；若不可行，则评估是否需要辅助工具或调整家具位置。",
  "safety_or_stability_consideration": "避免在移动沙发时造成不稳定或损坏，确保操作过程中不会拉扯电线或其他物品。",
  "uncertainty_or_missing_information": "遥控器的确切位置和形状未知，且沙发下方空间可能狭窄，影响抓取稳定性。",
  "reason": "由于遥控器位于沙发下方，直接伸手可能受限于手臂长度或障碍物。因此需先检查可达性，并根据情况决定是否需要辅助工具或调整环境以安全高效地完成任务。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "根据最新观察，沙发下方的遥控器可能已被移除或不在原位；当前视野中未见遥控器，但可见台面上有托盘、手机和书籍等物品。",
  "plan": [
    "确认原始任务目标（取出沙发下的遥控器）是否已完成——检查附近区域是否有遥控器被放置在新位置（如台面或地面）。",
    "若未找到遥控器，则返回至沙发下方区域，重新评估其可达性，并尝试使用一只手伸入抓取；若空间狭窄，考虑用另一只手辅助稳定或调整姿态。",
    "如果仍无法触及，检查环境中是否有可用工具（如托盘边缘可作为杠杆、手机用于照明等）以协助操作。"
  ],
  "estimated_number_of_trips": "few",
  "efficiency_consideration": "避免重复无效搜索；优先利用现有视野中的物体辅助操作或确认任务状态。",
  "safety_or_stability_consideration": "在尝试移动沙发或使用工具时，确保不会损坏家具或造成自身不稳定。托盘等物品可作为临时支撑但需谨慎使用。",
  "uncertainty_or_missing_information": "遥控器当前位置未知；新观察中未显示其存在，可能已被移走、隐藏于其他区域或仍在沙发下但不可见。",
  "reason": "结合O0和O1，原始任务目标（取出遥控器）尚未明确完成。由于新视野中无遥控器迹象，需重新检查原位置并评估是否需要工具辅助；若仍无法获取，则考虑扩大搜索范围或确认任务状态。"
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
  "task_understanding": "需要从沙发下方取出一个遥控器，该区域可能狭窄且光线不足，机械臂需谨慎伸入以避免碰撞或卡住。",
  "plan": [
    "移动至沙发前方，确认遥控器在沙发底部的具体位置。",
    "将机械臂缓慢伸入沙发下方，定位遥控器并夹取。",
    "收回机械臂，确保遥控器稳定握持后，将其放置于安全可见的位置（如茶几或桌面）。",
    "若首次尝试未成功，可调整角度或使用辅助工具（如有）再次尝试。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "直接操作效率最高，无需额外工具或多次往返；但需确保机械臂可达性和夹爪稳定性。",
  "safety_or_stability_consideration": "沙发下方空间狭窄，伸入时需避免机械臂与沙发结构碰撞导致损坏或自身失稳；夹取后应确认遥控器牢固握持再移动。",
  "uncertainty_or_missing_information": "图像中未明确显示遥控器的具体位置和形状，可能被遮挡或位于深部区域，影响首次操作成功率。",
  "reason": "基于当前环境观察，沙发下方存在可操作空间且目标物体（遥控器）体积较小、适合单次夹取。直接使用机械臂伸入是合理选择；若无法触及，则需考虑调整姿态或借助工具，但目前无明显辅助物可用。优先尝试直接操作以减少复杂性与风险。"
}
```

### Final Raw Response

```json
{
  "task_understanding": "根据O0和O1的综合信息，遥控器位于沙发下方（O0），而当前观察O1显示的是一个厨房台面场景，包含烤盘、台灯、手机等物体，但未见遥控器或沙发相关区域。因此，任务目标位置仍为沙发下方，当前环境不直接提供有用工具或辅助物。",
  "plan": [
    "返回至沙发前方区域，确认遥控器在沙发底部的具体位置。",
    "将机械臂缓慢伸入沙发下方，定位遥控器并夹取。",
    "收回机械臂，确保遥控器稳定握持后，将其放置于安全可见的位置（如茶几或桌面）。",
    "若首次尝试未成功，可调整角度或使用辅助工具（如有）再次尝试。"
  ],
  "estimated_number_of_trips": "single",
  "efficiency_consideration": "当前观察O1中无可用辅助物提升效率；任务仍需回到原始目标位置执行直接操作，因此计划不变。",
  "safety_or_stability_consideration": "沙发下方空间狭窄，伸入时需避免机械臂与沙发结构碰撞导致损坏或自身失稳；夹取后应确认遥控器牢固握持再移动。",
  "uncertainty_or_missing_information": "O1未提供关于遥控器位置的任何新信息，且当前场景与任务目标区域无关。遥控器是否仍在原位、是否有遮挡物仍不确定。",
  "reason": "尽管获得了新的观察O1，但其内容为厨房台面环境，并不包含沙发或遥控器相关元素，因此无法用于辅助任务执行。需继续聚焦于原始目标位置（沙发下方），并按原有计划直接操作。当前无可用工具或信息改变策略，故维持原计划不变。"
}
```

