class DryRunExecutionAdapter:
    """
    Dry-run execution adapter.

    Purpose:
    - simulate what would be executed
    - never perform real actions
    - enforce explicit execution permission

    This adapter:
    - does NOT execute
    - does NOT decide
    - does NOT mutate system state
    """

    ADAPTER_ID = "execution.dry_run"
    VERSION = "1.0.0"

    def __init__(self, config=None):
        self.config = config or {}

    def run(self, decision, context):
        """
        Inputs:
        - decision: structured decision output (or demo substitute)
        - context: system context

        Output:
        - execution plan (simulation only)
        """

        if context.get("execution_allowed", False):
            raise RuntimeError(
                "DryRunExecutionAdapter refuses to run when execution_allowed=True"
            )

        plan = {
            "adapter_id": self.ADAPTER_ID,
            "mode": "dry-run",
            "would_execute": False,
            "decision_reference": decision.get("id", "demo-decision"),
            "summary": "No execution performed. This is a simulation.",
            "steps": decision.get("proposed_steps", []),
        }

        return plan
