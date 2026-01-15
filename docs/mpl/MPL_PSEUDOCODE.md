FUNCTION MPL_EXECUTE(input_request):

    // ─────────────────────────────
    // SP-1: INPUT CANON CHECK
    // ─────────────────────────────
    decision_1 = CANON_EVALUATE_INPUT(input_request)

    IF decision_1 != ALLOW:
        LOG("SP-1 DENY", reason=decision_1.reason)
        RETURN HALT(reason="INPUT_CANON_VIOLATION")

    // ─────────────────────────────
    // SP-2: LLM CALL GATE
    // ─────────────────────────────
    decision_2 = CANON_EVALUATE_LLM_PERMISSION(input_request)

    IF decision_2 == DENY:
        LOG("SP-2 DENY", reason=decision_2.reason)
        RETURN HALT(reason="LLM_CALL_NOT_PERMITTED")

    IF decision_2 != ALLOW:
        LOG("SP-2 INVALID STATE")
        RETURN HARD_FAIL(reason="UNDEFINED_LLM_GATE_STATE")

    // ─────────────────────────────
    // LLM CALL (NO AUTHORITY)
    // ─────────────────────────────
    llm_response = CALL_LLM(input_request)

    IF llm_response == NULL:
        RETURN HARD_FAIL(reason="LLM_NO_RESPONSE")

    // ─────────────────────────────
    // SP-3: OUTPUT CANON CHECK
    // ─────────────────────────────
    decision_3 = CANON_EVALUATE_OUTPUT(llm_response)

    IF decision_3 != ALLOW:
        LOG("SP-3 DENY", reason=decision_3.reason)
        RETURN HALT(reason="OUTPUT_CANON_VIOLATION")

    // ─────────────────────────────
    // NO SILENT DEVIATION CHECK
    // ─────────────────────────────
    IF NOT ALL_DECISIONS_EXPLICIT(decision_1, decision_2, decision_3):
        LOG("SILENT DEVIATION DETECTED")
        RETURN HARD_FAIL(reason="SILENT_DEVIATION")

    // ─────────────────────────────
    // SUCCESSFUL COMPLETION
    // ─────────────────────────────
    LOG("MPL SUCCESS")
    RETURN OUTPUT(llm_response)
