class SkeletonModule:
    """
    Gold-standard reference module.

    This module exists to validate:
    - Module Contract boundaries
    - Guard chain integrity
    - Runtime invocation semantics

    It contains NO business logic.
    """

    MODULE_ID = "module.skeleton"
    VERSION = "1.0.0"

    def __init__(self, config=None):
        self.config = config or {}

    def run(self, intent, context):
        """
        Allowed:
        - Read intent (read-only)
        - Read context (read-only)

        Forbidden (by Module Contract):
        - Decision
        - Execution
        - Jurisdiction checks
        - Audit writes
        - Explain generation
        """

        # Minimal evaluation signal (non-binding)
        return {
            "module_id": self.MODULE_ID,
            "version": self.VERSION,
            "signal": "noop",
            "confidence": 0.0,
        }
