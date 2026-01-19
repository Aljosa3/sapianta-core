"""
Execution Gate.

The Execution Gate is the only allowed entry point
into execution adapters.

It enforces the invariant:
No execution without explicit Decision.
"""

from sapianta.decision.decision import Decision


class ExecutionGate:
    """
    Runtime execution safety gate.

    Responsibilities:
    - require explicit Decision instance
    - prevent execution without decision
    - delegate execution to adapter
    """

    def __init__(self, adapter):
        self.adapter = adapter

    def run(self, decision, context):
        # 1. Decision must exist
        if decision is None:
            raise RuntimeError(
                "ExecutionGate: execution denied — missing Decision."
            )

        # 2. Decision must be a Decision object
        if not isinstance(decision, Decision):
            raise TypeError(
                "ExecutionGate: invalid decision type. "
                "Expected Decision instance."
            )

        # 3. Delegate to execution adapter (dry-run or real)
        return self.adapter.run(
            decision=decision,
            context=context
        )
