#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BENCHMARK_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"

RUN_PREFIX="${RUN_PREFIX:-ollama_multi_$(date +%Y%m%d_%H%M%S)}"
CONFIG_DIR="${BENCHMARK_DIR}/outputs/${RUN_PREFIX}_generated_configs"
BASE_MODELS_CONFIG="${BENCHMARK_DIR}/config/models.yaml"
RUN_MODELS_CONFIG="${CONFIG_DIR}/models_ollama_large_enabled.yaml"

OLLAMA_LARGE_MODEL_IDS=(
  "ollama_qwen3_vl_32b_instruct_q4_K_M"
  "ollama_qwen3_vl_30b_a3b_instruct_q4_K_M"
  "ollama_qwen3_5_35b"
  "ollama_minicpm_v4_5_q8_0"
  "ollama_gemma3_27b_it_q8_0"
  "ollama_llama3_2_vision_11b_instruct_q8_0"
)

activate_codex_ollama() {
  if command -v conda >/dev/null 2>&1; then
    eval "$(conda shell.bash hook)"
    conda activate codex_ollama
    return
  fi

  local conda_sh=""
  for candidate in "${HOME}/miniconda3/etc/profile.d/conda.sh" "${HOME}/anaconda3/etc/profile.d/conda.sh"; do
    if [[ -f "${candidate}" ]]; then
      conda_sh="${candidate}"
      break
    fi
  done

  if [[ -z "${conda_sh}" ]]; then
    echo "[ERROR] conda was not found. Please install conda or activate codex_ollama manually." >&2
    exit 1
  fi

  # shellcheck source=/dev/null
  source "${conda_sh}"
  conda activate codex_ollama
}

prepare_models_config() {
  mkdir -p "${CONFIG_DIR}"
  python - "${BASE_MODELS_CONFIG}" "${RUN_MODELS_CONFIG}" "${OLLAMA_LARGE_MODEL_IDS[@]}" <<'PY'
from __future__ import annotations

import sys
from pathlib import Path

import yaml

src = Path(sys.argv[1])
dst = Path(sys.argv[2])
enabled_model_ids = set(sys.argv[3:])

data = yaml.safe_load(src.read_text(encoding="utf-8"))
for model in data.get("models", []):
    model["enabled"] = model.get("model_id") in enabled_model_ids

dst.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"[INFO] Wrote temporary models config: {dst}")
PY
}

run_prompt_category() {
  local category="$1"
  shift
  local prompt_ids=("$@")

  echo "[INFO] Benchmark dir: ${BENCHMARK_DIR}"
  echo "[INFO] Run prefix: ${RUN_PREFIX}"
  echo "[INFO] Category: ${category}"
  echo "[INFO] Prompts: ${prompt_ids[*]}"
  echo "[INFO] Extra run_batch args: ${EXTRA_RUN_ARGS[*]:-}"

  for model_id in "${OLLAMA_LARGE_MODEL_IDS[@]}"; do
    local output_dir="outputs/${RUN_PREFIX}_${category}_${model_id}"
    echo
    echo "[INFO] Running ${category} on ${model_id}"
    echo "[INFO] Output: ${output_dir}"
    (
      cd "${BENCHMARK_DIR}"
      python -m src.run_batch \
        --models "${RUN_MODELS_CONFIG}" \
        --prompts config/prompt_sets.yaml \
        --tasks config/tasks.yaml \
        --output_dir "${output_dir}" \
        --model_ids "${model_id}" \
        --prompt_ids "${prompt_ids[@]}" \
        --overwrite \
        "${EXTRA_RUN_ARGS[@]}"
    )
  done
}

run_prompt_category_for_models() {
  local category="$1"
  local models_csv="$2"
  shift 2
  local prompt_ids=("$@")
  IFS="," read -r -a selected_models <<< "${models_csv}"

  echo "[INFO] Benchmark dir: ${BENCHMARK_DIR}"
  echo "[INFO] Run prefix: ${RUN_PREFIX}"
  echo "[INFO] Category: ${category}"
  echo "[INFO] Models: ${selected_models[*]}"
  echo "[INFO] Prompts: ${prompt_ids[*]}"
  echo "[INFO] Extra run_batch args: ${EXTRA_RUN_ARGS[*]:-}"

  for model_id in "${selected_models[@]}"; do
    local output_dir="outputs/${RUN_PREFIX}_${category}_${model_id}"
    echo
    echo "[INFO] Running ${category} on ${model_id}"
    echo "[INFO] Output: ${output_dir}"
    (
      cd "${BENCHMARK_DIR}"
      python -m src.run_batch \
        --models "${RUN_MODELS_CONFIG}" \
        --prompts config/prompt_sets.yaml \
        --tasks config/tasks.yaml \
        --output_dir "${output_dir}" \
        --model_ids "${model_id}" \
        --prompt_ids "${prompt_ids[@]}" \
        --overwrite \
        "${EXTRA_RUN_ARGS[@]}"
    )
  done
}

bootstrap_batch() {
  EXTRA_RUN_ARGS=("$@")
  activate_codex_ollama
  prepare_models_config
}
