import json
import os
import importlib.util
from typing import Any, Dict


def _repo_root() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def _load_validator_module():
    repo_root = _repo_root()
    script_path = os.path.join(repo_root, "scripts", "validation", "validate_trading_decision_contract.py")
    spec = importlib.util.spec_from_file_location("validate_trading_decision_contract", script_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


def _load_contract() -> Dict[str, Any]:
    repo_root = _repo_root()
    path = os.path.join(repo_root, "governance", "domains", "trading", "TRADING_DECISION_CONTRACT_v0.1.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def test_contract_loads():
    c = _load_contract()
    assert c["contract_name"] == "TRADING_DECISION_CONTRACT"
    assert c["contract_version"] == "0.1"
    assert c["event_name"] == "TRADING_DECISION_PROPOSED"


def test_contract_validator_passes():
    v = _load_validator_module()
    c = _load_contract()
    v.validate_contract_data(c)


def test_fail_overlap_required_optional():
    v = _load_validator_module()
    bad = {
        "contract_name": "TRADING_DECISION_CONTRACT",
        "contract_version": "0.1",
        "event_name": "TRADING_DECISION_PROPOSED",
        "required_fields": ["decision_id", "action"],
        "optional_fields": ["action"],
        "constraints": {
            "action_enum": ["BUY", "SELL", "HOLD"],
            "timeframe_enum": ["1m", "5m", "15m", "1h", "4h", "1d"],
            "symbol_pattern": "^[A-Z0-9._-]{1,20}$",
            "max_rationale_len": 1000
        }
    }
    try:
        v.validate_contract_data(bad)
        assert False, "expected overlap failure"
    except ValueError as e:
        assert "overlap" in str(e)


def test_fail_bad_action_enum():
    v = _load_validator_module()
    bad = {
        "contract_name": "TRADING_DECISION_CONTRACT",
        "contract_version": "0.1",
        "event_name": "TRADING_DECISION_PROPOSED",
        "required_fields": ["decision_id", "signal_id", "action", "symbol", "timeframe"],
        "optional_fields": ["rationale"],
        "constraints": {
            "action_enum": ["LONG", "SHORT"],
            "timeframe_enum": ["1m", "5m", "15m", "1h", "4h", "1d"],
            "symbol_pattern": "^[A-Z0-9._-]{1,20}$",
            "max_rationale_len": 1000
        }
    }
    try:
        v.validate_contract_data(bad)
        assert False, "expected action_enum failure"
    except ValueError as e:
        assert "action_enum" in str(e)


def test_fail_bad_symbol_regex():
    v = _load_validator_module()
    bad = {
        "contract_name": "TRADING_DECISION_CONTRACT",
        "contract_version": "0.1",
        "event_name": "TRADING_DECISION_PROPOSED",
        "required_fields": ["decision_id", "signal_id", "action", "symbol", "timeframe"],
        "optional_fields": ["rationale"],
        "constraints": {
            "action_enum": ["BUY", "SELL", "HOLD"],
            "timeframe_enum": ["1m", "5m", "15m", "1h", "4h", "1d"],
            "symbol_pattern": "([",  # invalid regex
            "max_rationale_len": 1000
        }
    }
    try:
        v.validate_contract_data(bad)
        assert False, "expected regex compile failure"
    except Exception as e:
        # regex compile raises re.error, caught as Exception in validator usage
        assert "unterminated" in str(e).lower() or "regex" in str(e).lower()
