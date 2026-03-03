# /home/pisarna/work/sapianta/sapianta_system/tests/runtime/test_block3_boundary_validator.py

import pytest
from runtime.validation.block3_boundary_validator import (
    Block3BoundaryValidator,
    Block3BoundaryViolation
)


def test_explanation_pass():
    text = "Result: REJECTED. Triggered rules: R-07. DTI=0.51 (>0.45)."
    Block3BoundaryValidator.validate_explanation(text)


def test_explanation_fail():
    text = "I recommend rejection due to macro risk."
    with pytest.raises(Block3BoundaryViolation):
        Block3BoundaryValidator.validate_explanation(text)


def test_deliberation_pass():
    text = "Recommendation: REQUEST_MORE_INFO due to sector volatility."
    Block3BoundaryValidator.validate_deliberation(text)


def test_deliberation_fail():
    text = "Rule R-07 triggered the rejection."
    with pytest.raises(Block3BoundaryViolation):
        Block3BoundaryValidator.validate_deliberation(text)