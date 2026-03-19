
from fix_broken_module import FixBrokenModule


def test_basic():
    instance = FixBrokenModule()
    result = instance.run({})
    assert result is not None
