#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CODE_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

MODEL_ID="${MODEL_ID:-nvidia/Cosmos3-Nano}"
MODEL_LOCAL_DIR="${MODEL_LOCAL_DIR:-${CODE_DIR}/weights/Cosmos3-Nano}"
HF_HOME="${HF_HOME:-${CODE_DIR}/.cache/huggingface}"
HF_ENDPOINT="${HF_ENDPOINT:-https://hf-mirror.com}"
UV_CACHE_DIR="${UV_CACHE_DIR:-${CODE_DIR}/.cache/uv}"
PYPI_MIRROR="${PYPI_MIRROR:-https://pypi.tuna.tsinghua.edu.cn/simple}"
MIN_FREE_GB="${COSMOS_MODEL_MIN_FREE_GB:-100}"

mkdir -p "$(dirname "${MODEL_LOCAL_DIR}")" "${HF_HOME}" "${UV_CACHE_DIR}"

free_gb="$(df -BG "$(dirname "${MODEL_LOCAL_DIR}")" 2>/dev/null | awk 'NR==2 {gsub(/G/,"",$4); print $4}')"
if [[ -n "${free_gb}" ]] && (( free_gb < MIN_FREE_GB )) && [[ "${COSMOS_ALLOW_LOW_DISK:-0}" != "1" ]]; then
  echo "ERROR: only ${free_gb} GiB free near ${MODEL_LOCAL_DIR}; requested minimum is ${MIN_FREE_GB} GiB." >&2
  echo "Set MODEL_LOCAL_DIR and HF_HOME to a large disk, or free space, then rerun." >&2
  echo "To override anyway: COSMOS_ALLOW_LOW_DISK=1 bash $0" >&2
  exit 2
fi

if [[ -z "${HF_TOKEN:-}" ]]; then
  echo "WARNING: HF_TOKEN is not set. If ${MODEL_ID} is gated, download will fail." >&2
  echo "Set it with: export HF_TOKEN=hf_xxx" >&2
fi

mkdir -p "${MODEL_LOCAL_DIR}"

export HF_HOME
export HF_ENDPOINT
export UV_CACHE_DIR
export UV_DEFAULT_INDEX="${PYPI_MIRROR}"

echo "Downloading ${MODEL_ID}"
echo "HF endpoint: ${HF_ENDPOINT}"
echo "HF cache: ${HF_HOME}"
echo "Local dir: ${MODEL_LOCAL_DIR}"

uvx --from huggingface-hub hf download \
  --repo-type model \
  "${MODEL_ID}" \
  --local-dir "${MODEL_LOCAL_DIR}"

if [[ "${DOWNLOAD_GUARDRAILS:-0}" == "1" ]]; then
  uvx --from huggingface-hub hf download \
    --repo-type model \
    nvidia/Cosmos-Guardrail1 \
    --local-dir "${CODE_DIR}/weights/Cosmos-Guardrail1"

  uvx --from huggingface-hub hf download \
    --repo-type model \
    Qwen/Qwen3Guard-Gen-0.6B \
    --local-dir "${CODE_DIR}/weights/Qwen3Guard-Gen-0.6B"
fi

echo
echo "Download completed."
echo "Use checkpoint path: ${MODEL_LOCAL_DIR}"
