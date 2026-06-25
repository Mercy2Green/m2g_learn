"""Tool geometry generation and representation.

A generated tool is a sequence of N rectangular blocks connected as a kinematic
chain. Each block is defined by parameters [dx, dy, length, width, angle] that
describe its position relative to the previous block.
"""

from dataclasses import dataclass, field
from typing import List, Tuple

import numpy as np

from toolgen2d.config import TaskConfig


@dataclass
class BlockParams:
    """Parameters for a single rectangular block in the tool chain."""

    dx: float  # relative x offset from previous block endpoint
    dy: float  # relative y offset from previous block endpoint
    length: float  # rectangle length (along the block's local x-axis)
    width: float  # rectangle width (along the block's local y-axis)
    angle: float  # relative angle from previous block orientation (radians)


@dataclass
class ToolGeometry:
    """Complete geometry of a generated tool.

    Stores the absolute positions and orientations of each block in the world
    frame, along with the raw parameters.
    """

    blocks: List[BlockParams]
    # Absolute geometry in world frame (computed during decoding)
    abs_positions: List[Tuple[float, float]] = field(default_factory=list)
    abs_angles: List[float] = field(default_factory=list)
    # Rectangle corners for each block in world frame
    abs_corners: List[np.ndarray] = field(default_factory=list)
    # Total bounding box
    total_area: float = 0.0


def param_bounds_array(config: TaskConfig) -> Tuple[np.ndarray, np.ndarray]:
    """Return (lower, upper) arrays of shape (max_blocks * 5,)."""
    lower = []
    upper = []
    for _ in range(config.max_blocks):
        lower.extend([config.dx_range[0], config.dy_range[0],
                      config.length_range[0], config.width_range[0],
                      config.angle_range[0]])
        upper.extend([config.dx_range[1], config.dy_range[1],
                      config.length_range[1], config.width_range[1],
                      config.angle_range[1]])
    return np.array(lower, dtype=np.float64), np.array(upper, dtype=np.float64)


def decode_tool(params: np.ndarray, config: TaskConfig) -> ToolGeometry:
    """Decode a flat parameter vector into a ToolGeometry.

    Args:
        params: Flat array of shape (max_blocks * 5,). Values should be within
                the parameter bounds defined in config.
        config: TaskConfig with max_blocks and parameter ranges.

    Returns:
        ToolGeometry with computed absolute positions, angles, and corners.
    """
    n = config.max_blocks
    blocks = []
    abs_positions: List[Tuple[float, float]] = []
    abs_angles: List[float] = []
    abs_corners: List[np.ndarray] = []

    # The tool starts at the origin (0, 0) — the anchor/gripper position.
    # In the environment, this anchor is placed at the task-specific start location.
    prev_x, prev_y = 0.0, 0.0
    prev_angle = 0.0

    # Compute the endpoint of the previous block for the next attachment.
    # We maintain cumulative position and angle.
    cum_x, cum_y = 0.0, 0.0
    cum_angle = 0.0

    total_area = 0.0

    for i in range(n):
        dx = float(params[i * 5 + 0])
        dy = float(params[i * 5 + 1])
        length = float(params[i * 5 + 2])
        width = float(params[i * 5 + 3])
        angle = float(params[i * 5 + 4])

        block = BlockParams(dx=dx, dy=dy, length=length, width=width, angle=angle)
        blocks.append(block)

        # Update cumulative angle (relative to previous block orientation)
        cum_angle += angle

        cos_a = np.cos(cum_angle)
        sin_a = np.sin(cum_angle)

        if config.continuous_chain:
            # In continuous_chain mode, dx/dy are intentionally ignored to enforce
            # physical connectivity. The current block starts at (or slightly before)
            # the previous block's endpoint, with a small overlap for visual continuity.
            # We keep dx/dy in the parameter vector for backward compatibility with
            # existing checkpoints and optimizer dimensionality.
            overlap = float(getattr(config, "joint_overlap", 4.0))
            start_x = prev_x - overlap * cos_a
            start_y = prev_y - overlap * sin_a
            center_x = start_x + (length / 2.0) * cos_a
            center_y = start_y + (length / 2.0) * sin_a
        else:
            # Legacy mode: use dx/dy offsets from previous endpoint
            # Attachment point = previous block's endpoint
            attach_x, attach_y = prev_x, prev_y

            # dx, dy are in the LOCAL frame of the previous block's orientation
            local_dx_world = dx * np.cos(prev_angle) - dy * np.sin(prev_angle)
            local_dy_world = dx * np.sin(prev_angle) + dy * np.cos(prev_angle)

            center_x = attach_x + local_dx_world + (length / 2.0) * cos_a
            center_y = attach_y + local_dy_world + (length / 2.0) * sin_a

        abs_positions.append((center_x, center_y))
        abs_angles.append(cum_angle)

        # Compute rectangle corners in world frame
        hw = length / 2.0
        hh = width / 2.0
        # Local corners (before rotation)
        local_corners = np.array([
            [-hw, -hh],
            [hw, -hh],
            [hw, hh],
            [-hw, hh],
        ], dtype=np.float64)
        # Rotate by cum_angle
        rot = np.array([[cos_a, -sin_a], [sin_a, cos_a]])
        world_corners = local_corners @ rot.T + np.array([center_x, center_y])
        abs_corners.append(world_corners)

        # Update previous endpoint for next block
        # The endpoint of this block = center + half-length along orientation
        end_x = center_x + (length / 2.0) * cos_a
        end_y = center_y + (length / 2.0) * sin_a
        prev_x, prev_y = end_x, end_y
        prev_angle = cum_angle

        total_area += length * width

    return ToolGeometry(
        blocks=blocks,
        abs_positions=abs_positions,
        abs_angles=abs_angles,
        abs_corners=abs_corners,
        total_area=total_area,
    )


def compute_hook_score(tool: ToolGeometry) -> float:
    """Compute a heuristic 'hook score' for a tool.

    Measures how much the last block deviates laterally from the tool's
    overall direction. Higher values suggest a hook-like shape.
    """
    if len(tool.abs_positions) < 2:
        return 0.0

    # Overall direction from first block center to last block end
    last_end = tool.abs_positions[-1]
    first_center = tool.abs_positions[0]
    main_dir = np.array([last_end[0] - first_center[0], last_end[1] - first_center[1]])
    main_len = np.linalg.norm(main_dir)
    if main_len < 1e-6:
        return 0.0
    main_dir = main_dir / main_len

    # Perpendicular direction
    perp_dir = np.array([-main_dir[1], main_dir[0]])

    # Compute lateral deviation of each block center relative to the main line
    max_lateral = 0.0
    for pos in tool.abs_positions:
        vec = np.array([pos[0] - first_center[0], pos[1] - first_center[1]])
        lateral = abs(np.dot(vec, perp_dir))
        max_lateral = max(max_lateral, lateral)

    return max_lateral


def compute_sweeper_width_score(tool: ToolGeometry) -> float:
    """Compute a heuristic 'sweeper width' score.

    Measures the total width span (max y - min y) of the tool's block centers,
    which correlates with sweeping ability.
    """
    if len(tool.abs_positions) < 2:
        return 0.0
    ys = [p[1] for p in tool.abs_positions]
    return max(ys) - min(ys)


def compute_connection_gaps(tool: ToolGeometry) -> List[float]:
    """Estimate the gap (distance) between consecutive block endpoints.

    For each pair (i, i+1), computes the distance from block i's endpoint
    to block i+1's start point. In a perfectly continuous chain with overlap,
    this should be close to the configured joint_overlap value.

    Returns a list of gaps of length (n_blocks - 1), or empty if < 2 blocks.
    """
    gaps: List[float] = []
    n = len(tool.abs_positions)
    if n < 2:
        return gaps

    for i in range(n - 1):
        # Block i: center + half-length along its angle
        cx_i, cy_i = tool.abs_positions[i]
        a_i = tool.abs_angles[i]
        len_i = tool.blocks[i].length
        end_i_x = cx_i + 0.5 * len_i * np.cos(a_i)
        end_i_y = cy_i + 0.5 * len_i * np.sin(a_i)

        # Block i+1: center - half-length along its angle
        cx_j, cy_j = tool.abs_positions[i + 1]
        a_j = tool.abs_angles[i + 1]
        len_j = tool.blocks[i + 1].length
        start_j_x = cx_j - 0.5 * len_j * np.cos(a_j)
        start_j_y = cy_j - 0.5 * len_j * np.sin(a_j)

        gap = np.sqrt((end_i_x - start_j_x) ** 2 + (end_i_y - start_j_y) ** 2)
        gaps.append(float(gap))

    return gaps


def compute_self_overlap_penalty(tool: ToolGeometry) -> float:
    """Approximate penalty for blocks that overlap each other.

    Uses pairwise rectangle overlap estimation via axis-aligned bounding box
    intersection. This is a rough approximation.
    """
    penalty = 0.0
    for i, corners_i in enumerate(tool.abs_corners):
        for j in range(i + 1, len(tool.abs_corners)):
            corners_j = tool.abs_corners[j]
            # AABB overlap ratio
            xi_min, xi_max = float(np.min(corners_i[:, 0])), float(np.max(corners_i[:, 0]))
            yi_min, yi_max = float(np.min(corners_i[:, 1])), float(np.max(corners_i[:, 1]))
            xj_min, xj_max = float(np.min(corners_j[:, 0])), float(np.max(corners_j[:, 0]))
            yj_min, yj_max = float(np.min(corners_j[:, 1])), float(np.max(corners_j[:, 1]))

            overlap_x = max(0.0, min(xi_max, xj_max) - max(xi_min, xj_min))
            overlap_y = max(0.0, min(yi_max, yj_max) - max(yi_min, yj_min))
            overlap_area = overlap_x * overlap_y
            if overlap_area > 0:
                smaller_area = min(
                    (xi_max - xi_min) * (yi_max - yi_min),
                    (xj_max - xj_min) * (yj_max - yj_min),
                )
                if smaller_area > 0:
                    penalty += overlap_area / smaller_area
    return penalty