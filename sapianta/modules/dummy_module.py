"""
Dummy Module for SAPIANTA — CODEBASE_INIT.

This module intentionally does nothing meaningful.
It exists solely to prove that modules can be executed
without decision-making or interpretation.
"""


class DummyModule:
    name = "dummy_module"

    def __init__(self, trace):
        self.trace = trace

    def run(self, context):
        """
        Execute the dummy module.

        This method:
        - reads from context (if anything exists)
        - writes a placeholder value
        - does not interpret or decide
        """
        self.trace.record("dummy_module.run.start")

        # read existing context keys (no interpretation)
        keys = list(context.items())

        # write a placeholder output
        context.set("dummy_output", f"processed_{len(keys)}_items")

        self.trace.record("dummy_module.run.end")
