from typing import List

from sapianta_hoi.execution.session_controller import SessionController
from sapianta_hoi.runtime_stub.event import Event


class ExecutionTraceResult:
    """
    Deterministic execution trace container.
    """

    def __init__(self, states: List[str]):
        self.states = states

    @property
    def final_state(self) -> str:
        return self.states[-1] if self.states else None

    def __repr__(self) -> str:
        return f"ExecutionTraceResult(states={self.states})"


def run_execution_trace(
    initial_state: str,
    events: List[Event],
) -> ExecutionTraceResult:
    """
    Execute deterministic event sequence
    over guarded SessionController.

    Raises:
        ValueError if transition invalid
        ValueError if state invariant violated
    """

    controller = SessionController(initial_state=initial_state)

    state_trace = [controller.current_state.state_name]

    for event in events:
        new_state = controller.dispatch(event)
        state_trace.append(new_state.state_name)

    return ExecutionTraceResult(states=state_trace)
