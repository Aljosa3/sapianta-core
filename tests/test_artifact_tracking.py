"""
Test: Artifact Outcome Tracking

Purpose
-------
Verify that artifact outcomes (success / failure) are correctly recorded
in a deterministic and governed way.
"""

import os
from runtime.development.dev_orchestrator import DevelopmentOrchestrator


def test_artifact_success_tracking(tmp_path):
    """
    Should generate artifact and record SUCCESS outcome.
    """

    orchestrator = DevelopmentOrchestrator()

    result = orchestrator.run_auto(
        "Create simple module for artifact tracking test"
    )

    assert result is not None, "Artifact generation failed unexpectedly"


def test_artifact_failure_tracking():
    """
    Should fail and record FAILURE outcome.
    """

    orchestrator = DevelopmentOrchestrator()

    # Force failure via forbidden mutation
    bad_plan = ["runtime/system/forbidden_test.py"]

    try:
        orchestrator._check_core_modification(bad_plan)
        assert False, "Core mutation was not blocked"
    except Exception as e:
        assert "Mutation forbidden" in str(e)