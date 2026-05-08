from runtime.development.dev_governance_gate import DevGovernanceGate
from runtime.engine.decision_envelope_builder import build_decision_envelope


def test_decision_envelope_is_replay_stable():
    proposal = {
        "domain_id": "trading",
        "proposal_id": "P-001",
        "strategy_reference": "strategy-a",
        "timestamp": "2026-05-08T00:00:00Z",
        "action": {"type": "BUY", "quantity": 1},
        "risk_context": {"capital_at_risk": 10},
    }
    policy_result = {
        "decision": "APPROVE",
        "policy_trace": [{"rule": "max_quantity", "result": "PASS"}],
    }

    first = build_decision_envelope(proposal, policy_result)
    second = build_decision_envelope(proposal, policy_result)

    assert first == second
    assert first["decision_id"].startswith("DEC-")


def test_governance_approval_placeholder_fails_closed():
    gate = DevGovernanceGate()

    assert gate.final_decision(DevGovernanceGate.REVIEW) == DevGovernanceGate.REVIEW
    assert gate.request_approval({}) is False
    assert gate.request_approval({
        "approved_by_human": "operator",
        "approval_id": "APPROVAL-001",
    }) is True
