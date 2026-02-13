from typing import Callable, List

from sapianta_validation.architecture.validation_types import (
    ScenarioDefinition,
    ValidationFailure,
    ValidationResult,
    FailureType,
)
from sapianta_validation.determinism.snapshot_hasher import SnapshotHasher


class DeterministicSnapshotValidator:
    """
    Byte-level deterministic proof validator.
    """

    def __init__(self, executor: Callable):
        self.executor = executor

    def validate(self, scenario: ScenarioDefinition) -> ValidationResult:

        hashes: List[str] = []

        for _ in range(3):
            snapshot = self.executor(
                scenario.initial_state,
                scenario.events,
            )

            snapshot_dict = {
                "state": snapshot.state,
                "audit": getattr(snapshot, "audit_trace", []),
                "export": getattr(snapshot, "export_payload", {}),
            }

            hash_value = SnapshotHasher.hash_snapshot(snapshot_dict)
            hashes.append(hash_value)

        first_hash = hashes[0]

        for h in hashes[1:]:
            if h != first_hash:
                return ValidationResult(
                    scenario_name=scenario.name,
                    passed=False,
                    failures=[
                        ValidationFailure(
                            FailureType.DETERMINISM_FAILURE,
                            "Byte-level determinism violated",
                        )
                    ],
                )

        return ValidationResult(
            scenario_name=scenario.name,
            passed=True,
            failures=[],
        )
