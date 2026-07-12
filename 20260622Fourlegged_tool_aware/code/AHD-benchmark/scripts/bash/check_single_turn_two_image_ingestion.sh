#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AHD_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"
BENCHMARK_DIR="$(cd "${AHD_DIR}/../test_current_vlm/tool_counterexample_benchmark" && pwd)"
OUTPUT_DIR="${AHD_DIR}/outputs/sanity_check_single_turn_two_images"
LOG_DIR="${AHD_DIR}/outputs/logs"
REPORT="${LOG_DIR}/check_single_turn_two_image_ingestion_completion_report.md"
MODEL_IDS="${MODEL_IDS:-ollama_qwen3_5_35b}"
LIMIT="${LIMIT:-}"
OVERWRITE="${OVERWRITE:-0}"
REUSE_RAW="${REUSE_RAW:-0}"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
LOG_FILE="${LOG_DIR}/check_single_turn_two_image_ingestion_${TIMESTAMP}.log"

mkdir -p "${LOG_DIR}"
read -r -a model_args <<< "${MODEL_IDS}"
args=(
  sequential_o0_o1/scripts/check_single_turn_two_image_ingestion.py
  --models config/models.yaml
  --model_overrides sequential_o0_o1/config/sequential_model_overrides.yaml
  --output_dir "${OUTPUT_DIR}"
  --model_ids "${model_args[@]}"
)
if [[ -n "${LIMIT}" ]]; then
  args+=(--limit "${LIMIT}")
fi
if [[ "${OVERWRITE}" == "1" ]]; then
  args+=(--overwrite)
fi
if [[ "${REUSE_RAW}" == "1" ]]; then
  args+=(--reuse_raw)
fi

run_all() {
  echo "Single-turn image-ingestion diagnostic only; original candidate benchmark will not be rerun."
  echo "Models: ${MODEL_IDS}"
  echo "Sample limit: ${LIMIT:-none}"
  cd "${BENCHMARK_DIR}"
  python "${args[@]}"
  {
    echo "# Single-Turn Two-Image Ingestion Completion Report"
    echo
    echo "- Original helper-chain candidate experiments were not rerun."
    echo "- Original task prompts were not strengthened or modified."
    echo "- This run only checks image ingestion and image-order perception."
    echo "- Models: ${MODEL_IDS}"
    echo "- Sample limit: ${LIMIT:-none}"
    echo
    cat "${OUTPUT_DIR}/diagnostic_summary.md"
    echo
    echo "Manual review: ${OUTPUT_DIR}/diagnostic_manual_review.md"
    echo "Payload manifest: ${OUTPUT_DIR}/payload_manifest.jsonl"
  } > "${REPORT}"
  echo "Wrote completion report: ${REPORT}"
}

run_all 2>&1 | tee "${LOG_FILE}"
