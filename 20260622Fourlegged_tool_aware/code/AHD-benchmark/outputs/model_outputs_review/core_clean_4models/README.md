# core_clean_4models

Candidate model outputs only. No heuristic or VLM-judge labels are included.

- source: `/home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/AHD-benchmark/outputs/test_o0o1_v2/sequential_o0_o1_core_clean_4models_v2/raw_responses.jsonl`
- outputs: 384
- models: 4

## Models

- [ollama_qwen3_5_35b](./ollama_qwen3_5_35b/README.md): 96 outputs
- [ollama_qwen3_vl_30b_a3b_instruct_q4_K_M](./ollama_qwen3_vl_30b_a3b_instruct_q4_K_M/README.md): 96 outputs
- [ollama_qwen3_vl_32b_instruct_q4_K_M](./ollama_qwen3_vl_32b_instruct_q4_K_M/README.md): 96 outputs
- [ollama_qwen3_vl_8b](./ollama_qwen3_vl_8b/README.md): 96 outputs

## Task Counts

- `no_tool_control`: 48
- `positive_aggregate`: 48
- `positive_reach`: 48
- `same_o1_different_o0`: 144
- `wrong_helper_negative`: 96
