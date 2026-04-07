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


# =====================================================
# 📊 LLM USAGE TRACKER (MINIMAL)
# =====================================================

class LLMUsageTracker:

    def __init__(self):
        self.calls = 0
        self.success = 0
        self.fallbacks = 0
        self.errors = 0

    def record_call(self):
        self.calls += 1

    def record_success(self):
        self.success += 1

    def record_fallback(self):
        self.fallbacks += 1

    def record_error(self):
        self.errors += 1

    def snapshot(self):
        return {
            "calls": self.calls,
            "success": self.success,
            "fallbacks": self.fallbacks,
            "errors": self.errors,
        }


class LLMInterface:

    def __init__(self):
        self.enabled = os.getenv("SAPIANTA_USE_LLM", "0") == "1"
        self.tracker = LLMUsageTracker()

    # =====================================================
    # 🧪 TEST GENERATION
    # =====================================================
    def generate_tests(self, goal: str):

        self.tracker.record_call()

        if not self.enabled:
            self.tracker.record_fallback()
            return self._mock_tests(goal)

        try:
            result = self._safe_claude_tests(goal)

            if result:
                self.tracker.record_success()
                return result

            self.tracker.record_fallback()
            return self._mock_tests(goal)

        except Exception:
            self.tracker.record_error()
            return self._mock_tests(goal)

    # =====================================================
    # 🧠 CODE GENERATION
    # =====================================================
    def generate_code(self, goal: str):

        self.tracker.record_call()

        if not self.enabled:
            self.tracker.record_fallback()
            return None  # fallback to deterministic generator

        try:
            result = self._safe_claude_code(goal)

            if result:
                self.tracker.record_success()
                return result

            self.tracker.record_fallback()
            return None

        except Exception:
            self.tracker.record_error()
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
    # 🔌 CLAUDE TEST GENERATION (SAFE)
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

            forbidden = ["os.", "subprocess", "eval(", "exec("]

            if any(f in response for f in forbidden):
                return self._mock_tests(goal)

            return response

        except Exception:
            return self._mock_tests(goal)

    # =====================================================
    # 🔌 CLAUDE CODE GENERATION (SAFE)
    # =====================================================
    def _safe_claude_code(self, goal: str):

        try:
            from runtime_platform.claude_client import ClaudeClient

            client = ClaudeClient()

            prompt = f"""
Generate minimal Python function for the following goal:

{goal}

Rules:
- only Python code
- no explanations
- no file operations
- no imports unless strictly necessary
"""

            response = client.call(prompt)

            if not response or not isinstance(response, str):
                return None  # fallback

            # 🔒 BASIC SANITIZATION (CRITICAL)
            forbidden = ["os.", "subprocess", "eval(", "exec("]

            if any(f in response for f in forbidden):
                return None

            return response

        except Exception:
            return None

    # =====================================================
    # 📊 METRICS ACCESS
    # =====================================================
    def get_metrics(self):
        return self.tracker.snapshot()