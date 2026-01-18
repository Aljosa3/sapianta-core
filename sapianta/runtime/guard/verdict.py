"""
Verdict placeholder for SAPIANTA — RUNTIME_GUARD_INIT.

A Verdict represents the outcome of a guard evaluation.
In this phase, it carries no meaning and no decision.
"""


class Verdict:
    def __init__(self):
        # No attributes, no meaning
        pass

    def __repr__(self):
        return "<Verdict (empty)>"
