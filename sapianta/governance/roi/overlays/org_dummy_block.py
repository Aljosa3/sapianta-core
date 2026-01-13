from sapianta.core.types import ChatResponse
from sapianta.governance.roi.types import ROIContext, ROIResult


def org_dummy_block_on_accept(response: ChatResponse, context: ROIContext) -> ROIResult:
    """
    Dummy organizational overlay:
    - blokira, če je Core odločitev ACCEPTED
    """
    if response.status.value == "ACCEPTED":
        return ROIResult(
            allowed=False,
            reason="ORG_DUMMY_BLOCK"
        )

    return ROIResult(allowed=True)
