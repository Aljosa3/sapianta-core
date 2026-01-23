# runtime/mep/runner.py

from runtime.guard_lifecycle.orchestrator import GuardLifecycleOrchestrator
from runtime.guard_lifecycle.modes import ExecutionMode
from runtime.guard_lifecycle.errors import ProtocolViolation

from runtime.mep.orchestrator import Orchestrator
from runtime.mep.context import Phase


def main():
    """
    Canonical MEP entry point.

    Execution MUST pass through GuardLifecycle.
    Direct calls to Orchestrator.run(ctx) are forbidden.
    """

    # --- Build canonical request ---
    request = {
        "execution_mode": ExecutionMode.EXECUTION.value,
        "source": "chat",
        "raw_input": "Razloži razliko med odgovornostjo in avtoriteto."
    }

    try:
        # --- ENTER GUARD LIFECYCLE (SINGLE EXECUTION GATE) ---
        ctx = GuardLifecycleOrchestrator.run(request)

        # --- HARD CHECK: execution allowed ---
        if ctx.phase != Phase.EXECUTION:
            raise ProtocolViolation(
                f"MEP execution attempted outside EXECUTION phase (phase={ctx.phase})"
            )

        # --- Delegate to MEP orchestrator ---
        orchestrator = Orchestrator()
        ctx = orchestrator.run(ctx)

    except ProtocolViolation as e:
        print("\n=== GUARD LIFECYCLE VIOLATION ===")
        print(str(e))
        return

    # --- Output ---
    print("\n=== MEP EXECUTION RESULT ===")
    print("Context ID :", ctx.context_id)
    print("Origin     :", ctx._origin)
    print("Status     :", ctx.status)
    print("Phase      :", ctx.phase)
    print("Result     :", ctx.result)
    print("Error      :", ctx.error)

    print("\nDecisions:")
    for d in ctx.decisions:
        print(f" - [{d['time']}] {d['note']}")

    print("\nViolations:")
    for v in ctx.violations:
        print(f" - [{v['time']}] {v['note']}")


if __name__ == "__main__":
    main()
