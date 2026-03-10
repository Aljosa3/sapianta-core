"""
SAPIANTA Runtime Risk Guard

Monitors runtime safety conditions and triggers emergency stop signals.
"""

import os
import json
from datetime import datetime, timedelta


LEDGER_PATH = "runtime/history/decision_ledger.jsonl"
SIGNAL_PATH = "runtime/signals/RISK_STOP"


MAX_DECISIONS_PER_MINUTE = 10


def _load_recent_decisions():

    if not os.path.exists(LEDGER_PATH):
        return []

    with open(LEDGER_PATH, "r") as f:
        lines = [json.loads(line) for line in f]

    return lines


def check_decision_frequency():

    decisions = _load_recent_decisions()

    now = datetime.utcnow()
    window_start = now - timedelta(minutes=1)

    recent = []

    for entry in decisions:

        ts = entry.get("timestamp")

        if ts is None:
            continue

        ts = datetime.fromisoformat(ts)

        if ts >= window_start:
            recent.append(entry)

    return len(recent)


def trigger_risk_stop(reason: str):

    os.makedirs("runtime/signals", exist_ok=True)

    with open(SIGNAL_PATH, "w") as f:
        f.write(reason)

    print("RISK STOP TRIGGERED:", reason)


def evaluate_runtime_risk():

    decision_count = check_decision_frequency()

    if decision_count > MAX_DECISIONS_PER_MINUTE:

        trigger_risk_stop(
            f"decision frequency exceeded: {decision_count} decisions/min"
        )

        return False

    return True