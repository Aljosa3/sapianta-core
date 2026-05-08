"""
SAPIANTA Quality Signal Filter — v1

Purpose:
- Prevent false-positive improvement triggers when tests pass
- Validate that failure_info carries actionable structured error content
- Compute minimal quality proxy for generated code

Design:
- deterministic (regex-based, no LLM)
- no randomness
- fail-safe: ambiguous signals → not actionable
"""

import re
from pathlib import Path

# ================================================================
# PYTEST SUCCESS SIGNATURES — these are terminal output strings,
# NOT structured errors. Presence alone does not warrant a fix.
# ================================================================

_PYTEST_SUCCESS_MARKERS = [
    "passed",
    "[100%]",
    "no tests ran",
    "warnings summary",
    "short test summary info",
    "====",
    "----",
    "deprecated",
]

# ================================================================
# STRUCTURED ERROR MARKERS — indicate a real actionable failure
# ================================================================

_STRUCTURED_ERROR_MARKERS = [
    "Error",
    "Exception",
    "Traceback",
    "FAILED",
    "SyntaxError",
    "NameError",
    "TypeError",
    "ImportError",
    "ModuleNotFoundError",
    "AttributeError",
    "ValueError",
    "AssertionError",
]

# Pure pytest dot output: only dots, spaces, newlines, "[", "%", "]"
_DOT_ONLY_PATTERN = re.compile(r"^[.\s\[\]%\d]+$")


def is_actionable_signal(failure_info: dict) -> bool:
    """
    Returns True ONLY when failure_info contains a structured,
    actionable error that AutoFixEngine can meaningfully process.

    Returns False for:
    - pytest success output (dots, [100%], "1 passed")
    - empty or None error text
    - output that is only dots/whitespace/progress markers
    - any output containing only success markers and no error markers

    Deterministic: no side effects, no I/O.
    """
    if not isinstance(failure_info, dict):
        return False

    error_text = str(failure_info.get("error") or "").strip()
    test_output = str(failure_info.get("test_output") or "").strip()

    combined = f"{error_text}\n{test_output}".strip()

    # Empty signal → not actionable
    if not combined:
        return False

    # Pure dot/progress output → pytest success output → not actionable
    if _DOT_ONLY_PATTERN.match(combined):
        return False

    # Contains ONLY pytest success markers, no error markers → not actionable
    has_success_marker = any(m in combined for m in _PYTEST_SUCCESS_MARKERS)
    has_error_marker = any(m in combined for m in _STRUCTURED_ERROR_MARKERS)

    if has_success_marker and not has_error_marker:
        return False

    # Must contain at least one structured error marker to be actionable
    if not has_error_marker:
        return False

    return True


def compute_quality_score(generated_dir) -> dict:
    """
    Minimal quality proxy for generated code in generated_dir.

    Scans *.py (excluding test_*) and returns:
      - function_count   : total top-level def statements found
      - trivial_count    : functions whose body is only return None / pass / ...
      - assert_count     : total assert statements in test_*.py files
      - is_trivial       : True when all functions are trivial stubs

    Deterministic: stable sorted file order, no timestamps.
    """
    generated_dir = Path(generated_dir)

    function_count = 0
    trivial_count = 0
    assert_count = 0

    if not generated_dir.exists():
        return {
            "function_count": 0,
            "trivial_count": 0,
            "assert_count": 0,
            "is_trivial": True,
        }

    for py_file in sorted(generated_dir.glob("*.py")):

        try:
            content = py_file.read_text(encoding="utf-8")
        except Exception:
            continue

        if py_file.name.startswith("test_"):
            assert_count += content.count("assert")
            continue

        # Count top-level function defs
        defs = re.findall(r"^def\s+\w+", content, re.MULTILINE)
        function_count += len(defs)

        # Count trivial function bodies (return None / pass / ...)
        trivial_patterns = [
            r"def\s+\w+[^:]*:\s*\n\s+return\s+None\b",
            r"def\s+\w+[^:]*:\s*\n\s+pass\b",
            r"def\s+\w+[^:]*:\s*\n\s+\.\.\.",
        ]
        for pat in trivial_patterns:
            trivial_count += len(re.findall(pat, content))

    is_trivial = function_count > 0 and trivial_count >= function_count

    return {
        "function_count": function_count,
        "trivial_count": trivial_count,
        "assert_count": assert_count,
        "is_trivial": is_trivial,
    }


def is_improvement_needed(quality_score: dict) -> bool:
    """
    Returns True only when there is a meaningful, addressable quality gap.

    All three conditions must hold:
    1. There are generated functions to improve
    2. All functions are trivial stubs (return None / pass)
    3. Tests have assertions (improvement is verifiable)

    If any condition is missing, improvement is either impossible
    (no functions) or unverifiable (no asserts) → return False.
    """
    if not isinstance(quality_score, dict):
        return False

    fn_count = quality_score.get("function_count", 0)
    assert_count = quality_score.get("assert_count", 0)
    is_trivial = quality_score.get("is_trivial", False)

    if fn_count == 0:
        return False

    if assert_count == 0:
        return False

    return is_trivial
