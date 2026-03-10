"""
SAPIANTA Strategy Evolution Engine

Purpose
-------
Generate, test and evolve candidate strategies.

Capabilities
------------
1. Parametric search
2. Genetic mutation
3. Multi-scenario evaluation
4. Strategy ranking
5. Strategy registry persistence
"""

import random
import uuid
import json

from runtime.experiments.experiment_engine import run_strategy_experiment
from runtime.evolution.strategy_registry import register_strategy
from runtime.scenarios.scenario_engine import generate_scenario_suite


# ---------------------------------------------------------
# PARAMETRIC SEARCH
# ---------------------------------------------------------

def generate_parametric_strategies(base_strategy: dict, n: int = 10):

    strategies = []

    for i in range(n):

        quantity = round(random.uniform(0.01, 0.2), 3)

        strategy = {
            "strategy_id": f"{base_strategy['strategy_id']}_variant_{i}",
            "domain_id": base_strategy["domain_id"],
            "action": {
                "type": base_strategy["action"]["type"],
                "asset": base_strategy["action"]["asset"],
                "quantity": quantity
            }
        }

        strategies.append(strategy)

    return strategies


# ---------------------------------------------------------
# GENETIC MUTATION
# ---------------------------------------------------------

def mutate_strategy(strategy: dict):

    quantity = strategy["action"]["quantity"]

    mutation = round(random.uniform(-0.05, 0.05), 3)

    new_quantity = max(0.001, round(quantity + mutation, 3))

    return {
        "strategy_id": f"{strategy['strategy_id']}_mut_{uuid.uuid4().hex[:6]}",
        "domain_id": strategy["domain_id"],
        "action": {
            "type": strategy["action"]["type"],
            "asset": strategy["action"]["asset"],
            "quantity": new_quantity
        }
    }


def genetic_mutation(strategies: list, n_mutations: int = 5):

    mutated = []

    for _ in range(n_mutations):

        parent = random.choice(strategies)

        mutated.append(mutate_strategy(parent))

    return mutated


# ---------------------------------------------------------
# STRATEGY RANKING
# ---------------------------------------------------------

def rank_strategies(results: list):

    return sorted(
        results,
        key=lambda x: x["evaluation"]["avg_acceptance_ratio"],
        reverse=True
    )


# ---------------------------------------------------------
# FULL EVOLUTION CYCLE
# ---------------------------------------------------------

def run_evolution_cycle(base_strategy: dict, generation: int = 1):

    print("\n--- GENERATING STRATEGIES ---")

    strategies = generate_parametric_strategies(base_strategy, n=5)

    results = []

    for strategy in strategies:

        print(f"\nTesting strategy: {strategy['strategy_id']}")

        scenarios = generate_scenario_suite(strategy["strategy_id"])

        scenario_results = []

        for scenario in scenarios:

            print(f"  Scenario: {scenario['scenario_id']}")

            record = run_strategy_experiment(strategy, scenario)

            scenario_results.append(record)

        # ----------------------------------
        # aggregate scenario performance
        # ----------------------------------

        total_acceptance = sum(
            r["evaluation"]["acceptance_ratio"]
            for r in scenario_results
        )

        avg_acceptance = total_acceptance / len(scenario_results)

        aggregated = {
            "strategy_id": strategy["strategy_id"],
            "scenario_results": scenario_results,
            "evaluation": {
                "avg_acceptance_ratio": avg_acceptance
            }
        }

        # ----------------------------------
        # register strategy in registry
        # ----------------------------------

        register_strategy(
            strategy_id=strategy["strategy_id"],
            generation=generation,
            evaluation=aggregated["evaluation"]
        )

        results.append(aggregated)

    ranked = rank_strategies(results)

    print("\n--- RANKED STRATEGIES ---")

    for r in ranked:

        print(
            r["strategy_id"],
            r["evaluation"]["avg_acceptance_ratio"]
        )

    best = ranked[0]

    print("\nBest strategy:", best["strategy_id"])

    next_generation = genetic_mutation(
        strategies,
        n_mutations=3
    )

    return {
        "ranked_results": ranked,
        "next_generation": next_generation
    }


# ---------------------------------------------------------
# TEST RUN
# ---------------------------------------------------------

if __name__ == "__main__":

    base_strategy = {
        "strategy_id": "base_strategy",
        "domain_id": "trading",
        "action": {
            "type": "BUY",
            "asset": "BTC",
            "quantity": 0.1
        }
    }

    result = run_evolution_cycle(base_strategy)

    print("\nEvolution Result")

    print(json.dumps(result, indent=2))