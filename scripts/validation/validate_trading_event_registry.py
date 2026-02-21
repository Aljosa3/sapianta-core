#!/usr/bin/env python3
"""
Governance-level validation for TRADING_EVENT_REGISTRY_v0.1.json

Constraints:
- stdlib only
- deterministic (no timestamps, no randomness)
- exit 0 on pass, exit 1 on fail
"""

from __future__ import annotations

import json
import os
import re
import sys
from typing import Any, Dict, List


_UPPER_SNAKE_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")


def _fail(msg: str) -> int:
    sys.stderr.write(msg.rstrip() + "\n")
    return 1


def load_registry(registry_path: str) -> Dict[str, Any]:
    with open(registry_path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_registry_data(registry: Dict[str, Any]) -> None:
    if not isinstance(registry, dict):
        raise ValueError("Registry must be a JSON object (dict).")

    events = registry.get("events")
    if not isinstance(events, list):
        raise ValueError("Registry must contain 'events' as a list.")

    seen: set[str] = set()

    for i, ev in enumerate(events):
        if not isinstance(ev, dict):
            raise ValueError(f"Event at index {i} must be an object.")

        name = ev.get("event_name")
        if not isinstance(name, str) or not name:
            raise ValueError(f"Event at index {i} must have non-empty string 'event_name'.")

        if not _UPPER_SNAKE_RE.match(name):
            raise ValueError(f"event_name '{name}' violates UPPER_SNAKE_CASE pattern.")

        if name in seen:
            raise ValueError(f"Duplicate event_name detected: {name}")
        seen.add(name)

        version = ev.get("version")
        if not isinstance(version, str) or not version:
            raise ValueError(f"Event '{name}' must have non-empty string 'version'.")

        required_fields = ev.get("required_fields")
        optional_fields = ev.get("optional_fields")

        if not isinstance(required_fields, list):
            raise ValueError(f"Event '{name}': required_fields must be a list.")
        if not isinstance(optional_fields, list):
            raise ValueError(f"Event '{name}': optional_fields must be a list.")

        for field_list_name, field_list in (("required_fields", required_fields), ("optional_fields", optional_fields)):
            for j, field in enumerate(field_list):
                if not isinstance(field, str) or not field:
                    raise ValueError(f"Event '{name}': {field_list_name}[{j}] must be a non-empty string.")


def main(argv: List[str]) -> int:
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    default_path = os.path.join(
        repo_root, "governance", "domains", "trading", "TRADING_EVENT_REGISTRY_v0.1.json"
    )
    registry_path = argv[1] if len(argv) > 1 else default_path

    try:
        registry = load_registry(registry_path)
        validate_registry_data(registry)
    except Exception as e:
        return _fail(f"[TRADING_REGISTRY_VALIDATE] FAIL: {e}")

    sys.stdout.write("[TRADING_REGISTRY_VALIDATE] PASS\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))