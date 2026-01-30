"""
Minimal wiring layer for SAPIANTA_CHAT.

Purpose:
- Delegate raw user input to HOI Orchestrator
- Return response for presentation only

NO interpretation.
NO reasoning.
NO orchestration.
"""

from interaction.orchestrator.interaction_orchestrator import handle
from interaction.types.interaction_request import InteractionRequest
from sapianta_chat.models.chat_response import ChatResponse


def delegate_to_hoi(user_input: str) -> ChatResponse:
    """
    Delegate user input to HOI Orchestrator.

    This function is the ONLY permitted execution path
    from SAPIANTA_CHAT into the system.

    :param user_input: raw user input string
    :return: ChatResponse (presentation wrapper only)
    """
    request = InteractionRequest(payload=user_input)
    response = handle(request)

    # Adapt InteractionResponse → ChatResponse (presentation only)
    return ChatResponse(
        response_text=response.payload,
        response_type="informational",
        metadata={
            "source": "HOI_ORCHESTRATOR",
        },
    )
