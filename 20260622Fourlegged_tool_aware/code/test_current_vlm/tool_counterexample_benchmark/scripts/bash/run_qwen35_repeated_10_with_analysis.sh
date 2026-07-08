#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../.."

RUN_TAG="${RUN_TAG:-qwen35_repeated_10}"
OUTPUT_ROOT="${OUTPUT_ROOT:-outputs/${RUN_TAG}}"
ANALYSIS_DIR="${ANALYSIS_DIR:-analysis_review/${RUN_TAG}}"
VLM_JUDGE_DIR="${VLM_JUDGE_DIR:-analysis_review/${RUN_TAG}_vlm_judge_qwen32}"
JUDGE_MODEL="${JUDGE_MODEL:-qwen3-vl:32b-instruct-q4_K_M}"
OLLAMA_URL="${OLLAMA_URL:-http://localhost:11434}"
PROGRESS_EVERY="${PROGRESS_EVERY:-1}"
REPEATS="${REPEATS:-10}"
OLLAMA_KEEP_ALIVE="${OLLAMA_KEEP_ALIVE:-0}"
OLLAMA_STOP_BETWEEN_REPEATS="${OLLAMA_STOP_BETWEEN_REPEATS:-1}"

MODEL_ID="ollama_qwen3_5_35b"
OLLAMA_MODEL_NAME="qwen3.5:35b"

MODEL_IDS=(
  "${MODEL_ID}"
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

check_qwen35_model_name() {
  if ! command -v ollama >/dev/null 2>&1; then
    echo "[WARN] ollama command not found; skipping installed-model check." >&2
    return
  fi

  local installed
  installed="$(ollama list | awk 'NR > 1 {print $1}')"
  if ! grep -Fxq "${OLLAMA_MODEL_NAME}" <<< "${installed}"; then
    echo "[ERROR] Missing Ollama model: ${OLLAMA_MODEL_NAME}" >&2
    echo "[INFO] Current ollama list names:" >&2
    echo "${installed}" >&2
    exit 1
  fi
}

write_isolated_qwen35_models_config() {
  local output_path="$1"

  mkdir -p "$(dirname "${output_path}")"
  python - config/models.yaml "${output_path}" "${MODEL_ID}" "${OLLAMA_KEEP_ALIVE}" <<'PY'
from __future__ import annotations

import sys
from pathlib import Path

import yaml

src = Path(sys.argv[1])
dst = Path(sys.argv[2])
enabled_id = sys.argv[3]
keep_alive = sys.argv[4]

data = yaml.safe_load(src.read_text(encoding="utf-8"))
for model in data.get("models", []):
    model["enabled"] = model.get("model_id") == enabled_id
    if model.get("model_id") == enabled_id:
        model["keep_alive"] = keep_alive

dst.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"[INFO] Wrote isolated qwen3.5 models config: {dst}")
print(f"[INFO] {enabled_id} keep_alive={keep_alive!r}")
PY
}

stop_qwen35_if_requested() {
  if [[ "${OLLAMA_STOP_BETWEEN_REPEATS}" != "1" ]]; then
    return
  fi
  if ! command -v ollama >/dev/null 2>&1; then
    return
  fi

  echo "[INFO] Stopping ${OLLAMA_MODEL_NAME} to avoid residency between repeats..."
  if ! ollama stop "${OLLAMA_MODEL_NAME}" >/dev/null 2>&1; then
    echo "[WARN] ollama stop ${OLLAMA_MODEL_NAME} failed or model was not loaded; continuing." >&2
  fi
}

run_repeated_inference() {
  local run_models_config="$1"
  RUN_OUTPUT_DIRS=()

  echo "[INFO] Running repeated qwen3.5 inference..."
  echo "[INFO] Run tag: ${RUN_TAG}"
  echo "[INFO] Output root: ${OUTPUT_ROOT}"
  echo "[INFO] Repeats: ${REPEATS}"
  echo "[INFO] Model: ${MODEL_ID} (${OLLAMA_MODEL_NAME})"
  echo "[INFO] Prompt count: ${#PROMPT_IDS[@]}"
  echo "[INFO] Ollama keep_alive override: ${OLLAMA_KEEP_ALIVE}"
  echo "[INFO] Stop between repeats: ${OLLAMA_STOP_BETWEEN_REPEATS}"
  echo "[INFO] Extra task/run args: ${TASK_ARGS[*]:-<none>}"

  for repeat in $(seq 1 "${REPEATS}"); do
    repeat_label="$(printf "repeat_%02d" "${repeat}")"
    output_dir="${OUTPUT_ROOT}/${repeat_label}_${MODEL_ID}"
    RUN_OUTPUT_DIRS+=("${output_dir}")

    echo
    echo "[INFO] Running ${repeat_label}/${REPEATS} on ${MODEL_ID}"
    echo "[INFO] Output: ${output_dir}"
    stop_qwen35_if_requested
    python -m src.run_batch \
      --models "${run_models_config}" \
      --prompts config/prompt_sets.yaml \
      --tasks config/tasks.yaml \
      --output_dir "${output_dir}" \
      --model_ids "${MODEL_ID}" \
      --prompt_ids "${PROMPT_IDS[@]}" \
      "${TASK_ARGS[@]}" \
      --overwrite

    stop_qwen35_if_requested
  done
}

run_repeated_qwen35_pipeline() {
  validate_repeat_count

  local config_dir="outputs/${RUN_TAG}_generated_configs"
  local run_models_config="${config_dir}/models_qwen35_repeated_enabled.yaml"

  if [[ "${SKIP_CONDA_ACTIVATE:-0}" == "1" ]]; then
    echo "[INFO] SKIP_CONDA_ACTIVATE=1, using current shell environment."
  else
    activate_codex_ollama
  fi

  echo "[INFO] Python compile check..."
  python -m compileall scripts/analysis src

  echo "[INFO] YAML prompt ID check..."
  check_prompt_ids

  echo "[INFO] Checking installed qwen3.5 Ollama model name..."
  check_qwen35_model_name

  echo "[INFO] Preparing isolated qwen3.5 model config..."
  write_isolated_qwen35_models_config "${run_models_config}"

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

run_repeated_qwen35_pipeline
