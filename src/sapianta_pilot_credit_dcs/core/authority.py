def validate_action(policy, role, action):
    if role not in policy["payload"]["roles"]:
        raise ValueError("Role not defined in policy.")
    allowed = policy["payload"]["permissions"].get(action, [])
    if role not in allowed:
        raise ValueError(f"Role '{role}' not allowed to perform '{action}'.")
    return True
