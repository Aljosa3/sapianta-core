import pytest

try:
    from runtime.development.generated.test_syntax import add
except ModuleNotFoundError:
    add = None


def test_add_logic_fixed():
    if add is None:
        pytest.skip("generated module not present")

    assert add(1, 2) == 3
