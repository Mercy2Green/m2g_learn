# Strict VLM Judge V3 vs Heuristic V2

| group by | value | comparable | both pass | both fail | VLM pass / v2 fail | v2 pass / VLM fail | VLM pass / v2 review | v2 pass / VLM review | exact agreement | rate |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| overall | all | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0.000 |
| model_id | ollama_qwen3_vl_32b_instruct_q4_K_M | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0.000 |
| model_id | ollama_qwen3_vl_8b | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000 |
| protocol | single_turn_multi_image | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000 |
| protocol | two_turn_sequential | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0.000 |
| sample_type | positive_aggregate | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0.000 |
