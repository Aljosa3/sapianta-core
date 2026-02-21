# PATH: runtime/interaction_flow.py

def interaction_flow(guarded_output: dict) -> dict:
    """
    HDS Interaction Flow v0.1 — human-in-the-loop.
    """

    return {
        "interaction_state": "AWAITING_HUMAN_DECISION",
        "message": "System does not choose. Select an option or request details.",
        "data": guarded_output,
    }
