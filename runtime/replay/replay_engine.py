"""
SAPIANTA Deterministic Replay Engine

Purpose:
- replay historical decisions
- verify deterministic behavior
- detect divergence between historical and current logic
"""

import json
import hashlib
from pathlib import Path

from runtime.engine.policy_engine import evaluate_policy


LEDGER_PATH = Path("runtime/history/decision_ledger.jsonl")


def _deterministic_hash(data: dict) -> str:
    """Deterministic hash function used across replay."""
    serialized = json.dumps(data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode()).hexdigest()


def load_ledger():
    """Load ledger entries."""
    with open(LEDGER_PATH, "r") as f:
        for line in f:
            yield json.loads(line)


def replay_decision(decision_envelope: dict):
    """
    Replay a single decision.
    """

    proposal_reference = decision_envelope["proposal_reference"]

    # Reconstruct full proposal from envelope fields
    proposal = {
        "proposal_id": proposal_reference["proposal_id"],
        "strategy_reference": proposal_reference.get("strategy_reference"),
        "domain_id": decision_envelope["domain_id"],
        "action": decision_envelope["action"],
        "risk_context": decision_envelope["risk_context"],
    }

    # Re-evaluate policy (deterministic, side-effect free)
    policy_result = evaluate_policy(proposal)

    # Rebuild envelope using ORIGINAL decision_id and decision_timestamp
    # to ensure deterministic replay
    rebuilt_envelope = {
        "decision_id": decision_envelope["decision_id"],
        "domain_id": proposal["domain_id"],
        "proposal_reference": {
            "proposal_id": proposal["proposal_id"],
            "strategy_reference": proposal.get("strategy_reference")
        },
        "decision_result": policy_result["decision"],
        "decision_timestamp": decision_envelope["decision_timestamp"],
        "policy_trace": policy_result["policy_trace"],
        "action": proposal["action"],
        "risk_context": proposal["risk_context"]
    }

    # Compute envelope hash
    replay_hash = _deterministic_hash(rebuilt_envelope)

    stored_hash = decision_envelope["envelope_hash"]

    return {
        "decision_id": decision_envelope["decision_id"],
        "stored_hash": stored_hash,
        "replay_hash": replay_hash,
        "match": stored_hash == replay_hash,
    }


def replay_all():
    """
    Replay entire ledger.
    """

    results = []

    for entry in load_ledger():

        envelope = entry.get("decision_envelope", entry)

        result = replay_decision(envelope)

        results.append(result)

    return results


def replay_by_id(decision_id: str):
    """
    Replay a single decision by id.
    """

    for entry in load_ledger():

        envelope = entry.get("decision_envelope", entry)

        if envelope["decision_id"] == decision_id:
            return replay_decision(envelope)

    raise ValueError(f"Decision {decision_id} not found")


def replay_report():
    """
    Produce replay integrity report.
    """

    results = replay_all()

    total = len(results)
    matches = sum(1 for r in results if r["match"])

    return {
        "total_decisions": total,
        "deterministic_matches": matches,
        "divergence": total - matches,
        "integrity_ratio": matches / total if total else 0,
    }


if __name__ == "__main__":

    report = replay_report()

    print("SAPIANTA Replay Integrity Report")
    print(json.dumps(report, indent=2))