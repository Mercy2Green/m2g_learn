# Cosmos3 配置与使用说明

本目录统一放置 Cosmos3 相关内容，避免 `code/` 下出现多个同名目录。

## 目录结构

```text
cosmos3/
├── README.md                 # 本说明
├── upstream/                 # NVIDIA/Cosmos 官方入口仓库，包含 README、cookbooks、evaluation
├── framework/                # NVIDIA/cosmos-framework，可运行的训练/推理框架
├── setup/                    # 本项目本地化配置、下载、smoke-run 脚本
├── weights/                  # 模型权重默认下载位置，已 gitignore
└── .cache/                   # HF/uv 默认缓存位置，已 gitignore
```

当前推荐模型：`nv-community/Cosmos3-Nano`（ModelScope），对应 Hugging Face 上的 `nvidia/Cosmos3-Nano`。

## 当前机器配置

- GPU：4 x NVIDIA RTX A6000 48GB
- Driver：570.133.07
- 已验证环境：`/data0/yurunze/conda_envs/codex_cosmos`
- Python：3.13.14
- PyTorch：2.10.0+cu128
- CUDA runtime：12.8
- 已验证可 import：`torch`、`transformers`、`diffusers`、`cosmos_framework`、`huggingface_hub`

根分区当前空间较紧，建议把 conda 环境、uv cache、HF cache、权重都放到 `/data0/yurunze/` 或其它大盘。

## 环境配置

已配置好的环境路径：

```bash
conda activate /data0/yurunze/conda_envs/codex_cosmos
```

重新同步环境时从本目录的上一级 `code/` 或本目录执行都可以：

```bash
cd /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/cosmos3

COSMOS_CONDA_PREFIX=/data0/yurunze/conda_envs/codex_cosmos \
UV_CACHE_DIR=/data0/yurunze/cosmos3/uv-cache \
bash setup/setup_codex_cosmos_env.sh
```

默认依赖组是 `cu128-train`，适合当前驱动与 A6000 环境。如果后续升级驱动并要试 CUDA 13，可显式切换：

```bash
COSMOS_UV_GROUP=cu130-train \
COSMOS_CONDA_PREFIX=/data0/yurunze/conda_envs/codex_cosmos \
UV_CACHE_DIR=/data0/yurunze/cosmos3/uv-cache \
bash setup/setup_codex_cosmos_env.sh
```

如果要彻底重建环境：

```bash
COSMOS_RECREATE_ENV=1 \
COSMOS_CONDA_PREFIX=/data0/yurunze/conda_envs/codex_cosmos \
UV_CACHE_DIR=/data0/yurunze/cosmos3/uv-cache \
bash setup/setup_codex_cosmos_env.sh
```

## 下载 Cosmos3-Nano 权重

默认从 ModelScope 下载：

```bash
cd /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/cosmos3

MODELSCOPE_CACHE=/data0/yurunze/models/modelscope-cache \
MODEL_LOCAL_DIR=/data0/yurunze/models/Cosmos3-Nano \
bash setup/download_cosmos3_nano_weights.sh
```

如果要改回 Hugging Face 下载，先在 Hugging Face 上接受 `nvidia/Cosmos3-Nano` 的模型许可，并准备 read token：

```bash
export HF_TOKEN=hf_xxx

DOWNLOAD_SOURCE=huggingface \
MODEL_ID=nvidia/Cosmos3-Nano \
HF_HOME=/data0/yurunze/cosmos3/hf-cache \
MODEL_LOCAL_DIR=/data0/yurunze/models/Cosmos3-Nano \
bash setup/download_cosmos3_nano_weights.sh
```

不传 `MODEL_LOCAL_DIR` 时，默认下载到：

```text
code/cosmos3/weights/Cosmos3-Nano
```

## 运行 text-to-image smoke test

权重下载完成后运行：

```bash
cd /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/cosmos3

COSMOS_CONDA_PREFIX=/data0/yurunze/conda_envs/codex_cosmos \
CHECKPOINT_PATH=/data0/yurunze/models/Cosmos3-Nano \
HF_HOME=/data0/yurunze/models/hf-cache \
CUDA_VISIBLE_DEVICES=1 \
OUTPUT_DIR=/home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/cosmos3/framework/outputs/codex_t2i_nano_smoke_modelscope \
bash setup/run_t2i_smoke.sh
```

默认输出目录：

```text
code/cosmos3/framework/outputs/codex_t2i_nano_smoke
```

脚本使用 `framework/inputs/omni/t2i.json`，默认额外传入 `--no-use-torch-compile`，并加了 `--no-guardrails`，避免 smoke test 额外拉 guardrail 模型。需要覆盖额外参数时设置 `INFERENCE_EXTRA_ARGS`。

首次运行官方 framework 推理时，除了 `/data0/yurunze/models/Cosmos3-Nano` 主权重，还会自动下载以下辅助组件到 `HF_HOME`：

- `Qwen/Qwen3-VL-8B-Instruct`
- `Wan-AI/Wan2.2-TI2V-5B` 的 `Wan2.2_VAE.pth`
- `nvidia/Cosmos3-Nano` 的 `sound_tokenizer/*`

本机已缓存到：

```text
/data0/yurunze/models/hf-cache
```

后续 smoke test 会复用这些缓存，不需要重复下载。

## 已通过的 smoke tests

测试日期：2026-07-08。

1. 环境导入与 CUDA 检查

```bash
/data0/yurunze/conda_envs/codex_cosmos/bin/python - <<'PY'
import cosmos_framework, torch
print(cosmos_framework.__file__)
print(torch.__version__)
print(torch.cuda.is_available(), torch.cuda.device_count())
PY
```

结果：

```text
cosmos_framework: code/cosmos3/framework/cosmos_framework/__init__.py
torch: 2.10.0+cu128
cuda: True 4
```

2. CLI 可用性检查

```bash
cd /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/cosmos3/framework
/data0/yurunze/conda_envs/codex_cosmos/bin/python -m cosmos_framework.scripts.inference --help
```

结果：成功输出 inference 参数说明。

3. Cosmos3-Nano text-to-image 本地权重推理

```bash
cd /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/cosmos3

COSMOS_CONDA_PREFIX=/data0/yurunze/conda_envs/codex_cosmos \
CHECKPOINT_PATH=/data0/yurunze/models/Cosmos3-Nano \
HF_HOME=/data0/yurunze/models/hf-cache \
CUDA_VISIBLE_DEVICES=1 \
OUTPUT_DIR=/home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/cosmos3/framework/outputs/codex_t2i_nano_smoke_modelscope \
bash setup/run_t2i_smoke.sh
```

结果：

```text
status: success
output: code/cosmos3/framework/outputs/codex_t2i_nano_smoke_modelscope/t2i/vision.jpg
image: JPEG, 960x960
```

同一命令通过 `setup/run_t2i_smoke.sh` 包装脚本复测通过，输出：

```text
code/cosmos3/framework/outputs/codex_t2i_nano_smoke_script/t2i/vision.jpg
```

## 状态检查

```bash
cd /home/yurunze/peter_ws/m2g_learn/20260622Fourlegged_tool_aware/code/cosmos3

COSMOS_CONDA_PREFIX=/data0/yurunze/conda_envs/codex_cosmos \
UV_CACHE_DIR=/data0/yurunze/cosmos3/uv-cache \
bash setup/check_local_status.sh
```

## 常用路径

- Cosmos 总入口仓库：`code/cosmos3/upstream`
- Cosmos 可运行框架：`code/cosmos3/framework`
- 本地脚本：`code/cosmos3/setup`
- 推荐 conda 环境：`/data0/yurunze/conda_envs/codex_cosmos`
- 推荐 uv cache：`/data0/yurunze/cosmos3/uv-cache`
- 推荐 ModelScope cache：`/data0/yurunze/models/modelscope-cache`
- 推荐 Nano 权重：`/data0/yurunze/models/Cosmos3-Nano`

## 参考

- `upstream/README.md`
- `framework/docs/setup.md`
- `framework/docs/inference.md`
- ModelScope：`nv-community/Cosmos3-Nano`
