from sapianta.core.types import ChatResponse
from .types import ROIContext, ROIResult, ROINormativeLevel
from .registry import ROIRegistry


class ROIInterface:
    """
    ROI Interface:
    - bere ChatResponse
    - uveljavlja hierarhijo (community > organizational)
    - nikoli ne spreminja Core odločitve
    """

    def __init__(self, registry: ROIRegistry):
        self.registry = registry

    def evaluate(self, response: ChatResponse, context: ROIContext) -> ROIResult:
        # 1️⃣ Community frameworks (nadrejeni nivo)
        for name in context.active_community_frameworks:
            handler = self.registry.community_overlays.get(name)
            if handler:
                result = handler(response, context)
                if not result.allowed:
                    return ROIResult(
                        allowed=False,
                        reason=result.reason,
                        originating_layer=ROINormativeLevel.COMMUNITY
                    )

        # 2️⃣ Organizational policies (podrejeni nivo)
        for name in context.active_org_policies:
            handler = self.registry.org_overlays.get(name)
            if handler:
                result = handler(response, context)
                if not result.allowed:
                    return ROIResult(
                        allowed=False,
                        reason=result.reason,
                        originating_layer=ROINormativeLevel.ORGANIZATIONAL
                    )

        # 3️⃣ Če nič ne blokira
        return ROIResult(allowed=True)
