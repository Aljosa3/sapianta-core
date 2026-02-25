import argparse
import subprocess
import sys
from typing import List, Set


VALID_TYPES = {"cosmetic", "parametric", "structural"}

# Minimal "constitutional surface" tripwires.
TRIPWIRE_PREFIXES = [
    "governance/constitutional/",
    "sapianta_core/_internal/runtime/",
]

TRIPWIRE_FILES = {
    "sapianta_core/contracts.py",
    "sapianta_core/control.py",
    "sapianta_core/result.py",
    "sapianta_core/__init__.py",
}

# v0.1.2: structural changes require an approval artifact (staged or unstaged diff)
APPROVAL_PREFIX = "governance/evolution/approvals/"
APPROVAL_NAME_PREFIX = "STRUCTURAL_APPROVAL_"


def _run_capture(cmd: List[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def _run_or_exit(cmd: str) -> None:
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)


def _git_changed_files() -> List[str]:
    """
    Returns a union of:
    - unstaged changes
    - staged changes
    """
    files: Set[str] = set()

    r1 = _run_capture(["git", "diff", "--name-only"])
    if r1.returncode == 0:
        for line in r1.stdout.splitlines():
            line = line.strip()
            if line:
                files.add(line)

    r2 = _run_capture(["git", "diff", "--name-only", "--cached"])
    if r2.returncode == 0:
        for line in r2.stdout.splitlines():
            line = line.strip()
            if line:
                files.add(line)

    return sorted(files)


def _touches_tripwire(paths: List[str]) -> List[str]:
    touched = []
    for p in paths:
        if p in TRIPWIRE_FILES:
            touched.append(p)
            continue
        for pref in TRIPWIRE_PREFIXES:
            if p.startswith(pref):
                touched.append(p)
                break
    return touched


def _has_structural_approval_artifact(changed_paths: List[str]) -> bool:
    """
    v0.1.2 rule: structural approval requires at least one approval doc in diff.
    We accept any file under approvals/ starting with STRUCTURAL_APPROVAL_ (excluding TEMPLATE).
    """
    for p in changed_paths:
        if not p.startswith(APPROVAL_PREFIX):
            continue
        name = p.split("/")[-1]
        if not name.startswith(APPROVAL_NAME_PREFIX):
            continue
        if "TEMPLATE" in name:
            continue
        if not name.endswith(".md"):
            continue
        return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="promotion_gate_validator",
        description="SAPIANTA Promotion Gate v0.1.2 (path tripwire + approval artifact)",
    )
    parser.add_argument("change_type", help="cosmetic | parametric | structural")
    parser.add_argument(
        "--approve-structural",
        action="store_true",
        help="Explicitly approve STRUCTURAL changes.",
    )
    parser.add_argument(
        "--explain",
        action="store_true",
        help="Print changed files and tripwire evaluation, then exit.",
    )

    args = parser.parse_args()
    change_type = args.change_type.lower().strip()

    if change_type not in VALID_TYPES:
        print(f"Invalid change type: {change_type}. Allowed: {sorted(VALID_TYPES)}")
        sys.exit(1)

    changed = _git_changed_files()
    touched = _touches_tripwire(changed)
    has_approval = _has_structural_approval_artifact(changed)

    if args.explain:
        print("---- Promotion Gate v0.1.2 EXPLAIN ----")
        print(f"Requested change_type: {change_type}")
        print(f"Approve structural flag: {args.approve_structural}")
        print("Changed files:")
        if not changed:
            print("  (none detected in staged/unstaged diff)")
        else:
            for f in changed:
                print(f"  - {f}")
        print("Tripwire touched:")
        if not touched:
            print("  (no constitutional surface touched)")
        else:
            for f in touched:
                print(f"  - {f}")
        print(f"Structural approval artifact present in diff: {has_approval}")
        print("---- END EXPLAIN ----")
        return

    # Tripwire implies structural.
    effective_structural = (change_type == "structural") or bool(touched)

    if effective_structural:
        if not args.approve_structural:
            if touched:
                print("Tripwire detected constitutional surface touched:")
                for f in touched:
                    print(f"  - {f}")
            print("This requires explicit approval: --approve-structural")
            sys.exit(1)

        if not has_approval:
            print("STRUCTURAL approval requires an approval artifact in diff.")
            print(f"Add a file: {APPROVAL_PREFIX}{APPROVAL_NAME_PREFIX}<SOMETHING>.md")
            sys.exit(1)

    print("Running determinism checks...")
    _run_or_exit("pytest -q")

    print("Running layer freeze check...")
    _run_or_exit("python scripts/check_layer_freeze.py")

    print("Promotion Gate PASSED.")


if __name__ == "__main__":
    main()