"""
SAPIANTA Strategy Registry

Stores strategies that were approved through the Promotion Gate.
"""

import json
import os
import hashlib
from datetime import datetime


STRATEGY_REGISTRY_PATH = "runtime/history/strategy_registry.jsonl"


def _hash(data: dict) -> str:
    serialized = json.dumps(data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode()).hexdigest()


def register_strategy(strategy: dict):
    """
    Register a new runtime strategy.
    """

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "strategy": strategy
    }

    entry_hash = _hash(entry)

    entry["strategy_hash"] = entry_hash

    os.makedirs(os.path.dirname(STRATEGY_REGISTRY_PATH), exist_ok=True)

    with open(STRATEGY_REGISTRY_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")

    return entry


def load_strategies():
    """
    Load all registered strategies.
    """

    if not os.path.exists(STRATEGY_REGISTRY_PATH):
        return []

    with open(STRATEGY_REGISTRY_PATH, "r") as f:
        entries = [json.loads(line) for line in f]

    return [entry["strategy"] for entry in entries]