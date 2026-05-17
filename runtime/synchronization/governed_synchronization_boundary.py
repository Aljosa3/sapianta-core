"""Explicit governed synchronization boundary."""

ALLOWED_SYNCHRONIZED_FIELDS = (
    "last_exchange_id",
    "last_exchange_hash",
    "last_connector_result_id",
    "last_result_status",
)

PROHIBITED_SYNCHRONIZED_FIELDS = (
    "hidden_memory",
    "planner_state",
    "provider_state",
    "secret",
    "raw_prompt",
    "autonomous_continuation",
)

ALLOWED_SYNCHRONIZATION_SCOPE = "SESSION_EXCHANGE_METADATA"
