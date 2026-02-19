from runtime.layer2.state_transition_executor import StateTransitionExecutor


def test_transition_execution():
    executor = StateTransitionExecutor()

    def increment(state):
        return state + 1

    result = executor.execute("E1", 1, increment)
    assert result == 2
