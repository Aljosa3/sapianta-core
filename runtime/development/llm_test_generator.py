# runtime/development/llm_test_generator.py

"""
SAPIANTA LLM Test Generator (SAFE WRAPPER)

Purpose:
- generate test code using LLM
- enforce deterministic safety boundaries
- NEVER execute or trust LLM output directly
"""

from typing import Optional


class LLMTestGenerator:

    def __init__(self):
        pass

    def build_prompt(self, goal: str) -> str:
        """
        Strict prompt for safe test generation
        """

        return f"""
You are generating Python unit tests.

RULES:
- ONLY generate pytest tests
- DO NOT import os, subprocess, sys, or any system modules
- DO NOT use eval or exec
- DO NOT write files
- DO NOT include explanations
- ONLY output valid Python test code

GOAL:
{goal}

REQUIREMENTS:
- at least 2 assert statements
- use simple deterministic inputs
- cover basic functionality

OUTPUT FORMAT:
Python code only
"""

    def generate(self, goal: str) -> Optional[str]:
        """
        Placeholder for LLM call

        IMPORTANT:
        This does NOT call external API yet
        (safe staged rollout)
        """

        # 🔒 SAFE MOCK (phase 1)
        if "add" in goal.lower():
            return """
def test_add_basic():
    assert add(2, 3) == 5

def test_add_zero():
    assert add(0, 5) == 5
"""

        # fallback
        return """
def test_basic():
    assert True
"""