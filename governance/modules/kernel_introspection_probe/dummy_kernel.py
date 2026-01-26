"""
DummyKernel
Contract-valid placeholder kernel implementation.

Purpose:
- allow end-to-end execution of KERNEL_INTROSPECTION_PROBE
- validate contract shape
- demonstrate guard + observability flow

This is NOT a real kernel.
"""

from datetime import datetime
from typing import Dict, Any
import uuid

from .probe import DecisionRequest, DecisionResponse, KernelInterface


class DummyKernel(KernelInterface):
    """
    Deterministic, stateless kernel stub.
    """

    def evaluate(self, request: DecisionRequest) -> DecisionResponse:
        trace_id = self._new_trace_id()

        # --- very simple deterministic behavior ---
        if "forbidden" in request.user_input.lower():
            outcome = "deny"
            confidence = "high"
            guards = {
                "triggered": ["G_POLICY_FORBIDDEN_CONTENT"],
                "notes": "Explicit forbidden keyword detected."
            }
        elif request.risk_level == "high":
            outcome = "constrain"
            confidence = "medium"
            guards = {
                "triggered": ["G_RISK_HIGH"],
                "notes": "High risk input requires constraints."
            }
        else:
            outcome = "allow"
            confidence = "medium"
            guards = {
                "triggered": [],
                "notes": None
            }

        explanation = {
            "summary": f"DummyKernel decision: {outcome}",
            "key_factors": [
                f"risk_level={request.risk_level}",
                "dummy keyword checks only"
            ]
        }

        observability = {
            "trace_id": trace_id,
            "timestamp": datetime.utcnow().isoformat(),
            "event_ids": [f"EV-{uuid.uuid4()}"]
        }

        return DecisionResponse(
            request_id=request.request_id,
            outcome=outcome,
            confidence=confidence,
            constraints_applied=None if outcome != "constrain" else {
                "output_mode": "safe_summary_only"
            },
            explanation=explanation,
            guards=guards,
            observability=observability
        )

    def _new_trace_id(self) -> str:
        return f"TRACE-{uuid.uuid4()}"
