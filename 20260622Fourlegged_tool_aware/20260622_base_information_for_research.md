【一句话判断】
这个方向不能泛泛写成“tool-aware VLA for quadruped-arm mobile robot”；更硬的主线应该是：**工具使用不是高层语义选择问题，而是“工具功能—抓取点—接触力/力矩—底盘/机械臂可达性—长时序执行”的联合决策问题。**

---

## 【主命题】

这项调研真正要支撑的潜在研究命题是：

**在四足+机械臂移动机器人中，工具使用需要一种 tool-aware embodied policy，使机器人不仅知道“用哪个工具”，还要知道“如何拿、从哪里接触、如何移动身体/底盘、如何在交互力下稳定完成任务”。**

这里至少混了四层问题：

1. **语义层**：根据任务选择工具。
2. **视觉/几何层**：定位工具、可交互部位、接触点、目标区域。
3. **物理执行层**：工具会放大力矩、改变有效末端、引入碰撞与稳定性约束。
4. **移动具身层**：四足底盘位置、机身姿态、机械臂可达空间和工具使用轨迹耦合。

如果论文只做“VLM 选工具 + VLA 出动作”，大概率不够硬；如果能证明 **tool-aware 机制解决了普通 VLA / 普通 mobile manipulation 在工具交互中的系统性 failure mode**，才像研究问题。

---

# 1. 两个搜索大方向的关键词拆解

## A. Baseline / 机器人具身智能方向

这一组用于找**直接可比 baseline、系统框架、机器人实验协议**。

| 子方向                           | 核心问题          | 英文关键词                                                                                                                                       |
| ----------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| General VLA                   | 视觉语言到连续动作     | `vision-language-action model`, `VLA robotic manipulation`, `generalist robot policy`, `flow matching robot policy`, `action chunking`      |
| Mobile manipulation VLA       | 底盘+机械臂协同      | `mobile manipulation VLA`, `mobile manipulator vision language action`, `base-arm coordination`, `13-DoF mobile manipulation`, `OVMM VLA`   |
| Quadruped / loco-manipulation | 四足或全身具身执行     | `quadruped VLA`, `loco-manipulation VLA`, `whole-body VLA`, `legged manipulation`, `vision-language-action quadruped`                       |
| Tool-aware manipulation       | 工具选择、抓取、接触、力矩 | `robot tool use`, `tool-aware manipulation`, `task-aware grasping`, `wrench-aware grasp`, `tool affordance`, `tool-use trajectory planning` |
| WAM / world model             | 预测未来状态辅助行动    | `world action model`, `robot world model`, `video policy`, `action-conditioned world model`, `future prediction robot policy`               |
| Memory / long-horizon         | 长任务、历史依赖      | `long-horizon VLA`, `history-aware VLA`, `episodic memory robot policy`, `embodied memory`                                                  |
| Benchmark / evaluation        | 用来证明不是 demo   | `VLABench`, `RoboTwin 2.0`, `ManipBench`, `PhysToolBench`, `RoboCerebra`, `mobile manipulation benchmark`                                   |

这里最应该组合搜索的是：

`tool-aware mobile manipulation VLA`
`robot tool use VLM task-aware grasp wrench`
`quadruped arm mobile manipulation vision language action`
`world action model mobile manipulation robot tool use`
`long-horizon VLA tool use benchmark`

---

## B. CV / LLM 迁移方向

这一组不是直接 baseline，而是找**可迁移机制**：VLM grounding、affordance、agent tool use、物理推理、视频世界模型。

| 来源领域               | 你要找的机制          | 英文关键词                                                                                                                           |
| ------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| CV affordance      | 工具功能区域、接触区域     | `affordance localization`, `open-vocabulary affordance`, `part-level affordance`, `contact affordance`, `functional grasping`   |
| 3D / grounding     | 3D 接触点、目标点、几何约束 | `3D visual grounding`, `keypoint affordance`, `spatial constraints`, `object-centric representation`, `slot-based world model`  |
| Egocentric video   | 从人类视频学工具使用      | `egocentric video affordance`, `human video to robot manipulation`, `hand-object interaction`, `human-to-robot transfer`        |
| LLM agents         | 工具调用、任务分解、执行监控  | `LLM tool use`, `tool-aware planning`, `function calling`, `agentic planning`, `code as policy`, `multi-agent robotic planning` |
| Physical reasoning | 工具物理原理、力矩、接触    | `physical tool understanding`, `wrench transfer`, `contact-rich manipulation`, `physics-aware grasping`, `tool-use dynamics`    |
| Video world models | 用未来预测约束动作       | `video generation robot policy`, `world model for embodied AI`, `action-conditioned video prediction`, `WAM robotics`           |

这一组最关键的判断标准是：**它们能不能把“工具”从语义标签提升成一个改变机器人 action space 和 physical constraint 的对象。**

---

# 2. 2025–2026 重点相关文献：Baseline 主线

## 2.1 General VLA / Robot Foundation Model

| 优先级 | 文献                                                                                 | 为什么重要                                                                                                   | 对你项目的作用                                                                         |
| --- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 高   | **π0.5: a Vision-Language-Action Model with Open-World Generalization**, CoRL 2025 | 用多机器人、多任务、语义预测、web data 等 co-training 来提升真实家庭场景泛化。它是 2025 年最重要的 generalist VLA baseline 之一。([arXiv][1]) | 可作为“端到端 VLA 上限参考”，但不直接解决工具力学与四足底盘耦合。                                            |
| 高   | **Gemini Robotics 1.5 / Gemini Robotics-ER 1.5**, Google DeepMind, 2025            | 明确分成 embodied reasoning model 和 VLA execution model，并强调 motion transfer、多步任务、跨 embodiment。([arXiv][2])  | 对你的系统叙事很重要：高层 reasoning + 低层 action，比单一 VLA 更适合 tool-aware mobile manipulation。 |
| 高   | **GR00T N1 / N1.5**, NVIDIA, 2025                                                  | GR00T N1 是开源 humanoid VLA foundation model；N1.5 是增强版本，强调更好泛化和语言跟随。([arXiv][3])                          | 可作为大厂 open VLA 参考，但它偏 humanoid，不是四足+臂直接 baseline。                               |
| 高   | **FAST: Efficient Action Tokenization for VLA Models**, RSS 2025                   | 提出频域动作 tokenization，让自回归 VLA 能处理高频、灵巧、长动作序列，并降低训练时间。([arXiv][4])                                        | 如果你不用 diffusion/action chunking，而想做 AR action model，这篇是动作表示 baseline。           |
| 高   | **X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment VLA**, ICLR 2026   | 用 embodiment-specific soft prompts 处理跨机器人数据异质性。([OpenReview][5])                                        | 对 Go2+Piper 很相关：你的 embodiment 与主流 arm/humanoid 数据不一致。                           |
| 高   | **VLM4VLA**, ICLR 2026                                                             | 结论很关键：通用 VLM 能力并不能可靠预测下游 VLA 控制能力，视觉模块才是主要瓶颈。([arXiv][6])                                               | 可以用来反驳“直接换更强 VLM 就够了”的审稿人或组内直觉。                                                 |

**判断**：这些是“必须读”的 baseline 层。但它们多数证明的是 generalist manipulation，不是 tool-aware mobile manipulation。你的论文不能只把它们列为 related work，还要说清楚它们在工具使用上的缺口：**工具改变接触动力学和可达空间，而不是普通目标物体。**

---

## 2.2 Mobile manipulation / loco-manipulation / quadruped-relevant

| 优先级 | 文献                                                                            | 为什么重要                                                                                                              | 对你项目的作用                                                       |
| --- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| 高   | **MoManipVLA: Transferring VLA Models for General Mobile Manipulation**, 2025 | 把固定基座 VLA 转移到移动操作，利用 VLA 生成末端 waypoint，再通过 base-arm optimization 让轨迹可行。([arXiv][7])                                | 这是你最直接的 mobile manipulation baseline 之一。                      |
| 高   | **SG-VLA: Spatially-Grounded VLA for Mobile Manipulation**, 2026              | 针对 13D base-arm-gripper action，引入多视角 RGB、depth、历史帧和辅助监督，如机器人位置、关节、affordance、相对位姿、segmentation。([arXiv][8])        | 和你的 Go2+Piper 很接近：证明 mobile manipulation 不能只靠单帧 RGB+language。 |
| 中高  | **MobileVLA-R1**, 2025                                                        | 面向四足机器人，结合 CoT alignment 和 GRPO 强化学习，把语言 grounding 到连续控制。([arXiv][9])                                              | 四足 VLA 方向相关，但更偏导航/移动控制，不是机械臂工具操作。                             |
| 中高  | **WholeBodyVLA**, ICLR 2026                                                   | 面向 humanoid 大空间 loco-manipulation，从 action-free egocentric videos 学 unified latent action。([GitHub][10])           | 不直接是四足，但对“移动身体+操作”的统一动作空间有参考价值。                               |
| 中   | **MotionWAM**, 2026                                                           | 把 video world model 的中间 denoising features 接到 whole-body motion token，做实时 humanoid loco-manipulation。([arXiv][11]) | 对你后续 WAM 路线有启发，但现在更像大算力/大系统方向。                                |
| 中   | **MindExplore: Long-Horizon VLA System**, ICCV 2025                           | 层级 embodied system，包含 reasoning、acting、memory，动作包括机械臂位姿、速度和底盘线/角速度。([CVF Open Access][12])                         | 对“Agent + VLA skill”叙事很有用。                                    |

**判断**：MoManipVLA 和 SG-VLA 是当前最贴近你硬件形态的技术路线。MobileVLA-R1 能证明四足 VLA 方向存在，但它不能直接支撑“工具使用”。WholeBodyVLA/MotionWAM 更适合作为趋势参考，而不是直接 baseline。

---

# 3. 2025–2026 重点相关文献：Tool-aware / affordance / physical tool use

这一组是你方向的核心。真正的 novelty 很可能不在“VLA”，而在 **tool-aware representation / tool-conditioned action feasibility / tool-use dynamics**。

| 优先级 | 文献                                                                                          | 核心机制                                                                                                                                                | 对你的启发                                                                       |
| --- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| 最高  | **Dynamic Robot Tool Use with Vision Language Models / iTUP**, 2025                         | 指出已有方法只做工具选择或准静态操作，忽略 task-appropriate tool grasping；它把工具使用建模为 VLM grounding + trajectory planning + physics-informed grasp selection。([arXiv][13]) | 这是你 tool-aware 方向最该重点读的论文之一。你的问题也应从“选工具”推进到“工具如何改变抓取和执行”。                   |
| 最高  | **Learning Precise Affordances from Egocentric Videos for Robotic Manipulation**, ICCV 2025 | 从 egocentric videos 自动得到 precise affordance annotation，并用于 tool grasping 和 robot-to-human tool handover。([CVF Open Access][14])                     | 如果你想用 AIGC/人类视频预训练工具使用，这篇是关键 CV/robot bridge。                               |
| 高   | **AffordGrasp**, 2025                                                                       | 用 VLM 做 in-context affordance reasoning，实现 open-vocabulary task-oriented grasping。([arXiv][15])                                                     | 可作为“VLM affordance + grasp”baseline，但要注意它不处理四足底盘和工具动力学。                     |
| 高   | **PhysToolBench**, 2025                                                                     | 专门评测 MLLM 对物理工具的理解，分 tool recognition、tool understanding、tool creation；结果显示 MLLM 在工具理解上仍有明显缺口。([arXiv][16])                                         | 这能支撑你的问题动机：大模型会“说工具”，但未必真正理解工具物理功能。                                         |
| 中高  | **RobotSmith**, 2025                                                                        | 用 VLM agents + physics simulation 自动设计工具和工具使用轨迹。([arXiv][17])                                                                                       | 偏 tool design，不是你第一阶段直接 baseline，但很适合 related work 的“工具作为可设计外部 embodiment”。 |
| 中高  | **VLMgineer**, RSS 2025 Hardware Intelligence Oral                                          | 用 VLM + evolutionary search 自动 co-design physical tools and action plans。([arXiv][18])                                                              | 可作为高阶工具发明方向，不建议作为你第一篇主 baseline。                                            |
| 中   | **Learning Fast, Tool-Aware Collision Avoidance for Collaborative Robots**, RA-L 2025       | tool-aware collision avoidance 根据工具尺寸和交互模式实时调整，处理部分可见点云和动态障碍。([arXiv][19])                                                                          | 对四足+臂移动机器人非常现实：工具会改变碰撞体和安全距离。                                               |
| 中   | **PLATO: Planning with LLMs and Affordances for Tool Manipulation**, 2026                   | 多 LLM agent 处理语言、环境、工具 affordance 和 executable actions。([Springer][20])                                                                             | 更偏系统框架，不一定是强方法 baseline。                                                    |

**关键结论**：
你不能把“工具”只建模成 object category。文献里最硬的趋势是：**工具 = 改变接触点、末端有效长度、力矩传递、碰撞体积和任务可行性的外部 embodiment。**

---

# 4. 2025–2026 重点相关文献：WAM / World Model / Video Policy

| 优先级 | 文献                                                                     | 核心机制                                                                                          | 对你的启发                                                          |
| --- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 高   | **World Action Models: The Next Frontier in Embodied AI**, 2026 survey | 把 WAM 定义为同时建模 future states 和 actions，而不是只做 reactive observation-to-action。([arXiv][21])      | 可作为 WAM 方向总入口。                                                 |
| 高   | **Video Generators are Robot Policies**, 2025                          | 用 video diffusion model 加 action diffusion head，同时预测像素和动作。([videopolicy.cs.columbia.edu][22]) | 如果你想用 AIGC 视频/世界模型训练 VLA，这篇是核心路线。                              |
| 高   | **OA-WAM: Object-Addressable World Action Model**, 2026                | 用 object slots 表示世界状态，解决整体图像/latent 不利于根据指令定位特定对象的问题。([arXiv][23])                            | 对 tool-aware 特别有价值：工具、目标物、障碍物、机器人应作为可寻址对象，而不是一坨 global latent。 |
| 中高  | **WLA: World-Language-Action Model**, 2026                             | 同时预测 textual subtasks、subgoal images 和 robot actions，把 WAM 的世界建模与 VLA 的语言推理结合。([arXiv][24])   | 对“Agent reasoning + WAM prediction + VLA action”路线有参考价值。       |
| 中   | **MoWM: Mixture-of-World-Models for Embodied Planning**, 2026          | 讨论 pixel world model 和 latent world model 的互补：前者细节多但冗余，后者紧凑但可能丢失精细操作信息。([arXiv][25])          | 对工具使用很关键：只预测全局视频可能无法保留接触点/力矩信息。                                |
| 中   | **GigaBrain-0.5M***, 2026                                              | 用 world-model-based RL 提升 VLA 的 future anticipation 和长时序执行。([arXiv][26])                      | 大组/大厂式路线，值得看趋势，但实现门槛高。                                         |

**判断**：
WAM 对你不是天然必要。它只有在你要证明“工具使用失败来自缺少未来接触后果预测”时才是主机制。否则 WAM 很容易变成昂贵配件。

---

# 5. 2025–2026 重点 benchmark / evaluation

| 优先级 | Benchmark                   | 重点能力                                                                                                   | 对你的作用                                                    |
| --- | --------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| 高   | **VLABench**, ICCV 2025     | 100 类任务、2000+ objects、implicit human intention、world knowledge、long-horizon reasoning。([arXiv][27])    | 可作为语言条件长时序 manipulation benchmark 参考。                    |
| 高   | **RoboTwin 2.0**, 2025/2026 | 50-task bimanual benchmark，731 objects，147 categories，自动任务程序合成和数据生成。([Robot Simulation Platform][28])  | 适合借鉴数据生成和 domain randomization 思路。                       |
| 高   | **ManipBench**, CoRL 2025   | 评测 VLM 的低层 manipulation reasoning，包括 object-object interaction、deformable manipulation 等。([arXiv][29]) | 可用于证明 VLM 的物理/操作推理不足。                                    |
| 高   | **PhysToolBench**, 2025     | 专门评测 MLLM 的物理工具理解。([arXiv][16])                                                                        | 和你的 tool-aware 方向强相关，应该重点读。                              |
| 中高  | **RoboCerebra**, 2025       | 长时序 high-level reasoning，强调 System 1 / System 2 交互。([arXiv][30])                                       | 如果你走“VLM planner + VLA controller”路线，这个 benchmark 有参考价值。 |
| 中   | **Robo2VLM**, 2025          | 从真实机器人轨迹生成 VQA，用来评测/增强 VLM 的空间、目标条件、交互理解。([arXiv][31])                                                 | 可借鉴为你自己的 tool-use reasoning dataset：从轨迹自动生成工具理解问题。       |

---

# 6. 当前最强反对意见

1. **这可能只是模块化系统集成，不是新研究。**
   如果只是 VLM 选工具 + SAM 分割 + MoveIt/Nav2 执行 + VLA 微调，那更像工程系统，不像论文核心。

2. **“tool-aware”可能只是 affordance-aware 的换名。**
   你必须证明工具不仅是 affordance localization，还引入了普通 object manipulation 没有的 failure mode，例如杠杆力矩、接触方向、末端延长、底盘姿态、碰撞体积变化。

3. **四足+臂 embodiment 可能只是平台差异，不是研究贡献。**
   审稿人会问：为什么 mobile manipulator / humanoid 已有方法不能直接迁移？你的机制是否由四足+臂的约束逼出来？

4. **WAM 可能是过重配件。**
   如果没有实验证明 future prediction 对工具使用必要，WAM 会被认为是为了追热点而堆模块。

5. **baseline 很难公平。**
   你需要对比至少三类：modular agent、mobile manipulation VLA、tool-use specialist method。只对比普通 VLA 不够。

---

# 7. 最小可行研究切口

我建议你把这个方向先压成一个更可证明的命题：

**Tool-aware mobile manipulation requires jointly reasoning about task-conditioned tool affordance, grasp stability, and base-arm reachability; treating tools as ordinary graspable objects causes systematic failures under long-reach, contact-rich, or force-amplifying tasks.**

对应最小机制可以是：

1. **Tool-state representation**
   把工具表示为：`functional part + grasp region + effective contact point + tool axis + collision envelope + expected interaction type`。

2. **Tool-conditioned feasibility score**
   对候选动作评分时不仅看视觉目标，还看：机械臂可达性、底盘可达位置、工具末端是否能到达目标、碰撞风险、力矩/滑移风险。

3. **VLM/VLA/WAM 分层接口**
   VLM 负责语义和 affordance，planner 负责 base-arm-tool feasibility，VLA 或 diffusion policy 负责局部执行。WAM 只有在需要预测接触后果时才加入。

---

# 8. 最应该先读的 12 篇/组

按你的项目价值排序：

1. **Dynamic Robot Tool Use with VLMs / iTUP**
2. **MoManipVLA**
3. **SG-VLA**
4. **π0.5**
5. **Gemini Robotics 1.5**
6. **X-VLA**
7. **VLM4VLA**
8. **Learning Precise Affordances from Egocentric Videos**, ICCV 2025
9. **PhysToolBench**
10. **OA-WAM**
11. **VLABench**, ICCV 2025
12. **ManipBench**, CoRL 2025

---

# 9. 是否像论文方向

**现在像一个可能成长成论文的点子，但还不成立。**

原因很明确：
你现在有一个强方向，但还没有唯一主命题。它可能被写成：

* tool-aware VLA；
* mobile manipulation benchmark；
* VLM affordance system；
* WAM for tool use；
* quadruped-arm agent system；
* AIGC video pretraining for tool use。

这些不能并列当主贡献。最可能成立的是：

> **工具使用中的 failure mode 不是语义错误，而是工具改变了机器人可达性、接触动力学和动作可行性；因此需要 tool-aware feasibility / representation 介入 mobile manipulation policy。**

这比“做一个四足+臂 tool-aware VLA 系统”更像论文。

---

# 10. 下一步最应该想清楚的问题

1. **你的工具任务失败主要来自哪里？**
   是选错工具、抓错位置、底盘站位不对、工具末端够不到、接触力矩导致滑动，还是长时序记忆断裂？

2. **你的 tool-aware 机制相比普通 affordance / VLA / planner 多了什么不可替代信息？**
   如果只是多一个 prompt 或多一个 mask，不够。

3. **最小 benchmark 应该如何设计？**
   不要一上来 100 个家庭任务。先设计 3 类能打掉反对意见的任务：
   **reach-extension tools、force-amplifying tools、surface-contact tools**。每类都要有普通 VLA 会系统失败、tool-aware 机制能解释并改善的对照。

[1]: https://arxiv.org/abs/2504.16054?utm_source=chatgpt.com "$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization"
[2]: https://arxiv.org/abs/2510.03342?utm_source=chatgpt.com "Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer"
[3]: https://arxiv.org/abs/2503.14734?utm_source=chatgpt.com "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots"
[4]: https://arxiv.org/abs/2501.09747?utm_source=chatgpt.com "FAST: Efficient Action Tokenization for Vision-Language-Action Models"
[5]: https://openreview.net/forum?id=kt51kZH4aG&utm_source=chatgpt.com "X-VLA: Soft-Prompted Transformer as Scalable Cross- ..."
[6]: https://arxiv.org/abs/2601.03309?utm_source=chatgpt.com "VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models"
[7]: https://arxiv.org/abs/2503.13446?utm_source=chatgpt.com "MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation"
[8]: https://arxiv.org/abs/2603.22760?utm_source=chatgpt.com "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation"
[9]: https://arxiv.org/abs/2511.17889?utm_source=chatgpt.com "MobileVLA-R1: Reinforcing Vision-Language-Action for Mobile Robots"
[10]: https://github.com/OpenDriveLab/WholebodyVLA?utm_source=chatgpt.com "OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards ..."
[11]: https://arxiv.org/abs/2606.09215?utm_source=chatgpt.com "MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation"
[12]: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.pdf?utm_source=chatgpt.com "Towards Long-Horizon Vision-Language-Action System"
[13]: https://arxiv.org/html/2505.01399v1?utm_source=chatgpt.com "Dynamic Robot Tool Use with Vision Language Models"
[14]: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Learning_Precise_Affordances_from_Egocentric_Videos_for_Robotic_Manipulation_ICCV_2025_paper.pdf?utm_source=chatgpt.com "Learning Precise Affordances from Egocentric Videos for ..."
[15]: https://arxiv.org/abs/2503.00778?utm_source=chatgpt.com "AffordGrasp: In-Context Affordance Reasoning for Open-Vocabulary Task-Oriented Grasping in Clutter"
[16]: https://arxiv.org/abs/2510.09507?utm_source=chatgpt.com "PhysToolBench: Benchmarking Physical Tool Understanding for MLLMs"
[17]: https://arxiv.org/abs/2506.14763?utm_source=chatgpt.com "RobotSmith: Generative Robotic Tool Design for Acquisition of Complex Manipulation Skills"
[18]: https://arxiv.org/abs/2507.12644?utm_source=chatgpt.com "VLMgineer: Vision Language Models as Robotic Toolsmiths"
[19]: https://arxiv.org/abs/2508.20457?utm_source=chatgpt.com "Learning Fast, Tool aware Collision Avoidance for Collaborative Robots"
[20]: https://link.springer.com/article/10.1007/s10846-026-02392-y?utm_source=chatgpt.com "Planning with LLMs and Affordances for Tool Manipulation"
[21]: https://arxiv.org/abs/2605.12090?utm_source=chatgpt.com "World Action Models: The Next Frontier in Embodied AI"
[22]: https://videopolicy.cs.columbia.edu/assets/video_policy.pdf?utm_source=chatgpt.com "Video Generators are Robot Policies - Columbia University"
[23]: https://arxiv.org/abs/2605.06481?utm_source=chatgpt.com "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation"
[24]: https://arxiv.org/abs/2606.05979?utm_source=chatgpt.com "World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis"
[25]: https://arxiv.org/html/2509.21797v3?utm_source=chatgpt.com "MoWM: Mixture-of-World-Models for Embodied Planning ..."
[26]: https://arxiv.org/abs/2602.12099?utm_source=chatgpt.com "GigaBrain-0.5M*: a VLA That Learns From World Model-Based Reinforcement Learning"
[27]: https://arxiv.org/abs/2412.18194?utm_source=chatgpt.com "VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks"
[28]: https://robotwin-platform.github.io/?utm_source=chatgpt.com "RoboTwin 2.0"
[29]: https://arxiv.org/abs/2505.09698?utm_source=chatgpt.com "ManipBench: Benchmarking Vision-Language Models for Low-Level Robot Manipulation"
[30]: https://arxiv.org/abs/2506.06677?utm_source=chatgpt.com "RoboCerebra: A Large-scale Benchmark for Long-horizon Robotic Manipulation Evaluation"
[31]: https://arxiv.org/abs/2505.15517?utm_source=chatgpt.com "Robo2VLM: Visual Question Answering from Large-Scale In-the-Wild Robot Manipulation Datasets"
