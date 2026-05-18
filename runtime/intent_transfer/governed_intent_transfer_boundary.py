"""Boundary declarations for inert governed intent transfer packages."""

TRANSFER_BOUNDARY_STATEMENT = (
    "This transfer package is non-executing and requires explicit governance preview and confirmation."
)


def transfer_boundary_state() -> dict:
    return {
        "chatgpt_authority": False,
        "execution_authority": False,
        "automatic_dispatch": False,
        "orchestration": False,
        "hidden_continuation": False,
        "preview_required": True,
        "confirmation_required": True,
        "transfer_boundary_statement": TRANSFER_BOUNDARY_STATEMENT,
    }
