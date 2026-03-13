"""
SAPIANTA Experiment Runner

Purpose
-------
Run controlled strategy experiments across multiple market regimes.

This module is the first step toward the autonomous research loop.
"""

from runtime.market.market_regime_engine import generate_regime_suite
from runtime.market.market_simulator import simulate_market
from runtime.research.experiment_database import ExperimentDatabase


# ---------------------------------------------------------
# METRIC CALCULATION
# ---------------------------------------------------------

def compute_metrics(results):

    profits = [r["profit"] for r in results]

    total_profit = sum(profits)

    avg_profit = total_profit / len(profits)

    max_drawdown = min(profits)

    return {
        "total_profit": total_profit,
        "avg_profit": avg_profit,
        "worst_case": max_drawdown
    }


# ---------------------------------------------------------
# EXPERIMENT RUNNER
# ---------------------------------------------------------

def run_experiment(strategy, seed=None):

    regimes = generate_regime_suite()

    results = []

    for regime in regimes:

        simulation = simulate_market(
            strategy=strategy,
            regime=regime,
            seed=seed
        )

        results.append(simulation)

    metrics = compute_metrics(results)

    result = {
        "strategy": strategy.__name__,
        "metrics": metrics,
        "results": results
    }

    # -----------------------------------------------------
    # RECORD EXPERIMENT
    # -----------------------------------------------------

    db = ExperimentDatabase()
    db.record(result)

    return result


# ---------------------------------------------------------
# TEST STRATEGY
# ---------------------------------------------------------

def example_strategy(price_history):

    """
    Simple test strategy.

    Buy if price increased over last step.
    """

    if len(price_history) < 3:
        return "HOLD"

    if price_history[-1] > price_history[-2]:
        return "BUY"

    return "HOLD"


# ---------------------------------------------------------
# MANUAL TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    print("\nRunning experiment...\n")

    result = run_experiment(example_strategy)

    print(result)