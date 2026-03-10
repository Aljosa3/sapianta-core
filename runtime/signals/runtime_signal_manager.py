"""
SAPIANTA Runtime Signal Manager

Handles runtime control signals.
"""

import os
import time


SIGNAL_DIR = "runtime/signals"

STOP_SIGNAL = "STOP"
PAUSE_SIGNAL = "PAUSE"
RELOAD_SIGNAL = "RELOAD_STRATEGIES"


def _signal_path(name: str) -> str:
    return os.path.join(SIGNAL_DIR, name)


def check_runtime_signals() -> str:
    """
    Returns runtime state based on signal files.
    """

    if os.path.exists(_signal_path(STOP_SIGNAL)):
        return "STOP"

    if os.path.exists(_signal_path(PAUSE_SIGNAL)):
        return "PAUSE"

    if os.path.exists(_signal_path(RELOAD_SIGNAL)):
        return "RELOAD"

    return "RUN"


def wait_if_paused():
    """
    Blocks execution while PAUSE signal exists.
    """

    while os.path.exists(_signal_path(PAUSE_SIGNAL)):
        print("Runtime paused...")
        time.sleep(2)


def clear_reload_signal():
    """
    Removes reload signal after processing.
    """

    path = _signal_path(RELOAD_SIGNAL)

    if os.path.exists(path):
        os.remove(path)