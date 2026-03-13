"""
SAPIANTA Strategy Optimizer

Purpose
-------
Autonomous search for profitable strategies.

Pipeline
--------
generate strategy
↓
run experiment
↓
evaluate score
↓
mutate
↓
repeat
"""

import random

from runtime.research.experiment_runner import run_experiment
from runtime.research.strategy_registry import StrategyRegistry


# ---------------------------------------------------------
# STRATEGY GENERATOR
# ---------------------------------------------------------

def generate_random_strategy():

    threshold = random.uniform(0.0005, 0.02)

    def strategy(price_history):

        if len(price_history) < 2:
            return "HOLD"

        change = (price_history[-1] - price_history[-2]) / price_history[-2]

        if change > threshold:
            return "BUY"

        if change < -threshold:
            return "SELL"

        return "HOLD"

    strategy.__name__ = f"threshold_strategy_{round(threshold,5)}"

    return strategy


# ---------------------------------------------------------
# STRATEGY MUTATION
# ---------------------------------------------------------

def mutate_strategy(strategy):

    name = strategy.__name__

    threshold = float(name.split("_")[-1])

    mutation = random.uniform(-0.002, 0.002)

    new_threshold = max(0.0001, threshold + mutation)

    def new_strategy(price_history):

        if len(price_history) < 2:
            return "HOLD"

        change = (price_history[-1] - price_history[-2]) / price_history[-2]

        if change > new_threshold:
            return "BUY"

        if change < -new_threshold:
            return "SELL"

        return "HOLD"

    new_strategy.__name__ = f"threshold_strategy_{round(new_threshold,5)}"

    return new_strategy


# ---------------------------------------------------------
# OPTIMIZATION LOOP
# ---------------------------------------------------------

def optimize_strategies(iterations=20):

    registry = StrategyRegistry()

    best_strategy = None
    best_score = -999999

    strategy = generate_random_strategy()

    for i in range(iterations):

        result = run_experiment(strategy)

        score = result["metrics"]["total_profit"]

        # Save result to registry
        registry.register(strategy.__name__, score)

        print("\nIteration", i)
        print("Strategy:", strategy.__name__)
        print("Score:", score)

        if score > best_score:

            best_score = score
            best_strategy = strategy

        strategy = mutate_strategy(strategy)

    print("\nBest strategy discovered:")
    print(best_strategy.__name__)
    print("Score:", best_score)

    print("\nTop strategies discovered:")

    for s in registry.leaderboard(5):
        print(s)

    return best_strategy


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    optimize_strategies(20)