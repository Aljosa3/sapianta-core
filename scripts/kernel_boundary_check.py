#!/usr/bin/env python3

"""
Kernel Boundary Auto-Check Script
----------------------------------

Enforces namespace whitelist freeze for HOI Kernel v1.x.

This script verifies that only approved top-level namespaces
exist under sapianta_hoi/.

If any additional namespace appears, the script exits with
non-zero status.

Deterministic.
No external dependencies.
"""

import os
import sys


# Whitelisted namespaces aligned with
# KERNEL_PUBLIC_SURFACE_SNAPSHOT_v1.0.md (v1.1 freeze state)
ALLOWED_NAMESPACES = {
    "runtime_stub",
    "execution",
    "guards",
    "runtime_contracts",
    "advisory",
    "audit",
    "cli",
    "cli_bridge",
    "hoi_boundary",
    "integration",
    "prompt_export",
    "regression",
    "validator",
}


def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    kernel_root = os.path.join(project_root, "sapianta_hoi")

    if not os.path.isdir(kernel_root):
        print("ERROR: sapianta_hoi directory not found.")
        sys.exit(1)

    detected = set()

    for entry in os.listdir(kernel_root):
        path = os.path.join(kernel_root, entry)

        if os.path.isdir(path) and not entry.startswith("__"):
            detected.add(entry)

    violations = detected - ALLOWED_NAMESPACES

    if violations:
        print("KERNEL BOUNDARY VIOLATION DETECTED")
        print("Unauthorized namespaces found:")
        for v in sorted(violations):
            print(f" - sapianta_hoi.{v}")
        sys.exit(1)

    print("Kernel boundary check: PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
