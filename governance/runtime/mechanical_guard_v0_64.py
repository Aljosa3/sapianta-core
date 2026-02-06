"""
v0.64 — Mechanical Guard (Read-Only Enforcement Stub)

STATUS: INIT
PURPOSE:
- Hard DENY of execution and write paths
- No configuration
- No bypass
- No side-effects (except optional audit logging)

This guard is intentionally minimal and dumb.
"""

class MechanicalGuardDeny(Exception):
    pass


class MechanicalGuard:
    """
    Read-only mechanical guard.
    All operations are denied by default.
    """

    def __init__(self):
        # No configuration allowed
        pass

    def check_execution(self, *args, **kwargs):
        """
        Deny any execution attempt.
        """
        raise MechanicalGuardDeny("Execution denied by mechanical guard (v0.64)")

    def check_write(self, *args, **kwargs):
        """
        Deny any write attempt.
        """
        raise MechanicalGuardDeny("Write denied by mechanical guard (v0.64)")

    def check_self_build(self, *args, **kwargs):
        """
        Deny any self-build attempt.
        """
        raise MechanicalGuardDeny("Self-build denied by mechanical guard (v0.64)")

    def audit(self, message: str):
        """
        Optional read-only audit hook.
        Must not affect control flow.
        """
        try:
            # Intentionally minimal; replace with append-only logger if needed
            print(f"[MECHANICAL_GUARD_AUDIT] {message}")
        except Exception:
            # Swallow all errors to avoid side-effects
            pass


# Singleton-style access (optional, explicit)
GUARD = MechanicalGuard()
