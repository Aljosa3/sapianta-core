#!/usr/bin/env python3

"""
SAPIANTA Governance Lock-Pair Consistency Scanner (V5)

Scope-limited to:
- governance/vision/
- governance/artifacts/
- governance/audit/

Normative artifact = document that contains:
    - "Status: LOCKED"
      OR
    - "Authority:"

Lifecycle alone does NOT imply normative lock requirement.

Phase lifecycle is validated separately.

Exit codes:
0 = PASS
1 = FAIL
"""

import os
import sys
import re

BASE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../governance")
)

SCOPED_DIRS = [
    "vision",
    "artifacts",
    "audit",
]

FAILURES = []


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def is_in_scope(path):
    rel = os.path.relpath(path, BASE_PATH)
    top = rel.split(os.sep)[0]
    return top in SCOPED_DIRS


def is_normative(content):
    if "Status: LOCKED" in content:
        return True
    if "Authority:" in content:
        return True
    return False


def extract_lifecycle(content):
    match = re.search(r"Lifecycle:\s*(\w+)", content)
    return match.group(1).strip() if match else None


def scan():
    md_files = []

    for root, _, files in os.walk(BASE_PATH):
        for f in files:
            if f.endswith(".md"):
                full_path = os.path.join(root, f)
                if is_in_scope(full_path):
                    md_files.append(full_path)

    base_files = {}
    lock_files = {}

    for path in md_files:
        content = read_file(path)

        if path.endswith("_LOCK.md"):
            base_name = path.replace("_LOCK.md", ".md")
            lock_files[base_name] = path
        else:
            if is_normative(content):
                base_files[path] = content

    # 1️⃣ Missing LOCK pair (only normative bases)
    for base in base_files:
        if base not in lock_files:
            FAILURES.append(f"Missing LOCK pair: {base}")

    # 2️⃣ Orphan LOCK (only if base does not exist at all)
    for base_name, lock_path in lock_files.items():
        if not os.path.exists(base_name):
            FAILURES.append(f"Orphan LOCK file: {lock_path}")

    # 3️⃣ Lifecycle validation
    for base_name, lock_path in lock_files.items():
        if base_name in base_files:
            base_content = base_files[base_name]
            lock_content = read_file(lock_path)

            base_lifecycle = extract_lifecycle(base_content)
            lock_lifecycle = extract_lifecycle(lock_content)

            if base_lifecycle != "active":
                FAILURES.append(f"Base lifecycle not active: {base_name}")

            if lock_lifecycle != "frozen":
                FAILURES.append(f"LOCK lifecycle not frozen: {lock_path}")


def main():
    print("SAPIANTA LOCK-PAIR CONSISTENCY SCAN (V5)")
    print("----------------------------------------")
    print(f"Scope: {', '.join(SCOPED_DIRS)}\n")

    scan()

    if FAILURES:
        print("❌ FAILURES DETECTED:\n")
        for f in FAILURES:
            print(f" - {f}")
        sys.exit(1)
    else:
        print("✅ PASS: Lock-pair structure consistent.")
        sys.exit(0)


if __name__ == "__main__":
    main()