# PATH: runtime/wiring.py

from typing import Optional

from modules.llm_adapter import DummyLLMAdapter, LLMAdapter
from runtime.hoi_orchestrator import hoi_orchestrator
from runtime.hds_boundary import hds_boundary
from runtime.hds_schema import hds_schema
from runtime.hds_guard import hds_execution_guard
from runtime.interaction_flow import interaction_flow


def run(
    input_payload: dict,
    *,
    llm: Optional[LLMAdapter] = None,
) -> dict:
    """
    Canonical system entry point.
    No execution. No autonomy. No decisions.

    Invariants:
    - Single entry
    - Fixed order
    - No bypass
    """

    # Dependency injection (default: Dummy LLM)
    llm_adapter = llm if llm is not None else DummyLLMAdapter()

    # 1) HOI Orchestrator (reference-only)
    hoi_output = hoi_orchestrator(input_payload, llm=llm_adapter)

    # 2) HDS Boundary (passive normalization)
    boundary_output = hds_boundary(hoi_output)

    # 3) HDS Schema (typing / contract)
    schema_output = hds_schema(boundary_output)

    # 4) HDS Execution Guard (enforcement)
    guarded_output = hds_execution_guard(schema_output)

    # 5) Interaction Flow (human-in-the-loop, no execution)
    interaction_output = interaction_flow(guarded_output)

    return interaction_output
