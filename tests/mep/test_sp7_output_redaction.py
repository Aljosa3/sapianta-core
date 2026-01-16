from runtime.mep.context import ExecutionContext, Status
from runtime.mep.orchestrator import Orchestrator


def test_sp7_llm_output_is_structured_and_safe():
    """
    SP-7:
    - LLM output mora biti strukturiran dict
    - Ne sme vsebovati surovega API ključa
    - Ne sme vsebovati tracebacka ali exceptiona
    """

    ctx = ExecutionContext(
        source="chat",
        raw_input="Razloži razliko med odgovornostjo in avtoriteto."
    )

    orch = Orchestrator()
    result_ctx = orch.run(ctx)

    # 1. Normativni status
    assert result_ctx.status == Status.FINAL

    # 2. Rezultat obstaja
    assert result_ctx.result is not None
    assert isinstance(result_ctx.result, dict)

    # 3. Pričakovana struktura UC-2
    assert result_ctx.result.get("type") == "llm_proposed_answer"
    assert "content" in result_ctx.result
    assert isinstance(result_ctx.result["content"], str)

    # 4. SP-7: varnostni redaction check
    forbidden_markers = [
        "OPENAI_API_KEY",
        "sk-",
        "Traceback",
        "Exception",
    ]

    for marker in forbidden_markers:
        assert marker not in result_ctx.result["content"]
