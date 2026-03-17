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


# ---------------------------------------------------------
# DETERMINISTIC HASH
# ---------------------------------------------------------

def _deterministic_hash(data: dict) -> str:
    """Deterministic hash function used across replay."""
    serialized = json.dumps(data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode()).hexdigest()


# ---------------------------------------------------------
# LEDGER LOADING
# ---------------------------------------------------------

def load_ledger():
    """Load ledger entries."""
    if not LEDGER_PATH.exists():
        return

    with open(LEDGER_PATH, "r") as f:
        for line in f:
            yield json.loads(line)


# ---------------------------------------------------------
# ENVELOPE VALIDATION
# ---------------------------------------------------------

def _validate_envelope(envelope: dict):
    """
    Minimal deterministic validation.
    Returns (valid, error_message)
    """

    required_fields = [
        "decision_id",
        "domain_id",
        "action",
        "risk_context",
        "decision_timestamp",
        "envelope_hash",
    ]

    for field in required_fields:
        if field not in envelope:
            return False, f"missing_field:{field}"

    return True, None


# ---------------------------------------------------------
# REPLAY SINGLE DECISION
# ---------------------------------------------------------

def replay_decision(decision_envelope: dict):
    """
    Replay a single decision.
    """

    valid, error = _validate_envelope(decision_envelope)

    if not valid:
        return {
            "decision_id": decision_envelope.get("decision_id"),
            "error": error,
            "match": False,
        }

    proposal_reference = decision_envelope.get("proposal_reference")

    if not proposal_reference:
        return {
            "decision_id": decision_envelope.get("decision_id"),
            "error": "missing_proposal_reference",
            "match": False,
        }

    proposal = {
        "proposal_id": proposal_reference.get("proposal_id"),
        "strategy_reference": proposal_reference.get("strategy_reference"),
        "domain_id": decision_envelope["domain_id"],
        "action": decision_envelope["action"],
        "risk_context": decision_envelope["risk_context"],
    }

    policy_result = evaluate_policy(proposal)

    rebuilt_envelope = {
        "decision_id": decision_envelope["decision_id"],
        "domain_id": proposal["domain_id"],
        "proposal_reference": {
            "proposal_id": proposal["proposal_id"],
            "strategy_reference": proposal.get("strategy_reference"),
        },
        "decision_result": policy_result["decision"],
        "decision_timestamp": decision_envelope["decision_timestamp"],
        "policy_trace": policy_result["policy_trace"],
        "action": proposal["action"],
        "risk_context": proposal["risk_context"],
    }

    replay_hash = _deterministic_hash(rebuilt_envelope)
    stored_hash = decision_envelope.get("envelope_hash")

    return {
        "decision_id": decision_envelope["decision_id"],
        "stored_hash": stored_hash,
        "replay_hash": replay_hash,
        "match": stored_hash == replay_hash,
    }


# ---------------------------------------------------------
# REPLAY ENTIRE LEDGER
# ---------------------------------------------------------

def replay_all():
    """
    Replay entire ledger.
    """

    results = []

    for entry in load_ledger():

        envelope = entry.get("decision_envelope", entry)

        # skip legacy log entries that are not SAPIANTA envelopes
        if "decision_id" not in envelope:
            continue

        result = replay_decision(envelope)

        results.append(result)

    return results


# ---------------------------------------------------------
# REPLAY BY DECISION ID
# ---------------------------------------------------------

def replay_by_id(decision_id: str):
    """
    Replay a single decision by id.
    """

    for entry in load_ledger():

        envelope = entry.get("decision_envelope", entry)

        if envelope.get("decision_id") == decision_id:
            return replay_decision(envelope)

    raise ValueError(f"Decision {decision_id} not found")


# ---------------------------------------------------------
# REPLAY REPORT
# ---------------------------------------------------------

def replay_report():
    """
    Produce replay integrity report.
    """

    results = replay_all()

    total = len(results)
    matches = sum(1 for r in results if r.get("match"))

    return {
        "total_decisions": total,
        "deterministic_matches": matches,
        "divergence": total - matches,
        "integrity_ratio": matches / total if total else 0,
    }


# ---------------------------------------------------------
# CLI ENTRY
# ---------------------------------------------------------

if __name__ == "__main__":

    report = replay_report()

    print("SAPIANTA Replay Integrity Report")
    print(json.dumps(report, indent=2))