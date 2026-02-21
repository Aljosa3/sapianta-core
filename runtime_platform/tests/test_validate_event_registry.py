from __future__ import annotations

from scripts.validation.validate_event_registry import validate_registry


def test_registry_minimal_valid_passes():
    data = {
        "registry_version": "v0.1",
        "layer": "Layer1",
        "domain_closed": True,
        "policy": {
            "unknown_event": "FAIL_CLOSED",
            "implicit_creation": "FORBIDDEN",
            "source_of_truth": "THIS_FILE_ONLY",
        },
        "events": [
            {"id": "EVT_NOOP", "description": "noop", "status": "ALLOWED"},
        ],
        "invariants": {
            "ids_unique": True,
            "ids_uppercase": True,
            "ids_prefix": "EVT_",
            "min_events": 1,
        },
    }
    errors = validate_registry(data)
    assert errors == []


def test_registry_missing_required_key_fails():
    data = {
        "registry_version": "v0.1",
        "layer": "Layer1",
        "domain_closed": True,
        "events": [],
        "invariants": {},
    }
    errors = validate_registry(data)
    assert len(errors) >= 1


def test_registry_duplicate_event_id_fails():
    data = {
        "registry_version": "v0.1",
        "layer": "Layer1",
        "domain_closed": True,
        "policy": {
            "unknown_event": "FAIL_CLOSED",
            "implicit_creation": "FORBIDDEN",
            "source_of_truth": "THIS_FILE_ONLY",
        },
        "events": [
            {"id": "EVT_X", "description": "x", "status": "ALLOWED"},
            {"id": "EVT_X", "description": "x2", "status": "ALLOWED"},
        ],
        "invariants": {
            "ids_unique": True,
            "ids_uppercase": True,
            "ids_prefix": "EVT_",
            "min_events": 1,
        },
    }
    errors = validate_registry(data)
    assert any("Duplicate event id" in e.message for e in errors)
