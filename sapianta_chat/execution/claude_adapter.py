from sapianta_chat.execution.adapter_interface import ExecutionAdapter
from sapianta_chat.execution.prompt_renderer import ClaudePromptRenderer


class ClaudeAdapter(ExecutionAdapter):
    """
    Real Claude execution adapter.

    - One prompt
    - One LLM call
    - Raw output only
    """

    def __init__(self, claude_client):
        """
        :param claude_client: injected client with a .complete(prompt: str) -> str method
        """
        self._client = claude_client

    def execute(self, build_plan: dict) -> str:
        prompt = ClaudePromptRenderer.render(build_plan)

        # EXACTLY ONE CALL
        raw_output = self._client.complete(prompt)

        if not isinstance(raw_output, str):
            raise RuntimeError("Claude adapter received non-string output")

        return raw_output
