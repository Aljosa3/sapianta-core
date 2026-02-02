class FakeClaudeClient:
    """
    Deterministic fake LLM client for adapter tests.
    """

    def __init__(self, response: str):
        self._response = response
        self.calls = []

    def complete(self, prompt: str) -> str:
        self.calls.append(prompt)
        return self._response
