
from create_test_module_again import CreateTestModuleAgain


def test_basic():
    instance = CreateTestModuleAgain()
    result = instance.run({})
    assert result is not None
