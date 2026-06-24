"""Cross-Entropy Method (CEM) optimizer for tool parameter search.

CEM is a simple evolutionary algorithm that maintains a Gaussian distribution
over the parameter space. At each generation, it samples candidates, evaluates
them, selects the top fraction (elites), and updates the distribution parameters
(mean and std) from the elites.
"""

from typing import Callable, List, Tuple, Optional, Any
from dataclasses import dataclass, field

import numpy as np
from tqdm import tqdm
from rich.console import Console
from rich.table import Table

from toolgen2d.config import TaskConfig
from toolgen2d.geometry import param_bounds_array


@dataclass
class CEMConfig:
    """Configuration for the CEM optimizer."""

    population_size: int = 64
    elite_frac: float = 0.2
    n_generations: int = 80
    eval_seeds: int = 2  # number of random seeds to evaluate each candidate
    # Distribution initialization
    init_std_ratio: float = 0.35
    # Clipping
    min_std: float = 0.01
    max_std_ratio: float = 0.5
    # Moving average for update
    alpha: float = 0.7  # smoothing factor for mean/std update
    # Optional per-generation render callback (best_params, gen, total_gens) -> None
    render_callback: Optional[Callable[[np.ndarray, int, int], None]] = None


@dataclass
class CEMResult:
    """Result of a CEM optimization run."""

    best_params: np.ndarray = field(default_factory=lambda: np.array([]))
    best_reward: float = -np.inf
    history: List[dict] = field(default_factory=list)
    mean_history: List[np.ndarray] = field(default_factory=list)
    std_history: List[np.ndarray] = field(default_factory=list)


class CEMOptimizer:
    """Cross-Entropy Method optimizer for tool parameters."""

    def __init__(
        self,
        config: CEMConfig,
        task_config: TaskConfig,
        evaluate_fn: Callable[[np.ndarray, int], float],
        console: Optional[Console] = None,
    ):
        """Initialize CEM optimizer.

        Args:
            config: CEMConfig with hyperparameters.
            task_config: TaskConfig with parameter bounds.
            evaluate_fn: Function that takes (params, seed) and returns reward.
            console: Rich console for logging.
        """
        self.cfg = config
        self.task_cfg = task_config
        self.evaluate = evaluate_fn
        self.console = console or Console()

        # Parameter bounds
        self.lower, self.upper = param_bounds_array(task_config)
        self.dim = len(self.lower)

        # Distribution parameters
        self.mean = (self.lower + self.upper) / 2.0
        self.std = (self.upper - self.lower) * config.init_std_ratio

        # Ensure std is within bounds
        self.std = np.clip(self.std, config.min_std, (self.upper - self.lower) * config.max_std_ratio)

    def _sample_population(self) -> np.ndarray:
        """Sample a population from the current Gaussian distribution."""
        samples = np.random.randn(self.cfg.population_size, self.dim)
        samples = samples * self.std[np.newaxis, :] + self.mean[np.newaxis, :]
        # Clip to parameter bounds
        samples = np.clip(samples, self.lower[np.newaxis, :], self.upper[np.newaxis, :])
        return samples

    def _update_distribution(self, elites: np.ndarray) -> None:
        """Update mean and std from elite samples."""
        if len(elites) == 0:
            return

        new_mean = np.mean(elites, axis=0)
        new_std = np.std(elites, axis=0)

        # Smooth update with moving average
        self.mean = self.cfg.alpha * self.mean + (1.0 - self.cfg.alpha) * new_mean
        self.std = self.cfg.alpha * self.std + (1.0 - self.cfg.alpha) * new_std

        # Clip std to reasonable range
        self.std = np.clip(
            self.std,
            self.cfg.min_std,
            (self.upper - self.lower) * self.cfg.max_std_ratio,
        )

    def run(self, seed: int = 0) -> CEMResult:
        """Run CEM optimization.

        Args:
            seed: Random seed.

        Returns:
            CEMResult with best parameters and history.
        """
        np.random.seed(seed)
        result = CEMResult()
        best_reward = -np.inf
        best_params = self.mean.copy()

        # Track best params for each seed
        global_best_reward = -np.inf
        global_best_params = self.mean.copy()

        # Print table header
        self.console.print(f"\n[bold cyan]CEM Optimization (task={self.task_cfg.task_name})[/bold cyan]")
        self.console.print(f"Population: {self.cfg.population_size}, "
                          f"Generations: {self.cfg.n_generations}, "
                          f"Elite frac: {self.cfg.elite_frac}, "
                          f"Eval seeds: {self.cfg.eval_seeds}")

        for gen in range(self.cfg.n_generations):
            # Sample population
            population = self._sample_population()

            # Evaluate each candidate across multiple seeds
            rewards = np.zeros(self.cfg.population_size)
            for i in range(self.cfg.population_size):
                seed_rewards = []
                for eval_seed in range(self.cfg.eval_seeds):
                    r = self.evaluate(population[i], seed + eval_seed)
                    seed_rewards.append(r)
                rewards[i] = np.mean(seed_rewards)

            # Select elites
            n_elites = max(1, int(self.cfg.population_size * self.cfg.elite_frac))
            elite_indices = np.argsort(rewards)[-n_elites:]
            elites = population[elite_indices]

            # Update distribution
            self._update_distribution(elites)

            # Track best
            gen_best_idx = np.argmax(rewards)
            gen_best_reward = rewards[gen_best_idx]
            if gen_best_reward > best_reward:
                best_reward = gen_best_reward
                best_params = population[gen_best_idx].copy()

            # Global best across all generations
            if best_reward > global_best_reward:
                global_best_reward = best_reward
                global_best_params = best_params.copy()

            # Invoke render callback if set (after global best update)
            if self.cfg.render_callback is not None:
                try:
                    self.cfg.render_callback(global_best_params, gen, self.cfg.n_generations)
                except Exception as e:
                    self.console.print(f"[red]Render callback error at gen {gen}: {e}[/red]")

            # Record history
            gen_data = {
                "generation": gen,
                "best_reward": gen_best_reward,
                "mean_reward": float(np.mean(rewards)),
                "median_reward": float(np.median(rewards)),
                "std_reward": float(np.std(rewards)),
                "elite_mean_reward": float(np.mean(rewards[elite_indices])),
                "best_params_mean": float(np.mean(best_params)),
                "best_params_std": float(np.std(best_params)),
            }
            result.history.append(gen_data)
            result.mean_history.append(self.mean.copy())
            result.std_history.append(self.std.copy())

            # Print progress every 10 generations
            if gen % 10 == 0 or gen == self.cfg.n_generations - 1:
                self.console.print(
                    f"  Gen {gen:3d} | Best: {gen_best_reward:8.2f} | "
                    f"Mean: {np.mean(rewards):8.2f} | "
                    f"Elite mean: {np.mean(rewards[elite_indices]):8.2f} | "
                    f"Global best: {global_best_reward:8.2f}"
                )

        # Re-evaluate best params with original seed for deterministic result
        final_reward = self.evaluate(global_best_params, seed)
        result.best_params = global_best_params
        result.best_reward = final_reward

        # Summary table
        table = Table(title="CEM Results")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        table.add_row("Best Reward", f"{global_best_reward:.2f}")
        table.add_row("Best Params Norm", f"{np.linalg.norm(global_best_params):.2f}")
        table.add_row("Final Reward", f"{final_reward:.2f}")
        self.console.print(table)

        return result