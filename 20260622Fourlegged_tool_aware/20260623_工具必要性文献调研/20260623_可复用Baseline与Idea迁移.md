# 2025–2026 可复用 Baseline 与 Idea 迁移

## 1. Executive Summary

- **直接可复用：** Qwen3-VL inference/prompt/SFT、RoboTwin 2.0 data generation、Aff-Grasp affordance model、GR00T N1.7 official demo。
- **可适配但非本周主实验：** π0.5/openpi、GR00T finetuning、UWM、Video Policy、DreamGen、Human2LocoMan。
- **只有概念、不能称为可运行 baseline：** counterfactual tool use、robustness-aware tool selection、iTuP、Guardian、Dream2Fix、MoManipVLA、SG-VLA。
- **closed reference：** Gemini Robotics / Robotics-ER。
- 最适合迁移的 idea 是：tool-property intervention、generated-data verification、spatial auxiliary supervision、affordance-only input、simulation-in-the-loop task generation。
- 本周不训练通用 VLA/world model，不做完整 WBC，不采用 generated action labels。

## 2. Baseline Reusability Matrix

| Baseline/project | Year | Paper/project | Code | Dataset | Weights | Training process | Input | Output | Directly runnable? | First-stage use | Later-stage use | Relevance | Main limitation | Priority |
|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen3-VL | 2025 | [Paper](https://arxiv.org/abs/2511.21631) | [GitHub](https://github.com/QwenLM/Qwen3-VL) | Project-specific evaluation | HF 2B–235B | Transformers / SFT code | Image/video+text | Structured text | Yes | Four-mode reasoning | State-conditioned VLM | Tool-aware reasoning | Not an action policy | P0 |
| RoboTwin 2.0 | 2025 | [Paper](https://arxiv.org/abs/2506.18088) | [GitHub](https://github.com/robotwin-Platform/robotwin) | 100k+ HF trajectories | Policy integrations | Task config + collect scripts | Scene/task config | Multimodal trajectories | Yes | Data-generator smoke test | Synthetic training | AIGC+sim data | Bimanual tabletop | P0 |
| Aff-Grasp | 2025 | [ICCV](https://openaccess.thecvf.com/content/ICCV2025/html/Li_Learning_Precise_Affordances_from_Egocentric_Videos_for_Robotic_Manipulation_ICCV_2025_paper.html) | [GitHub](https://github.com/Reagan1311/Aff-Grasp) | HF data | HF model | Public modules | RGB/video | Affordance masks | Partial | Affordance-only baseline | Tool feature input | Tool function | No reachability/necessity | P0 |
| GR00T N1.7 | 2025–26 | [N1 paper](https://arxiv.org/abs/2503.14734) | [GitHub](https://github.com/NVIDIA/Isaac-GR00T) | LeRobot/demo | HF N1.7 | Finetune scripts | Image+state+language | Actions | Demo yes | Smoke test only | Full policy baseline | Robot foundation model | 40GB recommended tuning | P0/P1 |
| π0.5/openpi | 2025 | [Paper](https://arxiv.org/abs/2504.16054) | [GitHub](https://github.com/Physical-Intelligence/openpi) | LeRobot/DROID/LIBERO | Public configs/checkpoints | LoRA/full scripts | Images+state+text | Action chunks | Partial | No | Strong policy | VLA baseline | Embodiment mapping | P1 |
| Video Policy | 2025 | [Paper](https://arxiv.org/abs/2508.00795) | [GitHub](https://github.com/cvlab-columbia/videopolicy) | RoboCasa release | Released zip | Stage1/2/joint | Robot video | Future video+actions | Eval yes | No | AIGC/action baseline | Generated-video policy | 8×80GB reference training | P1 |
| UWM | 2025 | [Paper](https://arxiv.org/abs/2504.02792) | [GitHub](https://github.com/WEIRDLabUW/unified-world-model) | LIBERO/DROID | Released | Public scripts | Video/action | Video/action | Partial | No | Future baseline | World model | Heavy; no necessity | P1 |
| DreamGen | 2025 | [Paper](https://arxiv.org/abs/2505.12705) | [GitHub](https://github.com/nvidia/GR00T-dreams) | Demo/external | Dependent assets | World model+IDM | Frame+text | Video+pseudo-action | Partial | No | AIGC baseline | Data expansion | New embodiment IDM | P1 |
| Human2LocoMan | 2025 | [Project](https://human2bots.github.io/) | Linked | Open human/robot data | Linked models | Two-stage pretrain/finetune | Vision+state | Quadruped actions | Partial | Setting/data reference | Execution baseline | Four-legged arm | No tool necessity | P1 |
| Cosmos-Predict2 | 2025 | [Project](https://github.com/nvidia-cosmos/cosmos-predict2) | Yes, archived | External | HF collection | Inference/post-train | Image/video/text | Video | Partial | No | Visual generator | AIGC | Archived/heavy/license | P2 |
| Gemini Robotics | 2025 | [Report](https://arxiv.org/abs/2503.20020) | Closed | Closed | Closed | Restricted | Multimodal | Reasoning/actions | No | Reported reference | No reproducible test | Capability reference | Restricted | P2 |
| Tool-use papers without release | 2025–26 | iTuP / Robustness / Counterfactual Tool Use | Not found | Not found | Not found | Not found | Tool/task state | Tool/grasp/score | No | Motivation | Reimplementation only | Tool-state novelty | No code | P0/P2 |
| Guardian / Dream2Fix | 2025–26 | Failure papers | Not found | Claimed only | Not found | Paper description | Success/failure data | Failure/recovery | No | Idea only | Filtering/data study | Negative data | No release | P2 |
| MoManipVLA / SG-VLA | 2025–26 | Mobile VLA papers | Not found | Not found | Not found | Paper description | Mobile observations | Base-arm actions | No | No | Conceptual mobile baseline | Mobile setting | No release | P1/P2 |

## 3. Baseline Cards

### P0: Qwen3-VL Four-Mode Reasoning

- **Runnable:** Yes.
- **Exact use:** Same image/state cases; force JSON four-mode output.
- **Modification:** Prompt/schema and optional LoRA only.
- **Fair test:** Mature 2025 VLM reasoning before policy integration.
- **Cannot test:** Action feasibility.

### P0: RoboTwin 2.0 Data Generator

- **Runnable:** Yes on supported embodiments.
- **Exact use:** Run official collection; assess whether task configs can support matched tool-state variants.
- **Modification:** Project-specific tool states and labels.
- **Fair test:** Existing 2025 simulation generation pipeline.
- **Cannot test:** Quadruped tool-aware behavior without substantial extension.

### P0: Aff-Grasp

- **Runnable:** Partial; code/data/weights available.
- **Exact use:** Produce functional masks; feed only affordance information to the same Qwen3-VL decision prompt.
- **Fair test:** Whether affordance alone explains gains.
- **Cannot test:** Availability/reachability.

### P0/P1: GR00T N1.7

- **Runnable:** Official demo yes; custom quadruped finetuning partial.
- **Exact use now:** Install/inference smoke test and data-schema feasibility.
- **Later:** Mode-conditioned action policy.
- **Cannot test now:** Tool necessity without new labels.

### P1: π0.5/openpi

- **Runnable:** Supported examples yes.
- **Exact later use:** Convert dataset to LeRobot; add mode token or hierarchical conditioning.
- **Blocker:** GPU and embodiment adaptation.

### P1: UWM / Video Policy / DreamGen

- **Runnable:** Released evaluation pipelines; retraining is expensive.
- **Exact later use:** Generate/predict candidate futures, compare unfiltered/filtered data, or attach mode evaluation.
- **Blocker:** Video-model compute and action/label validity.

### P1: Human2LocoMan

- **Runnable:** Code/data/models linked.
- **Exact later use:** Quadruped observation/action interface and execution baseline.
- **Blocker:** LocoMan-specific embodiment; no tool necessity labels.

### Conceptual only

- Counterfactual Tool Use: targeted physical intervention。
- Robustness-Aware Tool Selection: robustness/suitability score。
- Physics-Conditioned Grasping: tool usability/action coupling。
- Guardian: procedural planning/execution failure taxonomy。
- Dream2Fix: semantic/visual/kinematic verification。
- MoManipVLA: base-arm feasibility separation。
- SG-VLA: spatial auxiliary supervision。

这些工作没有足够公开实现，不能写成“可复现 baseline”。

## 4. Idea Transfer Table

| Source 2025–2026 work | Transferable idea | Target baseline | What to modify | Project failure mode addressed | Minimal test | Risk |
|---|---|---|---|---|---|---|
| Counterfactual Tool Use 2026 | Single-property intervention | RoboTwin/Isaac Sim → Qwen3-VL | Change one of reachable/usable/suitable/direct-feasible | Category/appearance shortcut | Random scenes vs matched pairs | Simulation labels may be trivial |
| Guardian 2025 | Procedural failure taxonomy | RoboTwin task generator | Convert planning failures to tool-state/mode contradictions | Lack of negatives | Independent negatives vs structured perturbations | No public code |
| Dream2Fix 2026 | Structured generated-data verification | DreamGen/Cosmos visual augmentation | Check semantic, tool-state, geometry and label consistency | AIGC changes labels | No filter vs generic vs state filter | Reimplementation |
| Aff-Grasp 2025 | Functional mask | Qwen3-VL | Add affordance mask/description without reachability | Affordance confused with necessity | Image-only vs affordance-only vs full state | Mask domain shift |
| Robustness-Aware Tool Selection 2025 | Robustness score | Later GR00T/openpi selector | Score direct and each tool candidate | Suitable but fragile tool | Suitability-only vs robustness-aware | No released code |
| Physics-Conditioned Grasping 2025 | Tool usability from interaction physics | Later policy state | Add stability/usability field | Correct tool but unstable grasp | Availability vs usability | Physics labels costly |
| SG-VLA 2026 | Auxiliary spatial/state decoders | GR00T/openpi | Add reachability/base pose/tool-state auxiliary targets | Image-only latent ignores geometry | Action-only vs auxiliary supervision | No released implementation |
| MoManipVLA 2025 | Separate semantic waypoint and mobile feasibility | Later execution | Mode `reposition` triggers base-arm feasibility layer | Fixed-base action unreachable | No reposition vs feasibility correction | No released code |
| RoboTwin 2.0 2025 | Simulation-in-loop task verification | Project data generator | Reject invalid labels by rollout/planner checks | Incorrect oracle labels | Rule label vs verified rollout label | Platform mismatch |
| DreamGen 2025 | Generated visual trajectories + alignment scoring | AIGC data study | Use visual generation only before pseudo-actions | Visual diversity shortage | Original sim vs filtered generated | Embodiment drift |
| UWM 2025 | Separate video/action objectives | Later VLA | Compare action-only vs video+action under same labels | Claim that future modeling learns necessity | Objective ablation | Compute |
| Human2LocoMan 2025 | Modular embodiment tokenizers | Later quadruped policy | Keep shared reasoning trunk; adapt quadruped inputs/actions | Cross-embodiment gap | Shared vs embodiment-specific modules | Hardware-specific |

## 5. Final Recommendation

### P0 — 周末必须讲

1. Qwen3-VL：可直接运行的 four-mode reasoning baseline。
2. RoboTwin 2.0：可直接运行的 simulation data-generation reference。
3. GR00T N1.7：当前可运行 robot foundation model，但本周只做 smoke test。
4. Aff-Grasp：可复用 affordance-only baseline。
5. 三篇工具核心：iTuP、robustness-aware selection、counterfactual tool use；只作 motivation/idea。
6. Human2LocoMan：四足臂 setting 和公开数据/模型 reference。

### P1 — 后续论文 baseline

- π0.5/openpi；
- GR00T finetuning；
- UWM、Video Policy、DreamGen；
- MoManipVLA、SG-VLA；
- AIGC filtered versus unfiltered；
- quadruped execution。

### P2 — Background / limitation

- Gemini Robotics：closed reference；
- Guardian、Dream2Fix：negative-data/filtering idea；
- Cosmos-Predict2：重型生成器；
- MLM、MobileManiBench：execution/benchmark background。

### Remove

- 所有 pre-2025 工作；
- closed generic video services；
- pure agent/skill baselines；
- 自定义小模型作为“main baseline”。
