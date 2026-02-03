import os
import requests


class ClaudeClientError(RuntimeError):
    pass


class ClaudeClient:
    """
    Minimal real execution client for Anthropic Claude.

    Responsibilities:
    - accept a prompt (string)
    - perform exactly one API call
    - return raw string output

    This client:
    - performs NO retries
    - performs NO validation
    - performs NO interpretation
    """

    API_URL = "https://api.anthropic.com/v1/messages"
    MODEL = "claude-3-5-sonnet-20240620"
    MAX_TOKENS = 4096

    def __init__(self, api_key: str):
        self.api_key = api_key

    @classmethod
    def from_env(cls) -> "ClaudeClient":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ClaudeClientError(
                "ANTHROPIC_API_KEY not set in environment"
            )
        return cls(api_key=api_key)

    def call(self, prompt: str) -> str:
        if not isinstance(prompt, str):
            raise ClaudeClientError("Prompt must be a string")

        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }

        payload = {
            "model": self.MODEL,
            "max_tokens": self.MAX_TOKENS,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        }

        response = requests.post(
            self.API_URL,
            headers=headers,
            json=payload,
            timeout=60,
        )

        if response.status_code != 200:
            raise ClaudeClientError(
                f"Claude API error {response.status_code}: {response.text}"
            )

        data = response.json()

        try:
            content_blocks = data["content"]
            if not content_blocks:
                raise KeyError

            text = content_blocks[0]["text"]
            if not isinstance(text, str):
                raise TypeError

            return text

        except (KeyError, TypeError) as e:
            raise ClaudeClientError(
                f"Invalid Claude response format: {data}"
            ) from e

    # --- adapter compatibility (LOCKED contract) ---

    def complete(self, prompt: str) -> str:
        """
        Alias for adapter compatibility.
        Adapter contract is LOCKED (v0.13).
        """
        return self.call(prompt)
