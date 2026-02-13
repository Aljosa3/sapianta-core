#!/usr/bin/env python3

"""
Kernel Boundary Auto-Check Script (Governance-Bound)
-----------------------------------------------------

Validates that sapianta_hoi/ namespaces match the whitelist
defined in:

governance/kernel/KERNEL_PUBLIC_SURFACE_SNAPSHOT_v1.0.md

The governance document is treated as the source of truth.

Deterministic.
No external dependencies.
"""

import os
import sys


SNAPSHOT_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "governance",
    "kernel",
    "KERNEL_PUBLIC_SURFACE_SNAPSHOT_v1.0.md",
)


def extract_whitelist(snapshot_path):
    """
    Extract allowed namespaces from snapshot markdown.

    Expected format inside markdown:

    - sapianta_hoi.runtime_stub
    - sapianta_hoi.execution
    """

    if not os.path.isfile(snapshot_path):
        print("ERROR: Kernel snapshot file not found.")
        sys.exit(1)

    allowed = set()

    with open(snapshot_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line.startswith("- sapianta_hoi."):
                namespace = line.replace("- sapianta_hoi.", "").strip()
                allowed.add(namespace)

    if not allowed:
        print("ERROR: No namespaces extracted from snapshot.")
        sys.exit(1)

    return allowed


def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    kernel_root = os.path.join(project_root, "sapianta_hoi")

    if not os.path.isdir(kernel_root):
        print("ERROR: sapianta_hoi directory not found.")
        sys.exit(1)

    allowed_namespaces = extract_whitelist(SNAPSHOT_FILE)

    detected = set()

    for entry in os.listdir(kernel_root):
        path = os.path.join(kernel_root, entry)

        if os.path.isdir(path) and not entry.startswith("__"):
            detected.add(entry)

    unauthorized = detected - allowed_namespaces
    missing = allowed_namespaces - detected

    if unauthorized or missing:
        print("KERNEL BOUNDARY VIOLATION DETECTED")

        if unauthorized:
            print("Unauthorized namespaces:")
            for ns in sorted(unauthorized):
                print(f" - sapianta_hoi.{ns}")

        if missing:
            print("Missing namespaces declared in snapshot:")
            for ns in sorted(missing):
                print(f" - sapianta_hoi.{ns}")

        sys.exit(1)

    print("Kernel boundary check (governance-bound): PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
