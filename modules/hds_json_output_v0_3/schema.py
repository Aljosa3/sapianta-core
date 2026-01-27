from typing import List, Dict, Any


def hds_json_schema(options: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Deterministic JSON-safe envelope.
    No ranking, no implicit authority.
    """
    return {
        "options": options,
        "meta": {
            "version": "hds-json-output-v0.3",
            "disclaimer": "Decision authority rests solely with the human operator."
        }
    }
