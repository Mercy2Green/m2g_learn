#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AHD_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"
BENCHMARK_DIR="$(cd "${AHD_DIR}/../test_current_vlm/tool_counterexample_benchmark" && pwd)"
LOG_DIR="${AHD_DIR}/outputs/logs"
REVIEW_IMAGES_DIR="${AHD_DIR}/outputs/sequential_analysis_v2_review_images"
CORE_DIR="${BENCHMARK_DIR}/outputs/sequential_o0_o1_core_clean_4models"
SENSITIVITY_DIR="${BENCHMARK_DIR}/outputs/sequential_o0_o1_prompt_sensitivity_3models"
REPORT="${LOG_DIR}/sequential_analysis_v2_completion_report.md"
JUDGE_MODEL="${JUDGE_MODEL:-qwen3-vl:32b-instruct-q4_K_M}"
CORE_JUDGE_DIR="${CORE_DIR}/analysis_v2/response_judge_qwen32"
SENSITIVITY_JUDGE_DIR="${SENSITIVITY_DIR}/analysis_v2/response_judge_qwen32"

mkdir -p "${LOG_DIR}" "${REVIEW_IMAGES_DIR}"
cd "${BENCHMARK_DIR}"

python sequential_o0_o1/scripts/resummarize_existing_sequential_eval_v2.py \
  --input_dir "${CORE_DIR}" \
  --output_dir "${CORE_DIR}/analysis_v2" \
  --review_images_dir "${REVIEW_IMAGES_DIR}" \
  --experiment_name core_clean_4models \
  --overwrite

python sequential_o0_o1/scripts/resummarize_existing_sequential_eval_v2.py \
  --input_dir "${SENSITIVITY_DIR}" \
  --output_dir "${SENSITIVITY_DIR}/analysis_v2" \
  --review_images_dir "${REVIEW_IMAGES_DIR}" \
  --experiment_name prompt_sensitivity_3models \
  --overwrite

python sequential_o0_o1/scripts/judge_sequential_responses.py \
  --input_dir "${CORE_DIR}" \
  --judge_model "${JUDGE_MODEL}" \
  --output_dir "${CORE_JUDGE_DIR}" \
  --overwrite

python sequential_o0_o1/scripts/judge_sequential_responses.py \
  --input_dir "${SENSITIVITY_DIR}" \
  --judge_model "${JUDGE_MODEL}" \
  --output_dir "${SENSITIVITY_JUDGE_DIR}" \
  --overwrite

{
  echo "# Sequential O0/O1 Analysis V2 Completion Report"
  echo
  echo "- Candidate VLM experiments were not rerun; analysis used existing raw_responses.jsonl files only."
  echo "- The response-level VLM judge was rerun with the revised O0/O1 judging prompt."
  echo "- Judge model: ${JUDGE_MODEL}"
  echo "- Core manual review pack: ${CORE_DIR}/analysis_v2/manual_review_pack_v2.md"
  echo "- Sensitivity manual review pack: ${SENSITIVITY_DIR}/analysis_v2/manual_review_pack_v2.md"
  echo "- Review images: ${REVIEW_IMAGES_DIR}"
  echo
  echo "## Core Analysis V2"
  echo
  cat "${CORE_DIR}/analysis_v2/summary_v2.md"
  echo
  echo "## Prompt Sensitivity Analysis V2"
  echo
  cat "${SENSITIVITY_DIR}/analysis_v2/summary_v2.md"
  echo
  echo "## Core Response Judge"
  echo
  cat "${CORE_JUDGE_DIR}/response_vlm_judge_summary.md"
  echo
  echo "## Prompt Sensitivity Response Judge"
  echo
  cat "${SENSITIVITY_JUDGE_DIR}/response_vlm_judge_summary.md"
} > "${REPORT}"

echo "Wrote completion report: ${REPORT}"
