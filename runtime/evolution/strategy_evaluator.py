"""
SAPIANTA Strategy Evaluator

Purpose
-------
Unified strategy evaluation pipeline.

Combines:
- experiment_engine
- market_simulator
- fitness_metrics
- fitness_engine

Used by:
genome_population
strategy_search
future AI strategy discovery modules
"""

from runtime.experiments.experiment_engine import run_strategy_experiment
from runtime.experiments.experiment_engine_market_adapter import run_market_strategy_test
from runtime.scenarios.scenario_engine import generate_scenario_suite

from runtime.evolution.fitness_engine import evaluate_scenario_suite
from runtime.evolution.fitness_metrics import compute_performance_metrics


# ---------------------------------------------------------
# POLICY EVALUATION
# ---------------------------------------------------------

def evaluate_policy(strategy):

    scenarios = generate_scenario_suite(strategy["strategy_id"])

    results = []

    for scenario in scenarios:

        record = run_strategy_experiment(strategy, scenario)

        results.append(record)

    policy_fitness = evaluate_scenario_suite(results)

    return policy_fitness


# ---------------------------------------------------------
# MARKET PERFORMANCE
# ---------------------------------------------------------

def evaluate_market(strategy):

    market_result = run_market_strategy_test(strategy)

    returns = market_result["strategy_returns"]

    metrics = compute_performance_metrics(returns)

    return metrics


# ---------------------------------------------------------
# FINAL FITNESS
# ---------------------------------------------------------

def compute_final_fitness(policy_score, metrics):

    profit = metrics["profit"]
    drawdown = metrics["drawdown"]
    sharpe = min(metrics["sharpe_like"], 2.5)

    fitness = (
        policy_score * 0.5
        + sharpe * 0.3
        + profit * 0.2
        - drawdown * 0.4
    )

    return fitness


# ---------------------------------------------------------
# FULL STRATEGY EVALUATION
# ---------------------------------------------------------

def evaluate_strategy(strategy):

    policy_score = evaluate_policy(strategy)

    market_metrics = evaluate_market(strategy)

    fitness = compute_final_fitness(policy_score, market_metrics)

    return {

        "policy_score": policy_score,

        "market_metrics": market_metrics,

        "fitness": fitness
    }


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    strategy = {

        "strategy_id": "test_strategy",

        "domain_id": "trading",

        "action": {

            "type": "BUY",

            "asset": "BTC",

            "quantity": 0.1
        }
    }

    result = evaluate_strategy(strategy)

    print("\nStrategy evaluation:")

    print(result)