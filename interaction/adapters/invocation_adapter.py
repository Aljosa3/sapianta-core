"""
Adapter from Invocation → Interaction (NON-AUTHORITATIVE)
"""

from interaction.types.interaction_request import InteractionRequest
from invocation.types.request import InvocationRequest

def from_invocation(req: InvocationRequest) -> InteractionRequest:
    return InteractionRequest(payload=req.raw_input)
