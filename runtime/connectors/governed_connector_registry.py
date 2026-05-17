"""Static governed execution connector registry."""

CONNECTOR_REGISTRY = {
    "local_execution": {
        "connector_type": "LOCAL_EXECUTION",
        "allowed_execution_surfaces": ("GOVERNED_PYTEST_RUNTIME_SURFACE", "GOVERNED_EXECUTION_PREPARATION_SURFACE"),
    },
    "codex_execution": {
        "connector_type": "CODEX_EXECUTION",
        "allowed_execution_surfaces": ("GOVERNED_EXECUTION_PREPARATION_SURFACE",),
    },
    "claude_execution": {
        "connector_type": "CLAUDE_EXECUTION",
        "allowed_execution_surfaces": ("GOVERNED_EXECUTION_PREPARATION_SURFACE",),
    },
    "deterministic_filesystem": {
        "connector_type": "DETERMINISTIC_FILESYSTEM",
        "allowed_execution_surfaces": ("GOVERNED_STATE_READ_SURFACE", "GOVERNED_ARTIFACT_WRITE_SURFACE"),
    },
    "bounded_tool_execution": {
        "connector_type": "BOUNDED_TOOL_EXECUTION",
        "allowed_execution_surfaces": ("GOVERNED_PYTEST_RUNTIME_SURFACE", "GOVERNED_RESPONSE_EMISSION_SURFACE"),
    },
}
