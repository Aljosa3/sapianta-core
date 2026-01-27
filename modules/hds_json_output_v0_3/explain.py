from typing import Dict, Any


def explain_on_demand(option: Dict[str, Any]) -> Dict[str, Any]:
    """
    JSON-equivalent Explain-on-Demand.
    Returns explanation only for the requested option.
    """
    return {
        "id": option.get("id"),
        "title": option.get("title"),
        "rationale": option.get("rationale"),
        "consequences": option.get("consequences", []),
        "uncertainty": option.get("uncertainty")
    }
