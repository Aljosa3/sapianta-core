"""
AUDIT TRACE — IMPLEMENTATION HOOK

This hook provides a passive, read-only audit append mechanism.
It is intentionally NO-OP by default and MUST NOT influence runtime behavior.

Design guarantees:
- Audit is optional and disabled by default
- Audit never blocks, alters, or decides execution flow
- Failures in audit are swallowed (best-effort)
- Append-only semantics (no mutation, no deletion)
- No storage technology decision (simulated append only)
"""

from typing import Dict, Any, List, Optional
import threading
import time


class AuditHook:
    """
    Passive audit hook.

    Usage:
        audit = AuditHook(enabled=False)
        audit.emit({
            "event_type": "...",
            "origin": "...",
            "payload_ref": "..."
        })
    """

    REQUIRED_FIELDS = {"event_type", "origin", "payload_ref"}

    def __init__(self, enabled: bool = False) -> None:
        self.enabled: bool = enabled

        # In-memory append-only buffer (simulation only)
        self._buffer: List[Dict[str, Any]] = []

        # Thread-safety without behavioral guarantees
        self._lock = threading.Lock()

    def emit(self, event: Dict[str, Any]) -> None:
        """
        Receive an audit event.

        Behavior:
        - If audit is disabled → immediate return
        - Validate minimal structure
        - Append event snapshot (best-effort)
        - Never raise outward exceptions
        """
        if not self.enabled:
            return

        try:
            if not self._is_valid_event(event):
                return

            record = self._prepare_record(event)

            with self._lock:
                self._buffer.append(record)

            # Simulated append side-effect (visible but non-binding)
            print(f"[AUDIT] appended event: {record['event_type']}")

        except Exception:
            # Absolute rule: audit must never interfere with runtime
            return

    def _is_valid_event(self, event: Dict[str, Any]) -> bool:
        """
        Minimal structural validation only.
        No semantic interpretation.
        """
        if not isinstance(event, dict):
            return False

        missing = self.REQUIRED_FIELDS - event.keys()
        if missing:
            return False

        return True

    def _prepare_record(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create an immutable snapshot for append-only storage.
        """
        return {
            "timestamp": time.time(),
            "event_type": event.get("event_type"),
            "origin": event.get("origin"),
            "payload_ref": event.get("payload_ref"),
            "meta": event.get("meta", None),
        }

    def snapshot(self) -> List[Dict[str, Any]]:
        """
        Read-only snapshot of current audit buffer.
        Intended strictly for debugging or inspection.
        """
        with self._lock:
            return list(self._buffer)
