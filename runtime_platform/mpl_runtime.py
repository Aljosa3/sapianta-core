# runtime/mpl_runtime.py
# Status: MPL ONLY · NOT FOR EXTENSION
# Vezano na: F47_LOCK

from enum import Enum


class Decision(Enum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    HALT = "HALT"
    HARD_FAIL = "HARD_FAIL"


# ─────────────────────────────
# CANON EVALUATION STUBS
# (NO LOGIC, ONLY CONTRACT)
# ─────────────────────────────

def canon_evaluate_input(request):
    """
    Must return Decision.ALLOW or Decision.DENY
    """
    raise NotImplementedError("Canon input evaluation not implemented")


def canon_evaluate_llm_permission(request):
    """
    Must return Decision.ALLOW or Decision.DENY
    """
    raise NotImplementedError("Canon LLM permission not implemented")


def canon_evaluate_output(llm_output):
    """
    Must return Decision.ALLOW or Decision.DENY
    """
    raise NotImplementedError("Canon output evaluation not implemented")


# ─────────────────────────────
# LLM CALL (NO AUTHORITY)
# ─────────────────────────────

def call_llm(request):
    """
    Must return raw LLM output.
    No retries. No fallback.
    """
    raise NotImplementedError("LLM call not implemented")


# ─────────────────────────────
# MPL EXECUTION LOOP
# ─────────────────────────────

def mpl_execute(request):
    # SP-1: INPUT CHECK
    decision_1 = canon_evaluate_input(request)

    if decision_1 != Decision.ALLOW:
        return Decision.HALT, "INPUT_CANON_VIOLATION"

    # SP-2: LLM GATE
    decision_2 = canon_evaluate_llm_permission(request)

    if decision_2 != Decision.ALLOW:
        return Decision.HALT, "LLM_CALL_NOT_PERMITTED"

    # LLM CALL
    llm_output = call_llm(request)

    if llm_output is None:
        return Decision.HARD_FAIL, "LLM_NO_RESPONSE"

    # SP-3: OUTPUT CHECK
    decision_3 = canon_evaluate_output(llm_output)

    if decision_3 != Decision.ALLOW:
        return Decision.HALT, "OUTPUT_CANON_VIOLATION"

    # NO SILENT DEVIATION
    if None in (decision_1, decision_2, decision_3):
        return Decision.HARD_FAIL, "SILENT_DEVIATION"

    return Decision.ALLOW, llm_output
