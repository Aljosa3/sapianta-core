from runtime.models.dry_run_result import DryRunResult, DryRunStatus
from runtime.models.enforcement_level import EnforcementLevel
from runtime.engine.enforcement_mapper import EnforcementMapper


class DryRunEngine:
    """
    Runtime ogrodje za Dry-Run.
    FAZA 30C: E-level mapping (opis stanja).
    """

    def __init__(self):
        pass

    def evaluate(self, execution_intent, context):
        payload = execution_intent.payload or {}

        authority_snapshot = None
        anchor_snapshot = None

        if "authority" in payload:
            authority_snapshot = context.resolve_authority(payload.get("authority"))

        if "anchor" in payload:
            anchor_snapshot = context.resolve_anchor(payload.get("anchor"))

        # --- FAZA 30B (osnova) ---
        if authority_snapshot is None:
            status = DryRunStatus.REFUSED
        elif anchor_snapshot is not None and anchor_snapshot.exists is False:
            status = DryRunStatus.INELIGIBLE
        else:
            status = DryRunStatus.UNKNOWN

        # --- FAZA 30C (opcijski E-level mapping) ---
        # Če je v payloadu že določen enforcement_level (read-only signal),
        # ga samo preslikamo v status.
        raw_level = payload.get("enforcement_level")
        mapped_from = None

        if raw_level is not None:
            try:
                level = EnforcementLevel(raw_level)
                status = EnforcementMapper.map(level)
                mapped_from = level.value
            except ValueError:
                # Neveljavna vrednost → brez spremembe statusa
                pass

        return DryRunResult(
            status=status,
            details={
                "authority": authority_snapshot.__dict__ if authority_snapshot else None,
                "anchor": anchor_snapshot.__dict__ if anchor_snapshot else None,
                "enforcement_level": mapped_from,
            }
        )
