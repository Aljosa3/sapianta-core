"""Governed intent transfer response construction."""

from .governed_intent_transfer_boundary import transfer_boundary_state
from .governed_intent_transfer_evidence import governed_intent_transfer_evidence
from .governed_intent_transfer_package import build_intent_transfer_package
from .governed_intent_transfer_replay import build_intent_transfer_replay_identity
from .governed_intent_transfer_validator import validate_intent_transfer_request


def _blocked(request: dict, errors: list[dict]) -> dict:
    return {
        "status": "BLOCKED",
        "package": None,
        "replay_visible": True,
        "requires_preview": True,
        "requires_confirmation": True,
        "execution_authority": False,
        "chatgpt_authority": False,
        "boundary_state": transfer_boundary_state(),
        "validation": {"valid": False, "errors": errors},
        "closure": "BLOCKED",
    }


def create_governed_intent_transfer(request: dict) -> dict:
    validation = validate_intent_transfer_request(request)
    if not validation["valid"]:
        return _blocked(request, validation["errors"])
    package = build_intent_transfer_package(request=request)
    replay_identity = build_intent_transfer_replay_identity(request=request, package=package)
    return {
        "status": "TRANSFER_READY",
        "package": package,
        "transfer_identity": package["transfer_identity"],
        "replay_identity": replay_identity,
        "replay_visible": True,
        "requires_preview": True,
        "requires_confirmation": True,
        "execution_authority": False,
        "chatgpt_authority": False,
        "boundary_state": package["boundary_state"],
        "validation": validation,
        "closure": "PREVIEW_ONLY",
        "evidence": governed_intent_transfer_evidence(
            request=request,
            package=package,
            replay_identity=replay_identity,
        ),
    }
