#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AHD_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"
BENCHMARK_DIR="$(cd "${AHD_DIR}/../test_current_vlm/tool_counterexample_benchmark" && pwd)"
OUTPUT_ROOT="${AHD_DIR}/outputs/test_o0o1_v2"
CORE_DIR="${OUTPUT_ROOT}/sequential_o0_o1_core_clean_4models_v2"
SENSITIVITY_DIR="${OUTPUT_ROOT}/sequential_o0_o1_prompt_sensitivity_3models_v2"
LOG_DIR="${AHD_DIR}/outputs/logs"
REPORT="${LOG_DIR}/sequential_vlm_judge_strict_v3_image_audit_completion_report.md"
AUDIT_MODEL="${AUDIT_MODEL:-qwen3-vl:32b-instruct-q4_K_M}"
JUDGE_MODEL="${JUDGE_MODEL:-qwen3-vl:32b-instruct-q4_K_M}"
RUN_CORE="${RUN_CORE:-1}"
RUN_SENSITIVITY="${RUN_SENSITIVITY:-1}"
OVERWRITE="${OVERWRITE:-0}"
LIMIT="${LIMIT:-}"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
LOG_FILE="${LOG_DIR}/rerun_sequential_vlm_judge_strict_v3_image_audit_${TIMESTAMP}.log"

mkdir -p "${LOG_DIR}"

optional_args=()
if [[ -n "${LIMIT}" ]]; then
  optional_args+=(--limit "${LIMIT}")
fi
if [[ "${OVERWRITE}" == "1" ]]; then
  optional_args+=(--overwrite)
fi

run_experiment() {
  local input_dir="$1"
  local audit_dir="${input_dir}/task_image_audit_qwen32"
  local judge_dir="${input_dir}/response_judge_qwen32_strict_v3_image_audit"

  python sequential_o0_o1/scripts/audit_task_images.py \
    --input_dir "${input_dir}" \
    --output_dir "${audit_dir}" \
    --audit_model "${AUDIT_MODEL}" \
    "${optional_args[@]}"

  python sequential_o0_o1/scripts/judge_sequential_responses.py \
    --input_dir "${input_dir}" \
    --output_dir "${judge_dir}" \
    --judge_model "${JUDGE_MODEL}" \
    --judge_version strict_v3_image_audit \
    --image_audit_path "${audit_dir}/image_pair_audit.jsonl" \
    "${optional_args[@]}"
}

write_report() {
  {
    echo "# Sequential Strict VLM Judge V3 Image-Audit Completion Report"
    echo
    echo "- Candidate VLM experiments were not rerun."
    echo "- Task images were audited first; only the response-level VLM judge was rerun with audit metadata."
    echo "- Audit model: ${AUDIT_MODEL}"
    echo "- Judge model: ${JUDGE_MODEL}"
    echo "- Limit: ${LIMIT:-none}"
    if [[ "${RUN_CORE}" == "1" ]]; then
      echo
      echo "## Core Image Audit"
      echo
      cat "${CORE_DIR}/task_image_audit_qwen32/image_pair_audit_summary.md"
      echo
      echo "## Core Strict V3"
      echo
      cat "${CORE_DIR}/response_judge_qwen32_strict_v3_image_audit/response_vlm_judge_summary_strict_v3_image_audit.md"
      echo
      echo "## Core V3 vs Heuristic V2"
      echo
      cat "${CORE_DIR}/response_judge_qwen32_strict_v3_image_audit/vlm_v3_vs_v2_summary.md"
      echo
      echo "Core manual review pack: ${CORE_DIR}/response_judge_qwen32_strict_v3_image_audit/manual_review_pack_vlm_strict_v3_image_audit.md"
    fi
    if [[ "${RUN_SENSITIVITY}" == "1" ]]; then
      echo
      echo "## Sensitivity Image Audit"
      echo
      cat "${SENSITIVITY_DIR}/task_image_audit_qwen32/image_pair_audit_summary.md"
      echo
      echo "## Sensitivity Strict V3"
      echo
      cat "${SENSITIVITY_DIR}/response_judge_qwen32_strict_v3_image_audit/response_vlm_judge_summary_strict_v3_image_audit.md"
      echo
      echo "## Sensitivity V3 vs Heuristic V2"
      echo
      cat "${SENSITIVITY_DIR}/response_judge_qwen32_strict_v3_image_audit/vlm_v3_vs_v2_summary.md"
      echo
      echo "Sensitivity manual review pack: ${SENSITIVITY_DIR}/response_judge_qwen32_strict_v3_image_audit/manual_review_pack_vlm_strict_v3_image_audit.md"
    fi
  } > "${REPORT}"
  echo "Wrote completion report: ${REPORT}"
}

run_all() {
  echo "Task image audit plus strict VLM judge v3 only; candidate VLM evaluations will not be rerun."
  echo "Audit model: ${AUDIT_MODEL}"
  echo "Judge model: ${JUDGE_MODEL}"
  echo "Limit: ${LIMIT:-none}"
  cd "${BENCHMARK_DIR}"
  if [[ "${RUN_CORE}" == "1" ]]; then
    run_experiment "${CORE_DIR}"
  fi
  if [[ "${RUN_SENSITIVITY}" == "1" ]]; then
    run_experiment "${SENSITIVITY_DIR}"
  fi
  write_report
}

run_all 2>&1 | tee "${LOG_FILE}"
