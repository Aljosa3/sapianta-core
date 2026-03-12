"""
SAPIANTA Strategy Evolution Engine

Purpose
-------
Generate new strategy candidates based on
previous experiment evaluations.

Initial implementation performs:

• ranking
• mutation
• new strategy generation
"""

import random


class EvolutionEngine:

    def __init__(self):
        pass

    # ------------------------------------------------------------
    # RANK STRATEGIES
    # ------------------------------------------------------------

    def rank(self, evaluations):

        """
        Sort strategies by score
        """

        return sorted(
            evaluations,
            key=lambda x: x["evaluation"]["score"],
            reverse=True
        )

    # ------------------------------------------------------------
    # MUTATION
    # ------------------------------------------------------------

    def mutate(self, strategy):

        """
        Simple mutation of strategy parameters
        """

        mutated = strategy.copy()

        # example parameter mutation
        if "threshold" in mutated:
            mutated["threshold"] += random.choice([-1, 1])

        return mutated

    # ------------------------------------------------------------
    # GENERATE NEW STRATEGIES
    # ------------------------------------------------------------

    def generate_new(self, ranked_evaluations):

        """
        Produce next generation strategies
        """

        best = ranked_evaluations[0]

        base_strategy = best["strategy"]

        new_strategy = self.mutate(base_strategy)

        return new_strategy