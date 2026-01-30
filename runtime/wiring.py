# PATH: runtime/wiring.py

from runtime.hoi_orchestrator import hoi_orchestrator
from runtime.hds_boundary import hds_boundary
from runtime.hds_schema import hds_schema
from runtime.hds_guard import hds_execution_guard
from runtime.interaction_flow import interaction_flow


def run(input_payload: dict) -> dict:
    """
    Canonical system entry point.
    No execution. No autonomy. No decisions.
    """

    hoi_output = hoi_orchestrator(input_payload)
    boundary_output = hds_boundary(hoi_output)
    schema_output = hds_schema(boundary_output)
    guarded_output = hds_execution_guard(schema_output)
    interaction_output = interaction_flow(guarded_output)

    return interaction_output
