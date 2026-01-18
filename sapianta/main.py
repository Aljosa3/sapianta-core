"""
SAPIANTA — CODEBASE_INIT
Minimal entry point.

This file proves that:
- the runtime can start
- a context can be created
- a flow can be executed
without any decision-making logic.
"""

from sapianta.runtime.context import Context
from sapianta.runtime.runtime import Runtime
from sapianta.trace.trace import Trace


def main():
    # initialize trace (logging only, no interpretation)
    trace = Trace()
    trace.record("main.start")

    # create empty context
    context = Context()
    trace.record("context.created")

    # initialize runtime
    runtime = Runtime(trace=trace)
    trace.record("runtime.initialized")

    # execute runtime flow
    runtime.run(context)
    trace.record("runtime.completed")

    # end
    trace.record("main.end")


if __name__ == "__main__":
    main()
