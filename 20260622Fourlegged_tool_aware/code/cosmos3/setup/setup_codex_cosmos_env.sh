#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CODE_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
FRAMEWORK_DIR="${COSMOS_FRAMEWORK_DIR:-${CODE_DIR}/framework}"

ENV_NAME="${COSMOS_ENV_NAME:-codex_cosmos}"
CONDA_PREFIX_OVERRIDE="${COSMOS_CONDA_PREFIX:-}"
PYTHON_VERSION="${COSMOS_PYTHON_VERSION:-3.13}"
UV_GROUP="${COSMOS_UV_GROUP:-cu128-train}"
PYPI_MIRROR="${PYPI_MIRROR:-https://pypi.tuna.tsinghua.edu.cn/simple}"
UV_CACHE_DIR="${UV_CACHE_DIR:-${CODE_DIR}/.cache/uv}"
MIN_FREE_GB="${COSMOS_MIN_FREE_GB:-120}"

if [[ ! -d "${FRAMEWORK_DIR}" ]]; then
  echo "ERROR: Cosmos framework repo not found: ${FRAMEWORK_DIR}" >&2
  echo "Clone it with: git clone https://github.com/NVIDIA/cosmos-framework.git ${FRAMEWORK_DIR}" >&2
  exit 1
fi

if ! command -v conda >/dev/null 2>&1; then
  echo "ERROR: conda is required for the requested env name '${ENV_NAME}'." >&2
  exit 1
fi

mkdir -p "${UV_CACHE_DIR}"

eval "$(conda shell.bash hook)"

if [[ -n "${CONDA_PREFIX_OVERRIDE}" ]]; then
  mkdir -p "$(dirname "${CONDA_PREFIX_OVERRIDE}")"
  if [[ ! -x "${CONDA_PREFIX_OVERRIDE}/bin/python" ]]; then
    conda create -y -p "${CONDA_PREFIX_OVERRIDE}" "python=${PYTHON_VERSION}" \
      -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main \
      -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  fi
  conda activate "${CONDA_PREFIX_OVERRIDE}"
else
  if ! conda env list | awk '{print $1}' | grep -qx "${ENV_NAME}"; then
    conda create -y -n "${ENV_NAME}" "python=${PYTHON_VERSION}" \
      -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main \
      -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  fi
  conda activate "${ENV_NAME}"
fi

env_free_gb="$(df -BG "${CONDA_PREFIX}" | awk 'NR==2 {gsub(/G/,"",$4); print $4}')"
cache_free_gb="$(df -BG "${UV_CACHE_DIR}" | awk 'NR==2 {gsub(/G/,"",$4); print $4}')"
if { (( env_free_gb < MIN_FREE_GB )) || (( cache_free_gb < MIN_FREE_GB )); } && [[ "${COSMOS_ALLOW_LOW_DISK:-0}" != "1" ]]; then
  echo "ERROR: insufficient free disk for Cosmos dependencies." >&2
  echo "Conda env path: ${CONDA_PREFIX} (${env_free_gb} GiB free)" >&2
  echo "UV cache path: ${UV_CACHE_DIR} (${cache_free_gb} GiB free)" >&2
  echo "Requested minimum: ${MIN_FREE_GB} GiB." >&2
  echo "Use COSMOS_CONDA_PREFIX and UV_CACHE_DIR on a large disk, or free space, then rerun." >&2
  echo "To override anyway: COSMOS_ALLOW_LOW_DISK=1 bash $0" >&2
  exit 2
fi

if [[ "${COSMOS_RECREATE_ENV:-0}" == "1" ]]; then
  if [[ -n "${CONDA_PREFIX_OVERRIDE}" ]]; then
    conda deactivate
    rm -rf "${CONDA_PREFIX_OVERRIDE}"
    conda create -y -p "${CONDA_PREFIX_OVERRIDE}" "python=${PYTHON_VERSION}" \
    -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main \
    -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
    conda activate "${CONDA_PREFIX_OVERRIDE}"
  else
    conda deactivate
    conda env remove -y -n "${ENV_NAME}"
    conda create -y -n "${ENV_NAME}" "python=${PYTHON_VERSION}" \
      -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main \
      -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
    conda activate "${ENV_NAME}"
  fi
fi

export UV_DEFAULT_INDEX="${PYPI_MIRROR}"
export UV_CACHE_DIR
export UV_LINK_MODE="${UV_LINK_MODE:-copy}"
export LD_LIBRARY_PATH=

cd "${FRAMEWORK_DIR}"

echo "Using conda env: ${CONDA_PREFIX}"
echo "Using uv group: ${UV_GROUP}"
echo "Using PyPI mirror: ${UV_DEFAULT_INDEX}"
echo "Using uv cache: ${UV_CACHE_DIR}"

uv pip install \
  --python "${CONDA_PREFIX}/bin/python" \
  -r pyproject.toml \
  --all-extras \
  --group="${UV_GROUP}"

uv pip install \
  --python "${CONDA_PREFIX}/bin/python" \
  -e .

python - <<'PY'
import importlib.util
import sys

mods = ["torch", "transformers", "diffusers", "cosmos_framework", "huggingface_hub"]
print("python:", sys.version.split()[0])
for mod in mods:
    print(f"{mod}:", "ok" if importlib.util.find_spec(mod) else "missing")
PY

echo
echo "Environment sync completed."
if [[ -n "${CONDA_PREFIX_OVERRIDE}" ]]; then
  echo "Activate with: conda activate ${CONDA_PREFIX_OVERRIDE}"
else
  echo "Activate with: conda activate ${ENV_NAME}"
fi
echo "Then run from: ${FRAMEWORK_DIR}"
