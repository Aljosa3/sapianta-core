"""
Guard interface for SAPIANTA — RUNTIME_GUARD_INIT.

The Guard is a structural placeholder.
It may be invoked by the runtime but performs no evaluation.
"""

from sapianta.runtime.guard.verdict import Verdict


class Guard:
    def __init__(self, trace):
        self.trace = trace

    def evaluate(self, context):
        """
        Evaluate the context.

        In RUNTIME_GUARD_INIT this method:
        - performs no checks
        - makes no decisions
        - always returns an empty Verdict
        """
        self.trace.record("guard.evaluate.called")
        return Verdict()
