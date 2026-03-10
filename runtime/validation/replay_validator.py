"""
SAPIANTA Ledger Replay Validator

Verifies integrity of the decision ledger.
"""

import json
import hashlib


def _hash(data: dict) -> str:
    import json
    serialized = json.dumps(data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode()).hexdigest()


def validate_ledger_chain(ledger_path: str):

    with open(ledger_path, "r") as f:
        entries = [json.loads(line) for line in f]

    previous_hash = None

    for index, entry in enumerate(entries):

        entry_copy = dict(entry)
        stored_hash = entry_copy.pop("entry_hash")

        computed_hash = _hash(entry_copy)

        if computed_hash != stored_hash:
            raise Exception(f"Ledger corruption detected at entry {index}")

        if entry["previous_hash"] != previous_hash:
            raise Exception(f"Ledger chain broken at entry {index}")

        previous_hash = stored_hash

    return True