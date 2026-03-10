"""
SAPIANTA Genome Population Engine

Purpose
-------
Manage evolutionary populations of strategy genomes.

Provides:
- population initialization
- evaluation
- selection
- mutation
- crossover
- next generation creation
"""

import random
import json

from runtime.evolution.strategy_genome import (
    create_random_genome,
    mutate_genome,
    crossover,
    genome_to_strategy
)

from runtime.experiments.experiment_engine import run_strategy_experiment
from runtime.scenarios.scenario_engine import generate_scenario_suite

from runtime.evolution.fitness_engine import evaluate_scenario_suite


# ---------------------------------------------------------
# POPULATION INITIALIZATION
# ---------------------------------------------------------

def initialize_population(size=10):

    population = []

    for _ in range(size):

        genome = create_random_genome()

        population.append(genome)

    return population


# ---------------------------------------------------------
# FITNESS EVALUATION
# ---------------------------------------------------------

def evaluate_genome(genome):

    strategy = genome_to_strategy(genome)

    scenarios = generate_scenario_suite(strategy["strategy_id"])

    results = []

    for scenario in scenarios:

        record = run_strategy_experiment(strategy, scenario)

        results.append(record)

    # NEW FITNESS ENGINE
    fitness = evaluate_scenario_suite(results)

    return fitness


# ---------------------------------------------------------
# POPULATION EVALUATION
# ---------------------------------------------------------

def evaluate_population(population):

    evaluated = []

    for genome in population:

        print(f"Evaluating genome {genome['genome_id']}")

        fitness = evaluate_genome(genome)

        evaluated.append({
            "genome": genome,
            "fitness": fitness
        })

    return evaluated


# ---------------------------------------------------------
# SELECTION
# ---------------------------------------------------------

def select_top(evaluated, top_k=3):

    ranked = sorted(
        evaluated,
        key=lambda x: x["fitness"],
        reverse=True
    )

    return ranked[:top_k]


# ---------------------------------------------------------
# NEXT GENERATION
# ---------------------------------------------------------

def create_next_generation(selected, population_size=10):

    next_population = []

    parents = [s["genome"] for s in selected]

    # keep best genomes
    next_population.extend(parents)

    while len(next_population) < population_size:

        parent_a = random.choice(parents)
        parent_b = random.choice(parents)

        child = crossover(parent_a, parent_b)

        if random.random() < 0.5:

            child = mutate_genome(child)

        next_population.append(child)

    return next_population


# ---------------------------------------------------------
# FULL EVOLUTION RUN
# ---------------------------------------------------------

def run_evolution(generations=3, population_size=10):

    population = initialize_population(population_size)

    for generation in range(generations):

        print(f"\n=== GENERATION {generation} ===")

        evaluated = evaluate_population(population)

        selected = select_top(evaluated)

        print("\nTop genomes:")

        for s in selected:

            print(s["genome"]["genome_id"], s["fitness"])

        population = create_next_generation(
            selected,
            population_size
        )

    return population


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    final_population = run_evolution(
        generations=2,
        population_size=6
    )

    print("\nFinal population:")

    print(json.dumps(final_population, indent=2))