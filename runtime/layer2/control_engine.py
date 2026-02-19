from typing import Any, Callable, Dict

from runtime.layer2.policy_evaluator import PolicyEvaluator
from runtime.layer2.state_transition_executor import StateTransitionExecutor
from runtime.layer2.audit_trace_collector import AuditTraceCollector


class ControlEngine:
    """
    Deterministic Control Engine (Layer 2)

    Orchestrates:
    - Policy evaluation
    - State transition
    - Audit trace collection

    Fail-closed:
    - If policy denies → no transition
    - If transition invalid → exception
    """

    def __init__(
        self,
        policy_evaluator: PolicyEvaluator,
        transition_executor: StateTransitionExecutor,
        audit_collector: AuditTraceCollector,
    ):
        if not policy_evaluator:
            raise ValueError("PolicyEvaluator required.")
        if not transition_executor:
            raise ValueError("StateTransitionExecutor required.")
        if not audit_collector:
            raise ValueError("AuditTraceCollector required.")

        self._policy = policy_evaluator
        self._executor = transition_executor
        self._audit = audit_collector

    def process(
        self,
        event_id: str,
        state: Any,
        transition_fn: Callable[[Any], Any],
    ) -> Dict[str, Any]:

        if not event_id:
            raise ValueError("event_id must be provided.")

        allowed = self._policy.evaluate(event_id, state)

        if not allowed:
            # Fail-closed: state unchanged
            return self._audit.collect(
                event_id=event_id,
                previous_state=state,
                new_state=state,
                allowed=False,
            )

        new_state = self._executor.execute(
            event_id=event_id,
            state=state,
            transition_fn=transition_fn,
        )

        return self._audit.collect(
            event_id=event_id,
            previous_state=state,
            new_state=new_state,
            allowed=True,
        )
