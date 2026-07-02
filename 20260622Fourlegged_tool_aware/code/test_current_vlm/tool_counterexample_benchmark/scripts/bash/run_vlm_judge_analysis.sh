#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BENCHMARK_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"

INPUT="analysis_review/round04_strong_tools_v2/all_rows_merged.jsonl"
OUTPUT_DIR="analysis_review/round04_strong_tools_vlm_judge_qwen32_full"
RULE_CASE_REREVIEW="analysis_review/round04_strong_tools_v2/case_rereview.csv"
JUDGE_MODEL="qwen3-vl:32b-instruct-q4_K_M"
OLLAMA_URL="http://localhost:11434"
PROGRESS_EVERY="1"
TEMPERATURE="0"
MAX_RETRIES="2"
OVERWRITE="yes"
RUN_SUMMARY="yes"
NO_IMAGE="no"
EXTRA_JUDGE_ARGS=()

usage() {
  cat <<'EOF'
Run image-aware local VLM judge analysis and summary generation.

Default target is the round04 strong-tools analysis:
  input:      analysis_review/round04_strong_tools_v2/all_rows_merged.jsonl
  output_dir: analysis_review/round04_strong_tools_vlm_judge_qwen32_full
  rule:       analysis_review/round04_strong_tools_v2/case_rereview.csv
  judge:      qwen3-vl:32b-instruct-q4_K_M

Usage:
  scripts/bash/run_vlm_judge_analysis.sh [options] [-- extra vlm_judge_rereview.py args]

Options:
  --input PATH                 Merged rows JSONL.
  --output_dir DIR             Judge output directory.
  --rule_case_rereview PATH    Rule rereview CSV for comparison.
  --judge_model MODEL          Ollama judge model.
  --ollama_url URL             Ollama base URL.
  --progress_every N           Print progress every N rows.
  --temperature FLOAT          Judge temperature.
  --max_retries N              JSON retry count.
  --limit N                    Forwarded smoke-test limit.
  --task_ids ...               Forwarded task filter; stop values with another --option or --.
  --model_ids ...              Forwarded tested-model filter; stop values with another --option or --.
  --prompt_ids ...             Forwarded prompt filter; stop values with another --option or --.
  --no_image                   Run judge without images.
  --no_overwrite               Do not pass --overwrite.
  --no_summary                 Skip summarize_vlm_judge.py.
  -h, --help                   Show this help.

Examples:
  scripts/bash/run_vlm_judge_analysis.sh

  scripts/bash/run_vlm_judge_analysis.sh \
    --input analysis_review/another_round/all_rows_merged.jsonl \
    --output_dir analysis_review/another_round_vlm_judge \
    --rule_case_rereview analysis_review/another_round/case_rereview.csv

  scripts/bash/run_vlm_judge_analysis.sh --limit 5 --progress_every 1
EOF
}

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

collect_values() {
  local target_name="$1"
  shift
  local values=()
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --*)
        break
        ;;
      *)
        values+=("$1")
        shift
        ;;
    esac
  done
  if [[ ${#values[@]} -eq 0 ]]; then
    echo "[ERROR] ${target_name} requires at least one value." >&2
    exit 1
  fi
  EXTRA_JUDGE_ARGS+=("${target_name}" "${values[@]}")
  REMAINING_ARGS=("$@")
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --input)
      INPUT="$2"
      shift 2
      ;;
    --output_dir)
      OUTPUT_DIR="$2"
      shift 2
      ;;
    --rule_case_rereview)
      RULE_CASE_REREVIEW="$2"
      shift 2
      ;;
    --judge_model)
      JUDGE_MODEL="$2"
      shift 2
      ;;
    --ollama_url)
      OLLAMA_URL="$2"
      shift 2
      ;;
    --progress_every)
      PROGRESS_EVERY="$2"
      shift 2
      ;;
    --temperature)
      TEMPERATURE="$2"
      shift 2
      ;;
    --max_retries)
      MAX_RETRIES="$2"
      shift 2
      ;;
    --limit)
      EXTRA_JUDGE_ARGS+=("--limit" "$2")
      shift 2
      ;;
    --task_ids|--model_ids|--prompt_ids)
      key="$1"
      shift
      REMAINING_ARGS=()
      collect_values "${key}" "$@"
      set -- "${REMAINING_ARGS[@]}"
      ;;
    --no_image)
      NO_IMAGE="yes"
      shift
      ;;
    --no_overwrite)
      OVERWRITE="no"
      shift
      ;;
    --no_summary)
      RUN_SUMMARY="no"
      shift
      ;;
    --)
      shift
      EXTRA_JUDGE_ARGS+=("$@")
      break
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "[ERROR] Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

cd "${BENCHMARK_DIR}"
activate_codex_ollama

if [[ ! -f "${INPUT}" ]]; then
  echo "[ERROR] Input JSONL not found: ${INPUT}" >&2
  echo "[INFO] Build it first with scripts/analysis/build_result_index.py." >&2
  exit 1
fi

if [[ -n "${RULE_CASE_REREVIEW}" && ! -f "${RULE_CASE_REREVIEW}" ]]; then
  echo "[ERROR] Rule rereview CSV not found: ${RULE_CASE_REREVIEW}" >&2
  exit 1
fi

JUDGE_CMD=(
  python scripts/analysis/vlm_judge_rereview.py
  --input "${INPUT}"
  --output_dir "${OUTPUT_DIR}"
  --judge_model "${JUDGE_MODEL}"
  --ollama_url "${OLLAMA_URL}"
  --temperature "${TEMPERATURE}"
  --max_retries "${MAX_RETRIES}"
  --progress_every "${PROGRESS_EVERY}"
)

if [[ -n "${RULE_CASE_REREVIEW}" ]]; then
  JUDGE_CMD+=(--rule_case_rereview "${RULE_CASE_REREVIEW}")
fi
if [[ "${OVERWRITE}" == "yes" ]]; then
  JUDGE_CMD+=(--overwrite)
fi
if [[ "${NO_IMAGE}" == "yes" ]]; then
  JUDGE_CMD+=(--no_image)
fi
if [[ ${#EXTRA_JUDGE_ARGS[@]} -gt 0 ]]; then
  JUDGE_CMD+=("${EXTRA_JUDGE_ARGS[@]}")
fi

echo "[INFO] Benchmark dir: ${BENCHMARK_DIR}"
echo "[INFO] Input: ${INPUT}"
echo "[INFO] Output dir: ${OUTPUT_DIR}"
echo "[INFO] Rule rereview: ${RULE_CASE_REREVIEW:-<none>}"
echo "[INFO] Judge model: ${JUDGE_MODEL}"
echo "[INFO] Progress every: ${PROGRESS_EVERY}"
echo "[INFO] Running VLM judge..."
"${JUDGE_CMD[@]}"

if [[ "${RUN_SUMMARY}" == "yes" ]]; then
  SUMMARY_CMD=(
    python scripts/analysis/summarize_vlm_judge.py
    --input_dir "${OUTPUT_DIR}"
  )
  if [[ -n "${RULE_CASE_REREVIEW}" ]]; then
    SUMMARY_CMD+=(--rule_case_rereview "${RULE_CASE_REREVIEW}")
  fi
  echo "[INFO] Running VLM judge summary..."
  "${SUMMARY_CMD[@]}"
fi

JSONL="${OUTPUT_DIR}/vlm_case_rereview.jsonl"
CSV="${OUTPUT_DIR}/vlm_case_rereview.csv"
if [[ -f "${JSONL}" && -f "${CSV}" ]]; then
  jsonl_lines="$(wc -l < "${JSONL}")"
  csv_lines="$(wc -l < "${CSV}")"
  echo "[INFO] Row count check:"
  echo "  ${JSONL}: ${jsonl_lines}"
  echo "  ${CSV}: ${csv_lines} (includes header)"
else
  echo "[WARN] Expected judge output files were not both found." >&2
fi

echo "[INFO] Done. Main docs:"
echo "  ${OUTPUT_DIR}/vlm_aggregate_findings.md"
echo "  ${OUTPUT_DIR}/vlm_rule_disagreements.md"
echo "  ${OUTPUT_DIR}/README_FOR_CHATGPT.md"
