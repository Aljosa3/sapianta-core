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
from .sp7_output_redaction import sp7_output_redaction

# 👉 UC-2: Controlled LLM Answer
from runtime.use_cases.uc2_llm_controlled_answer import execute_uc2


class Orchestrator:
    """
    Minimal Orchestrator (MEP)

    Execution order (normatively enforced):

    Guards
      → SP-1 (Input Sanity)
      → SP-2 (Permission / Intent)
      → EXECUTION (UC-2)
      → SP-3 (Output Sanity)
      → SP-7 (Output Redaction / Safety)   [non-normative]
      → SP-4 (Explain / Trace)             [post-decision]
      → SP-5 (Policy Binding)
      → FINALIZE (normative closure)
      → SP-6 (Audit export, best-effort)

    NOTE:
    Explain, redaction and audit layers MUST NOT influence normative decisions.
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

        # 5. EXECUTION (UC-2: Controlled LLM Answer)
        try:
            ctx.add_decision("Orchestrator execution started")

            # 🔒 UC-2 je izvedbena enota, ne avtoriteta
            ctx.result = execute_uc2(ctx)

            ctx.add_decision("Orchestrator execution completed")

            # 6. SP-3: Output sanity
            if not sp3_output_sanity(ctx):
                return ctx

            # 7. SP-7: Output redaction / safety (NON-NORMATIVE)
            # Nikoli ne blokira, nikoli ne spreminja statusa
            sp7_output_redaction(ctx)

            # 8. SP-4: Explain / trace (post-decision artifact)
            if not sp4_explain_trace(ctx):
                return ctx

            # 9. SP-5: Policy binding
            if not sp5_policy_binding(ctx):
                return ctx

            # 10. FINALIZE (normative closure)
            ctx.finalize(status=Status.FINAL, result=ctx.result)

            # 11. SP-6: Audit export (best-effort, AFTER finalize)
            sp6_audit_export(ctx, target="stdout")

            return ctx

        except Exception as e:
            ctx.add_violation(str(e))
            ctx.finalize(
                status=Status.HARD_FAIL,
                error=str(e)
            )
            return ctx
