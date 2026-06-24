"""Visualization CLI for toolgen2d.

Loads a saved best.json checkpoint and runs a rollout with rendering.
Can save the rollout as a GIF animation and a final frame PNG.
"""

import argparse
import json
import os

import numpy as np
import imageio
from rich.console import Console

from toolgen2d.config import get_config
from toolgen2d.envs import HookEnv, SweeperEnv
from toolgen2d.geometry import decode_tool, param_bounds_array


def create_env(task_name: str, seed: int):
    """Create the appropriate environment for the given task."""
    config = get_config(task_name)
    if task_name == "hook":
        return HookEnv(config, seed=seed)
    elif task_name == "sweeper":
        return SweeperEnv(config, seed=seed)
    else:
        raise ValueError(f"Unknown task: {task_name}")


def main():
    parser = argparse.ArgumentParser(description="toolgen2d: Visualize a saved tool rollout")
    parser.add_argument("--task", type=str, default="hook", choices=["hook", "sweeper"],
                        help="Task type")
    parser.add_argument("--checkpoint", type=str, required=True,
                        help="Path to best.json checkpoint")
    parser.add_argument("--gif", type=str, default=None,
                        help="Path to save rollout GIF (e.g., outputs/hook/seed_0/best_rollout.gif)")
    parser.add_argument("--png", type=str, default=None,
                        help="Path to save final frame PNG")
    parser.add_argument("--seed", type=int, default=0,
                        help="Random seed for rollout")
    parser.add_argument("--headless", action="store_true",
                        help="Run headless (no pygame window)")
    args = parser.parse_args()

    console = Console()

    # Load checkpoint
    console.print(f"[bold]Loading checkpoint: {args.checkpoint}[/bold]")
    with open(args.checkpoint, "r") as f:
        data = json.load(f)

    params = np.array(data["params"])
    console.print(f"  Task: {data['task']}")
    console.print(f"  Total area: {data.get('total_area', 'N/A')}")

    # Create environment
    env = create_env(args.task, args.seed)

    # Run rollout with rendering
    render = not args.headless
    has_gif = args.gif is not None
    console.print(f"[bold]Running rollout...[/bold]")
    result = env.run_rollout(params, render=render, gif_frames=has_gif)

    # Print metrics
    console.print(f"\n[bold]Rollout Metrics:[/bold]")
    console.print(f"  Reward: {result.reward:.2f}")
    if args.task == "hook":
        console.print(f"  Target displacement: {result.target_displacement:.1f}")
        console.print(f"  Success: {result.success}")
        console.print(f"  Hook score: {result.hook_score:.1f}")
    else:
        console.print(f"  Debris in container: {result.inside_count}/{result.inside_count + result.outside_count}")
        console.print(f"  Sweeper width score: {result.sweeper_width_score:.1f}")

    # Save GIF
    if has_gif and result.frames:
        console.print(f"[bold]Saving GIF to {args.gif}...[/bold]")
        os.makedirs(os.path.dirname(args.gif), exist_ok=True)
        imageio.mimsave(args.gif, result.frames, fps=30, loop=0)
        console.print(f"[green]✓[/green] GIF saved to {args.gif} ({len(result.frames)} frames)")

    # Save final frame PNG
    if args.png and result.frames:
        os.makedirs(os.path.dirname(args.png), exist_ok=True)
        imageio.imwrite(args.png, result.frames[-1])
        console.print(f"[green]✓[/green] Final frame saved to {args.png}")

    # Save final frame as PNG even without explicit --png flag if we have frames
    if not args.png and has_gif and result.frames:
        png_path = args.gif.replace(".gif", ".png")
        if png_path != args.gif:
            os.makedirs(os.path.dirname(png_path), exist_ok=True)
            imageio.imwrite(png_path, result.frames[-1])
            console.print(f"[green]✓[/green] Final frame saved to {png_path}")

    # Close
    env.close()
    console.print("[green]Done![/green]")


if __name__ == "__main__":
    main()