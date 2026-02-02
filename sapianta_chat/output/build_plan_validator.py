# PATH: sapianta_chat/output/build_plan_validator.py

from typing import Dict, Any, List, Set


class BuildPlanValidationError(RuntimeError):
    pass


def validate_claude_output(
    build_plan: Dict[str, Any],
    claude_output: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Validates Claude Code output against an approved build plan.

    Expected claude_output shape:
    {
        "files": {
            "path/to/file.py": "...content...",
            ...
        }
    }

    This validator performs NO execution and NO mutation.
    """

    plan_steps = build_plan.get("steps", [])
    constraints = set(build_plan.get("constraints", []))

    files = claude_output.get("files")
    if not isinstance(files, dict):
        raise BuildPlanValidationError(
            "Claude output must contain a 'files' dictionary."
        )

    created_paths: Set[str] = set(files.keys())

    violations: List[str] = []

    # -----------------------------
    # Constraint checks
    # -----------------------------

    for path in created_paths:
        if "no_markdown_files" in constraints and path.endswith(".md"):
            violations.append(f"Forbidden markdown file: {path}")

        if "analysis_only_modules" in constraints:
            if "/runtime/" in path or path.startswith("runtime/"):
                violations.append(f"Forbidden runtime path: {path}")

    # -----------------------------
    # Step coverage check (minimal)
    # -----------------------------

    for step in plan_steps:
        desc = step.get("description", "").lower()

        if "create module directory" in desc:
            if not any("/modules/" in p for p in created_paths):
                violations.append(
                    f"Planned module directory not reflected in output: {desc}"
                )

        if "extract_" in desc:
            if not any("extract_" in p for p in created_paths):
                violations.append(
                    f"Planned extractor function not reflected in output: {desc}"
                )

    # -----------------------------
    # Final result
    # -----------------------------

    if violations:
        return {
            "status": "FAIL",
            "violations": violations,
        }

    return {
        "status": "PASS",
        "violations": [],
    }
