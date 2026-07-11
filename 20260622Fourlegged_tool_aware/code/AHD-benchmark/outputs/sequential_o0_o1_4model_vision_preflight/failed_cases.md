# Sequential Failed and Review Cases

Heuristic labels are a baseline first pass and require human review before research claims.

- positive_aggregate_001 / ollama_qwen3_vl_8b / multi_image__natural_free_plan: fail - No valid aggregate helper-target action chain; direct/one-by-one handling is insufficient. Plan: 检查厨房区域确认饮料数量和状态; 规划从厨房到卧室的最短路径; 将饮料运送到卧室并交付
- positive_aggregate_001 / ollama_qwen3_vl_32b_instruct_q4_K_M / multi_image__natural_free_plan: fail - No valid aggregate helper-target action chain; direct/one-by-one handling is insufficient. Plan: 确认所有饮料瓶的位置和数量，并检查是否适合搬运（如无破损、标签清晰）; 规划从厨房到卧室的安全路径，避开障碍物并确保稳定移动; 分批或一次性将饮料运送到卧室，优先保证效率与安全
- positive_aggregate_001 / ollama_qwen3_vl_30b_a3b_instruct_q4_K_M / multi_image__natural_free_plan: fail - No valid aggregate helper-target action chain; direct/one-by-one handling is insufficient. Plan: 确认所有七瓶饮料都在厨房的台面上。; 拿起最左边的第一瓶饮料。; 离开厨房，前往卧室。; 在卧室内找到正在打牌的同学，并将第一瓶饮料递给他们。; 返回厨房，重复上述步骤，直到所有七瓶饮料都送达。
- positive_aggregate_001 / ollama_qwen3_5_35b / multi_image__natural_free_plan: fail - No valid aggregate helper-target action chain; direct/one-by-one handling is insufficient. Plan: 确认所有瓶子为可饮用的液体且无安全隐患; 检查从厨房到卧室的路径是否畅通无阻; 分两次搬运：第一次运送四瓶，第二次运送三瓶至卧室桌面
