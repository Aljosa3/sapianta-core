from runtime.mep.context import ExecutionContext
from runtime.mep.orchestrator import Orchestrator


def main():
    """
    Entry point za MEP execution.
    Zaženemo ga iz root projekta kot modul:
        python -m runtime.mep.runner
    """

    # Minimalni testni kontekst
    ctx = ExecutionContext(
        source="chat",
        raw_input="Razloži razliko med odgovornostjo in avtoriteto."
    )

    orchestrator = Orchestrator()
    ctx = orchestrator.run(ctx)

    print("\n=== MEP EXECUTION RESULT ===")
    print("Context ID :", ctx.context_id)
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
