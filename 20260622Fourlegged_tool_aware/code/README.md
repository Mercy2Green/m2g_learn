# toolgen2d

> 2D 工具形态演化小实验 —— 在 MacBook Air 上验证：**给定一个脚本化的工具使用动作（钩、扫），工具几何形状能否通过任务奖励搜索（CEM 进化优化）自发涌现出功能形态（hook / sweeper）？**

## 科学问题

这个项目在验证一个最小命题：

> **给定 scripted tool-use motion，工具几何本身是否能通过 task reward 被搜索出功能形态？**

它不是 GET-USE 的完整复现，而是先跑通最小可验证闭环。如果 CEM 能很快搜出 hook / sweeper 形态，才值得下一步上 RL、diffusion、真实物体匹配。

## 环境

| 任务 | 目标 | 期望发现的形态 |
|------|------|---------------|
| **Hook** (钩) | 工具绕过障碍墙，将目标圆盘拉回左侧可达区 | 钩状末端偏移（lateral protrusion） |
| **Sweeper** (扫) | 工具从右向左扫，将散落碎片推入右侧容器 | 宽形或微凹的扫帚状（wide / concave） |

## 快速开始（Smoke Test）

```bash
cd code
uv sync

# Hook 任务快速测试（3代，8个候选）
uv run python -m toolgen2d.train --task hook --generations 3 --population 8 --seed 0

# 可视化结果
uv run python -m toolgen2d.visualize \
    --task hook \
    --checkpoint outputs/hook/seed_0/best.json \
    --gif outputs/hook/seed_0/smoke.gif --headless

# Sweeper 任务快速测试
uv run python -m toolgen2d.train --task sweeper --generations 3 --population 8 --seed 1
```

## 完整训练

### Hook 任务

```bash
uv run python -m toolgen2d.train \
    --task hook \
    --optimizer cem \
    --generations 80 \
    --population 64 \
    --seed 0
```

### Sweeper 任务

```bash
uv run python -m toolgen2d.train \
    --task sweeper \
    --optimizer cem \
    --generations 80 \
    --population 64 \
    --seed 1
```

### 随机搜索基线

```bash
uv run python -m toolgen2d.train \
    --task hook \
    --optimizer random \
    --generations 80 \
    --population 64 \
    --seed 0
```

### 训练参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--task` | `hook` | `hook` 或 `sweeper` |
| `--optimizer` | `cem` | `cem` (进化) 或 `random` (随机搜索) |
| `--generations` | `80` | 进化代数 |
| `--population` | `64` | 每代候选数 |
| `--elite-frac` | `0.2` | CEM 精英比例 |
| `--eval-seeds` | `2` | 每个候选评估的随机种子数 |
| `--seed` | `0` | 全局随机种子 |
| `--render-every` | `0` | 每 N 代自动弹出 pygame 窗口播放最佳工具运动（0=不开启） |
| `--render-final` | 无 | 加上此标志，训练结束后弹窗展示最终最佳工具 rollout |
| `--save-gif` | 无 | 加上此标志，训练结束后自动保存最终最佳工具的运动 GIF 到输出目录 |
| `--save-interval` | `0` | 每 N 代保存一次中间过程的 rollout GIF 到 `rollouts/` 子文件夹（0=不开启） |
| `--output-dir` | 自动 | 输出目录（默认 `outputs/{task}/seed_{seed}/`） |

## 实时可视化

训练过程中可以直接观看工具的运动模拟，无需等待训练结束再单独执行 visualize。

### 训练中实时观看（`--render-every`）

加上 `--render-every N`，每 N 代自动弹出 pygame 窗口，播放当前最佳工具的 rollout 动画。

```bash
# 每 10 代看一次当前最佳工具的表现
uv run python -m toolgen2d.train \
    --task hook --generations 80 --population 64 --seed 0 \
    --render-every 10
```

```bash
# 每 10 代看一次当前最佳工具的表现
uv run python -m toolgen2d.train \
    --task sweeper --generations 80 --population 64 --seed 0 \
    --render-every 10
```

运行后会看到：
1. 终端打印优化进度
2. 每 10 代自动弹出 pygame 窗口
3. 窗口中动画展示工具沿轨迹运动、与目标/障碍物碰撞的全过程
4. **关闭 pygame 窗口后**，训练继续到下一代

### 训练后查看最终效果（`--render-final`）

```bash
uv run python -m toolgen2d.train \
    --task hook --generations 80 --population 64 --seed 0 \
    --render-final
```

### 组合使用

```bash
uv run python -m toolgen2d.train \
    --task hook --generations 80 --population 64 --seed 0 \
    --render-every 10 --render-final
```

### 自动保存 GIF（`--save-gif`）

训练结束时自动将最终最佳工具的运动动画保存为 GIF，无需单独执行 visualize 命令：

```bash
uv run python -m toolgen2d.train \
    --task hook --generations 80 --population 64 --seed 0 \
    --save-gif
```

GIF 保存到 `outputs/hook/seed_0/best_rollout.gif`。

### 保存中间过程的 GIF（`--save-interval`）

每 N 代自动保存当前最佳工具的 rollout GIF 到 `rollouts/` 子文件夹（headless，不弹窗）。适合事后回顾工具的形态演化过程。

```bash
# 每 10 代保存一次 GIF，输出到 outputs/hook/seed_0/rollouts/
uv run python -m toolgen2d.train \
    --task hook --generations 200 --population 64 --seed 0 \
    --save-interval 10
```

```bash
# 每 10 代保存一次 GIF，输出到 outputs/hook/seed_0/rollouts/
uv run python -m toolgen2d.train \
    --task sweeper --generations 80 --population 64 --seed 0 \
    --save-interval 10
```

生成的文件：`outputs/hook/seed_0/rollouts/gen_0000.gif`, `gen_0010.gif`, `gen_0020.gif`, ...

## 离线可视化

训练结束后，也可以单独用 visualize 命令回放最佳工具的 rollout。

### 导出 GIF 动画

```bash
# Hook 最佳工具的运动回放
uv run python -m toolgen2d.visualize \
    --task hook \
    --checkpoint outputs/hook/seed_0/best.json \
    --gif outputs/hook/seed_0/best_rollout.gif

# Sweeper 最佳工具的运动回放
uv run python -m toolgen2d.visualize \
    --task sweeper \
    --checkpoint outputs/sweeper/seed_0/best.json \
    --gif outputs/sweeper/seed_0/best_rollout.gif
```

### 无窗口模式（服务器 / headless）

```bash
uv run python -m toolgen2d.visualize \
    --task hook \
    --checkpoint outputs/hook/seed_0/best.json \
    --gif outputs/hook/seed_0/best_rollout.gif --headless
```

### 可视化参数说明

| 参数 | 说明 |
|------|------|
| `--task` | 任务类型（`hook` / `sweeper`） |
| `--checkpoint` | 必填。`best.json` 文件路径 |
| `--gif` | 导出 GIF 动画路径 |
| `--png` | 导出最后帧 PNG 路径 |
| `--headless` | 不打开 pygame 窗口（仅生成文件） |
| `--seed` | 回放用的随机种子 |

## 输出文件

训练完成后，结果保存于 `outputs/{task}/seed_{seed}/`：

| 文件 | 说明 |
|------|------|
| `best.json` | 最佳工具参数（含所有 block 的 dx/dy/length/width/angle） |
| `best.png` | 最佳工具几何静态可视化 |
| `history.csv` | 每代训练指标（best_reward, mean_reward, elite_mean_reward 等） |
| `curve_reward.png` | 奖励曲线（best / mean / elite mean） |
| `curve_success.png` | 成功率曲线（仅 Hook 任务） |
| `*.gif` | 运动回放动画（通过 visualize 命令生成） |

### best.json 结构

```json
{
  "task": "hook",
  "params": [dx1, dy1, len1, wid1, ang1, dx2, ...],
  "total_area": 3553.0,
  "blocks": [
    {"dx": 40.0, "dy": 5.0, "length": 80.0, "width": 15.0, "angle": 0.3},
    ...
  ]
}
```

## 项目结构

```
code/
├── pyproject.toml              # uv 项目配置，依赖管理
├── README.md                   # 本文档
├── toolgen2d/                  # 核心代码
│   ├── __init__.py
│   ├── config.py               # 物理常数、参数范围、奖励权重
│   ├── geometry.py             # 工具几何解码（参数 → 矩形块链）
│   ├── physics.py              # Pymunk 物理辅助函数
│   ├── render.py               # pygame 渲染引擎
│   ├── train.py                # 训练 CLI 入口
│   ├── visualize.py            # 可视化 CLI 入口
│   ├── analysis.py             # 事后分析工具
│   ├── envs/
│   │   ├── base.py             # 环境基类（Scene / Trajectory / Reward）
│   │   ├── hook_env.py         # Hook 任务场景
│   │   └── sweeper_env.py      # Sweeper 任务场景
│   └── optim/
│       ├── cem.py              # 交叉熵方法进化优化器
│       └── random_search.py    # 随机搜索基线
└── outputs/                    # 训练输出（gitignore）
```

## 核心概念

### 工具几何表示

工具由 N 个矩形块顺序连接而成。每个块的参数：

```
[dx, dy, length, width, angle]
```

- `dx, dy`: 相对前一块终点的偏移（前一块朝向坐标系）
- `length, width`: 矩形尺寸
- `angle`: 相对前一块朝向的旋转角

所有块在仿真中属于**同一个刚体**（kinematic body），沿脚本化轨迹运动。

### 物理引擎

- **Pymunk** 轻量 2D 刚体物理
- **无重力**（俯视视角）
- 工具为 **kinematic**（运动学驱动），不与物理积分耦合
- 目标/碎片为 **dynamic**（受碰撞影响）

### CEM 优化流程

1. 从高斯分布 `N(mean, std)` 采样候选参数
2. 每个候选使用多个随机种子评估（防过拟合）
3. 选择 top `elite_frac` 的精英
4. 用精英更新 `mean` 和 `std`（EMA 平滑）
5. 重复直到达到设定代数

## 已知局限

- **刚性工具**：工具是单一刚体，不是铰接链。沿脚本化轨迹运动。
- **CEM 不是 RL**：第一版只用进化搜索，后续可替换为 PPO / diffusion。
- **2D 简化接触**：Pymunk 提供简化 2D 碰撞动力学。
- **奖励塑造偏差**：奖励函数设计会影响发现的几何形态，需要定性验证。
- **尚未学习工具选择**：系统目前不基于真实物体 affordance 选择工具。

## 未来工作

1. 用 PPO 或 diffusion 替代 CEM
2. 添加铰接工具关节
3. 集成真实物体 affordance 匹配
4. 扩展到 3D（Isaac Sim / MuJoCo）
5. 机器人平台验证（Go2 + Piper arm）

## 依赖

- Python 3.10–3.12
- pymunk, pygame, numpy, matplotlib, imageio, tqdm, rich, pydantic

所有依赖通过 `uv sync` 自动安装。