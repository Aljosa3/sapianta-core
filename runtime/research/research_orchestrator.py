"""
SAPIANTA Research Orchestrator

Coordinates the autonomous research loop
and registers artifacts in the Artifact Registry.

Now supports:
- Research Queue
- Strategy Memory
"""

import time

from runtime.research.idea_engine import IdeaEngine
from runtime.research.experiment_engine import ExperimentEngine
from runtime.research.evaluation_engine import EvaluationEngine
from runtime.evolution.evolution_engine import EvolutionEngine

from runtime.artifacts.artifact_registry import register_artifact
from runtime.production.strategy_promotion_engine import promote_strategy

from runtime.memory.strategy_memory import StrategyMemory

from runtime.examples.simple_strategy import simple_strategy


class ResearchOrchestrator:

    def __init__(self):

        self.idea_engine = IdeaEngine()
        self.experiment_engine = ExperimentEngine(simple_strategy)
        self.evaluation_engine = EvaluationEngine()
        self.evolution_engine = EvolutionEngine()

        # NEW
        self.memory = StrategyMemory()

    # ------------------------------------------------
    # GENERATE IDEAS
    # ------------------------------------------------

    def generate_ideas(self, count=20):

        ideas = []
        attempts = 0

        while len(ideas) < count and attempts < count * 5:

            attempts += 1

            idea = self.idea_engine.generate_idea()

            strategy = {
                "type": "momentum",
                "threshold": 100
            }

            idea["strategy"] = strategy

            # -----------------------------------------
            # CHECK MEMORY
            # -----------------------------------------

            if self.memory.exists(strategy):
                continue

            artifact = register_artifact(
                artifact_type="idea",
                domain_id="research",
                artifact_location="runtime/research",
                producer="IdeaEngine",
                metadata=idea
            )

            idea["artifact_id"] = artifact["artifact_id"]

            ideas.append(idea)

        return ideas

    # ------------------------------------------------
    # RUN EXPERIMENTS
    # ------------------------------------------------

    def run_experiments(self, ideas):

        results = []

        dataset = [120, 130, 110, 140]

        for idea in ideas:

            strategy = idea["strategy"]

            result = self.experiment_engine.run_experiment(dataset)

            artifact = register_artifact(
                artifact_type="experiment",
                domain_id="research",
                artifact_location="runtime/research",
                producer="ExperimentEngine",
                metadata={
                    "idea_id": idea["artifact_id"],
                    "dataset": dataset,
                    "result": result
                }
            )

            results.append({
                "idea": idea,
                "experiment_result": result,
                "artifact_id": artifact["artifact_id"]
            })

        return results

    # ------------------------------------------------
    # EVALUATE STRATEGIES
    # ------------------------------------------------

    def evaluate_results(self, experiments):

        evaluations = []

        for exp in experiments:

            evaluation = self.evaluation_engine.evaluate(exp["experiment_result"])

            strategy = exp["idea"]["strategy"]

            evaluation["strategy"] = strategy

            artifact = register_artifact(
                artifact_type="evaluation",
                domain_id="research",
                artifact_location="runtime/research",
                producer="EvaluationEngine",
                metadata={
                    "experiment_id": exp["artifact_id"],
                    "evaluation": evaluation,
                    "strategy": strategy
                }
            )

            evaluations.append(evaluation)

        return evaluations

    # ------------------------------------------------
    # EVOLVE STRATEGIES
    # ------------------------------------------------

    def evolve_strategies(self, evaluations):

        ranked = self.evolution_engine.rank(evaluations)

        best = ranked[0]

        new_strategy = self.evolution_engine.generate_new(ranked)

        artifact = register_artifact(
            artifact_type="strategy",
            domain_id="research",
            artifact_location="runtime/research",
            producer="EvolutionEngine",
            metadata={
                "source_strategy": best["strategy"],
                "new_strategy": new_strategy
            }
        )

        return new_strategy, best

    # ------------------------------------------------
    # RESEARCH CYCLE
    # ------------------------------------------------

    def run_cycle(self):

        print("\nGenerating ideas...")

        ideas = self.generate_ideas(20)

        print(f"{len(ideas)} ideas generated")

        print("\nRunning experiments...")

        experiments = self.run_experiments(ideas)

        print("\nEvaluating results...")

        evaluations = self.evaluate_results(experiments)

        print("\nRanking strategies...")

        new_strategy, best_eval = self.evolve_strategies(evaluations)

        # -----------------------------------------
        # REGISTER IN MEMORY
        # -----------------------------------------

        self.memory.register(new_strategy, best_eval)

        print("\nBEST STRATEGY FOUND:")
        print(new_strategy)

        promote_strategy(new_strategy, best_eval)

        return new_strategy

    # ------------------------------------------------
    # LOOP
    # ------------------------------------------------

    def run(self, cycles=10, delay=1):

        strategy = None

        for i in range(cycles):

            print("\n==============================")
            print(f"RESEARCH CYCLE {i+1}")
            print("==============================")

            strategy = self.run_cycle()

            time.sleep(delay)

        print("\nResearch completed.")


# ------------------------------------------------
# AUTO RESEARCH TRIGGER ENTRYPOINT
# ------------------------------------------------

def run_research_cycle():

    orchestrator = ResearchOrchestrator()

    orchestrator.run(cycles=1)


if __name__ == "__main__":

    orchestrator = ResearchOrchestrator()

    orchestrator.run(cycles=5)