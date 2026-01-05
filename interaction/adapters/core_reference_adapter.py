"""
Core Reference Adapter (REFERENCE ONLY)
No Core calls allowed in this phase.
"""

from interaction.types.interaction_request import InteractionRequest
from interaction.types.interaction_response import InteractionResponse

def to_core_reference(req: InteractionRequest) -> InteractionResponse:
    return InteractionResponse(payload="CORE_REFERENCE_ONLY")
