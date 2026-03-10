"""
SAPIANTA Runtime Orchestrator

Executes the autonomous decision loop.
"""

import time

from runtime.strategies.strategy_executor import generate_proposal
from runtime.engine.decision_spine import run_decision_pipeline

from runtime.signals.runtime_signal_manager import (
    check_runtime_signals,
    wait_if_paused,
    clear_reload_signal
)

from runtime.safety.runtime_risk_guard import evaluate_runtime_risk


def run_runtime_loop(interval_seconds: int = 10):
    """
    Runs the autonomous decision loop.
    """

    print("SAPIANTA runtime loop started")

    while True:

        # --- Risk guard check ---
        if not evaluate_runtime_risk():
            print("Runtime stopped by risk guard")
            break

        # --- Runtime signal handling ---
        state = check_runtime_signals()

        if state == "STOP":
            print("Runtime stop signal detected")
            break

        if state == "PAUSE":
            wait_if_paused()
            continue

        if state == "RELOAD":
            print("Reload strategies signal detected")
            clear_reload_signal()

        try:

            proposal = generate_proposal()

            if proposal is None:
                print("No strategy available")
                time.sleep(interval_seconds)
                continue

            decision = run_decision_pipeline(proposal)

            print("Decision executed:", decision["decision_id"])

        except Exception as e:

            print("Runtime error:", e)

        time.sleep(interval_seconds)