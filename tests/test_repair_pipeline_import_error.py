from pathlib import Path

from runtime.development.auto_fix_engine import AutoFixEngine
from runtime.development.dev_orchestrator import DevelopmentOrchestrator


def test_full_self_healing_pipeline_import_error(tmp_path):

    generated_dir = tmp_path / "runtime" / "development" / "generated"
    generated_dir.mkdir(parents=True, exist_ok=True)

    module_path = generated_dir / "test_module.py"

    broken_code = """
import non_existing_module

def test_func():
    return 1
"""
    module_path.write_text(broken_code, encoding="utf-8")

    failure_info = {
        "error": "ModuleNotFoundError: No module named 'non_existing_module'",
        "file": str(module_path),
        "system_context": {}
    }

    engine = AutoFixEngine()
    orchestrator = DevelopmentOrchestrator()

    fixes = engine.generate_fixes(failure_info)

    assert len(fixes) > 0

    # 🔥 POSODOBLJENO: nova strategija
    target_fix = next(
        fix for fix in fixes
        if fix.get("strategy") == "import_error_try_wrapper"
    )

    applied = orchestrator.apply_fix(
        target_fix,
        implementation_plan=[str(module_path)]
    )

    assert applied is True

    repaired_code = module_path.read_text(encoding="utf-8")

    # 🔥 ZDAJ PRIČAKUJEMO SUCCESS (ne več failure)
    compile(repaired_code, str(module_path), "exec")

    namespace = {}
    exec(compile(repaired_code, str(module_path), "exec"), namespace)

    assert "test_func" in namespace