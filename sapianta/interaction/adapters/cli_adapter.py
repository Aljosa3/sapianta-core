from sapianta.governance.interface.interface import GovernanceInterface
from sapianta.governance.interface.types import GovernanceRequest


def handle_cli_input(user_input: str):
    request = GovernanceRequest(
        request_type="CLI",
        raw_input=user_input
    )

    return GovernanceInterface.handle(request)
