from runtime.layer2.exceptions import (
    ControlLayerError,
    PolicyDeniedError,
    ContractViolationError,
    PreInvariantViolationError,
    PostInvariantViolationError,
)


def test_exception_hierarchy():
    assert issubclass(PolicyDeniedError, ControlLayerError)
    assert issubclass(ContractViolationError, ControlLayerError)
    assert issubclass(PreInvariantViolationError, ControlLayerError)
    assert issubclass(PostInvariantViolationError, ControlLayerError)
