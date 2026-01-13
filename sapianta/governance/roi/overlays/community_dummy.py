from sapianta.core.types import ChatResponse
from sapianta.governance.roi.types import ROIContext, ROIResult


def community_dummy_allow(response: ChatResponse, context: ROIContext) -> ROIResult:
    """
    Dummy community overlay:
    - vedno pusti
    - ne gleda vsebine
    """
    return ROIResult(allowed=True)
