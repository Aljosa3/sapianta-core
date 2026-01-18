"""
Runtime Orchestrator for SAPIANTA — CODEBASE_INIT.

The Runtime is responsible only for:
- coordinating the execution flow
- passing context through the flow
- recording trace events

It does not:
- make decisions
- interpret data
- enforce rules
"""

from sapianta.runtime.flow import ExecutionFlow


class Runtime:
    def __init__(self, trace):
        self.trace = trace
        self.flow = ExecutionFlow(trace=self.trace)

    def run(self, context):
        """
        Execute the runtime flow with the given context.
        """
        self.trace.record("runtime.run.start")

        # delegate execution to the flow
        self.flow.execute(context)

        self.trace.record("runtime.run.end")
