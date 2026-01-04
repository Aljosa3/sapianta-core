"""
Sapianta Interaction Layer — Request Builder

Status: NON-AUTHORITATIVE
Phase: 2
Purpose: Assist in constructing AbstractRequest objects.

This module helps transform human input into an abstract request form.
It does not validate meaning, assess acceptability, or call the Core.
"""

from typing import Optional, Dict
from uuid import uuid4

from implementation.core_meaning_kernel.types import AbstractRequest


def build_abstract_request(
    raw_input: str,
    metadata: Optional[Dict] = None,
) -> AbstractRequest:
    """
    Construct an AbstractRequest from raw human input.

    Rules:
    - No semantic interpretation is performed.
    - No validation of correctness or acceptability.
    - Input is treated as opaque content.
    - A unique request_id is always generated.

    This function is a structural helper only.
    """

    payload: Dict = {
        "raw_input": raw_input,
    }

    if metadata is not None:
        payload["metadata"] = metadata

    return AbstractRequest(
        request_id=str(uuid4()),
        payload=payload,
    )
