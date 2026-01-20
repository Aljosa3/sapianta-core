from sapianta.modules.chat import ChatModule
from sapianta.modules.risk_assessment import RiskAssessmentModule
from sapianta.decision.decision import Decision
from sapianta.decision.decision_engine import DecisionEngine
from sapianta.execution.dry_run import DryRunExecutionAdapter


class DemoDecisionEngine(DecisionEngine):
    """
    Demo-only decision logic.

    This is NOT a real decision engine.
    It exists solely to prove architectural flow.
    """

    def evaluate(self, signals: dict, context: dict) -> Decision:
        risk_level = signals.get("risk_level", "unknown")

        if risk_level == "unknown":
            outcome = "HOLD"
        else:
            outcome = "ALLOW"

        return Decision(
            decision_id="demo-decision-002",
            outcome=outcome,
            authority="system",
            basis=["risk_assessment", f"jurisdiction:{context.get('jurisdiction')}"],
            binding=False
        )


def run_demo():
    print("\n=== SAPIANTA DEMO FLOW 2 ===\n")

    # 1. Chat input (pure communication)
    chat = ChatModule()
    user_input = "Ali je ta zahteva skladna z EU pravili?"
    chat_output = chat.run(user_input)

    print("Chat output:")
    print(chat_output)
    print()

    # 2. Minimal system context
    context = {
        "source": "demo_flow_2",
        "jurisdiction": "EU",
        "phase": "demo",
        "execution_allowed": False
    }

    # 3. Risk assessment
    risk_module = RiskAssessmentModule()
    risk_output = risk_module.run(
        intent=chat_output["intent"],
        context=context
    )

    print("Risk assessment output:")
    print(risk_output)
    print()

    # 4. Decision layer (explicit)
    decision_engine = DemoDecisionEngine()
    decision = decision_engine.evaluate(
        signals=risk_output,
        context=context
    )

    print("Decision output:")
    print({
        "decision_id": decision.decision_id,
        "outcome": decision.outcome,
        "authority": decision.authority,
        "basis": decision.basis,
        "binding": decision.binding
    })
    print()

    # 5. Execution adapter (dry-run, decision-bound)
    execution_adapter = DryRunExecutionAdapter()
    execution_output = execution_adapter.run(
        decision=decision,
        context=context
    )

    print("Execution adapter (dry-run) output:")
    print(execution_output)
    print()

    # 6. Explain (display-only)
    explain = {
        "status": "decided",
        "decision": decision.outcome,
        "note": "Decision evaluated. No execution performed."
    }

    print("Explain output:")
    print(explain)

    print("\n=== END DEMO FLOW 2 ===\n")


if __name__ == "__main__":
    run_demo()
