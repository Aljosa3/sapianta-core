"""Minimal localhost operational preview runtime."""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from sapianta_system.runtime.codex_handoff import create_governed_codex_handoff, create_governed_codex_handoff_request
from sapianta_system.runtime.codex_synthesis import create_governed_codex_task_request, synthesize_governed_codex_task
from sapianta_system.runtime.execution_gate import create_execution_authorization_request, authorize_downstream_execution
from sapianta_system.runtime.execution_consumer import create_execution_consumer_request, consume_execution_authority
from sapianta_system.runtime.execution_observability import (
    create_execution_observability_request,
    observe_governed_execution,
)
from sapianta_system.runtime.codex_execution_adapter import create_codex_execution_request, execute_governed_codex
from sapianta_system.runtime.chatgpt_bridge_v2 import create_chatgpt_bridge_request, bridge_chatgpt_conversation
from sapianta_system.runtime.intent_transfer import create_intent_transfer_request, create_governed_intent_transfer
from sapianta_system.runtime.intent_transfer_ingestion import (
    create_intent_transfer_ingestion_request,
    ingest_governed_intent_transfer,
)
from sapianta_system.runtime.intent import create_governed_intent_request, interpret_governed_intent
from sapianta_system.runtime.ux import create_governed_interaction_session
from sapianta_system.runtime.wiring import (
    close_runtime_invocation_session,
    create_runtime_invocation_session,
    invoke_governed_runtime,
)

from .governed_preview_runtime_evidence import governed_preview_runtime_evidence
from .governed_preview_runtime_lifecycle import close_preview_lifecycle, start_preview_lifecycle
from .governed_preview_runtime_response import create_preview_runtime_response
from .governed_preview_runtime_validator import (
    validate_preview_binding,
    validate_preview_runtime_request,
    validate_preview_runtime_response,
)


def _blocked(request: dict, *, lifecycle: dict, errors: list[dict]) -> dict:
    closure = close_preview_lifecycle(lifecycle=lifecycle)
    evidence = governed_preview_runtime_evidence(request=request, response=None, lifecycle=lifecycle, closure=closure)
    return {
        "status": "BLOCKED",
        "request": request,
        "validation": {"valid": False, "errors": errors},
        "evidence": evidence,
        "closure": "BLOCKED",
    }


def handle_preview_invoke(
    *,
    request: dict,
    host: str = "127.0.0.1",
    port: int = 8010,
    activation_output: dict,
    operation_output: dict,
    surface_output: dict,
    transport_lineage: dict,
) -> dict:
    lifecycle = start_preview_lifecycle(host=host, port=port)
    binding_validation = validate_preview_binding(host=host)
    if not binding_validation["valid"]:
        return _blocked(request, lifecycle=lifecycle, errors=binding_validation["errors"])
    request_validation = validate_preview_runtime_request(request)
    if not request_validation["valid"]:
        return _blocked(request, lifecycle=lifecycle, errors=request_validation["errors"])
    lineage = request["lineage"]
    ux_session = create_governed_interaction_session(
        interaction_seed={"preview_runtime_request_id": request["preview_runtime_request_id"]},
        lineage=lineage,
    )
    invocation_session = create_runtime_invocation_session(
        interaction_identity=request["request_payload"]["interaction_identity"],
        lineage={
            "governed_interaction_session_id": ux_session["governed_interaction_session_id"],
            "governed_session_id": lineage["governed_session_id"],
        },
    )
    invocation_output = invoke_governed_runtime(
        invocation_session=invocation_session,
        ux_session=ux_session,
        interaction_payload=request["request_payload"]["interaction_payload"],
        transport_lineage=transport_lineage,
        activation_output=activation_output,
        operation_output=operation_output,
        surface_output=surface_output,
    )
    if invocation_output["invocation_status"] != "RETURNED":
        return _blocked(request, lifecycle=lifecycle, errors=invocation_output["validation"]["errors"])
    invocation_closure = close_runtime_invocation_session(session=invocation_output["invocation_session"])
    if not invocation_closure["validation"]["valid"]:
        return _blocked(request, lifecycle=lifecycle, errors=invocation_closure["validation"]["errors"])
    response = create_preview_runtime_response(
        request=request,
        invocation_output=invocation_output,
        closure_output=invocation_closure,
    )
    response_validation = validate_preview_runtime_response(response=response, request=request)
    if not response_validation["valid"]:
        return _blocked(request, lifecycle=lifecycle, errors=response_validation["errors"])
    closure = close_preview_lifecycle(lifecycle=lifecycle, response=response)
    evidence = governed_preview_runtime_evidence(request=request, response=response, lifecycle=lifecycle, closure=closure)
    return {
        **response,
        "validation": {"valid": True, "errors": []},
        "evidence": evidence,
        "lifecycle": lifecycle,
        "runtime_closure": closure,
    }


def _default_activation() -> dict:
    return {
        "validation": {"valid": True},
        "runtime_activation_gate_binding": {"runtime_activation_gate_id": "GATE-1", "activation_authorized": True},
    }


def _default_operation() -> dict:
    return {"validation": {"valid": True}, "runtime_operation_evidence": {"runtime_operation_envelope_id": "ENV-1"}}


def _default_surface() -> dict:
    return {
        "validation": {"valid": True},
        "runtime_execution_surface_evidence": {
            "runtime_execution_surface_id": "SURFACE-1",
            "runtime_surface": "GOVERNED_PYTEST_RUNTIME_SURFACE",
        },
    }


def _default_transport_lineage() -> dict:
    return {
        "runtime_activation_gate_id": "GATE-1",
        "runtime_operation_envelope_id": "ENV-1",
        "runtime_execution_surface_id": "SURFACE-1",
        "execution_exchange_session_id": "EXCHANGE-1",
        "execution_relay_session_id": "RELAY-1",
        "runtime_execution_commit_id": "COMMIT-1",
        "response_return_id": "RETURN-1",
    }


class _PreviewRequestHandler(BaseHTTPRequestHandler):
    server_version = "SapiantaPreviewRuntime/1"

    def do_POST(self) -> None:  # noqa: N802
        if self.path not in {
            "/governed-invoke",
            "/governed-interpret",
            "/governed-codex-synthesize",
            "/governed-codex-handoff",
            "/governed-execution-authorize",
            "/governed-execution-consume",
            "/governed-codex-execute",
            "/governed-execution-observe",
            "/governed-chatgpt-bridge",
            "/governed-intent-transfer",
            "/governed-intent-transfer-ingest",
        }:
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        try:
            request = json.loads(self.rfile.read(length).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            request = {}
        if self.path == "/governed-interpret":
            result = interpret_governed_intent(
                create_governed_intent_request(natural_language=request.get("natural_language", ""))
            )
        elif self.path == "/governed-codex-synthesize":
            result = synthesize_governed_codex_task(
                create_governed_codex_task_request(natural_language=request.get("natural_language", ""))
            )
        elif self.path == "/governed-codex-handoff":
            result = create_governed_codex_handoff(
                create_governed_codex_handoff_request(
                    synthesis_response=request.get("synthesis_response", {}),
                    original_human_request=request.get("original_human_request", ""),
                )
            )
        elif self.path == "/governed-execution-authorize":
            result = authorize_downstream_execution(
                create_execution_authorization_request(
                    handoff_package=request.get("handoff_package", {}),
                    approved_by=request.get("approved_by", ""),
                    approval_timestamp=request.get("approval_timestamp", ""),
                )
            )
        elif self.path == "/governed-execution-consume":
            result = consume_execution_authority(
                create_execution_consumer_request(
                    handoff_package=request.get("handoff_package", {}),
                    authority_token=request.get("authority_token", {}),
                    now=request.get("now", ""),
                    revoked_token_ids=set(request.get("revoked_token_ids", [])),
                )
            )
        elif self.path == "/governed-codex-execute":
            result = execute_governed_codex(
                create_codex_execution_request(
                    handoff_package=request.get("handoff_package", {}),
                    authority_token=request.get("authority_token", {}),
                    now=request.get("now", ""),
                    revoked_token_ids=set(request.get("revoked_token_ids", [])),
                    codex_executable=request.get("codex_executable", "codex"),
                    timeout_seconds=request.get("timeout_seconds", 30),
                )
            )
        elif self.path == "/governed-execution-observe":
            result = observe_governed_execution(
                create_execution_observability_request(
                    handoff_package=request.get("handoff_package", {}),
                    authority_token=request.get("authority_token", {}),
                    consumer_response=request.get("consumer_response", {}),
                    adapter_response=request.get("adapter_response", {}),
                    now=request.get("now", ""),
                    revoked_token_ids=set(request.get("revoked_token_ids", [])),
                )
            )
        elif self.path == "/governed-chatgpt-bridge":
            result = bridge_chatgpt_conversation(
                create_chatgpt_bridge_request(conversational_input=request.get("conversational_input", ""))
            )
        elif self.path == "/governed-intent-transfer":
            result = create_governed_intent_transfer(
                create_intent_transfer_request(
                    conversational_input=request.get("conversational_input", ""),
                    normalized_governed_request=request.get("normalized_governed_request", {}),
                    governance_mode=request.get("governance_mode", ""),
                    replay_identity=request.get("replay_identity", ""),
                )
            )
        elif self.path == "/governed-intent-transfer-ingest":
            result = ingest_governed_intent_transfer(
                create_intent_transfer_ingestion_request(
                    transfer_package=request.get("transfer_package", {}),
                    replay_identity=request.get("replay_identity", ""),
                    transfer_identity=request.get("transfer_identity", ""),
                )
            )
        else:
            result = handle_preview_invoke(
                request=request,
                host=self.server.server_address[0],
                port=self.server.server_address[1],
                activation_output=_default_activation(),
                operation_output=_default_operation(),
                surface_output=_default_surface(),
                transport_lineage=_default_transport_lineage(),
            )
        encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode("utf-8")
        self.send_response(
            200
            if result["status"]
            in {
                "RETURNED",
                "INTERPRETED",
                "SYNTHESIZED",
                "HANDOFF_READY",
                "AUTHORIZED",
                "MOCK_EXECUTION_ACCEPTED",
                "EXECUTION_ACCEPTED",
                "OBSERVED",
                "NORMALIZED",
                "TRANSFER_READY",
                "INGESTED_PREVIEW_READY",
            }
            else 400
        )
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, format: str, *args: Any) -> None:
        return


def create_local_preview_server(*, host: str = "127.0.0.1", port: int = 8010) -> ThreadingHTTPServer:
    validation = validate_preview_binding(host=host)
    if not validation["valid"]:
        raise ValueError("localhost-only binding required")
    return ThreadingHTTPServer((host, port), _PreviewRequestHandler)
