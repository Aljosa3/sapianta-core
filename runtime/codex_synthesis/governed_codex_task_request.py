"""Deterministic requests for bounded Codex task synthesis."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash


WORKER_EXECUTION_CONSTRAINTS = {
    "file_mutation_allowed": False,
    "provider_invocation_allowed": False,
    "scope_broadening_allowed": False,
    "automatic_retry_allowed": False,
    "delegation_allowed": False,
    "stdout_required": True,
}


def create_governed_codex_worker_execution_contract(
    *,
    authorized_task: str,
    grounded_targets: list[dict],
    requested_output_type: str,
) -> dict:
    """Build bounded Worker instructions without granting execution authority."""

    return {
        "worker_role": "CODEX",
        "worker_kind": "SELECTED_WORKER_NOT_PROVIDER_OR_PLANNER",
        "authorized_task": authorized_task,
        "grounded_targets": deepcopy(grounded_targets),
        "requested_output_type": requested_output_type,
        "constraints": deepcopy(WORKER_EXECUTION_CONSTRAINTS),
    }


def create_governed_codex_task_request(
    *,
    natural_language: str,
    worker_execution_contract: dict | None = None,
) -> dict:
    contract = deepcopy(worker_execution_contract)
    value = {
        "natural_language": natural_language,
        "worker_execution_contract": contract,
    }
    replay_identity = stable_hash(value)
    return {
        "governed_codex_task_request_id": f"GOVERNED-CODEX-TASK-REQUEST-{replay_identity[:24]}",
        **value,
        "replay_identity": replay_identity,
        "bounded": True,
    }
