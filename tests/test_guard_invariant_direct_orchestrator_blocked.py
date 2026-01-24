import pytest

from runtime.mep.context import ExecutionContext
from runtime.mep.orchestrator import Orchestrator
from runtime.guard_lifecycle.errors import ProtocolViolation


def test_direct_orchestrator_invocation_is_blocked():
    """
    Invariant:
    Orchestrator MUST NOT be callable directly without GuardLifecycle.
    """

    ctx = ExecutionContext(
        source="chat",
        raw_input="test"
    )

    orchestrator = Orchestrator()

    with pytest.raises(Exception):
        orchestrator.run(ctx)
