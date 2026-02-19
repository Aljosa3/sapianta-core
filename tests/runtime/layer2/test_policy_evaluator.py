from runtime.layer2.policy_evaluator import PolicyEvaluator


class AllowAllPolicy(PolicyEvaluator):
    def evaluate(self, event_id, state):
        return True


def test_policy_allows():
    policy = AllowAllPolicy()
    assert policy.evaluate("E1", {}) is True
