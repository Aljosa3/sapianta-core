# runtime/mep/orchestrator.py

from context import ExecutionContext, Status, Phase
from guards import runtime_guards, GuardViolation
from sp_passes import (
    sp1_input_sanity,
    sp2_permission_intent,
    sp3_output_sanity
)


class Orchestrator:
    """
    Minimal Orchestrator (MEP)
    Guards → SP-1 → SP-2 → Execution → SP-3 → FINAL
    """

    def run(self, ctx: ExecutionContext) -> ExecutionContext:

        # 1. Runtime Guards
        try:
            runtime_guards(ctx)
        except GuardViolation:
            return ctx

        # 2. Dovoljenost po guardih
        if ctx.status != Status.ALLOW or ctx.phase != Phase.EXECUTION:
            ctx.finalize(status=Status.HALT, error="Execution not permitted after guards")
            return ctx

        # 3. SP-1
        if not sp1_input_sanity(ctx):
            return ctx

        # 4. SP-2
        if not sp2_permission_intent(ctx):
            return ctx

        # 5. Execution
        try:
            ctx.add_decision("Orchestrator execution started")

            ctx.result = {
                "message": "MEP execution completed successfully (with SP-1 + SP-2 + SP-3)"
            }

            ctx.add_decision("Orchestrator execution completed")

            # 6. SP-3
            if not sp3_output_sanity(ctx):
                return ctx

            ctx.finalize(status=Status.FINAL, result=ctx.result)
            return ctx

        except Exception as e:
            ctx.add_violation(str(e))
            ctx.finalize(status=Status.HARD_FAIL, error=str(e))
            return ctx
