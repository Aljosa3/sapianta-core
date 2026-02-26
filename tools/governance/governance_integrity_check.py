#!/usr/bin/env python3

"""
SAPIANTA Governance Integrity Gate

Runs:
- Lock Pair Validator (V3)
- Phase Lifecycle Validator (V2)

Exit codes:
0 = PASS
1 = FAIL
"""

import subprocess
import sys
import os

BASE_DIR = os.path.dirname(__file__)

LOCK_PAIR = os.path.join(BASE_DIR, "lock_pair_scan.py")
PHASE_SCAN = os.path.join(BASE_DIR, "phase_lifecycle_scan.py")


def run(script):
    result = subprocess.run(
        ["python3", script],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print(result.stderr)
        return False

    return True


def main():
    print("=====================================")
    print("SAPIANTA GOVERNANCE INTEGRITY CHECK")
    print("=====================================\n")

    ok_lock = run(LOCK_PAIR)
    ok_phase = run(PHASE_SCAN)

    if ok_lock and ok_phase:
        print("\n✅ GOVERNANCE INTEGRITY: PASS")
        sys.exit(0)
    else:
        print("\n❌ GOVERNANCE INTEGRITY: FAIL")
        sys.exit(1)


if __name__ == "__main__":
    main()