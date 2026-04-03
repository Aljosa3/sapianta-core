"""
SAPIANTA LLM Code Generator (SAFE LAYER)

Design:
- optional
- isolated
- no side effects
- no file writes
- returns raw code only
"""

import os
from typing import Optional


class LLMCodeGenerator:

    def __init__(self):
        self.enabled = os.getenv("SAPIANTA_USE_LLM", "0") == "1"

    def generate(self, task: dict) -> Optional[str]:
        """
        Returns generated code or None (fallback trigger)
        """

        if not self.enabled:
            return None

        try:
            prompt = self._build_prompt(task)

            code = self._call_llm(prompt)

            # 🔒 BASIC SANITY FILTER (minimal)
            if not self._is_valid(code):
                return None

            return code

        except Exception:
            return None

    # --------------------------------------

    def _build_prompt(self, task: dict) -> str:
        goal = task.get("goal", "")

        return f"""
You are a Python code generator.

Rules:
- return ONLY valid Python code
- no explanations
- no comments outside code
- no imports of dangerous modules
- no file operations

Task:
{goal}
"""

    # --------------------------------------

    def _call_llm(self, prompt: str) -> str:
        """
        Replace with Claude / API call
        """

        # 🔧 TEMP MOCK (SAFE)
        return f"""
def generated_function(a, b):
    return a + b
"""

    # --------------------------------------

    def _is_valid(self, code: str) -> bool:
        forbidden = ["os.system", "subprocess", "exec(", "eval("]

        return not any(f in code for f in forbidden)