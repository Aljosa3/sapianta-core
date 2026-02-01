from .contract import LLMAdapter, LLMRequest, LLMResponse


class DummyLLMAdapter:
    """
    Deterministic, no-op LLM adapter.

    This adapter is used for:
    - testing wiring and interaction flow
    - enforcing architectural boundaries
    - proving that the system does not depend on LLM intelligence

    It does NOT call any external service.
    """

    def generate(self, request: LLMRequest) -> LLMResponse:
        if not isinstance(request, LLMRequest):
            raise TypeError("DummyLLMAdapter expects LLMRequest")

        # Deterministic placeholder response
        return LLMResponse(
            text=f"[DUMMY_LLM_RESPONSE]\nPrompt received:\n{request.prompt}"
        )
