# Counterexample Candidates Ranked

Only primary clean prompts are ranked here. Tool-prior and diagnostic rows are excluded.

## 1. task_001 / Weixin Image_20260629231738_395_27.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, physical_capacity_hallucination, helper_mention_without_use, visual_uncertainty, tool_necessity_miss
- Evidence quote: 检查桌面上的矿泉水数量和摆放位置，确认是否可以一次性搬运全部瓶子。; 若可一次搬运，则小心拿起所有水瓶；否则分批搬运。; 移动到卧室，将水瓶放置在方便取用的位置（如桌子或茶几上）。; 返回原处检查是否有遗漏物品，并确保桌面整洁。 桌面上有6-7瓶矿泉水，体积适中且重量可控，可一次性搬运；若路径无障碍，则单次往返即可完成任务。但需先确认卧室位置及路径安全以确保高效与稳定执行。 一次性搬运所有水瓶可减少往返次数，提高效率；需评估自身承载能力以避免掉落或损坏。 搬运时注意保持...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 2. task_001 / Weixin Image_20260629231738_395_27.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty, physical_capacity_hallucination
- Evidence quote: 检查并确认所有矿泉水瓶是否稳固可搬运，避免倾倒或漏水。; 一次性取走全部矿泉水瓶（共6瓶），放置于机器人承载平台或托盘上，确保平衡与稳定。; 导航至卧室，避开障碍物，平稳移动。; 将水瓶安全送达卧室指定位置（如桌面或地面），并确认同学可方便取用。; 返回原位或待命状态。 一次性搬运所有水瓶可最大化效率并减少往返次数。当前桌面上有6瓶水，体积适中且重量可控，适合单次运输。需确保路径安全、承载稳定，并在送达后确认物品可用性以完成任务。 一次性搬运全部水瓶，避免多次往返，提高...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 3. task_001 / Weixin Image_20260629231738_395_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查桌面所有水瓶的位置和数量，确认是否全部需要搬运。; 使用双手同时抓取两瓶水（每次最多两瓶），分批搬运至卧室。; 在每次搬运后返回原位继续取水，直至所有水瓶被送达卧室。 桌面上共有6瓶矿泉水，双手每次可稳定携带2瓶，因此预计需要3次往返。任务目标清晰为送水至卧室，但具体送达位置和路径未知，故计划以安全高效为核心原则执行。 优先使用双手同时抓取以减少往返次数；避免单手搬运导致效率降低或掉落风险。 确保每次搬运的水瓶数量不超过两只，防止因重量不均或重心偏移造成滑落或损坏；...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 4. task_001 / Weixin Image_20260629231738_395_27.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查桌面所有水瓶的位置和数量，确认共有6瓶水（均为透明塑料瓶，绿色瓶盖）。; 使用双手同时抓取两组水瓶：左手抓取左侧三瓶，右手抓取右侧三瓶，确保每只手稳定握持一组，避免掉落。; 携带水瓶前往卧室，途中保持手臂平稳，防止晃动导致瓶子碰撞或漏水。; 到达卧室后，将所有水瓶放置在安全、易于拿取的位置（如桌面或茶几），并确认同学可方便饮用。; 返回原处，检查是否还有其他需要运送的物品。 6瓶水体积适中，可由双手分组稳定抓取一次性运送到目的地。桌面空间充足且物品摆放集中，无需额外...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 5. task_001 / Weixin Image_20260629231738_395_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查桌面水瓶数量和摆放位置，确认是否可一次性抓取或需分批搬运。; 若一次无法稳定携带所有水瓶，则优先抓取靠近边缘、易于夹持的一组（如2-3瓶），确保机械臂平衡与夹爪稳定性。; 移动至卧室并放置水瓶在安全、易取的位置，如桌面或茶几上。; 返回原桌继续搬运剩余水瓶，重复上述步骤直至全部送达。 水瓶数量较多且无物理捆绑，夹爪一次无法稳定携带全部。需分批运输以确保安全与稳定性。同时，卧室环境和放置点不详，可能需要现场调整策略。 由于夹爪一次仅能稳定携带少量物体（建议不超过3瓶）...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 6. task_001 / Weixin Image_20260629231738_395_27.jpg / efficient_safe_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查桌面水瓶数量和摆放位置，确认是否可以一次性稳定携带部分水瓶（如2-3瓶）。; 若无法一次携带全部，则优先携带靠近边缘且易于抓取的水瓶，分批运送至卧室。; 每次搬运后返回原位继续取剩余水瓶，直至所有水瓶送达卧室。 桌面上共有6-7瓶水，单次搬运若仅限1瓶则需多次往返，效率较低。但若能稳定同时抓取2-3瓶（如并排摆放且间距合适），可减少至2-3趟。由于未提供卧室位置和路径信息，无法精确规划路线，因此计划以分批高效运输为主，并优先处理易获取的水瓶。 尽量减少往返次数，通过...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 7. task_002 / Weixin Image_20260629231739_396_27.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: helper_search_failure, aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty, physical_capacity_hallucination
- Evidence quote: 检查桌面水瓶数量及摆放位置，确认是否可一次性搬运全部水瓶。; 若可一次搬运，则抓取所有水瓶并移动至卧室；否则分批搬运。; 将水瓶安全放置于卧室指定区域（如桌子或地面），确保不倾倒、不洒漏。 桌面上有7-8瓶水，若机器人具备足够承载能力且路径畅通，则可一次性搬运完成任务。优先考虑单次高效运输以减少往返次数。 一次性搬运全部水瓶可减少往返次数，提高效率；需评估自身负载能力是否允许。 搬运时确保水瓶稳固排列，避免滑落或碰撞造成损坏或洒漏；移动路径应无障碍物。 未明确卧室位置、...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 8. task_002 / Weixin Image_20260629231739_396_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_search_failure
- Evidence quote: 检查桌面右侧区域，确认所有矿泉水的位置和数量。; 使用双手同时抓取两组瓶子（每只手最多稳定拿2-3瓶），分批搬运以确保安全与效率。; 前往卧室并交付水瓶给同学。; 返回原处继续搬运剩余水瓶，直至全部送达。 桌面上共有约7-8瓶矿泉水，双手可分批高效搬运。由于水瓶数量适中且体积较小，预计只需2-3次往返即可完成任务。需注意安全抓握和路径通畅性以确保快速送达。 优先采用双手同时抓取多瓶的方式减少往返次数；避免单手携带过多导致失衡或掉落。 每只手最多稳定拿2-3瓶水，防止因重...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: text-only evidence; still verify image before claims

## 9. task_002 / Weixin Image_20260629231739_396_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_search_failure, physical_capacity_hallucination
- Evidence quote: 检查桌面水瓶数量和摆放位置，确认是否可以一次性安全携带部分瓶子。; 分批抓取并搬运水瓶至卧室（每次最多携带1-2瓶以确保稳定）。; 在卧室放置水瓶后返回原位继续搬运剩余水瓶。 根据任务要求和物理限制（单次携带能力、平衡性），必须分批运输。同时需要确保搬运过程中的稳定性和安全性，避免损坏物品或造成意外。 由于夹爪一次只能稳定携带少量物体，且水瓶数量较多（约7-8瓶），需分多次运输以确保安全和效率。 搬运过程中必须保持身体平衡，避免因负载不均或移动过快导致倾倒；每次仅抓取1...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: text-only evidence; still verify image before claims

## 10. task_004 / Weixin Image_20260629231742_398_27.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查桌面上可用的饮品（如瓶装水、盒装饮料）和食物（如零食包、苹果），选择适合分享的项目。; 将选定的饮品和食物整理并携带至客厅区域。; 放置物品在客厅合适的位置，确保易于取用。 当前桌面上有多种可食用零食和饮品可供选择，且物品集中于一张桌子，一次性取用效率高。优先选取瓶装水（安全稳定）和独立包装的零食（便于分享），苹果也可作为健康选项携带。无需多次往返即可完成任务。 一次性选取所有合适的饮品和食物，避免多次往返；优先选择体积小、易携带的物品（如瓶装水、独立包装零食）。...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 11. task_004 / Weixin Image_20260629231742_398_27.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查桌面上可用的食物和饮料：包括苹果、独立包装零食（如饼干/糕点）、绿色纸盒装饮品（可能是果汁或茶饮）以及瓶装水。; 选择一个苹果和一包零食作为食物，同时拿取绿色纸盒饮品和瓶装水作为饮品，确保种类多样且便于携带。; 使用双手分别持握：左手拿苹果与纸盒饮品组合，右手拿零食与瓶装水组合（或根据稳定性调整），避免掉落。; 前往客厅并将物品放置在聊天区域的合适位置（如茶几）供人取用。 当前桌面上有多种可食用和可饮用物品，通过合理组合并利用双臂同时抓取，可在一次行动中完成任务。优...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 12. task_004 / Weixin Image_20260629231742_398_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查桌面上可用的饮品（如瓶装水、盒装饮料）和食物（如独立包装零食、苹果），确认哪些适合携带并分享。; 选择一个饮品（例如瓶装水或绿色盒装饮料）和一种食物（例如苹果或一包零食），确保它们可以被夹爪稳定抓取。; 移动到客厅区域，将选定的饮品和食物放置在合适的位置供人享用。 基于当前桌面可见物品和机器人能力限制（单次仅能稳定携带一个物体），选择最实用且安全的组合进行一次搬运。若需更多物品，则需多次往返，但任务要求为‘拿些’，故一次取用合理。 优先选择体积小、重量轻且易于携带的...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 13. task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty, tool_necessity_miss
- Evidence quote: 移动到沙发前方，确认遥控器在沙发底部的位置。; 伸展机械臂尝试够到遥控器；若直接无法触及，则调整位置或使用夹爪辅助抓取。; 成功拾取后，将遥控器移出沙发下方并放置于安全可见处。 遥控器位于沙发底部且可见，但因空间限制需谨慎操作。通过分步计划确保安全、稳定地完成任务，并考虑潜在的物理约束。 尽量一次性完成任务，避免重复移动；优先尝试直接抓取以减少操作步骤。 在伸展机械臂时确保身体平衡，防止因过度前倾导致失稳；夹爪需稳定抓握遥控器以防掉落。 沙发下方空间深度和遥控器具体位置...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 14. task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / efficient_safe_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, tool_necessity_miss, visual_uncertainty
- Evidence quote: 移动至沙发前方，确保机械臂可伸入沙发底部间隙。; 使用夹爪小心探入沙发下方，定位并抓取遥控器。; 将遥控器从沙发下取出，并保持稳定握持。; 移动到指定放置位置（如茶几或用户手中）并释放遥控器。 沙发下方空间虽狭窄但遥控器可见且无遮挡，机械臂可尝试直接抓取。一次操作即可完成任务，无需多次往返。若首次尝试失败，则需检查是否因空间限制导致无法触及，并考虑调整姿态或使用辅助手段。 一次性完成抓取与放置，避免多次往返；优先使用机械臂直接操作以减少移动次数。 在伸入沙发下方时需确保...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 15. task_002 / Weixin Image_20260629231739_396_27.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_search_failure
- Evidence quote: 检查桌面上的水瓶数量和摆放位置，确认是否可以一次性搬运全部水瓶。; 若无法一次搬运所有水瓶，则规划分批运输路线，优先确保安全高效地运送第一批次。; 移动至卧室，将水瓶放置在方便取用的位置（如桌面或茶几）。; 返回原桌继续搬运剩余水瓶，直至全部送达。 根据图像可见桌上有约7-8瓶矿泉水，体积较大且易滑落，一次性搬运存在风险；同时任务要求‘尽快’送达，因此分批运输是更合理、安全的选择。路径和卧室位置未明确，故需在执行前确认环境无障碍。 由于水瓶数量较多且体积较大，一次性搬运...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: text-only evidence; still verify image before claims

## 16. task_002 / Weixin Image_20260629231739_396_27.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_search_failure
- Evidence quote: 检查桌面右侧区域，确认所有矿泉水瓶的位置和数量（共7瓶）。; 使用双手同时抓取两组水瓶：左手抓取3瓶，右手抓取4瓶，确保每只手的负载稳定且不溢出。; 携带水瓶前往卧室，途中保持平稳移动以避免碰撞或洒漏。; 到达卧室后，将所有水瓶放置在方便拿取的位置（如桌面或茶几）。; 返回原位置确认任务完成。 通过一次性携带全部水瓶并合理分配双手负载，可在保证安全的前提下最大化效率；同时考虑了移动过程中的稳定性和潜在路径不确定性。 一次性携带全部7瓶水可避免多次往返，提高效率；双手同时...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: text-only evidence; still verify image before claims

## 17. task_002 / Weixin Image_20260629231739_396_27.jpg / efficient_safe_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_search_failure
- Evidence quote: 检查桌面右侧水瓶堆叠情况，确认是否可以稳定抓取两到三瓶作为一组进行搬运（避免单次携带过多导致失衡）。; 若可稳定抓取，则一次携带2-3瓶水移动至卧室；否则逐瓶运送。; 重复上述步骤直至所有水瓶被送达卧室，并确保放置平稳，便于同学取用。 基于当前桌面布局，右侧有7-8瓶矿泉水集中摆放。通过分组搬运可显著提升效率，同时避免因单次携带过多导致失衡或掉落风险。需先评估物理组合的可行性再执行。 优先尝试一次性搬运多瓶水以减少往返次数，但需保证机械臂抓握稳定性和移动过程中的平衡性。...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: text-only evidence; still verify image before claims

## 18. task_004 / Weixin Image_20260629231742_398_27.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: 检查桌面上可用的饮品和食物选项; 选择合适的饮品（如瓶装水或盒装饮料）和食物（如小包装零食或苹果）; 将选定的饮品和食物收集到一起; 移动至客厅并将物品放置在合适的位置 桌面上有多种可选的饮品（瓶装水、盒装饮料）和食物（小包装零食、苹果），可以组合成一份合适的点心。一次性携带能高效完成任务，但若客厅距离较远或人数较多，可能需要多次往返；当前信息不足以判断是否需额外准备物品。 一次性携带所有选定物品以减少往返次数，提高效率。 确保携带过程中饮品和食物不会洒落或掉落，避免造...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: text-only evidence; still verify image before claims

## 19. task_004 / Weixin Image_20260629231742_398_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查桌面上可用的饮品（如瓶装水、盒装饮料）和食物（如零食包、苹果），选择适合分享的组合。; 使用双手分别拿取一个饮品和一份食物（例如一瓶水和一袋零食，或一个苹果和一盒饮料），确保抓握稳定。; 移动到客厅区域，将物品放置在聊天人群附近可及的位置（如茶几或小桌）。; 返回原位或等待进一步指令。 当前桌面已有多种可食用和可饮用的物品（如瓶装水、盒装饮料、苹果、零食包），具备一次性完成任务的基础条件。选择单次携带合理组合，既高效又安全。 优先选择体积适中、易于携带且适合分享的饮...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 20. task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty, aggregation_failure, container_affordance_miss
- Evidence quote: 移动到沙发前方，靠近遥控器的位置; 伸出手臂或使用机械爪探入沙发底座下方以抓取遥控器; 将遥控器取出并放置在安全、易取用的区域（如沙发旁的地面上） 根据图像判断遥控器位于沙发下方且可见，任务可直接执行。需注意操作空间有限，确保机械臂能顺利伸入并抓取目标。 直接操作，无需多次往返或额外工具，一次完成任务即可。 确保在伸入沙发下方时避免碰撞家具结构或自身倾覆；地面光滑需注意移动稳定性。 遥控器是否被障碍物遮挡或卡住？当前图像未显示其完整状态，可能需要轻微调整位置以确认抓取可...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 21. task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty, aggregation_failure, container_affordance_miss
- Evidence quote: 移动到沙发前方，确认遥控器的具体位置和可及性。; 伸展机械臂或使用抓取工具进入沙发下方，拾取遥控器。; 将遥控器安全移出并放置在指定区域（如沙发旁的茶几上）。; 完成任务后返回原位或待命。 图像显示遥控器位于沙发下方且位置清晰可见，无需额外搜索。直接执行拾取操作效率最高，但需先检查空间是否允许安全进入并完成抓取。 直接定位目标物，避免不必要的移动；使用一次抓取动作即可完成任务，减少往返次数。 在伸入沙发下方时需确保机械臂稳定，防止碰撞或刮擦家具；地面光滑，移动时注意防滑...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 22. task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty, aggregation_failure, container_affordance_miss
- Evidence quote: 检查沙发下方空间，确认遥控器位置和可及性。; 使用一只手或夹爪伸入沙发下方抓取遥控器。; 将遥控器取出并放置在安全、可见的位置。 根据图像可见，遥控器位于沙发下方但未完全隐藏，且地面平坦无障碍。机器人可尝试直接伸入抓取；若空间狭窄则需调整姿态或使用工具辅助。 直接操作，无需多次往返；优先使用单次动作完成任务。 确保手臂伸入时不会刮伤地板或损坏沙发结构；抓取遥控器时保持稳定避免掉落。 不确定遥控器是否被其他物体遮挡，或其具体位置是否在深窄区域中难以触及。 { "task_...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 23. task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 伸展左臂进入沙发底部空间，定位并抓取遥控器。; 确认遥控器被稳定握持后，将手臂缓慢抽出沙发下方。; 将遥控器放置在安全可见的位置（如沙发旁的地板或附近桌面上） 基于图像可见性判断遥控器位于可触及范围，且地面平坦无障碍；使用单臂操作即可完成任务，无需额外工具或多次往返。 直接使用单臂操作避免往返；利用光滑地面减少移动阻力，提高抓取效率。 确保手臂伸入时不会碰撞沙发结构或刮伤地板；取出遥控器后保持稳定握持以防掉落。 遥控器是否被其他物体遮挡、其具体位置深度未知，可能需要微调...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 24. task_004 / Weixin Image_20260629231742_398_27.jpg / efficient_safe_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: 检查桌面，确认哪些物品是适合携带的食品和饮料; 优先选择易于携带且稳定的物品，如瓶装水、苹果和独立包装的零食; 使用夹爪一次携带一个主要饮品（如瓶装水）和少量零食组合（如几包小包装食品），确保负载稳定; 移动到客厅，保持身体平衡，避免碰撞或掉落; 将所携物品放置在合适的位置，供人们取用 为了高效完成任务并确保安全，机器人应优先选择稳定且易于携带的饮品和食物组合，并尽量减少移动次数。由于无法确定具体需求，选择通用性较强的物品（如瓶装水、苹果和小包装零食）以满足大多数情况。...
- Why it is a counterexample: primary clean prompt failed under text rereview with 3 model(s).
- Caveat: text-only evidence; still verify image before claims

## 25. task_005 / Weixin Image_20260629231743_399_27.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty, aggregation_failure, container_affordance_miss
- Evidence quote: 检查桌面所有餐具，确认需要回收的物品包括白色带勺小杯、两个白色碗、一个不锈钢碗和一个金属保温杯。; 将上述餐具小心叠放或分组放置于可移动区域（如托盘或机器人承载区），避免碰撞或掉落。; 携带餐具前往厨房区域，确保路径畅通无阻。; 将餐具放入厨房水槽或指定清洗区域。 通过一次性收集所有可见用过的餐具，可高效完成任务。路径规划应优先考虑安全与稳定性，避免多次往返增加风险和时间成本。 一次性收集所有物品可减少往返次数；优先选择稳定堆叠方式以避免中途掉落导致额外操作。 金属碗和...
- Why it is a counterexample: primary clean prompt failed under text rereview with 3 model(s).
- Caveat: needs image verification

## 26. task_005 / Weixin Image_20260629231743_399_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty, aggregation_failure, container_affordance_miss
- Evidence quote: 检查桌面所有餐具，确认需要回收的物品：白色带勺小杯、两个白色瓷碗、一个不锈钢碗、一个金属保温杯。; 使用双手分别抓取两组物品（例如左手拿小杯和一个白碗，右手拿另一个白碗和不锈钢碗），避免一次携带过多导致不稳定。; 将收集到的餐具安全运送到厨房区域（如水槽或橱柜附近）。; 若金属保温杯内有液体，需先倾倒再搬运；否则直接搬运。 桌面存在多个可回收的餐具物品，需分批安全搬运至厨房区域；由于双手操作限制和稳定性考虑，不宜一次性携带全部物品，因此计划分组处理以确保效率与安全。 优...
- Why it is a counterexample: primary clean prompt failed under text rereview with 3 model(s).
- Caveat: needs image verification

## 27. task_005 / Weixin Image_20260629231743_399_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查桌面所有可用的餐具，确认哪些是需要回收的用过物品。; 逐个拾取餐具，每次仅携带一个稳定物体，避免掉落或碰撞。; 移动至厨房区域，将每个餐具放置在指定位置（如水槽、碗碟架等）。; 重复上述步骤直至所有餐具处理完毕。 根据任务要求和机器人物理限制，必须分步处理每个餐具以确保安全与稳定性；同时因缺乏厨房布局信息，无法预估单次搬运数量或路径优化。 由于机械臂一次只能稳定携带一个物体，且部分物品形状不规则或易滑动（如金属杯、碗），需分多次搬运以确保安全与效率。 在移动过程中保...
- Why it is a counterexample: primary clean prompt failed under text rereview with 3 model(s).
- Caveat: needs image verification

## 28. task_009 / Weixin Image_20260629231751_404_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b
- Failure modes: helper_mention_without_use, visual_uncertainty, wrong_helper_type, aggregation_failure, container_affordance_miss
- Evidence quote: Check nearby area for obstacles (bottles, broom) and locate all visible paper targets on the floor.; Pick up one or two pieces of paper simultaneously using both hands to maximize efficiency, then move towards the hanging trash bin locat...
- Why it is a counterexample: primary clean prompt failed under text rereview with 3 model(s).
- Caveat: needs image verification

## 29. task_009 / Weixin Image_20260629231751_404_27.jpg / efficient_safe_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b
- Failure modes: aggregation_failure, container_affordance_miss, wrong_helper_type
- Evidence quote: 扫描环境以确认所有纸团的精确位置坐标及可用的垃圾存放容器。; 移动至距离当前位姿最近的纸团处，调整底盘姿态保持平衡，使用夹爪抓取并提起物体。; 携带单个物体移动至收集点（如右上角挂篮或簸箕），松开夹爪释放物体后返回继续作业。; 重复上述拾取与投放流程，按空间顺序优先处理最近的目标以减少往返距离，直至地面清洁完毕。 采用‘最近邻’策略规划拾取路径，减少底盘在狭长区域内的无效移动；利用左侧簸箕或右侧挂篮作为收集点以减少单次搬运距离。 不确定右上角挂篮是否已准备好作为垃圾桶（...
- Why it is a counterexample: primary clean prompt failed under text rereview with 3 model(s).
- Caveat: text-only evidence; still verify image before claims

## 30. task_003 / 372f92c1ce9c87231d199c1102dcf7b4.jpg / efficient_safe_free_plan

- Models failed: ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: 合上正在使用的MacBook屏幕，确保数据已保存。; 将左侧散乱的纸质文件或报纸叠好整理在一起。; 拿起右侧的水杯和整理的文件，连同笔记本电脑一起放入黑色的斜挎包中。 优先处理核心移动设备（电脑）和个人随身物品（水杯、文件），忽略固定办公设备（显示器）。一次性完成打包动作以减少往返时间。 在拿取笔记本电脑时注意避开桌面上的线缆，防止拉扯导致电源适配器或外设掉落损坏；整理纸张时要小心不要弄乱其他小物件。 不确定右侧的电池盒和玩偶是否需要带走（可能是办公室公用物品），计划中...
- Why it is a counterexample: primary clean prompt failed under text rereview with 2 model(s).
- Caveat: needs image verification

## 31. task_005 / Weixin Image_20260629231743_399_27.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查桌面区域，确认所有目标物品的位置和状态（包括白色马克杯、不锈钢大碗、叠放的白碗及保温杯）。; 利用双臂同时抓取稳定的物体组合以提高效率（例如：左手抓握一组碗或杯子，右手抓握另一个较大的金属碗或水杯），尽可能减少单次搬运数量。; 将抓取到的餐具安全运送至厨房指定位置并放下；若未全部拿完则重复上述步骤直到桌面清空。 利用双臂同时操作，每次尝试搬运2-3个主要物体以减少往返次数。 确保抓取时陶瓷碗和金属杯的稳定性，防止滑落破碎；避免过度堆叠导致重心不稳。 未明确厨房的具体...
- Why it is a counterexample: primary clean prompt failed under text rereview with 2 model(s).
- Caveat: needs image verification

## 32. task_005 / Weixin Image_20260629231743_399_27.jpg / efficient_safe_free_plan_quadruped_single_arm

- Models failed: ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查桌面，识别所有待回收的餐具：白色带勺小杯、两个叠放的白瓷碗、一个不锈钢碗、一个金属保温杯。; 优先将可稳定携带的物品组合拾取（如两个叠放的白瓷碗可一次夹取），其余单个物品分次搬运。; 移动至厨房区域，依次放置所有餐具于指定清洗或收纳位置。 桌面存在多个可回收餐具，部分可组合搬运以提高效率。金属杯和不锈钢碗需单独处理以防倾倒或掉落。移动路径应确保稳定性和安全性，避免多次往返。 优先组合稳定堆叠的物品以减少往返次数；避免同时携带多个松散、易倾倒的物体。 搬运时确保夹爪抓...
- Why it is a counterexample: primary clean prompt failed under text rereview with 2 model(s).
- Caveat: needs image verification

## 33. task_006 / Weixin Image_20260629231745_400_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0
- Failure modes: helper_mention_without_use, visual_uncertainty, aggregation_failure, container_affordance_miss
- Evidence quote: 检查所有可见区域以确认目标物体位置，特别是靠近墙壁或家具下方可能被遮挡的地方。; 使用机械臂逐一拾取地面上的小物件，并确保夹爪稳定抓住每个物品（注意：一次只能携带一个普通小物体）。; 将拾取到的物品移动至指定篮子中放置。 任务需要多次往返于拾取点和放置点之间，并且由于物体分布较散乱，预计会有多次移动。 尽量减少不必要的移动，优先处理容易到达且数量较多的区域。 保持身体平衡，在拾取和搬运过程中避免倾倒或掉落物品。注意地面平整性以防止滑倒。 无法确定篮子内部空间是否足够容纳...
- Why it is a counterexample: primary clean prompt failed under text rereview with 2 model(s).
- Caveat: needs image verification

## 34. task_007 / Weixin Image_20260629231746_401_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查椅子上所有衣物的位置和状态，确认可抓取的衣物。; 用右手拿起深蓝色T恤，左手拿起绿色条纹裤子，同时抓取两个物体。; 将衣物放入旁边的塑料篮中。; 如果一次无法装下所有衣物，则重复上述步骤直到全部收集完毕。; 提着装有衣物的篮子前往洗衣区。 椅子上衣物分布清晰且易于接近，可同时使用双手抓取多个物体。由于篮子容量和洗衣区距离不明确，预计需要少量往返，但整体任务可通过高效分步执行完成。 优先一次性抓取多个稳定物体，减少往返次数。 确保每次抓取时衣物不会滑落，避免因负载不稳...
- Why it is a counterexample: primary clean prompt failed under text rereview with 2 model(s).
- Caveat: needs image verification

## 35. task_007 / Weixin Image_20260629231746_401_27.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: 使用左手拿起搭在椅背左侧的绿黑条纹短裤（或上衣），右手同时拿起搭在椅背右侧的深蓝色连帽衫。; 将椅子座面上的绿黑条纹裤子和深蓝色T恤依次拾起，放入双手已持有的衣物中，确保每只手稳定抓握一组衣物（如左手持两件，右手持两件）。; 携带所有衣物走向洗衣区，途中保持平衡与稳定。; 到达洗衣区后，将衣物全部投入洗衣篮或洗衣机内。 衣物集中在一把椅子上，数量适中（共4件），可由双臂一次性抓取并搬运；使用双手分组持握能最大化单次运输量，减少往返次数，符合高效安全原则。 通过同时使用双...
- Why it is a counterexample: primary clean prompt failed under text rereview with 2 model(s).
- Caveat: needs image verification

## 36. task_009 / Weixin Image_20260629231751_404_27.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: 检查垃圾篓是否已满或可接受放置更多物品。如果可以，则将垃圾篓移动到更方便的位置以腾出空间。; 使用右手拿起最近的一个纸屑，并将其放入垃圾篓中。; 重复上述步骤，用左手拿取剩余的纸屑并丢入垃圾篓，确保每只手都尽量多地处理一个物体以减少往返次数。 通过同时使用两只手来最大化效率，并将多次小动作整合为较少的整体行动。 确保在移动垃圾篓和处理纸屑时不会打翻或损坏周围的物品，如扫帚、垃圾桶等。 { "task_understanding": "需要清理地面上的纸屑，使地面干净。"...
- Why it is a counterexample: primary clean prompt failed under text rereview with 2 model(s).
- Caveat: text-only evidence; still verify image before claims

## 37. task_009 / Weixin Image_20260629231751_404_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: 使用机械臂夹爪逐一拾取地上的纸屑; 将纸屑放入旁边的垃圾桶中 根据纸屑分布情况和数量，可能需要多次往返移动以完成清理。 在拾取过程中保持身体平衡，并确保夹爪稳定抓取每个纸屑，避免掉落或损坏。 地面瓷砖的缝隙较深且狭窄，机械臂是否能顺利伸入并拾取到所有位置的纸屑存在不确定性。 { "task_understanding": "需要清理地面上的纸屑，保持环境整洁。", "plan": [ "使用机械臂夹爪逐一拾取地上的纸屑", "将纸屑放入旁边的垃圾桶中" ], "esti...
- Why it is a counterexample: primary clean prompt failed under text rereview with 2 model(s).
- Caveat: text-only evidence; still verify image before claims

## 38. task_003 / 372f92c1ce9c87231d199c1102dcf7b4.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_qwen3_5_35b
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查右侧黑色背包的开口状态及内部容量，确认是否已准备好收纳电脑; 使用左手合上笔记本电脑屏幕并关闭电源，右手辅助稳定机身; 将笔记本电脑放入右侧的黑色包中；随后整理左侧散落的纸张和杂物，将其归拢或移入包内/垃圾桶 优先处理核心电子设备（笔记本），利用双臂协同动作减少单臂往返次数。 移动笔记本电脑时需小心屏幕和接口；整理纸张时避免遮挡正在运行的电脑散热口或碰倒水杯。 不确定用户具体要带走哪些纸质文件或杂物，也不确定黑色背包是否已经装入了其他物品（如充电器）。 { "tas...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: needs image verification

## 39. task_005 / Weixin Image_20260629231743_399_27.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: Locate all used cups and dishes on the table.; Pick up each cup/dish one by one.; Transport each item to the kitchen.; Repeat until all items are moved. The task requires moving multiple objects from one location (the table) to another (...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: text-only evidence; still verify image before claims

## 40. task_006 / Weixin Image_20260629231745_400_27.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: Scan the area to identify all individual objects.; Pick up each object one by one.; Place each object into the trash can.; Verify that no objects remain on the floor. The image shows a variety of small objects scattered on the floor. The...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: text-only evidence; still verify image before claims

## 41. task_006 / Weixin Image_20260629231745_400_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: Scan the area to identify all individual objects needing collection.; Pick up one object at a time with either hand, prioritizing smaller/lighter items first.; Transport the object to the trash can and deposit it inside.; Repeat steps 2-...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: needs image verification

## 42. task_007 / Weixin Image_20260629231746_401_27.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: Locate and grasp the green striped shirt.; Transport the green striped shirt to the laundry area.; Locate and grasp the blue hoodie.; Transport the blue hoodie to the laundry area.; Locate and grasp the black t-shirt.; Transport the blac...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: needs image verification

## 43. task_007 / Weixin Image_20260629231746_401_27.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: 1. Navigate to the pile of clothes.; 2. Grasp and lift the green striped shirt.; 3. Transport the green striped shirt to the laundry area and deposit it.; 4. Return to the remaining clothes.; 5. Grasp and lift the blue hoodie.; 6. Transp...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: needs image verification

## 44. task_007 / Weixin Image_20260629231746_401_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_qwen3_vl_30b_a3b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: 移动到椅子旁边; 检查椅子上所有衣物的位置和状态; 逐件拿起衣物并放入夹爪中; 确保每次只携带一件衣物以保持稳定; 移动到洗衣区; 将衣物放置在指定区域 椅子上的衣物分散且部分堆叠，需要逐件收集；夹爪一次只能稳定携带一个物体，因此需要多次往返 优先处理容易取用的衣物，减少移动次数 确保每次只携带一件衣物以避免夹爪负载过重或失衡 洗衣区的具体位置未明确，需根据环境判断路径 {"task_understanding": "将椅子上的衣物收集并运送到洗衣区", "plan":...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: text-only evidence; still verify image before claims

## 45. task_009 / Weixin Image_20260629231751_404_27.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: Scan the area to confirm all debris locations and identify any obstacles.; Navigate to each piece of crumpled paper.; Pick up each piece of crumpled paper.; Navigate to the trash can (visible in the image).; Deposit the crumpled paper in...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: text-only evidence; still verify image before claims

## 46. task_009 / Weixin Image_20260629231751_404_27.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: 1. Scan the area for obstacles and ensure a clear path to all debris.; 2. Collect all visible crumpled paper from the floor.; 3. Locate the trash can (likely near the toilet) and deposit the collected paper.; 4. Re-scan the cleaned area...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: text-only evidence; still verify image before claims

## 47. task_010 / Weixin Image_20260629231750_403_27.jpg / natural_free_plan

- Models failed: ollama_minicpm_v4_5_q8_0
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查附近区域是否有障碍物或不稳定因素，确保移动路径畅通且安全。; 识别并定位需要搬运的主要物品：鸡蛋和纸箱。 尽量减少搬运次数以提高效率，但需根据物品数量和重量合理规划。 确保在搬运过程中物品不会倾倒或损坏，并注意避免碰撞到其他物体。 { "task_understanding": "将桌面上的物品（包括鸡蛋、盒子等）安全搬运到餐桌。", "plan": [ "检查附近区域是否有障碍物或不稳定因素，确保移动路径畅通且安全。", "识别并定位需要搬运的主要物品：鸡蛋和纸箱...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: needs image verification

## 48. task_010 / Weixin Image_20260629231750_403_27.jpg / efficient_safe_free_plan

- Models failed: ollama_qwen3_vl_30b_a3b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: 检查周围环境，确认路径无障碍物; 先拿起金属碗并放置在餐桌上; 拿起塑料蛋托并放置在餐桌上; 逐一将鸡蛋从当前桌面移动至餐桌，并确保不滚动或掉落; 拿起纸箱并将其搬到餐桌; 拿起遥控器并放置在餐桌上; 拿起JBL音箱并放置在餐桌上; 整理桌面上的物品，使其摆放整齐 为保证任务高效完成并减少对易碎品（鸡蛋）的损坏风险，应优先搬运关键物品，并在每次移动中尽量多带物品以降低往返次数。同时需确保机器人在搬运过程中的稳定性，避免因负载不均导致倾倒。 优先搬运易碎品（鸡蛋）和重物（...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: text-only evidence; still verify image before claims

## 49. task_010 / Weixin Image_20260629231750_403_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查当前桌面所有物品的位置与状态，确认哪些是需要移动的，并评估其稳定性与脆弱性。; 优先拾取并搬运最易损或最重的物体（如金属碗、JBL音箱），确保单次携带一个稳定物体。; 逐个小心拾取鸡蛋，每次仅携带1-2枚，避免碰撞；若需搬运多个鸡蛋，可考虑使用透明塑料托盘作为临时容器进行批量转移。; 将遥控器、小包装物品等轻便物件分批或一次性安全放置于餐桌。; 最后清理桌面残留物（如空盒、包装纸），确保原位置整洁。 任务要求安全搬运，而桌面上存在多个易碎或需谨慎处理的物体。为确保无...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: needs image verification

## 50. task_010 / Weixin Image_20260629231750_403_27.jpg / efficient_safe_free_plan_quadruped_single_arm

- Models failed: ollama_qwen3_vl_30b_a3b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查桌面布局，确认所有目标物体的位置和可接近性。; 先使用机械臂拾取并移动鸡蛋，逐个放入塑料蛋托中以防止破损。; 将金属碗、遥控器、JBL音箱等物品依次搬运至餐桌。; 整理纸巾盒和零食包装，确保它们在运输过程中不会掉落或散开。; 检查所有物体是否已安全放置于餐桌上，并确认无遗漏。 任务涉及多个松散物品，其中鸡蛋易碎，必须谨慎处理。通过分批搬运、优先保护脆弱物品并优化路径规划，可在保证安全的前提下提高效率。 优先搬运易碎物品（鸡蛋），并使用蛋托进行保护，减少单次搬运数量以...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: needs image verification

## 51. task_011 / Weixin Image_20260629231748_402_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_minicpm_v4_5_q8_0
- Failure modes: helper_mention_without_use
- Evidence quote: 检查机械臂是否能直接到达桌面中央位置以抓取瓶子，确认没有障碍物遮挡。如果无法直接够到，则考虑调整自身位置或使用其他工具辅助（如先移动桌子边缘物品）。; 若可以直接够到，伸展机械臂并打开夹爪，精准定位在水瓶底部周围，确保夹持稳定。; 关闭夹爪，牢固抓住瓶子后提起，保持平衡移动至目标位置。 任务明确要求取下桌面上的那瓶水，并且瓶子位于桌子中央区域，预计只需一次移动即可完成。 尽量一次性完成任务以提高效率，并避免多次往返。 在抓取和搬运过程中确保身体平衡，防止倾倒或掉落物品。...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: text-only evidence; still verify image before claims

