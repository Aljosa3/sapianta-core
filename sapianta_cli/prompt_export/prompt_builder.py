from sapianta_hoi.runtime_contracts.state_completeness import validate_state_completeness
from sapianta_hoi.prompt_export.prompt_contract import PromptPayload
from sapianta_hoi.prompt_export.prompt_template import (
    TEMPLATE_VERSION,
    PROMPT_TEMPLATE_STRUCTURE,
)


def build_prompt_payload(canonical_state) -> PromptPayload:
    """
    Deterministic transformation from canonical state to PromptPayload.

    Guarantees:
    - No I/O
    - No mutation
    - No interpretation
    - Fail-fast on incomplete state
    """

    # Enforce completeness before export
    validate_state_completeness(canonical_state)

    state_snapshot = {
        "state_name": canonical_state.state_name
    }

    return PromptPayload(
        state_name=canonical_state.state_name,
        state_snapshot=state_snapshot,
        template_version=TEMPLATE_VERSION,
    )


def export_prompt_payload(payload: PromptPayload) -> dict:
    """
    Deterministic final export structure.

    No formatting.
    No LLM calls.
    No string rendering.
    """

    return {
        "header": PROMPT_TEMPLATE_STRUCTURE["header"],
        "payload": payload.to_dict(),
        "footer": PROMPT_TEMPLATE_STRUCTURE["footer"],
    }
