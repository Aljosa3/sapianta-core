from ..core.hashing import artifact_hash

def build_global_authority_policy():
    base = {
        "artifact_type": "AUTHORITY_POLICY",
        "artifact_version": "1.0",
        "payload": {
            "policy_scope": "GLOBAL",
            "policy_id": "AUTH_BASELINE_v0.1",
            "roles": ["RO", "ANL", "EXE", "AUD"],
            "permissions": {
                "create_proposal": ["RO"],
                "submit_proposal": ["RO"],
                "issue_decision": ["EXE"],
                "override_decision": ["EXE"],
                "replay": ["AUD"]
            }
        }
    }
    base["hash"] = artifact_hash(base)
    return base
