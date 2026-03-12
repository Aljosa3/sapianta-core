"""
SAPIANTA Strategy Mutation Engine

Generates new strategies by mutating successful ones.
"""

import random


class StrategyMutationEngine:

    def mutate(self, strategy, count=10):

        base_threshold = strategy["threshold"]

        mutations = []

        for _ in range(count):

            delta = random.randint(-5, 5)

            new_threshold = base_threshold + delta

            new_strategy = {
                "type": strategy["type"],
                "threshold": new_threshold
            }

            mutations.append(new_strategy)

        return mutations