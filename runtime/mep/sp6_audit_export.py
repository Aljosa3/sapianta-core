from .context import ExecutionContext


def sp6_audit_export(ctx: ExecutionContext, target: str = "stdout"):
    """
    SP-6: Audit Export (best-effort)

    Exports execution metadata for audit purposes.
    This pass is NON-NORMATIVE and MUST NOT influence:
    - ctx.status
    - ctx.result
    - any execution decision

    It is executed strictly AFTER ctx has been finalized.
    """

    try:
        record = {
            "context_id": ctx.context_id,
            "status": ctx.status.name,
            "phase": ctx.phase.name,
            "decisions": ctx.decisions,
            "violations": ctx.violations,
            "policy": getattr(ctx, "policy", None),
            "timestamp": ctx.created_at,
        }

        if target == "stdout":
            print("[AUDIT]", record)

        # Other targets (file, db, stream) may be added later

    except Exception:
        # Audit must NEVER break execution
        pass
