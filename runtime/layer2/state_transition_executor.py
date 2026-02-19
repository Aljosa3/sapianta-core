from typing import Any, Callable


class StateTransitionExecutor:
    """
    Deterministic state transition executor.

    Applies a provided transition function to state.
    Transition function must be pure.
    """

    def execute(
        self,
        event_id: str,
        state: Any,
        transition_fn: Callable[[Any], Any],
    ) -> Any:
        if transition_fn is None:
            raise ValueError("Transition function must be provided.")

        new_state = transition_fn(state)

        if new_state is None:
            raise ValueError("Transition function returned invalid state.")

        return new_state
