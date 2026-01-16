# runtime/mep/sp7_output_redaction.py

from runtime.mep.context import ExecutionContext


MAX_OUTPUT_LENGTH = 800  # znakov


def sp7_output_redaction(ctx: ExecutionContext) -> bool:
    """
    SP-7: Output Redaction / Safety Pass

    - ne spreminja normativnega statusa
    - ne blokira executiona
    - samo preoblikuje izhod (če je potrebno)
    """

    if not isinstance(ctx.result, dict):
        # Ni strukturiran izhod – SP-7 se preskoči
        return True

    content = ctx.result.get("content")
    if not isinstance(content, str):
        return True

    redacted = content

    # 1. Omejitev dolžine
    if len(redacted) > MAX_OUTPUT_LENGTH:
        redacted = redacted[:MAX_OUTPUT_LENGTH].rstrip() + "…"
        ctx.add_decision("SP-7 applied: output truncated")

    # 2. Osnovna zaščita (primer: ključne besede)
    banned_phrases = [
        "geslo",
        "password",
        "api ključ",
        "secret key"
    ]

    for phrase in banned_phrases:
        if phrase.lower() in redacted.lower():
            redacted = "[IZHOD SKRIT – VSEBINA NI VARNA ZA PRIKAZ]"
            ctx.add_decision("SP-7 applied: sensitive content redacted")
            break

    ctx.result["content"] = redacted
    return True
