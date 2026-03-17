from runtime.development.dev_governance_gate import DevGovernanceGate


def test_block_dangerous_task():

    gate = DevGovernanceGate()

    task = {
        "task_type": "implementation",
        "idea": "delete kernel validation logic",
    }

    decision = gate.evaluate(task)

    assert decision == DevGovernanceGate.BLOCK


def test_review_sensitive_task():

    gate = DevGovernanceGate()

    task = {
        "task_type": "implementation",
        "idea": "improve governance policy engine",
    }

    decision = gate.evaluate(task)

    assert decision == DevGovernanceGate.REVIEW


def test_allow_bugfix():

    gate = DevGovernanceGate()

    task = {
        "task_type": "bugfix",
        "idea": "fix replay bug",
    }

    decision = gate.evaluate(task)

    assert decision == DevGovernanceGate.ALLOW