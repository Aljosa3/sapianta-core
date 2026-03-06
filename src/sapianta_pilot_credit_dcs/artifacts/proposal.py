from ..core.hashing import artifact_hash

def build_proposal(income, debt, state="DRAFT"):
    base = {
        "artifact_type": "PROPOSAL",
        "artifact_version": "1.0",
        "state": state,
        "payload": {
            "income_monthly": float(income),
            "existing_debt_monthly": float(debt),
        }
    }
    base["hash"] = artifact_hash(base)
    return base

def submit_proposal(draft):
    if draft["state"] != "DRAFT":
        raise ValueError("Only DRAFT can be submitted.")
    p = dict(draft)
    p["state"] = "SUBMITTED"
    p.pop("hash", None)
    from ..core.hashing import artifact_hash
    p["hash"] = artifact_hash(p)
    return p
