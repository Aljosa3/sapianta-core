"""
SAPIANTA Strategy Promotion Engine

Purpose
-------
Promotes validated research strategies to production.

Flow
----
evaluation → validation → production strategy
"""

import json
import os
from datetime import datetime


PRODUCTION_PATH = "runtime/production/current_strategy.json"


# ------------------------------------------------------------
# VALIDATION RULES
# ------------------------------------------------------------

def validate_strategy(evaluation: dict) -> bool:

    metrics = evaluation["evaluation"]

    profit = metrics.get("profit", 0)
    trade_count = metrics.get("trade_count", 0)

    # basic safety rules
    if profit <= 0:
        return False

    if trade_count < 3:
        return False

    return True


# ------------------------------------------------------------
# PROMOTION
# ------------------------------------------------------------

def promote_strategy(strategy: dict, evaluation: dict):

    if not validate_strategy(evaluation):

        print("Strategy failed validation. Not promoted.")
        return False

    os.makedirs(os.path.dirname(PRODUCTION_PATH), exist_ok=True)

    production_record = {
        "timestamp": datetime.utcnow().isoformat(),
        "strategy": strategy,
        "evaluation": evaluation["evaluation"]
    }

    with open(PRODUCTION_PATH, "w") as f:
        json.dump(production_record, f, indent=2)

    print("Strategy promoted to production.")

    return True


# ------------------------------------------------------------
# LOAD CURRENT STRATEGY
# ------------------------------------------------------------

def load_current_strategy():

    if not os.path.exists(PRODUCTION_PATH):
        return None

    with open(PRODUCTION_PATH) as f:
        return json.load(f)


# ------------------------------------------------------------
# DEBUG
# ------------------------------------------------------------

if __name__ == "__main__":

    print("Current production strategy:")

    strategy = load_current_strategy()

    print(strategy)