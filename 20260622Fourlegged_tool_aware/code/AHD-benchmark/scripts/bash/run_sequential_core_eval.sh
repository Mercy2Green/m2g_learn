#!/usr/bin/env bash
set -euo pipefail

AHD_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
BENCHMARK_DIR="$(cd "${AHD_DIR}/../test_current_vlm/tool_counterexample_benchmark" && pwd)"
OUTPUT_DIR="${OUTPUT_DIR:-outputs/sequential_o0_o1_core_clean_4models}"
RUN_JUDGE="${RUN_JUDGE:-1}"
PARALLEL_MODELS="${PARALLEL_MODELS:-4}"

MODEL_IDS=(
  ollama_qwen3_vl_8b
  ollama_qwen3_vl_32b_instruct_q4_K_M
  ollama_qwen3_vl_30b_a3b_instruct_q4_K_M
  ollama_qwen3_5_35b
)

PROMPT_IDS=(
  multi_image__natural_free_plan two_turn__natural_free_plan
  multi_image__efficient_safe_free_plan two_turn__efficient_safe_free_plan
  multi_image__natural_free_plan_humanoid_dual_arm two_turn__natural_free_plan_humanoid_dual_arm
  multi_image__efficient_safe_free_plan_humanoid_dual_arm two_turn__efficient_safe_free_plan_humanoid_dual_arm
  multi_image__natural_free_plan_quadruped_single_arm two_turn__natural_free_plan_quadruped_single_arm
  multi_image__efficient_safe_free_plan_quadruped_single_arm two_turn__efficient_safe_free_plan_quadruped_single_arm
)

cd "${BENCHMARK_DIR}"

python sequential_o0_o1/scripts/build_sequential_prompt_sets.py \
  --old_prompts config/prompt_sets.yaml \
  --output sequential_o0_o1/prompts/sequential_prompt_sets_full.yaml \
  --overwrite

python sequential_o0_o1/scripts/build_sequential_core_eval_dataset.py \
  --curated_index ../../AHD-benchmark/data/curated_pools/ahd_cosmos3_raw240_qwen32/curated_index.jsonl \
  --output sequential_o0_o1/data/sequential_core_eval_samples.jsonl \
  --overwrite

python sequential_o0_o1/scripts/run_sequential_eval.py \
  --samples sequential_o0_o1/data/sequential_core_eval_samples.jsonl \
  --models config/models.yaml \
  --model_overrides sequential_o0_o1/config/sequential_model_overrides.yaml \
  --sequential_prompts sequential_o0_o1/prompts/sequential_prompt_sets_full.yaml \
  --output_dir "${OUTPUT_DIR}" \
  --model_ids "${MODEL_IDS[@]}" \
  --prompt_ids "${PROMPT_IDS[@]}" \
  --parallel_models "${PARALLEL_MODELS}" \
  --overwrite

if [[ "${RUN_JUDGE}" == "1" ]]; then
  python sequential_o0_o1/scripts/judge_sequential_responses.py \
    --input_dir "${OUTPUT_DIR}" \
    --judge_model qwen3-vl:32b-instruct-q4_K_M \
    --output_dir "${OUTPUT_DIR}/response_judge_qwen32" \
    --overwrite
fi

echo "Sequential core evaluation complete: ${BENCHMARK_DIR}/${OUTPUT_DIR}"
