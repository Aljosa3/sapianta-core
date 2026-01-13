from sapianta.core.engine import evaluate
from sapianta.core.types import CoreRequest
from .types import GovernanceRequest, GovernanceResponse


class GovernanceInterface:
    """
    Normativno prazen Governance Interface.
    """

    @staticmethod
    def handle(request: GovernanceRequest) -> GovernanceResponse:
        # Shematska validacija
        if not request.request_type:
            raise ValueError("Missing request_type")

        # Pretvorba v CoreRequest
        core_request = CoreRequest(
            request_type=request.request_type,
            payload=request.raw_input
        )

        # Klic Core
        core_response = evaluate(core_request)

        # Neposredna vrnitev rezultata
        return GovernanceResponse(core_response=core_response)
