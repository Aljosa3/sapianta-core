import pytest

from sapianta_chat.execution.claude_adapter import ClaudeAdapter
from sapianta_chat.execution.prompt_renderer import ClaudePromptRenderer
from tests.execution.fake_claude_client import FakeClaudeClient


SAMPLE_BUILD_PLAN = {
    "version": "SAPIANTA_BUILD_PLAN_V1",
    "module": "example_module",
    "files": [
        {
            "path": "example.py",
            "content": "print('hello')"
        }
    ]
}


def test_adapter_executes_single_call_and_returns_raw_output():
    fake_output = "RAW LLM OUTPUT"
    fake_client = FakeClaudeClient(response=fake_output)

    adapter = ClaudeAdapter(fake_client)

    result = adapter.execute(SAMPLE_BUILD_PLAN)

    assert result == fake_output
    assert len(fake_client.calls) == 1


def test_prompt_snapshot_is_deterministic():
    prompt_1 = ClaudePromptRenderer.render(SAMPLE_BUILD_PLAN)
    prompt_2 = ClaudePromptRenderer.render(SAMPLE_BUILD_PLAN)

    assert prompt_1 == prompt_2

    # Optional: guard against accidental header/footer changes
    assert "SAPIANTA BUILD PLAN START" in prompt_1
    assert "SAPIANTA BUILD PLAN END" in prompt_1


def test_adapter_raises_hard_failure_on_non_string_output():
    class BadClient:
        def complete(self, prompt: str):
            return {"not": "a string"}

    adapter = ClaudeAdapter(BadClient())

    with pytest.raises(RuntimeError):
        adapter.execute(SAMPLE_BUILD_PLAN)
