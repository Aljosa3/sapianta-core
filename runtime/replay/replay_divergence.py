"""
SAPIANTA Replay Divergence Analyzer

Purpose:
- detect differences between stored and replayed decisions
- explain why deterministic replay fails
- support policy and strategy evolution analysis
"""

import json
from runtime.replay.replay_engine import load_ledger
from runtime.engine.policy_engine import evaluate_policy


def _rebuild_envelope(stored_envelope: dict):
    """
    Reconstruct decision envelope using replay logic.
    """

    proposal_reference = stored_envelope["proposal_reference"]

    proposal = {
        "proposal_id": proposal_reference["proposal_id"],
        "strategy_reference": proposal_reference.get("strategy_reference"),
        "domain_id": stored_envelope["domain_id"],
        "action": stored_envelope["action"],
        "risk_context": stored_envelope["risk_context"],
    }

    policy_result = evaluate_policy(proposal)

    rebuilt_envelope = {
        "decision_id": stored_envelope["decision_id"],
        "domain_id": proposal["domain_id"],
        "proposal_reference": {
            "proposal_id": proposal["proposal_id"],
            "strategy_reference": proposal.get("strategy_reference"),
        },
        "decision_result": policy_result["decision"],
        "decision_timestamp": stored_envelope["decision_timestamp"],
        "policy_trace": policy_result["policy_trace"],
        "action": proposal["action"],
        "risk_context": proposal["risk_context"],
    }

    return rebuilt_envelope


def _compare_dicts(stored: dict, rebuilt: dict):
    """
    Compare two envelopes and list differences.
    """

    differences = {}

    for key in set(stored.keys()).union(rebuilt.keys()):

        if key == "envelope_hash":
            continue

        stored_value = stored.get(key)
        rebuilt_value = rebuilt.get(key)

        if stored_value != rebuilt_value:
            differences[key] = {
                "stored": stored_value,
                "replayed": rebuilt_value
            }

    return differences


def analyze_divergence():
    """
    Analyze divergence across entire ledger.
    """

    results = []

    for entry in load_ledger():

        stored_envelope = entry.get("decision_envelope", entry)

        rebuilt_envelope = _rebuild_envelope(stored_envelope)

        differences = _compare_dicts(stored_envelope, rebuilt_envelope)

        results.append({
            "decision_id": stored_envelope["decision_id"],
            "divergence": len(differences) > 0,
            "differences": differences
        })

    return results


def divergence_report():
    """
    Produce divergence report.
    """

    results = analyze_divergence()

    total = len(results)
    divergent = sum(1 for r in results if r["divergence"])

    return {
        "total_decisions": total,
        "divergent_decisions": divergent,
        "consistent_decisions": total - divergent,
        "divergence_ratio": divergent / total if total else 0
    }


if __name__ == "__main__":

    report = divergence_report()

    print("SAPIANTA Replay Divergence Report")
    print(json.dumps(report, indent=2))