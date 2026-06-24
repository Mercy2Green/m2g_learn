"""Analysis tools for toolgen2d.

Provides functions for comparing optimization runs, generating summary reports,
and analyzing discovered tool geometries.
"""

import json
import os
from typing import List, Dict, Any, Optional

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table

from toolgen2d.config import get_config
from toolgen2d.geometry import decode_tool, compute_hook_score, compute_sweeper_width_score


def load_history(csv_path: str) -> List[Dict[str, Any]]:
    """Load a history CSV file."""
    import csv
    history = []
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            history.append({k: float(v) if v.replace('.', '', 1).replace('-', '', 1).isdigit() else v
                           for k, v in row.items()})
    return history


def load_best(best_path: str) -> Dict[str, Any]:
    """Load a best.json file."""
    with open(best_path, "r") as f:
        return json.load(f)


def compare_runs(run_dirs: List[str], labels: List[str], output_dir: str) -> None:
    """Compare multiple optimization runs and save comparison plots.

    Args:
        run_dirs: List of directories containing history.csv files.
        labels: Labels for each run.
        output_dir: Directory to save comparison plots.
    """
    os.makedirs(output_dir, exist_ok=True)
    fig, ax = plt.subplots(figsize=(12, 6))

    colors = plt.cm.tab10(np.linspace(0, 1, len(run_dirs)))

    for i, (run_dir, label) in enumerate(zip(run_dirs, labels)):
        csv_path = os.path.join(run_dir, "history.csv")
        if not os.path.exists(csv_path):
            continue
        history = load_history(csv_path)
        gens = [h["generation"] for h in history]
        best = [h["best_reward"] for h in history]
        mean = [h["mean_reward"] for h in history]

        ax.plot(gens, best, color=colors[i], label=f"{label} (best)", linewidth=2)
        ax.plot(gens, mean, color=colors[i], linestyle="--", label=f"{label} (mean)", alpha=0.6)

    ax.set_xlabel("Generation")
    ax.set_ylabel("Reward")
    ax.set_title("Comparison of Optimization Runs")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.savefig(os.path.join(output_dir, "comparison.png"), dpi=150, bbox_inches="tight")
    plt.close(fig)


def analyze_tool_geometry(best_path: str, task: str, output_dir: str) -> None:
    """Analyze and visualize the geometry of a discovered tool.

    Args:
        best_path: Path to best.json.
        task: Task name ('hook' or 'sweeper').
        output_dir: Directory to save analysis outputs.
    """
    os.makedirs(output_dir, exist_ok=True)
    data = load_best(best_path)
    params = np.array(data["params"])
    config = get_config(task)
    tool = decode_tool(params, config)

    # Compute metrics
    hook_score = compute_hook_score(tool)
    width_score = compute_sweeper_width_score(tool)

    # Create detailed geometry plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Plot 1: Tool geometry with block indices
    ax = axes[0]
    for i, corners in enumerate(tool.abs_corners):
        xs = [c[0] for c in corners] + [corners[0][0]]
        ys = [c[1] for c in corners] + [corners[0][1]]
        ax.fill(xs, ys, alpha=0.6, label=f"Block {i}" if i < 5 else None)
        center = np.mean(corners, axis=0)
        ax.text(center[0], center[1], str(i), ha="center", va="center", fontsize=10)

    ax.set_aspect("equal")
    ax.set_title(f"Tool Geometry: {task}")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 2: Block parameter bar chart
    ax = axes[1]
    param_names = ["dx", "dy", "length", "width", "angle"]
    n_blocks = len(tool.blocks)
    x = np.arange(n_blocks)
    width = 0.15

    for pi, pname in enumerate(param_names):
        values = []
        for b in tool.blocks:
            v = getattr(b, pname)
            values.append(v)
        ax.bar(x + pi * width, values, width, label=pname)

    ax.set_xlabel("Block Index")
    ax.set_ylabel("Parameter Value")
    ax.set_title("Block Parameters")
    ax.set_xticks(x + width * 2)
    ax.set_xticklabels([str(i) for i in range(n_blocks)])
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, "tool_analysis.png"), dpi=150, bbox_inches="tight")
    plt.close(fig)

    # Print metrics
    console = Console()
    table = Table(title=f"Tool Geometry Analysis ({task})")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("Total area", f"{tool.total_area:.0f}")
    table.add_row("Number of blocks", str(len(tool.blocks)))
    table.add_row("Hook score", f"{hook_score:.2f}")
    table.add_row("Sweeper width score", f"{width_score:.2f}")
    console.print(table)