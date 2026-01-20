"""SAPIANTA IGL — INIT
Implementation Guard Layer (read-only checker)
Rule: IGL-GR-001 — No Semantic Fallbacks
"""

from pathlib import Path
from typing import List, Tuple


DISALLOWED_STRING_LITERALS = [
    "No handler configured",
    "System not ready",
    "No decision handler",
    "handler not configured",
]

DISALLOWED_RESPONSE_CONSTRUCTION = [
    "ChatResponse(",
    "Response(",
]


def scan_file(path: Path) -> List[str]:
    violations: List[str] = []
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return violations

    for literal in DISALLOWED_STRING_LITERALS:
        if literal in content:
            violations.append(f"{path}: disallowed semantic literal '{literal}'")

    for ctor in DISALLOWED_RESPONSE_CONSTRUCTION:
        if ctor in content:
            violations.append(f"{path}: potential semantic response construction '{ctor}'")

    return violations


def scan_tree(root: Path) -> Tuple[bool, List[str]]:
    all_violations: List[str] = []
    for path in root.rglob("*.py"):
        if "sapianta/igl" in str(path):
            continue
        all_violations.extend(scan_file(path))

    if all_violations:
        return False, all_violations

    return True, []


def run(target_path: str) -> int:
    root = Path(target_path)
    ok, violations = scan_tree(root)

    if ok:
        print("IGL-INIT: PASS")
        return 0

    print("IGL-INIT: FAIL")
    for v in violations:
        print(f"- {v}")
    return 1


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 igl_init.py <path-to-scan>")

    raise SystemExit(run(sys.argv[1]))
