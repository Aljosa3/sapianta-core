# runtime/mep/context.py

from datetime import datetime
from enum import Enum
import uuid


class Status(str, Enum):
    PENDING = "PENDING"
    ALLOW = "ALLOW"
    DENY = "DENY"
    HALT = "HALT"
    HARD_FAIL = "HARD_FAIL"
    FINAL = "FINAL"


class Phase(str, Enum):
    INIT = "INIT"
    EXECUTION = "EXECUTION"
    FINAL = "FINAL"


class ExecutionContext:
    """
    Minimal Execution Context (MEP)
    Skladno z F52_EXECUTION_CONTEXT.md
    """

    def __init__(self, source: str, raw_input: str):
        self.context_id = str(uuid.uuid4())
        self.created_at = datetime.utcnow().isoformat()

        self.source = source

        self.status = Status.PENDING
        self.phase = Phase.INIT

        self.input = raw_input
        self.normalized_input = raw_input.strip()

        self.decisions = []
        self.violations = []

        self.result = None
        self.error = None

    def add_decision(self, note: str):
        self.decisions.append({
            "time": datetime.utcnow().isoformat(),
            "note": note
        })

    def add_violation(self, note: str):
        self.violations.append({
            "time": datetime.utcnow().isoformat(),
            "note": note
        })

    def finalize(self, status: Status, result=None, error=None):
        self.status = status
        self.phase = Phase.FINAL
        self.result = result
        self.error = error
