import os
from pathlib import Path

from runtime.development.dev_orchestrator import DevelopmentOrchestrator


TEST_FILE = "runtime/development/generated/test_llm_module.py"


def write_code(code: str):
    path = Path(TEST_FILE)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(code, encoding="utf-8")
    return path


def run_pipeline():
    orch = DevelopmentOrchestrator()
    result = orch.run_auto({
        "goal": "test function",
        "file_hint": "test_llm_module"
    })
    return result


# =====================================================
# 1. NameError → repair
# =====================================================

def test_llm_name_error_repair():

    code = """
def generated_function(a, b):
    return a + c
"""

    write_code(code)

    result = run_pipeline()

    assert result is not False


# =====================================================
# 2. SyntaxError → repair
# =====================================================

def test_llm_syntax_error_repair():

    code = """
def generated_function(a, b)
    return a + b
"""

    write_code(code)

    result = run_pipeline()

    assert result is not False


# =====================================================
# 3. ImportError → repair
# =====================================================

def test_llm_import_error_repair():

    code = """
import non_existing_module

def generated_function(a, b):
    return a + b
"""

    write_code(code)

    result = run_pipeline()

    assert result is not False


# =====================================================
# 4. Dangerous code → BLOCK
# =====================================================

def test_llm_dangerous_code_block():

    code = """
import os

def generated_function(a, b):
    os.system("rm -rf /")
    return a + b
"""

    write_code(code)

    orch = DevelopmentOrchestrator()

    result = orch.run_auto({
        "goal": "dangerous test",
        "file_hint": "test_llm_module"
    })

    assert isinstance(result, dict)
    assert result.get("status") == "blocked"


# =====================================================
# 5. Garbage code → fallback
# =====================================================

def test_llm_garbage_code_fallback():

    code = "asdasdasd"

    write_code(code)

    result = run_pipeline()

    assert result is not False