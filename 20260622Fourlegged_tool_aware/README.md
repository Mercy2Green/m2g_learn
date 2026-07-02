
# PROJECT_tool_aware_mobile_manipulation.md


## 2026701

【一句话判断】
你现在的想法里，**“VLM 不会稳定建立 task-target-helper 关系”比“VLM 没有使用工具的第一性认知”更像研究问题**；前者可以被形式化、训练和验证，后者更像解释性说法，容易被审稿人质疑成心理化描述。

---

## 【主命题】

这项工作真正要证明的是：

> 当前通用 VLM 在家庭移动操作规划中，缺少稳定的 **task-conditioned helper-target relational affordance grounding**：它能看见目标物和辅助物，也能理解任务，但不能稳定判断“哪个辅助物能通过什么动作链帮助完成当前任务”。

中文说得更直白一点：

> 模型的问题不是完全看不见袋子、托盘、长杆，而是不会稳定地把“任务目标”和“场景里的辅助物”关联起来，并进一步生成“先用辅助物改变任务条件，再完成目标”的规划链。

这个比“没有工具意识”更硬。

---

## 【它属于哪类研究对象】

你现在讨论的是三个层次混在一起：

1. **新分析 / benchmark finding**
   当前结果显示：VLM 在 clean prompt 下不稳定使用 helper；tool-prior 有有限改善；失败集中在多物体聚合、helper search、reach-extension。

2. **新中间表征 / 方法机制**
   你想加入一个“helper-target-task 关联表征”，让模型显式或隐式地学会目标物、辅助物、任务之间的关系。

3. **可能的新训练数据 / affordance 数据构造**
   你在想是否需要文本配对、推理链、bbox/mask、object pair 标签。

真正可以发展成方法贡献的是第 2 层：

> **Task-conditioned Helper-Target Affordance Relation Modeling**

不要把它写成“工具意识”。应该写成：

> 给 VLM/VLA 增加一种面向任务的 helper-target relational affordance grounding，使模型从“识别物体”变成“识别哪个物体能通过哪种功能关系帮助完成任务”。

---

## 【对你两个解释角度的判断】

### 角度 1：VLM 没有“使用工具的第一性认知”

这个说法可以作为直觉，但不适合作为论文主命题。

原因是你自己的实验已经显示：tool-prior prompt 能恢复一部分 case，尤其 task_008 reach-extension。这说明模型不是完全没有工具知识，而是**激活不稳定、关联不稳定、动作链不稳定**。你的 prompt intervention 结果更支持“弱工具先验 / 弱任务激活”，而不是“完全没有工具意识”。

更安全的表述是：

> 当前 VLM 可能具备部分 latent tool-use knowledge，但这种知识不会在普通任务提示下稳定激活；即使显式提示 helper，也不总能转化为完整 planning chain。

这个说法和你目前数据更一致。

---

### 角度 2：VLM 不能稳定建立 helper、task、target 的关联

这个角度更强，也更像研究问题。

你现在的失败本质上可以写成：

```text
Task: 给卧室同学送多瓶水
Target: 多瓶水
Helper candidates: 袋子 / 托盘 / 篮子 / 盒子
Expected relation: aggregate-and-transport-with
Expected chain: 放入 helper → 搬运 helper → 送达目标地点
```

或者：

```text
Task: 拿沙发下遥控器
Target: 遥控器
Helper candidates: 长杆 / 扫把 / 抓取杆
Expected relation: extend-reach-with
Expected chain: 用 helper 拨出目标 → 再抓取目标
```

这不是普通 object detection，也不是普通 affordance map。它是一个**任务条件下的对象关系判断**：

> 当前任务下，哪个 object 不是 target，但能改变 target 的可达性、可搬运性、稳定性或效率？

这比“注意力没有关联”更准确。

---

## 【关于你说的 attention / cosine similarity】

你的直觉方向对，但表述需要收紧。

你说：

> VLM 看了图、听了话，无法把图中的物体区域特征之间使用 attention 进行关联。

这句话在机制上不能直接 claim，因为你没有 attention map、hidden state probing、causal intervention 的证据。你最多能说：

> 从行为结果看，模型未能稳定利用视觉中可见的 helper object 来生成与任务相关的 helper-mediated plan；这可能反映了 task-conditioned relational grounding 不足。

如果要把 attention/cosine 写成方法，不建议直接说“因为 attention 不够”。建议说：

> 我们引入一个显式的 helper-target relation scorer，在候选 helper object 和 target object 之间建模 task-conditioned functional relation。

这可以是 cross-attention，也可以是 pairwise similarity，也可以是 graph scorer，但论文里核心不是 attention 形式，而是**这个关系对象本身**。

---

## 【最强反对意见】

### 1. 这是不是只是 prompt 不够好？

你已经有 tool-prior 和 efficient/safe prompt，可以初步反驳，但还不够。你要强调：

* tool-prior 提高 helper-chain rate，但 robust failure 仍多；
* diagnostic probe 也不能完全解决；
* 所以不是简单加一句“考虑工具”就能解决。

但审稿人仍可能说：更强 prompt / CoT / self-reflection 会改善。你需要补一个 stronger prompt baseline，例如：

```text
First list all visible objects.
Then list possible helper objects.
Then decide whether each helper can improve efficiency, safety, stability, or reachability.
Then generate plan.
```

如果这个还不能完全解决，你的 claim 才更硬。

---

### 2. 这是不是 VLM 识别不到 helper，而不是不会建立关系？

你需要区分：

* helper visible but unused：task_001, task_008；
* helper not visible, should search：task_002；
* helper visible and used successfully：task_006。

尤其 task_001 和 task_008 很重要，因为它们能证明不是纯视觉识别问题。

---

### 3. 这是不是任务期望太主观？

例如 task_004 “拿些吃的喝的”，直接拿一个苹果一瓶水也可能合理。这个 case 不能作为最硬证据。

最硬任务应该是：

* task_001：多瓶水 + 可见袋子；
* task_002：多瓶水 + 无容器，需要 search；
* task_008：沙发下遥控器 + 长杆；
* task_005：多个杯盘 + 托盘/盆。

---

### 4. 你的方法会不会只是加一个 heuristic tool selector？

如果你只是“检测到袋子就提示用袋子”，这会被认为是规则补丁。

要避免这个，你的方法必须证明：

* 它不是 object category lookup；
* 它能根据 task 改变 helper 选择；
* 同一个 object 在不同任务下角色不同；
* 同一个 task 在不同 scene 下 helper 可以不同；
* 它能拒绝不合适 helper。

---

## 【如果它要成立，最小必要机制是什么】

不是“给所有 helper 类物体做识别”这么简单。最小必要机制应该是：

> **一个 task-conditioned helper-target relation module。**

形式上可以是：

```text
Input:
Image I
Instruction x
Target object candidates T = {t_i}
Helper candidates H = {h_j}
Embodiment constraint e

Output:
For each pair (t_i, h_j):
relation type r_ij
usefulness score s_ij
expected action chain c_ij
```

关系类型可以先定义成少数几类：

| Relation type            | 例子           | 任务      |
| ------------------------ | ------------ | ------- |
| aggregate-transport-with | 水瓶 → 袋子/托盘   | 多物体搬运   |
| search-helper-for        | 水瓶 → 搜索袋子/托盘 | 无明显容器   |
| extend-reach-with        | 遥控器 → 长杆     | 沙发下目标   |
| collect-into             | 小物体 → 收纳篮    | 本地收纳    |
| clean-with               | 纸屑 → 扫把/簸箕   | 清理      |
| direct-is-enough         | 单瓶水 → 不需要工具  | control |

你真正要学的是这个 relation，不是单纯 tool category。

---

## 【算法/方法建议】

### 方法 1：Helper-Target Relation Scorer

这是最像论文核心的版本。

给定图像、任务、候选目标物和候选 helper，模型预测：

```text
Is h useful for completing task x involving target t?
What role does h play?
What action chain should use h?
```

可以输出：

```json
{
  "target": "water bottles",
  "helper": "orange bag",
  "relation": "aggregate_transport_with",
  "score": 0.91,
  "chain": ["put bottles into bag", "carry bag to bedroom", "deliver bottles"]
}
```

训练方式：

* 正样本：合理 target-helper pair；
* 负样本：无关 helper、错误 helper、target-as-helper、过度使用 helper；
* loss：relation classification + usefulness ranking + chain generation。

这比直接 finetune VLM 输出最终 plan 更可控。

---

### 方法 2：Object-pair contrastive training

你提到 cosine similarity，这个可以做成 contrastive learning，但不要只做文本相似度。

样本形式：

```text
(task, target, helper_positive, helper_negative_1, helper_negative_2)
```

例如：

```text
Task: 拿沙发下遥控器
Target: remote
Positive helper: long rod
Negative helper: tray, bottle, cushion
Relation: extend_reach_with
```

训练目标：

```text
score(task, target, positive_helper) > score(task, target, negative_helper)
```

这可以用：

* CLIP-style contrastive loss；
* pairwise ranking loss；
* DPO / preference loss；
* multiple-choice VQA loss。

优点：标注成本比轨迹低。
缺点：只能学 helper 选择，不能保证生成完整 planning chain。

所以它最好和 chain generation 搭配。

---

### 方法 3：Structured planning SFT / DPO

让模型输出结构化中间结果：

```json
{
  "target_objects": [...],
  "candidate_helpers": [...],
  "selected_helper": "...",
  "helper_relation": "...",
  "why_helper_needed": "...",
  "action_chain": [...]
}
```

训练数据可以从你的 benchmark 开始扩展。

推荐数据包括三类：

1. **positive chain**
   正确 helper + 正确 chain。

2. **negative chain**
   直接抓取、分批搬运、错误 helper、只提不使用、target-as-helper。

3. **preference pair**
   同一图像同一任务下：

   * chosen：用 helper 的合理 plan；
   * rejected：直接抓/分批搬/错误 helper plan。

这比单纯 SFT 更适合你的发现，因为你已经有大量 failure response，可以直接构造成 rejected samples。

---

### 方法 4：Grounded helper proposal + planner reranking

这是更工程但更容易先跑通的版本。

Pipeline：

```text
Image + task
↓
Object proposal / open-vocab grounding
↓
Target objects + helper candidates
↓
Relation scorer
↓
Generate top-k plans
↓
Helper-aware plan reranker
```

这个方案不需要直接改 VLM backbone，可以先作为 post-hoc planner/critic 做 proof-of-concept。

它能回答一个关键问题：

> 如果我们显式给模型候选 helper-target relation，能不能显著修复 clean prompt failure？

如果能，说明你的 failure diagnosis 是对的。

---

## 【和现有 Affordance/VLA 工作的关系】

现在最新的 affordance/VLA 工作确实在往“中间表征”走，但它们多数聚焦的是**目标物的可操作区域或动作生成**，而你这里更偏**helper-target-task 关系**。

例如，AffordanceVLA 把 affordance forecasting 作为 task-oriented intermediate representation，并分成 Which2Act、Where2Act、How2Act：object-centric grounding、2D interaction localization、3D geometric reasoning，用来桥接 vision-language 和 action。([arXiv][1])

AffordVLA 则试图通过 affordance teacher 对齐 VLA 的中间视觉表征，让 VLA 内化 manipulation-centric affordance perception，而不是显式插入 mask，从而减少额外标注和推理开销。([arXiv][2])

A2A 这类工作更接近你的需求，因为它强调 task-conditioned scene-level affordance grounding，并指出现实场景中同一个 object 可对应不同任务 affordance，同一个任务也可能有多个有效 functional regions。([arXiv][3])

但你的区别在于：

> 你不是只问“目标物哪里能抓/哪里能操作”，而是问“场景里哪个非目标物能作为 helper 改变目标任务的可执行性”。

这是一个可以站得住的 gap。

---

## 【数据应该怎么准备】

你问“文本配对 + 推理怎么训练，还是直接全部圈出来？”我的判断是：

> 如果你只想证明 planning-level improvement，可以先不做 dense mask；
> 如果你想证明 visual grounding 和 helper-target relation，就必须至少有 bbox/mask 级 object annotation。

我建议分四层数据，从低成本到高成本。

---

### Level 1：任务级标签

每个样本标：

```json
{
  "task_id": "task_001",
  "should_use_helper": true,
  "expected_relation": "aggregate_transport_with",
  "expected_helper_types": ["bag", "tray", "basket", "box"],
  "target_objects": ["water bottles"]
}
```

用途：训练/评估 plan 是否该用 helper。
缺点：不能证明模型看到了哪个 helper。

---

### Level 2：object-level grounding 标签

给图像中目标物和 helper 标 bbox/mask：

```json
{
  "target_boxes": [...],
  "helper_boxes": [...],
  "helper_labels": ["orange bag"],
  "distractor_boxes": [...]
}
```

用途：训练 helper proposal / relation scorer。
建议至少用 bbox；mask 更好但成本更高。

---

### Level 3：relation 标签

标注 target-helper-task 三元组：

```json
{
  "target": "water bottles",
  "helper": "orange bag",
  "relation": "aggregate_transport_with",
  "is_positive": true
}
```

同时标负样本：

```json
{
  "target": "water bottles",
  "helper": "laptop",
  "relation": "none",
  "is_positive": false
}
```

这是你最需要的数据层。

---

### Level 4：action-chain 标签

标最终 plan：

```json
{
  "chain": [
    "pick up the orange bag",
    "put the water bottles into the bag",
    "carry the bag to the bedroom",
    "place the bottles near the students"
  ]
}
```

用途：训练 chain generation 或 plan reranking。

---

## 【你可以如何低成本构造第一版训练数据】

你现在已经有 benchmark，可以做 bootstrap：

1. 用 Grounded-SAM / detection model 找 objects；
2. 用 VLM/LLM 生成候选 helper list；
3. 用规则或 LLM 生成 target-helper relation candidates；
4. 人工只 verify top candidates；
5. 把模型失败输出作为 rejected plan；
6. 把人工修正 plan 作为 chosen plan。

这样可以得到：

```text
(image, task, target, helper, relation, chosen_chain, rejected_chain)
```

这比从零采 robot trajectory 容易得多。

---

## 【最小实验闭环】

如果你想把这个从 idea 变成论文，最小实验不是直接训练大模型，而是：

### Experiment 1：Relation annotation agreement

找 50–100 个 household scenes，让 2–3 个人标：

* target；
* helper；
* relation type；
* expected chain。

证明这个问题不是你主观臆造。

---

### Experiment 2：Base VLM failure

用当前 benchmark 证明：

* clean prompt fail；
* tool-prior 有限恢复；
* diagnostic probe 仍不完全解决。

你已经有这个雏形。

---

### Experiment 3：Helper relation module 是否改善

比较：

1. Base VLM；
2. Base VLM + tool-prior prompt；
3. Base VLM + object list；
4. Base VLM + helper-target relation hint；
5. 你的 trained relation scorer / reranker。

如果 4/5 显著改善，说明你的 diagnosis 和 mechanism 对上了。

---

### Experiment 4：Ablation

必须测：

* 去掉 helper candidates；
* 去掉 target-helper relation；
* 只给 object list；
* 只给 helper category；
* 只给 tool-prior prompt；
* 用错误 helper relation。

这能证明你的方法不是“多给了信息就好”，而是 relation 本身有效。

---

## 【是否像论文】

现在判断：

> **这是一个可能成长成论文的点子，但方法部分还没有成立。**

成立的部分：

* benchmark finding 有雏形；
* failure mode 很具体；
* “helper-target-task relation”是合理问题定义；
* 能和 affordance/VLA 中间表征工作接上。

不成立的部分：

* 你还没有定义 relation label space；
* 没有训练数据构造协议；
* 没有证明 relation module 比 prompt/heuristic 更必要；
* 还没有最小模型闭环。

---

## 【我建议你下一步只想清楚三个问题】

### 1. 你的核心对象到底是什么？

我建议定义成：

> **Task-conditioned helper-target affordance relation**

不要定义成“工具意识”。

---

### 2. 你的最小机制是 scorer 还是 generator？

两种路线：

* scorer：判断哪个 helper 对当前 target/task 有用；
* generator：生成完整 helper-mediated action chain。

我建议先做 scorer + reranker，风险更低。

---

### 3. 你的数据标注到哪一层？

最低可发雏形：

```text
task-level label + helper-target relation label + chosen/rejected plan
```

更强版本：

```text
bbox/mask + relation label + action chain
```

如果没有 bbox/mask，你的工作更像 planning benchmark。
如果有 bbox/mask，它才更像 visual grounding / affordance representation。

[1]: https://arxiv.org/abs/2606.06155?utm_source=chatgpt.com "AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding"
[2]: https://arxiv.org/abs/2605.17517?utm_source=chatgpt.com "AffordVLA: Injecting Affordance Representations into Vision-Language-Action Models via Implicit Feature Alignment"
[3]: https://arxiv.org/abs/2606.04172?utm_source=chatgpt.com "Affordance2Action: Task-Conditioned Scene-level Affordance Grounding for Real-Time Manipulation"



## 0. Project Name

Tool-Aware Mobile Manipulation with Quadruped-Arm Robot

---

## 1. Current Project Context

The current active project is about a quadruped robot with a manipulator performing tool-aware mobile manipulation.

The project is still in an early research formulation stage. It currently has a broad story, but the exact paper claim, technical mechanism, dataset route, baseline suite, and target venue are not fully determined.

The current task is not simply to implement a pipeline.
The current task is to help compress the broad project story into a researchable problem.

---

## 2. High-Level Project Goal

The project is not only about making the robot use tools.

The deeper goal is to study whether a robot can understand:

1. when a tool is necessary;
2. when a tool is unnecessary;
3. whether a tool is available, reachable, suitable, or usable;
4. whether using or not using a tool leads to different future outcomes;
5. whether tool state / tool necessity changes the robot’s action, trajectory, or mode decision.

The project should avoid being reduced to simple tool recognition.

---

## 3. Current Technical Frame

The current project frame includes:

* quadruped robot + robot arm;
* mobile manipulation;
* tool-awareness;
* AIGC-generated video data;
* simulation-generated data, especially IsaacSim or similar simulators;
* positive and negative samples;
* world model / video prediction / future prediction;
* VLA / WAM / robot foundation models;
* output of end-effector trajectory, mode signal, or tool-use decision;
* low-level execution by WBC / local motion controller.

Current discussions include:

* using AIGC models such as Cosmos-like or Sora-like video generation to generate egocentric robot videos;
* using simulation to generate more controllable positive/negative samples;
* training a world model or VLA model to learn tool-use intention or tool necessity;
* eventually connecting high-level decision or trajectory output to low-level WBC.

---

## 4. Important Boundary

This project should not drift into the following as main directions:

* multi-robot coordination;
* shared-server coordination;
* explicit atomic skill library as the core method;
* pure LLM agent planning;
* pure navigation;
* pure motion planning;
* pure tool classification;
* pure system demo without research claim.

These can appear as related work, baseline, or comparison, but should not become the main project unless explicitly re-approved.

---

## 5. Core Research Question Candidates

The project should search for one small, provable research question inside the broad tool-aware mobile manipulation frame.

Candidate questions include:

### Candidate 1: Tool Necessity Learning

Can positive-negative data teach a robot to decide when a tool is necessary, rather than only how to use a tool?

Possible claim:

> Counterfactual positive-negative samples enable a robot policy or world model to distinguish tool-necessary states from tool-optional states in mobile manipulation.

---

### Candidate 2: AIGC Data Validity

Can AIGC-generated videos provide useful supervision for tool-use decision learning, despite physical and action inconsistency?

Possible claim:

> AIGC-generated tool-use videos are useful only when filtered or structured by tool necessity, physical plausibility, and task outcome consistency.

---

### Candidate 3: Tool-State Intervention

Does tool state actually change the action / trajectory / mode output of a VLA or world model?

Possible claim:

> Tool-state conditioning changes downstream action or mode decisions under controlled counterfactual scenes, showing that the model uses tool information rather than visual shortcuts.

---

### Candidate 4: Simulation vs AIGC Complementarity

What is the complementary role of simulation and AIGC in creating positive-negative samples for tool-aware mobile manipulation?

Possible claim:

> Simulation provides controllable physical counterfactuals, while AIGC provides diverse semantic scenarios; combining them improves tool necessity generalization.

---

## 6. What “Tool-Aware” Should Mean

Tool-awareness should be decomposed into levels:

1. **Tool Recognition**
   The robot recognizes that an object is a tool.

2. **Tool Affordance**
   The robot understands what function the tool can provide.

3. **Tool State**
   The robot knows whether the tool is available, reachable, held, blocked, broken, too far, too short, too long, or suitable.

4. **Tool Necessity**
   The robot decides whether the task requires a tool.

5. **Tool-Conditioned Decision**
   The robot changes its action, trajectory, skill, or mode based on tool information.

The project should aim at levels 3-5, not only level 1.

---

## 7. Positive-Negative Sample Design

The central data idea is to construct positive and negative examples.

A good positive-negative pair should satisfy:

* same task;
* same target;
* same environment;
* same robot capability;
* same initial condition as much as possible;
* only the tool-use-related variable changes.

Examples:

### Positive Sample

* Tool is used.
* Task succeeds.
* The tool is necessary or helpful.
* The future state shows successful completion.

### Negative Sample

* Tool is not used, or tool is unavailable / unreachable / wrong.
* Task fails.
* Failure is caused by the absence, wrongness, or unavailability of the tool.
* Failure should not be caused by unrelated artifacts.

Bad negative samples:

* random failure;
* physically impossible video;
* failure caused by poor control rather than tool necessity;
* scene visually different in many unrelated ways;
* failure that can be solved without the tool.

---

## 8. Data Routes

Current candidate data routes:

### 8.1 Real Robot Data

Pros:

* physically valid;
* directly connected to action;
* useful for final grounding.

Cons:

* expensive;
* difficult to generate failures;
* limited diversity;
* safety and hardware cost.

---

### 8.2 Simulation Data

Pros:

* controllable;
* can generate counterfactuals;
* can produce action labels;
* good for variable isolation.

Cons:

* sim-to-real gap;
* limited visual diversity;
* simulator asset and task design burden.

---

### 8.3 AIGC Video Data

Pros:

* high diversity;
* easy to scale;
* can generate rare or difficult scenarios;
* useful for semantic pretraining or world model training.

Cons:

* physical inconsistency;
* no reliable action labels;
* tool interaction may be unrealistic;
* may teach visual shortcuts;
* needs filtering and verification.

---

### 8.4 Hybrid Data

Possible route:

* use AIGC for semantic diversity and broad tool-use scenarios;
* use simulation for physically grounded counterfactual pairs;
* use small real robot data for grounding and evaluation.

This hybrid route may be more defensible than relying only on AIGC.

---

## 9. Literature Review Scope

Prioritize papers from:

* ICRA;
* IROS;
* CoRL;
* RSS;
* NeurIPS;
* ICLR;
* CVPR;
* ICCV;
* ECCV;
* TRO;
* RA-L;
* Science Robotics;
* high-quality arXiv from major robotics / AI labs.

Search areas:

1. robotic tool use;
2. tool affordance learning;
3. when to use tools;
4. tool necessity;
5. tool-conditioned manipulation;
6. mobile manipulation;
7. quadruped manipulation;
8. VLA / WAM / robot foundation models;
9. world model for robot manipulation;
10. video prediction for robot learning;
11. AIGC / synthetic video for robotics;
12. simulation data for robot learning;
13. failure learning;
14. negative samples;
15. counterfactual data.

---

## 10. Literature Review Questions

Every literature review for this project should answer:

1. Do existing works solve how to use tools or when to use tools?
2. Do they model tool necessity?
3. Do they use positive-negative or counterfactual data?
4. Do they use AIGC or synthetic video?
5. Do they generate action labels or only videos?
6. Do they prove that tool state changes action?
7. Do they work on mobile manipulation or only tabletop manipulation?
8. What are their main limitations?
9. Which methods can be baseline?
10. What is the smallest research gap we can claim?

---

## 11. Baseline Categories

Potential baseline categories:

### 11.1 No Tool-Awareness VLA

A VLA policy trained without explicit tool state or tool necessity data.

Purpose:

* test whether tool-awareness data matters.

---

### 11.2 Language-Prompt-Only Baseline

Add tool instruction only through text prompt.

Purpose:

* test whether prompt engineering is enough.

---

### 11.3 Affordance-Recognition Baseline

Use a VLM or affordance model to identify tool function, then feed it to the policy.

Purpose:

* test whether recognition-level tool understanding is sufficient.

---

### 11.4 Simulation-Only Positive-Negative Baseline

Train using simulated positive-negative pairs.

Purpose:

* test controllable physical counterfactuals.

---

### 11.5 AIGC-Only Positive-Negative Baseline

Train using generated video pairs.

Purpose:

* test whether AIGC supervision helps.

---

### 11.6 Hybrid AIGC + Simulation Baseline

Combine semantic diversity from AIGC with physical consistency from simulation.

Purpose:

* test complementarity.

---

### 11.7 Wrong / Shuffled Tool Condition Baseline

Shuffle tool state, use wrong tool, or remove tool condition.

Purpose:

* test whether the model truly uses tool condition.

---

### 11.8 Agent + Skill Library Baseline

LLM planner chooses tool-use action from predefined skills.

Purpose:

* compare end-to-end VLA/world-model route with explicit planning route.

This should be baseline only, not the main project route.

---

## 12. Evaluation Metrics

Possible evaluation dimensions:

### 12.1 Tool Necessity Accuracy

Whether the model correctly predicts if a tool is needed.

---

### 12.2 Tool-Use Decision Success

Whether the robot chooses to use or not use the tool appropriately.

---

### 12.3 Task Success Rate

Whether the full task succeeds.

---

### 12.4 Counterfactual Consistency

Whether predictions/actions change correctly when tool availability or tool type changes.

---

### 12.5 Action / Trajectory Difference

Whether tool-state changes produce meaningful trajectory or mode changes.

---

### 12.6 Failure Prediction

Whether the model predicts that not using the tool will fail.

---

### 12.7 Generalization

Performance on:

* unseen tools;
* unseen tasks;
* unseen rooms;
* unseen reachability configurations;
* unseen robot-tool distances.

---

## 13. Strongest Reviewer Objections

Any proposed paper in this project must answer these objections:

1. Is this just tool recognition rather than tool-awareness?
2. Is the model learning tool necessity or just visual shortcut?
3. Are negative samples truly causal failures?
4. Are AIGC videos physically meaningful?
5. Does video prediction actually help action?
6. Does tool state change the policy output?
7. Would a simple prompt or VLM affordance classifier solve it?
8. Is simulation enough without AIGC?
9. Is AIGC useful beyond data augmentation?
10. Does this generalize beyond one demo task?

---

## 14. Current Weekly Deliverable

The current near-term deliverable is a PQE-style or opening-report-style literature and project formulation PPT.

The PPT should not be a loose survey.
It should define the project’s research space.

Recommended PPT structure:

1. Project definition;
2. Why tool-awareness is not tool recognition;
3. Tool-awareness levels;
4. Literature map;
5. Representative baselines;
6. What existing work solves;
7. What existing work does not solve;
8. Data route comparison: real / simulation / AIGC / hybrid;
9. Positive-negative sample design;
10. Candidate research claims;
11. Strongest objections;
12. Minimal experiments;
13. Recommended next 2-week plan.

---

## 15. This Week’s Minimum Tasks

This week, focus on:

1. Read and classify 20-30 papers;
2. Build a literature matrix;
3. Identify 5-8 key limitations;
4. Identify 5 baseline categories;
5. Propose 3 candidate claims;
6. Design 10 positive-negative sample scenarios;
7. Prepare a 15-20 page PPT for advisor discussion.

Do not try to solve the entire project this week.

---

## 16. Forbidden Drift

When using AI agents for this project, do not let them shift the topic toward:

* generic embodied AI survey;
* pure LLM agent;
* pure skill library;
* pure multi-robot coordination;
* pure navigation;
* pure manipulation without tools;
* pure video generation without robot decision;
* pure simulator engineering.

If the agent starts drifting, redirect it to:

> tool necessity, tool-state-conditioned action, positive-negative data, AIGC/simulation validity, and mobile manipulation.

---

## 17. Core Project Reminder

The current project should be framed as:

> We are not simply teaching a robot how to use a tool.
> We are studying whether a mobile manipulator can learn when a tool is necessary, whether tool state changes future outcomes, and whether such tool-awareness can be learned from structured AIGC/simulation positive-negative data and transferred into action or trajectory decisions.

The project is currently early-stage.
The most important task is to find a small, provable claim inside this broad story.



# Four-legged Tool-Aware Mobile Manipulation Literature Package

本目录包含两轮材料：

- `20260622_base_information_for_research.md`：前置宽口径材料。
- `20260622_paper_family_comparison.md`：前置 paper-family 对比。
- `20260623_工具必要性文献调研/`：本轮完整调研，包括总结、领域地图、22 篇论文卡片、baseline、实验设计、PPT 大纲和论文索引。

本轮检索截止日期：**2026-06-23**。

使用约定：

- `事实`：论文明确提出、报告或实验支持的内容。
- `推断`：根据论文任务定义、数据和评测范围作出的研究判断。
- venue 无法从论文主页可靠确认时，统一写作 `arXiv preprint`，不猜测。
- “tool necessity”专指：在同一任务分布中，把“不使用工具”作为真实可选决策，并判断工具是必要、可选、无益或不可用；仅做工具选择、工具抓取或预设工具任务不算。
