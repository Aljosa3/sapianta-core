from runtime.mep.context import ExecutionContext, Status, Phase
from runtime.mep.sp8_rate_cost_guard import sp8_rate_cost_guard


def test_sp8_blocks_when_budget_exceeded():
    # 🔹 raw_input JE STRING (kanonično)
    ctx = ExecutionContext(
        source="test",
        raw_input="test prompt"
    )

    # simulacija faze po guardih
    ctx.phase = Phase.EXECUTION
    ctx.status = Status.ALLOW

    # UC-2 kontekst (STRUKTURIRANO)
    ctx.intent = "ask_llm"
    ctx.input_payload = {"prompt": "test"}

    # SP-8 podatki
    ctx.metadata["cost_estimate"] = 9999
    ctx.metadata["cost_limit"] = 10

    allowed = sp8_rate_cost_guard(ctx)

    assert allowed is False
    assert ctx.status == Status.DENY
