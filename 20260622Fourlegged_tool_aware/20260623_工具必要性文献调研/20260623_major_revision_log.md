# 20260623 Major Revision Log

## 1. Scope

- Revision target: weekend advisor presentation.
- Main-line filter: only 2025–2026 papers/projects.
- Files modified successfully:
  - `20260623_领域地图与命题.md`
  - `20260623_论文卡片.md`
  - `20260623_Baseline与实验.md`
  - `20260623_PPT大纲.md`
  - `20260623_总结.md`
  - `20260623_可复用Baseline与Idea迁移.md`
  - `20260623_论文索引.csv`
- Failed modifications: none.

## 2. Removed From the Main Line

The following pre-2025 papers/projects were removed from literature maps, cards, baselines, experiments, PPT, reading priorities and advisor questions:

- OpenVLA (2024)
- Octo (2024)
- AHA / FailGen (2024)
- RT-Affordance (2024)
- RoboTool / Creative Robot Tool Use with LLMs (2023)
- UMI on Legs (2024)
- RoboDuet original paper (2024)
- Gen2Act (2024)
- CoPa (2024)
- Open X-Embodiment / RT-X (2023)
- All older agent/skill-library references

AffordGrasp was retained because its current paper is dated 2025. It remains conceptual because a runnable official release was not found.

## 3. Retained 2025–2026 Works

### AIGC / world model

- Video Generators are Robot Policies / Video Policy (2025)
- DreamGen / GR00T-Dreams (2025)
- Unified World Models (2025)
- EMMA: Generative Visual Transfer (2025)
- NVIDIA Cosmos-Predict2 current 2025 project

### Simulation / synthetic data

- RoboTwin 2.0 (2025)
- MobileManiBench (2026)

### VLM / VLA / foundation models

- Qwen3-VL (2025)
- π0.5 / current openpi (2025)
- GR00T N1 / current Isaac-GR00T N1.7 (2025–2026)
- Gemini Robotics / Robotics-ER (2025)

### Mobile / quadruped manipulation

- MoManipVLA (2025)
- Human2LocoMan (2025)
- MLM (2025)
- SLIM (2025)
- SG-VLA (2026)

### Tool use / affordance / counterfactual

- Physics-Conditioned Grasping for Stable Tool Use (2025)
- Robustness-Aware Tool Selection and Manipulation Planning (2025 paper / ICRA 2026)
- AffordGrasp (2025)
- Learning Precise Affordances from Egocentric Videos / Aff-Grasp (2025)
- Creative Robot Tool Use by Counterfactual Reasoning (2026)
- Guardian (2025)
- Dream2Fix (2026)

## 4. Newly Added 2025–2026 Works

- Qwen3-VL
- RoboTwin 2.0
- MobileManiBench
- Guardian
- Human2LocoMan
- MLM
- SLIM
- SG-VLA
- Current GR00T N1.7 project status
- Current Cosmos-Predict2 project status

## 5. Runnable / Near-Runnable Baselines

| Baseline | Evidence | Assigned role |
|---|---|---|
| Qwen3-VL | GitHub, Hugging Face weights, inference/SFT instructions | First-stage four-mode reasoning |
| RoboTwin 2.0 | MIT code, task generator, collection scripts, HF data | Simulation data-generation reference |
| Aff-Grasp | MIT code, HF data and model | Affordance-only baseline |
| GR00T N1.7 | Official code, HF weights, demo and finetuning process | Smoke test now; later action baseline |
| π0.5/openpi | Official code, checkpoints and data conversion | Later strong policy baseline |
| UWM | Public code/checkpoints/scripts | Later world-model baseline |
| Video Policy | Public code/checkpoints/dataset/training configs | Later generated-video/action baseline |
| DreamGen | Public NVIDIA pipeline | Later AIGC/pseudo-action baseline |
| Human2LocoMan | Project links code/data/models | Later quadruped execution/data baseline |

## 6. Conceptual-Only Baselines / Idea Sources

Public runnable code/data was not found after search for:

- Creative Robot Tool Use by Counterfactual Reasoning
- Robustness-Aware Tool Selection
- Physics-Conditioned Grasping / iTuP
- Guardian
- Dream2Fix
- MoManipVLA
- SG-VLA
- MLM

These are now labeled conceptual or limitation sources, not reproducible baselines.

Gemini Robotics is labeled restricted/closed and is used only as a capability reference.

## 7. Experiments Now Anchored to Existing Baselines

### First stage

- Qwen3-VL 2025 zero-shot four-mode reasoning.
- Qwen3-VL independent versus matched-counterfactual few-shot/SFT.
- Aff-Grasp 2025 affordance-only input.
- RoboTwin 2.0 2025 data-generator smoke test or project Isaac Sim extension.
- GR00T N1.7 official inference smoke test.

### Later stage

- π0.5/openpi or GR00T mode-conditioned action policy.
- UWM / Video Policy future-model objective comparison.
- DreamGen/Cosmos filtered versus unfiltered AIGC augmentation.
- Human2LocoMan-based quadruped observation/action interface.

Any project-specific classifier is explicitly labeled `custom sanity check, not existing baseline`.

## 8. Moved Out or Deleted

- Pre-2025 papers and baselines: deleted from all main materials.
- Agent + skill-library line: deleted.
- Generic embodied-AI survey content: deleted.
- Full WBC as a first-stage contribution: deleted.
- AIGC-as-action-label claim: deleted.
- OpenVLA/Octo/AHA-derived first-stage experiments: replaced by Qwen3-VL/RoboTwin/Aff-Grasp/GR00T baselines.
- No separate backup file was created; this log records removals.

## 9. Remaining Information Gaps

- MobileManiBench public code/data release was not found after search.
- Guardian public code and benchmark download were not found after search.
- Dream2Fix code, weights and 120k-pair download were not found after search.
- MoManipVLA and SG-VLA official code were not found after search.
- Robustness-aware tool selection, iTuP and counterfactual tool-use implementations were not found.
- AffordGrasp project page lists “Code” but no runnable release was resolved.
- Exact hardware requirements for UWM, DreamGen, Aff-Grasp and Human2LocoMan need local installation confirmation.
- RoboTwin 2.0 is bimanual/tabletop; effort to add a quadruped-arm embodiment remains unknown.

## 10. Quality Check

- Main-index years: only 2025 and 2026.
- Main paper cards: 20, all dated 2025–2026.
- PPT slides: 18.
- Pre-2025 named baselines in main content: none, except explicit statements saying they were removed.
- Each proposed first-stage experiment names an existing 2025–2026 baseline.
- AIGC is positioned as filtered supporting data, not default action supervision.
- Mobile/quadruped papers are used for setting/execution, not tool-awareness novelty.
