"""
SAPIANTA Policy Engine
Evaluates governance policies for proposals.
"""

def evaluate_policy(proposal: dict) -> dict:
    """
    Minimal placeholder policy evaluation.
    """

    policy_trace = []

    # Example policy
    quantity = proposal.get("action", {}).get("quantity", 0)

    if quantity and quantity > 1000:
        policy_trace.append({
            "policy_module": "max_quantity_limit",
            "result": "FAIL"
        })

        return {
            "decision": "REJECTED",
            "policy_trace": policy_trace
        }

    policy_trace.append({
        "policy_module": "max_quantity_limit",
        "result": "PASS"
    })

    return {
        "decision": "APPROVED",
        "policy_trace": policy_trace
    }