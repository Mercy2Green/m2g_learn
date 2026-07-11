# Strict VLM Judge V2 vs Heuristic V2

| group by | value | comparable | both pass | both fail | VLM pass / v2 fail | v2 pass / VLM fail | VLM pass / v2 review | v2 pass / VLM review | exact agreement | rate |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| overall | all | 524 | 105 | 118 | 4 | 45 | 137 | 27 | 241 | 0.460 |
| model_id | ollama_qwen3_5_35b | 165 | 27 | 40 | 2 | 12 | 39 | 8 | 77 | 0.467 |
| model_id | ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 180 | 29 | 41 | 0 | 21 | 48 | 10 | 71 | 0.394 |
| model_id | ollama_qwen3_vl_32b_instruct_q4_K_M | 179 | 49 | 37 | 2 | 12 | 50 | 9 | 93 | 0.520 |
| protocol | single_turn_multi_image | 260 | 21 | 78 | 0 | 8 | 72 | 21 | 110 | 0.423 |
| protocol | two_turn_sequential | 264 | 84 | 40 | 4 | 37 | 65 | 6 | 131 | 0.496 |
| sample_type | positive_aggregate | 106 | 11 | 59 | 0 | 19 | 0 | 16 | 70 | 0.660 |
| sample_type | same_o1_different_o0 | 313 | 62 | 58 | 0 | 21 | 123 | 11 | 138 | 0.441 |
| sample_type | wrong_helper_negative | 105 | 32 | 1 | 4 | 5 | 14 | 0 | 33 | 0.314 |
