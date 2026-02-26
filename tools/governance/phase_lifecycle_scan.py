#!/usr/bin/env python3

"""
SAPIANTA Phase Lifecycle Validator (V2)

Legacy-tolerant, future-strict model.

Rules:
- LOCK requires INIT (unless legacy)
- COMPLETE requires INIT (unless legacy)
- INIT alone is allowed
- REPORT ignored
- v1.x and above always strict

Exit codes:
0 = PASS
1 = FAIL
"""

import os
import sys
import re

BASE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../governance/phases")
)

FAILURES = []

# 👇 Legacy prefixes (historic model without INIT discipline)
LEGACY_PREFIXES = {
    "v0.3A",
    "HDS_CHAT_SHELL_v0.1",
    "PHASE_v0.20_MULTI_FILE_MODULE",
    "PHASE_EXT-4_SEMANTIC_BOUNDARY",
    "AUDIT_HARNESS_v0.1",
    "v0.20_KERNEL",
    "PHASE_v0.17_OUTPUT_PROTOCOL",
    "PHASE_v0.12_BUILD_PIPELINE_OPERATIONAL",
    "PHASE_v0.13_REAL_CLAUDE_ADAPTER",
    "PHASE_v0.14_WIRING_REAL_ADAPTER",
    "HOI_CLI_ADAPTER_v0.1",
}


def extract_prefix(filename):
    match = re.match(r"(.+?)_(INIT|LOCK|COMPLETE|REPORT)\.md$", filename)
    if match:
        return match.group(1), match.group(2)
    return None, None


def is_strict_prefix(prefix):
    # Strict for v1.x and above
    if prefix.startswith("v1."):
        return True
    return False


def scan():
    phase_map = {}

    for root, _, files in os.walk(BASE_PATH):
        for f in files:
            if f.endswith(".md"):
                prefix, state = extract_prefix(f)
                if prefix:
                    if prefix not in phase_map:
                        phase_map[prefix] = set()
                    phase_map[prefix].add(state)

    for prefix, states in phase_map.items():

        strict_mode = is_strict_prefix(prefix)

        # Legacy handling
        if prefix in LEGACY_PREFIXES:
            continue

        # LOCK requires INIT (strict or normal)
        if "LOCK" in states and "INIT" not in states:
            FAILURES.append(
                f"Orphan LOCK without INIT: {prefix}"
            )

        # COMPLETE requires INIT
        if "COMPLETE" in states and "INIT" not in states:
            FAILURES.append(
                f"COMPLETE without INIT: {prefix}"
            )


def main():
    print("SAPIANTA PHASE LIFECYCLE VALIDATOR (V2)")
    print("---------------------------------------")
    print(f"Scanning: {BASE_PATH}\n")

    scan()

    if FAILURES:
        print("❌ FAILURES DETECTED:\n")
        for f in FAILURES:
            print(f" - {f}")
        sys.exit(1)
    else:
        print("✅ PASS: Phase lifecycle structure valid (legacy tolerated, future strict).")
        sys.exit(0)


if __name__ == "__main__":
    main()