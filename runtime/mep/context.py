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
        # --- Identiteta in čas ---
        self.context_id = str(uuid.uuid4())
        self.created_at = datetime.utcnow().isoformat()

        # --- Izvor ---
        self.source = source

        # --- HARD INVARIANT: origin marker ---
        # Nastavi ga IZKLJUČNO GuardLifecycleOrchestrator
        # MEP, guards, SP-ji ga NE smejo spreminjati
        self._origin = None

        # --- Status in faza ---
        self.status = Status.PENDING
        self.phase = Phase.INIT

        # --- Vhod (KANONIČNO: vedno string) ---
        self.input = raw_input
        self.normalized_input = raw_input.strip()

        # --- Metapodatki (SP-8, SP-9, stroški, kvote, rate, tenant …) ---
        # NE vpliva na normativne odločitve
        self.metadata = {}

        # --- Sledi odločitev in kršitev ---
        self.decisions = []
        self.violations = []

        # --- Rezultat ---
        self.result = None
        self.error = None

        # --- SP-5: Policy binding (minimalno) ---
        self.policy = {
            "source": "CANON",
            "version": "F47+",
            "bindings": ["MEP"]
        }
        self.policy_ok = None

        # --- SP-4: Explain layer (post-decision artifact, NON-NORMATIVE) ---
        # Mora vedno obstajati in ne sme vplivati na status
        self.explain = {}

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
