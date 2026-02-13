"""
HOI Runtime Stop Conditions — Silence as Success

This file defines when the HOI runtime MUST stop asking questions
and enter a silent state.

There is intentionally:
- no logic
- no thresholds calculated at runtime
- no heuristics
- no learning

Silence is a valid and successful runtime outcome.
"""

# -------------------------------------------------------------------
# STOP CONDITIONS (NORMATIVE)
# -------------------------------------------------------------------

STOP_CONDITIONS = {
    # Clarity no longer increases
    "clarity_plateau",          # additional questions do not improve understanding

    # Honest and stable uncertainty
    "stable_uncertainty",       # user explicitly remains unsure without avoidance

    # Attention constraints
    "attention_budget_exhausted",  # too many consecutive orientation questions

    # No irreversible risk present
    "no_irreversible_risk",     # no decision would cause permanent change

    # Explicit user pause
    "user_requests_pause",     # user asks to stop, pause, or reflect

    # Circular clarification
    "repetition_without_progress", # same uncertainty restated without gain
}

# -------------------------------------------------------------------
# SILENCE REQUIREMENTS
# -------------------------------------------------------------------

SILENCE_REQUIREMENTS = {
    # What HOI MUST do when stopping
    "explicitly_state_stop",        # clearly say that questioning is stopping
    "confirm_no_decisions_made",    # state that no decisions were taken
    "preserve_reentry",             # allow return to HOI at any time

    # What HOI MUST NOT do when stopping
    "no_final_push",                # no last attempt to extract an answer
    "no_summary_as_decision",       # summary must not imply closure
    "no_forward_motion",            # no progression toward execution
}

# -------------------------------------------------------------------
# GUARANTEES
# -------------------------------------------------------------------

# When HOI enters silence:
# - responsibility remains fully with the human
# - all paths remain considered reversible
# - no implicit consent is assumed
# - silence is not treated as failure

# Silence exists to protect attention, not to block progress.
