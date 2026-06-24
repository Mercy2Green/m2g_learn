"""Training CLI for toolgen2d.

Runs CEM or random search optimization for Hook or Sweeper tasks.
Saves outputs including best parameters, history curves, and snapshots.
Supports real-time pygame visualization during training.
"""

import argparse
import json
import os
from typing import Dict, Any, Optional, Callable

import numpy as np
import matplotlib
matplotlib.use("Agg")  # non-interactive backend for headless saving
import matplotlib.pyplot as plt
from rich.console import Console

from toolgen2d.config import get_config
from toolgen2d.envs import HookEnv, SweeperEnv
from toolgen2d.optim import CEMOptimizer, RandomSearchOptimizer
from toolgen2d.optim.cem import CEMConfig
from toolgen2d.geometry import decode_tool, param_bounds_array
from toolgen2d.render import Renderer


def create_env(task_name: str, seed: int):
    """Create the appropriate environment for the given task."""
    config = get_config(task_name)
    if task_name == "hook":
        return HookEnv(config, seed=seed)
    elif task_name == "sweeper":
        return SweeperEnv(config, seed=seed)
    else:
        raise ValueError(f"Unknown task: {task_name}")


def make_evaluate_fn(task_name: str, seed: int, env_seed_offset: int = 0):
    """Create an evaluation function for the optimizer.

    Args:
        task_name: 'hook' or 'sweeper'.
        seed: Base seed for the evaluation.
        env_seed_offset: Offset applied per evaluation call.

    Returns:
        A function that takes (params, eval_seed) and returns reward.
    """
    def evaluate(params: np.ndarray, eval_seed: int) -> float:
        env = create_env(task_name, seed + eval_seed + env_seed_offset)
        result = env.run_rollout(params)
        env.close()
        return result.reward
    return evaluate


def save_best_tool(params: np.ndarray, task_name: str, output_dir: str) -> None:
    """Save the best tool's geometry as a visualization image."""
    config = get_config(task_name)
    tool = decode_tool(params, config)

    # Save as JSON
    data = {
        "task": task_name,
        "params": params.tolist(),
        "total_area": tool.total_area,
        "num_positions": len(tool.abs_positions),
        "abs_positions": [(float(x), float(y)) for x, y in tool.abs_positions],
        "abs_angles": [float(a) for a in tool.abs_angles],
        "blocks": [
            {
                "dx": b.dx, "dy": b.dy,
                "length": b.length, "width": b.width,
                "angle": b.angle,
            }
            for b in tool.blocks
        ],
    }
    with open(os.path.join(output_dir, "best.json"), "w") as f:
        json.dump(data, f, indent=2)

    # Save visualization using matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    for corners in tool.abs_corners:
        xs = [c[0] for c in corners] + [corners[0][0]]
        ys = [c[1] for c in corners] + [corners[0][1]]
        ax.fill(xs, ys, alpha=0.7, color="steelblue", edgecolor="navy", linewidth=2)

    ax.set_xlim(-100, 200)
    ax.set_ylim(-150, 150)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.set_title(f"Best {task_name} tool (area: {tool.total_area:.0f})")
    fig.savefig(os.path.join(output_dir, "best.png"), dpi=150, bbox_inches="tight")
    plt.close(fig)


def save_curves(history: list, output_dir: str, task_name: str) -> None:
    """Save training curves as PNG images and CSV."""
    gens = [h["generation"] for h in history]
    best_rewards = [h["best_reward"] for h in history]
    mean_rewards = [h["mean_reward"] for h in history]
    elite_mean_rewards = [h["elite_mean_reward"] for h in history]

    # Save CSV
    import csv
    csv_path = os.path.join(output_dir, "history.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=history[0].keys())
        writer.writeheader()
        writer.writerows(history)

    # Reward curve
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(gens, best_rewards, "b-", label="Best", linewidth=2)
    ax.plot(gens, mean_rewards, "g-", label="Mean", alpha=0.7)
    ax.plot(gens, elite_mean_rewards, "r-", label="Elite Mean", alpha=0.7)
    ax.fill_between(gens, mean_rewards, best_rewards, alpha=0.1, color="blue")
    ax.set_xlabel("Generation")
    ax.set_ylabel("Reward")
    ax.set_title(f"{task_name.upper()} - CEM Training Curves")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.savefig(os.path.join(output_dir, "curve_reward.png"), dpi=150, bbox_inches="tight")
    plt.close(fig)

    # Success curve (if task is hook and success metric available)
    if task_name == "hook":
        successes = [h.get("success", 0) for h in history]
        if len(successes) > 0 and any(s > 0 for s in successes):
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(gens, successes, "m-", label="Success", linewidth=2)
            ax.set_xlabel("Generation")
            ax.set_ylabel("Success")
            ax.set_title(f"{task_name.upper()} - Success Rate")
            ax.legend()
            ax.grid(True, alpha=0.3)
            fig.savefig(os.path.join(output_dir, "curve_success.png"), dpi=150, bbox_inches="tight")
            plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="toolgen2d: Train tool geometry via CEM")
    parser.add_argument("--task", type=str, default="hook", choices=["hook", "sweeper"],
                        help="Task to optimize for")
    parser.add_argument("--optimizer", type=str, default="cem", choices=["cem", "random"],
                        help="Optimization method")
    parser.add_argument("--generations", type=int, default=80,
                        help="Number of generations (CEM) or iterations (random)")
    parser.add_argument("--population", type=int, default=64,
                        help="Population size (CEM) or samples per gen (random)")
    parser.add_argument("--elite-frac", type=float, default=0.2,
                        help="Fraction of elites to keep (CEM)")
    parser.add_argument("--max-blocks", type=int, default=None,
                        help="Override max blocks for the task")
    parser.add_argument("--eval-seeds", type=int, default=2,
                        help="Number of evaluation seeds per candidate")
    parser.add_argument("--seed", type=int, default=0,
                        help="Random seed")
    parser.add_argument("--render-every", type=int, default=0,
                        help="Render every N generations with pygame window (0 = never)")
    parser.add_argument("--render-final", action="store_true",
                        help="Open pygame window for final best rollout")
    parser.add_argument("--output-dir", type=str, default=None,
                        help="Output directory (default: outputs/{task}/seed_{seed})")
    args = parser.parse_args()

    console = Console()

    # Setup output directory
    output_dir = args.output_dir or f"outputs/{args.task}/seed_{args.seed}"
    os.makedirs(output_dir, exist_ok=True)

    # Get task config
    task_config = get_config(args.task)
    if args.max_blocks is not None:
        from dataclasses import replace
        task_config = replace(task_config, max_blocks=args.max_blocks)

    # We'll track the best params discovered so far so render_callback can show them
    current_best_params: list = [None]

    # Create evaluation function
    eval_fn = make_evaluate_fn(args.task, args.seed)

    # --- Per-generation render callback ---
    def render_callback(best_params: np.ndarray, gen: int, total_gens: int) -> None:
        """Render current best tool rollout in a pygame window."""
        current_best_params[0] = best_params
        if args.render_every <= 0 or gen % args.render_every != 0:
            return
        env = create_env(args.task, args.seed)
        console.print(
            f"\n[yellow]Rendering generation {gen}/{total_gens} "
            f"(best reward so far)... close pygame window to continue[/yellow]"
        )
        try:
            env.run_rollout(best_params, render=True)
        finally:
            env.close()

    # Run optimization
    if args.optimizer == "cem":
        cem_cfg = CEMConfig(
            population_size=args.population,
            elite_frac=args.elite_frac,
            n_generations=args.generations,
            eval_seeds=args.eval_seeds,
            render_callback=render_callback,
        )
        optimizer = CEMOptimizer(cem_cfg, task_config, eval_fn, console=console)
        result = optimizer.run(seed=args.seed)
    else:  # random search
        optimizer = RandomSearchOptimizer(task_config, eval_fn, console=console)
        n_samples = args.generations * args.population
        from toolgen2d.optim.random_search import RandomSearchResult
        result_raw = optimizer.run(n_samples=n_samples, seed=args.seed,
                                    eval_seeds=args.eval_seeds)
        result = RandomSearchResult()
        result.best_params = result_raw.best_params
        result.best_reward = result_raw.best_reward
        history = []
        gens = args.generations
        pop = args.population
        for g in range(gens):
            start = g * pop
            end = min((g + 1) * pop, len(result_raw.history))
            if start >= len(result_raw.history):
                break
            gen_rewards = [h["reward"] for h in result_raw.history[start:end]]
            if not gen_rewards:
                break
            history.append({
                "generation": g,
                "best_reward": max(gen_rewards),
                "mean_reward": float(np.mean(gen_rewards)),
                "median_reward": float(np.median(gen_rewards)),
                "std_reward": float(np.std(gen_rewards)),
                "elite_mean_reward": float(np.mean(sorted(gen_rewards)[-max(1, pop//5):])),
                "best_params_mean": float(np.mean(result_raw.best_params)),
                "best_params_std": float(np.std(result_raw.best_params)),
            })
        result.history = history

    # Save outputs
    console.print(f"\n[bold]Saving outputs to {output_dir}/[/bold]")
    save_best_tool(result.best_params, args.task, output_dir)
    save_curves(result.history, output_dir, args.task)
    console.print(f"[green]✓[/green] Best tool saved to {output_dir}/best.json")
    console.print(f"[green]✓[/green] Best tool image saved to {output_dir}/best.png")
    console.print(f"[green]✓[/green] Training curves saved to {output_dir}/curve_reward.png")

    # Final rollout: metrics + optional interactive render
    console.print(f"\n[bold]Running final rollout...[/bold]")
    env = create_env(args.task, args.seed)
    final_result = env.run_rollout(
        result.best_params,
        render=args.render_final,
    )
    env.close()

    console.print(f"\n[bold]Final Rollout Metrics:[/bold]")
    console.print(f"  Reward: {final_result.reward:.2f}")
    if args.task == "hook":
        console.print(f"  Target displacement: {final_result.target_displacement:.1f}")
        console.print(f"  Success: {final_result.success}")
        console.print(f"  Hook score: {final_result.hook_score:.1f}")
    else:
        n_total = final_result.inside_count + final_result.outside_count
        console.print(f"  Debris in container: {final_result.inside_count}/{n_total}")
        console.print(f"  Sweeper width score: {final_result.sweeper_width_score:.1f}")
    console.print(f"  Total area: {final_result.total_area:.0f}")


if __name__ == "__main__":
    main()