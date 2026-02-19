from typing import Any, Callable, List, Type

from runtime.layer2.exceptions import ContractViolationError


class TransitionContract:
    """
    Formal deterministic transition contract.
    """

    def __init__(
        self,
        event_id: str,
        state_type: Type,
        transition_fn: Callable[[Any], Any],
        pre_invariants: List[Callable[[Any], bool]],
        post_invariants: List[Callable[[Any], bool]],
    ):

        if not event_id:
            raise ContractViolationError("event_id must be defined.")

        if state_type is None:
            raise ContractViolationError("state_type must be defined.")

        if transition_fn is None:
            raise ContractViolationError("transition_fn must be defined.")

        self.event_id = event_id
        self.state_type = state_type
        self.transition_fn = transition_fn
        self.pre_invariants = list(pre_invariants or [])
        self.post_invariants = list(post_invariants or [])

    def validate_event(self, event_id: str):
        if event_id != self.event_id:
            raise ContractViolationError("Event ID does not match contract.")

    def validate_state_type(self, state: Any):
        if not isinstance(state, self.state_type):
            raise ContractViolationError("State type does not match contract.")
