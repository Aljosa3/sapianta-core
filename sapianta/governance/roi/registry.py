from typing import Callable
from sapianta.core.types import ChatResponse
from .types import ROIContext, ROIResult


ROIHandler = Callable[[ChatResponse, ROIContext], ROIResult]


class ROIRegistry:
    """
    Register ROI overlayjev.
    Ne izvaja logike – samo hrani reference.
    """

    def __init__(self):
        self.community_overlays: dict[str, ROIHandler] = {}
        self.org_overlays: dict[str, ROIHandler] = {}

    def register_community(self, name: str, handler: ROIHandler):
        self.community_overlays[name] = handler

    def register_org(self, name: str, handler: ROIHandler):
        self.org_overlays[name] = handler
