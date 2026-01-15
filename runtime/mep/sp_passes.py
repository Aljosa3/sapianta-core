# runtime/mep/sp_passes.py

from context import ExecutionContext, Status


def sp1_input_sanity(ctx: ExecutionContext):
    """
    SP-1: Input Sanity Pass
    """

    if ctx.input is None:
        ctx.add_violation("Input is missing")
        ctx.finalize(status=Status.DENY, error="Input missing")
        return False

    if not isinstance(ctx.input, str):
        ctx.add_violation("Input is not a string")
        ctx.finalize(status=Status.DENY, error="Invalid input type")
        return False

    if not ctx.normalized_input:
        ctx.add_violation("Input is empty after normalization")
        ctx.finalize(status=Status.DENY, error="Empty input")
        return False

    ctx.add_decision("SP-1 input sanity passed")
    return True


def sp2_permission_intent(ctx: ExecutionContext):
    """
    SP-2: Permission / Intent Pass
    """

    if ctx.status != Status.ALLOW:
        ctx.add_violation("SP-2 blocked: context not allowed")
        ctx.finalize(status=Status.DENY, error="Execution not permitted by SP-2")
        return False

    if ctx.source != "chat":
        ctx.add_violation("SP-2 blocked: source not permitted")
        ctx.finalize(status=Status.DENY, error="Source not permitted by SP-2")
        return False

    ctx.add_decision("SP-2 permission check passed")
    return True


def sp3_output_sanity(ctx: ExecutionContext):
    """
    SP-3: Output Sanity / Validation Pass
    """

    if ctx.result is None:
        ctx.add_violation("SP-3 blocked: missing result")
        ctx.finalize(status=Status.HARD_FAIL, error="Missing result")
        return False

    if not isinstance(ctx.result, dict):
        ctx.add_violation("SP-3 blocked: result is not a dict")
        ctx.finalize(status=Status.HARD_FAIL, error="Invalid result format")
        return False

    ctx.add_decision("SP-3 output sanity passed")
    return True


def sp4_explain_trace(ctx: ExecutionContext):
    """
    SP-4: Explain / Trace Pass

    Ustvari razlagalni zapis o poteku izvajanja.
    Mora biti odporen na manjkajoče metapodatke.
    """

    try:
        # varen ID (fallback, če ni eksplicitnega)
        context_id = (
            getattr(ctx, "id", None)
            or getattr(ctx, "context_id", None)
            or "UNKNOWN"
        )

        explanation = {
            "context_id": context_id,
            "status": ctx.status.name,
            "phase": ctx.phase.name,
            "decisions": ctx.decisions,
            "violations": ctx.violations,
        }

        ctx.explain = explanation
        ctx.add_decision("SP-4 explain trace generated")
        return True

    except Exception as e:
        ctx.add_violation(f"SP-4 failed: {str(e)}")
        ctx.finalize(status=Status.HARD_FAIL, error="Explain trace failure")
        return False
