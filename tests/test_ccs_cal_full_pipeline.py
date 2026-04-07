import os
from pathlib import Path

from runtime.development.dev_orchestrator import DevelopmentOrchestrator


def test_ccs_triggers_cal_and_fix_pipeline(tmp_path):
    """
    FULL PIPELINE TEST:

    1. create broken code
    2. run orchestrator
    3. CCS should reject
    4. CAL should generate fix
    5. AutoFix should repair
    6. final result should be success
    """

    # ------------------------------------------------------------
    # SETUP: isolated generated dir
    # ------------------------------------------------------------
    generated_dir = tmp_path / "runtime" / "development" / "generated"
    generated_dir.mkdir(parents=True, exist_ok=True)

    # NE spreminjaj global cwd

    # ------------------------------------------------------------
    # CREATE BROKEN MODULE (SyntaxError)
    # ------------------------------------------------------------
    module_path = generated_dir / "test_module.py"

    module_path.write_text(
        "def add(a, b)\n    return a + b\n",
        encoding="utf-8"
    )

    # ------------------------------------------------------------
    # RUN ORCHESTRATOR
    # ------------------------------------------------------------
    orchestrator = DevelopmentOrchestrator(execution_root=tmp_path)

    result = orchestrator.run_auto({
        "goal": "fix broken function"
    })

    # ------------------------------------------------------------
    # ASSERT PIPELINE RESULT
    # ------------------------------------------------------------
    assert isinstance(result, dict)

    # success lahko pride direktno ali po fixu
    assert (
        result.get("success") is True
        or result.get("reason") == "execution_completed_after_fix"
        or result.get("reason") == "execution_completed"
    )

    # ------------------------------------------------------------
    # VERIFY MODULE IS NOW VALID
    # ------------------------------------------------------------
    code = module_path.read_text(encoding="utf-8")

    # mora biti valid python
    compile(code, str(module_path), "exec")

    # mora vsebovati popravljeno funkcijo
    assert "def add" in code
    assert "return" in code