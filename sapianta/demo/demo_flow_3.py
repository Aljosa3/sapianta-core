from sapianta.modules.chat import ChatModule
from sapianta.modules.risk_assessment import RiskAssessmentModule

from sapianta.decision.decision import Decision
from sapianta.decision.decision_engine import DecisionEngine

from sapianta.execution.dry_run import DryRunExecutionAdapter
from sapianta.execution.gate import ExecutionGate


class DemoDecisionEngine(DecisionEngine):
    """
    Demo-only decision logic.
    Proves that Decision governs execution.
    """

    def evaluate(self, signals: dict, context: dict) -> Decision:
        risk_level = signals.get("risk_level", "unknown")

        outcome = "HOLD" if risk_level == "unknown" else "ALLOW"

        return Decision(
            decision_id="demo-decision-003",
            outcome=outcome,
            authority="system",
            basis=["risk_assessment", f"jurisdiction:{context.get('jurisdiction')}"],
            binding=False
        )


def run_demo():
    print("\n=== SAPIANTA DEMO FLOW 3 (ExecutionGate enforced) ===\n")

    # 1. Chat → Intent
    chat = ChatModule()
    chat_output = chat.run("Ali je ta zahteva skladna z EU pravili?")

    # 2. Context
    context = {
        "source": "demo_flow_3",
        "jurisdiction": "EU",
        "phase": "demo",
        "execution_allowed": False
    }

    # 3. Risk
    risk_module = RiskAssessmentModule()
    risk_output = risk_module.run(
        intent=chat_output["intent"],
        context=context
    )

    # 4. Decision
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
        "binding": decision.binding
    })
    print()

    # 5a. NEGATIVE TEST — direct adapter call (must fail)
    adapter = DryRunExecutionAdapter()
    try:
        print("Attempting direct execution adapter call (should FAIL)...")
        adapter.run(decision=None, context=context)
    except Exception as e:
        print("Direct adapter call blocked as expected:")
        print(str(e))
    print()

    # 5b. POSITIVE TEST — via ExecutionGate (must succeed)
    gate = ExecutionGate(adapter)
    execution_output = gate.run(
        decision=decision,
        context=context
    )

    print("Execution via gate (dry-run) output:")
    print(execution_output)
    print()

    print("=== END DEMO FLOW 3 ===\n")


if __name__ == "__main__":
    run_demo()
