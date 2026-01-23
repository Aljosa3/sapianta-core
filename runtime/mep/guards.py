from .context import ExecutionContext, Status, Phase


class GuardViolation(Exception):
    """
    Raised when a runtime guard blocks execution.
    """
    pass


def runtime_guards(ctx: ExecutionContext):
    """
    Runtime Guards (MEP)

    Guards are the ONLY place where:
    - Status may transition from PENDING → ALLOW

    Guards are NOT allowed to:
    - transition Phase (INIT → EXECUTION)

    Phase transition is owned exclusively by GuardLifecycle.
    Any failure here MUST prevent execution.
    """

    # --- Structural validation ---
    if not isinstance(ctx, ExecutionContext):
        raise GuardViolation("Invalid execution context")

    # --- Phase enforcement (NO mutation) ---
    if ctx.phase != Phase.EXECUTION:
        raise GuardViolation(
            "Execution attempted outside EXECUTION phase"
        )

    # --- Source validation ---
    if not ctx.source:
        ctx.add_violation("Guard blocked: missing source")
        ctx.finalize(
            status=Status.DENY,
            error="Missing source"
        )
        raise GuardViolation("Missing source")

    # --- Allow execution (status only) ---
    ctx.status = Status.ALLOW
