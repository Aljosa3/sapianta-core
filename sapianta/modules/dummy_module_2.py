"""
Second Dummy Module for SAPIANTA — CODEBASE_EXTENSION_1.

This module exists to prove that the execution flow
can be extended without changing runtime semantics.
"""


class DummyModule2:
    name = "dummy_module_2"

    def __init__(self, trace):
        self.trace = trace

    def run(self, context):
        """
        Execute the second dummy module.

        Performs a trivial, non-semantic write to context.
        """
        self.trace.record("dummy_module_2.run.start")

        # read existing context keys (no interpretation)
        keys = list(context.items())

        # write another placeholder output
        context.set("dummy_output_2", f"observed_{len(keys)}_items")

        self.trace.record("dummy_module_2.run.end")
