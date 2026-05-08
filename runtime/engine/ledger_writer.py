"""
SAPIANTA Ledger Writer

Append-only tamper-evident decision ledger.
"""

import json
import hashlib
import os
import fcntl
from datetime import datetime


LEDGER_PATH = "runtime/history/decision_ledger.jsonl"
RISK_STOP_PATH = "runtime/signals/RISK_STOP"


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


def _previous_hash_from_lines(lines):
    if not lines:
        return None
    last_entry = json.loads(lines[-1])
    return last_entry["entry_hash"]


def _assert_no_risk_stop():
    if os.path.exists(RISK_STOP_PATH):
        raise RuntimeError("Risk stop is active; refusing to append decision ledger entry")


def write_ledger_entry(envelope: dict):

    _assert_no_risk_stop()
    os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)

    with open(LEDGER_PATH, "a+", encoding="utf-8") as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        try:
            f.seek(0)
            previous_hash = _previous_hash_from_lines(f.readlines())

            entry = {
                "timestamp": envelope.get(
                    "decision_timestamp",
                    datetime.utcnow().isoformat()
                ),
                "decision_envelope": envelope,
                "previous_hash": previous_hash
            }

            entry_hash = _hash(entry)

            entry["entry_hash"] = entry_hash

            f.write(json.dumps(entry, sort_keys=True) + "\n")
            f.flush()
            os.fsync(f.fileno())
        finally:
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)


    return entry
