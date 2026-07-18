"""Bounded governed Codex task synthesis responses."""

from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
from pathlib import PurePosixPath

from .governed_codex_evidence import governed_codex_synthesis_evidence
from .governed_codex_prompt_synthesizer import synthesize_codex_prompt
from .governed_codex_prompt_validator import validate_codex_prompt
from .governed_codex_replay import build_codex_synthesis_replay_identity
from .governed_codex_task_request import WORKER_EXECUTION_CONSTRAINTS
from .governed_codex_task_classifier import BLOCKED_MARKERS, classify_governed_codex_task

GOVERNANCE_MODE = "BOUNDED_CODEX_SYNTHESIS"


def _request_valid(request: dict) -> dict:
    errors = []
    if not isinstance(request, dict):
        return {"valid": False, "errors": [{"field": "request", "reason": "malformed request"}]}
    value = request.get("natural_language")
    if not isinstance(value, str) or not value.strip():
        errors.append({"field": "natural_language", "reason": "must be non-empty"})
    if isinstance(value, str) and len(value) > 240:
        errors.append({"field": "natural_language", "reason": "must remain bounded"})
    errors.extend(_execution_contract_errors(request.get("worker_execution_contract"), value))
    return {"valid": not errors, "errors": errors}


def _execution_contract_errors(contract: object, natural_language: object) -> list[dict]:
    if contract is None:
        return []
    if not isinstance(contract, dict):
        return [{"field": "worker_execution_contract", "reason": "malformed contract"}]
    errors = []
    if contract.get("worker_role") != "CODEX":
        errors.append({"field": "worker_role", "reason": "selected Worker role mismatch"})
    if contract.get("worker_kind") != "SELECTED_WORKER_NOT_PROVIDER_OR_PLANNER":
        errors.append({"field": "worker_kind", "reason": "Worker authority mismatch"})
    task = contract.get("authorized_task")
    if not isinstance(task, str) or not task.strip():
        errors.append({"field": "authorized_task", "reason": "authorized task missing"})
    elif not isinstance(natural_language, str) or not natural_language.endswith(task):
        errors.append({"field": "authorized_task", "reason": "authorized task substitution"})
    if contract.get("requested_output_type") not in {"UNIFIED_DIFF", "AUTHORIZED_TASK_RESULT"}:
        errors.append({"field": "requested_output_type", "reason": "unsupported output type"})
    if contract.get("constraints") != WORKER_EXECUTION_CONSTRAINTS:
        errors.append({"field": "constraints", "reason": "Worker constraints substituted"})
    targets = contract.get("grounded_targets")
    if not isinstance(targets, list) or len(targets) != 2:
        errors.append({"field": "grounded_targets", "reason": "exact grounded pair required"})
        return errors
    roles = []
    paths = []
    for target in targets:
        if not isinstance(target, dict):
            errors.append({"field": "grounded_targets", "reason": "malformed grounded target"})
            continue
        role = target.get("target_role")
        path = target.get("target_path")
        roles.append(role)
        paths.append(path)
        if role not in {"IMPLEMENTATION", "FOCUSED_TEST"}:
            errors.append({"field": "grounded_targets", "reason": "grounded target role mismatch"})
        if not isinstance(path, str) or not path or "\n" in path or "\r" in path:
            errors.append({"field": "grounded_targets", "reason": "invalid grounded target path"})
        elif PurePosixPath(path).is_absolute() or ".." in PurePosixPath(path).parts:
            errors.append({"field": "grounded_targets", "reason": "grounded target path escaped workspace"})
    if set(roles) != {"IMPLEMENTATION", "FOCUSED_TEST"} or len(set(paths)) != 2:
        errors.append({"field": "grounded_targets", "reason": "unique implementation/test pair required"})
    return errors


def _blocked(request: dict, errors: list[dict]) -> dict:
    response = {
        "status": "BLOCKED",
        "task_class": None,
        "governance_mode": GOVERNANCE_MODE,
        "requires_confirmation": True,
        "allowed_to_execute_automatically": False,
        "codex_prompt_preview": None,
        "replay_visible": True,
        "blocked_capability_checks": list(BLOCKED_MARKERS),
        "closure": "BLOCKED",
        "validation": {"valid": False, "errors": errors},
    }
    response["replay_identity"] = build_codex_synthesis_replay_identity(request=request, synthesis=response.copy())
    response["evidence"] = governed_codex_synthesis_evidence(request=request, response=response)
    return response


def synthesize_governed_codex_task(request: dict) -> dict:
    request_validation = _request_valid(request)
    if not request_validation["valid"]:
        return _blocked(request, request_validation["errors"])
    classification = classify_governed_codex_task(request["natural_language"])
    if not classification["valid"]:
        return _blocked(request, [{"field": "natural_language", "reason": classification["reason"]}])
    contract = request.get("worker_execution_contract")
    prompt = synthesize_codex_prompt(
        task_class=classification["task_class"],
        natural_language=request["natural_language"],
        worker_execution_contract=contract,
    )
    prompt_validation = validate_codex_prompt(
        prompt, worker_execution_contract=contract
    )
    if not prompt_validation["valid"]:
        return _blocked(request, prompt_validation["errors"])
    response = {
        "status": "SYNTHESIZED",
        "task_class": classification["task_class"],
        "governance_mode": GOVERNANCE_MODE,
        "requires_confirmation": True,
        "allowed_to_execute_automatically": False,
        "codex_prompt_preview": prompt,
        "bounded_prompt_sha256": sha256(prompt.encode("utf-8")).hexdigest(),
        "worker_execution_contract": deepcopy(contract),
        "replay_visible": True,
        "blocked_capability_checks": list(BLOCKED_MARKERS),
        "closure": "PREVIEW",
        "validation": prompt_validation,
    }
    response["replay_identity"] = build_codex_synthesis_replay_identity(request=request, synthesis=response.copy())
    response["evidence"] = governed_codex_synthesis_evidence(request=request, response=response)
    return response
