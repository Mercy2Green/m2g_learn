#!/usr/bin/env bash
set -euo pipefail

AHD_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
BENCHMARK_DIR="$(cd "${AHD_DIR}/../test_current_vlm/tool_counterexample_benchmark" && pwd)"
INPUT_DIR="${INPUT_DIR:-outputs/sequential_o0_o1_core_clean_4models}"
OUTPUT_DIR="${OUTPUT_DIR:-${INPUT_DIR}/response_judge_qwen32}"
JUDGE_MODEL="${JUDGE_MODEL:-qwen3-vl:32b-instruct-q4_K_M}"

cd "${BENCHMARK_DIR}"
python sequential_o0_o1/scripts/judge_sequential_responses.py \
  --input_dir "${INPUT_DIR}" \
  --judge_model "${JUDGE_MODEL}" \
  --output_dir "${OUTPUT_DIR}" \
  --overwrite \
  "$@"

echo "Sequential response judge complete: ${BENCHMARK_DIR}/${OUTPUT_DIR}"
