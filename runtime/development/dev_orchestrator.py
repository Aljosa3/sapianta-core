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
import subprocess

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

# 🔥 STRUCTURE-AWARE PATCHER
from runtime.development.function_patcher import FunctionPatcher


# ------------------------------------------------
# EXECUTION CONTEXT DETECTOR
# ------------------------------------------------

def is_running_under_pytest():
    return "PYTEST_CURRENT_TEST" in os.environ


def _log(msg):
    print(f"[DEV_ORCH] {msg}")


# ------------------------------------------------
# STRICT TEST VALIDATION
# ------------------------------------------------

def run_strict_generated_tests():

    _log("STRICT TEST MODE → validating generated modules")

    result = subprocess.run(
        ["pytest", "-vv", "runtime/development/generated"],
        capture_output=True,
        text=True
    )

    output_text = result.stdout + result.stderr

    no_tests_collected = "collected 0 items" in output_text
    success = (result.returncode == 0) and not no_tests_collected

    if no_tests_collected:
        _log("STRICT TEST FAILED → no tests collected")

    if not success:
        _log("STRICT TEST FAILED")
        _log(result.stdout)
        _log(result.stderr)
    else:
        _log("STRICT TEST PASSED")

    return {
        "success": success,
        "error": output_text,
        "output": result.stdout
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

        self.test_runner = TestRunner()
        self.auto_fix_engine = AutoFixEngine()

        self.current_patch = None

    # ------------------------------------------------
    # APPLY FIX (STRUCTURE-AWARE)
    # ------------------------------------------------

    def apply_fix(self, fix, implementation_plan):

        if not fix:
            _log("No fix provided")
            return False

        action = fix.get("action")

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
            code = path.read_text(encoding="utf-8")

            # --------------------------------------------
            # 🔥 STRUCTURE-AWARE PATCH
            # --------------------------------------------
            if action == "replace_function":

                function_name = fix.get("function")
                new_function_code = fix.get("code")

                if not function_name or not new_function_code:
                    _log("Invalid replace_function payload")
                    return False

                _log(f"Applying replace_function → {function_name}")

                new_code = FunctionPatcher.replace_function(
                    code,
                    function_name,
                    new_function_code
                )

                path.write_text(new_code, encoding="utf-8")

                _log("Function replaced successfully")
                return True

            # --------------------------------------------
            # FALLBACK (append)
            # --------------------------------------------
            if fix.get("code"):

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
    # AUTO MODE (MULTI-FIX LOOP 🔥)
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

            # -------------------------
            # TEST + MULTI-FIX LOOP
            # -------------------------

            MAX_RETRIES = 3

            for attempt in range(MAX_RETRIES):

                _log(f"Test run {attempt + 1}")

                test_result = self.test_runner.run_tests()
                strict_result = run_strict_generated_tests()

                if strict_result["success"]:
                    _log("Tests PASSED (strict)")
                    test_result.success = True
                    break

                _log("Tests FAILED → fixing")

                failure_info = strict_result

                # 🔥 MULTI-FIX ENGINE
                fixes = self.auto_fix_engine.generate_fixes(failure_info)

                _log(f"Generated {len(fixes)} fix candidates")

                applied_success = False

                for fix in fixes:

                    _log(f"Trying fix strategy: {fix.get('strategy')}")

                    applied = self.apply_fix(fix, implementation_plan)

                    if not applied:
                        _log("Fix failed to apply → skipping")
                        continue

                    # re-run strict test
                    strict_result = run_strict_generated_tests()

                    if strict_result["success"]:
                        _log(f"Fix SUCCESS with strategy: {fix.get('strategy')}")
                        applied_success = True
                        break
                    else:
                        _log("Fix did not resolve issue → trying next")

                if not applied_success:
                    _log("All fixes failed")
                    break

            else:
                _log("Max retries reached → FAIL")
                return None

            _log("AUTO MODE COMPLETE")
            return True

        except Exception:
            _log("AUTO MODE FAILED")
            _log(traceback.format_exc())
            return None

    # ------------------------------------------------
    # HELPERS
    # ------------------------------------------------

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