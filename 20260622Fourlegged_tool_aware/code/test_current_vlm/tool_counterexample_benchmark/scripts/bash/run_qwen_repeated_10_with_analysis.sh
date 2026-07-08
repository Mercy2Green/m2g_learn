#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../.."

RUN_TAG="${RUN_TAG:-qwen_repeated_10}"
OUTPUT_ROOT="${OUTPUT_ROOT:-outputs/${RUN_TAG}}"
ANALYSIS_DIR="${ANALYSIS_DIR:-analysis_review/${RUN_TAG}}"
VLM_JUDGE_DIR="${VLM_JUDGE_DIR:-analysis_review/${RUN_TAG}_vlm_judge_qwen32}"
JUDGE_MODEL="${JUDGE_MODEL:-qwen3-vl:32b-instruct-q4_K_M}"
OLLAMA_URL="${OLLAMA_URL:-http://localhost:11434}"
PROGRESS_EVERY="${PROGRESS_EVERY:-1}"
REPEATS="${REPEATS:-10}"

MODEL_IDS=(
  ollama_qwen3_vl_4b
  ollama_qwen3_vl_8b
  ollama_qwen3_vl_30b_a3b_instruct_q4_K_M
  ollama_qwen3_vl_32b_instruct_q4_K_M
  ollama_qwen3_5_35b
)

PROMPT_IDS=(
  natural_free_plan
  efficient_safe_free_plan
  tool_prior_free_plan
  strong_decomposition_free_plan
  search_explicit_strong_decomposition_free_plan
  structured_tool_probe
  natural_free_plan_humanoid_dual_arm
  efficient_safe_free_plan_humanoid_dual_arm
  tool_prior_free_plan_humanoid_dual_arm
  strong_decomposition_free_plan_humanoid_dual_arm
  search_explicit_strong_decomposition_free_plan_humanoid_dual_arm
  structured_tool_action_chain_probe_humanoid_dual_arm
  natural_free_plan_quadruped_single_arm
  efficient_safe_free_plan_quadruped_single_arm
  tool_prior_free_plan_quadruped_single_arm
  strong_decomposition_free_plan_quadruped_single_arm
  search_explicit_strong_decomposition_free_plan_quadruped_single_arm
  structured_tool_action_chain_probe_quadruped_single_arm
)

TASK_ARGS=("$@")

# shellcheck source=scripts/bash/_round05_pipeline_common.sh
source scripts/bash/_round05_pipeline_common.sh

validate_repeat_count() {
  if ! [[ "${REPEATS}" =~ ^[1-9][0-9]*$ ]]; then
    echo "[ERROR] REPEATS must be a positive integer, got: ${REPEATS}" >&2
    exit 1
  fi
}

check_ollama_model_names() {
  local missing=()
  local model_names=(
    qwen3-vl:4b
    qwen3-vl:8b
    qwen3-vl:30b-a3b-instruct-q4_K_M
    qwen3-vl:32b-instruct-q4_K_M
    qwen3.5:35b
  )

  if ! command -v ollama >/dev/null 2>&1; then
    echo "[WARN] ollama command not found; skipping installed-model check." >&2
    return
  fi

  local installed
  installed="$(ollama list | awk 'NR > 1 {print $1}')"
  for model_name in "${model_names[@]}"; do
    if ! grep -Fxq "${model_name}" <<< "${installed}"; then
      missing+=("${model_name}")
    fi
  done

  if [[ ${#missing[@]} -gt 0 ]]; then
    echo "[ERROR] Missing Ollama models: ${missing[*]}" >&2
    echo "[INFO] Current ollama list names:" >&2
    echo "${installed}" >&2
    exit 1
  fi
}

run_repeated_inference() {
  local run_models_config="$1"
  RUN_OUTPUT_DIRS=()

  echo "[INFO] Running repeated Qwen inference..."
  echo "[INFO] Run tag: ${RUN_TAG}"
  echo "[INFO] Output root: ${OUTPUT_ROOT}"
  echo "[INFO] Repeats: ${REPEATS}"
  echo "[INFO] Models: ${MODEL_IDS[*]}"
  echo "[INFO] Prompt count: ${#PROMPT_IDS[@]}"
  echo "[INFO] Extra task/run args: ${TASK_ARGS[*]:-<none>}"

  for repeat in $(seq 1 "${REPEATS}"); do
    repeat_label="$(printf "repeat_%02d" "${repeat}")"
    echo
    echo "[INFO] Starting ${repeat_label}/${REPEATS}"

    for model_id in "${MODEL_IDS[@]}"; do
      output_dir="${OUTPUT_ROOT}/${repeat_label}_${model_id}"
      RUN_OUTPUT_DIRS+=("${output_dir}")

      echo "[INFO] Running ${repeat_label} on ${model_id}"
      echo "[INFO] Output: ${output_dir}"
      python -m src.run_batch \
        --models "${run_models_config}" \
        --prompts config/prompt_sets.yaml \
        --tasks config/tasks.yaml \
        --output_dir "${output_dir}" \
        --model_ids "${model_id}" \
        --prompt_ids "${PROMPT_IDS[@]}" \
        "${TASK_ARGS[@]}" \
        --overwrite
    done
  done
}

run_repeated_qwen_pipeline() {
  validate_repeat_count

  local config_dir="outputs/${RUN_TAG}_generated_configs"
  local run_models_config="${config_dir}/models_qwen_repeated_enabled.yaml"

  if [[ "${SKIP_CONDA_ACTIVATE:-0}" == "1" ]]; then
    echo "[INFO] SKIP_CONDA_ACTIVATE=1, using current shell environment."
  else
    activate_codex_ollama
  fi

  echo "[INFO] Python compile check..."
  python -m compileall scripts/analysis src

  echo "[INFO] YAML prompt ID check..."
  check_prompt_ids

  echo "[INFO] Checking installed Ollama model names..."
  check_ollama_model_names

  echo "[INFO] Preparing model config..."
  write_enabled_models_config "${run_models_config}" "${MODEL_IDS[@]}"

  run_repeated_inference "${run_models_config}"

  echo "[INFO] Building merged result index..."
  python scripts/analysis/build_result_index.py \
    --output_dirs "${RUN_OUTPUT_DIRS[@]}" \
    --output_dir "${ANALYSIS_DIR}"

  echo "[INFO] Running rule-based rereview..."
  python scripts/analysis/rereview_results.py \
    --input "${ANALYSIS_DIR}/all_rows_merged.jsonl" \
    --output_dir "${ANALYSIS_DIR}"

  echo "[INFO] Summarizing rule-based rereview..."
  python scripts/analysis/summarize_rereview.py \
    --input "${ANALYSIS_DIR}/case_rereview.jsonl" \
    --output_dir "${ANALYSIS_DIR}"

  echo "[INFO] Running image-aware VLM judge rereview..."
  python scripts/analysis/vlm_judge_rereview.py \
    --input "${ANALYSIS_DIR}/all_rows_merged.jsonl" \
    --output_dir "${VLM_JUDGE_DIR}" \
    --judge_model "${JUDGE_MODEL}" \
    --ollama_url "${OLLAMA_URL}" \
    --rule_case_rereview "${ANALYSIS_DIR}/case_rereview.csv" \
    --overwrite \
    --progress_every "${PROGRESS_EVERY}"

  echo "[INFO] Summarizing VLM judge rereview..."
  python scripts/analysis/summarize_vlm_judge.py \
    --input_dir "${VLM_JUDGE_DIR}" \
    --rule_case_rereview "${ANALYSIS_DIR}/case_rereview.csv"

  OUTPUT_DIR="${OUTPUT_ROOT}"
  check_row_counts

  echo "[INFO] Done."
  echo "  OUTPUT_ROOT=${OUTPUT_ROOT}"
  echo "  ANALYSIS_DIR=${ANALYSIS_DIR}"
  echo "  VLM_JUDGE_DIR=${VLM_JUDGE_DIR}"
  echo "  Rule handoff: ${ANALYSIS_DIR}/README_FOR_CHATGPT.md"
  echo "  Rule aggregate: ${ANALYSIS_DIR}/aggregate_findings.md"
  echo "  VLM handoff: ${VLM_JUDGE_DIR}/README_FOR_CHATGPT.md"
  echo "  VLM aggregate: ${VLM_JUDGE_DIR}/vlm_aggregate_findings.md"
}

run_repeated_qwen_pipeline
