from typing import Dict, Any


def compute_confidence(snapshot: Dict[str, Any]) -> float:
    """
    Deterministic confidence score.

    Rule:
    - If state is terminal → 1.0
    - Else → 0.5
    """

    if snapshot.get("is_terminal"):
        return 1.0

    return 0.5
