"""
SAPIANTA Minimal Repair Orchestrator (v0.4)

Fixes:
- correct failure_info structure (test_output)
- FIXED: correct apply layer (FixOrchestrator)
"""

import re

from runtime.development.test_runner import TestRunner
from runtime.development.auto_fix_engine import AutoFixEngine
from runtime.development.dev_governance_gate import DevGovernanceGate
from runtime.development.fix_orchestrator import FixOrchestrator


# ================================================================
# FAILURE EXTRACTION (FIXED)
# ================================================================

def extract_failures(diagnostics):

    failures = []

    if diagnostics.success:
        return failures

    fi = diagnostics.failure_info if diagnostics.failure_info else {}

    for module in diagnostics.failed_modules:
        failures.append({
            "module": module,
            "error": fi.get("error") or diagnostics.raw_output or "",
            "test_output": fi.get("test_output") or diagnostics.raw_output or "",
            "file": fi.get("file"),
            "system_context": {}
        })

    return failures


# ================================================================
# SYSTEM CONTEXT
# ================================================================

def _build_system_context(failure_info: dict) -> dict:

    context = {
        "missing_connections": [],
        "missing_imports": [],
        "missing_functions": []
    }

    combined = (failure_info.get("error", "") or "") + "\n" + (failure_info.get("test_output", "") or "")

    context["missing_imports"].extend(
        re.findall(r"No module named '([\w\.]+)'", combined)
    )

    context["missing_functions"].extend(
        re.findall(r"NameError: name '(\w+)' is not defined", combined)
    )

    if "generate_fix" in combined and "generate_fixes" in combined:
        context["missing_connections"].append(
            "generate_fix → generate_fixes mismatch"
        )

    for key in context:
        context[key] = sorted(set(context[key]))

    return context


# ================================================================
# MAIN
# ================================================================

def main():
    print("🔧 SAPIANTA Repair Orchestrator (v0.4)\n")

    # ------------------------------------------------------------
    # TEST RUN
    # ------------------------------------------------------------
    print("▶ Running tests...")
    runner = TestRunner(project_root=".", timeout=10)
    diagnostics = runner.run_tests()

    if diagnostics.success:
        print(f"✅ All {diagnostics.tests_passed} tests passed.")
        return

    print(f"❌ {diagnostics.tests_failed} tests failed\n")

    failures = extract_failures(diagnostics)

    # ------------------------------------------------------------
    # INIT
    # ------------------------------------------------------------
    fixer = AutoFixEngine()
    gate = DevGovernanceGate()
    fix_applicator = FixOrchestrator()  # 🔥 KLJUČ

    # ------------------------------------------------------------
    # PROCESS
    # ------------------------------------------------------------
    for i, failure in enumerate(failures, start=1):

        print(f"\n--- Failure {i} ---")
        print(f"Module: {failure['module']}")

        try:
            system_context = _build_system_context(failure)
            failure["system_context"] = system_context

            print("\n🧠 System context:")
            print(system_context)

        except Exception as e:
            print(f"⚠️ Context build failed: {e}")

        # --------------------------------------------------------
        # GENERATE FIXES
        # --------------------------------------------------------
        try:
            fixes = fixer.generate_fixes(failure)
        except Exception as e:
            print(f"⚠️ Fix generation failed: {e}")
            continue

        if not fixes:
            print("⚠️ No fixes generated.")
            continue

        # --------------------------------------------------------
        # APPLY FIXES
        # --------------------------------------------------------
        for fix in fixes:

            print("\n💡 Proposed fix:")
            print(fix)

            try:
                approved = gate.request_approval(fix)
            except Exception as e:
                print(f"⚠️ Governance error: {e}")
                continue

            if not approved:
                print("🚫 Rejected by governance")
                continue

            # ----------------------------------------------------
            # TARGET FILE
            # ----------------------------------------------------
            target_file = fix.get("file")

            if not target_file:
                module = failure.get("module")
                if module:
                    module = module.replace("FAILED ", "").strip()
                    target_file = module.replace(".", "/") + ".py"

            if target_file and "test_" in target_file:
                target_file = target_file.replace("test_", "")

            if not target_file:
                print("⚠️ No target file")
                continue

            fix["file"] = target_file

            print("[APPLY TARGET]", target_file)

            # ----------------------------------------------------
            # 🔥 PRAVILEN APPLY
            # ----------------------------------------------------
            success = fix_applicator._apply_fix(target_file, fix)

            if success:
                print(f"✅ FIX APPLIED → {target_file}")

                print("\n🔁 Re-running tests after fix...")

                diagnostics = runner.run_tests()

                if diagnostics.success:
                    print("🎉 FIX SUCCESSFUL → TESTS PASSED")
                    return
                else:
                    print("⚠️ Fix did not resolve issue, continuing...")

                break
            else:
                print("⚠️ APPLY FAILED")

    print("\n🔁 Repair cycle complete.")


if __name__ == "__main__":
    main()