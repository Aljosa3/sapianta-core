# runtime/llm/openai_adapter.py

import os
from typing import Optional

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


class LLMAdapterError(Exception):
    pass


def generate_answer(prompt: str) -> str:
    """
    Real LLM adapter (OpenAI).

    ⚠️ LLM nima konteksta sistema.
    ⚠️ LLM ne pozna Canona.
    ⚠️ LLM ne sprejema odločitev.

    Vrne samo besedilo.
    """

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise LLMAdapterError("OPENAI_API_KEY not set")

    if OpenAI is None:
        raise LLMAdapterError("openai package not installed")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a text generation engine. "
                    "Do not give advice, commands, or judgments."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=300,
    )

    return response.choices[0].message.content.strip()
