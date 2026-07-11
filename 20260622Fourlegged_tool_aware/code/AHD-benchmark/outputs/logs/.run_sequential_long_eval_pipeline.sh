#!/usr/bin/env bash
set -euo pipefail

cd /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/AHD-benchmark

TS="$(date +%Y%m%d_%H%M%S)"
STATUS_LOG="outputs/logs/sequential_long_eval_pipeline_status.log"
CORE_LOG="outputs/logs/run_sequential_core_eval_4models_${TS}.log"
SENS_LOG="outputs/logs/run_sequential_prompt_sensitivity_3models_${TS}.log"
SENS_JUDGE_LOG="outputs/logs/run_sequential_prompt_sensitivity_response_judge_${TS}.log"

{
  echo "STARTED $(date --iso-8601=seconds)"
  echo "SCREEN_SESSION=m2g"
  echo "SCREEN_WINDOW=seq_long"
  echo "PARALLEL_MODELS_CORE=2"
  echo "PARALLEL_MODELS_SENSITIVITY=2"
  echo "CORE_LOG=${CORE_LOG}"
  echo "SENSITIVITY_LOG=${SENS_LOG}"
  echo "SENSITIVITY_JUDGE_LOG=${SENS_JUDGE_LOG}"
} > "${STATUS_LOG}"

fail() {
  echo "FAILED_STAGE=$1" | tee -a "${STATUS_LOG}"
  echo "FAILED_AT=$(date --iso-8601=seconds)" | tee -a "${STATUS_LOG}"
  exit 1
}

echo "===== CORE CLEAN START $(date --iso-8601=seconds) =====" | tee "${CORE_LOG}"
if ! RUN_JUDGE=1 PARALLEL_MODELS=2 bash scripts/bash/run_sequential_core_eval.sh 2>&1 | tee -a "${CORE_LOG}"; then
  fail core_clean
fi

CORE_ROOT="../test_current_vlm/tool_counterexample_benchmark/outputs/sequential_o0_o1_core_clean_4models"
CORE_FILES=(
  raw_responses.jsonl
  parsed_results.jsonl
  sequential_evaluation.csv
  summary.md
  failed_cases.md
  response_judge_qwen32/response_vlm_judge.jsonl
  response_judge_qwen32/response_vlm_judge_summary.md
  response_judge_qwen32/disagreement_cases.md
)
for file in "${CORE_FILES[@]}"; do
  [[ -f "${CORE_ROOT}/${file}" ]] || fail "core_missing_${file//\//_}"
done
echo "CORE_FILES_VERIFIED=YES" | tee -a "${STATUS_LOG}"

echo "===== PROMPT SENSITIVITY START $(date --iso-8601=seconds) =====" | tee "${SENS_LOG}"
if ! PARALLEL_MODELS=2 bash scripts/bash/run_sequential_prompt_sensitivity.sh 2>&1 | tee -a "${SENS_LOG}"; then
  fail prompt_sensitivity
fi

SENS_ROOT="../test_current_vlm/tool_counterexample_benchmark/outputs/sequential_o0_o1_prompt_sensitivity_3models"
SENS_FILES=(raw_responses.jsonl parsed_results.jsonl sequential_evaluation.csv summary.md failed_cases.md)
for file in "${SENS_FILES[@]}"; do
  [[ -f "${SENS_ROOT}/${file}" ]] || fail "sensitivity_missing_${file}"
done
echo "SENSITIVITY_FILES_VERIFIED=YES" | tee -a "${STATUS_LOG}"

echo "===== PROMPT SENSITIVITY JUDGE START $(date --iso-8601=seconds) =====" | tee "${SENS_JUDGE_LOG}"
if ! INPUT_DIR=outputs/sequential_o0_o1_prompt_sensitivity_3models \
  OUTPUT_DIR=outputs/sequential_o0_o1_prompt_sensitivity_3models/response_judge_qwen32 \
  JUDGE_MODEL=qwen3-vl:32b-instruct-q4_K_M \
  bash scripts/bash/run_sequential_response_judge.sh 2>&1 | tee -a "${SENS_JUDGE_LOG}"; then
  fail prompt_sensitivity_response_judge
fi

SENS_JUDGE_FILES=(
  response_judge_qwen32/response_vlm_judge.jsonl
  response_judge_qwen32/response_vlm_judge_summary.md
  response_judge_qwen32/disagreement_cases.md
)
for file in "${SENS_JUDGE_FILES[@]}"; do
  [[ -f "${SENS_ROOT}/${file}" ]] || fail "sensitivity_judge_missing_${file//\//_}"
done
echo "SENSITIVITY_JUDGE_FILES_VERIFIED=YES" | tee -a "${STATUS_LOG}"

cat > outputs/logs/sequential_long_eval_completion_report.md <<'EOF'
# Sequential O0/O1 Long Eval Completion Report

## Core Clean 4 Models
Output:
../test_current_vlm/tool_counterexample_benchmark/outputs/sequential_o0_o1_core_clean_4models

Expected files:
- raw_responses.jsonl
- parsed_results.jsonl
- sequential_evaluation.csv
- summary.md
- failed_cases.md
- response_judge_qwen32/response_vlm_judge.jsonl
- response_judge_qwen32/response_vlm_judge_summary.md
- response_judge_qwen32/disagreement_cases.md

## Prompt Sensitivity 3 Models
Output:
../test_current_vlm/tool_counterexample_benchmark/outputs/sequential_o0_o1_prompt_sensitivity_3models

Expected files:
- raw_responses.jsonl
- parsed_results.jsonl
- sequential_evaluation.csv
- summary.md
- failed_cases.md
- response_judge_qwen32/response_vlm_judge.jsonl
- response_judge_qwen32/response_vlm_judge_summary.md
- response_judge_qwen32/disagreement_cases.md

## Notes
- qwen3.5:35b must be included.
- Response judge is secondary evidence only.
- generation_budget_exhausted/provider_error rows are not task-capability failures.
EOF

CORE_SUMMARY="${CORE_ROOT}/summary.md"
CORE_JUDGE="${CORE_ROOT}/response_judge_qwen32/response_vlm_judge_summary.md"
SENS_SUMMARY="${SENS_ROOT}/summary.md"
SENS_JUDGE="${SENS_ROOT}/response_judge_qwen32/response_vlm_judge_summary.md"

{
  echo ""
  echo "## Core Summary"
  [[ -f "${CORE_SUMMARY}" ]] && cat "${CORE_SUMMARY}" || echo "Missing ${CORE_SUMMARY}"
  echo ""
  echo "## Core Judge Summary"
  [[ -f "${CORE_JUDGE}" ]] && cat "${CORE_JUDGE}" || echo "Missing ${CORE_JUDGE}"
  echo ""
  echo "## Sensitivity Summary"
  [[ -f "${SENS_SUMMARY}" ]] && cat "${SENS_SUMMARY}" || echo "Missing ${SENS_SUMMARY}"
  echo ""
  echo "## Sensitivity Judge Summary"
  [[ -f "${SENS_JUDGE}" ]] && cat "${SENS_JUDGE}" || echo "Missing ${SENS_JUDGE}"
} >> outputs/logs/sequential_long_eval_completion_report.md

echo "COMPLETED $(date --iso-8601=seconds)" | tee -a "${STATUS_LOG}"
