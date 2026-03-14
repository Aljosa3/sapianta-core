"""
SAPIANTA Generation Manager

Population-based strategy evolution.

Pipeline

generate population
↓
run experiments
↓
score strategies
↓
select best
↓
mutate
↓
next generation
"""

import random

from runtime.research.strategy_optimizer import (
    generate_random_strategy,
    mutate_strategy,
)
from runtime.research.experiment_runner import run_experiment
from runtime.research.strategy_registry import StrategyRegistry


class GenerationManager:

    def __init__(self, population_size=20, survivors=5):

        self.population_size = population_size
        self.survivors = survivors
        self.registry = StrategyRegistry()

    # ---------------------------------------------------------
    # CREATE INITIAL POPULATION
    # ---------------------------------------------------------

    def create_population(self):

        population = []

        for _ in range(self.population_size):

            strategy = generate_random_strategy()

            population.append(strategy)

        return population

    # ---------------------------------------------------------
    # EVALUATE POPULATION
    # ---------------------------------------------------------

    def evaluate_population(self, population):

        results = []

        for strategy in population:

            result = run_experiment(strategy)

            score = result["metrics"]["total_profit"]

            self.registry.register(strategy.__name__, score)

            results.append((strategy, score))

        return results

    # ---------------------------------------------------------
    # SELECT BEST STRATEGIES
    # ---------------------------------------------------------

    def select_survivors(self, evaluated):

        evaluated.sort(key=lambda x: x[1], reverse=True)

        survivors = evaluated[: self.survivors]

        return [s[0] for s in survivors]

    # ---------------------------------------------------------
    # GENERATE NEXT GENERATION
    # ---------------------------------------------------------

    def generate_next_generation(self, survivors):

        new_population = []

        # keep survivors
        new_population.extend(survivors)

        # mutate survivors to fill population
        while len(new_population) < self.population_size:

            parent = random.choice(survivors)

            child = mutate_strategy(parent)

            new_population.append(child)

        return new_population

    # ---------------------------------------------------------
    # RUN GENERATIONS
    # ---------------------------------------------------------

    def evolve(self, generations=10):

        population = self.create_population()

        best_strategy = None
        best_score = -999999

        for g in range(generations):

            print(f"\nGeneration {g}")

            evaluated = self.evaluate_population(population)

            for strategy, score in evaluated:

                print(strategy.__name__, score)

                if score > best_score:

                    best_score = score
                    best_strategy = strategy

            survivors = self.select_survivors(evaluated)

            population = self.generate_next_generation(survivors)

        print("\nBest strategy overall:")
        print(best_strategy.__name__, best_score)

        return best_strategy


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    manager = GenerationManager(population_size=20, survivors=5)

    manager.evolve(generations=10)