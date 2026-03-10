"""
SAPIANTA Scenario Engine

Purpose
-------
Generate deterministic evaluation scenarios for strategy experiments.

Design Principles
-----------------
- Deterministic
- Replayable
- Scenario diversity
- Governance compatible

Scenarios simulate different risk environments.
"""

import hashlib
import json


# ---------------------------------------------------------
# DETERMINISTIC HASH SEED
# ---------------------------------------------------------

def deterministic_seed(value: str) -> int:
    """
    Convert string to deterministic numeric seed.
    """
    h = hashlib.sha256(value.encode()).hexdigest()
    return int(h[:8], 16)


# ---------------------------------------------------------
# BASE SCENARIOS
# ---------------------------------------------------------

def generate_base_scenarios():

    """
    Core risk scenarios.
    """

    return [

        {
            "scenario_id": "low_exposure",
            "risk_context": {
                "exposure_before": 0.05,
                "exposure_after": 0.08
            }
        },

        {
            "scenario_id": "moderate_exposure",
            "risk_context": {
                "exposure_before": 0.10,
                "exposure_after": 0.15
            }
        },

        {
            "scenario_id": "high_exposure",
            "risk_context": {
                "exposure_before": 0.20,
                "exposure_after": 0.35
            }
        },

        {
            "scenario_id": "extreme_exposure",
            "risk_context": {
                "exposure_before": 0.30,
                "exposure_after": 0.60
            }
        }

    ]


# ---------------------------------------------------------
# SCENARIO SUITE
# ---------------------------------------------------------

def generate_scenario_suite(strategy_id: str):

    """
    Generate deterministic scenario suite per strategy.

    Ensures reproducibility across runs.
    """

    base = generate_base_scenarios()

    seed = deterministic_seed(strategy_id)

    # deterministic ordering
    ordered = sorted(
        base,
        key=lambda x: deterministic_seed(x["scenario_id"]) ^ seed
    )

    return ordered


# ---------------------------------------------------------
# TEST RUN
# ---------------------------------------------------------

if __name__ == "__main__":

    scenarios = generate_scenario_suite("test_strategy")

    print("Generated Scenario Suite")

    print(json.dumps(scenarios, indent=2))