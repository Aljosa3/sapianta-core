# runtime/mep/orchestrator.py

from context import ExecutionContext, Status, Phase
from guards import runtime_guards, GuardViolation


class Orchestrator:
    """
    Minimal Orchestrator (MEP)
    Skladno z F53_ORCHESTRATOR.md
    """

    def __init__(self):
        pass

    def run(self, ctx: ExecutionContext) -> ExecutionContext:
        """
        Izvede celoten execution tok na podlagi Execution Contexta.
        """
        # 1. Zaženi runtime guards
        try:
            runtime_guards(ctx)
        except GuardViolation:
            # Guards so že ustavili ali zavrnili kontekst
            return ctx

        # 2. Preveri, ali je dovoljeno izvajanje
        if ctx.status != Status.ALLOW or ctx.phase != Phase.EXECUTION:
            ctx.finalize(
                status=Status.HALT,
                error="Execution not permitted after guards"
            )
            return ctx

        # 3. Minimalna izvedba (MEP nima dejanskih korakov)
        try:
            ctx.add_decision("Orchestrator execution started")

            # Tukaj bi v prihodnje klicali module / LLM / korake
            # MEP: simuliramo uspešen zaključek
            result = {
                "message": "MEP execution completed successfully"
            }

            ctx.add_decision("Orchestrator execution completed")
            ctx.finalize(
                status=Status.FINAL,
                result=result
            )
            return ctx

        except Exception as e:
            # Vsaka nepredvidena napaka → HARD_FAIL
            ctx.add_violation(str(e))
            ctx.finalize(
                status=Status.HARD_FAIL,
                error=str(e)
            )
            return ctx
