from .unicode_map import UNICODE_REPLACEMENTS
from .errors import InvalidTextInputError


def normalize_text(text: str) -> str:
    """
    Deterministically normalize text:
    - validates input
    - normalizes unicode characters
    - collapses whitespace
    """
    if not isinstance(text, str):
        raise InvalidTextInputError("Input must be a string")

    normalized = text

    for source, target in UNICODE_REPLACEMENTS.items():
        normalized = normalized.replace(source, target)

    # Normalize whitespace
    normalized = normalized.replace("\r\n", "\n")
    normalized = normalized.replace("\r", "\n")

    lines = []
    for line in normalized.split("\n"):
        collapsed = " ".join(line.split())
        lines.append(collapsed)

    return "\n".join(lines).strip()
