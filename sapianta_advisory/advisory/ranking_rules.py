from typing import Dict, Any, List


def rank_options(snapshot: Dict[str, Any]) -> List[str]:
    """
    Deterministic ranking.

    Currently minimal:
    - Sort available transitions alphabetically.
    """

    transitions = snapshot.get("available_transitions", [])

    return sorted(transitions)
