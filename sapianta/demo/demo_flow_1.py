from sapianta.modules.chat import ChatModule
from sapianta.modules.risk_assessment import RiskAssessmentModule
from sapianta.execution import DryRunExecutionAdapter


def run_demo():
    print("\n=== SAPIANTA DEMO FLOW 1 ===\n")

    # 1. Chat input (pure communication channel)
    chat = ChatModule()
    user_input = "Ali je ta zahteva skladna z EU pravili?"
    chat_output = chat.run(user_input)

    print("Chat output:")
    print(chat_output)
    print()

    # 2. Minimal system context (demo-only, non-decisional)
    context = {
        "source": "demo_flow_1",
        "jurisdiction": "EU",
        "phase": "demo",
        "execution_allowed": False
    }

    # 3. Risk assessment (system module, requires context)
    risk_module = RiskAssessmentModule()
    risk_output = risk_module.run(
        intent=chat_output["intent"],
        context=context
    )

    print("Risk assessment output:")
    print(risk_output)
    print()

    # 4. Explain (simulated, display-only)
    explain = {
        "status": "assessed",
        "risk_level": risk_output.get("risk_level", "unknown"),
        "note": "Assessment completed. No execution performed."
    }

    print("Explain output:")
    print(explain)
    print()

    # 5. Execution adapter (dry-run only, no real execution)
    adapter = DryRunExecutionAdapter()

    fake_decision = {
        "id": "demo-decision-001",
        "proposed_steps": [
            "Check applicable EU compliance framework",
            "Prepare non-binding assessment summary",
            "Notify user that no execution was performed"
        ]
    }

    execution_plan = adapter.run(
        decision=fake_decision,
        context=context
    )

    print("Execution adapter (dry-run) output:")
    print(execution_plan)

    print("\n=== END DEMO ===\n")


if __name__ == "__main__":
    run_demo()
