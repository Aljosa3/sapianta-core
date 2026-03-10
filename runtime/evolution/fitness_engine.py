"""
SAPIANTA Fitness Engine

Purpose
-------
Evaluate strategy performance using multiple metrics.

Moves evaluation beyond simple policy acceptance.

Fitness considers:
- acceptance ratio
- exposure efficiency
- risk penalty
- strategy stability
"""

import math


# ---------------------------------------------------------
# METRIC EXTRACTION
# ---------------------------------------------------------

def extract_metrics(experiment_record):

    evaluation = experiment_record["evaluation"]

    acceptance_ratio = evaluation.get("acceptance_ratio", 0)

    scenario = experiment_record.get("scenario", {})
    risk_context = scenario.get("risk_context", {})

    exposure_before = risk_context.get("exposure_before", 0)
    exposure_after = risk_context.get("exposure_after", 0)

    exposure_change = exposure_after - exposure_before

    return {
        "acceptance_ratio": acceptance_ratio,
        "exposure_change": exposure_change
    }


# ---------------------------------------------------------
# FITNESS FUNCTION
# ---------------------------------------------------------

def compute_fitness(metrics):

    acceptance = metrics["acceptance_ratio"]
    exposure_change = metrics["exposure_change"]

    # exposure penalty
    exposure_penalty = max(0, exposure_change)

    fitness = (
        acceptance * 1.0
        - exposure_penalty * 0.5
    )

    return fitness


# ---------------------------------------------------------
# EXPERIMENT FITNESS
# ---------------------------------------------------------

def evaluate_experiment_fitness(experiment_record):

    metrics = extract_metrics(experiment_record)

    fitness = compute_fitness(metrics)

    return fitness


# ---------------------------------------------------------
# SCENARIO FITNESS
# ---------------------------------------------------------

def evaluate_scenario_suite(results):

    fitness_values = []

    for record in results:

        fitness = evaluate_experiment_fitness(record)

        fitness_values.append(fitness)

    if not fitness_values:

        return 0

    return sum(fitness_values) / len(fitness_values)


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    test_record = {

        "evaluation": {
            "acceptance_ratio": 0.8
        },

        "scenario": {
            "risk_context": {
                "exposure_before": 0.1,
                "exposure_after": 0.2
            }
        }
    }

    fitness = evaluate_experiment_fitness(test_record)

    print("Fitness:", fitness)