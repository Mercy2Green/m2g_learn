cd /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/AHD-benchmark

python scripts/05_ollama_enrich_scene_specs.py --model qwen3-vl:32b-instruct-q4_K_M --max_specs 20
python scripts/06_check_llm_enrichment.py specs/enrichment/llm_enriched_qwen3-vl_32b-instruct-q4_K_M_preview.jsonl

python scripts/05_ollama_enrich_scene_specs.py --model qwen3-vl:30b-a3b-instruct-q4_K_M --max_specs 20
python scripts/06_check_llm_enrichment.py specs/enrichment/llm_enriched_qwen3-vl_30b-a3b-instruct-q4_K_M_preview.jsonl

python scripts/05_ollama_enrich_scene_specs.py --model qwen3.5:35b --max_specs 20
python scripts/06_check_llm_enrichment.py specs/enrichment/llm_enriched_qwen3.5_35b_preview.jsonl

python scripts/05_ollama_enrich_scene_specs.py --model gemma3:27b-it_q8_0 --max_specs 20
python scripts/06_check_llm_enrichment.py specs/enrichment/llm_enriched_gemma3_27b-it_q8_0_preview.jsonl