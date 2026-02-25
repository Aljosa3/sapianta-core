import argparse
import subprocess
import sys
from typing import List, Set


VALID_TYPES = {"cosmetic", "parametric", "structural"}

# Minimal "constitutional surface" tripwires.
# If any changed file touches these paths, change is treated as STRUCTURAL.
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
    If none, returns [].
    """
    files: Set[str] = set()

    # Unstaged changes
    r1 = _run_capture(["git", "diff", "--name-only"])
    if r1.returncode == 0:
        for line in r1.stdout.splitlines():
            line = line.strip()
            if line:
                files.add(line)

    # Staged changes
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


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="promotion_gate_validator",
        description="SAPIANTA Promotion Gate v0.1.1 (path-based tripwire)",
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

    if args.explain:
        print("---- Promotion Gate v0.1.1 EXPLAIN ----")
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
        print("---- END EXPLAIN ----")
        return

    # Hard rule: STRUCTURAL requires explicit approval.
    if change_type == "structural" and not args.approve_structural:
        print("STRUCTURAL change requires explicit approval flag: --approve-structural")
        sys.exit(1)

    # Tripwire rule: if constitutional surface touched, treat as STRUCTURAL.
    if touched and not args.approve_structural:
        print("Tripwire detected constitutional surface touched:")
        for f in touched:
            print(f"  - {f}")
        print("This requires explicit approval: --approve-structural")
        sys.exit(1)

    print("Running determinism checks...")
    _run_or_exit("pytest -q")

    print("Running layer freeze check...")
    _run_or_exit("python scripts/check_layer_freeze.py")

    print("Promotion Gate PASSED.")


if __name__ == "__main__":
    main()