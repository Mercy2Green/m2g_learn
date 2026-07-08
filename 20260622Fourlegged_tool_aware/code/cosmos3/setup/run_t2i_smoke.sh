#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CODE_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
FRAMEWORK_DIR="${COSMOS_FRAMEWORK_DIR:-${CODE_DIR}/framework}"
ENV_NAME="${COSMOS_ENV_NAME:-codex_cosmos}"
CONDA_PREFIX_OVERRIDE="${COSMOS_CONDA_PREFIX:-}"
CHECKPOINT_PATH="${CHECKPOINT_PATH:-${CODE_DIR}/weights/Cosmos3-Nano}"
OUTPUT_DIR="${OUTPUT_DIR:-${FRAMEWORK_DIR}/outputs/codex_t2i_nano_smoke}"
HF_HOME="${HF_HOME:-${CODE_DIR}/.cache/huggingface}"
CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
INFERENCE_EXTRA_ARGS="${INFERENCE_EXTRA_ARGS:---no-use-torch-compile}"

if [[ ! -d "${FRAMEWORK_DIR}" ]]; then
  echo "ERROR: Cosmos framework repo not found: ${FRAMEWORK_DIR}" >&2
  exit 1
fi

if [[ ! -d "${CHECKPOINT_PATH}" ]]; then
  echo "ERROR: checkpoint path not found: ${CHECKPOINT_PATH}" >&2
  echo "Run: bash ${SCRIPT_DIR}/download_cosmos3_nano_weights.sh" >&2
  exit 1
fi

eval "$(conda shell.bash hook)"
if [[ -n "${CONDA_PREFIX_OVERRIDE}" ]]; then
  conda activate "${CONDA_PREFIX_OVERRIDE}"
else
  conda activate "${ENV_NAME}"
fi

export LD_LIBRARY_PATH=
export HF_HOME
export CUDA_VISIBLE_DEVICES
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

cd "${FRAMEWORK_DIR}"

python -m cosmos_framework.scripts.inference \
  --parallelism-preset=latency \
  ${INFERENCE_EXTRA_ARGS} \
  -i "inputs/omni/t2i.json" \
  -o "${OUTPUT_DIR}" \
  --checkpoint-path "${CHECKPOINT_PATH}" \
  --seed=0 \
  --no-guardrails

echo
echo "Smoke output: ${OUTPUT_DIR}"
