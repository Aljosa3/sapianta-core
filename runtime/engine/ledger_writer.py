"""
SAPIANTA Ledger Writer

Append-only tamper-evident decision ledger.
"""

import json
import hashlib
import os
from datetime import datetime


LEDGER_PATH = "runtime/history/decision_ledger.jsonl"


def _hash(data: dict) -> str:
    serialized = json.dumps(data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode()).hexdigest()


def _get_previous_hash():
    if not os.path.exists(LEDGER_PATH):
        return None

    with open(LEDGER_PATH, "r") as f:
        lines = f.readlines()

    if not lines:
        return None

    last_entry = json.loads(lines[-1])
    return last_entry["entry_hash"]


def write_ledger_entry(envelope: dict):

    previous_hash = _get_previous_hash()

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "decision_envelope": envelope,
        "previous_hash": previous_hash
    }

    entry_hash = _hash(entry)

    entry["entry_hash"] = entry_hash

    os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)

    with open(LEDGER_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")

    return entry