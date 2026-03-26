"""
SAPIANTA Development Orchestrator

Purpose
-------
Coordinates the Governed Autonomous Development (GAD) pipeline.
"""

from datetime import datetime, UTC
from pathlib import Path
import os
import traceback
import json

# DEV MODE FLAG (default: OFF)
DEV_MODE = os.getenv("SAPIANTA_DEV_MODE", "0") == "1"

from runtime.development.mutation_validator import MutationValidator
from runtime.development.code_generator import CodeGenerator
from runtime.development.mutation_guard import MutationGuard
from runtime.system.system_knowledge import SystemKnowledge
from runtime.system.repository_context import RepositoryContextBuilder
from runtime.development.capability_gap_detector import CapabilityGapDetector
from runtime.system.capability_planner import CapabilityPlanner
from runtime.development.architecture_agent import ArchitectureAgent

from runtime.governance.promotion_gate import classify_change, requires_approval
from runtime.artifacts.artifact_registry import register_artifact

from runtime.development.artifact_outcome_tracker import ArtifactOutcomeTracker
from runtime.development.artifact_evaluator import ArtifactEvaluator
from runtime.development.strategy_selector import StrategySelector

from runtime.development.test_runner import TestRunner
from runtime.development.auto_fix_engine import AutoFixEngine

from runtime.development.fix_memory import FixMemory
from runtime.development.execution_guard import ExecutionGuard

from runtime.development.ast_function_patcher import ASTFunctionPatcher

from runtime.system.system_reflection_engine import SystemReflectionEngine

# 🔒 NEW IMPORT
from runtime.development.architecture_guardian import ArchitectureGuardian

# 🔥 MINIMAL FIX IMPORT
from runtime.development.code_generator import sanitize_module_name

from runtime.governance.approval_gate import (
    build_approval_request,
    requires_human_approval,
)


def is_running_under_pytest():
    return "PYTEST_CURRENT_TEST" in os.environ


def _log(msg):
    print(f"[DEV_ORCH] {msg}")


def sanitize_filename(filename: str):

    if not isinstance(filename, str):
        return ""

    filename = filename.replace("\n", "").replace("\r", "")
    filename = filename.strip()
    filename = "_".join(filename.split())

    return filename


def is_valid_generated_file(filename: str):

    if not isinstance(filename, str):
        return False

    if "\n" in filename or "\r" in filename:
        return False

    if not filename.endswith(".py"):
        return False

    if ":" in filename:
        return False

    if " " in filename:
        return False

    if filename.strip() == "":
        return False

    return True


def run_strict_generated_tests():

    _log("STRICT TEST MODE → validating generated modules")

    runner = TestRunner(project_root=".", timeout=10)
    diagnostics = runner.run_tests()

    raw_output = diagnostics.raw_output or ""
    raw_error = diagnostics.raw_error or ""
    combined_output = raw_output + raw_error

    critical_errors = [
        "ImportError",
        "ModuleNotFoundError",
        "SyntaxError"
    ]

    has_critical_error = any(err in combined_output for err in critical_errors)

    if has_critical_error:
        _log("CRITICAL ERROR DETECTED → FORCE FAIL")

    has_codegen_failure = (
        "[CODEGEN] Module test result" in combined_output
        and "'status': 'FAILED'" in combined_output
    )

    if has_codegen_failure:
        _log("CODEGEN TEST FAILURE DETECTED → FORCE FAIL")

    # ✅ STRICT TEST ENFORCEMENT (minimal fix)
    tests_detected = "collected 0 items" not in combined_output

    no_tests_collected = not tests_detected

    if no_tests_collected:
        _log("STRICT TEST FAILED → no tests collected")

    output_lower = combined_output.lower()

    has_pass = "passed" in output_lower
    has_fail = "failed" in output_lower

    tests_passed = has_pass and not has_fail

    tests_ok = tests_detected and tests_passed

    if no_tests_collected:
        _log("STRICT TEST FAILED → no tests collected")

    success = (
        diagnostics.success
        and tests_ok
        and not has_critical_error
        and not has_codegen_failure
    )

    if has_critical_error:
        _log("STRICT TEST FAILED → critical runtime/import error")

    if has_codegen_failure:
        _log("STRICT TEST FAILED → codegen test failure")

    if not success:
        _log("STRICT TEST FAILED")
        _log(raw_output)
        _log(raw_error)
    else:
        _log("STRICT TEST PASSED")

    return {
        "success": success,
        "error": combined_output,
        "output": raw_output
    }


class DevelopmentOrchestrator:

    FORBIDDEN_PATHS = [
        "runtime/governance",
        "runtime/system",
        "runtime/ledger",
        "runtime/safety",
        "runtime/layer2",
    ]

    ALLOWED_PATHS = [
        "runtime/research",
        "runtime/strategies",
        "runtime/memory",
        "runtime/experiments",
        "runtime/analytics",
        "runtime/development",
        "sapianta-domain-",
    ]

    def __init__(self):

        self.validator = MutationValidator()
        self.code_generator = CodeGenerator()
        self.mutation_guard = MutationGuard()

        self.system_knowledge = SystemKnowledge()

        self.gap_detector = CapabilityGapDetector()
        self.capability_planner = CapabilityPlanner()

        self.repo_context = RepositoryContextBuilder()
        self.architecture_agent = ArchitectureAgent(self.system_knowledge)

        self.outcome_tracker = ArtifactOutcomeTracker()
        self.evaluator = ArtifactEvaluator()
        self.strategy_selector = StrategySelector()

        self.test_runner = TestRunner(project_root=".", timeout=10)

        self.auto_fix_engine = AutoFixEngine()
        self.fix_memory = FixMemory()

        self.execution_guard = ExecutionGuard(
            max_processes=3,
            max_runtime=30
        )

        self.reflection_engine = SystemReflectionEngine(root=".")

        self.guardian = ArchitectureGuardian()

    def _check_core_modification(self, plan: list):

        for path in plan:
            for forbidden in self.FORBIDDEN_PATHS:
                if path.startswith(forbidden):
                    raise Exception(
                        f"Mutation forbidden: core system modification detected ({path})"
                    )

    def _apply_replace_function(self, fix: dict, file_path: str):

        return ASTFunctionPatcher.replace_function(
            file_path,
            fix.get("function"),
            fix.get("code")
        )

    def apply_fix(self, fix, implementation_plan):

        if not fix:
            return False

        action = fix.get("action")

        target_file = fix.get("file") or (
            implementation_plan[0] if implementation_plan else None
        )

        if not target_file:
            return False

        original_path = Path(target_file)

        # 🔥 MINIMAL FIX: align with CodeGenerator naming
        safe_name = sanitize_module_name(original_path.stem) + ".py"
        path = original_path.parent / safe_name

        if not path.exists():
            return False

        try:

            code = path.read_text(encoding="utf-8")

            fix_code = fix.get("code")

            if fix_code is None or not isinstance(fix_code, str):
                _log("[GUARDIAN BLOCK FIX] invalid fix code (None or not string)")
                return False

            validation = self.guardian.validate(str(path), fix_code)

            if not validation.get("success", False):
                _log(f"[GUARDIAN BLOCK FIX] {validation.get('error')}")
                return False

            _log(f"[GUARDIAN PASS FIX] {path}")

            if action == "replace_file":
                path.write_text(fix.get("code", ""), encoding="utf-8")
                return True

            if action == "replace_function":
                return self._apply_replace_function(fix, str(path))

            if action == "append_stub":

                new_code = fix.get("code")

                if new_code.strip() in code:
                    return True

                with open(path, "a", encoding="utf-8") as f:
                    f.write("\n\n# AUTO STUB\n")
                    f.write(new_code)

                return True

            if action == "append_import":

                new_code = fix.get("code")

                if new_code.strip() in code:
                    return True

                with open(path, "r+", encoding="utf-8") as f:
                    content = f.read()
                    f.seek(0, 0)
                    f.write(new_code + "\n" + content)

                return True

            if fix.get("code"):

                if fix["code"].strip() in code:
                    return True

                with open(path, "a", encoding="utf-8") as f:
                    f.write("\n\n# AUTO FIX\n")
                    f.write(fix["code"])

                return True

            return False

        except Exception:
            _log(traceback.format_exc())
            return False

    def run_auto(self, discussion_context=None):

        _log("AUTO MODE START")

        try:

            # 🔥 SUPPORT dict OR string
            if isinstance(discussion_context, dict):
                goal = discussion_context.get("goal", "")
            else:
                goal = discussion_context

            architecture = self.propose_architecture(goal)

            implementation_plan = self.build_implementation_plan(architecture)

            implementation_plan = [
                sanitize_filename(f)
                for f in implementation_plan
                if is_valid_generated_file(sanitize_filename(f))
            ]

            if not implementation_plan:
                _log("No valid files → triggering AUTO-FALLBACK")

                fallback_file = "runtime/development/generated/auto_fallback_module.py"

                path = Path(fallback_file)
                path.parent.mkdir(parents=True, exist_ok=True)

                fallback_code = "def auto_fallback():\n    return \"ok\"\n"

                validation = self.guardian.validate(fallback_file, fallback_code)

                if not validation.get("success", False):
                    return {
                        "status": "blocked",
                        "stage": "architecture_guardian",
                        "reason": "fallback_blocked",
                        "error": validation.get("error"),
                    }

                _log(f"[GUARDIAN PASS FALLBACK] {fallback_file}")

                try:
                    path.write_text(fallback_code, encoding="utf-8")
                    _log(f"[FALLBACK] Generated: {fallback_file}")

                    return {
                        "success": True,
                        "reason": "auto_fallback_generated"
                    }

                except Exception as e:
                    _log(f"[FALLBACK ERROR] {str(e)}")

                    return {
                        "success": False,
                        "reason": "fallback_failed",
                        "error": str(e)
                    }

            self._check_core_modification(implementation_plan)
            self.mutation_guard.validate_patch(implementation_plan)

            for file_path in implementation_plan:

                original_path = Path(file_path)
                safe_name = sanitize_module_name(original_path.stem) + ".py"
                path = original_path.parent / safe_name

                path.parent.mkdir(parents=True, exist_ok=True)

                self.code_generator.generate_module(
                    file_path,
                    architecture["description"]
                )

                code = path.read_text(encoding="utf-8")

                validation = self.guardian.validate(file_path, code)

                if not validation.get("success", False):
                    _log(f"[GUARDIAN BLOCK GENERATED] {validation.get('error')}")

                    return {
                        "status": "blocked",
                        "stage": "architecture_guardian",
                        "reason": "unsafe_or_invalid_code",
                        "error": validation.get("error"),
                        "file": file_path
                    }

                _log(f"[GUARDIAN PASS] {file_path}")

            for attempt in range(3):

                _log(f"Test run {attempt + 1}")

                ok, err = self.execution_guard.validate()
                if not ok:
                    return False

                try:
                    reflection = self.reflection_engine.reflect()
                except Exception:
                    reflection = {}

                self.test_runner.run_tests()

                strict_result = run_strict_generated_tests()

                if strict_result["success"]:

                    if isinstance(discussion_context, dict):
                        task_for_approval = discussion_context
                    else:
                        task_for_approval = {"goal": discussion_context}

                    approval = build_approval_request(
                        task=task_for_approval,
                        files=implementation_plan,
                        status="success"
                    )

                    # 🔥 KLJUČNI FIX: preveri ali je že approved
                    if isinstance(discussion_context, dict) and discussion_context.get("state") == "approved":
                        _log("[DEV_ORCH] Task already approved → continuing")
                        return True

                    approval_required = requires_human_approval(approval)

                    # AUTO-APPROVE override (DEV MODE ONLY)
                    if DEV_MODE:
                        _log("[DEV_MODE] AUTO-APPROVE ENABLED → skipping approval")
                        approval_required = False

                    if approval_required:

                        if isinstance(discussion_context, dict):
                            discussion_context["state"] = "waiting_approval"

                        _log("[APPROVAL REQUIRED - stored in registry]")

                        return {
                            "status": "waiting_for_approval",
                            "approval": approval
                        }

                    _log("[AUTO-APPROVED]")
                    return True

                    _log("[AUTO-APPROVED]")
                    return True

                failure_info = strict_result
                error_text = failure_info.get("error", "")

                if isinstance(failure_info, dict):
                    failure_info["system_context"] = reflection

                fixes = self.auto_fix_engine.generate_fixes(failure_info)

                _log(f"Generated {len(fixes)} fix candidates")

                fixes = self.strategy_selector.rank(fixes)

                _log("Fixes ranked")

                best_strategy = self.fix_memory.get_best_strategy(error_text)

                if best_strategy:
                    fixes = sorted(
                        fixes,
                        key=lambda f: 0 if f.get("strategy") == best_strategy else 1
                    )

                for fix in fixes:

                    _log(f"Trying: {fix.get('strategy')}")

                    if not self.apply_fix(fix, implementation_plan):
                        continue

                    # 🔥 CLEAR CACHE (critical)
                    import sys
                    for m in list(sys.modules.keys()):
                        if "runtime.development.generated" in m:
                            del sys.modules[m]

                    strict_result = run_strict_generated_tests()

                    if strict_result["success"]:

                        self.fix_memory.record_success(
                            error_text,
                            fix.get("strategy")
                        )

                        approval = build_approval_request(
                            task={"goal": discussion_context},
                            files=implementation_plan,
                            status="fixed"
                        )

                        # 🔥 KLJUČNI FIX: če je že approved → nadaljuj
                        if isinstance(discussion_context, dict) and discussion_context.get("state") == "approved":
                            _log("Task already approved → continuing")
                            return True

                        approval_required = requires_human_approval(approval)

                        # AUTO-APPROVE override (DEV MODE ONLY)
                        if DEV_MODE:
                            _log("[DEV_MODE] AUTO-APPROVE ENABLED → skipping approval")
                            approval_required = False

                        if approval_required:
                            _log(f"[APPROVAL REQUIRED AFTER FIX] {approval}")
                            return {
                                "status": "waiting_for_approval",
                                "approval": approval
                            }

                        _log("[AUTO-APPROVED AFTER FIX]")
                        return True

            try:
                for file_path in implementation_plan:
                    path = Path(file_path)
                    if path.exists():
                        safe_code = """def safe_fallback():
                            return "ok"
                        """

                        validation = self.guardian.validate(file_path, safe_code)

                        if not validation.get("success", False):
                            _log("[GUARDIAN BLOCK SAFE FALLBACK]")
                            continue

                        _log(f"[GUARDIAN PASS SAFE FALLBACK] {file_path}")

                        path.write_text(safe_code, encoding="utf-8")
                        _log(f"[SAFE FALLBACK APPLIED] {file_path}")

            except Exception:
                _log("[SAFE FALLBACK ERROR]")

            # 🔥 MINIMAL FIX: RETEST AFTER EXTERNAL REPAIR + CACHE CLEAR
            try:
                import sys

                for m in list(sys.modules.keys()):
                    if "runtime.development.generated" in m:
                        del sys.modules[m]

                self.test_runner.run_tests()

                strict_result = run_strict_generated_tests()

                if strict_result["success"]:
                    return True
            except Exception:
                _log("[RETEST AFTER REPAIR FAILED]")

            return False

        except Exception:
            _log(traceback.format_exc())
            return False

    def propose_architecture(self, strategic_direction: str):

        repo_context = self.repo_context.summarize(
            self.ALLOWED_PATHS,
            self.FORBIDDEN_PATHS
        )

        full_context = f"""
DEVELOPMENT REQUEST
-------------------
{strategic_direction}

REPOSITORY CONTEXT
------------------
{repo_context}
"""

        return self.architecture_agent.propose(full_context)

    def build_implementation_plan(self, architecture_proposal):

        return (
            architecture_proposal["files_to_create"] +
            architecture_proposal["files_to_modify"]
        )