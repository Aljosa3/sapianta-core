"""
SAPIANTA Development Governance Gate

Purpose:
Evaluate AI-generated development tasks before execution.

Decisions:

ALLOW
REVIEW
BLOCK
"""


class DevGovernanceGate:
    """
    Governance gate for development tasks.
    """

    ALLOW = "ALLOW"
    REVIEW = "REVIEW"
    BLOCK = "BLOCK"

    def evaluate(self, task: dict) -> str:
        """
        Evaluate development task risk.
        """

        idea = task.get("idea", "").lower()
        task_type = task.get("task_type", "")

        # dangerous keywords

        dangerous = [
            "delete",
            "remove kernel",
            "drop table",
            "override governance",
        ]

        for word in dangerous:
            if word in idea:
                return self.BLOCK

        # sensitive areas

        sensitive = [
            "governance",
            "kernel",
            "security",
            "policy",
        ]

        for word in sensitive:
            if word in idea:
                return self.REVIEW

        # bugfix always allowed

        if task_type == "bugfix":
            return self.ALLOW

        return self.ALLOW