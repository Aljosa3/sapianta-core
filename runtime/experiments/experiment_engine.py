"""
SAPIANTA Experiment Engine

Purpose
-------
Execute deterministic experiments on candidate strategies.

The engine:

1. generates candidate decisions
2. runs them through the decision spine
3. records outcomes
4. evaluates experiment performance

This creates a safe experimentation layer on top of the decision runtime.
"""

import uuid
import json
from datetime import datetime, UTC
from pathlib import Path

from runtime.engine.decision_spine import run_decision_pipeline


EXPERIMENT_LOG = Path("runtime/history/experiment_log.jsonl")


def _write_experiment_record(record: dict):
    """Append experiment record to log."""
    with open(EXPERIMENT_LOG, "a") as f:
        f.write(json.dumps(record) + "\n")


def run_experiment(strategy: dict, scenario: dict):
    """
    Execute a single strategy experiment.

    strategy:
        strategy_id
        action template

    scenario:
        market input
    """

    proposal = {
        "proposal_id": str(uuid.uuid4()),
        "domain_id": strategy["domain_id"],
        "timestamp": datetime.now(UTC).isoformat(),
        "strategy_reference": strategy["strategy_id"],
        "action": strategy["action"],
        "risk_context": scenario.get("risk_context", {}),
    }

    envelope = run_decision_pipeline(proposal)

    return envelope


def evaluate_experiment(results: list):
    """
    Evaluate experiment results.
    """

    decisions = len(results)

    accepted = sum(
        1 for r in results if r["decision_result"] == "APPROVE"
    )

    rejected = decisions - accepted

    return {
        "decisions": decisions,
        "accepted": accepted,
        "rejected": rejected,
        "acceptance_ratio": accepted / decisions if decisions else 0
    }


def record_experiment(strategy: dict, scenario: dict, results: list):
    """
    Record experiment run.
    """

    evaluation = evaluate_experiment(results)

    record = {
        "experiment_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "strategy_id": strategy["strategy_id"],
        "scenario": scenario,
        "evaluation": evaluation,
        "decision_ids": [r["decision_id"] for r in results]
    }

    _write_experiment_record(record)

    return record


def run_strategy_experiment(strategy: dict, scenario: dict, runs: int = 5):
    """
    Run full experiment cycle.
    """

    results = []

    for _ in range(runs):

        envelope = run_experiment(strategy, scenario)

        results.append(envelope)

    record = record_experiment(strategy, scenario, results)

    return record


if __name__ == "__main__":

    # simple test strategy

    strategy = {
        "strategy_id": "test_strategy_001",
        "domain_id": "trading",
        "action": {
            "type": "BUY",
            "asset": "BTC",
            "quantity": 0.1
        }
    }

    scenario = {
        "risk_context": {
            "exposure_before": 0.1,
            "exposure_after": 0.2
        }
    }

    result = run_strategy_experiment(strategy, scenario)

    print("SAPIANTA Experiment Result")
    print(json.dumps(result, indent=2))