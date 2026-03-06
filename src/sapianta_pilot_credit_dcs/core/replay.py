from ..artifacts.advisory import build_advisory
from ..core.authority import validate_action

def replay_advisory(proposal):
    return build_advisory(proposal)

def replay_authority(decision, authority_policy):
    role = decision["payload"]["signature"]["role"]
    validate_action(authority_policy, role, "issue_decision")
    if decision["payload"]["human_override"]:
        validate_action(authority_policy, role, "override_decision")
    return True
