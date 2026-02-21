"""
Deterministic Decision → Intent transformer
TRADING v0.5
"""

from __future__ import annotations

from typing import Dict, Any


def transform_decision_to_intent(decision: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deterministic mapping according to:
    TRADING_DECISION_TO_INTENT_SPEC_v0.1
    """

    required_fields = ["decision_id", "action", "symbol", "timeframe"]

    for field in required_fields:
        if field not in decision:
            raise ValueError(f"Missing required field: {field}")

    intent = {
        "intent_id": "INTENT_" + decision["decision_id"],
        "decision_id": decision["decision_id"],
        "action": decision["action"],
        "symbol": decision["symbol"],
        "timeframe": decision["timeframe"],
    }

    if "rationale" in decision:
        intent["notes"] = decision["rationale"]

    return intent