"""
Prompt Export Isolation Layer

This package provides a deterministic, pure, side-effect-free
prompt generation layer that transforms canonical state into
a reproducible PromptPayload.

This layer:
- does NOT call any LLM
- does NOT perform I/O
- does NOT perform interpretation
- does NOT mutate state

It only transforms canonical state into a formal prompt payload.
"""
