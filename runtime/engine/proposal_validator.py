"""
SAPIANTA Proposal Validator
Validates proposal artifacts against basic structural requirements.
"""

REQUIRED_FIELDS = [
    "proposal_id",
    "domain_id",
    "timestamp",
    "action",
    "risk_context"
]


def validate_proposal(proposal: dict) -> None:
    """
    Validates proposal structure.

    Raises ValueError if proposal is invalid.
    """

    if not isinstance(proposal, dict):
        raise ValueError("Proposal must be a dictionary")

    for field in REQUIRED_FIELDS:
        if field not in proposal:
            raise ValueError(f"Missing required proposal field: {field}")

    if "type" not in proposal["action"]:
        raise ValueError("Action must include 'type'")