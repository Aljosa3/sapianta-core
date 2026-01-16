from .context import ExecutionContext, Status, Phase


class GuardViolation(Exception):
    """
    Raised when a runtime guard blocks execution.
    """
    pass


def runtime_guards(ctx: ExecutionContext):
    """
    Runtime Guards

    Guards are the ONLY place where:
    - Status may transition from PENDING → ALLOW
    - Phase may transition from INIT → EXECUTION

    Any failure here MUST prevent execution.
    """

    # Basic structural validation
    if not isinstance(ctx, ExecutionContext):
        raise GuardViolation("Invalid execution context")

    # Source must be present
    if not ctx.source:
        ctx.add_violation("Guard blocked: missing source")
        ctx.finalize(
            status=Status.DENY,
            error="Missing source"
        )
        raise GuardViolation("Missing source")

    # Allow execution
    ctx.status = Status.ALLOW
    ctx.phase = Phase.EXECUTION
