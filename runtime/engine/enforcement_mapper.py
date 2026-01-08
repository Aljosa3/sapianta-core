from runtime.models.enforcement_level import EnforcementLevel
from runtime.models.dry_run_result import DryRunStatus


class EnforcementMapper:
    """
    Čista preslikava E-nivojev v DryRunStatus.
    Brez odločanja, brez executiona.
    """

    MAP = {
        EnforcementLevel.E0: DryRunStatus.ELIGIBLE,
        EnforcementLevel.E1: DryRunStatus.INELIGIBLE,
        EnforcementLevel.E2: DryRunStatus.REFUSED,
        EnforcementLevel.E3: DryRunStatus.ERROR,
    }

    @classmethod
    def map(cls, level: EnforcementLevel) -> DryRunStatus:
        return cls.MAP.get(level, DryRunStatus.UNKNOWN)
