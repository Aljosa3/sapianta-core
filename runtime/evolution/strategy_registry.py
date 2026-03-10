"""
SAPIANTA Strategy Registry

Purpose
-------
Persistent registry of evaluated strategies.

Stores experiment outcomes and strategy metadata
to enable long-term evolution and promotion.
"""

import json
from pathlib import Path
from datetime import datetime, UTC


REGISTRY_PATH = Path("runtime/history/strategy_registry.jsonl")


def _write_record(record: dict):
    """Append strategy record."""
    with open(REGISTRY_PATH, "a") as f:
        f.write(json.dumps(record) + "\n")


def register_strategy(strategy_id: str, generation: int, evaluation: dict):
    """
    Register strategy evaluation result.
    """

    record = {
        "strategy_id": strategy_id,
        "generation": generation,
        "timestamp": datetime.now(UTC).isoformat(),
        "evaluation": evaluation,
        "promoted": False
    }

    _write_record(record)

    return record


def load_registry():
    """Load registry entries."""

    if not REGISTRY_PATH.exists():
        return []

    entries = []

    with open(REGISTRY_PATH) as f:
        for line in f:
            entries.append(json.loads(line))

    return entries


def best_strategies(limit: int = 5):
    """
    Return best strategies by acceptance_ratio.
    """

    entries = load_registry()

    ranked = sorted(
        entries,
        key=lambda x: x["evaluation"]["acceptance_ratio"],
        reverse=True
    )

    return ranked[:limit]