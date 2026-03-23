"""
SAPIANTA Minimal Repair Orchestrator (v0.3)

Enhancements:
- system context builder (v1)
- compatible with AutoFixEngine.generate_fixes
- non-breaking changes
"""

import re

from runtime.development.test_runner import TestRunner
from runtime.development.auto_fix_engine import AutoFixEngine
from runtime.development.dev_governance_gate import DevGovernanceGate
from runtime.development.fix_orchestrator import FixOrchestrator  # 🔥 MINIMAL ADD


# ================================================================
# FAILURE EXTRACTION
# ================================================================

def extract_failures(diagnostics):
    """
    Convert TestRunResult into failure list usable by fix engine.
    """
    failures = []

    if diagnostics.success:
        return failures

    for module in diagnostics.failed_modules:
        failures.append({
            "module": module,
            "raw_output": diagnostics.raw_output,
            "errors": diagnostics.raw_error,
            "error": diagnostics.raw_error,   # compatibility
            "output": diagnostics.raw_output  # compatibility
        })

    return failures


# ================================================================
# 🧠 SYSTEM CONTEXT BUILDER (SAFE v1)
# ================================================================

def _build_system_context(failure_info: dict) -> dict:

    context = {
        "missing_connections": [],
        "missing_imports": [],
        "missing_functions": []
    }

    error_text = failure_info.get("error", "") or ""
    output = failure_info.get("output", "") or ""

    combined = error_text + "\n" + output

    # ------------------------------------------------
    # 🔌 MISSING IMPORTS
    # ------------------------------------------------
    import_matches = re.findall(
        r"No module named '([\w\.]+)'",
        combined
    )

    for mod in import_matches:
        context["missing_imports"].append(mod)

    # ------------------------------------------------
    # 🔥 NAME ERROR → missing function
    # ------------------------------------------------
    name_matches = re.findall(
        r"NameError: name '(\w+)' is not defined",
        combined
    )

    for name in name_matches:
        context["missing_functions"].append(name)

    # ------------------------------------------------
    # 🔗 SIMPLE API MISMATCH
    # ------------------------------------------------
    if "generate_fix" in combined and "generate_fixes" in combined:
        context["missing_connections"].append(
            "generate_fix → generate_fixes mismatch"
        )

    # ------------------------------------------------
    # CLEAN DUPLICATES
    # ------------------------------------------------
    for key in context:
        context[key] = sorted(set(context[key]))

    return context


# ================================================================
# MAIN
# ================================================================

def main():
    print("🔧 SAPIANTA Repair Orchestrator (aligned v0.3)\n")

    # 1. Run tests
    print("▶ Running tests...")
    runner = TestRunner(project_root=".", timeout=10)
    diagnostics = runner.run_tests()

    if diagnostics.success:
        print(f"✅ All {diagnostics.tests_passed} tests passed.")
        return

    print(f"❌ {diagnostics.tests_failed} tests failed\n")

    failures = extract_failures(diagnostics)

    # 2. Initialize components
    fixer = AutoFixEngine()
    gate = DevGovernanceGate()
    fix_applicator = FixOrchestrator()  # 🔥 MINIMAL ADD

    # 3. Process failures
    for i, failure in enumerate(failures, start=1):
        print(f"\n--- Failure {i} ---")
        print(f"Module: {failure['module']}")

        # 🧠 BUILD SYSTEM CONTEXT
        try:
            system_context = _build_system_context(failure)
            failure["system_context"] = system_context

            print("\n🧠 System context:")
            print(system_context)

        except Exception as e:
            print(f"⚠️ Context build failed: {e}")

        # 3.1 Generate fixes
        try:
            fixes = fixer.generate_fixes(failure)
        except Exception as e:
            print(f"⚠️ Fix generation failed: {e}")
            continue

        if not fixes:
            print("⚠️ No fixes generated.")
            continue

        # 3.2 Process multiple fixes
        for fix in fixes:

            print("\n💡 Proposed fix:")
            print(fix)

            # Governance approval
            try:
                approved = gate.request_approval(fix)
            except Exception as e:
                print(f"⚠️ Governance gate error: {e}")
                continue

            if not approved:
                print("🚫 Fix rejected by governance.")
                continue

            # 🔥 MINIMAL FIX: fallback target_file + test → source
            try:
                target_file = fix.get("file")

                if not target_file:
                    module = failure.get("module")

                    if module:
                        module = module.replace("FAILED ", "").strip()

                        target_file = module.replace(".", "/") + ".py"

                        # 🔥 KLJUČNI FIX (2 vrstici)
                        if "test_" in target_file:
                            target_file = target_file.replace("test_", "")

                        fix["file"] = target_file

                if not target_file:
                    print("⚠️ No target file specified in fix")
                    continue

                success = fix_applicator._apply_fix(target_file, fix)

                if success:
                    print(f"✅ Fix applied to {target_file}")
                else:
                    print(f"⚠️ Fix application failed for {target_file}")

            except Exception as e:
                print(f"⚠️ Failed to apply fix: {e}")

    print("\n🔁 Repair cycle complete.")


if __name__ == "__main__":
    main()