from typing import Protocol, runtime_checkable
from dataclasses import dataclass


@dataclass(frozen=True)
class LLMRequest:
    prompt: str


@dataclass(frozen=True)
class LLMResponse:
    text: str


@runtime_checkable
class LLMAdapter(Protocol):
    def generate(self, request: LLMRequest) -> LLMResponse:
        ...
