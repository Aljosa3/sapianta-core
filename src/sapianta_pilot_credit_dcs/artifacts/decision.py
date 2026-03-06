from ..core.hashing import artifact_hash
from ..core.authority import validate_action

def build_decision(proposal_hash, advisory, authority_policy,
                   signature, human_override=False, outcome=None, reason=""):

    role = signature["role"]

    validate_action(authority_policy, role, "issue_decision")

    expected = "APPROVED" if advisory["payload"]["recommendation"] == "APPROVE" else "REJECTED"

    if not human_override:
        final = expected
    else:
        validate_action(authority_policy, role, "override_decision")
        if outcome is None:
            raise ValueError("Override requires outcome.")
        if outcome != expected and not reason.strip():
            raise ValueError("Override changing outcome requires reason.")
        final = outcome

    base = {
        "artifact_type": "DECISION",
        "artifact_version": "1.0",
        "payload": {
            "proposal_hash": proposal_hash,
            "advisory_hash": advisory["hash"],
            "authority_policy_hash": authority_policy["hash"],
            "outcome": final,
            "human_override": human_override,
            "reasoning_summary": reason,
            "signature": signature
        }
    }

    base["hash"] = artifact_hash(base)
    return base
