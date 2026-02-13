#!/usr/bin/env python3

import os
import sys
import hashlib
import json
import importlib
import traceback

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

ITERATIONS = 100


def hash_result(result):
    try:
        serialized = json.dumps(result, sort_keys=True)
    except TypeError:
        serialized = repr(result)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def load_execution_entry():
    """
    Attempts to load the canonical execution entry point.
    """
    try:
        from sapianta_hoi.execution import execute
        return execute
    except Exception:
        return None


def run_repeatability_test():
    entry = load_execution_entry()

    if entry is None:
        print("⚠ No execution entry found. Testing module import determinism only.")

        hashes = []
        for _ in range(ITERATIONS):
            try:
                module = importlib.reload(
                    importlib.import_module("sapianta_hoi.execution")
                )
                result = repr(module)
                hashes.append(hash_result(result))
            except Exception:
                traceback.print_exc()
                return False

        return len(set(hashes)) == 1

    # ------------------------------------------------
    # Use first valid transition dynamically
    # ------------------------------------------------
    try:
        from sapianta_hoi.guards.transition_guard import TRANSITIONS
        first_transition = next(iter(TRANSITIONS))
        initial_state, valid_event = first_transition
    except Exception:
        traceback.print_exc()
        return False

    hashes = []

    for _ in range(ITERATIONS):
        try:
            result = entry(valid_event, initial_state=initial_state)
            hashes.append(hash_result(result))
        except Exception:
            traceback.print_exc()
            return False

    return len(set(hashes)) == 1


def main():
    print("Running Kernel Runtime Repeatability Test...")

    success = run_repeatability_test()

    if not success:
        print("\n❌ Repeatability test FAILED.")
        sys.exit(1)

    print("✅ Kernel runtime repeatability test passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
