from typing import Any


class PolicyEvaluator:
    """
    Minimal deterministic policy evaluator interface.

    Policy must return True (allow) or False (deny).
    No side effects allowed.
    """

    def evaluate(self, event_id: str, state: Any) -> bool:
        """
        Evaluate whether the given event is allowed
        for the provided state.

        Must be deterministic.
        """
        raise NotImplementedError("PolicyEvaluator.evaluate must be implemented.")
