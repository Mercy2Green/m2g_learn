"""Base environment class for toolgen2d tasks."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Any, Optional

import numpy as np
import pymunk

import pygame

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
        self.tool_shapes: List[pymunk.Poly] = []  # ordered list of tool collision shapes
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
        self.tool_shapes = []

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

        # Add tool body to space first, then shapes (corners are in body-local frame).
        # Preserve creation order in tool_shapes so rendering matches block order.
        self.space.add(self.tool_body)
        self.tool_shapes = []
        for corners in self.current_tool.abs_corners:
            shape = pymunk.Poly(self.tool_body, corners.tolist())
            shape.collision_type = COLLTYPE_TOOL
            shape.friction = 0.5
            shape.elasticity = 0.3
            self.space.add(shape)
            self.tool_shapes.append(shape)

        # Add optional joint connector circles at each block joint.
        # These fill gaps visually and physically at the connection points,
        # making bent tools continuous at joints.
        if self.config.add_joint_connectors and len(self.current_tool.abs_positions) >= 2:
            radius = float(self.config.joint_connector_radius)
            for i in range(len(self.current_tool.abs_positions) - 1):
                cx_i, cy_i = self.current_tool.abs_positions[i]
                a_i = self.current_tool.abs_angles[i]
                len_i = self.current_tool.blocks[i].length
                # Block i's endpoint = center + half-length along angle (in local frame)
                ep_x = cx_i + 0.5 * len_i * np.cos(a_i)
                ep_y = cy_i + 0.5 * len_i * np.sin(a_i)
                # This point is already in local frame of the body (body at (0,0) angle=0).
                # Create a Circle shape at that local position.
                circ = pymunk.Circle(self.tool_body, radius, offset=(float(ep_x), float(ep_y)))
                circ.collision_type = COLLTYPE_TOOL
                circ.friction = 0.5
                circ.elasticity = 0.3
                self.space.add(circ)
                self.tool_shapes.append(circ)

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

    def _get_tool_world_corners(self) -> List[np.ndarray]:
        """Return world-frame corners of the actual Pymunk collision geometry.

        Rendering uses the same geometry that physics uses, eliminating any
        false mismatches caused by vertex ordering or body.shapes iteration order.
        """
        if self.tool_body is None:
            return []

        world_corners: List[np.ndarray] = []
        for shape in self.tool_shapes:
            if not hasattr(shape, "get_vertices"):
                continue

            verts = []
            for v in shape.get_vertices():
                # Use Pymunk's built-in local-to-world transform (handles
                # position + rotation identically to the physics engine).
                w = self.tool_body.local_to_world(v)
                verts.append([float(w.x), float(w.y)])

            arr = np.asarray(verts, dtype=np.float64)
            if arr.ndim == 2 and arr.shape[0] >= 3 and arr.shape[1] == 2:
                world_corners.append(arr)

        return world_corners

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

        # Draw tool ON TOP of trajectory, using the actual Pymunk collision
        # geometry so rendering exactly matches physics.
        world_corners = self._get_tool_world_corners()
        if world_corners:
            self.renderer.draw_tool(world_corners, block_labels=True)

        # Draw joint connector circles (Circle shapes from tool_shapes)
        if self.tool_body is not None:
            for shape in self.tool_shapes:
                if hasattr(shape, "radius") and hasattr(shape, "offset"):
                    # Circle shape on a kinematic body
                    w = self.tool_body.local_to_world(shape.offset)
                    self.renderer.draw_circle(
                        float(w.x), float(w.y),
                        float(shape.radius),
                        color=(60, 120, 200),  # same as tool fill
                    )
                    # Small outline
                    sx = int(float(w.x) * self.renderer.display_scale)
                    sy = int(float(w.y) * self.renderer.display_scale)
                    sr = int(float(shape.radius) * self.renderer.display_scale)
                    pygame.draw.circle(self.renderer.screen, (30, 60, 120), (sx, sy), sr, 2)

        # Draw anchor cross at tool body position
        if self.tool_body is not None:
            ax = float(self.tool_body.position.x)
            ay = float(self.tool_body.position.y)
            self.renderer.draw_cross(ax, ay, size=8, color=(255, 255, 0))

        # Debug overlay: block count, position, angle
        if self.tool_body is not None:
            px = float(self.tool_body.position.x)
            py = float(self.tool_body.position.y)
            pa = float(self.tool_body.angle)
            n_blocks = len(world_corners) if world_corners else 0
            self.renderer.draw_text(
                f"blocks={n_blocks} pos=({px:.1f},{py:.1f}) angle={pa:.2f}",
                10, 30, color=(20, 20, 20),
            )

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