
from test_execution_stability import TestExecutionStability


def test_basic():
    instance = TestExecutionStability()
    result = instance.run({})
    assert result is not None
