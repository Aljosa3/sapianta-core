"""
SAPIANTA Decision Analytics

Provides basic analytics over the decision ledger.

Design principles:
- deterministic
- read-only
- no runtime side effects
"""

import json
from pathlib import Path
from collections import Counter


LEDGER_PATH = Path("runtime/history/decision_ledger.jsonl")


def load_ledger():
    """
    Loads decision ledger entries.
    """

    if not LEDGER_PATH.exists():
        return []

    entries = []

    with open(LEDGER_PATH, "r") as f:
        for line in f:
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    return entries


def compute_decision_count(entries):
    """
    Total number of decisions.
    """

    return len(entries)


def compute_decision_types(entries):
    """
    Counts decision types (BUY / SELL etc).
    """

    counter = Counter()

    for entry in entries:

        envelope = entry.get("decision_envelope", {})
        action = envelope.get("action", {})
        decision_type = action.get("type")

        if decision_type:
            counter[decision_type] += 1

    return dict(counter)


def compute_asset_usage(entries):
    """
    Counts which assets are used.
    """

    counter = Counter()

    for entry in entries:

        envelope = entry.get("decision_envelope", {})
        action = envelope.get("action", {})
        asset = action.get("asset")

        if asset:
            counter[asset] += 1

    return dict(counter)


def compute_strategy_usage(entries):
    """
    Counts strategies used in decisions.
    """

    counter = Counter()

    for entry in entries:

        envelope = entry.get("decision_envelope", {})
        proposal_ref = envelope.get("proposal_reference", {})

        strategy = proposal_ref.get("strategy_reference")

        if strategy:
            counter[str(strategy)] += 1

    return dict(counter)


def generate_decision_summary():
    """
    Generates overall decision analytics summary.
    """

    entries = load_ledger()

    summary = {
        "decision_count": compute_decision_count(entries),
        "decision_types": compute_decision_types(entries),
        "asset_usage": compute_asset_usage(entries),
        "strategy_usage": compute_strategy_usage(entries),
    }

    return summary


if __name__ == "__main__":

    summary = generate_decision_summary()

    print("SAPIANTA Decision Analytics")
    print(summary)