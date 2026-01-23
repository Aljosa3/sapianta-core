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
from .sp8_rate_cost_guard import sp8_rate_cost_guard

# 👉 UC-2: Controlled LLM Answer
from runtime.use_cases.uc2_llm_controlled_answer import execute_uc2

# 🔒 GuardLifecycle invariant
from runtime.guard_lifecycle.errors import ProtocolViolation


class Orchestrator:
    """
    Minimal Orchestrator (MEP)

    ⚠️ NOT an entry-point.
    Must ONLY be invoked via GuardLifecycleOrchestrator.

    Guards
      → SP-1
      → SP-2
      → SP-8
      → EXECUTION (UC-2)
      → SP-3
      → SP-7
      → SP-4
      → SP-5
      → FINALIZE
      → SP-6
    """

    def run(self, ctx: ExecutionContext) -> ExecutionContext:

        # ============================================================
        # 🔒 HARD INVARIANT: Orchestrator is NOT an entry-point
        # ============================================================
        if getattr(ctx, "_origin", None) is None:
            raise ProtocolViolation(
                "Direct Orchestrator invocation is forbidden. "
                "Use GuardLifecycleOrchestrator."
            )

        # 1. Runtime Guards
        try:
            runtime_guards(ctx)
        except GuardViolation:
            return ctx

        # 2. Guards did NOT allow → MUST HALT
        if ctx.status != Status.ALLOW or ctx.phase != Phase.EXECUTION:
            ctx.finalize(
                status=Status.HALT,
                error="Execution not permitted by guards"
            )
            return ctx

        # 3. SP-1: Input sanity
        if not sp1_input_sanity(ctx):
            return ctx

        # 4. SP-2: Permission / intent
        if not sp2_permission_intent(ctx):
            return ctx

        # 5. SP-8: Rate / Cost guard (normative)
        if not sp8_rate_cost_guard(ctx):
            return ctx

        # 6. EXECUTION (UC-2)
        try:
            ctx.add_decision("Orchestrator execution started")

            ctx.result = execute_uc2(ctx)

            ctx.add_decision("Orchestrator execution completed")

            # 7. SP-3: Output sanity
            if not sp3_output_sanity(ctx):
                return ctx

            # 8. SP-7: Output redaction (NON-normative)
            sp7_output_redaction(ctx)

            # 9. SP-4: Explain / trace (NON-normative)
            sp4_explain_trace(ctx)

            # 10. SP-5: Policy binding
            if not sp5_policy_binding(ctx):
                return ctx

            # 11. FINALIZE — edini pravilen zaključek po ALLOW
            ctx.finalize(status=Status.FINAL, result=ctx.result)

            # 12. SP-6: Audit export (best-effort)
            sp6_audit_export(ctx, target="stdout")

            return ctx

        except Exception as e:
            # HARD_FAIL only for true runtime corruption
            ctx.add_violation(str(e))
            ctx.finalize(
                status=Status.HARD_FAIL,
                error=str(e)
            )
            return ctx
