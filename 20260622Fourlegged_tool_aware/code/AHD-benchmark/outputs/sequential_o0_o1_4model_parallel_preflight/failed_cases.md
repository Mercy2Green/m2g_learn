# Sequential Failed and Review Cases

Heuristic labels are a baseline first pass and require human review before research claims.

- positive_aggregate_001 / ollama_qwen3_vl_30b_a3b_instruct_q4_K_M / multi_image__natural_free_plan: fail - No valid aggregate helper-target action chain; direct/one-by-one handling is insufficient. Plan: 检查当前环境，确认所有饮料瓶都在厨房的台面上。; 使用机械臂抓取最左侧的黄色饮料瓶。; 离开厨房，前往卧室方向。; 进入卧室，将黄色饮料瓶放在桌上。; 返回厨房，重复上述步骤，依次运送剩余六瓶饮料。; 在运送过程中，注意避开障碍物并保持平稳移动。
- positive_aggregate_001 / ollama_qwen3_vl_32b_instruct_q4_K_M / multi_image__natural_free_plan: fail - No valid aggregate helper-target action chain; direct/one-by-one handling is insufficient. Plan: 确认所有饮料瓶的位置和数量，并检查是否适合搬运（如无破损、标签清晰）; 规划从厨房到卧室的安全路径，避开障碍物并确保稳定移动; 分批或一次性将饮料运送到卧室，优先保证效率与安全
- positive_aggregate_001 / ollama_qwen3_vl_8b / multi_image__natural_free_plan: fail - No valid aggregate helper-target action chain; direct/one-by-one handling is insufficient. Plan: 检查厨房台面饮料位置及数量; 规划从厨房到卧室的最短路径; 运送饮料至卧室并交付
