# Intersection Focus Revision Log

## 1. Original Problem

上一版虽然限制到 2025–2026，但组织方式仍容易变成：

- mobile manipulation survey；
- tool-use survey；
- AIGC/world-model survey。

这些单线工作不能直接回答导师关心的 `AIGC/sim × quadruped/mobile × tool-aware`。

## 2. New Repair

所有工作重新按三个维度审计：

1. AIGC / simulation data；
2. mobile / quadruped embodiment；
3. tool-aware / tool-use / affordance / reachability。

新增字段：

- Intersection Level；
- Platform Type；
- Data Type；
- Tool-Aware Role；
- Robot Platform；
- Weekend Role；
- Should Read Before Weekend。

## 3. Search Queries Executed

第一层三元/双重交集检索包括：

- `2025 generated video mobile manipulation tool use robot`
- `2025 AIGC mobile manipulation tool use robot`
- `2025 synthetic video mobile manipulation tool affordance`
- `2025 world model mobile manipulation tool use`
- `2026 generated video mobile manipulation tool use`
- `2026 world model mobile manipulation tool-aware robot`
- `2025 simulation data quadruped arm tool use`
- `2025 Isaac Sim mobile manipulation tool use`
- `2025 Isaac Lab quadruped arm tool use`
- `2026 Isaac Sim mobile manipulation tool-aware`
- `2025 mobile manipulation tool necessity`
- `2025 mobile robot tool selection reachability`
- `2025 mobile manipulation tool reachability`
- `2025 quadruped manipulation tool reachability`
- `2026 mobile manipulation tool state`
- `2025 direct manipulation versus tool use robot`

第二层仅在交集不足时搜索：

- generated-video robot manipulation tool use；
- simulation/mobile manipulation benchmarks；
- fixed-base tool-use simulation；
- quadruped reachability and structured affordance。

## 4. Added or Reclassified Works

### Added

- GET-USE (2025) — L3。
- SAGA (2025) — L2C。
- RAKOMO (2025) — L2A。
- RIGVid (2025) — L2B。
- RobotSmith (2025) — L2B。

### Reclassified

- RoboTwin 2.0 → L1A, simulation generator only。
- Qwen3-VL → not intersection evidence; runnable baseline。
- GR00T → L1A due synthetic foundation pretraining; later policy。
- Aff-Grasp → L1C affordance-only。
- Human2LocoMan → L1B quadruped-only。
- SLIM / MobileManiBench / SG-VLA / MoManipVLA → L2A。
- Counterfactual Tool Use / Robustness-Aware / iTuP → L2B。

## 5. Downgraded Works

- General AIGC projects are no longer described as tool-aware.
- Mobile/quadruped papers are no longer treated as full related-work evidence.
- Fixed-base tool papers are no longer treated as mobile baselines.
- Qwen3-VL and GR00T are explicitly baseline resources, not mobile/tool literature.
- No-code works are conceptual motivation only.

## 6. L3 Direct Evidence

Found:

- GET-USE: simulation + bimanual mobile manipulation + generalized tool usage。

Not found:

- runnable L3 code/data；
- quadruped-arm L3；
- AIGC-video + mobile + tool necessity；
- direct/use_tool/reposition/abort four-mode benchmark。

Gap statement:

> Direct L3 evidence is sparse. Existing work does not provide a runnable quadruped-arm pipeline that combines verified AIGC/simulation counterfactual data with tool necessity and mobile mode decisions.

## 7. PPT Structure Change

The PPT now:

1. defines the three-way intersection；
2. audits L3/L2/L1 coverage；
3. explains each ingredient and its missing dimension；
4. presents GET-USE and SAGA as closest evidence；
5. separates runnable baselines from intersection literature；
6. derives first-stage tests from existing projects；
7. ends with advisor decisions。

## 8. Remaining Manual Confirmation

- GET-USE code/data release status。
- SAGA code/data release status。
- RIGVid code/data release status。
- MobileManiBench release status。
- Whether RoboTwin 2.0 can support a quadruped-arm embodiment without major asset work。
- Whether Aff-Grasp dependencies can run in the available environment。
- Available GPU for Qwen3-VL and GR00T smoke tests。
- Whether the advisor accepts mobile bimanual GET-USE as the closest L3 motivation despite not being quadruped。

## 9. Final Consistency Fix on 2026-06-24

- Re-sorted `20260623_论文索引.csv` by required weekend priority order: P0-Intersection Core → P0-Mobile-Sim Core → P0-Tool-Sim Core → P0-Runnable Baseline → P1-Later AIGC / Policy → Background / Remove。
- Moved SAGA next to GET-USE under P0-Intersection Core because it is closest mobile/quadruped + tool-affordance evidence, but explicitly lacks AIGC/simulation and necessity。
- Moved Human2LocoMan back into the P0-Mobile-Sim/Core mobile embodiment block; it remains L1B because it lacks AIGC/sim and tool-awareness。
- Rechecked CSV required fields, year filter, PPT slide count, and reading-group count。
