# runtime/mep/runner.py

from context import ExecutionContext
from orchestrator import Orchestrator


def main():
    # 1. Ustvari Execution Context (MEP dovoljuje samo source="chat")
    ctx = ExecutionContext(
        source="chat",
        raw_input="Hello, Sapianta MEP"
    )

    # 2. Zaženi Orchestrator
    orchestrator = Orchestrator()
    final_ctx = orchestrator.run(ctx)

    # 3. Izpis končnega stanja
    print("\n=== MEP EXECUTION RESULT ===")
    print(f"Context ID : {final_ctx.context_id}")
    print(f"Status     : {final_ctx.status}")
    print(f"Phase      : {final_ctx.phase}")
    print(f"Result     : {final_ctx.result}")
    print(f"Error      : {final_ctx.error}")

    print("\nDecisions:")
    for d in final_ctx.decisions:
        print(f" - [{d['time']}] {d['note']}")

    print("\nViolations:")
    for v in final_ctx.violations:
        print(f" - [{v['time']}] {v['note']}")


if __name__ == "__main__":
    main()
