# runtime/mep/guards.py

from context import ExecutionContext, Status, Phase


class GuardViolation(Exception):
    """Base exception for guard violations."""
    pass


def assert_context_integrity(ctx: ExecutionContext):
    """
    Assertion Guard
    Preveri osnovno integriteto Execution Contexta.
    """
    if ctx is None:
        raise GuardViolation("ExecutionContext is missing")

    if not isinstance(ctx, ExecutionContext):
        raise GuardViolation("Invalid ExecutionContext type")

    if ctx.context_id is None:
        raise GuardViolation("Missing context_id")

    if ctx.phase == Phase.FINAL:
        raise GuardViolation("Context already finalized")


def assert_execution_phase(ctx: ExecutionContext):
    """
    Assertion Guard
    Preveri, ali je kontekst v pravilni fazi za izvajanje.
    """
    if ctx.phase != Phase.INIT:
        raise GuardViolation(f"Invalid phase for execution: {ctx.phase}")


def permission_guard(ctx: ExecutionContext):
    """
    Permission Guard
    Minimalna dovoljenost za MEP.
    (V MEP dovolimo samo 'chat' izvor.)
    """
    if ctx.source != "chat":
        ctx.add_violation("Source not permitted in MEP")
        ctx.finalize(
            status=Status.DENY,
            error="Source not permitted"
        )
        raise GuardViolation("Permission denied")


def runtime_guards(ctx: ExecutionContext):
    """
    Centralni vstop v Runtime Guards (F54).
    Izvede vse guard preverbe zaporedno.
    """
    try:
        assert_context_integrity(ctx)
        assert_execution_phase(ctx)
        permission_guard(ctx)

        # Če vse prestane:
        ctx.add_decision("All runtime guards passed")
        ctx.status = Status.ALLOW
        ctx.phase = Phase.EXECUTION

    except GuardViolation as gv:
        # Če guard sproži izjemo in še ni FINAL:
        if ctx.phase != Phase.FINAL:
            ctx.add_violation(str(gv))
            ctx.finalize(
                status=Status.HALT,
                error=str(gv)
            )
        raise
