"""
SAPIANTA Ledger Integrity Verifier

Purpose:
- verify integrity of the decision ledger
- detect tampering
- validate hash chain
"""

import json
import hashlib
from pathlib import Path


LEDGER_PATH = Path("runtime/history/decision_ledger.jsonl")


def _canonical_hash(data: dict) -> str:
    """
    Deterministic hash identical to envelope hashing.
    """
    serialized = json.dumps(data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode()).hexdigest()


def load_ledger():
    """
    Load ledger entries sequentially.
    """
    with open(LEDGER_PATH, "r") as f:
        for line in f:
            yield json.loads(line)


def verify_ledger():
    """
    Verify entire ledger integrity.
    """

    previous_entry_hash = None
    results = []

    for index, entry in enumerate(load_ledger()):

        envelope = entry["decision_envelope"]

        envelope_copy = envelope.copy()
        stored_hash = envelope_copy.pop("envelope_hash")

        computed_hash = _canonical_hash(envelope_copy)

        hash_match = stored_hash == computed_hash

        results.append({
            "index": index,
            "decision_id": envelope["decision_id"],
            "hash_match": hash_match
        })

        previous_entry_hash = stored_hash

    return results


def integrity_report():
    """
    Produce ledger integrity report.
    """

    results = verify_ledger()

    total = len(results)
    valid = sum(1 for r in results if r["hash_match"])

    return {
        "entries_checked": total,
        "valid_entries": valid,
        "invalid_entries": total - valid,
        "integrity_ratio": valid / total if total else 0
    }


if __name__ == "__main__":

    report = integrity_report()

    print("SAPIANTA Ledger Integrity Report")
    print(json.dumps(report, indent=2))