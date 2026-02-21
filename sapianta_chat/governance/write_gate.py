# sapianta_chat/governance/write_gate.py

from pathlib import Path


class WriteGateDeny(Exception):
    """Raised when WRITE-GATE denies a write operation."""
    pass


class WriteGate:
    """
    WRITE-GATE v1.0 — minimal, deterministic, governance-only.

    Responsibilities:
    - evaluate explicit WRITE-INTENT
    - enforce promotion preconditions
    - ALLOW or DENY (hard)
    """

    def __init__(
        self,
        *,
        artifact: str,
        source_path: Path,
        target_root: Path,
        validator_passed: bool,
    ):
        self.artifact = artifact
        self.source_path = source_path
        self.target_root = target_root
        self.validator_passed = validator_passed

    def evaluate(self) -> None:
        """
        Evaluate WRITE-INTENT legitimacy.

        Raises:
            WriteGateDeny on any violation.
        """

        # 1. Explicitness checks
        if not self.artifact:
            raise WriteGateDeny("Missing artifact identifier.")

        if not self.source_path:
            raise WriteGateDeny("Missing source path.")

        if not self.target_root:
            raise WriteGateDeny("Missing target canonical domain.")

        # 2. Source existence
        if not self.source_path.exists():
            raise WriteGateDeny(
                f"Source path does not exist: {self.source_path}"
            )

        # 3. Validator authority
        if not self.validator_passed:
            raise WriteGateDeny(
                "Validator result is not PASS."
            )

        # 4. Target collision prevention
        target_path = self.target_root / self.artifact
        if target_path.exists():
            raise WriteGateDeny(
                f"Target already exists: {target_path}"
            )

        # If all checks pass → ALLOW (implicit)
        return None
