from typing import Any, List, Callable

from runtime.layer2.exceptions import (
    PreInvariantViolationError,
    PostInvariantViolationError,
)


class InvariantGuard:
    """
    Deterministic invariant validator.
    """

    def validate_pre(
        self,
        state: Any,
        invariants: List[Callable[[Any], bool]],
    ):
        for invariant in invariants:
            if not invariant(state):
                raise PreInvariantViolationError(
                    f"Pre-invariant failed: {invariant.__name__}"
                )

    def validate_post(
        self,
        state: Any,
        invariants: List[Callable[[Any], bool]],
    ):
        for invariant in invariants:
            if not invariant(state):
                raise PostInvariantViolationError(
                    f"Post-invariant failed: {invariant.__name__}"
                )
