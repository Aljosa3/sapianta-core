# PATH: sapianta_chat/tests/test_hasbt_enforcement_readonly.py
"""
READ-ONLY TEST HARNESS — HASBT ENFORCEMENT

This test suite verifies that HASBT enforcement is FAIL-CLOSED.

Constraints:
- NO filesystem writes
- NO WRITE-GATE interaction
- NO unlock
- NO side effects
- NO test doubles or mocks
"""

import pytest

from governance.hasbt import evaluate_hasbt, HASBTDeny


def test_hasbt_missing_payload_denies():
    """
    Missing payload must FAIL-CLOSED.

    Expected:
    - TypeError or HASBTDeny
    - Execution must not continue
    """
    with pytest.raises(Exception):
        evaluate_hasbt(None)


def test_hasbt_invalid_payload_type_denies():
    """
    Non-dict payload must FAIL-CLOSED.
    """
    with pytest.raises(HASBTDeny):
        evaluate_hasbt("not-a-dict")


def test_hasbt_missing_required_keys_denies():
    """
    Missing required schema keys must FAIL-CLOSED.
    """
    payload = {
        "hasbt_version": "0.1",
        # missing authorization_confirmed
    }

    with pytest.raises(HASBTDeny):
        evaluate_hasbt(payload)


def test_hasbt_authorization_not_confirmed_denies():
    """
    authorization_confirmed != True must FAIL-CLOSED.
    """
    payload = {
        "hasbt_version": "0.1",
        "authorization_confirmed": False,
        "authorization_actor": "human",
        "authorization_context": "test",
    }

    with pytest.raises(HASBTDeny):
        evaluate_hasbt(payload)


def test_hasbt_valid_payload_passes():
    """
    Explicitly confirmed authorization must PASS.

    PASS means:
    - function returns None
    - no exception raised
    - no state change
    """
    payload = {
        "hasbt_version": "0.1",
        "authorization_confirmed": True,
        "authorization_actor": "human",
        "authorization_context": "test",
    }

    result = evaluate_hasbt(payload)
    assert result is None
