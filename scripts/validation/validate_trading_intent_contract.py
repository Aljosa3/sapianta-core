#!/usr/bin/env python3
"""
Governance-level validation for TRADING_INTENT_CONTRACT_v0.1.json

Constraints:
- stdlib only
- deterministic
- exit 0 on pass, exit 1 on fail
"""

from __future__ import annotations

import json
import os
import re
import sys
from typing import Any, Dict, List


def _fail(msg: str) -> int:
    sys.stderr.write(msg.rstrip() + "\n")
    return 1


def _require_str_list(obj: Dict[str, Any], key: str) -> List[str]:
    v = obj.get(key)
    if not isinstance(v, list) or not all(isinstance(x, str) and x for x in v):
        raise ValueError(f"'{key}' must be a list of non-empty strings.")
    return v


def load_contract(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_contract_data(contract: Dict[str, Any]) -> None:
    if not isinstance(contract, dict):
        raise ValueError("Contract must be a JSON object.")

    if contract.get("contract_name") != "TRADING_INTENT_CONTRACT":
        raise ValueError("contract_name must be 'TRADING_INTENT_CONTRACT'.")

    if contract.get("contract_version") != "0.1":
        raise ValueError("contract_version must be '0.1'.")

    if contract.get("event_name") != "TRADING_INTENT_CREATED":
        raise ValueError("event_name must be 'TRADING_INTENT_CREATED'.")

    required_fields = _require_str_list(contract, "required_fields")
    optional_fields = _require_str_list(contract, "optional_fields")

    overlap = set(required_fields).intersection(optional_fields)
    if overlap:
        raise ValueError(f"required_fields and optional_fields overlap: {sorted(overlap)}")

    constraints = contract.get("constraints")
    if not isinstance(constraints, dict):
        raise ValueError("'constraints' must be an object.")

    action_enum = constraints.get("action_enum")
    timeframe_enum = constraints.get("timeframe_enum")
    symbol_pattern = constraints.get("symbol_pattern")
    max_notes_len = constraints.get("max_notes_len")

    if not isinstance(action_enum, list) or not all(isinstance(x, str) and x for x in action_enum):
        raise ValueError("constraints.action_enum must be a list of non-empty strings.")
    if action_enum != ["BUY", "SELL", "HOLD"]:
        raise ValueError("constraints.action_enum must be exactly ['BUY','SELL','HOLD'].")

    if not isinstance(timeframe_enum, list) or not all(isinstance(x, str) and x for x in timeframe_enum):
        raise ValueError("constraints.timeframe_enum must be a list of non-empty strings.")
    if timeframe_enum != ["1m", "5m", "15m", "1h", "4h", "1d"]:
        raise ValueError("constraints.timeframe_enum must be exactly ['1m','5m','15m','1h','4h','1d'].")

    if not isinstance(symbol_pattern, str) or not symbol_pattern:
        raise ValueError("constraints.symbol_pattern must be a non-empty string.")
    re.compile(symbol_pattern)

    if not isinstance(max_notes_len, int) or max_notes_len <= 0:
        raise ValueError("constraints.max_notes_len must be a positive integer.")

    must_have = {"intent_id", "decision_id", "action", "symbol", "timeframe"}
    if not must_have.issubset(set(required_fields)):
        raise ValueError(f"required_fields must include at least: {sorted(must_have)}")


def main(argv: List[str]) -> int:
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    default_path = os.path.join(
        repo_root, "governance", "domains", "trading", "TRADING_INTENT_CONTRACT_v0.1.json"
    )
    path = argv[1] if len(argv) > 1 else default_path

    try:
        contract = load_contract(path)
        validate_contract_data(contract)
    except Exception as e:
        return _fail(f"[TRADING_INTENT_CONTRACT_VALIDATE] FAIL: {e}")

    sys.stdout.write("[TRADING_INTENT_CONTRACT_VALIDATE] PASS\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
