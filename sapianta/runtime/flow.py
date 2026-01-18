"""
Execution Flow for SAPIANTA — CODEBASE_INIT.

The ExecutionFlow coordinates the sequential execution
of modules without interpreting their meaning or results.
"""

from sapianta.modules.dummy_module import DummyModule


class ExecutionFlow:
    def __init__(self, trace):
        self.trace = trace
        # initialize modules (no logic, fixed order)
        self.modules = [
            DummyModule(trace=self.trace)
        ]

    def execute(self, context):
        """
        Execute all modules sequentially.
        """
        self.trace.record("flow.execute.start")

        for module in self.modules:
            self.trace.record(f"flow.module.start:{module.name}")
            module.run(context)
            self.trace.record(f"flow.module.end:{module.name}")

        self.trace.record("flow.execute.end")
