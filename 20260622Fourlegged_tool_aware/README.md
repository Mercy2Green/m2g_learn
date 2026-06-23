
# PROJECT_tool_aware_mobile_manipulation.md

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
