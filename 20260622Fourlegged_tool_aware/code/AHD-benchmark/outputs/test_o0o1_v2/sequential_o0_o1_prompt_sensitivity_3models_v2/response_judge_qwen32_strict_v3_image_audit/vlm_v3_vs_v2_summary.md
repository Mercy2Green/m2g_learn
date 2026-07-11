# Strict VLM Judge V3 vs Heuristic V2

| group by | value | comparable | both pass | both fail | VLM pass / v2 fail | v2 pass / VLM fail | VLM pass / v2 review | v2 pass / VLM review | exact agreement | rate |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| overall | all | 523 | 119 | 99 | 9 | 7 | 102 | 51 | 224 | 0.428 |
| model_id | ollama_qwen3_5_35b | 164 | 34 | 29 | 4 | 0 | 41 | 13 | 65 | 0.396 |
| model_id | ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 179 | 38 | 36 | 1 | 4 | 30 | 18 | 74 | 0.413 |
| model_id | ollama_qwen3_vl_32b_instruct_q4_K_M | 180 | 47 | 34 | 4 | 3 | 31 | 20 | 85 | 0.472 |
| protocol | single_turn_multi_image | 259 | 29 | 76 | 0 | 2 | 69 | 19 | 111 | 0.429 |
| protocol | two_turn_sequential | 264 | 90 | 23 | 9 | 5 | 33 | 32 | 113 | 0.428 |
| sample_type | positive_aggregate | 105 | 21 | 50 | 1 | 2 | 0 | 23 | 71 | 0.676 |
| sample_type | same_o1_different_o0 | 312 | 61 | 49 | 2 | 5 | 50 | 28 | 116 | 0.372 |
| sample_type | wrong_helper_negative | 106 | 37 | 0 | 6 | 0 | 52 | 0 | 37 | 0.349 |
