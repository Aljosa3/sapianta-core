"""
SAPIANTA Decision Envelope Builder
Creates deterministic decision envelope artifacts.
"""

import hashlib
import json
import uuid
from datetime import datetime


def _hash(data: dict) -> str:
    """Deterministic envelope hash."""
    serialized = json.dumps(data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode()).hexdigest()


def build_decision_envelope(proposal: dict, policy_result: dict) -> dict:
    """
    Build deterministic decision envelope.

    proposal: proposal artifact
    policy_result: result from policy evaluation
    """

    envelope = {
        "decision_id": str(uuid.uuid4()),
        "domain_id": proposal["domain_id"],

        "proposal_reference": {
            "proposal_id": proposal["proposal_id"],
            "strategy_reference": proposal.get("strategy_reference")
        },

        "decision_result": policy_result["decision"],
        "decision_timestamp": datetime.utcnow().isoformat(),

        "policy_trace": policy_result["policy_trace"],

        "action": proposal["action"],
        "risk_context": proposal["risk_context"]
    }

    envelope["envelope_hash"] = _hash(envelope)

    return envelope