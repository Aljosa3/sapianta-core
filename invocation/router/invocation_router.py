"""
Invocation Router (NON-EXECUTABLE)
"""

from invocation.types.request import InvocationRequest
from invocation.types.response import InvocationResponse
from invocation.adapters.interaction_adapter import to_interaction

def route(request: InvocationRequest) -> InvocationResponse:
    return to_interaction(request)
