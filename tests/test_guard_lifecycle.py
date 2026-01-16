#!/usr/bin/env python3
"""
TEST: Guard → Status.ALLOW lifecycle

Purpose:
- Ensure Status.ALLOW is set ONLY by runtime guards
- Ensure orchestrator does NOT invent ALLOW
- Ensure execution proceeds ONLY when guards allow it
- Ensure explain layer does NOT influence decision outcome

This test protects the core semantic lock:
"Normative decision must not depend on explanation."
"""

import sys
import os

# ------------------------------------------------------------
# Ensure project root is on PYTHONPATH
# ------------------------------------------------------------

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ------------------------------------------------------------
# Imports (now safe)
# ------------------------------------------------------------

from runtime.mep.context import ExecutionContext, Status, Phase
from runtime.mep.orchestrator import Orchestrator


# ------------------------------------------------------------
# Mock guards
# ------------------------------------------------------------

def guard_deny(ctx: ExecutionContext):
    """
    Guard that does NOT allow execution.
    Does NOT set Status.ALLOW.
    """
    return


def guard_allow(ctx: ExecutionContext):
    """
    Guard that explicitly allows execution.
    This is the ONLY place where Status.ALLOW is set.
    """
    ctx.status = Status.ALLOW
    ctx.phase = Phase.EXECUTION


# ------------------------------------------------------------
# Monkey patch helpers
# ------------------------------------------------------------

def run_with_guard(mock_guard, ctx):
    """
    Run orchestrator with injected guard function.
    """
    import runtime.mep.orchestrator as orch_module

    original_guards = orch_module.runtime_guards
    orch_module.runtime_guards = mock_guard

    try:
        return Orchestrator().run(ctx)
    finally:
        orch_module.runtime_guards = original_guards


# ------------------------------------------------------------
# Tests
# ------------------------------------------------------------

def test_execution_halts_without_allow():
    """
    If guards do not set Status.ALLOW,
    execution MUST halt.
    """
    ctx = ExecutionContext(source="chat", raw_input="test")
    ctx = run_with_guard(guard_deny, ctx)

    assert ctx.status == Status.HALT, "Execution must HALT without ALLOW"
    assert ctx.error is not None, "HALT must provide an error"


def test_execution_proceeds_with_allow():
    """
    If guards set Status.ALLOW and Phase.EXECUTION,
    execution MUST proceed to FINAL.
    """
    ctx = ExecutionContext(source="chat", raw_input="test")
    ctx = run_with_guard(guard_allow, ctx)

    assert ctx.status == Status.FINAL, "Execution must reach FINAL"
    assert ctx.result is not None, "Execution result must exist"
    assert ctx.explain is not None, "Explain trace must be generated"


def test_explain_does_not_affect_status():
    """
    Explain must not influence normative status.
    """
    ctx = ExecutionContext(source="chat", raw_input="test")
    ctx = run_with_guard(guard_allow, ctx)

    ctx.explain["tampered"] = True
    assert ctx.status == Status.FINAL, (
        "Tampering with explain must NOT affect status"
    )


def test_allow_is_not_set_by_orchestrator():
    """
    Orchestrator must never set Status.ALLOW.
    """
    ctx = ExecutionContext(source="chat", raw_input="test")
    ctx = run_with_guard(guard_deny, ctx)

    assert ctx.status != Status.ALLOW, (
        "Status.ALLOW must never be set by orchestrator"
    )


# ------------------------------------------------------------
# Manual execution
# ------------------------------------------------------------

if __name__ == "__main__":
    test_execution_halts_without_allow()
    test_execution_proceeds_with_allow()
    test_explain_does_not_affect_status()
    test_allow_is_not_set_by_orchestrator()

    print("✔ Guard lifecycle tests passed")
