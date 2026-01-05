"""
Interaction Adapter (REFERENCE ONLY)
"""

from invocation.types.request import InvocationRequest
from invocation.types.response import InvocationResponse

def to_interaction(request: InvocationRequest) -> InvocationResponse:
    # Placeholder: no execution, no decision
    return InvocationResponse(payload="INTERACTION_REFERENCE")
