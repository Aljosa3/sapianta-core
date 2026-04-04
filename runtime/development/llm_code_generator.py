"""
SAPIANTA LLM Code Generator (SAFE LAYER)

Design:
- optional
- isolated
- no side effects
- no file writes
- returns raw code only (UNTRUSTED)
"""

import os
import hashlib
from typing import Optional


class LLMCodeGenerator:

    def __init__(self):
        self.enabled = os.getenv("SAPIANTA_USE_LLM", "0") == "1"

    def generate(self, task: dict) -> Optional[dict]:
        """
        Returns:
            {
                "code": str,
                "source": "llm",
                "prompt_hash": str
            }
            OR None (fallback trigger)

        NOTE:
        - returned code is UNTRUSTED
        - must pass Architecture Guardian + STRICT TEST MODE
        """

        if not self.enabled:
            return None

        try:
            prompt = self._build_prompt(task)

            code = self._call_llm(prompt)

            if not code:
                return None

            # 🔒 PRE-FILTER (NOT SECURITY BOUNDARY)
            if not self._is_valid(code):
                return None

            return {
                "code": code,
                "source": "llm",
                "prompt_hash": hashlib.sha256(prompt.encode()).hexdigest()
            }

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
        """
        PRE-FILTER ONLY (non-authoritative)

        Final safety is enforced by:
        - Architecture Guardian
        - STRICT TEST MODE

        This only removes obvious unsafe patterns early.
        """

        forbidden = ["os.system", "subprocess", "exec(", "eval("]

        return not any(f in code for f in forbidden)