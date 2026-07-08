cd /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/AHD-benchmark

python scripts/05_ollama_enrich_scene_specs.py \
    --model qwen3-vl:30b-a3b-instruct-q4_K_M \
    --stratified_per_type 10

python scripts/06_check_llm_enrichment.py \
    specs/enrichment/llm_enriched_qwen3-vl_30b-a3b-instruct-q4_K_M_stratified10_preview.jsonl
