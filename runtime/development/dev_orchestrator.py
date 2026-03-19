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

# 🔴 NOVO: AST patcher
from runtime.development.ast_function_patcher import ASTFunctionPatcher


def is_running_under_pytest():
    return "PYTEST_CURRENT_TEST" in os.environ


def _log(msg):
    print(f"[DEV_ORCH] {msg}")


def run_strict_generated_tests():

    _log("STRICT TEST MODE → validating generated modules")

    runner = TestRunner(project_root=".", timeout=10)
    diagnostics = runner.run_tests()

    no_tests_collected = diagnostics.tests_total == 0
    success = diagnostics.success and not no_tests_collected

    if no_tests_collected:
        _log("STRICT TEST FAILED → no tests collected")

    if not success:
        _log("STRICT TEST FAILED")
        _log(diagnostics.raw_output)
        _log(diagnostics.raw_error)
    else:
        _log("STRICT TEST PASSED")

    return {
        "success": success,
        "error": diagnostics.raw_output + diagnostics.raw_error,
        "output": diagnostics.raw_output
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

        self.current_patch = None

    # =================================================
    # ✅ AST FUNCTION REPLACEMENT (PRODUCTION READY)
    # =================================================

    def _apply_replace_function(self, fix: dict):

        file_path = fix.get("file")
        function_name = fix.get("function")
        new_code = fix.get("code")

        if not file_path or not function_name or not new_code:
            return False

        return ASTFunctionPatcher.replace_function(
            file_path,
            function_name,
            new_code
        )

    # =================================================
    # ✅ GOVERNANCE CHECK (FIX FOR TEST)
    # =================================================

    def _check_core_modification(self, plan):

        forbidden = ["runtime/system/"]

        for file in plan:
            for f in forbidden:
                if file.startswith(f):
                    raise Exception("Mutation forbidden")

        return True

    # ------------------------------------------------
    # APPLY FIX
    # ------------------------------------------------

    def apply_fix(self, fix, implementation_plan):

        if not fix:
            _log("No fix provided")
            return False

        action = fix.get("action")

        if not action and fix.get("strategy") in ["syntax_error", "syntax_fix"]:
            action = "replace_file"

        target_file = fix.get("file") or (
            implementation_plan[0] if implementation_plan else None
        )

        if not target_file:
            _log("No target file")
            return False

        path = Path(target_file)

        if not path.exists():
            _log(f"Target file missing: {target_file}")
            return False

        try:

            # FULL FILE REPLACE
            if action == "replace_file":

                new_code = fix.get("code")

                if not new_code:
                    _log("Missing code for replace_file")
                    return False

                _log("Applying FULL FILE REPLACE")
                path.write_text(new_code, encoding="utf-8")
                _log("File replaced successfully")
                return True

            # 🔴 AST FUNCTION REPLACE
            if action == "replace_function":

                _log(f"Applying replace_function → {fix.get('function')}")

                success = self._apply_replace_function(fix)

                if success:
                    _log("Function replaced successfully (AST)")
                    return True
                else:
                    _log("Function replace FAILED")
                    return False

            # fallback append
            if fix.get("code"):

                code = path.read_text(encoding="utf-8")

                if fix["code"].strip() in code:
                    _log("Fix already present")
                    return True

                with open(path, "a", encoding="utf-8") as f:
                    f.write("\n\n# --- AUTO FIX APPLIED ---\n")
                    f.write(fix["code"])
                    f.write("\n")

                _log("Fallback fix appended")
                return True

            return False

        except Exception as e:
            _log(f"apply_fix error: {e}")
            _log(traceback.format_exc())
            return False

    # ------------------------------------------------
    # AUTO MODE
    # ------------------------------------------------

    def run_auto(self, discussion_context=None):

        _log("AUTO MODE START")

        if not discussion_context:
            discussion_context = "Generic system improvement"

        try:

            architecture = self.propose_architecture(discussion_context)

            if not architecture["files_to_create"] and not architecture["files_to_modify"]:
                return self.run_implementation(discussion_context)

            implementation_plan = self.build_implementation_plan(architecture)

            self.mutation_guard.validate_patch(implementation_plan)

            _log("Generating modules...")

            for file_path in implementation_plan:

                path = Path(file_path)
                path.parent.mkdir(parents=True, exist_ok=True)

                self.code_generator.generate_module(
                    file_path,
                    architecture["description"]
                )

            MAX_RETRIES = 3
            strict_result = {"success": False}

            for attempt in range(MAX_RETRIES):

                _log(f"Test run {attempt + 1}")

                ok, err = self.execution_guard.validate()
                if not ok:
                    _log(f"EXECUTION GUARD TRIGGERED → {err}")
                    return False

                self.test_runner.run_tests()

                ok, err = self.execution_guard.validate()
                if not ok:
                    _log(f"EXECUTION GUARD TRIGGERED (post-test) → {err}")
                    return False

                strict_result = run_strict_generated_tests()

                if strict_result["success"]:
                    _log("Tests PASSED (strict)")
                    break

                _log("Tests FAILED → fixing")

                failure_info = strict_result
                error_text = failure_info.get("error", "")

                best_strategy = self.fix_memory.get_best_strategy(error_text)
                fixes = self.auto_fix_engine.generate_fixes(failure_info)

                if best_strategy:
                    fixes = sorted(
                        fixes,
                        key=lambda f: 0 if f.get("strategy") == best_strategy else 1
                    )
                    _log(f"Memory boost → prioritizing strategy: {best_strategy}")

                _log(f"Generated {len(fixes)} fix candidates")

                applied_success = False

                for fix in fixes:

                    _log(f"Trying fix strategy: {fix.get('strategy')}")

                    applied = self.apply_fix(fix, implementation_plan)

                    if not applied:
                        _log("Fix failed to apply → skipping")
                        continue

                    strict_result = run_strict_generated_tests()

                    if strict_result["success"]:
                        _log(f"Fix SUCCESS with strategy: {fix.get('strategy')}")

                        self.fix_memory.record_success(
                            error_text,
                            fix.get("strategy")
                        )

                        applied_success = True
                        break
                    else:
                        _log("Fix did not resolve issue → trying next")

                if not applied_success:
                    _log("All fixes failed → FAIL-CLOSED")
                    return False

            if strict_result["success"]:
                _log("AUTO MODE COMPLETE → SUCCESS")
                return True
            else:
                _log("AUTO MODE COMPLETE → FAILED")
                return False

        except Exception:
            _log("AUTO MODE FAILED")
            _log(traceback.format_exc())
            return None

    def propose_architecture(self, strategic_direction: str):

        repo_context = self.repo_context.summarize(
            self.ALLOWED_PATHS,
            self.FORBIDDEN_PATHS
        )

        enriched_prompt = f"""
SYSTEM CONTEXT
--------------
{repo_context}

DEVELOPMENT REQUEST
-------------------
{strategic_direction}
"""

        return self.architecture_agent.propose(enriched_prompt)

    def build_implementation_plan(self, architecture_proposal):

        return (
            architecture_proposal["files_to_create"] +
            architecture_proposal["files_to_modify"]
        )