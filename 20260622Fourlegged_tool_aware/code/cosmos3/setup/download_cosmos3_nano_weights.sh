#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CODE_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

DOWNLOAD_SOURCE="${DOWNLOAD_SOURCE:-modelscope}"
MODEL_ID="${MODEL_ID:-nv-community/Cosmos3-Nano}"
MODEL_LOCAL_DIR="${MODEL_LOCAL_DIR:-${CODE_DIR}/weights/Cosmos3-Nano}"
HF_HOME="${HF_HOME:-${CODE_DIR}/.cache/huggingface}"
HF_ENDPOINT="${HF_ENDPOINT:-https://hf-mirror.com}"
MODELSCOPE_CACHE="${MODELSCOPE_CACHE:-${CODE_DIR}/.cache/modelscope}"
MODELSCOPE_MAX_WORKERS="${MODELSCOPE_MAX_WORKERS:-8}"
UV_CACHE_DIR="${UV_CACHE_DIR:-${CODE_DIR}/.cache/uv}"
PYPI_MIRROR="${PYPI_MIRROR:-https://pypi.tuna.tsinghua.edu.cn/simple}"
MIN_FREE_GB="${COSMOS_MODEL_MIN_FREE_GB:-100}"

mkdir -p "$(dirname "${MODEL_LOCAL_DIR}")" "${HF_HOME}" "${MODELSCOPE_CACHE}" "${UV_CACHE_DIR}"

free_gb="$(df -BG "$(dirname "${MODEL_LOCAL_DIR}")" 2>/dev/null | awk 'NR==2 {gsub(/G/,"",$4); print $4}')"
if [[ -n "${free_gb}" ]] && (( free_gb < MIN_FREE_GB )) && [[ "${COSMOS_ALLOW_LOW_DISK:-0}" != "1" ]]; then
  echo "ERROR: only ${free_gb} GiB free near ${MODEL_LOCAL_DIR}; requested minimum is ${MIN_FREE_GB} GiB." >&2
  echo "Set MODEL_LOCAL_DIR and HF_HOME to a large disk, or free space, then rerun." >&2
  echo "To override anyway: COSMOS_ALLOW_LOW_DISK=1 bash $0" >&2
  exit 2
fi

if [[ -z "${HF_TOKEN:-}" ]]; then
  if [[ "${DOWNLOAD_SOURCE}" == "huggingface" ]]; then
    echo "WARNING: HF_TOKEN is not set. If ${MODEL_ID} is gated, download will fail." >&2
    echo "Set it with: export HF_TOKEN=hf_xxx" >&2
  fi
fi

mkdir -p "${MODEL_LOCAL_DIR}"

export HF_HOME
export HF_ENDPOINT
export MODELSCOPE_CACHE
export UV_CACHE_DIR
export UV_DEFAULT_INDEX="${PYPI_MIRROR}"

echo "Downloading ${MODEL_ID}"
echo "Download source: ${DOWNLOAD_SOURCE}"
echo "Local dir: ${MODEL_LOCAL_DIR}"

case "${DOWNLOAD_SOURCE}" in
  modelscope)
    echo "ModelScope cache: ${MODELSCOPE_CACHE}"
    uvx --from modelscope modelscope download \
      --repo-type model \
      --max-workers "${MODELSCOPE_MAX_WORKERS}" \
      --cache-dir "${MODELSCOPE_CACHE}" \
      --local-dir "${MODEL_LOCAL_DIR}" \
      "${MODEL_ID}"
    ;;
  huggingface)
    echo "HF endpoint: ${HF_ENDPOINT}"
    echo "HF cache: ${HF_HOME}"
    uvx --from huggingface-hub hf download \
      --repo-type model \
      "${MODEL_ID}" \
      --local-dir "${MODEL_LOCAL_DIR}"
    ;;
  *)
    echo "ERROR: unsupported DOWNLOAD_SOURCE='${DOWNLOAD_SOURCE}'. Use 'modelscope' or 'huggingface'." >&2
    exit 1
    ;;
esac

if [[ "${DOWNLOAD_GUARDRAILS:-0}" == "1" && "${DOWNLOAD_SOURCE}" == "huggingface" ]]; then
  uvx --from huggingface-hub hf download \
    --repo-type model \
    nvidia/Cosmos-Guardrail1 \
    --local-dir "${CODE_DIR}/weights/Cosmos-Guardrail1"

  uvx --from huggingface-hub hf download \
    --repo-type model \
    Qwen/Qwen3Guard-Gen-0.6B \
    --local-dir "${CODE_DIR}/weights/Qwen3Guard-Gen-0.6B"
elif [[ "${DOWNLOAD_GUARDRAILS:-0}" == "1" ]]; then
  echo "WARNING: DOWNLOAD_GUARDRAILS is currently implemented only for DOWNLOAD_SOURCE=huggingface." >&2
fi

echo
echo "Download completed."
echo "Use checkpoint path: ${MODEL_LOCAL_DIR}"
