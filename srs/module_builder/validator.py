from typing import Dict, List, Any


def validate_igl(spec: Any) -> Dict[str, Any]:
    """
    Minimal IGL validation placeholder.

    This function does NOT interpret IGL rules.
    It only provides a deterministic PASS result
    with an explicit structure.
    """

    return {
        "ok": True,
        "errors": [],
    }
