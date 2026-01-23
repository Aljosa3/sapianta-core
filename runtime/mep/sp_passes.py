from .context import ExecutionContext, Status


def sp1_input_sanity(ctx: ExecutionContext):
    if ctx.input is None:
        ctx.add_violation("Input is missing")
        return False

    if not isinstance(ctx.input, str):
        ctx.add_violation("Input is not a string")
        return False

    if not ctx.normalized_input:
        ctx.add_violation("Input is empty after normalization")
        return False

    ctx.add_decision("SP-1 input sanity passed")
    return True


def sp2_permission_intent(ctx: ExecutionContext):
    if ctx.status != Status.ALLOW:
        ctx.add_violation("SP-2 blocked: context not allowed")
        return False

    if ctx.source != "chat":
        ctx.add_violation("SP-2 blocked: source not permitted")
        return False

    ctx.add_decision("SP-2 permission check passed")
    return True


def sp3_output_sanity(ctx: ExecutionContext):
    if ctx.result is None:
        ctx.add_violation("SP-3 blocked: missing result")
        return False

    if not isinstance(ctx.result, dict):
        ctx.add_violation("SP-3 blocked: result is not a dict")
        return False

    ctx.add_decision("SP-3 output sanity passed")
    return True


def sp4_explain_trace(ctx: ExecutionContext):
    try:
        ctx.explain = {
            "context_id": ctx.context_id,
            "status": ctx.status.name,
            "phase": ctx.phase.name,
            "decisions": ctx.decisions,
            "violations": ctx.violations,
        }
    except Exception as e:
        ctx.explain = {"error": str(e)}
        ctx.add_violation(f"SP-4 partial failure: {str(e)}")

    ctx.add_decision("SP-4 explain trace generated")
    return True


def sp5_policy_binding(ctx: ExecutionContext):
    policy = getattr(ctx, "policy", None)

    if not policy:
        ctx.add_violation("SP-5 blocked: missing policy")
        return False

    if not isinstance(policy, dict):
        ctx.add_violation("SP-5 blocked: invalid policy format")
        return False

    if "version" not in policy:
        ctx.add_violation("SP-5 blocked: policy version missing")
        return False

    ctx.policy_ok = True
    ctx.add_decision(
        f"SP-5 policy bound ({policy.get('source')} {policy.get('version')})"
    )
    return True
