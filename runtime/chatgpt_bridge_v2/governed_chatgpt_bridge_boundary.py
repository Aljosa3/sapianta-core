"""Constitutional boundary declarations for the conversational bridge."""

CONSTITUTIONAL_STATEMENT = "ChatGPT reasoning is non-authoritative and cannot directly trigger execution."


def bridge_boundary_state() -> dict:
    return {
        "chatgpt_authority": False,
        "execution_authority": False,
        "automatic_dispatch": False,
        "orchestration": False,
        "hidden_continuation": False,
        "constitutional_statement": CONSTITUTIONAL_STATEMENT,
    }
