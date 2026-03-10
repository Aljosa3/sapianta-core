"""
SAPIANTA Strategy Executor

Generates decision proposals from the selected strategy.
"""

from datetime import datetime
import uuid

from runtime.strategies.strategy_selector import select_strategy


def generate_proposal():

    strategy = select_strategy()

    if strategy is None:
        return None

    proposal = {
        "proposal_id": str(uuid.uuid4()),
        "domain_id": "trading",
        "timestamp": datetime.utcnow().isoformat(),

        "strategy_reference": {
            "artifact_id": strategy.get("artifact_id")
        },

        "action": {
            "type": "BUY",
            "asset": "BTC",
            "quantity": 0.1
        },

        "risk_context": {
            "exposure_before": 0.10,
            "exposure_after": 0.11
        }
    }

    return proposal