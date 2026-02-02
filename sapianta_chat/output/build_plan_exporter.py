# PATH: sapianta_chat/output/build_plan_exporter.py

import json
from typing import Dict, Any, List


class BuildPlanExportError(RuntimeError):
    pass


BUILD_PLAN_PROTOCOL = "SAPIANTA_BUILD_PLAN_V1"


def export_build_plan(
    reviewed_response: Dict[str, Any],
    path: str,
) -> None:
    """
    Export a human-confirmed build plan into a strict,
    Claude-consumable JSON artifact.

    Preconditions:
    - reviewed_response MUST be the output of cli_proposal_gate
    - decision authority is already resolved by the human
    - this function performs NO execution
    """

    # --- hard precondition ---
    if reviewed_response.get("mode") != "PROPOSAL_REVIEW_RESULT":
        raise BuildPlanExportError(
            "Response is not a reviewed build proposal."
        )

    content = reviewed_response.get("content", {})

    approved: List[Dict[str, Any]] = content.get("approved", [])
    modified: List[Dict[str, Any]] = content.get("modified", [])

    steps: List[Dict[str, str]] = []

    # Approved steps
    for step in approved:
        desc = step.get("description")
        if desc:
            steps.append({"description": desc})

    # Modified steps
    for step in modified:
        desc = step.get("description")
        if desc:
            steps.append({"description": desc})

    if not steps:
        raise BuildPlanExportError(
            "No approved or modified build steps to export."
        )

    # --- strict Claude-facing build plan ---
    build_plan = {
        "protocol": BUILD_PLAN_PROTOCOL,
        "execution_role": "CLAUDE_CODE_EXECUTOR",
        "constraints": {
            "no_markdown": True,
            "no_extra_files": True,
            "no_forbidden_imports": True,
            "no_governance_changes": True,
            "analysis_only_modules": True,
            "no_execution_logic": True,
        },
        "steps": steps,
        "rules": [
            "Generate only the steps listed",
            "Use pure Python only",
            "Do not add files beyond the plan",
            "Do not include explanations or prose",
        ],
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(build_plan, f, indent=2, ensure_ascii=False)

    print(f"[EXPORT] Build plan exported to {path}")
