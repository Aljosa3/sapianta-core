"""Deterministic mock dispatch only."""

from __future__ import annotations


def perform_mock_dispatch() -> dict:
    return {
        "dispatch_status": "MOCK_DISPATCH_ACCEPTED",
        "dispatch_mode": "DETERMINISTIC_PRE_EXECUTION_SIMULATION",
        "execution_performed": False,
    }
