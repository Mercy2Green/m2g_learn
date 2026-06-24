"""Sweeper task environment.

The goal is to generate a tool that can sweep debris particles (small circles)
from a scattered region into a container zone on the right side of the screen.
A wide or slightly concave sweeper geometry should outperform a narrow stick.
"""

from typing import List, Tuple

import numpy as np
import pymunk

from toolgen2d.config import (
    TaskConfig, WORLD_WIDTH, WORLD_HEIGHT,
    COLLTYPE_DEBRIS, COLLTYPE_OBSTACLE, COLLTYPE_BOUNDARY,
    SWEEPER_CONFIG, COLOR_DEBRIS,
)
from toolgen2d.envs.base import ToolEnv, RolloutResult
from toolgen2d.geometry import compute_sweeper_width_score
from toolgen2d.physics import create_circle, create_boundary_walls


# Scene layout constants
NUM_DEBRIS = 12
DEBRIS_RADIUS = 8.0
DEBRIS_MASS = 0.5
CONTAINER_X = 700.0
CONTAINER_Y = 230.0
CONTAINER_WIDTH = 150.0
CONTAINER_HEIGHT = 140.0

# Start sweep position
SWEEP_START_X = 300.0
SWEEP_START_Y = 300.0

# Trajectory for sweeper: sweep left to right with slight up/down motion
SWEEPER_TRAJECTORY: List[Tuple[float, float, float]] = [
    (300.0, 300.0, 0.0),        # start
    (400.0, 290.0, 0.0),        # begin sweep
    (500.0, 310.0, 0.0),        # sweep with slight motion
    (600.0, 290.0, 0.0),
    (730.0, 300.0, 0.0),        # reach container
    (730.0, 300.0, 0.0),        # hold position
]


class SweeperEnv(ToolEnv):
    """Sweeper task: generate a wide tool to sweep debris into a container."""

    def __init__(self, config: TaskConfig = SWEEPER_CONFIG, seed: int = 0,
                 render_mode: str = "none"):
        super().__init__(config, seed, render_mode)
        self.initial_debris_positions: List[Tuple[float, float]] = []

    def _build_scene(self) -> None:
        """Build the Sweeper task scene."""
        if self.space is None:
            return

        # Boundary walls
        create_boundary_walls(self.space, WORLD_WIDTH, WORLD_HEIGHT)

        # Debris particles scattered around the sweep region
        self.debris_bodies = []
        self.initial_debris_positions = []
        for _ in range(NUM_DEBRIS):
            x = self.rng.uniform(450, 650)
            y = self.rng.uniform(240, 360)
            body = create_circle(
                self.space, x, y, DEBRIS_RADIUS,
                COLLTYPE_DEBRIS, mass=DEBRIS_MASS,
            )
            self.debris_bodies.append(body)
            self.initial_debris_positions.append((x, y))

    def _get_tool_trajectory(self) -> List[Tuple[float, float, float]]:
        return SWEEPER_TRAJECTORY

    def _compute_result(self) -> RolloutResult:
        """Compute reward and metrics after rollout."""
        result = RolloutResult()

        # Count debris inside/outside container
        inside_count = 0
        total_x_displacement = 0.0

        for i, body in enumerate(self.debris_bodies):
            x, y = body.position.x, body.position.y
            in_container = (CONTAINER_X <= x <= CONTAINER_X + CONTAINER_WIDTH and
                            CONTAINER_Y <= y <= CONTAINER_Y + CONTAINER_HEIGHT)
            if in_container:
                inside_count += 1
            initial_x = self.initial_debris_positions[i][0] if i < len(self.initial_debris_positions) else x
            total_x_displacement += x - initial_x

        outside_count = NUM_DEBRIS - inside_count

        # Sweeper width score (heuristic measure of sweeping ability)
        width_score = compute_sweeper_width_score(self.current_tool) if self.current_tool else 0.0

        # Compute reward
        # Reward structure:
        # - Reward for debris inside container
        # - Penalty for debris outside container
        # - Penalties for large area and many blocks
        reward = (self.config.reward_inside_weight * inside_count
                  - self.config.penalty_outside_weight * outside_count
                  - self.config.penalty_area_weight * self.current_tool.total_area
                  - self.config.penalty_block_count * self.config.max_blocks)

        result.reward = reward
        result.inside_count = inside_count
        result.outside_count = outside_count
        result.total_area = self.current_tool.total_area
        result.num_blocks = self.config.max_blocks
        result.sweeper_width_score = width_score

        return result

    def _draw_scene(self) -> None:
        """Draw Sweeper-specific scene elements."""
        if self.renderer is None:
            return

        # Container region (right side)
        self.renderer.draw_container(
            CONTAINER_X, CONTAINER_Y,
            CONTAINER_WIDTH, CONTAINER_HEIGHT,
        )

        # Debris particles
        for body in self.debris_bodies:
            self.renderer.draw_circle(
                body.position.x, body.position.y,
                DEBRIS_RADIUS, COLOR_DEBRIS,
            )