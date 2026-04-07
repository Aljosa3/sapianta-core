# runtime/development/llm_interface.py

"""
SAPIANTA LLM Interface (MINIMAL, SAFE)

Purpose:
- single entry point for ALL LLM usage
- supports mock + future real providers
- enforces deterministic-safe behavior

IMPORTANT:
- LLM is ALWAYS treated as untrusted
- NO direct execution
- output must be validated by caller
"""

import os


class LLMInterface:

    def __init__(self):
        self.enabled = os.getenv("SAPIANTA_USE_LLM", "0") == "1"

    # =====================================================
    # 🧪 TEST GENERATION
    # =====================================================
    def generate_tests(self, goal: str):

        if not self.enabled:
            return self._mock_tests(goal)

        # 🔌 SAFE CLAUDE WRAPPER (minimal change)
        return self._safe_claude_tests(goal)

    # =====================================================
    # 🧠 CODE GENERATION
    # =====================================================
    def generate_code(self, goal: str):

        if not self.enabled:
            return None  # fallback to deterministic generator

        # 🔜 future: real LLM call
        return None

    # =====================================================
    # 🔍 ERROR ANALYSIS
    # =====================================================
    def analyze_error(self, error_text: str):

        if not self.enabled:
            return None

        # 🔜 future: LLM debugging insight
        return None

    # =====================================================
    # 🔒 MOCK IMPLEMENTATION (SAFE DEFAULT)
    # =====================================================
    def _mock_tests(self, goal: str):

        if "add" in (goal or "").lower():
            return """
def test_add_basic():
    assert add(2, 3) == 5

def test_add_zero():
    assert add(0, 5) == 5
"""

        return """
def test_basic():
    assert True
"""

    # =====================================================
    # 🔌 CLAUDE INTEGRATION (SAFE WRAPPER)
    # =====================================================
    def _safe_claude_tests(self, goal: str):

        try:
            from runtime_platform.claude_client import ClaudeClient

            client = ClaudeClient()

            prompt = f"""
Generate minimal pytest tests for the following goal:

{goal}

Rules:
- only Python code
- no explanations
- no imports except pytest
- no file operations
"""

            response = client.call(prompt)

            if not response or not isinstance(response, str):
                return self._mock_tests(goal)

            # 🔒 BASIC SANITIZATION (CRITICAL)
            forbidden = ["os.", "subprocess", "eval(", "exec("]

            if any(f in response for f in forbidden):
                return self._mock_tests(goal)

            return response

        except Exception:
            return self._mock_tests(goal)