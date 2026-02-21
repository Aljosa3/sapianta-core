#!/usr/bin/env python3

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

REGISTRY_PATH = Path("governance/registry/EVENT_REGISTRY_v0.1.json")

@dataclass(frozen=True)
class ValidationError:
    message: str

def _fail(errors: List[ValidationError]) -> int:
    print("L1_EVENT_REGISTRY_VALIDATION: FAIL")
    for e in errors:
        print(f"- {e.message}")
    return 2

def _pass() -> int:
    print("L1_EVENT_REGISTRY_VALIDATION: PASS")
    return 0

def _load_registry(path: Path) -> Dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        raw = path.read_text(encoding="utf-8")
        return json.loads(raw)
    except Exception:
        return None

def validate_registry(data: Dict[str, Any]) -> List[ValidationError]:
    errors: List[ValidationError] = []

    required_top = ["registry_version", "layer", "domain_closed", "policy", "events", "invariants"]
    for k in required_top:
        if k not in data:
            errors.append(ValidationError(f"Missing required top-level key: {k}"))

    if errors:
        return errors

    if data.get("domain_closed") is not True:
        errors.append(ValidationError("domain_closed must be true."))

    events = data.get("events")
    if not isinstance(events, list):
        errors.append(ValidationError("events must be a list."))
        return errors

    ids = []
    for ev in events:
        if not isinstance(ev, dict):
            errors.append(ValidationError("event must be object"))
            continue
        ev_id = ev.get("id")
        if not isinstance(ev_id, str):
            errors.append(ValidationError("event id must be string"))
        else:
            ids.append(ev_id)

    if len(ids) != len(set(ids)):
        errors.append(ValidationError("Duplicate event id detected."))

    return errors

def main() -> int:
    data = _load_registry(REGISTRY_PATH)
    if data is None:
        return _fail([ValidationError("Registry missing or invalid JSON.")])

    errors = validate_registry(data)
    if errors:
        return _fail(errors)

    return _pass()

if __name__ == "__main__":
    raise SystemExit(main())
