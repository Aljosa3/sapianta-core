import pytest
from runtime.mep.context import ExecutionContext
from runtime.mep.orchestrator import Orchestrator
from runtime.guard_lifecycle.errors import ProtocolViolation


def test_execution_without_origin_is_rejected():
    """
    Invariant:
    Execution MUST NOT proceed without GuardLifecycle origin.
    """

    ctx = ExecutionContext(
        source="chat",
        raw_input="test input"
    )

    orchestrator = Orchestrator()

    with pytest.raises(ProtocolViolation):
        orchestrator.run(ctx)
