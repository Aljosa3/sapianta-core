"""Replay-visible conversational bridge evidence."""


def governed_chatgpt_bridge_evidence(*, request: dict, response: dict) -> dict:
    return {
        "original_conversational_input": request.get("conversational_input", ""),
        "normalized_request": response.get("normalized_request"),
        "replay_identity": response.get("replay_identity", ""),
        "normalization_outcome": response.get("status", ""),
        "blocked_ambiguity": response.get("status") == "BLOCKED",
        "downstream_governance_request": response.get("downstream_governance_request"),
        "bridge_boundary_state": response.get("bridge_boundary_state"),
        "closure": response.get("closure", ""),
    }
