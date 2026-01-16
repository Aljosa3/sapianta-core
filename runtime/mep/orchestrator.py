from .context import ExecutionContext, Status, Phase
from .guards import runtime_guards, GuardViolation
from .sp_passes import (
    sp1_input_sanity,
    sp2_permission_intent,
    sp3_output_sanity,
    sp4_explain_trace,
    sp5_policy_binding
)
from .sp6_audit_export import sp6_audit_export


class Orchestrator:
    """
    Minimal Orchestrator (MEP)

    Execution order (normatively enforced):

    Guards
      → SP-1 (Input Sanity)
      → SP-2 (Permission / Intent)
      → EXECUTION (decision + result)
      → SP-3 (Output Sanity)
      → SP-4 (Explain / Trace)        [post-decision]
      → SP-5 (Policy Binding)
      → FINALIZE (normative closure)
      → SP-6 (Audit export, best-effort)

    NOTE:
    Explain and audit layers MUST NOT influence normative decisions.
    """

    def run(self, ctx: ExecutionContext) -> ExecutionContext:

        # 1. Runtime Guards
        try:
            runtime_guards(ctx)
        except GuardViolation:
            return ctx

        # 2. Guard-based permission check
        if ctx.status != Status.ALLOW or ctx.phase != Phase.EXECUTION:
            ctx.finalize(
                status=Status.HALT,
                error="Execution not permitted after guards"
            )
            return ctx

        # 3. SP-1: Input sanity
        if not sp1_input_sanity(ctx):
            return ctx

        # 4. SP-2: Permission / intent
        if not sp2_permission_intent(ctx):
            return ctx

        # 5. EXECUTION (normative decision path)
        try:
            ctx.add_decision("Orchestrator execution started")

            ctx.result = {
                "message": (
                    "MEP execution completed successfully "
                    "(with SP-1 + SP-2 + SP-3 + SP-4 + SP-5 + SP-6)"
                )
            }

            ctx.add_decision("Orchestrator execution completed")

            # 6. SP-3: Output sanity
            if not sp3_output_sanity(ctx):
                return ctx

            # 7. SP-4: Explain / trace (post-decision artifact)
            if not sp4_explain_trace(ctx):
                return ctx

            # 8. SP-5: Policy binding
            if not sp5_policy_binding(ctx):
                return ctx

            # 9. FINALIZE (normative closure)
            ctx.finalize(status=Status.FINAL, result=ctx.result)

            # 10. SP-6: Audit export (best-effort, AFTER finalize)
            sp6_audit_export(ctx, target="stdout")

            return ctx

        except Exception as e:
            ctx.add_violation(str(e))
            ctx.finalize(
                status=Status.HARD_FAIL,
                error=str(e)
            )
            return ctx
