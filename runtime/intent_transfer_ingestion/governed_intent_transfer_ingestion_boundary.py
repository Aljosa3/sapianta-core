"""Boundary declarations for governed intent transfer ingestion."""

INGESTION_BOUNDARY_STATEMENT = (
    "Governed transfer ingestion validates transfer admissibility but does not grant execution authority."
)


def ingestion_boundary_state() -> dict:
    return {
        "chatgpt_authority": False,
        "execution_authority": False,
        "authority_granted": False,
        "automatic_dispatch": False,
        "orchestration": False,
        "hidden_continuation": False,
        "preview_required": True,
        "confirmation_required": True,
        "ingestion_boundary_statement": INGESTION_BOUNDARY_STATEMENT,
    }
