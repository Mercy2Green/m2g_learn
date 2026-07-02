#!/usr/bin/env bash
set -euo pipefail

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

write_enabled_models_config() {
  local output_path="$1"
  shift
  local model_ids=("$@")

  mkdir -p "$(dirname "${output_path}")"
  python - config/models.yaml "${output_path}" "${model_ids[@]}" <<'PY'
from __future__ import annotations

import sys
from pathlib import Path

import yaml

src = Path(sys.argv[1])
dst = Path(sys.argv[2])
enabled_ids = set(sys.argv[3:])

data = yaml.safe_load(src.read_text(encoding="utf-8"))
for model in data.get("models", []):
    model["enabled"] = model.get("model_id") in enabled_ids

dst.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
print(f"[INFO] Wrote enabled models config: {dst}")
PY
}

check_prompt_ids() {
  python - "${PROMPT_IDS[@]}" <<'PY'
from __future__ import annotations

import sys
from pathlib import Path

import yaml

required = sys.argv[1:]
data = yaml.safe_load(Path("config/prompt_sets.yaml").read_text(encoding="utf-8"))
ids = [item["prompt_id"] for item in data["prompts"]]
missing = [item for item in required if item not in ids]
duplicates = sorted({item for item in ids if ids.count(item) > 1})
print(f"[INFO] prompt count: {len(ids)}")
print(f"[INFO] required prompt count: {len(required)}")
if missing:
    raise SystemExit(f"Missing prompt IDs: {missing}")
if duplicates:
    raise SystemExit(f"Duplicate prompt IDs: {duplicates}")
print("[INFO] Prompt ID check passed.")
PY
}

line_count() {
  local path="$1"
  if [[ ! -f "${path}" ]]; then
    echo "0"
    return
  fi
  wc -l < "${path}"
}

check_row_counts() {
  local all_rows_jsonl="${ANALYSIS_DIR}/all_rows_merged.jsonl"
  local rereview_jsonl="${ANALYSIS_DIR}/case_rereview.jsonl"
  local rereview_csv="${ANALYSIS_DIR}/case_rereview.csv"
  local vlm_jsonl="${VLM_JUDGE_DIR}/vlm_case_rereview.jsonl"
  local vlm_csv="${VLM_JUDGE_DIR}/vlm_case_rereview.csv"

  local all_rows rereview_rows rereview_csv_rows vlm_rows vlm_csv_rows
  all_rows="$(line_count "${all_rows_jsonl}")"
  rereview_rows="$(line_count "${rereview_jsonl}")"
  rereview_csv_rows="$(line_count "${rereview_csv}")"
  vlm_rows="$(line_count "${vlm_jsonl}")"
  vlm_csv_rows="$(line_count "${vlm_csv}")"

  echo "[INFO] Row count check:"
  echo "  ${all_rows_jsonl}: ${all_rows}"
  echo "  ${rereview_jsonl}: ${rereview_rows}"
  echo "  ${rereview_csv}: ${rereview_csv_rows} (includes header)"
  echo "  ${vlm_jsonl}: ${vlm_rows}"
  echo "  ${vlm_csv}: ${vlm_csv_rows} (includes header)"

  if [[ "${all_rows}" != "${rereview_rows}" ]]; then
    echo "[ERROR] case_rereview.jsonl rows do not match all_rows_merged.jsonl." >&2
    exit 1
  fi
  if [[ "${all_rows}" != "${vlm_rows}" ]]; then
    echo "[ERROR] vlm_case_rereview.jsonl rows do not match all_rows_merged.jsonl." >&2
    exit 1
  fi
  if [[ "${rereview_csv_rows}" -ne $((rereview_rows + 1)) ]]; then
    echo "[ERROR] case_rereview.csv line count is not JSONL rows + header." >&2
    exit 1
  fi
  if [[ "${vlm_csv_rows}" -ne $((vlm_rows + 1)) ]]; then
    echo "[ERROR] vlm_case_rereview.csv line count is not JSONL rows + header." >&2
    exit 1
  fi
}

run_round05_pipeline() {
  : "${RUN_TAG:?RUN_TAG must be set}"
  : "${OUTPUT_DIR:?OUTPUT_DIR must be set}"
  : "${ANALYSIS_DIR:?ANALYSIS_DIR must be set}"
  : "${VLM_JUDGE_DIR:?VLM_JUDGE_DIR must be set}"
  : "${JUDGE_MODEL:?JUDGE_MODEL must be set}"
  : "${OLLAMA_URL:?OLLAMA_URL must be set}"

  local config_dir="outputs/${RUN_TAG}_generated_configs"
  local run_models_config="${config_dir}/models_round05_enabled.yaml"

  if [[ "${SKIP_CONDA_ACTIVATE:-0}" == "1" ]]; then
    echo "[INFO] SKIP_CONDA_ACTIVATE=1, using current shell environment."
  else
    activate_codex_ollama
  fi

  echo "[INFO] Python compile check..."
  python -m compileall scripts/analysis src

  echo "[INFO] YAML prompt ID check..."
  check_prompt_ids

  echo "[INFO] Preparing model config..."
  write_enabled_models_config "${run_models_config}" "${MODEL_IDS[@]}"

  echo "[INFO] Running benchmark inference..."
  python -m src.run_batch \
    --models "${run_models_config}" \
    --prompts config/prompt_sets.yaml \
    --tasks config/tasks.yaml \
    --output_dir "${OUTPUT_DIR}" \
    --model_ids "${MODEL_IDS[@]}" \
    --prompt_ids "${PROMPT_IDS[@]}" \
    "${TASK_ARGS[@]}" \
    --overwrite

  echo "[INFO] Building merged result index..."
  python scripts/analysis/build_result_index.py \
    --output_dirs "${OUTPUT_DIR}" \
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
    --progress_every "${PROGRESS_EVERY:-1}"

  echo "[INFO] Summarizing VLM judge rereview..."
  python scripts/analysis/summarize_vlm_judge.py \
    --input_dir "${VLM_JUDGE_DIR}" \
    --rule_case_rereview "${ANALYSIS_DIR}/case_rereview.csv"

  check_row_counts

  echo "[INFO] Done."
  echo "  OUTPUT_DIR=${OUTPUT_DIR}"
  echo "  ANALYSIS_DIR=${ANALYSIS_DIR}"
  echo "  VLM_JUDGE_DIR=${VLM_JUDGE_DIR}"
  echo "  Rule handoff: ${ANALYSIS_DIR}/README_FOR_CHATGPT.md"
  echo "  Rule aggregate: ${ANALYSIS_DIR}/aggregate_findings.md"
  echo "  VLM handoff: ${VLM_JUDGE_DIR}/README_FOR_CHATGPT.md"
  echo "  VLM aggregate: ${VLM_JUDGE_DIR}/vlm_aggregate_findings.md"
}
