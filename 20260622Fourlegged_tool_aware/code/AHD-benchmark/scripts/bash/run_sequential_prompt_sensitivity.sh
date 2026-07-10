#!/usr/bin/env bash
set -euo pipefail

AHD_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
BENCHMARK_DIR="$(cd "${AHD_DIR}/../test_current_vlm/tool_counterexample_benchmark" && pwd)"
OUTPUT_DIR="${OUTPUT_DIR:-outputs/sequential_o0_o1_prompt_sensitivity_3models}"
INCLUDE_QWEN8="${INCLUDE_QWEN8:-0}"
PARALLEL_MODELS="${PARALLEL_MODELS:-3}"

MODEL_IDS=(
  ollama_qwen3_vl_32b_instruct_q4_K_M
  ollama_qwen3_vl_30b_a3b_instruct_q4_K_M
  ollama_qwen3_5_35b
)
if [[ "${INCLUDE_QWEN8}" == "1" ]]; then
  MODEL_IDS=(ollama_qwen3_vl_8b "${MODEL_IDS[@]}")
fi

SAMPLE_IDS=(
  positive_aggregate_001
  wrong_helper_negative_aggregate_001
  same_o1_aggregate_001
  same_o1_direct_001
  same_o1_reach_001
)

cd "${BENCHMARK_DIR}"
python sequential_o0_o1/scripts/run_sequential_eval.py \
  --samples sequential_o0_o1/data/sequential_core_eval_samples.jsonl \
  --models config/models.yaml \
  --model_overrides sequential_o0_o1/config/sequential_model_overrides.yaml \
  --sequential_prompts sequential_o0_o1/prompts/sequential_prompt_sets_full.yaml \
  --output_dir "${OUTPUT_DIR}" \
  --sample_ids "${SAMPLE_IDS[@]}" \
  --model_ids "${MODEL_IDS[@]}" \
  --parallel_models "${PARALLEL_MODELS}" \
  --overwrite

echo "Prompt sensitivity evaluation complete: ${BENCHMARK_DIR}/${OUTPUT_DIR}"
