
from create_simple_test_module_again import CreateSimpleTestModuleAgain


def test_basic():
    instance = CreateSimpleTestModuleAgain()
    result = instance.run({})
    assert result is not None
