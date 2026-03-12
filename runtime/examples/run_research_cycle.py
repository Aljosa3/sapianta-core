from runtime.research.idea_engine import IdeaEngine
from runtime.research.experiment_engine import ExperimentEngine
from runtime.research.evaluation_engine import EvaluationEngine
from runtime.evolution.evolution_engine import EvolutionEngine

from runtime.examples.simple_strategy import simple_strategy


idea_engine = IdeaEngine()
experiment_engine = ExperimentEngine(simple_strategy)
evaluation_engine = EvaluationEngine()
evolution_engine = EvolutionEngine()


# ------------------------------------------------------------
# STEP 1 IDEA
# ------------------------------------------------------------

idea = idea_engine.generate_idea()

strategy = {
    "type": "momentum",
    "threshold": 100
}

idea["strategy"] = strategy

print("\nIDEA:")
print(idea)


# ------------------------------------------------------------
# STEP 2 EXPERIMENT
# ------------------------------------------------------------

dataset = [120, 130, 110, 140]

result = experiment_engine.run_experiment(dataset)

print("\nEXPERIMENT:")
print(result)

# ------------------------------------------------------------
# STEP 3 EVALUATION
# ------------------------------------------------------------

evaluation = evaluation_engine.evaluate(result)

evaluation["strategy"] = strategy

print("\nEVALUATION:")
print(evaluation)


# ------------------------------------------------------------
# STEP 4 EVOLUTION
# ------------------------------------------------------------

ranked = evolution_engine.rank([evaluation])

new_strategy = evolution_engine.generate_new(ranked)

print("\nNEW STRATEGY:")
print(new_strategy)