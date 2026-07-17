"""Bounded Codex subprocess dispatch only."""

from __future__ import annotations

import subprocess
from collections.abc import Callable
from time import monotonic
from typing import Any

MAX_CAPTURE_CHARS = 4096


def _capture(value: str | bytes | None) -> tuple[str, int, int, bool]:
    raw = value or b""
    if isinstance(raw, bytes):
        byte_length = len(raw)
        text = raw.decode("utf-8", errors="replace")
    else:
        text = str(raw)
        byte_length = len(text.encode("utf-8"))
    return text[-MAX_CAPTURE_CHARS:], len(text), byte_length, len(text) > MAX_CAPTURE_CHARS


def _diagnostics(
    *,
    started_at: float,
    stdout: str | bytes | None,
    stderr: str | bytes | None,
    exception_type: str = "",
    exception_message: str = "",
) -> tuple[str, str, dict[str, Any]]:
    bounded_stdout, stdout_chars, stdout_bytes, stdout_truncated = _capture(stdout)
    bounded_stderr, stderr_chars, stderr_bytes, stderr_truncated = _capture(stderr)
    return bounded_stdout, bounded_stderr, {
        "duration_seconds": round(max(0.0, monotonic() - started_at), 6),
        "exception_type": exception_type,
        "exception_message": _capture(exception_message)[0],
        "stdout_character_length": stdout_chars,
        "stderr_character_length": stderr_chars,
        "stdout_byte_length": stdout_bytes,
        "stderr_byte_length": stderr_bytes,
        "stdout_truncated": stdout_truncated,
        "stderr_truncated": stderr_truncated,
    }


def dispatch_bounded_codex(
    *,
    command: tuple[str, ...],
    timeout_seconds: int,
    runner: Callable[..., Any] = subprocess.run,
) -> dict:
    started_at = monotonic()
    try:
        completed = runner(
            list(command),
            capture_output=True,
            text=True,
            shell=False,
            timeout=timeout_seconds,
        )
        stdout, stderr, diagnostics = _diagnostics(
            started_at=started_at,
            stdout=completed.stdout,
            stderr=completed.stderr,
        )
        return {
            "execution_status": "EXECUTION_ACCEPTED" if completed.returncode == 0 else "EXECUTION_FAILURE",
            "returncode": completed.returncode,
            "stdout": stdout,
            "stderr": stderr,
            "timed_out": False,
            "diagnostics": diagnostics,
            "metadata": {
                "args": list(command),
                "shell": False,
                "timeout_seconds": timeout_seconds,
                "capture_limit_chars": MAX_CAPTURE_CHARS,
            },
        }
    except subprocess.TimeoutExpired as exc:
        stdout, stderr, diagnostics = _diagnostics(
            started_at=started_at,
            stdout=exc.stdout,
            stderr=exc.stderr,
            exception_type=exc.__class__.__name__,
            exception_message="process exceeded the bounded execution timeout",
        )
        return {
            "execution_status": "EXECUTION_TIMEOUT",
            "returncode": 124,
            "stdout": stdout,
            "stderr": stderr,
            "timed_out": True,
            "diagnostics": diagnostics,
            "metadata": {
                "args": list(command),
                "shell": False,
                "timeout_seconds": timeout_seconds,
                "capture_limit_chars": MAX_CAPTURE_CHARS,
            },
        }
    except OSError as exc:
        stdout, stderr, diagnostics = _diagnostics(
            started_at=started_at,
            stdout="",
            stderr=exc.__class__.__name__,
            exception_type=exc.__class__.__name__,
            exception_message=exc.strerror or "operating system process-start failure",
        )
        return {
            "execution_status": "EXECUTION_FAILURE",
            "returncode": 125,
            "stdout": stdout,
            "stderr": stderr,
            "timed_out": False,
            "diagnostics": diagnostics,
            "metadata": {
                "args": list(command),
                "shell": False,
                "timeout_seconds": timeout_seconds,
                "capture_limit_chars": MAX_CAPTURE_CHARS,
            },
        }
