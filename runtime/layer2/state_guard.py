from copy import deepcopy
from typing import Any

from runtime.layer2.exceptions import StateMutationError


class StateGuard:
    """
    Detects in-place mutation of original state.
    """

    def snapshot(self, state: Any) -> Any:
        return deepcopy(state)

    def validate_no_mutation(self, original_state: Any, snapshot: Any):
        if original_state != snapshot:
            raise StateMutationError("In-place state mutation detected.")
