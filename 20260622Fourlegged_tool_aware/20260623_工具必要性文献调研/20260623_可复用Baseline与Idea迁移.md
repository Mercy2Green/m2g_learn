# 2025–2026 可复用 Baseline 与 Idea 迁移

## 1. Executive Summary

- GET-USE 是当前最接近三元交集的 L3 工作，但没有公开实现，也不是四足/necessity baseline。
- SAGA 是 mobile/quadruped+affordance 的 L2C 证据；SLIM/MobileManiBench/SG-VLA 是 mobile+sim 的 L2A 证据。
- RIGVid、counterfactual tool use、iTuP、robustness-aware selection 是 AIGC/sim+tool 的 L2B 证据。
- 本周可运行资源仍是 Qwen3-VL、RoboTwin 2.0、Aff-Grasp 和 GR00T demo；它们分别只覆盖部分 ingredient。
- 没有公开 baseline 直接输出四足臂 `direct/use_tool/reposition/abort`。
- 本周应做“现有 baseline + project-specific intersection data”，而不是声称存在完整现成 baseline。

## 2. Intersection Audit

| Work | AIGC/sim? | Mobile/quadruped? | Tool-aware? | Intersection Level | Directly runnable? | Can be baseline? | If not, what role? | Why relevant |
|---|---|---|---|---|---|---|---|---|
| GET-USE | Yes | Yes | Yes | L3 | No | Conceptual | Main intersection motivation | Closest full intersection |
| SAGA | No | Yes | Yes | L2C | No | Conceptual | Mobile affordance method | Quadruped structured affordance |
| SLIM | Yes | Yes | No | L2A | Partial | Setting baseline | Sim-to-real mobile evidence | Quadruped modes/reposition |
| MobileManiBench | Yes | Yes | No | L2A | No release found | Benchmark reference | Mobile simulation schema | Rich state/action annotations |
| SG-VLA | Yes | Yes | No | L2A | No | Conceptual | Spatial supervision idea | Base-arm state grounding |
| MoManipVLA | Yes | Yes | Reachability adjacent | L2A | No | Conceptual | Reposition interface | Mobile feasibility |
| RAKOMO | Yes | Yes | Reachability adjacent | L2A | No | Conceptual | Reachability method | Tool-tip/base feasibility idea |
| Counterfactual Tool Use | Yes | No | Yes | L2B | No | Conceptual | Intervention idea | Tool-property causal pairs |
| Robustness-Aware Selection | Yes | No | Yes | L2B | No | Conceptual | Suitability motivation | Tool robustness |
| iTuP | Yes | No | Yes | L2B | No | Conceptual | Tool action motivation | Tool physics changes action |
| RobotSmith | Yes | No | Yes | L2B | No | Conceptual | Simulation tool design | Physics verification |
| RIGVid | Yes | No | Yes, action only | L2B | No code found | Conceptual | AIGC+tool action evidence | Generated videos for wiping/mixing |
| RoboTwin 2.0 | Yes | No | No | L1A | Yes | Data baseline | — | Runnable simulation generator |
| Aff-Grasp | No | No | Yes | L1C | Partial | Affordance baseline | — | Runnable tool-function input |
| Human2LocoMan | No | Yes | No | L1B | Partial | Later execution/data | — | Open quadruped interface |
| Qwen3-VL | No | No | No | Remove | Yes | Reasoning baseline | — | Runnable four-mode evaluator |
| GR00T N1.7 | Synthetic pretraining | No | No | L1A | Demo yes | Later policy | — | Runnable foundation policy |
| DreamGen/Video Policy/UWM | Yes | No | No | L1A | Partial | Later AIGC policy | — | Generated data/future baseline |

### Audit conclusion

存在一篇稀疏 L3（GET-USE），但不存在可直接运行且覆盖四足臂、AIGC/sim pairs、tool necessity 和四类 mode 的 L3 baseline。当前项目 gap 是“把三个 ingredient 闭合”，不是宣称任何单线为空白。

## 3. Reusable Baselines

### Qwen3-VL — P0 Runnable

- **Intersection:** none; baseline only。
- **Input/output:** image/video+prompt → JSON mode/reasoning。
- **This week:** zero-shot、independent few-shot、matched-pair few-shot、wrong-state。
- **Cannot prove:** mobile action feasibility。

### RoboTwin 2.0 — P0 Runnable Data Reference

- **Intersection:** L1A。
- **Input/output:** task/scene config → multimodal simulation trajectories。
- **This week:** run data collection；estimate cost of adding tool-state variants。
- **Cannot prove:** mobile/quadruped tool-aware。

### Aff-Grasp — P0 Runnable Affordance Reference

- **Intersection:** L1C。
- **Input/output:** RGB/video → functional/graspable masks。
- **This week:** affordance-only prompt/input。
- **Cannot prove:** necessity/reposition。

### GR00T N1.7 — P0 Smoke Test / P1 Policy

- **Intersection:** L1A due synthetic foundation pretraining。
- **Input/output:** image+state+language → actions。
- **This week:** official demo/schema smoke test only。
- **Cannot prove:** tool-aware mode without new data/target。

### Human2LocoMan — P1 Mobile Execution

- **Intersection:** L1B。
- **Input/output:** quadruped vision/state → actions。
- **Use:** observation/action schema and later execution。
- **Cannot prove:** AIGC/sim or tool necessity。

## 4. Idea Transfer Table

| Source work | Transferable idea | Target baseline | What to modify | Failure mode addressed | Minimal test | Risk |
|---|---|---|---|---|---|---|
| GET-USE | Simulated embodiment extension and absent-best-tool cases | RoboTwin/Isaac + Qwen3-VL | Generate multiple tools, missing optimal tool, mobile pose variants | Always assumes one valid tool | best present vs absent vs direct feasible | No code; mobile robot differs |
| SAGA | Structured 3D affordance input | GR00T/Qwen3-VL later | Add tool functional heatmap/state separate from RGB | Global pixels hide function | image vs affordance vs full state | No release |
| SLIM | Hierarchical mobile modes | Four-mode label schema | Reuse search/approach/reposition structure; insert tool decision | Flat policy conflates locomotion/manipulation | no reposition vs explicit reposition | Not tool-specific |
| MobileManiBench | Rich mobile simulation annotations | Project Isaac Sim | Record multi-view RGB-D-segmentation, robot/object state | Missing state supervision | RGB only vs RGB+state | Release unconfirmed |
| SG-VLA | Auxiliary spatial decoders | GR00T/openpi later | Predict base pose, tool relative pose, reachability, affordance | Action latent ignores geometry | action-only vs auxiliaries | No code |
| MoManipVLA | Separate semantic waypoint and mobile feasibility | Later execution | Trigger reposition feasibility after mode output | Fixed-base action unreachable | no correction vs base-arm correction | No code |
| RAKOMO | Learned reachability margin | Tool-state estimator | Define tool-tip/base-arm reachability score | Reachability reduced to distance | distance vs reachability margin | Planning-heavy |
| Counterfactual Tool Use | Targeted physical interventions | Simulation pair generator | Change one tool property per pair | Appearance shortcuts | random vs targeted pairs | Physics design |
| Robustness-Aware Selection | Suitability/robustness score | Later selector | Score direct action and each tool | Semantically suitable but fragile | suitability vs robustness | No code |
| iTuP | Task-conditioned tool usability | Later policy state | Add wrench/stability field | Tool available but unusable | availability vs usability | Label cost |
| RIGVid | Generated video filtering + 6D retargeting | AIGC extension | Initially reuse filter concept only | Generated video violates task | no filter vs task/state filter | No code |
| Dream2Fix | Semantic/visual/kinematic verifier | DreamGen/Cosmos data | Verify tool state and mode label preservation | AIGC label corruption | generic vs structured filter | Reimplementation |
| Aff-Grasp | Functional mask | Qwen3-VL | Add affordance-only input | Confusing affordance with necessity | affordance-only vs full state | Domain shift |

## 5. Priority

### P0-Intersection Core

- GET-USE。
- SAGA as closest L2C。

### P0-Mobile-Sim Core

- SLIM、MobileManiBench、SG-VLA、MoManipVLA、RAKOMO。

### P0-Tool-Sim Core

- Counterfactual Tool Use、Robustness-Aware Selection、iTuP、RobotSmith、RIGVid。

### P0-Runnable Baseline

- Qwen3-VL、RoboTwin 2.0、Aff-Grasp、GR00T demo。

### P1-Later AIGC / Policy

- π0.5/openpi、GR00T finetuning、UWM、Video Policy、DreamGen、Cosmos、Human2LocoMan。
