# runtime/use_cases/uc2_llm_controlled_answer.py

from runtime.mep.context import ExecutionContext, Status
from runtime.llm.openai_adapter import generate_answer, LLMAdapterError


def execute_uc2(ctx: ExecutionContext) -> dict:
    """
    UC-2: Controlled LLM Answer

    LLM:
      - predlaga besedilo
      - nima normativne moči

    Sistem:
      - odloča, ali je izhod sploh sprejemljiv
    """

    prompt = ctx.normalized_input

    try:
        answer = generate_answer(prompt)

    except LLMAdapterError as e:
        ctx.add_violation(f"LLM adapter error: {str(e)}")
        ctx.finalize(
            status=Status.HARD_FAIL,
            error="LLM adapter failure"
        )
        return None

    except Exception as e:
        ctx.add_violation(f"Unexpected LLM error: {str(e)}")
        ctx.finalize(
            status=Status.HARD_FAIL,
            error="Unexpected LLM failure"
        )
        return None

    # 🔒 Strukturiran rezultat (ne golo besedilo)
    return {
        "type": "llm_proposed_answer",
        "model": "openai",
        "content": answer
    }
