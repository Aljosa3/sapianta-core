#!/usr/bin/env python3
"""
Governance-level validation of TRADING_DECISION_TO_INTENT_SPEC_v0.1.md

This validator ensures that the transformation spec
contains all mandatory deterministic governance elements.

No runtime logic.
No parsing beyond structural phrase validation.
"""

import os
import sys


SPEC_PATH = "governance/domains/trading/TRADING_DECISION_TO_INTENT_SPEC_v0.1.md"

REQUIRED_PHRASES = [
    "Deterministic Mapping Rules",
    "intent_id = \"INTENT_\" + decision_id",
    "Prohibited Transformations",
    "Version Binding",
    "Determinism Guarantee",
]


def main():
    if not os.path.exists(SPEC_PATH):
        print("[TRADING_DECISION_TO_INTENT_SPEC_VALIDATE] FAIL: spec file missing")
        return 1

    with open(SPEC_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    for phrase in REQUIRED_PHRASES:
        if phrase not in content:
            print(f"[TRADING_DECISION_TO_INTENT_SPEC_VALIDATE] FAIL: missing '{phrase}'")
            return 1

    print("[TRADING_DECISION_TO_INTENT_SPEC_VALIDATE] PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
