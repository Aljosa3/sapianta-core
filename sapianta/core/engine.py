from .types import CoreRequest, ChatResponse, DecisionStatus


def evaluate(request: CoreRequest) -> ChatResponse:
    """
    Determinističen placeholder za Meaning Kernel.
    """
    if not request.payload.strip():
        return ChatResponse(
            status=DecisionStatus.REJECTED,
            reason="EMPTY_REQUEST"
        )

    return ChatResponse(
        status=DecisionStatus.ACCEPTED,
        reason=None
    )
