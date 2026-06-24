"""Random search optimizer for tool parameter optimization.

Simple baseline that samples random parameter vectors and keeps the best one.
"""

from typing import Callable, Optional
from dataclasses import dataclass, field

import numpy as np
from rich.console import Console
from rich.table import Table

from toolgen2d.config import TaskConfig
from toolgen2d.geometry import param_bounds_array


@dataclass
class RandomSearchResult:
    """Result of a random search optimization run."""

    best_params: np.ndarray = field(default_factory=lambda: np.array([]))
    best_reward: float = -np.inf
    history: list = field(default_factory=list)


class RandomSearchOptimizer:
    """Simple random search baseline for tool parameter optimization."""

    def __init__(
        self,
        task_config: TaskConfig,
        evaluate_fn: Callable[[np.ndarray, int], float],
        console: Optional[Console] = None,
    ):
        """Initialize random search optimizer.

        Args:
            task_config: TaskConfig with parameter bounds.
            evaluate_fn: Function that takes (params, seed) and returns reward.
            console: Rich console for logging.
        """
        self.task_cfg = task_config
        self.evaluate = evaluate_fn
        self.console = console or Console()
        self.lower, self.upper = param_bounds_array(task_config)
        self.dim = len(self.lower)

    def run(self, n_samples: int = 1000, seed: int = 0, eval_seeds: int = 2) -> RandomSearchResult:
        """Run random search.

        Args:
            n_samples: Number of random parameter vectors to try.
            seed: Random seed.
            eval_seeds: Number of evaluation seeds per candidate.

        Returns:
            RandomSearchResult with best parameters and history.
        """
        np.random.seed(seed)
        result = RandomSearchResult()
        best_reward = -np.inf
        best_params = self.lower.copy()

        self.console.print(f"\n[bold yellow]Random Search (task={self.task_cfg.task_name})[/bold yellow]")
        self.console.print(f"Samples: {n_samples}, Eval seeds: {eval_seeds}")

        for i in range(n_samples):
            params = np.random.uniform(self.lower, self.upper)
            rewards = []
            for eval_seed in range(eval_seeds):
                r = self.evaluate(params, seed + eval_seed)
                rewards.append(r)
            reward = np.mean(rewards)

            result.history.append({
                "sample": i,
                "reward": reward,
                "params_mean": float(np.mean(params)),
            })

            if reward > best_reward:
                best_reward = reward
                best_params = params.copy()

            if i % 200 == 0 or i == n_samples - 1:
                self.console.print(f"  Sample {i:4d}/{n_samples} | Best: {best_reward:.2f}")

        # Final re-evaluation
        final_reward = self.evaluate(best_params, seed)
        result.best_params = best_params
        result.best_reward = final_reward

        table = Table(title="Random Search Results")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        table.add_row("Best Reward", f"{final_reward:.2f}")
        table.add_row("Best Params Norm", f"{np.linalg.norm(best_params):.2f}")
        self.console.print(table)

        return result