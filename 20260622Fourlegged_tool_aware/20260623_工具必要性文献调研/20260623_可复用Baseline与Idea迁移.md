# 可复用 Baseline 与 Idea 迁移总结

核验日期：2026-06-23。  
判断标准：只有官方代码、数据/示例、checkpoint 或明确训练流程可访问时，才评为 Level A/B；搜索后未找到公开实现的工作明确标记为 `Not found after search`。

## 1. Executive Summary

1. **本周最值得直接使用的是轻量 image/language classifier、冻结视觉语言表示 + mode head、结构化 tool-state head 和 paired counterfactual loss；不是完整 VLA 微调。**
2. 在现成机器人模型中，**Octo-Small 最接近可直接改造的 backbone**：MIT 代码、27M checkpoint、`head_only` finetuning 和 debug dataset 均公开。
3. **OpenVLA、openpi π0/π0.5、Isaac GR00T 均有代码、权重和训练流程，但数据格式与显存成本使其更适合后续完整论文。**
4. **Open X-Embodiment/RT-1-X 更适合作为数据接口和通用 policy reference，不适合直接做四类 mode classifier。**
5. affordance 路线中，**Aff-Grasp 有代码、数据和模型权重；RT-Affordance 与 AffordGrasp 未找到可直接运行的官方训练代码。**
6. **AHA/FailGen 是最可直接迁移的数据生成实现**：公开了 RLBench/CoppeliaSim 失败扰动脚本；不需要复现其 13B VLM 训练。
7. **Dream2Fix、counterfactual tool-use、robustness-aware selection 和 iTuP 当前更适合作为 idea source**；没有找到足够公开实现支持直接复现。
8. AIGC/world-model 中，UWM、Video Policy、DreamGen、Cosmos 均有代码，但训练成本和数据适配显著；**只应作为 Claim A 成立后的后续对照**。
9. UMI on Legs 和 RoboDuet 的执行代码公开，但依赖 Isaac Gym、特定四足/机械臂和部署栈；**只进入后续 WBC/trajectory 阶段**。
10. Go：本周跑 P0 的四个 mode baselines，并复用 FailGen 的“程序化扰动”设计。No-go：现在微调整个 VLA、训练 world model、做完整 WBC 或让 AIGC 成为主实验。

## 2. Baseline Reusability Matrix

| Baseline | Level | Code | Data | Weights | Training scripts | Input/Output compatibility | First-stage use | Later-stage use | Priority | Main blocker |
|---|---|---|---|---|---|---|---|---|---|---|
| Lightweight CLIP/SigLIP + mode head | A | Public model libraries | Our matched dataset | Public encoder weights | Simple local head | RGB+text → 4 modes, exact match | Yes | Yes | P0 | Need our labels/data |
| Octo-Small frozen/head-only | A | [GitHub](https://github.com/octo-models/octo) | Debug/OXE/custom adapter | [HF checkpoints](https://huggingface.co/rail-berkeley) | `scripts/finetune.py` | RGB+text → action; replace/readout with mode head | Yes, representation only | Yes | P0 | JAX/custom dataset adapter |
| AHA FailGen data generator | A | [GitHub](https://github.com/NVlabs/AHA) | Generated RLBench failures | Not needed for generator | Public generation commands | Success state → perturbed labeled failure | Yes, idea/code adaptation | Yes | P0 | CoppeliaSim/RLBench setup |
| Aff-Grasp affordance model | A/B | [GitHub](https://github.com/Reagan1311/Aff-Grasp) | [HF data](https://huggingface.co/datasets/Reagan1311/Data_for_Aff-Grasp) | [HF model](https://huggingface.co/Reagan1311/Model_for_Aff-Grasp) | Learning/extraction code | RGB/depth → functional/grasp regions | Partial | Yes | P0 | Heavy dependencies; output is affordance, not mode |
| OpenVLA | B | [GitHub](https://github.com/openvla/openvla) | OXE/RLDS/custom | [HF](https://huggingface.co/openvla/openvla-7b) | LoRA/full scripts | RGB+text → 7-DoF action | No | Yes | P1 | 7B; ≥27 GB LoRA; RLDS adapter |
| openpi π0/π0.5 | B | [GitHub](https://github.com/Physical-Intelligence/openpi) | LeRobot/DROID/LIBERO/custom | Public GCS checkpoints | JAX/PyTorch training | Multi-image+state+text → action chunks | No | Yes | P1 | ≥22.5 GB LoRA; embodiment adaptation |
| Isaac GR00T N1.7 | B | [GitHub](https://github.com/NVIDIA/Isaac-GR00T) | Demo/LeRobot v2/custom | [HF](https://huggingface.co/nvidia/GR00T-N1.7-3B) | Finetune/inference scripts | Images+state+language → continuous actions | No | Yes | P1 | 40 GB recommended; EA stack |
| Open X-Embodiment / RT-1-X | B | [GitHub](https://github.com/google-deepmind/open_x_embodiment) | RLDS datasets | RT-1-X JAX checkpoint | Inference/data examples | RGB+task → 7D action | Partial, data interface only | Yes | P1 | Large heterogeneous data; old TF/JAX stack |
| UWM | B | [GitHub](https://github.com/WEIRDLabUW/unified-world-model) | LIBERO/Robomimic/DROID | Public LIBERO/DROID checkpoints | Pretrain/finetune scripts | Current/future video+action → action/video | No | Yes | P1 | World-model compute and Zarr conversion |
| Video Policy | B | [GitHub](https://github.com/cvlab-columbia/videopolicy) | Public RoboCasa package | Public checkpoint zip | Stage 1/2/joint scripts | Video observations → video+actions | No | Yes | P1 | Reference training uses 8×80GB GPUs |
| DreamGen / GR00T-Dreams | B | [GitHub](https://github.com/nvidia/GR00T-dreams) | Demo and embodiment-specific pipelines | IDM/world-model dependencies | IDM/GR00T scripts | Initial frame+text → video → pseudo-actions | No | Yes | P1 | Cosmos + IDM + embodiment adaptation |
| Cosmos-Predict2 | B/D | [Archived repo](https://github.com/nvidia-cosmos/cosmos-predict2) | External/custom videos | [HF collection](https://huggingface.co/collections/nvidia/cosmos-predict2) | Inference/post-training | Image/video+text/action → future video | No | Maybe | P2 | Archived; high compute; model license; no necessity labels |
| UMI on Legs | B | [GitHub](https://github.com/real-stanford/umi-on-legs) | Checkpoint/data download in repo docs | WBC checkpoints available | Isaac Gym training/deploy | EE trajectory → quadruped whole-body action | No | Yes | P2 | Specific hardware/network/WBC stack |
| RoboDuet | B | [GitHub](https://github.com/locomanip-duet/RoboDuet) | Simulation environment | Trained run path expected | Isaac Gym RL training | 6D target → coordinated leg/arm action | No | Yes | P2 | Isaac Gym Preview 4; Go1/Go2+ARX5 |
| RT-Affordance | C | Project page only | Not found after search | Not found after search | Not found after search | Image+language → affordance plan → policy | Conceptual affordance-only | Maybe | P1 | No public implementation located |
| AffordGrasp | C | Project page; code link inactive/unresolved | Not found after search | Not found after search | Not found after search | RGB-D+instruction → mask+6D grasp | Conceptual/replace with Aff-Grasp | Maybe | P2 | GPT-4o + AnyGrasp; no runnable release found |
| Counterfactual Tool Use | C | Not found after search | Not found after search | None found | None found | Tool properties → causal suitability/keypoints | Idea only | Maybe | P1 | No public implementation |
| Robustness-Aware Tool Selection | C | Not found after search | Not found after search | None found | None found | Tool/configuration → robustness score/trajectory | No | Maybe | P1 | No public code/data found |
| Physics-Conditioned Grasping / iTuP | C | Not found after search | Not found after search | None found | None found | Tool/trajectory/grasp → physics score | No | Maybe | P1 | No public code/data found |
| RoboTool | C | [Project](https://creative-robotool.github.io/) only | Prompt/task examples not packaged | API model dependent | No official runnable repo found | Language+skills → executable code | Prompt-only conceptual baseline | Yes | P1 | No official code; skill library/hardware coupling |
| Dream2Fix | C | Not found after search | Claimed 120k pairs; download not found | None found | None found | Failure video → type+recovery trajectory | Idea only | Maybe | P1 | No public code/data found |
| MoManipVLA | C | Not found after search | OVMM/public base datasets only | None found | None found | VLA waypoint → base-arm trajectory | No | Conceptual execution baseline | P2 | No official project/code located |
| Gen2Act | C | [Project](https://homangab.github.io/gen2act/) only | Not found after search | Video generator closed/unspecified | Not found after search | Image+text → human video → robot policy | No | Conceptual AIGC baseline | P2 | No code; generator dependency |
| Sora-like closed video service | D | No reusable training code/weights | Closed provider data | Closed | API/product dependent | Prompt/image → video only | No | No | Remove | Closed, unstable access, no action labels |

### Level interpretation

- **Level A — Directly Runnable:** 代码、示例数据/checkpoint 和运行流程齐全；仍可能需要小型 adapter。
- **Level B — Adaptable:** 可运行，但需要明显数据格式、head、embodiment 或算力适配。
- **Level C — Conceptual Baseline Only:** 论文机制有价值，但公开实现不足。
- **Level D — Not Useful Now:** 当前投入与 mode-decision 最小实验不成比例。

## 3. Baseline Cards

# P0 — This week

## Baseline Card: Lightweight CLIP/SigLIP + Mode Head

* **Name / Paper:** Frozen vision-language encoder + lightweight four-way classifier
* **Year / Status:** Implementation baseline; standard open pretrained encoders
* **Project / Code Link:** [Hugging Face Transformers](https://github.com/huggingface/transformers)
* **Dataset Link:** 本项目 IsaacSim matched counterfactual dataset
* **Model Weights:** Public CLIP/SigLIP checkpoints through Hugging Face
* **License / Access restriction:** Depends on selected checkpoint; verify its model card
* **Main task:** Scene/instruction classification
* **Input:** RGB + task instruction; optional structured tool state
* **Output:** `direct / use tool / reposition / abort-recovery`
* **Training / Finetuning command or process:** Freeze encoder; cache image/text embeddings; train 2–3 layer MLP with CE; B2 adds pairwise consistency/ranking loss
* **Hardware requirement:** One consumer GPU; CPU inference is possible after feature caching
* **Can we directly run it?** Yes
* **Can it serve our first-stage mode baseline?** Yes
* **Can it serve later full-policy baseline?** Partial
* **What modification is needed for our project:** Dataset loader, four-mode head, pair IDs and tool-state vector
* **What it can fairly test:** Whether paired supervision and tool state improve mode classification
* **What it cannot test:** Continuous control or closed-loop execution
* **Risk / blocker:** Shortcut learning; handle with hard pairs/group split
* **Priority:** P0

## Baseline Card: Octo-Small Frozen Representation / Head-Only

* **Name / Paper:** Octo: An Open-Source Generalist Robot Policy
* **Year / Status:** 2024 / open-source generalist policy
* **Project / Code Link:** https://github.com/octo-models/octo
* **Dataset Link:** [Open X-Embodiment](https://robotics-transformer-x.github.io/); repo includes debug dataset flow
* **Model Weights:** `hf://rail-berkeley/octo-small-1.5` and Octo-Base on Hugging Face
* **License / Access restriction:** MIT code
* **Main task:** Language/goal-conditioned robot action generation
* **Input:** One or more RGB observations; language or goal image
* **Output:** Diffusion action samples
* **Training / Finetuning command or process:** `python scripts/finetune.py --config.pretrained_path=hf://rail-berkeley/octo-small-1.5`; supports `head_only`, `head_mlp_only`, `full`
* **Hardware requirement:** README reports inference on one RTX 4090; debug finetune is provided
* **Can we directly run it?** Yes
* **Can it serve our first-stage mode baseline?** Yes, if used only as frozen representation/head-only
* **Can it serve later full-policy baseline?** Yes
* **What modification is needed for our project:** Replace/add action readout with four-class mode head; build a small custom dataset adapter
* **What it can fairly test:** Whether robot-pretrained features outperform generic VLM features
* **What it cannot test:** Tool necessity without our matched labels
* **Risk / blocker:** JAX stack and observation schema adaptation
* **Priority:** P0

## Baseline Card: AHA / FailGen

* **Name / Paper:** AHA / FailGen
* **Year / Status:** 2024; ICLR 2025 project release
* **Project / Code Link:** https://github.com/NVlabs/AHA
* **Dataset Link:** Generated through included RLBench scripts; co-training links are in README
* **Model Weights:** Projector/base dependencies linked; full AHA release is not needed here
* **License / Access restriction:** NVIDIA repository license; CoppeliaSim/RLBench have separate terms
* **Main task:** Procedural failure generation and failure reasoning
* **Input:** Successful RLBench demonstrations + failure type
* **Output:** Perturbed failure trajectories and QA labels
* **Training / Finetuning command or process:** Install CoppeliaSim/PyRep/RLBench; run `ex_custom_data_generator.py`; full VLM tuning uses RoboPoint
* **Hardware requirement:** Failure generation needs simulator/GPU modestly; full AHA training reports ~40 h on 8×A100-80GB
* **Can we directly run it?** Yes for FailGen; partial for full AHA
* **Can it serve our first-stage mode baseline?** Yes as data-generation implementation, not as classifier
* **Can it serve later full-policy baseline?** Partial
* **What modification is needed for our project:** Replace keyframe execution perturbations with direct/tool/reachability/availability scene interventions; emit mode labels and pair IDs
* **What it can fairly test:** Programmatic perturbation versus random/unpaired negatives
* **What it cannot test:** Tool necessity without rewriting the failure taxonomy
* **Risk / blocker:** RLBench/CoppeliaSim differs from IsaacSim; port the idea, not necessarily the full environment
* **Priority:** P0

## Baseline Card: Aff-Grasp

* **Name / Paper:** Learning Precise Affordances from Egocentric Videos for Robotic Manipulation / Aff-Grasp
* **Year / Status:** 2025 / ICCV 2025
* **Project / Code Link:** https://github.com/Reagan1311/Aff-Grasp
* **Dataset Link:** https://huggingface.co/datasets/Reagan1311/Data_for_Aff-Grasp
* **Model Weights:** https://huggingface.co/Reagan1311/Model_for_Aff-Grasp
* **License / Access restriction:** MIT code; check licenses of GroundedSAM/ViT-Adapter and source video datasets
* **Main task:** Graspable/functional affordance segmentation and affordance-oriented grasping
* **Input:** RGB/depth or egocentric interaction data
* **Output:** Functional/graspable masks; downstream grasp proposals
* **Training / Finetuning command or process:** `ego2aff` extracts labels; `affordance-learning` trains predictor; exact environment follows component READMEs
* **Hardware requirement:** GPU required; exact benchmark VRAM not stated
* **Can we directly run it?** Partial
* **Can it serve our first-stage mode baseline?** Partial
* **Can it serve later full-policy baseline?** Partial
* **What modification is needed for our project:** Use predicted functional mask/embedding as the only extra feature, then train the same four-mode head
* **What it can fairly test:** Whether affordance information alone explains gains attributed to necessity/tool state
* **What it cannot test:** Reachability, availability, acquisition cost or base reposition by itself
* **Risk / blocker:** Multi-repository dependencies; mask quality may dominate comparison
* **Priority:** P0

# P1 — Later full-paper baselines or high-value idea sources

## Baseline Card: OpenVLA

* **Name / Paper:** OpenVLA
* **Year / Status:** 2024 / open-source 7B VLA
* **Project / Code Link:** https://github.com/openvla/openvla
* **Dataset Link:** [Open X-Embodiment](https://robotics-transformer-x.github.io/); [BridgeData V2](https://rail-berkeley.github.io/bridgedata/)
* **Model Weights:** https://huggingface.co/openvla/openvla-7b
* **License / Access restriction:** MIT code; checkpoint inherits Llama 2 Community License restrictions
* **Main task:** Language-conditioned 7-DoF robot action prediction
* **Input:** RGB + language
* **Output:** Discrete robot action
* **Training / Finetuning command or process:** `vla-scripts/finetune.py`; LoRA, full and custom RLDS/PyTorch dataset options
* **Hardware requirement:** LoRA minimum reported ~27 GB VRAM; example uses A100-80GB; full tuning recommends 8×A100
* **Can we directly run it?** Yes for inference; partial for our data
* **Can it serve our first-stage mode baseline?** No
* **Can it serve later full-policy baseline?** Yes
* **What modification is needed for our project:** Add/copy a mode head from hidden representation or encode modes as action tokens; convert data to RLDS
* **What it can fairly test:** Whether general VLA representation/action training already captures tool-state-dependent decisions
* **What it cannot test:** Necessity without matched labels/interventions
* **Risk / blocker:** Compute and RLDS integration can consume the whole two-week window
* **Priority:** P1

## Baseline Card: openpi π0 / π0.5

* **Name / Paper:** π0 / π0.5 via openpi
* **Year / Status:** Active official open-source release
* **Project / Code Link:** https://github.com/Physical-Intelligence/openpi
* **Dataset Link:** DROID, LIBERO and LeRobot-format custom datasets linked in repo
* **Model Weights:** Public `gs://openpi-assets/checkpoints/pi0_base`, `pi05_base`, DROID/LIBERO experts
* **License / Access restriction:** Apache-2.0 code plus Gemma/base-model terms; inspect checkpoint-specific terms
* **Main task:** Flow-matching/autoregressive VLA action generation
* **Input:** Multi-view images, robot state and prompt
* **Output:** Action chunks
* **Training / Finetuning command or process:** Convert to LeRobot; compute norm stats; run `scripts/train.py` or PyTorch training; examples for LIBERO/ALOHA/UR5
* **Hardware requirement:** Inference >8 GB; LoRA >22.5 GB; full tuning >70 GB
* **Can we directly run it?** Yes on supported examples
* **Can it serve our first-stage mode baseline?** No
* **Can it serve later full-policy baseline?** Yes
* **What modification is needed for our project:** New input/output data config, mode auxiliary head or mode-conditioned action policy
* **What it can fairly test:** Strong modern VLA baseline after Claim A is established
* **What it cannot test:** Tool necessity without project-specific supervision
* **Risk / blocker:** Embodiment mismatch; repository explicitly warns adaptation may fail
* **Priority:** P1

## Baseline Card: NVIDIA Isaac GR00T N1.7

* **Name / Paper:** NVIDIA Isaac GR00T
* **Year / Status:** 2026 current N1.7 Early Access
* **Project / Code Link:** https://github.com/NVIDIA/Isaac-GR00T
* **Dataset Link:** Included demo data; external DROID/LIBERO/SimplerEnv; custom LeRobot v2 format
* **Model Weights:** https://huggingface.co/nvidia/GR00T-N1.7-3B
* **License / Access restriction:** Apache-2.0; N1.7 marked Early Access with limited stability guarantees
* **Main task:** Cross-embodiment language/image/state-conditioned continuous action generation
* **Input:** Video/images + robot state + language + embodiment tag
* **Output:** Relative EEF/action chunks
* **Training / Finetuning command or process:** Convert to GR00T LeRobot v2 + `modality.json`; use `launch_finetune.py`; open-loop inference scripts included
* **Hardware requirement:** Inference 16 GB+; fine-tuning 40 GB+ recommended
* **Can we directly run it?** Yes on demo data
* **Can it serve our first-stage mode baseline?** No
* **Can it serve later full-policy baseline?** Yes
* **What modification is needed for our project:** Add quadruped-arm modality/embodiment config and mode head or hierarchical interface
* **What it can fairly test:** Whether a synthetic/human-video-pretrained foundation model helps after identical necessity supervision
* **What it cannot test:** AIGC necessity effectiveness from pretraining alone
* **Risk / blocker:** Large stack, EA changes, 40 GB tuning recommendation
* **Priority:** P1

## Baseline Card: Open X-Embodiment / RT-1-X

* **Name / Paper:** Open X-Embodiment and RT-X Models
* **Year / Status:** 2023 / official open dataset and RT-1-X checkpoint
* **Project / Code Link:** https://github.com/google-deepmind/open_x_embodiment
* **Dataset Link:** Dataset spreadsheet and RLDS download instructions in repo
* **Model Weights:** RT-1-X JAX checkpoint on Google Cloud Storage
* **License / Access restriction:** Apache-2.0 software; CC-BY materials; individual contributed datasets have their own citations/terms
* **Main task:** Cross-robot language-conditioned manipulation
* **Input:** Workspace RGB + task string
* **Output:** Seven gripper-motion variables
* **Training / Finetuning command or process:** Dataset colab and inference examples; no simple current first-stage head workflow
* **Hardware requirement:** Dataset is large; framework uses TFDS/RLDS/JAX
* **Can we directly run it?** Partial
* **Can it serve our first-stage mode baseline?** Partial as data schema/reference only
* **Can it serve later full-policy baseline?** Yes
* **What modification is needed for our project:** Build a small RLDS dataset with explicit mode labels or reuse loader only
* **What it can fairly test:** Generic cross-embodiment data/pretraining baseline
* **What it cannot test:** Four-way tool necessity without new labels
* **Risk / blocker:** Large data and older framework complexity
* **Priority:** P1

## Baseline Card: RT-Affordance

* **Name / Paper:** RT-Affordance
* **Year / Status:** 2024 / preprint, project page
* **Project / Code Link:** https://snasiriany.me/rt-affordance
* **Dataset Link:** Not found after search
* **Model Weights:** Not found after search
* **License / Access restriction:** Unknown for model/data
* **Main task:** Affordance-plan-conditioned manipulation
* **Input:** Initial image + task language
* **Output:** Affordance plan, then robot action
* **Training / Finetuning command or process:** Not found after search
* **Hardware requirement:** Unknown
* **Can we directly run it?** No
* **Can it serve our first-stage mode baseline?** Conceptually yes, implementation no
* **Can it serve later full-policy baseline?** Partial
* **What modification is needed for our project:** Implement only an affordance feature/mask baseline, not the full hierarchy
* **What it can fairly test:** Whether affordance/how-to features explain necessity gains
* **What it cannot test:** Availability/reachability/necessity without added state
* **Risk / blocker:** No released training stack located
* **Priority:** P1

## Baseline Card: Counterfactual Tool Use

* **Name / Paper:** Creative Robot Tool Use by Counterfactual Reasoning
* **Year / Status:** 2026 / arXiv preprint
* **Project / Code Link:** Not found after search
* **Dataset Link:** Not found after search
* **Model Weights:** Not applicable/not found
* **License / Access restriction:** Unknown
* **Main task:** Causal discovery of tool suitability
* **Input:** Tool/task features and simulated interventions
* **Output:** Causal properties, tool classification and transfer keypoints
* **Training / Finetuning command or process:** Not found after search
* **Hardware requirement:** Dynamics simulation required
* **Can we directly run it?** No
* **Can it serve our first-stage mode baseline?** No; idea source
* **Can it serve later full-policy baseline?** Partial
* **What modification is needed for our project:** Apply single-variable interventions to `reachable/usable/suitable/direct_feasible`; label expected mode flip
* **What it can fairly test:** Causal intervention design
* **What it cannot test:** Direct/no-tool mode without our formulation
* **Risk / blocker:** Reimplementation required
* **Priority:** P1

## Baseline Card: Robustness-Aware Tool Selection

* **Name / Paper:** Robustness-Aware Tool Selection and Manipulation Planning with Learned Energy-Informed Guidance
* **Year / Status:** 2026 / ICRA 2026
* **Project / Code Link:** Not found after search
* **Dataset Link:** Not found after search
* **Model Weights:** Not found after search
* **License / Access restriction:** Unknown
* **Main task:** Robust tool/configuration selection and contact-rich planning
* **Input:** Candidate tools/configurations and environment state
* **Output:** Robustness score, selected tool and trajectory
* **Training / Finetuning command or process:** Not found after search
* **Hardware requirement:** Simulation/optimization expected; exact requirement unavailable
* **Can we directly run it?** No
* **Can it serve our first-stage mode baseline?** No
* **Can it serve later full-policy baseline?** Conceptual/partial
* **What modification is needed for our project:** Add “direct manipulation” as a candidate with its own feasibility/cost score
* **What it can fairly test:** Whether suitability/robustness alone is enough
* **What it cannot test:** Learned visual necessity without implementation/data
* **Risk / blocker:** Full method reimplementation
* **Priority:** P1

## Baseline Card: Physics-Conditioned Grasping / iTuP

* **Name / Paper:** Physics-Conditioned Grasping for Stable Tool Use
* **Year / Status:** 2025 / arXiv preprint
* **Project / Code Link:** Not found after search
* **Dataset Link:** Not found after search
* **Model Weights:** Not found after search
* **License / Access restriction:** Unknown
* **Main task:** Task-wrench-conditioned grasp selection
* **Input:** Tool geometry, candidate grasp and intended trajectory
* **Output:** Physics-conditioned grasp score/selection
* **Training / Finetuning command or process:** Not found after search
* **Hardware requirement:** Unknown
* **Can we directly run it?** No
* **Can it serve our first-stage mode baseline?** No
* **Can it serve later full-policy baseline?** Partial
* **What modification is needed for our project:** Use a simplified tool usability/suitability score as structured input after mode selection
* **What it can fairly test:** Whether downstream tool physics changes action choice
* **What it cannot test:** Whether a tool is necessary
* **Risk / blocker:** No release; mechanics beyond first-stage scope
* **Priority:** P1

## Baseline Card: RoboTool

* **Name / Paper:** Creative Robot Tool Use with Large Language Models / RoboTool
* **Year / Status:** 2023 / project page and paper
* **Project / Code Link:** https://creative-robotool.github.io/
* **Dataset Link:** Not found after search
* **Model Weights:** Uses external LLM APIs/models; no project checkpoint
* **License / Access restriction:** Provider API and skill-library dependent
* **Main task:** Language-to-executable tool-use code generation
* **Input:** Natural-language task and skill/environment description
* **Output:** Python control program
* **Training / Finetuning command or process:** Prompted Analyzer–Planner–Calculator–Coder; official runnable repository not found
* **Hardware requirement:** LLM/API plus robot/simulator skill stack
* **Can we directly run it?** No
* **Can it serve our first-stage mode baseline?** Partial as a prompt-only four-way decision
* **Can it serve later full-policy baseline?** Yes conceptually
* **What modification is needed for our project:** Ask the same LLM to choose one of four modes from structured scene facts; do not implement full skills now
* **What it can fairly test:** Explicit language reasoning versus learned visual/state classifier
* **What it cannot test:** End-to-end visual grounding unless perception is supplied
* **Risk / blocker:** API variance and unfair oracle scene descriptions
* **Priority:** P1

## Baseline Card: UWM

* **Name / Paper:** Unified World Models
* **Year / Status:** 2025 / RSS 2025
* **Project / Code Link:** https://github.com/WEIRDLabUW/unified-world-model
* **Dataset Link:** LIBERO, Robomimic, DROID wrappers included
* **Model Weights:** Public LIBERO-90 and DROID checkpoints linked in README
* **License / Access restriction:** Repository license not clearly surfaced in the parsed README; inspect before redistribution
* **Main task:** Joint action/video diffusion for policy, forward/inverse dynamics and video generation
* **Input:** Current/future observations and optional actions
* **Output:** Actions and/or future observations
* **Training / Finetuning command or process:** Public Robomimic/LIBERO Python commands and DROID shell scripts
* **Hardware requirement:** Exact requirement not stated; diffusion video training is materially heavier than a classifier
* **Can we directly run it?** Partial
* **Can it serve our first-stage mode baseline?** No
* **Can it serve later full-policy baseline?** Yes
* **What modification is needed for our project:** Compare candidate direct/tool future predictions or attach a mode head; convert matched data to Zarr wrapper
* **What it can fairly test:** Whether future modeling adds value beyond action/representation training
* **What it cannot test:** Intent/necessity without explicit labels
* **Risk / blocker:** Compute and data conversion
* **Priority:** P1

## Baseline Card: Video Generators are Robot Policies

* **Name / Paper:** Video Policy
* **Year / Status:** 2025 / arXiv; public code
* **Project / Code Link:** https://github.com/cvlab-columbia/videopolicy
* **Dataset Link:** Public simulation dataset zip linked in README
* **Model Weights:** Public checkpoint zip linked in README
* **License / Access restriction:** Repository includes a license file; derived from Stable Video Diffusion, so downstream model terms must be checked
* **Main task:** Video generation plus action decoding
* **Input:** Robot video observations/task data
* **Output:** Future video and actions
* **Training / Finetuning command or process:** Stage-1 video, stage-2 action decoder and joint-training configs are provided
* **Hardware requirement:** Reference scripts use 8 GPUs × 80 GB VRAM
* **Can we directly run it?** Yes for released evaluation; not cheaply for retraining
* **Can it serve our first-stage mode baseline?** No
* **Can it serve later full-policy baseline?** Yes
* **What modification is needed for our project:** Train/evaluate on direct/tool candidate videos or use generated-video features for the same mode head
* **What it can fairly test:** Whether video prediction objective improves mode generalization
* **What it cannot test:** Necessity unless candidate futures and labels are controlled
* **Risk / blocker:** Prohibitive reference training cost
* **Priority:** P1

## Baseline Card: DreamGen / GR00T-Dreams

* **Name / Paper:** DreamGen
* **Year / Status:** 2025 / public NVIDIA code
* **Project / Code Link:** https://github.com/nvidia/GR00T-dreams
* **Dataset Link:** Demo data and embodiment-specific preprocessing in repo; external Cosmos/robot data required
* **Model Weights:** IDM/world-model assets referenced by the repository
* **License / Access restriction:** NVIDIA repository and dependent Cosmos/GR00T licenses apply
* **Main task:** Generate robot videos and recover pseudo-actions
* **Input:** Initial frame + language
* **Output:** Synthetic video + IDM/LAPA pseudo-actions
* **Training / Finetuning command or process:** World-model generation, video preprocessing, optional IDM training, GR00T finetuning; scripts support Franka/GR1/SO100/RoboCasa
* **Hardware requirement:** Multiple large models; exact end-to-end minimum not stated
* **Can we directly run it?** Partial
* **Can it serve our first-stage mode baseline?** No
* **Can it serve later full-policy baseline?** Yes
* **What modification is needed for our project:** Initially use only DreamGen Bench-style instruction/physics scoring for generated tool-state variants
* **What it can fairly test:** Filtered versus unfiltered AIGC augmentation
* **What it cannot test:** Reliable action supervision by default
* **Risk / blocker:** New quadruped-arm embodiment requires custom IDM/data config
* **Priority:** P1

## Baseline Card: Dream2Fix

* **Name / Paper:** Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis
* **Year / Status:** 2026 / arXiv preprint
* **Project / Code Link:** Not found after search
* **Dataset Link:** Claimed 120k paired samples; public download not found after search
* **Model Weights:** Not found after search
* **License / Access restriction:** Unknown
* **Main task:** Generated failure/recovery pairs and recovery prediction
* **Input:** Successful demonstrations plus perturbed actions/world-model rollout
* **Output:** Verified failure videos, failure type and recovery trajectory
* **Training / Finetuning command or process:** Described in paper; runnable release not found
* **Hardware requirement:** Generative world model and VLM tuning; exact requirement unavailable
* **Can we directly run it?** No
* **Can it serve our first-stage mode baseline?** No; verifier idea only
* **Can it serve later full-policy baseline?** Partial
* **What modification is needed for our project:** Implement lightweight checks for label preservation, tool-state consistency and kinematic plausibility
* **What it can fairly test:** Whether filtering generated samples matters
* **What it cannot test:** Initial necessity without our state labels
* **Risk / blocker:** Full pipeline cannot be reproduced from available release
* **Priority:** P1

# P2 — Background / later execution

## Baseline Card: UMI on Legs

* **Name / Paper:** UMI on Legs
* **Year / Status:** 2024 / CoRL 2024
* **Project / Code Link:** https://github.com/real-stanford/umi-on-legs
* **Dataset Link:** Checkpoint/data download documented in repository
* **Model Weights:** WBC checkpoints documented
* **License / Access restriction:** MIT code; Isaac Gym and hardware SDK terms apply
* **Main task:** Track high-level EE trajectories with quadruped whole-body controller
* **Input:** Future end-effector trajectory in task/world frame
* **Output:** Whole-body quadruped/arm actions
* **Training / Finetuning command or process:** Isaac Gym RL training and real deployment modules are public
* **Hardware requirement:** NVIDIA GPU for Isaac Gym; real stack uses Unitree-style quadruped, ARX5, camera/iPhone odometry
* **Can we directly run it?** Yes for documented WBC rollout; partial for our hardware
* **Can it serve our first-stage mode baseline?** No
* **Can it serve later full-policy baseline?** Yes
* **What modification is needed for our project:** Map selected mode to EE trajectory source; do not modify WBC for Claim A
* **What it can fairly test:** Whether high-level mode/trajectory interface survives mobile embodiment
* **What it cannot test:** Tool necessity
* **Risk / blocker:** Hardware/networking and one-way interface; project notes reachability feedback is missing
* **Priority:** P2

## Baseline Card: RoboDuet

* **Name / Paper:** RoboDuet
* **Year / Status:** 2024 preprint; project reports RA-L 2025 acceptance
* **Project / Code Link:** https://github.com/locomanip-duet/RoboDuet
* **Dataset Link:** Simulation environment generated online; no separate task dataset required
* **Model Weights:** No simple universal checkpoint link found; play commands expect trained run directories
* **License / Access restriction:** MIT; Isaac Gym Preview 4 and deployment components have separate terms
* **Main task:** Cooperative locomotion/arm 6D pose tracking
* **Input:** Locomotion commands and EE target pose
* **Output:** Leg and arm joint actions
* **Training / Finetuning command or process:** `python scripts/auto_train.py --num_envs 4096 ... --robot go1|go2`
* **Hardware requirement:** CUDA GPU; Isaac Gym Preview 4; real deployment targets Go1/Go2+ARX5
* **Can we directly run it?** Partial
* **Can it serve our first-stage mode baseline?** No
* **Can it serve later full-policy baseline?** Yes
* **What modification is needed for our project:** Feed target poses only after mode selection
* **What it can fairly test:** WBC/whole-body execution, not decision quality
* **What it cannot test:** Necessity, tool-state reasoning or AIGC
* **Risk / blocker:** Specific embodiment and simulator version
* **Priority:** P2

## Baseline Card: MoManipVLA

* **Name / Paper:** MoManipVLA
* **Year / Status:** 2025 / CVPR 2025
* **Project / Code Link:** Not found after search
* **Dataset Link:** Uses OVMM/public simulation resources; project-specific release not found
* **Model Weights:** Not found after search
* **License / Access restriction:** Unknown
* **Main task:** Convert fixed-base VLA waypoints into feasible mobile base-arm trajectories
* **Input:** VLA end-effector waypoints and mobile robot state
* **Output:** Base waypoints and arm trajectory
* **Training / Finetuning command or process:** Not found after search
* **Hardware requirement:** Mobile manipulation simulation/optimizer
* **Can we directly run it?** No
* **Can it serve our first-stage mode baseline?** No
* **Can it serve later full-policy baseline?** Conceptual
* **What modification is needed for our project:** Place it after `reposition/use-tool` mode, with tool-tip feasibility costs
* **What it can fairly test:** Base-arm feasibility interface
* **What it cannot test:** Tool necessity or data-source claims
* **Risk / blocker:** No official implementation located
* **Priority:** P2

## Baseline Card: Cosmos-Predict2 / Cosmos-Reason

* **Name / Paper:** NVIDIA Cosmos-Predict2; Cosmos-Reason is used inside current GR00T releases
* **Year / Status:** Predict2 repository archived in 2025 in favor of newer versions
* **Project / Code Link:** https://github.com/nvidia-cosmos/cosmos-predict2
* **Dataset Link:** GR00T-Dreams/DROID/AgiBot examples linked in repository
* **Model Weights:** https://huggingface.co/collections/nvidia/cosmos-predict2
* **License / Access restriction:** Apache-2.0 code; NVIDIA Open Model License for weights; third-party filters have separate licenses
* **Main task:** Text/image/video/action-conditioned visual world generation
* **Input:** Image/video + text; some checkpoints also accept actions
* **Output:** Future video
* **Training / Finetuning command or process:** Inference and post-training guides exist; 2B/14B variants
* **Hardware requirement:** Ampere or newer; CUDA 12.6/Linux; model-specific VRAM can be large
* **Can we directly run it?** Partial
* **Can it serve our first-stage mode baseline?** No
* **Can it serve later full-policy baseline?** Partial as AIGC generator
* **What modification is needed for our project:** Generate only appearance/semantic variants; apply state/label verifier before training
* **What it can fairly test:** Whether generated visual diversity helps after filtering
* **What it cannot test:** Action correctness or necessity without external labels
* **Risk / blocker:** Archived version, heavy compute and license constraints
* **Priority:** P2

# Remove / not useful now

## Baseline Card: Sora-like Closed Video Generator

* **Name / Paper:** Closed text/video generation service
* **Year / Status:** Provider-dependent
* **Project / Code Link:** Closed; no reusable training code/weights
* **Dataset Link:** Not available
* **Model Weights:** Not available
* **License / Access restriction:** Commercial service terms and access limits
* **Main task:** Generic video generation
* **Input:** Prompt/image/video
* **Output:** Video
* **Training / Finetuning command or process:** Not available
* **Hardware requirement:** Provider hosted
* **Can we directly run it?** Possibly as a service, not reproducibly
* **Can it serve our first-stage mode baseline?** No
* **Can it serve later full-policy baseline?** No
* **What modification is needed for our project:** None worth doing now
* **What it can fairly test:** At most qualitative visual augmentation
* **What it cannot test:** Reproducible action/necessity learning
* **Risk / blocker:** Closed and unstable
* **Priority:** Remove

## 4. Ideas That Can Be Transferred Into Existing Baselines

| Source paper | Transferable idea | Target baseline | How to modify baseline | Failure mode addressed | Minimal ablation | Risk |
|---|---|---|---|---|---|---|
| AHA / FailGen | Programmatic perturbation of successful examples | IsaacSim matched-pair generator + B0–B3 | Replace grasp-slip/pose failures with one-variable changes to `direct_feasible`, `tool_reachable`, `tool_usable`, `tool_suitable`; save pair ID and expected mode | Random negatives do not isolate causal tool state | Random independent negatives vs matched perturbations at equal count | Simulator labels may be too easy |
| Dream2Fix | Structured verification of generated counterfactuals | AIGC augmentation over B2 | Add semantic-label preservation, tool presence/state, geometry/kinematics and outcome checks before accepting generated frames/videos | Visually plausible AIGC silently changes the label | No filter vs CLIP filter vs state verifier at same accepted count | Reimplement verifier; no released code |
| Counterfactual Tool Use | Targeted tool-property intervention | B2 paired counterfactual loss | Generate matched variants changing one physical/functional property; require correct pairwise mode flip | Model uses category/appearance shortcuts | Targeted property pairs vs random tool replacement | Detailed physics may exceed first-stage scope |
| RT-Affordance | Compact intermediate affordance representation | Affordance-only baseline | Predict/use functional mask or key pose embedding, but exclude availability/reachability fields | Necessity gain may actually be affordance gain | Image-only vs affordance-only vs full tool state | No official code; use Aff-Grasp substitute |
| AffordGrasp / Aff-Grasp | Functional-region mask as task-conditioned feature | B1 affordance-only head | Pool frozen visual features inside predicted functional region and feed to same mode head | Global image features miss tool function | Full-image vs mask-pooled feature, same head | Mask predictor errors confound decision |
| OpenVLA / Octo | Frozen robot-pretrained representation + lightweight readout | B0/B1/B2 | Freeze backbone; attach four-class mode head; do not finetune action decoder | Generic CLIP may lack robot-action features | Generic VLM encoder vs Octo/OpenVLA frozen features | Hidden-feature extraction/API work |
| Octo | Existing `head_only` finetuning modes | First-stage robot-pretrained baseline | Replace diffusion action readout with categorical mode readout; keep transformer frozen | Full finetuning obscures data-effect claim | Frozen vs head-only vs full on small subset | JAX/custom dataset adapter |
| Robustness-Aware Tool Selection | Treat direct manipulation as another candidate with cost/robustness | Later selector | Score `direct`, each tool and `reposition` using feasibility/cost before invoking policy | Correct affordance but poor robustness or excessive acquisition cost | Suitability-only vs suitability+cost/robustness | No code; requires scoring design |
| iTuP | Tool-conditioned physical usability score | B1 structured state / later action selector | Add a coarse `tool_usable` or predicted stability score after necessity decision | Tool is semantically suitable but physically unstable | Binary availability vs availability+usability score | Physics labels difficult |
| UMI on Legs | EE-trajectory/WBC interface | Later quadruped execution | Map mode output to one of multiple high-level trajectory providers; keep WBC fixed | Decision contribution gets mixed with controller changes | Same WBC for all mode models | One-way interface lacks reachability feedback |
| MoManipVLA | Base-arm feasibility correction | Later `reposition` execution | Use mode `reposition` to trigger base waypoint optimization; return feasibility as state | Fixed-base policy requests unreachable poses | No reposition vs optimized reposition | No released code |
| RoboDuet | Cooperative whole-body pose tracking | Later execution baseline | Feed identical target poses from each mode policy into RoboDuet controller | Mobile embodiment tracking failures | Same targets with standard WBC vs RoboDuet | Specific Go1/Go2+ARX5 stack |
| UWM | Separate future/action objectives | Later world-model baseline | Add mode head to shared representation; compare action-only vs video+action vs video+action+necessity | Claim that future prediction alone yields necessity | Same data/backbone with objectives ablated | Heavy compute |
| DreamGen | Pseudo-action route and DreamGen Bench-style scoring | Later AIGC baseline | Initially reuse instruction-following/physics-alignment evaluation only; add pseudo-actions only after video validity is established | Generated videos are accepted based on appearance | Unfiltered vs IF/PA-filtered generated data | New embodiment requires IDM |
| Video Policy | Freeze video generator, train action/readout head | Later generated-future baseline | Freeze video U-Net and train only mode head before attempting action head | End-to-end training hides whether video features matter | Frozen-video mode head vs joint training | Released reference uses 8×80GB |
| RoboTool | Explicit four-mode language decision | Prompt-only baseline | Provide identical structured scene facts; force one of four labels; no skill execution | Learned classifier may only reproduce obvious rules | Neutral prompt vs explicit CoT vs wrong state | Oracle text descriptions make comparison unfair |

这些迁移均只改变既有 baseline 的数据、readout、loss、filter 或接口；不要求另建 agent 系统、world model 或 WBC。

## 5. First-Stage Baselines We Should Actually Run

只推荐以下五项；其中 B2 是 proposed variant，B3 是控制实验。

| Order | Baseline | Start condition | What is needed | Recommendation |
|---|---|---|---|---|
| 1 | **B0: frozen CLIP/SigLIP image-language features + mode head** | 今天 | Matched dataset schema；无需外部机器人代码 | **立即开始** |
| 2 | **B1: B0 + structured tool state** | 今天 | `present/reachable/usable/suitable/direct_feasible` fields | **立即开始** |
| 3 | **B2: B1 + paired counterfactual consistency/ranking loss** | Pair IDs ready | Pair sampler and loss | **本周核心** |
| 4 | **B3: shuffled/wrong/noisy tool-state control** | B1 runs | State permutation/noise scripts | **必须做** |
| 5 | **Octo-Small frozen/head-only representation** | B0–B3 pipeline stable | Clone Octo; custom dataset/readout adapter | **找代码后做；时间不足可延后一周** |

Affordance-only 对照的执行建议：

- 若 Aff-Grasp 环境能在 1–2 天内跑通，则把其 functional mask pooled feature 接到 B0 的同一个 mode head；
- 若依赖冲突明显，则先用 IsaacSim oracle functional mask 做 affordance-only upper bound，不能把它称为 Aff-Grasp 复现。

### First-stage go/no-go

**Go to VLA/AIGC integration only if：**

1. B2 在 grouped unseen scenes 上优于 B1 和 same-count unpaired baseline；
2. B3 显著下降，说明模型实际使用 tool state；
3. 距离匹配 hard pairs 上仍有增益；
4. counterfactual consistency 的提升不是仅由类平衡造成。

**No-go：** 若只有训练/随机切分 accuracy 提升，或 B3 不下降，则先修数据和标签，不进入 OpenVLA、AIGC 或 WBC。

## 6. Later-Stage Baselines

| Baseline | Why later, not first-stage |
|---|---|
| OpenVLA LoRA/full tuning | 7B、RLDS 数据转换和 ≥27 GB 显存会把问题变成工程适配；应在 paired-data effect 成立后测试完整 VLA |
| Octo full/action finetuning | 第一阶段只需 frozen/head-only；完整 diffusion action training会混入动作质量变量 |
| openpi π0/π0.5 | 模型强但 embodiment/config 适配较重；用于最终强 VLA baseline |
| GR00T N1.7 | 40 GB tuning recommendation、EA stack 和 LeRobot modality mapping；适合作为 foundation-model 后续对照 |
| AIGC filtered vs unfiltered | 依赖 Claim A classifier 作为下游测量工具；否则无法判断生成数据是否有用 |
| UWM / Video Policy future prediction | 需要视频/动作联合数据和大计算；用于测试 future objective，而非建立最小 necessity claim |
| DreamGen pseudo-actions | 新四足臂 embodiment 需要 IDM；先验证生成视频和标签保持性 |
| RoboTool/LLM skill library | 先只做 prompt-level mode baseline；完整 agent 会偏离端到端主线 |
| MoManipVLA / UMI on Legs / RoboDuet | 它们测试 waypoint/WBC/mobile execution，不测试第一阶段 mode learning |
| Real robot sanity baseline | 第一阶段仿真结论稳定后，仅做小规模静态 scene-to-mode 检查，再进入闭环 |

## 7. What Not to Do Now

- 不要现在微调整个 OpenVLA、Octo、π0/π0.5 或 GR00T。
- 不要现在训练 UWM、Video Policy、DreamGen 或 Cosmos world model。
- 不要现在做完整四足 WBC、base-arm trajectory 或硬件闭环。
- 不要现在让 AIGC 成为主实验或默认 action supervision。
- 不要把 RoboTool/LLM agent + skill library 变成项目主线。
- 不要为无公开代码的 iTuP、robustness-aware selection、Dream2Fix 做完整复现。
- 不要把 oracle tool state 的提升直接解释为真实 perception 下的 tool-awareness。
- 不要把 affordance mask、工具存在或目标距离单独当成 necessity。

## 8. Advisor Discussion Points

1. 是否同意第一阶段只跑 P0 baselines：B0–B3，Octo frozen/head-only 作为有时间才加的机器人预训练表示？
2. 是否同意 OpenVLA、openpi、GR00T 和完整 Octo action finetuning全部放到 Claim A 成立后？
3. 是否同意 affordance-only 是必要对照，并接受先用 oracle mask upper bound、再尝试 Aff-Grasp 实现？
4. 是否同意迁移 AHA/FailGen 的程序化扰动设计，以及 Dream2Fix 的 verification 思路，而不复现其完整 VLM/world-model？
5. 是否同意采用明确 gate：Claim A 通过 grouped hard-pair 与 shuffled-state 检验后，才进入 AIGC filtering 或 VLA integration？

## Final Self-Check

1. **哪些能直接做 baseline？** 已明确：轻量分类器、Octo frozen/head-only、FailGen 数据生成、Aff-Grasp 组件。
2. **哪些 idea 能迁移？** 已给出 source → target → modification → ablation，共 15 项。
3. **是否有真实链接和训练信息？** 有；缺失项均写 `Not found after search`。
4. **是否区分第一阶段与后续？** 是；本周只保留五项，完整 VLA/world model/WBC 后置。
5. **是否避免泛综述？** 是；所有内容围绕 tool necessity 和四类 mode。
6. **是否可用于导师讨论？** 是；结尾给出 go/no-go 和五个明确决策问题。
