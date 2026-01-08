from enum import Enum


class DryRunStatus(Enum):
    """
    Status dry-run rezultata.
    Ne predstavlja odločitve, temveč opis stanja.
    """

    UNKNOWN = "UNKNOWN"
    ELIGIBLE = "ELIGIBLE"
    INELIGIBLE = "INELIGIBLE"
    REFUSED = "REFUSED"
    ERROR = "ERROR"


class DryRunResult:
    """
    Tehnični rezultat dry-run evaluacije.
    """

    def __init__(self, status: DryRunStatus, details=None):
        self.status = status
        self.details = details
