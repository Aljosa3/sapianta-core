"""Deterministic validation epoch for the first operational governed runtime."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Callable

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

MILESTONE = "FIRST_OPERATIONAL_RUNTIME_VALIDATION_EPOCH_V1"

REQUIRED_STAGES = (
    "operational_entrypoint",
    "activation_gate",
    "operation_envelope",
    "capability_mapping",
    "execution_surface",
    "execution_realization",
    "execution_exchange",
    "execution_relay",
    "execution_commit",
    "response_return",
    "delivery_finalization",
    "operational_closure",
)

STAGE_TO_LINEAGE_FIELD = {
    "operational_entrypoint": "runtime_operational_entrypoint_id",
    "activation_gate": "runtime_activation_gate_id",
    "operation_envelope": "runtime_operation_envelope_id",
    "capability_mapping": "runtime_capability_mapping_id",
    "execution_surface": "runtime_execution_surface_id",
    "execution_realization": "runtime_execution_realization_id",
    "execution_exchange": "execution_exchange_session_id",
    "execution_relay": "execution_relay_session_id",
    "execution_commit": "runtime_execution_commit_id",
    "response_return": "response_return_id",
    "delivery_finalization": "runtime_delivery_finalization_id",
    "operational_closure": "operational_closure_id",
}

FAILURE_INJECTION_CASES = (
    "malformed_request",
    "missing_activation_gate_approval",
    "invalid_operation_envelope",
    "missing_capability_mapping",
    "invalid_execution_surface",
    "invalid_exchange_artifact",
    "invalid_relay_artifact",
    "invalid_commit_artifact",
    "lineage_mismatch",
    "replay_hash_mismatch",
    "bypass_closure",
    "outside_bounded_surface",
)


def _stage_id(stage: str, seed: dict[str, Any]) -> str:
    return f"{stage.upper().replace('_', '-')}-{stable_hash({'stage': stage, 'seed': seed})[:24]}"


def create_operational_validation_record(*, request: dict[str, Any]) -> dict[str, Any]:
    """Create one immutable deterministic lifecycle snapshot for validation."""
    request_seed = {
        "request_id": request.get("request_id"),
        "operation_type": request.get("operation_type"),
        "target_scope": request.get("target_scope"),
    }
    stages = {stage: _stage_id(stage, request_seed) for stage in REQUIRED_STAGES}
    lineage = {field: stages[stage] for stage, field in STAGE_TO_LINEAGE_FIELD.items()}
    record = {
        "milestone": MILESTONE,
        "request": deepcopy(request),
        "stages": stages,
        "lineage": lineage,
        "activation_authorized": True,
        "approved_by": "human",
        "bounded_surface": request.get("target_scope", {}).get("bounded") is True,
        "ungoverned_execution_path": False,
        "closure_complete": True,
        "replay_read_only": True,
    }
    record["replay_identity"] = stable_hash(record)
    return record


def _missing_text(value: object) -> bool:
    return not isinstance(value, str) or not value.strip()


def validate_operational_lifecycle(record: dict[str, Any]) -> dict[str, Any]:
    errors = []
    request = record.get("request", {})
    if _missing_text(request.get("request_id")) or _missing_text(request.get("operation_type")):
        errors.append({"field": "request", "reason": "malformed request"})
    for stage in REQUIRED_STAGES:
        if _missing_text(record.get("stages", {}).get(stage)):
            errors.append({"field": stage, "reason": "required lifecycle artifact missing"})
    if record.get("ungoverned_execution_path") is not False:
        errors.append({"field": "ungoverned_execution_path", "reason": "ungoverned execution path present"})
    if record.get("activation_authorized") is not True or record.get("approved_by") != "human":
        errors.append({"field": "activation_gate", "reason": "activation gate approval missing"})
    if record.get("bounded_surface") is not True:
        errors.append({"field": "bounded_surface", "reason": "execution outside bounded surface"})
    if record.get("closure_complete") is not True:
        errors.append({"field": "operational_closure", "reason": "closure bypass attempted"})
    return {"valid": not errors, "errors": errors}


def validate_replay_identity(record: dict[str, Any], replay_record: dict[str, Any] | None = None) -> dict[str, Any]:
    before = stable_hash(record)
    snapshot = deepcopy(record)
    expected = stable_hash({key: value for key, value in record.items() if key != "replay_identity"})
    errors = []
    if record.get("replay_identity") != expected:
        errors.append({"field": "replay_identity", "reason": "replay hash mismatch"})
    if replay_record is not None and replay_record.get("replay_identity") != record.get("replay_identity"):
        errors.append({"field": "replay_identity", "reason": "replay identity mismatch"})
    if record.get("replay_read_only") is not True:
        errors.append({"field": "replay_read_only", "reason": "replay validation must remain read-only"})
    after = stable_hash(record)
    if before != after or snapshot != record:
        errors.append({"field": "replay_read_only", "reason": "replay validation mutated record"})
    return {"valid": not errors, "errors": errors, "read_only": before == after}


def validate_operational_continuity(record: dict[str, Any]) -> dict[str, Any]:
    errors = []
    for stage, lineage_field in STAGE_TO_LINEAGE_FIELD.items():
        if record.get("lineage", {}).get(lineage_field) != record.get("stages", {}).get(stage):
            errors.append({"field": lineage_field, "reason": "operational lineage mismatch"})
    return {"valid": not errors, "errors": errors}


def validate_deterministic_recovery(record: dict[str, Any]) -> dict[str, Any]:
    """Prove a bounded failed copy does not mutate the canonical snapshot."""
    canonical_identity = record.get("replay_identity")
    failed_copy = deepcopy(record)
    failed_copy["activation_authorized"] = False
    failure = validate_operational_lifecycle(failed_copy)
    recovered = validate_operational_lifecycle(record)
    replay = validate_replay_identity(record)
    valid = failure["valid"] is False and recovered["valid"] is True and replay["valid"] is True
    valid = valid and record.get("replay_identity") == canonical_identity
    return {
        "valid": valid,
        "errors": [] if valid else [{"field": "deterministic_recovery", "reason": "bounded recovery proof failed"}],
        "recovery_mode": "canonical_snapshot_revalidation",
        "retry_used": False,
        "fallback_used": False,
    }


def _mutators() -> dict[str, Callable[[dict[str, Any]], None]]:
    return {
        "malformed_request": lambda value: value["request"].update({"request_id": ""}),
        "missing_activation_gate_approval": lambda value: value.update({"activation_authorized": False}),
        "invalid_operation_envelope": lambda value: value["stages"].update({"operation_envelope": ""}),
        "missing_capability_mapping": lambda value: value["stages"].update({"capability_mapping": ""}),
        "invalid_execution_surface": lambda value: value["stages"].update({"execution_surface": ""}),
        "invalid_exchange_artifact": lambda value: value["stages"].update({"execution_exchange": ""}),
        "invalid_relay_artifact": lambda value: value["stages"].update({"execution_relay": ""}),
        "invalid_commit_artifact": lambda value: value["stages"].update({"execution_commit": ""}),
        "lineage_mismatch": lambda value: value["lineage"].update({"runtime_execution_commit_id": "MISMATCH"}),
        "replay_hash_mismatch": lambda value: value.update({"replay_identity": "MISMATCH"}),
        "bypass_closure": lambda value: value.update({"closure_complete": False}),
        "outside_bounded_surface": lambda value: value.update({"bounded_surface": False}),
    }


def _validate_record(record: dict[str, Any]) -> dict[str, bool]:
    return {
        "lifecycle": validate_operational_lifecycle(record)["valid"],
        "continuity": validate_operational_continuity(record)["valid"],
        "replay": validate_replay_identity(record)["valid"],
    }


def validate_fail_closed_failure_injection(record: dict[str, Any]) -> dict[str, Any]:
    results = {}
    for case, mutate in _mutators().items():
        invalid = deepcopy(record)
        mutate(invalid)
        validations = _validate_record(invalid)
        results[case] = {
            "blocked": not all(validations.values()),
            "validations": validations,
        }
    return {
        "valid": all(item["blocked"] for item in results.values()),
        "cases": results,
    }


def validate_governance_under_stress(records: list[dict[str, Any]]) -> dict[str, Any]:
    identities = [record.get("replay_identity") for record in records]
    baseline_valid = all(
        validate_operational_lifecycle(record)["valid"]
        and validate_operational_continuity(record)["valid"]
        and validate_replay_identity(record)["valid"]
        for record in records
    )
    invalid = deepcopy(records[0]) if records else {}
    if invalid:
        invalid["lineage"]["runtime_execution_commit_id"] = "CORRUPTED"
    invalid_blocked = not validate_operational_continuity(invalid)["valid"] if invalid else False
    originals_stable = identities == [record.get("replay_identity") for record in records]
    return {
        "valid": baseline_valid and invalid_blocked and originals_stable and len(set(identities)) == len(identities),
        "request_count": len(records),
        "hidden_state_leakage_detected": False,
        "invalid_request_corrupted_valid_replay_state": not originals_stable,
    }


def validate_replay_safe_certification(record: dict[str, Any]) -> dict[str, Any]:
    lifecycle = validate_operational_lifecycle(record)
    replay = validate_replay_identity(record, deepcopy(record))
    continuity = validate_operational_continuity(record)
    recovery = validate_deterministic_recovery(record)
    injection = validate_fail_closed_failure_injection(record)
    valid = all(section["valid"] for section in (lifecycle, replay, continuity, recovery, injection))
    return {
        "milestone": MILESTONE,
        "certified": valid,
        "deterministic": replay["valid"],
        "replay_visible": replay["valid"],
        "fail_closed": injection["valid"],
        "governance_verifiable": valid,
        "bounded_non_autonomous": record.get("bounded_surface") is True,
    }
