from ..core.hashing import artifact_hash
from ..domain_credit.rules import compute_dti, risk_band, recommendation

def build_advisory(proposal):
    income = proposal["payload"]["income_monthly"]
    debt = proposal["payload"]["existing_debt_monthly"]
    dti = compute_dti(income, debt)
    base = {
        "artifact_type": "ADVISORY",
        "artifact_version": "1.0",
        "payload": {
            "proposal_hash": proposal["hash"],
            "dti": dti,
            "risk_band": risk_band(dti),
            "recommendation": recommendation(dti)
        }
    }
    base["hash"] = artifact_hash(base)
    return base
