"""
SAPIANTA Research Orchestrator

Coordinates the autonomous research loop.
"""

import time

from runtime.research.idea_engine import IdeaEngine
from runtime.research.experiment_engine import ExperimentEngine
from runtime.research.evaluation_engine import EvaluationEngine
from runtime.evolution.evolution_engine import EvolutionEngine

from runtime.examples.simple_strategy import simple_strategy


class ResearchOrchestrator:

    def __init__(self):

        self.idea_engine = IdeaEngine()
        self.experiment_engine = ExperimentEngine(simple_strategy)
        self.evaluation_engine = EvaluationEngine()
        self.evolution_engine = EvolutionEngine()

    def run_cycle(self):

        # IDEA
        idea = self.idea_engine.generate_idea()

        strategy = {
            "type": "momentum",
            "threshold": 100
        }

        idea["strategy"] = strategy

        print("\nIDEA:")
        print(idea)

        # EXPERIMENT DATA
        dataset = [120, 130, 110, 140]

        result = self.experiment_engine.run_experiment(dataset)

        print("\nEXPERIMENT:")
        print(result)

        # EVALUATION
        evaluation = self.evaluation_engine.evaluate(result)

        evaluation["strategy"] = strategy

        print("\nEVALUATION:")
        print(evaluation)

        # EVOLUTION
        ranked = self.evolution_engine.rank([evaluation])

        new_strategy = self.evolution_engine.generate_new(ranked)

        print("\nNEW STRATEGY:")
        print(new_strategy)

        return new_strategy

    def run(self, cycles=10, delay=1):

        strategy = None

        for i in range(cycles):

            print("\n==============================")
            print(f"RESEARCH CYCLE {i+1}")
            print("==============================")

            strategy = self.run_cycle()

            time.sleep(delay)

        print("\nResearch completed.")


if __name__ == "__main__":

    orchestrator = ResearchOrchestrator()

    orchestrator.run(cycles=5)