"""
Decision Ledger

Canonical ledger used by SAPIANTA.
Stores decisions in JSONL format.
"""

import json
import os
from datetime import datetime


LEDGER_PATH = "runtime/history/decision_ledger.jsonl"


def record_decision(price, signal, strategy, domain="trading", asset="BTC"):

    os.makedirs("runtime/history", exist_ok=True)

    action = "BUY" if signal == 1 else "SELL"

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "domain": domain,
        "asset": asset,
        "price": float(price),
        "signal": int(signal),
        "action": action,
        "strategy": strategy,
    }

    with open(LEDGER_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")