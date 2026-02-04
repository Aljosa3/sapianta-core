# validator_pipeline_v020.py
#
# SAPIANTA v0.20
# Validator integration pipeline (Module Graph Pass)
#
# PURPOSE:
# - Integrates ModuleGraphPass into the existing validation flow
# - Acts as a hard gate BEFORE any writing occurs
#
# LOCKED BY:
# - PHASE_v0.20_MULTI_FILE_MODULE_LOCK.md
# - PHASE_v0.20_IMPLEMENTATION_CHECKLIST.md
#
# IMPORTANT:
# - This file does NOT replace the existing validator
# - It composes validation steps deterministically
# - Any failure here MUST hard-fail the build


from typing import Dict

from sapianta_chat.validation.module_graph_pass import (
    ModuleGraphPass,
    ModuleGraphValidationError,
)


class ValidationHardFail(Exception):
    """
    Canonical hard-fail exception for the validation pipeline.
    """
    pass


class ValidatorPipelineV020:
    """
    v0.20 validation pipeline.

    Input:
        files: Dict[str, str]
            Mapping of FILE path -> file content

    Behavior:
        - Executes Module Graph Pass
        - Propagates HARD FAIL on any violation
        - Produces no side effects
    """

    def __init__(self, files: Dict[str, str]) -> None:
        self.files = files

    def run(self) -> None:
        """
        Executes the v0.20 validator pipeline.

        PASS:
            returns None

        FAIL:
            raises ValidationHardFail
        """
        try:
            self._run_module_graph_pass()
        except ModuleGraphValidationError as e:
            raise ValidationHardFail(str(e)) from e

    # ------------------------------------------------------------
    # v0.20 Phase — Module Graph Pass
    # ------------------------------------------------------------

    def _run_module_graph_pass(self) -> None:
        graph_pass = ModuleGraphPass(self.files)
        graph_pass.run()
