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

根分区当前空间较紧，建议把 conda 环境、uv cache、HF cache、权重都放到 `/data0/yurunze/cosmos3/` 或其它大盘。

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
bash setup/run_t2i_smoke.sh
```

默认输出目录：

```text
code/cosmos3/framework/outputs/codex_t2i_nano_smoke
```

脚本使用 `framework/inputs/omni/t2i.json`，并加了 `--no-guardrails`，避免 smoke test 额外拉 guardrail 模型。

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
