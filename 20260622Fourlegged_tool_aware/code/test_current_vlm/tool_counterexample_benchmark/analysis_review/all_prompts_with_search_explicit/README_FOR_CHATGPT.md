# README For ChatGPT

This is an automatic text-based rereview handoff. It suggests analysis directions but is not final paper evidence.

## Data Scope
- Rows: 1188
- Models: 6 (ollama_gemma3_27b_it_q8_0, ollama_llama3_2_vision_11b_instruct_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M)
- Tasks: 11 (task_001, task_002, task_003, task_004, task_005, task_006, task_007, task_008, task_009, task_010, task_011)
- Prompt categories: {'generic_clean': 132, 'tool_prior_intervention': 198, 'strong_decomposition_intervention': 198, 'search_explicit_strong_decomposition_intervention': 198, 'diagnostic_probe': 198, 'embodiment_clean': 264}
- Rereview labels: {'true_fail': 386, 'parse_error': 273, 'true_pass': 529}
- Context risk labels: {'low': 990, 'unknown': 198}

## Rereview Rubric Summary
- Valid helper use requires a committed action chain, not just helper mention.
- Conditional helper-only plans are not counted as valid helper use.
- Tool-prior prompts are intervention checks, not clean evidence.
- Visual uncertainty remains unresolved until image-level review.

## Top 10 Findings
- parse_failure: 273 text-based labels
- helper_mention_without_use: 246 text-based labels
- visual_uncertainty: 179 text-based labels
- aggregation_failure: 134 text-based labels
- container_affordance_miss: 134 text-based labels
- helper_search_failure: 77 text-based labels
- tool_necessity_miss: 61 text-based labels
- physical_capacity_hallucination: 19 text-based labels
- wrong_helper_type: 6 text-based labels
- field_plan_inconsistency: 4 text-based labels

## Top Clean Counterexample Candidates
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_qwen3_vl_32b_instruct_q4_K_M / natural_free_plan: aggregation_failure;container_affordance_miss;physical_capacity_hallucination | 检查桌面上的矿泉水数量和摆放位置，确认是否可以一次性搬运全部瓶子。; 若可一次搬运，则小心拿起所有水瓶；否则分批搬运。; 移动到卧室，将水瓶放置在方便取用的位置（如桌子或茶几上）。; 返回原处检查是否有遗漏物品，并确保桌面整洁。 桌面上有6-7瓶矿泉水，体积适中且重量可控，可一次性搬运；若路径无障碍，则单次往返即可完成任务。但需先确认卧室位置及路径安全以确保高效与稳定执行。 一次性搬运所有水瓶可减少往返次数，提高效率；需评估自身承载能力以避免掉落或损坏。 搬运时注意保持...
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_qwen3_vl_30b_a3b_instruct_q4_K_M / natural_free_plan: aggregation_failure;container_affordance_miss | 检查周围环境以确保路径畅通无阻。; 拿起最靠近自己的那瓶矿泉水。; 沿着规划的路线前往卧室。; 在卧室内找到同学并递送水瓶。 由于有多个水瓶需要运送，且目的地为卧室，需多次往返以完成任务。 优先搬运所有水瓶，以减少往返次数，提高效率。 搬运时保持平稳，避免水瓶倾倒或掉落造成滑倒风险。 不清楚卧室的具体位置和路径细节。 { "task_understanding": "将桌上的矿泉水瓶从当前位置运送到卧室，供正在打牌的同学解渴。", "plan": [ "检查周围环境以确...
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_qwen3_5_35b / natural_free_plan: helper_mention_without_use;visual_uncertainty | Navigate towards the table and identify the specific location of the six or more water bottles, distinguishing them from books, laptops, and bags.; Grasp the water bottles securely; given their number (approx. 6-7), plan to carry them in...
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_minicpm_v4_5_q8_0 / natural_free_plan: aggregation_failure;container_affordance_miss;tool_necessity_miss | 拿起桌子右侧的几瓶矿泉水; 前往卧室 直接拿最靠近门口且数量较多的水，减少搬运次数和时间。 确保瓶子稳定，避免倾倒或洒漏。 未明确卧室的具体位置及同学的位置，需根据环境判断路线。 { "task_understanding": "需要将桌上的矿泉水送到卧室给正在打牌的同学。", "plan": [ "拿起桌子右侧的几瓶矿泉水", "前往卧室" ], "estimated_number_of_trips": "single", "efficiency_considerat...
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_gemma3_27b_it_q8_0 / natural_free_plan: aggregation_failure;container_affordance_miss;physical_capacity_hallucination | Navigate to the table with the water bottles.; Grasp and lift one or more water bottles (depending on carrying capacity).; Navigate to the bedroom where the students are playing cards.; Place the water bottles within reach of the student...
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_qwen3_vl_32b_instruct_q4_K_M / efficient_safe_free_plan: helper_mention_without_use;visual_uncertainty | 检查并确认所有矿泉水瓶是否稳固可搬运，避免倾倒或漏水。; 一次性取走全部矿泉水瓶（共6瓶），放置于机器人承载平台或托盘上，确保平衡与稳定。; 导航至卧室，避开障碍物，平稳移动。; 将水瓶安全送达卧室指定位置（如桌面或地面），并确认同学可方便取用。; 返回原位或待命状态。 一次性搬运所有水瓶可最大化效率并减少往返次数。当前桌面上有6瓶水，体积适中且重量可控，适合单次运输。需确保路径安全、承载稳定，并在送达后确认物品可用性以完成任务。 一次性搬运全部水瓶，避免多次往返，提高...
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_qwen3_vl_30b_a3b_instruct_q4_K_M / efficient_safe_free_plan: aggregation_failure;container_affordance_miss | 检查周围环境，确认路径无障碍物。; 拿起最靠近自己的那瓶水。; 沿直线路径前往卧室。; 在卧室内找到同学并递送水瓶。; 返回原处，重复上述步骤，直到所有水瓶送达。 为了高效完成任务并确保安全，应分批运输，并优先处理易取的物品。 优先搬运距离近、易于抓取的物品，并规划最优路径以减少移动次数和时间。 在搬运过程中保持平稳，避免水瓶倾斜或掉落造成滑倒或损坏。 不清楚卧室的具体位置以及是否有其他障碍物；不确定是否需要一次性运送所有水瓶。 { "task_understandin...
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_qwen3_5_35b / efficient_safe_free_plan: helper_mention_without_use;visual_uncertainty | 移动到桌边，定位并抓取第一批水瓶（约3-4瓶）。; 携带水瓶前往卧室并将水放置在安全位置。; 返回桌边抓取剩余的水瓶。; 将剩余水瓶搬运至卧室完成交付。 尝试一次抓握尽可能多的水瓶以减少往返次数；优先处理桌面上排列整齐、易于抓取的一组水。 由于水瓶数量较多且为圆柱形易滚动物体，需确保机械手抓握稳固防止滑落或倾倒造成危险；移动过程中保持平稳以防液体溅出。 未明确卧室的具体方位及内部布局（如是否有足够空间放置所有水），也未确认是否可以使用容器辅助搬运以提高效率。 { "ta...
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_minicpm_v4_5_q8_0 / efficient_safe_free_plan: aggregation_failure;container_affordance_miss;physical_capacity_hallucination | 识别并定位桌面上的矿泉水瓶（共7瓶）; 拿起所有矿泉水瓶，确保不遗漏任何一瓶; 前往卧室位置 任务要求尽快送水，一次性拿取所有矿泉水可以提高效率。 一次性拿取所有矿泉水以减少往返次数。 小心搬运，避免瓶子倾倒或掉落。 未明确卧室的具体位置和距离；未说明是否需要其他物品伴随。 { "task_understanding": "将桌上的矿泉水送到卧室给正在打牌的同学。", "plan": [ "识别并定位桌面上的矿泉水瓶（共7瓶）", "拿起所有矿泉水瓶，确保不遗漏任何一瓶...
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_gemma3_27b_it_q8_0 / efficient_safe_free_plan: aggregation_failure;container_affordance_miss;physical_capacity_hallucination | Navigate to the table with the water bottles.; Grasp and lift all the water bottles.; Navigate to the bedroom where the students are playing cards.; Place the water bottles on a stable surface near the students. The image shows several b...

## Top Prompted Improvement Cases
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_qwen3_vl_32b_instruct_q4_K_M: natural_free_plan fail -> tool_prior_free_plan pass
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_qwen3_vl_32b_instruct_q4_K_M: natural_free_plan fail -> tool_prior_free_plan pass
- task_007 / Weixin Image_20260629231746_401_27.jpg / ollama_gemma3_27b_it_q8_0: natural_free_plan fail -> tool_prior_free_plan pass
- task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / ollama_qwen3_vl_32b_instruct_q4_K_M: natural_free_plan fail -> tool_prior_free_plan pass
- task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / ollama_qwen3_vl_30b_a3b_instruct_q4_K_M: natural_free_plan fail -> tool_prior_free_plan pass
- task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / ollama_gemma3_27b_it_q8_0: natural_free_plan fail -> tool_prior_free_plan pass
- task_009 / Weixin Image_20260629231751_404_27.jpg / ollama_gemma3_27b_it_q8_0: natural_free_plan fail -> tool_prior_free_plan pass
- task_010 / Weixin Image_20260629231750_403_27.jpg / ollama_minicpm_v4_5_q8_0: natural_free_plan fail -> tool_prior_free_plan pass
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_qwen3_5_35b: natural_free_plan_humanoid_dual_arm fail -> tool_prior_free_plan_humanoid_dual_arm pass
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_gemma3_27b_it_q8_0: natural_free_plan_humanoid_dual_arm fail -> tool_prior_free_plan_humanoid_dual_arm pass

## Top Robust Failures Across Clean/Tool-Prior
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_qwen3_vl_30b_a3b_instruct_q4_K_M: clean and tool-prior both true_fail
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_minicpm_v4_5_q8_0: clean and tool-prior both true_fail
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_gemma3_27b_it_q8_0: clean and tool-prior both true_fail
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_qwen3_vl_32b_instruct_q4_K_M: clean and tool-prior both true_fail
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_qwen3_vl_30b_a3b_instruct_q4_K_M: clean and tool-prior both true_fail
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_minicpm_v4_5_q8_0: clean and tool-prior both true_fail
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_gemma3_27b_it_q8_0: clean and tool-prior both true_fail
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_minicpm_v4_5_q8_0: clean and tool-prior both true_fail
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_gemma3_27b_it_q8_0: clean and tool-prior both true_fail
- task_005 / Weixin Image_20260629231743_399_27.jpg / ollama_gemma3_27b_it_q8_0: clean and tool-prior both true_fail

## Main Uncertainty Sources
- Image visibility of helpers/targets was not checked.
- Parse-recoverable outputs need manual interpretation.
- Some helper mentions may be background or conditional rather than committed use.
- Strong decomposition prompt rows may still need targeted label audit; see `label_inconsistency_audit.md` when available.
- Check `aggregate_findings.md` context usage warnings before interpreting long-prompt runs.

## Generated Files
- `aggregate_findings.md`: aggregate text-rereview metrics.
- `task_family_summary.csv`: per-task metrics.
- `model_prompt_matrix.csv`: per-model/prompt matrix.
- `prompt_intervention_delta.md`: clean vs tool-prior comparisons.
- `counterexample_candidates_ranked.md`: ranked clean failure candidates.
- `label_inconsistency_audit.md`: high-risk label consistency audit when generated by rereview.

## Warning
Automatic text rereview is not final paper evidence. Selected claims require image-level human review.
