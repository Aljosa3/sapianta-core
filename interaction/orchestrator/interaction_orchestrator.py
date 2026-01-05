"""
Interaction Orchestrator (NON-EXECUTABLE)
"""

from interaction.types.interaction_request import InteractionRequest
from interaction.types.interaction_response import InteractionResponse
from interaction.adapters.core_reference_adapter import to_core_reference

def handle(req: InteractionRequest) -> InteractionResponse:
    return to_core_reference(req)
