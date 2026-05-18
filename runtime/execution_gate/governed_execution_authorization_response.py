"""Governed downstream execution authorization responses."""

from __future__ import annotations

from .governed_execution_authority_token import create_execution_authority_token
from .governed_execution_authorization_chain import build_approval_chain
from .governed_execution_authorization_validator import validate_authorization_request
from .governed_execution_evidence import governed_execution_authorization_evidence
from .governed_execution_receipt import create_execution_receipt
from .governed_execution_replay import build_authorization_replay_identity


def authorize_downstream_execution(request: dict) -> dict:
    validation = validate_authorization_request(request)
    if not validation["valid"]:
        return {
            "status": "REJECTED",
            "requires_explicit_authorization": True,
            "validation": validation,
            "receipt": create_execution_receipt(token={}, authority_status="REJECTED", approval_chain=[]),
        }
    token = create_execution_authority_token(request=request)
    approval_chain = build_approval_chain(request=request, token=token)
    receipt = create_execution_receipt(token=token, authority_status="AUTHORIZED", approval_chain=approval_chain)
    replay_identity = build_authorization_replay_identity(request=request, token=token, approval_chain=approval_chain)
    return {
        "status": "AUTHORIZED",
        **token,
        "authorization_replay_identity": replay_identity,
        "approval_chain": approval_chain,
        "receipt": receipt,
        "validation": validation,
        "evidence": governed_execution_authorization_evidence(
            request=request,
            token=token,
            approval_chain=approval_chain,
            receipt=receipt,
        ),
    }
