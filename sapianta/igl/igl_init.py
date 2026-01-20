"""SAPIANTA IGL — INIT
Implementation Guard Layer (read-only checker)

Rules enforced:
- GR-001 — No Semantic Fallbacks
- GR-002 — No Implicit Authority Escalation
- GR-003 — No Implicit Defaults
- GR-004 — No Hidden Control Flow (decorators restricted)
- GR-006 — No Global State Mutation (runtime-only)
"""

from pathlib import Path
from typing import List, Tuple
import re


# ─────────────────────────────────────────────────────────────
# ZONE DEFINITIONS
# ─────────────────────────────────────────────────────────────

DECLARATIVE_PATH_MARKERS = [
    "/interfaces/",
]

DECLARATIVE_FILES = [
    "__init__.py",
]

RUNTIME_PATH_MARKERS = [
    "/chat/",
    "/core/",
    "/execution/",
    "/decision/",
    "/interaction/",
]


def is_declarative(path: Path) -> bool:
    p = str(path)
    return (
        path.name in DECLARATIVE_FILES
        or any(marker in p for marker in DECLARATIVE_PATH_MARKERS)
    )


def is_runtime(path: Path) -> bool:
    p = str(path)
    return any(marker in p for marker in RUNTIME_PATH_MARKERS)


# ─────────────────────────────────────────────────────────────
# GR-001 — No Semantic Fallbacks
# ─────────────────────────────────────────────────────────────

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


# ─────────────────────────────────────────────────────────────
# GR-002 — No Implicit Authority Escalation
# ─────────────────────────────────────────────────────────────

DISALLOWED_AUTHORITY_PATTERNS = [
    "sapianta.core",
    "engine.execute",
    "core.run",
    "system.apply",
]


# ─────────────────────────────────────────────────────────────
# GR-003 — No Implicit Defaults
# ─────────────────────────────────────────────────────────────

DISALLOWED_DEFAULT_REGEX = [
    r"\sor\s",
    r"if\s+.+\s+else\s+",
    r"=\s*.+\s+or\s+.+",
]


# ─────────────────────────────────────────────────────────────
# GR-004 — No Hidden Control Flow (decorators)
# ─────────────────────────────────────────────────────────────

ALLOWED_DECORATORS = {
    "abstractmethod",
    "dataclass",
}

DECORATOR_REGEX = re.compile(r"@([a-zA-Z_][a-zA-Z0-9_]*)")


# ─────────────────────────────────────────────────────────────
# GR-006 — No Global State Mutation (runtime-only)
# ─────────────────────────────────────────────────────────────

GLOBAL_MUTATION_REGEX = re.compile(
    r"^[a-zA-Z_][a-zA-Z0-9_]*\s*=",
    re.MULTILINE,
)


# ─────────────────────────────────────────────────────────────

def scan_file(path: Path) -> List[str]:
    violations: List[str] = []

    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return violations

    # ── GR-001
    for literal in DISALLOWED_STRING_LITERALS:
        if literal in content:
            violations.append(
                f"{path}: GR-001 disallowed semantic literal '{literal}'"
            )

    for ctor in DISALLOWED_RESPONSE_CONSTRUCTION:
        if ctor in content:
            violations.append(
                f"{path}: GR-001 potential semantic response construction '{ctor}'"
            )

    # ── GR-002
    for pattern in DISALLOWED_AUTHORITY_PATTERNS:
        if pattern in content:
            violations.append(
                f"{path}: GR-002 implicit authority escalation via '{pattern}'"
            )

    # ── GR-003
    for regex in DISALLOWED_DEFAULT_REGEX:
        if re.search(regex, content):
            violations.append(
                f"{path}: GR-003 implicit default detected (pattern '{regex}')"
            )

    # ── GR-004 (decorators)
    for match in DECORATOR_REGEX.findall(content):
        if match not in ALLOWED_DECORATORS:
            violations.append(
                f"{path}: GR-004 disallowed decorator '@{match}'"
            )

    # ── GR-006 (runtime-only global mutation)
    if is_runtime(path) and not is_declarative(path):
        for match in GLOBAL_MUTATION_REGEX.findall(content):
            if match not in ("__all__",):
                violations.append(
                    f"{path}: GR-006 top-level state mutation '{match} ='"
                )

    return violations


def scan_tree(root: Path) -> Tuple[bool, List[str]]:
    all_violations: List[str] = []

    for path in root.rglob("*.py"):
        # no self-scan
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
