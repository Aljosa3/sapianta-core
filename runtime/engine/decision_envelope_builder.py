"""
SAPIANTA Decision Envelope Builder
Creates deterministic decision envelope artifacts.
"""

import hashlib
import json
import uuid
from datetime import datetime


def _hash(data: dict) -> str:
    serialized = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(serialized).hexdigest()


def build_decision_envelope(proposal: dict, policy_result: dict) -> dict:

    envelope = {
        "decision_id": str(uuid.uuid4()),
        "domain_id": proposal["domain_id"],

        # Proposal provenance
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