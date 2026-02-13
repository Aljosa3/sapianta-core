from typing import List, Callable
import os

from sapianta_validation.architecture.validation_types import (
    ScenarioDefinition,
    ValidationFailure,
    CoverageRecord,
)
from sapianta_validation.architecture.coverage_matrix import CoverageMatrix
from sapianta_validation.architecture.failure_classification import (
    FailureClassifier,
)
from sapianta_validation.validators.determinism_validator import (
    DeterminismValidator,
)
from sapianta_validation.validators.invariant_validator import (
    InvariantValidator,
)
from sapianta_validation.boundary.boundary_import_validator import (
    BoundaryImportValidator,
)
from sapianta_validation.scenarios.closed_domain_enforcer import (
    ClosedDomainEnforcer,
)
from sapianta_validation.coverage.full_coverage_enforcer import (
    FullCoverageEnforcer,
)
from sapianta_validation.determinism.deterministic_snapshot_validator import (
    DeterministicSnapshotValidator,
)
from sapianta_validation.runner.validation_report import ValidationReport


class ValidationRunner:
    """
    Central industrial validation orchestrator.

    Responsibilities:
    - Constitution boundary enforcement
    - Closed event domain enforcement
    - Determinism validation (logical equality)
    - Byte-level deterministic snapshot hashing
    - Invariant validation
    - Coverage tracking
    - Full coverage enforcement (100% required)
    - Failure classification
    - Fail-fast enforcement
    """

    def __init__(
        self,
        scenarios: List[ScenarioDefinition],
        executor: Callable,
        registered_events: List[str],
    ):
        self.scenarios = scenarios
        self.executor = executor
        self.registered_events = registered_events

    def run(self) -> ValidationReport:
        """
        Executes full deterministic validation pipeline.
        Fail-fast on first violation.
        Pure in-memory.
        Deterministic.
        """

        # ------------------------------------------------------------------
        # Phase 9.1a — Constitution Enforcement
        # ------------------------------------------------------------------
        boundary_validator = BoundaryImportValidator(
            project_root=os.getcwd()
        )
        boundary_validator.validate()

        # ------------------------------------------------------------------
        # Phase 9.1b — Closed Event Domain Enforcement
        # ------------------------------------------------------------------
        closed_domain_enforcer = ClosedDomainEnforcer(
            registered_events=self.registered_events
        )
        closed_domain_enforcer.validate(self.scenarios)

        # ------------------------------------------------------------------
        # Core validation components
        # ------------------------------------------------------------------
        coverage = CoverageMatrix()
        determinism_validator = DeterminismValidator(self.executor)
        snapshot_validator = DeterministicSnapshotValidator(self.executor)
        invariant_validator = InvariantValidator()

        total = len(self.scenarios)
        passed = 0
        all_failures: List[ValidationFailure] = []
        determinism_confirmed = True

        # ------------------------------------------------------------------
        # Scenario Execution Loop
        # ------------------------------------------------------------------
        for scenario in self.scenarios:

            # --- Logical Determinism Validation ---
            det_result = determinism_validator.validate(scenario)

            if not det_result.passed:
                determinism_confirmed = False
                all_failures.extend(det_result.failures)
                raise Exception(
                    f"Fail-fast: Determinism violation in scenario '{scenario.name}'"
                )

            # --- Byte-Level Determinism Validation (Phase 9.1d) ---
            snapshot_result = snapshot_validator.validate(scenario)

            if not snapshot_result.passed:
                determinism_confirmed = False
                all_failures.extend(snapshot_result.failures)
                raise Exception(
                    f"Fail-fast: Byte-level determinism violation in scenario '{scenario.name}'"
                )

            # --- Execute Scenario (single final execution for invariant check) ---
            final_snapshot = self.executor(
                scenario.initial_state,
                scenario.events,
            )

            # --- Invariant Validation ---
            inv_result = invariant_validator.validate(
                scenario,
                final_snapshot.state,
            )

            if not inv_result.passed:
                all_failures.extend(inv_result.failures)
                raise Exception(
                    f"Fail-fast: Invariant violation in scenario '{scenario.name}'"
                )

            # --- Coverage Tracking ---
            coverage.add_record(
                CoverageRecord(
                    scenario=scenario.name,
                    events_tested=scenario.events,
                )
            )

            passed += 1

        # ------------------------------------------------------------------
        # Phase 9.1c — Full Coverage Enforcement (100% required)
        # ------------------------------------------------------------------
        full_coverage_enforcer = FullCoverageEnforcer(
            registered_events=self.registered_events
        )

        full_coverage_enforcer.validate(
            coverage_records=coverage._records
        )

        # ------------------------------------------------------------------
        # Post-Execution Aggregation
        # ------------------------------------------------------------------
        breakdown = FailureClassifier.classify(all_failures)

        coverage_percent = coverage.coverage_percentage(
            self.registered_events
        )

        invariant_score = 100.0 if passed == total else 0.0

        # ------------------------------------------------------------------
        # Final Validation Report (Pure Data Object)
        # ------------------------------------------------------------------
        return ValidationReport(
            total_scenarios=total,
            passed=passed,
            failed=total - passed,
            failure_breakdown=breakdown,
            coverage_percentage=coverage_percent,
            determinism_confirmed=determinism_confirmed,
            invariant_score=invariant_score,
        )
