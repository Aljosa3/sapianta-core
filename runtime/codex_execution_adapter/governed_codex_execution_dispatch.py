"""Bounded Codex subprocess dispatch only."""

from __future__ import annotations

import subprocess
from collections.abc import Callable
from typing import Any

MAX_CAPTURE_CHARS = 4096


def _bounded(value: str) -> str:
    return value[-MAX_CAPTURE_CHARS:]


def dispatch_bounded_codex(
    *,
    command: tuple[str, ...],
    timeout_seconds: int,
    runner: Callable[..., Any] = subprocess.run,
) -> dict:
    try:
        completed = runner(
            list(command),
            capture_output=True,
            text=True,
            shell=False,
            timeout=timeout_seconds,
        )
        return {
            "execution_status": "EXECUTION_ACCEPTED" if completed.returncode == 0 else "EXECUTION_FAILURE",
            "returncode": completed.returncode,
            "stdout": _bounded(completed.stdout or ""),
            "stderr": _bounded(completed.stderr or ""),
            "timed_out": False,
            "metadata": {
                "args": list(command),
                "shell": False,
                "timeout_seconds": timeout_seconds,
                "capture_limit_chars": MAX_CAPTURE_CHARS,
            },
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "execution_status": "EXECUTION_TIMEOUT",
            "returncode": 124,
            "stdout": _bounded(exc.stdout or ""),
            "stderr": _bounded(exc.stderr or ""),
            "timed_out": True,
            "metadata": {
                "args": list(command),
                "shell": False,
                "timeout_seconds": timeout_seconds,
                "capture_limit_chars": MAX_CAPTURE_CHARS,
            },
        }
    except OSError as exc:
        return {
            "execution_status": "EXECUTION_FAILURE",
            "returncode": 125,
            "stdout": "",
            "stderr": exc.__class__.__name__,
            "timed_out": False,
            "metadata": {
                "args": list(command),
                "shell": False,
                "timeout_seconds": timeout_seconds,
                "capture_limit_chars": MAX_CAPTURE_CHARS,
            },
        }
