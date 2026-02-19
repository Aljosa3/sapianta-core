from typing import Any, Dict

from runtime.layer2.policy_evaluator import PolicyEvaluator
from runtime.layer2.state_transition_executor import StateTransitionExecutor
from runtime.layer2.audit_trace_collector import AuditTraceCollector
from runtime.layer2.transition_contract import TransitionContract
from runtime.layer2.invariant_guard import InvariantGuard
from runtime.layer2.state_guard import StateGuard
from runtime.layer2.exceptions import PolicyDeniedError


class ControlEngine:
    """
    Deterministic Control Engine (Layer 2.3)

    Enforces:
    - Policy
    - TransitionContract validation
    - Pre-invariants
    - No in-place mutation
    - Transition execution
    - Post-invariants
    - Audit trace
    """

    def __init__(
        self,
        policy_evaluator: PolicyEvaluator,
        transition_executor: StateTransitionExecutor,
        audit_collector: AuditTraceCollector,
    ):
        self._policy = policy_evaluator
        self._executor = transition_executor
        self._audit = audit_collector
        self._invariant_guard = InvariantGuard()
        self._state_guard = StateGuard()

    def process(
        self,
        event_id: str,
        state: Any,
        contract: TransitionContract,
    ) -> Dict[str, Any]:

        if not self._policy.evaluate(event_id, state):
            raise PolicyDeniedError("Policy denied execution.")

        contract.validate_event(event_id)
        contract.validate_state_type(state)

        self._invariant_guard.validate_pre(state, contract.pre_invariants)

        snapshot = self._state_guard.snapshot(state)

        new_state = self._executor.execute(
            event_id=event_id,
            state=state,
            transition_fn=contract.transition_fn,
        )

        self._state_guard.validate_no_mutation(state, snapshot)

        self._invariant_guard.validate_post(new_state, contract.post_invariants)

        return self._audit.collect(
            event_id=event_id,
            previous_state=state,
            new_state=new_state,
            allowed=True,
        )
