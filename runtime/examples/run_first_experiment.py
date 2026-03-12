from runtime.research.idea_engine import IdeaEngine
from runtime.research.experiment_engine import ExperimentEngine
from runtime.research.evaluation_engine import EvaluationEngine
from runtime.examples.simple_strategy import simple_momentum


def main():

    dataset = [95, 102, 110, 98, 120, 130, 90]

    idea_engine = IdeaEngine()
    idea = idea_engine.generate_idea()

    print("IDEA GENERATED:")
    print(idea)

    experiment_engine = ExperimentEngine(simple_momentum)
    result = experiment_engine.run_experiment(dataset)

    print("\nEXPERIMENT RESULT:")
    print(result)

    evaluation_engine = EvaluationEngine()
    evaluation = evaluation_engine.evaluate(result)

    print("\nEVALUATION:")
    print(evaluation)


if __name__ == "__main__":
    main()
