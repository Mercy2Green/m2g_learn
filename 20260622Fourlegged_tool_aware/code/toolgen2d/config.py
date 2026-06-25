"""Configuration constants for toolgen2d environments and optimization."""

from dataclasses import dataclass, field
from typing import Tuple


# Physics constants
PHYSICS_DT: float = 1.0 / 60.0  # physics timestep
PHYSICS_SUBSTEPS: int = 1
GRAVITY: Tuple[float, float] = (0.0, 0.0)  # no gravity, 2D top-down

# World dimensions (pixels)
WORLD_WIDTH: int = 900
WORLD_HEIGHT: int = 600

# Collision types
COLLTYPE_TOOL: int = 1
COLLTYPE_TARGET: int = 2
COLLTYPE_DEBRIS: int = 3
COLLTYPE_OBSTACLE: int = 4
COLLTYPE_BOUNDARY: int = 5

# Rendering colors (R, G, B)
COLOR_BACKGROUND: Tuple[int, int, int] = (240, 240, 245)
COLOR_REACHABLE_ZONE: Tuple[int, int, int] = (200, 230, 200)
COLOR_CONTAINER: Tuple[int, int, int] = (200, 230, 200)
COLOR_OBSTACLE: Tuple[int, int, int] = (140, 140, 140)
COLOR_TARGET: Tuple[int, int, int] = (220, 80, 80)
COLOR_DEBRIS: Tuple[int, int, int] = (200, 160, 60)
COLOR_TOOL: Tuple[int, int, int] = (60, 120, 200)
COLOR_TOOL_OUTLINE: Tuple[int, int, int] = (30, 60, 120)
COLOR_TRAJECTORY: Tuple[int, int, int] = (180, 180, 180)


@dataclass
class TaskConfig:
    """Configuration for a specific task environment."""

    task_name: str
    max_blocks: int
    dx_range: Tuple[float, float] = (15.0, 80.0)
    dy_range: Tuple[float, float] = (-60.0, 60.0)
    length_range: Tuple[float, float] = (20.0, 110.0)
    width_range: Tuple[float, float] = (8.0, 30.0)
    angle_range: Tuple[float, float] = (-1.4, 1.4)

    # Simulation
    sim_steps: int = 360
    render_every: int = 2  # render every N steps when visualizing

    # Reward weights
    reward_progress_weight: float = 0.02
    reward_success_bonus: float = 100.0
    penalty_area_weight: float = 0.002
    penalty_block_count: float = 0.5
    penalty_out_of_bounds: float = 5.0
    # Sweeper-specific
    reward_inside_weight: float = 20.0
    penalty_outside_weight: float = 2.0

    # Continuous chain geometry (blocks are attached end-to-end, not floating)
    continuous_chain: bool = True
    joint_overlap: float = 4.0  # pixels of overlap between consecutive blocks

    # Joint connector circles (fills gaps visually at block joints)
    add_joint_connectors: bool = True
    joint_connector_radius: float = 8.0


# Specific configs
HOOK_CONFIG = TaskConfig(
    task_name="hook",
    max_blocks=5,
    dx_range=(15.0, 80.0),
    dy_range=(-60.0, 60.0),
    length_range=(20.0, 110.0),
    width_range=(8.0, 30.0),
    angle_range=(-1.4, 1.4),
    sim_steps=360,
    reward_progress_weight=0.02,
    reward_success_bonus=100.0,
    penalty_area_weight=0.002,
    penalty_block_count=0.5,
    penalty_out_of_bounds=5.0,
)

SWEEPER_CONFIG = TaskConfig(
    task_name="sweeper",
    max_blocks=7,
    dx_range=(0.0, 70.0),
    dy_range=(-80.0, 80.0),
    length_range=(20.0, 120.0),
    width_range=(8.0, 35.0),
    angle_range=(-1.8, 1.8),
    sim_steps=360,
    reward_inside_weight=20.0,
    penalty_outside_weight=2.0,
    penalty_area_weight=0.0015,
    penalty_block_count=0.3,
)


def get_config(task_name: str) -> TaskConfig:
    """Return the TaskConfig for the given task name."""
    if task_name == "hook":
        return HOOK_CONFIG
    elif task_name == "sweeper":
        return SWEEPER_CONFIG
    else:
        raise ValueError(f"Unknown task: {task_name}. Must be 'hook' or 'sweeper'.")