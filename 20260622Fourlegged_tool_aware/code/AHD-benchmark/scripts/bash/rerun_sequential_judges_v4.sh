#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AHD_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"
BENCHMARK_DIR="$(cd "${AHD_DIR}/../test_current_vlm/tool_counterexample_benchmark" && pwd)"
ROOT="${AHD_DIR}/outputs/test_o0o1_v2"
AUDIT_MODEL="${AUDIT_MODEL:-qwen3-vl:32b-instruct-q4_K_M}"
JUDGE_MODEL="${JUDGE_MODEL:-qwen3-vl:32b-instruct-q4_K_M}"
LIMIT="${LIMIT:-}"; RUN_CORE="${RUN_CORE:-1}"; RUN_SENSITIVITY="${RUN_SENSITIVITY:-1}"; OVERWRITE="${OVERWRITE:-0}"; RUN_FULL_VLM="${RUN_FULL_VLM:-0}"
args=(); [[ -n "${LIMIT}" ]] && args+=(--limit "${LIMIT}"); [[ "${OVERWRITE}" == 1 ]] && args+=(--overwrite)
run_one() {
  local dir="$1" audit="${1}/task_image_audit_v2" judge="${1}/response_judge_qwen32_strict_v4_task_state"
  python sequential_o0_o1/text_evaluator_v3.py --input_dir "${dir}" --output_dir "${dir}/analysis_text_v3"
  python sequential_o0_o1/scripts/audit_task_images_v2.py --input_dir "${dir}" --output_dir "${audit}" --audit_model "${AUDIT_MODEL}" "${args[@]}"
  if [[ "${RUN_FULL_VLM}" != 1 && -z "${LIMIT}" ]]; then
    echo "RUN_FULL_VLM is not 1 and LIMIT is empty; skipping VLM judge."
    echo "Exact full-run command: cd ${BENCHMARK_DIR} && RUN_FULL_VLM=1 ${SCRIPT_DIR}/rerun_sequential_judges_v4.sh"
    return 0
  fi
  if [[ "${RUN_FULL_VLM}" == 1 && "${STY:-}" != *m2g* ]]; then
    echo "Not inside screen m2g (STY=${STY:-unset}); refusing long VLM run."
    echo "Exact full-run command: cd ${BENCHMARK_DIR} && RUN_FULL_VLM=1 ${SCRIPT_DIR}/rerun_sequential_judges_v4.sh"
    return 0
  fi
  python sequential_o0_o1/scripts/judge_sequential_responses_v4.py --input_dir "${dir}" --output_dir "${judge}" --image_audit_path "${audit}/image_fact_catalog.jsonl" --judge_model "${JUDGE_MODEL}" "${args[@]}"
  python sequential_o0_o1/scripts/adjudicate_sequential_evaluation_v4.py --text "${dir}/analysis_text_v3/text_evaluation_v3.jsonl" --vlm "${judge}/response_vlm_judge_strict_v4_task_state.jsonl" --image_audit "${audit}/image_fact_catalog.jsonl" --validity_config sequential_o0_o1/configs/model_protocol_validity.yaml --output_dir "${dir}/adjudication_v4"
}
echo "STY=${STY:-unset}"
echo "Candidate experiments and historical raw_responses.jsonl are read-only."
cd "${BENCHMARK_DIR}"
[[ "${RUN_CORE}" == 1 ]] && run_one "${ROOT}/sequential_o0_o1_core_clean_4models_v2"
[[ "${RUN_SENSITIVITY}" == 1 ]] && run_one "${ROOT}/sequential_o0_o1_prompt_sensitivity_3models_v2"
