#!/usr/bin/env bash
set -euo pipefail

CODE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_NAME="${COSMOS_ENV_NAME:-codex_cosmos}"
CONDA_PREFIX_OVERRIDE="${COSMOS_CONDA_PREFIX:-}"

echo "Code dir: ${CODE_DIR}"
echo
echo "Repositories:"
for repo in upstream framework; do
  if [[ -d "${CODE_DIR}/${repo}/.git" ]]; then
    printf "  %-18s " "${repo}"
    git -C "${CODE_DIR}/${repo}" remote get-url origin
    printf "  %-18s " ""
    git -C "${CODE_DIR}/${repo}" rev-parse --short HEAD
  else
    echo "  ${repo}: missing"
  fi
done

echo
echo "Disk:"
df -h "${CODE_DIR}"
if [[ -n "${CONDA_PREFIX_OVERRIDE}" ]]; then
  df -h "${CONDA_PREFIX_OVERRIDE}" 2>/dev/null || true
fi
if [[ -n "${UV_CACHE_DIR:-}" ]]; then
  df -h "${UV_CACHE_DIR}" 2>/dev/null || true
fi

echo
echo "Conda env:"
if [[ -n "${CONDA_PREFIX_OVERRIDE}" && -x "${CONDA_PREFIX_OVERRIDE}/bin/python" ]]; then
  "${CONDA_PREFIX_OVERRIDE}/bin/python" --version
  "${CONDA_PREFIX_OVERRIDE}/bin/python" -c "import importlib.util; mods=['torch','transformers','diffusers','cosmos_framework','huggingface_hub']; [print(f'{m}: ' + ('ok' if importlib.util.find_spec(m) else 'missing')) for m in mods]"
elif conda env list | awk '{print $1}' | grep -qx "${ENV_NAME}"; then
  conda run -n "${ENV_NAME}" python --version
  conda run -n "${ENV_NAME}" python -c "import importlib.util; mods=['torch','transformers','diffusers','cosmos_framework','huggingface_hub']; [print(f'{m}: ' + ('ok' if importlib.util.find_spec(m) else 'missing')) for m in mods]"
else
  echo "${ENV_NAME}: missing"
fi
