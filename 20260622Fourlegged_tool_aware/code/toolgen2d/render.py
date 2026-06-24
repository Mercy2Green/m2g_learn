"""Rendering utilities using pygame for 2D visualization and GIF export."""

from typing import List, Tuple, Optional, Callable
import os

import numpy as np
import pygame
import pymunk

from toolgen2d.config import (
    WORLD_WIDTH, WORLD_HEIGHT,
    COLOR_BACKGROUND, COLOR_REACHABLE_ZONE, COLOR_CONTAINER,
    COLOR_OBSTACLE, COLOR_TARGET, COLOR_DEBRIS,
    COLOR_TOOL, COLOR_TOOL_OUTLINE, COLOR_TRAJECTORY,
)


class Renderer:
    """Pygame-based renderer for 2D tool-generation environments.

    Supports interactive display and headless frame capture for GIF export.
    """

    def __init__(self, headless: bool = False, display_scale: float = 1.0):
        """Initialize the renderer.

        Args:
            headless: If True, don't open a pygame window (for batch/GIF generation).
            display_scale: Scale factor for the display window.
        """
        self.headless = headless
        self.display_scale = display_scale
        self.screen: Optional[pygame.Surface] = None
        self.clock: Optional[pygame.time.Clock] = None
        self.width = int(WORLD_WIDTH * display_scale)
        self.height = int(WORLD_HEIGHT * display_scale)
        self._initialized = False

    def initialize(self) -> None:
        """Initialize pygame and create the display surface."""
        if self._initialized:
            return

        pygame.init()
        pygame.font.init()
        if not self.headless:
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.set_caption("toolgen2d")
            self.clock = pygame.time.Clock()
        else:
            self.screen = pygame.Surface((self.width, self.height))
        self._initialized = True
        self.font = pygame.font.SysFont("Arial", 16)
        self.title_font = pygame.font.SysFont("Arial", 20, bold=True)

    def handle_events(self) -> bool:
        """Handle pygame events. Returns False if user quit."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True

    def clear(self) -> None:
        """Clear the screen with background color."""
        if self.screen is not None:
            self.screen.fill(COLOR_BACKGROUND)

    def draw_reachable_zone(self, x: float, y: float, width: float, height: float) -> None:
        """Draw the reachable zone (green shaded area)."""
        if self.screen is None:
            return
        rect = pygame.Rect(
            int(x * self.display_scale),
            int(y * self.display_scale),
            int(width * self.display_scale),
            int(height * self.display_scale),
        )
        s = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        s.fill((*COLOR_REACHABLE_ZONE, 100))
        self.screen.blit(s, rect)

    def draw_container(self, x: float, y: float, width: float, height: float) -> None:
        """Draw the container region (green shaded area for sweeper)."""
        if self.screen is None:
            return
        rect = pygame.Rect(
            int(x * self.display_scale),
            int(y * self.display_scale),
            int(width * self.display_scale),
            int(height * self.display_scale),
        )
        s = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        s.fill((*COLOR_CONTAINER, 100))
        self.screen.blit(s, rect)
        # Draw border
        pygame.draw.rect(self.screen, (100, 180, 100), rect, 2)

    def draw_obstacle(self, x: float, y: float, width: float, height: float) -> None:
        """Draw an obstacle rectangle."""
        if self.screen is None:
            return
        rect = pygame.Rect(
            int(x * self.display_scale),
            int(y * self.display_scale),
            int(width * self.display_scale),
            int(height * self.display_scale),
        )
        pygame.draw.rect(self.screen, COLOR_OBSTACLE, rect)
        pygame.draw.rect(self.screen, (100, 100, 100), rect, 2)

    # Per-block color palette for visual distinction
    TOOL_BLOCK_COLORS = [
        (60, 120, 200),     # blue
        (200, 120, 60),     # orange
        (60, 180, 120),     # green
        (180, 80, 160),     # purple
        (200, 60, 60),      # red
        (60, 180, 180),     # teal
        (160, 160, 60),     # olive
    ]
    TOOL_BLOCK_OUTLINES = [
        (30, 60, 120),      # dark blue
        (140, 80, 20),      # dark orange
        (30, 120, 60),      # dark green
        (120, 40, 100),     # dark purple
        (140, 20, 20),      # dark red
        (20, 120, 120),     # dark teal
        (100, 100, 20),     # dark olive
    ]

    def draw_tool(self, corners_list: List[np.ndarray], block_labels: bool = False) -> None:
        """Draw the tool rectangles from their world-frame corners.

        Args:
            corners_list: List of 4-corner arrays for each block.
            block_labels: If True, use distinct colors per block and draw block index.
        """
        if self.screen is None:
            return
        for i, corners in enumerate(corners_list):
            color_idx = i % len(self.TOOL_BLOCK_COLORS)
            fill_color = self.TOOL_BLOCK_COLORS[color_idx] if block_labels else COLOR_TOOL
            outline_color = self.TOOL_BLOCK_OUTLINES[color_idx] if block_labels else COLOR_TOOL_OUTLINE

            scaled_corners = [
                (int(c[0] * self.display_scale), int(c[1] * self.display_scale))
                for c in corners
            ]
            if len(scaled_corners) < 3:
                continue

            # Fill with solid color
            pygame.draw.polygon(self.screen, fill_color, scaled_corners)

            # Thick outline (3px) so it's visible against any background
            pygame.draw.polygon(self.screen, outline_color, scaled_corners, 3)

            # Draw block index label
            if block_labels:
                cx = int(np.mean([c[0] for c in scaled_corners]))
                cy = int(np.mean([c[1] for c in scaled_corners]))
                label = self.font.render(str(i), True, (255, 255, 255))
                self.screen.blit(label, (cx - label.get_width() // 2, cy - label.get_height() // 2))

    def draw_circle(self, x: float, y: float, radius: float, color: Tuple[int, int, int]) -> None:
        """Draw a filled circle."""
        if self.screen is None:
            return
        pygame.draw.circle(
            self.screen,
            color,
            (int(x * self.display_scale), int(y * self.display_scale)),
            int(radius * self.display_scale),
        )

    def draw_trajectory(self, points: List[Tuple[float, float]]) -> None:
        """Draw a trajectory line."""
        if self.screen is None or len(points) < 2:
            return
        scaled = [
            (int(x * self.display_scale), int(y * self.display_scale))
            for x, y in points
        ]
        pygame.draw.lines(self.screen, COLOR_TRAJECTORY, False, scaled, 1)

    def draw_text(self, text: str, x: float, y: float, color: Tuple[int, int, int] = (0, 0, 0),
                  font: Optional[pygame.font.Font] = None) -> None:
        """Draw text on screen."""
        if self.screen is None:
            return
        f = font or self.font
        surf = f.render(text, True, color)
        self.screen.blit(surf, (int(x * self.display_scale), int(y * self.display_scale)))

    def draw_title(self, text: str) -> None:
        """Draw a title at the top of the screen."""
        self.draw_text(text, 10, 5, font=self.title_font)

    def flip(self) -> None:
        """Flip the display buffer."""
        if not self.headless and self.screen is not None:
            pygame.display.flip()
            if self.clock is not None:
                self.clock.tick(60)

    def get_frame(self) -> np.ndarray:
        """Get the current frame as a numpy array (for GIF export)."""
        if self.screen is None:
            return np.zeros((self.height, self.width, 3), dtype=np.uint8)
        return pygame.surfarray.array3d(self.screen).transpose(1, 0, 2)

    def close(self) -> None:
        """Close the renderer."""
        if self._initialized:
            pygame.quit()
            self._initialized = False