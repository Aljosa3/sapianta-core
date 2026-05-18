"""Read-only governed execution observability responses."""

from __future__ import annotations

from .governed_execution_observability_evidence import governed_execution_observability_evidence
from .governed_execution_observability_replay import build_execution_observability_replay_identity
from .governed_execution_observability_summary import summarize_execution_trace
from .governed_execution_observability_timeline import build_execution_timeline
from .governed_execution_observability_trace import build_execution_trace
from .governed_execution_observability_validator import validate_execution_observability_request


def observe_governed_execution(request: dict) -> dict:
    validation = validate_execution_observability_request(request)
    replay_identity = build_execution_observability_replay_identity(request=request, validation=validation)
    if not validation["valid"]:
        return {
            "status": "BLOCKED",
            "validation": validation,
            "read_only": True,
            "execution_triggered": False,
            "replay_identity": replay_identity,
        }
    trace = build_execution_trace(request=request, validation=validation, replay_identity=replay_identity)
    timeline = build_execution_timeline(trace=trace)
    return {
        "status": "OBSERVED",
        "read_only": True,
        "execution_triggered": False,
        "replay_identity": replay_identity,
        "trace": trace,
        "timeline": timeline,
        "summary": summarize_execution_trace(trace=trace),
        "validation": validation,
        "evidence": governed_execution_observability_evidence(request=request, trace=trace, timeline=timeline),
    }
