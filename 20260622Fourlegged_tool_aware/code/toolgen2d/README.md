# toolgen2d

A lightweight 2D tool-generation toy benchmark built with Pymunk.

## Purpose

This is a minimal test of simulated embodiment-extension tool generation. The goal is to test whether functional tool geometry (hook, sweeper) can emerge through simple evolutionary optimization (CEM) before attempting full RL or diffusion-based methods.

**Not** a full GET-USE reproduction — this is a minimal viable closed loop to answer: *Given a scripted tool-use motion, can tool geometry itself be discovered through task reward optimization?*

## Installation

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
cd toolgen2d
uv sync
```

## Training Commands

### CEM Optimization (recommended)

```bash
# Hook task
uv run python -m toolgen2d.train --task hook --optimizer cem --generations 80 --population 64 --seed 0

# Sweeper task
uv run python -m toolgen2d.train --task sweeper --optimizer cem --generations 80 --population 64 --seed 1
```

### Random Search Baseline

```bash
uv run python -m toolgen2d.train --task hook --optimizer random --generations 80 --population 64 --seed 0
```

## Visualization Commands

```bash
uv run python -m toolgen2d.visualize --task hook --checkpoint outputs/hook/seed_0/best.json --gif outputs/hook/seed_0/best_rollout.gif

uv run python -m toolgen2d.visualize --task sweeper --checkpoint outputs/sweeper/seed_1/best.json --gif outputs/sweeper/seed_1/best_rollout.gif
```

For headless (no pygame window):

```bash
uv run python -m toolgen2d.visualize --task hook --checkpoint outputs/hook/seed_0/best.json --gif outputs/hook/seed_0/best_rollout.gif --headless
```

## Smoke Tests

Quick tests to verify the pipeline works:

```bash
# Hook smoke test (3 generations, 8 population)
uv run python -m toolgen2d.train --task hook --generations 3 --population 8 --seed 0

# Visualize hook smoke test
uv run python -m toolgen2d.visualize --task hook --checkpoint outputs/hook/seed_0/best.json --gif outputs/hook/seed_0/smoke.gif --headless

# Sweeper smoke test
uv run python -m toolgen2d.train --task sweeper --generations 3 --population 8 --seed 1
```

## Output Files

After training, results are saved in `outputs/{task}/seed_{seed}/`:

| File | Description |
|------|-------------|
| `best.json` | Best tool parameters (can be loaded for visualization) |
| `best.png` | Static visualization of the best tool geometry |
| `history.csv` | Per-generation optimization metrics |
| `curve_reward.png` | Training reward curves |
| `curve_success.png` | Success rate over generations (hook only) |
| `best_rollout.gif` | Full physics rollout animation (from visualize command) |

## Project Structure

```
toolgen2d/
├── pyproject.toml          # Project configuration
├── README.md               # This file
├── toolgen2d/
│   ├── __init__.py         # Package init
│   ├── config.py           # Physics constants, parameter bounds
│   ├── geometry.py         # Tool geometry decoding and representation
│   ├── physics.py          # Pymunk simulation helpers
│   ├── render.py           # Pygame-based rendering
│   ├── train.py            # Training CLI
│   ├── visualize.py        # Visualization CLI
│   ├── analysis.py         # Post-hoc analysis tools
│   ├── envs/
│   │   ├── __init__.py
│   │   ├── base.py         # Base environment class
│   │   ├── hook_env.py     # Hook task environment
│   │   └── sweeper_env.py  # Sweeper task environment
│   └── optim/
│       ├── __init__.py
│       ├── cem.py          # CEM optimizer
│       └── random_search.py # Random search baseline
└── outputs/                # Training outputs (gitignored)
```

## Known Limitations

- **Kinematic tool body**: The tool is a single rigid body, not articulated joints. This limits the tool to rigid motion along a scripted trajectory.
- **Evolution / CEM, not RL**: The first version uses evolutionary search, not reinforcement learning. This is intentional for rapid prototyping.
- **2D simplified contact**: 2D physics with Pymunk provides simplified contact dynamics.
- **Reward shaping bias**: The reward function can bias discovered geometry. Results should be validated qualitatively.
- **No tool selection from real objects**: The system does not yet learn to select tools based on object affordances — that's a future step.

## Next Steps (Future Work)

1. Replace CEM with PPO or diffusion-based generation
2. Add articulated tool joints
3. Integrate with real object affordance matching
4. Scale to 3D with more complex physics simulators