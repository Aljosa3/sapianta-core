"""
CLI Adapter (NON-AUTHORITATIVE)
"""

from invocation.types.request import InvocationRequest

def from_cli(raw_input: str) -> InvocationRequest:
    return InvocationRequest(raw_input=raw_input)
