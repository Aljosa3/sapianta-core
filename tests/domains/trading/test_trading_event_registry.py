import json
import os
import importlib.util
from typing import Any, Dict


def _repo_root() -> str:
    # tests/domains/trading -> tests -> repo root
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def _load_validator_module():
    repo_root = _repo_root()
    script_path = os.path.join(repo_root, "scripts", "validation", "validate_trading_event_registry.py")
    spec = importlib.util.spec_from_file_location("validate_trading_event_registry", script_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


def _load_registry() -> Dict[str, Any]:
    repo_root = _repo_root()
    registry_path = os.path.join(
        repo_root, "governance", "domains", "trading", "TRADING_EVENT_REGISTRY_v0.1.json"
    )
    with open(registry_path, "r", encoding="utf-8") as f:
        return json.load(f)


def test_registry_loads():
    reg = _load_registry()
    assert isinstance(reg, dict)
    assert reg.get("registry_name") == "TRADING_EVENT_REGISTRY"
    assert reg.get("registry_version") == "0.1"
    assert isinstance(reg.get("events"), list)


def test_uniqueness_and_schema_pass():
    validator = _load_validator_module()
    reg = _load_registry()
    # should not raise
    validator.validate_registry_data(reg)


def test_intentional_failure_duplicate_event_name():
    validator = _load_validator_module()
    bad = {
        "registry_name": "TRADING_EVENT_REGISTRY",
        "registry_version": "0.1",
        "events": [
            {"event_name": "TRADING_SIGNAL_CANDIDATE", "version": "0.1", "required_fields": [], "optional_fields": []},
            {"event_name": "TRADING_SIGNAL_CANDIDATE", "version": "0.1", "required_fields": [], "optional_fields": []},
        ],
    }
    try:
        validator.validate_registry_data(bad)
        assert False, "Expected validation to fail on duplicate event_name"
    except ValueError as e:
        assert "Duplicate event_name" in str(e)


def test_intentional_failure_bad_field_list_types():
    validator = _load_validator_module()
    bad = {
        "registry_name": "TRADING_EVENT_REGISTRY",
        "registry_version": "0.1",
        "events": [
            {
                "event_name": "TRADING_DECISION_PROPOSED",
                "version": "0.1",
                "required_fields": "not-a-list",
                "optional_fields": [],
            }
        ],
    }
    try:
        validator.validate_registry_data(bad)
        assert False, "Expected validation to fail on required_fields not being a list"
    except ValueError as e:
        assert "required_fields must be a list" in str(e)