#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path

REGISTRY_PATH = Path("governance/registry/EVENT_REGISTRY_v0.1.json")

EXCLUDED_DIRS = {
    "governance",
    "tests",
    "scripts/validation",
    "__pycache__"
}

EVENT_PATTERN = re.compile(r'["\'](EVT_[A-Z0-9_]+)["\']')


def load_registry():
    if not REGISTRY_PATH.exists():
        print("L1.1 FAIL: Registry missing.")
        sys.exit(2)

    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    events = data.get("events", [])
    return {e["id"] for e in events if "id" in e}


def should_skip(path):
    return any(part in EXCLUDED_DIRS for part in path.parts)


def main():
    allowed = load_registry()
    violations = []

    for path in Path(".").rglob("*.py"):
        if should_skip(path):
            continue

        content = path.read_text(encoding="utf-8")

        for match in EVENT_PATTERN.findall(content):
            if match not in allowed:
                violations.append(f"{path}: Unknown event literal '{match}'")

    if violations:
        print("L1.1 EVENT REFERENCE VALIDATION: FAIL")
        for v in violations:
            print("-", v)
        sys.exit(2)

    print("L1.1 EVENT REFERENCE VALIDATION: PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
