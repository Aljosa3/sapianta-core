from sapianta.execution.types import ExecutionDecision, ExecutionResult
from sapianta.runtime.types import RuntimeDecision, RuntimeResult


class ExecutionGate:
    """
    Execution Gate:
    - edina dovoljena točka za execution
    - trenutno NO-OP
    - nikoli ne spreminja Runtime odločitve
    """

    def process(self, runtime_result: RuntimeResult) -> ExecutionResult:
        # Če runtime ne dovoli nadaljevanja → NO-OP
        if runtime_result.decision != RuntimeDecision.PROCEED:
            return ExecutionResult(
                decision=ExecutionDecision.NO_OP,
                runtime_result=runtime_result,
                note="Runtime halted execution"
            )

        # Tudi če runtime dovoli → še vedno NO-OP (za zdaj)
        return ExecutionResult(
            decision=ExecutionDecision.NO_OP,
            runtime_result=runtime_result,
            note="Execution gate present but execution disabled"
        )
