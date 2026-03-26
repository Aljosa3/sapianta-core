"""
SAPIANTA Approval Gate

Purpose
-------
Human-controlled approval layer for autonomous development.

This module enforces:
- explicit approval before applying changes
- deterministic status classification
- separation of authority (AI vs Human)
"""

from datetime import datetime, UTC


ALLOWED_STATUSES = {
    "success",
    "failed",
    "blocked",
    "requires_approval"
}

ALLOWED_RISK_LEVELS = {
    "low",
    "medium",
    "high"
}


def classify_risk(files: list) -> str:
    """
    Simple deterministic risk classification.
    """

    if not files:
        return "low"

    for f in files:
        if f.startswith("runtime/governance") or f.startswith("runtime/system"):
            return "high"

    if len(files) > 3:
        return "medium"

    return "low"


def build_approval_request(task: dict, files: list, status: str) -> dict:
    """
    Constructs a deterministic approval request.
    """

    if status not in ALLOWED_STATUSES:
        status = "failed"

    risk = classify_risk(files)

    return {
        "timestamp": datetime.now(UTC).isoformat(),
        "task_id": task.get("id"),
        "goal": task.get("goal"),
        "status": status,
        "files": files,
        "risk": risk,
        "approved": False
    }


def requires_human_approval(approval_request: dict) -> bool:
    """
    FORCE APPROVAL MODE
    -------------------
    All changes require explicit human approval.

    This is used in CONTROLLED PRODUCTION phase.
    """

    return True


def apply_human_decision(approval_request: dict, approved: bool) -> dict:
    """
    Applies human decision.
    """

    approval_request["approved"] = approved
    approval_request["decision_timestamp"] = datetime.now(UTC).isoformat()

    return approval_request