"""Hook task environment.

The goal is to generate a tool that can pull a target object (circle) from the
right side of the screen past an obstacle wall into a reachable zone on the left.
A straight stick should perform poorly; a hook-like geometry should succeed.
"""

from typing import List, Tuple

import numpy as np
import pymunk

from toolgen2d.config import (
    TaskConfig, WORLD_WIDTH, WORLD_HEIGHT,
    COLLTYPE_TARGET, COLLTYPE_OBSTACLE, COLLTYPE_BOUNDARY,
    HOOK_CONFIG,
)
from toolgen2d.envs.base import ToolEnv, RolloutResult
from toolgen2d.geometry import compute_hook_score
from toolgen2d.physics import create_circle, create_rectangle_body, create_boundary_walls


# Scene layout constants (all in pixels)
ANCHOR_START_X = 250.0
ANCHOR_START_Y = 300.0
TARGET_START_X = 620.0
TARGET_START_Y = 300.0
TARGET_RADIUS = 18.0
REACHABLE_ZONE_X = 250.0  # x < this is reachable zone

# Obstacle wall: vertical wall at x=480 with a gap at y=250 to y=350
WALL_X = 480.0
WALL_THICKNESS = 15.0
WALL_TOP_BOTTOM_Y = 175.0  # center of top/bottom wall segments
WALL_TOP_HEIGHT = 250.0  # from y=0 to y=250
WALL_BOTTOM_Y = 425.0  # center of bottom wall segment
WALL_BOTTOM_HEIGHT = 250.0  # from y=350 to y=600

# Trajectory waypoints for the hook task:
# 1. Move forward from start to beyond the target (reach around behind)
# 2. Shift y slightly to catch with hook
# 3. Pull back to the left
HOOK_TRAJECTORY: List[Tuple[float, float, float]] = [
    (250.0, 300.0, 0.0),        # start
    (400.0, 300.0, 0.0),        # move right
    (680.0, 300.0, 0.0),        # past target, past obstacle
    (680.0, 260.0, 0.1),        # shift up slightly to hook
    (220.0, 260.0, 0.0),        # pull back left (with hook engaged)
    (220.0, 300.0, 0.0),        # final position
]


class HookEnv(ToolEnv):
    """Hook task: generate a hook-like tool to pull a target past an obstacle."""

    def __init__(self, config: TaskConfig = HOOK_CONFIG, seed: int = 0,
                 render_mode: str = "none"):
        super().__init__(config, seed, render_mode)
        self.initial_target_pos: Tuple[float, float] = (0.0, 0.0)
        self.initial_dist: float = 0.0

    def _build_scene(self) -> None:
        """Build the Hook task scene."""
        if self.space is None:
            return

        # Boundary walls
        create_boundary_walls(self.space, WORLD_WIDTH, WORLD_HEIGHT)

        # Obstacle wall with gap
        # Top wall segment (y=0 to y=250)
        create_rectangle_body(
            self.space, WALL_X, WALL_TOP_BOTTOM_Y,
            WALL_THICKNESS, WALL_TOP_HEIGHT,
            COLLTYPE_OBSTACLE,
        )
        # Bottom wall segment (y=350 to y=600)
        create_rectangle_body(
            self.space, WALL_X, WALL_BOTTOM_Y,
            WALL_THICKNESS, WALL_BOTTOM_HEIGHT,
            COLLTYPE_OBSTACLE,
        )

        # Target object (dynamic circle)
        target = create_circle(
            self.space, TARGET_START_X, TARGET_START_Y,
            TARGET_RADIUS, COLLTYPE_TARGET, mass=2.0,
        )
        self.target_bodies = [target]
        self.initial_target_pos = (TARGET_START_X, TARGET_START_Y)
        self.initial_dist = TARGET_START_X - REACHABLE_ZONE_X

    def _get_tool_trajectory(self) -> List[Tuple[float, float, float]]:
        return HOOK_TRAJECTORY

    def _compute_result(self) -> RolloutResult:
        """Compute reward and metrics after rollout."""
        result = RolloutResult()

        if not self.target_bodies:
            return result

        target = self.target_bodies[0]
        final_x = target.position.x
        final_y = target.position.y
        initial_x = self.initial_target_pos[0]

        # Displacement toward robot (positive = moved left)
        displacement = initial_x - final_x

        # Success: target is within reachable zone
        success = final_x < REACHABLE_ZONE_X and 180 < final_y < 420

        # Out of bounds check
        out_of_bounds = (final_x < -50 or final_x > WORLD_WIDTH + 50 or
                         final_y < -50 or final_y > WORLD_HEIGHT + 50)

        # Progress toward reachable zone
        final_dist = max(0.0, final_x - REACHABLE_ZONE_X)
        progress = self.initial_dist - final_dist

        # Hook score (heuristic measure of hook-like shape)
        hook_score = compute_hook_score(self.current_tool) if self.current_tool else 0.0

        # Compute reward
        # Reward structure:
        # - Progress toward robot (higher is better)
        # - Big bonus for success
        # - Penalties for large area, many blocks, out of bounds
        reward = (self.config.reward_progress_weight * progress
                  + self.config.reward_success_bonus * (1.0 if success else 0.0)
                  - self.config.penalty_area_weight * self.current_tool.total_area
                  - self.config.penalty_block_count * self.config.max_blocks)

        if out_of_bounds:
            reward -= self.config.penalty_out_of_bounds

        result.reward = reward
        result.final_target_x = final_x
        result.target_displacement = displacement
        result.success = success
        result.out_of_bounds = out_of_bounds
        result.total_area = self.current_tool.total_area
        result.num_blocks = self.config.max_blocks
        result.hook_score = hook_score

        return result

    def _draw_scene(self) -> None:
        """Draw Hook-specific scene elements."""
        if self.renderer is None:
            return

        # Reachable zone (left side, x < 250, full height)
        self.renderer.draw_reachable_zone(0, 0, REACHABLE_ZONE_X, WORLD_HEIGHT)

        # Obstacle wall (two wall segments with gap)
        # Top wall
        wall_top_y = WALL_TOP_BOTTOM_Y - WALL_TOP_HEIGHT / 2
        self.renderer.draw_obstacle(
            WALL_X - WALL_THICKNESS / 2, wall_top_y,
            WALL_THICKNESS, WALL_TOP_HEIGHT,
        )
        # Bottom wall
        wall_bot_y = WALL_BOTTOM_Y - WALL_BOTTOM_HEIGHT / 2
        self.renderer.draw_obstacle(
            WALL_X - WALL_THICKNESS / 2, wall_bot_y,
            WALL_THICKNESS, WALL_BOTTOM_HEIGHT,
        )

        # Target
        if self.target_bodies:
            t = self.target_bodies[0]
            self.renderer.draw_circle(t.position.x, t.position.y, TARGET_RADIUS,
                                      (220, 80, 80))