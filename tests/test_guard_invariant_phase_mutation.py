import pytest

from runtime.mep.context import ExecutionContext, Phase
from runtime.mep.guards import runtime_guards


def test_runtime_guards_do_not_mutate_phase():
    """
    Invariant:
    Guards MUST NOT transition phase INIT → EXECUTION.
    """

    ctx = ExecutionContext(
        source="chat",
        raw_input="test"
    )

    assert ctx.phase == Phase.INIT

    try:
        runtime_guards(ctx)
    except Exception:
        pass

    # Phase must NOT be mutated by guards
    assert ctx.phase == Phase.INIT
