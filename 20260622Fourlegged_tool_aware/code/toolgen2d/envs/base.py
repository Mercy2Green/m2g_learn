"""Base environment class for toolgen2d tasks."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Any, Optional

import numpy as np
import pymunk

from toolgen2d.config import (
    TaskConfig, WORLD_WIDTH, WORLD_HEIGHT,
    PHYSICS_DT, COLLTYPE_TOOL, COLLTYPE_TARGET,
    COLLTYPE_DEBRIS, COLLTYPE_OBSTACLE,
)
from toolgen2d.geometry import ToolGeometry, decode_tool
from toolgen2d.render import Renderer


@dataclass
class RolloutResult:
    """Result of a single environment rollout with a given tool."""

    reward: float = 0.0
    # Task-specific metrics
    final_target_x: float = 0.0
    target_displacement: float = 0.0
    success: bool = False
    inside_count: int = 0
    outside_count: int = 0
    # Penalty components
    total_area: float = 0.0
    num_blocks: int = 0
    out_of_bounds: bool = False
    # Auxiliary metrics
    hook_score: float = 0.0
    sweeper_width_score: float = 0.0
    # Full state for replay
    frames: List[np.ndarray] = field(default_factory=list)


class ToolEnv(ABC):
    """Abstract base class for tool-generation environments.

    Each environment defines:
    - Scene layout (objects, obstacles, boundaries)
    - Scripted tool trajectory
    - Reward function
    - Visualization
    """

    def __init__(self, config: TaskConfig, seed: int = 0, render_mode: str = "none"):
        """Initialize the environment.

        Args:
            config: TaskConfig with task-specific parameters.
            seed: Random seed for deterministic simulation.
            render_mode: "none", "human", or "gif".
        """
        self.config = config
        self.seed = seed
        self.rng = np.random.RandomState(seed)
        self.render_mode = render_mode
        self.renderer: Optional[Renderer] = None

        # Physics space
        self.space: Optional[pymunk.Space] = None
        self.tool_body: Optional[pymunk.Body] = None
        self.target_bodies: List[pymunk.Body] = []
        self.debris_bodies: List[pymunk.Body] = []
        self.obstacle_bodies: List[pymunk.Body] = []
        self.wall_bodies: List[pymunk.Body] = []
        self.all_bodies: List[pymunk.Body] = []

        # Trajectory
        self.trajectory_points: List[Tuple[float, float]] = []

        # Tool state
        self.current_tool: Optional[ToolGeometry] = None

        # Logging
        self.log: Dict[str, Any] = {}

    @abstractmethod
    def _build_scene(self) -> None:
        """Build the static scene: boundaries, obstacles, targets/debris."""
        ...

    @abstractmethod
    def _get_tool_trajectory(self) -> List[Tuple[float, float, float]]:
        """Return the scripted tool trajectory as (x, y, angle) waypoints.

        The trajectory defines the tool anchor's position and orientation over time.
        """
        ...

    def _create_physics_space(self) -> pymunk.Space:
        """Create a fresh Pymunk space for a new simulation."""
        space = pymunk.Space()
        space.gravity = (0, 0)  # no gravity, top-down view
        space.collision_slop = 0.1
        return space

    def reset(self, params: np.ndarray) -> None:
        """Reset the environment with a new tool parameter vector.

        Args:
            params: Flat parameter vector for tool geometry.
        """
        # Decode tool
        self.current_tool = decode_tool(params, self.config)

        # Create fresh physics space
        self.space = self._create_physics_space()
        self.target_bodies = []
        self.debris_bodies = []
        self.obstacle_bodies = []
        self.wall_bodies = []
        self.all_bodies = []
        self.trajectory_points = []

        # Build the scene
        self._build_scene()

    def _interpolate_trajectory(self, t: float, trajectory: List[Tuple[float, float, float]]
                                ) -> Tuple[float, float, float]:
        """Interpolate the trajectory at time t [0, 1]."""
        n = len(trajectory)
        if n < 2:
            return trajectory[0] if n == 1 else (0.0, 0.0, 0.0)
        idx = t * (n - 1)
        i = int(idx)
        frac = idx - i
        i = min(i, n - 2)

        x = trajectory[i][0] + frac * (trajectory[i + 1][0] - trajectory[i][0])
        y = trajectory[i][1] + frac * (trajectory[i + 1][1] - trajectory[i][1])
        a = trajectory[i][2] + frac * (trajectory[i + 1][2] - trajectory[i][2])
        return x, y, a

    def run_rollout(self, params: np.ndarray, render: bool = False,
                    gif_frames: bool = False) -> RolloutResult:
        """Run a full rollout for a given tool parameter vector.

        Args:
            params: Tool parameter vector.
            render: Whether to render interactively.
            gif_frames: Whether to save frame data for GIF export.

        Returns:
            RolloutResult with reward and metrics.
        """
        # Reset environment with new tool
        self.reset(params)
        if self.current_tool is None:
            return RolloutResult()

        # Compute tool trajectory
        trajectory = self._get_tool_trajectory()
        sim_steps = self.config.sim_steps
        dt = PHYSICS_DT

        # Create tool body (kinematic) at the anchor origin.
        # Tool corners from decode_tool are computed assuming anchor at (0,0)
        # with angle=0. The body starts at (0,0) and will be moved along the
        # trajectory during simulation.
        self.tool_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.tool_body.position = (0.0, 0.0)
        self.tool_body.angle = 0.0

        # Add tool body to space first, then shapes (corners are in body-local frame)
        self.space.add(self.tool_body)
        for corners in self.current_tool.abs_corners:
            shape = pymunk.Poly(self.tool_body, corners.tolist())
            shape.collision_type = COLLTYPE_TOOL
            shape.friction = 0.5
            shape.elasticity = 0.3
            self.space.add(shape)

        # Set the body to the initial trajectory position for rendering
        start_x, start_y, start_angle = trajectory[0]
        self.tool_body.position = (start_x, start_y)
        self.tool_body.angle = start_angle

        self.all_bodies.append(self.tool_body)

        # Initialize renderer if needed
        if render or gif_frames:
            if self.renderer is None:
                headless = not render
                self.renderer = Renderer(headless=headless)
                self.renderer.initialize()
            self.renderer.clear()

        # Render initial frame
        frames = []
        if gif_frames:
            self._render_frame(0, sim_steps)
            frames.append(self.renderer.get_frame())
            if render:
                self.renderer.flip()

        # Run simulation
        t = 0.0
        dt_traj = 1.0 / sim_steps
        for step in range(sim_steps):
            # Update tool position along trajectory
            t = (step + 1) / sim_steps
            tx, ty, ta = self._interpolate_trajectory(t, trajectory)
            self.tool_body.position = (tx, ty)
            self.tool_body.angle = ta
            self.tool_body.velocity = (0, 0)
            self.tool_body.angular_velocity = 0.0

            # Step physics
            self.space.step(dt)

            # Record trajectory
            self.trajectory_points.append((tx, ty))

            # Render
            if (render or gif_frames) and (step % max(1, self.config.render_every) == 0):
                self._render_frame(step + 1, sim_steps)
                if gif_frames:
                    frames.append(self.renderer.get_frame())
                if render:
                    self.renderer.flip()
                    if not self.renderer.handle_events():
                        break

        # Compute result
        result = self._compute_result()
        result.num_blocks = self.config.max_blocks
        result.total_area = self.current_tool.total_area
        result.frames = frames

        return result

    def _render_frame(self, step: int, total_steps: int) -> None:
        """Render the current state to the renderer."""
        if self.renderer is None or self.current_tool is None:
            return
        self.renderer.clear()

        # Draw boundaries and scene elements
        self._draw_scene()

        # Draw trajectory FIRST (so tool draws on top)
        if self.trajectory_points:
            self.renderer.draw_trajectory(self.trajectory_points)

        # Draw tool ON TOP of trajectory
        if self.current_tool:
            if self.tool_body:
                bx, by = self.tool_body.position
                shifted = [
                    np.array([c[0] + bx, c[1] + by]) for c in self.current_tool.abs_corners
                ]
                self.renderer.draw_tool(shifted, block_labels=True)

        # Draw info text
        self.renderer.draw_title(f"{self.config.task_name.upper()} | Step {step}/{total_steps}")

    def _draw_scene(self) -> None:
        """Draw the static scene elements."""
        pass  # Override in subclasses

    @abstractmethod
    def _compute_result(self) -> RolloutResult:
        """Compute and return the RolloutResult after simulation."""
        ...

    def close(self) -> None:
        """Close the environment and renderer."""
        if self.renderer is not None:
            self.renderer.close()
            self.renderer = None