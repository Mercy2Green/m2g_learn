#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AHD_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"
BENCHMARK_DIR="$(cd "${AHD_DIR}/../test_current_vlm/tool_counterexample_benchmark" && pwd)"
OUTPUT_ROOT="${AHD_DIR}/outputs/test_o0o1_v2"
CORE_DIR="${OUTPUT_ROOT}/sequential_o0_o1_core_clean_4models_v2"
SENSITIVITY_DIR="${OUTPUT_ROOT}/sequential_o0_o1_prompt_sensitivity_3models_v2"
CORE_JUDGE_DIR="${CORE_DIR}/response_judge_qwen32_strict_v2"
SENSITIVITY_JUDGE_DIR="${SENSITIVITY_DIR}/response_judge_qwen32_strict_v2"
LOG_DIR="${AHD_DIR}/outputs/logs"
REPORT="${LOG_DIR}/sequential_vlm_judge_strict_v2_completion_report.md"
JUDGE_MODEL="${JUDGE_MODEL:-qwen3-vl:32b-instruct-q4_K_M}"
RUN_CORE="${RUN_CORE:-1}"
RUN_SENSITIVITY="${RUN_SENSITIVITY:-1}"
LIMIT="${LIMIT:-}"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
LOG_FILE="${LOG_DIR}/rerun_sequential_vlm_judge_strict_v2_${TIMESTAMP}.log"

mkdir -p "${LOG_DIR}"

run_judge() {
  local input_dir="$1"
  local output_dir="$2"
  local args=(
    sequential_o0_o1/scripts/judge_sequential_responses.py
    --input_dir "${input_dir}"
    --output_dir "${output_dir}"
    --judge_model "${JUDGE_MODEL}"
    --judge_version strict_v2
    --overwrite
  )
  if [[ -n "${LIMIT}" ]]; then
    args+=(--limit "${LIMIT}")
  fi
  python "${args[@]}"
}

run_all() {
  echo "Strict VLM judge v2 only; candidate VLM evaluations will not be rerun."
  echo "Judge model: ${JUDGE_MODEL}"
  echo "Limit: ${LIMIT:-none}"
  cd "${BENCHMARK_DIR}"

  if [[ "${RUN_CORE}" == "1" ]]; then
    run_judge "${CORE_DIR}" "${CORE_JUDGE_DIR}"
  fi
  if [[ "${RUN_SENSITIVITY}" == "1" ]]; then
    run_judge "${SENSITIVITY_DIR}" "${SENSITIVITY_JUDGE_DIR}"
  fi

  {
    echo "# Sequential Strict VLM Judge V2 Completion Report"
    echo
    echo "- Candidate VLM experiments were not rerun."
    echo "- Only the response-level strict VLM judge v2 was run."
    echo "- Judge model: ${JUDGE_MODEL}"
    echo "- Limit: ${LIMIT:-none}"
    echo "- Core manual review pack: ${CORE_JUDGE_DIR}/manual_review_pack_vlm_strict_v2.md"
    echo "- Sensitivity manual review pack: ${SENSITIVITY_JUDGE_DIR}/manual_review_pack_vlm_strict_v2.md"
    if [[ "${RUN_CORE}" == "1" ]]; then
      echo
      echo "## Core Strict V2 Summary"
      echo
      cat "${CORE_JUDGE_DIR}/response_vlm_judge_summary_strict_v2.md"
      echo
      echo "## Core VLM vs Heuristic V2"
      echo
      cat "${CORE_JUDGE_DIR}/vlm_vs_v2_summary.md"
    fi
    if [[ "${RUN_SENSITIVITY}" == "1" ]]; then
      echo
      echo "## Sensitivity Strict V2 Summary"
      echo
      cat "${SENSITIVITY_JUDGE_DIR}/response_vlm_judge_summary_strict_v2.md"
      echo
      echo "## Sensitivity VLM vs Heuristic V2"
      echo
      cat "${SENSITIVITY_JUDGE_DIR}/vlm_vs_v2_summary.md"
    fi
  } > "${REPORT}"
  echo "Wrote completion report: ${REPORT}"
}

run_all 2>&1 | tee "${LOG_FILE}"
