"""
KERNEL_INTROSPECTION_PROBE
Minimal, stateless kernel probe module.

This module exists solely to exercise the Module ↔ Kernel contract.
It contains no memory, no learning, and no adaptive behavior.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any
import uuid


# =========================
# Data structures (contract-aligned)
# =========================

@dataclass
class DecisionRequest:
    request_id: str
    actor: str
    user_input: str
    declared_intent: Optional[str]
    risk_level: str
    constraints: Optional[Dict[str, Any]]
    context: Optional[Dict[str, Any]]


@dataclass
class DecisionResponse:
    request_id: str
    outcome: str
    confidence: str
    constraints_applied: Optional[Dict[str, Any]]
    explanation: Dict[str, Any]
    guards: Dict[str, Any]
    observability: Dict[str, Any]


# =========================
# Kernel interface (placeholder)
# =========================

class KernelInterface:
    """
    Abstract boundary for kernel interaction.

    This is intentionally thin.
    The real kernel implementation must satisfy the contract spec.
    """

    def evaluate(self, request: DecisionRequest) -> DecisionResponse:
        raise NotImplementedError("KernelInterface.evaluate must be implemented by kernel")


# =========================
# Probe module
# =========================

class KernelIntrospectionProbe:
    ACTOR_ID = "KERNEL_INTROSPECTION_PROBE"

    def __init__(self, kernel: KernelInterface):
        self.kernel = kernel

    def run(
        self,
        user_input: str,
        declared_intent: Optional[str] = None,
        risk_level: str = "unknown",
        constraints: Optional[Dict[str, Any]] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> DecisionResponse:
        """
        Execute a single, stateless probe invocation.
        """

        request = DecisionRequest(
            request_id=self._new_request_id(),
            actor=self.ACTOR_ID,
            user_input=user_input,
            declared_intent=declared_intent,
            risk_level=risk_level,
            constraints=constraints,
            context=context,
        )

        response = self.kernel.evaluate(request)

        self._validate_response(response)
        self._emit_observability(response)

        return response

    # =========================
    # Internal helpers
    # =========================

    def _new_request_id(self) -> str:
        return str(uuid.uuid4())

    def _validate_response(self, response: DecisionResponse) -> None:
        """
        Minimal contract validation.
        This is not logic — it is safety.
        """
        required_fields = [
            "request_id",
            "outcome",
            "confidence",
            "explanation",
            "guards",
            "observability",
        ]

        for field in required_fields:
            if not hasattr(response, field):
                raise ValueError(f"Kernel response missing required field: {field}")

        if "trace_id" not in response.observability:
            raise ValueError("Kernel response missing observability.trace_id")

    def _emit_observability(self, response: DecisionResponse) -> None:
        """
        Minimal, allowed logging surface.
        No persistence, no aggregation.
        """
        trace_id = response.observability.get("trace_id")
        timestamp = response.observability.get("timestamp", datetime.utcnow().isoformat())

        print(
            f"[KERNEL_PROBE] trace_id={trace_id} "
            f"outcome={response.outcome} "
            f"confidence={response.confidence} "
            f"time={timestamp}"
        )
