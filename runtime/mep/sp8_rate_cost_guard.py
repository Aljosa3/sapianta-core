from time import time
from .context import ExecutionContext, Status

# Preprosta in deterministična in-memory evidenca
# (za SP-8 je to OK; kasneje se lahko zamenja z Redis / DB)
_RATE_STATE = {
    # source: {"window_start": ts, "requests": int, "tokens": int}
}

WINDOW_SECONDS = 60
MAX_REQUESTS_PER_WINDOW = 10
MAX_TOKENS_PER_WINDOW = 8_000
MAX_TOKENS_PER_REQUEST = 2_000


def _estimate_tokens(text: str) -> int:
    # Konzervativna ocena: ~4 znaki = 1 token
    if not text:
        return 0
    return max(1, len(text) // 4)


def sp8_rate_cost_guard(ctx: ExecutionContext) -> bool:
    """
    SP-8: Rate / Cost / Token Guard

    Zavrne izvajanje, če presega:
    - per-request token limit
    - per-window request limit
    - per-window token limit
    """

    now = time()
    source = ctx.source or "UNKNOWN"

    # 0️⃣ Cost budget check (NORMATIVE, fail-open if metadata missing)
    cost_estimate = ctx.metadata.get("cost_estimate")
    cost_limit = ctx.metadata.get("cost_limit")

    if cost_estimate is not None and cost_limit is not None:
        if cost_estimate > cost_limit:
            ctx.add_violation(
                f"SP-8 blocked: cost budget exceeded "
                f"({cost_estimate} > {cost_limit})"
            )
            ctx.finalize(
                status=Status.DENY,
                error="SP-8: cost budget exceeded"
            )
            return False

    est_tokens = _estimate_tokens(ctx.normalized_input)

    # 1️⃣ Per-request token limit
    if est_tokens > MAX_TOKENS_PER_REQUEST:
        ctx.add_violation(
            f"SP-8 blocked: per-request token limit exceeded "
            f"({est_tokens} > {MAX_TOKENS_PER_REQUEST})"
        )
        ctx.finalize(
            status=Status.DENY,
            error="SP-8: per-request token limit exceeded"
        )
        return False

    state = _RATE_STATE.get(source)

    # 2️⃣ Init ali reset okna
    if not state or (now - state["window_start"]) > WINDOW_SECONDS:
        _RATE_STATE[source] = {
            "window_start": now,
            "requests": 0,
            "tokens": 0,
        }
        state = _RATE_STATE[source]

    # 3️⃣ Per-window request limit
    if state["requests"] + 1 > MAX_REQUESTS_PER_WINDOW:
        ctx.add_violation(
            f"SP-8 blocked: request rate exceeded "
            f"({state['requests'] + 1} > {MAX_REQUESTS_PER_WINDOW})"
        )
        ctx.finalize(
            status=Status.DENY,
            error="SP-8: request rate exceeded"
        )
        return False

    # 4️⃣ Per-window token limit
    if state["tokens"] + est_tokens > MAX_TOKENS_PER_WINDOW:
        ctx.add_violation(
            f"SP-8 blocked: token budget exceeded "
            f"({state['tokens'] + est_tokens} > {MAX_TOKENS_PER_WINDOW})"
        )
        ctx.finalize(
            status=Status.DENY,
            error="SP-8: token budget exceeded"
        )
        return False

    # 5️⃣ Zabeleži porabo
    state["requests"] += 1
    state["tokens"] += est_tokens

    ctx.add_decision(
        f"SP-8 rate/cost guard passed "
        f"(req={state['requests']}, tokens={state['tokens']})"
    )
    return True
