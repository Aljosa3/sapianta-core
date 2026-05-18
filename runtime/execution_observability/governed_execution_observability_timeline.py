"""Deterministic execution lifecycle timeline."""

from __future__ import annotations


def build_execution_timeline(*, trace: dict) -> list[dict]:
    return [
        {"stage": "AUTHORIZATION", "status": trace["authorization_status"]},
        {"stage": "EXPIRATION", "status": trace["expiration_status"]},
        {"stage": "REVOCATION", "status": trace["revocation_status"]},
        {"stage": "HANDOFF_INTEGRITY", "status": trace["handoff_integrity_status"]},
        {"stage": "CONSUMER_RECEIPT", "status": trace["consumer_receipt_status"]},
        {"stage": "ADAPTER_RECEIPT", "status": trace["adapter_receipt_status"]},
        {"stage": "CLOSURE", "status": trace["deterministic_closure_status"]},
    ]
