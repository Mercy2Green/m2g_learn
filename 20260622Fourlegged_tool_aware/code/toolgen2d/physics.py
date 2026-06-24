"""Physics simulation helpers using Pymunk.

Provides utility functions to create Pymunk bodies/shapes for the tool,
targets, debris, obstacles, and boundaries.
"""

from typing import List, Tuple, Optional

import numpy as np
import pymunk

from toolgen2d.config import (
    COLLTYPE_TOOL, COLLTYPE_TARGET, COLLTYPE_DEBRIS,
    COLLTYPE_OBSTACLE, COLLTYPE_BOUNDARY,
    PHYSICS_DT,
)
from toolgen2d.geometry import ToolGeometry


def create_tool_body(space: pymunk.Space, tool: ToolGeometry,
                     anchor_pos: Tuple[float, float] = (0.0, 0.0),
                     anchor_angle: float = 0.0) -> pymunk.Body:
    """Create a single kinematic Pymunk body for the entire tool.

    All rectangle shapes are attached to one body in the tool's local frame.
    The body is kinematic (mass=0, moment=0) and follows a scripted trajectory.

    Args:
        space: Pymunk space to add the shapes to.
        tool: ToolGeometry with block positions and corners.
        anchor_pos: (x, y) world position of the tool anchor.
        anchor_angle: Rotation of the tool anchor in radians.

    Returns:
        The kinematic Pymunk Body for the tool.
    """
    body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    body.position = anchor_pos
    body.angle = anchor_angle

    for i, corners in enumerate(tool.abs_corners):
        # Convert world-frame corners to body-local frame
        # Since the body starts at (0,0) with angle=0 in the tool's initial
        # configuration, the corners as decoded are already in body-local frame.
        # But we need to account for the anchor offset.
        # We compute shapes relative to the body's position.
        # For simplicity, we set body.position to (0,0) initially and define
        # all shapes in the local frame. The environment will move the body.
        local_corners = corners - np.array(tool.abs_positions[0])  # approximate
        # Actually, the corners are already in world frame with anchor at (0,0).
        # We'll use them as-is since we'll position the body at the anchor.

        shape = pymunk.Poly(body, corners.tolist())
        shape.collision_type = COLLTYPE_TOOL
        shape.friction = 0.5
        shape.elasticity = 0.3
        shape.filter = pymunk.ShapeFilter(categories=COLLTYPE_TOOL)
        space.add(shape)

    return body


def create_single_tool_shape(space: pymunk.Space, tool: ToolGeometry,
                              body: pymunk.Body) -> None:
    """Add shapes for the tool to an existing kinematic body."""
    for corners in tool.abs_corners:
        shape = pymunk.Poly(body, corners.tolist())
        shape.collision_type = COLLTYPE_TOOL
        shape.friction = 0.5
        shape.elasticity = 0.3
        shape.filter = pymunk.ShapeFilter(categories=COLLTYPE_TOOL)
        space.add(shape)


def create_circle(space: pymunk.Space, x: float, y: float, radius: float,
                  collision_type: int, mass: float = 1.0) -> pymunk.Body:
    """Create a dynamic circular body in the space."""
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    body.position = x, y
    shape = pymunk.Circle(body, radius)
    shape.collision_type = collision_type
    shape.friction = 0.8
    shape.elasticity = 0.2
    shape.filter = pymunk.ShapeFilter(categories=collision_type)
    space.add(body, shape)
    return body


def create_rectangle_body(space: pymunk.Space, x: float, y: float,
                           width: float, height: float,
                           collision_type: int,
                           body_type: str = "static"
                           ) -> pymunk.Body:
    """Create a static or kinematic rectangular body."""
    if body_type == "static":
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
    elif body_type == "kinematic":
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    else:
        mass = 1000.0
        moment = pymunk.moment_for_box(mass, (width, height))
        body = pymunk.Body(mass, moment, body_type=pymunk.Body.DYNAMIC)
    body.position = x, y
    shape = pymunk.Poly.create_box(body, (width, height))
    shape.collision_type = collision_type
    shape.friction = 0.8
    shape.elasticity = 0.1
    shape.filter = pymunk.ShapeFilter(categories=collision_type)
    space.add(body, shape)
    return body


def create_boundary_walls(space: pymunk.Space, width: int, height: int) -> List[pymunk.Body]:
    """Create four boundary walls to keep objects inside the world."""
    walls = []
    thickness = 20
    wall_defs = [
        (width / 2, -thickness / 2, width, thickness),           # top
        (width / 2, height + thickness / 2, width, thickness),    # bottom
        (-thickness / 2, height / 2, thickness, height),          # left
        (width + thickness / 2, height / 2, thickness, height),   # right
    ]
    for wx, wy, ww, wh in wall_defs:
        body = create_rectangle_body(space, wx, wy, ww, wh, COLLTYPE_BOUNDARY)
        walls.append(body)
    return walls


def step_simulation(space: pymunk.Space, steps: int, dt: float = PHYSICS_DT) -> None:
    """Step the physics simulation for a given number of steps."""
    for _ in range(steps):
        space.step(dt)
