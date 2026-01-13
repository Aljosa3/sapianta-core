from sapianta.runtime import RuntimeController
from sapianta.governance.interface.types import GovernanceRequest
from sapianta.governance.roi import ROIRegistry, ROIInterface, ROIContext
from sapianta.governance.roi.overlays import (
    community_dummy_allow,
    org_dummy_block_on_accept
)

# Za F34.A: minimalni runtime wiring (brez execution)
_registry = ROIRegistry()
_registry.register_community("DUMMY_COMMUNITY", community_dummy_allow)
_registry.register_org("DUMMY_ORG", org_dummy_block_on_accept)

_roi_interface = ROIInterface(_registry)
_runtime = RuntimeController(_roi_interface)


def handle_cli_input(user_input: str):
    request = GovernanceRequest(
        request_type="CLI",
        raw_input=user_input
    )

    context = ROIContext(
        active_community_frameworks=["DUMMY_COMMUNITY"],
        active_org_policies=["DUMMY_ORG"]
    )

    return _runtime.process(request, context)
