from typing import Dict, Any, List


def _lower_text(payload: Dict[str, Any]) -> str:
    return (
        str(payload.get("code", "")) +
        str(payload.get("text", ""))
    ).lower()


def _get_capital(payload: Dict[str, Any]):
    """
    Extract capital_ratio from:
    1) direct payload field
    2) regex parsing from code/text (ROBUST)
    """

    # 1️⃣ direct
    try:
        direct = payload.get("capital_ratio", None)
        if direct is not None:
            return float(direct)
    except Exception:
        pass

    # 2️⃣ regex (🔥 GLAVNI FIX)
    try:
        import re

        text = (
            str(payload.get("code", "")) +
            str(payload.get("text", ""))
        )

        match = re.search(r"capital_ratio[^0-9]*(\d+)", text)
        if match:
            value = float(match.group(1))

            # 🔥 NORMALIZACIJA (20 → 0.20)
            if value > 1:
                value = value / 100.0

            return value

    except Exception:
        pass

    return None


# --------------------------------------------------
# POLICY CHECKS
# --------------------------------------------------

def check_capital(payload):
    capital = _get_capital(payload)
    text = _lower_text(payload)

    # 🔍 DEBUG (lahko odstraniš kasneje)
    print("DEBUG CAPITAL:", capital)

    # 🔥 če imamo capital_ratio → vedno validiraj
    if capital is not None:
        if capital < 0.30:
            return {
                "status": "FAIL",
                "reason": "Capital adequacy below 30%.",
                "risk": "Decision violates lending policy.",
                "severity": "HIGH",
                "evidence": f"capital_ratio={capital}"
            }
        return {"status": "PASS"}

    # fallback
    if (
        "loan" not in text and
        "kredit" not in text and
        "capital_ratio" not in text
    ):
        return {"status": "PASS"}

    return {
        "status": "FAIL",
        "reason": "Missing capital_ratio.",
        "risk": "Decision may approve credit without risk data.",
        "severity": "HIGH",
        "evidence": "capital_ratio missing"
    }


def check_explanation(payload):
    text = _lower_text(payload)

    if any(x in text for x in ["because", "reason", "ker", "razlog"]):
        return {"status": "PASS"}

    return {
        "status": "FAIL",
        "reason": "No explanation provided.",
        "risk": "Decision is not transparent.",
        "severity": "MEDIUM",
        "evidence": "missing explanation"
    }


def check_risk(payload):
    text = _lower_text(payload)

    if any(x in text for x in ["risk", "tveganje"]):
        return {"status": "PASS"}

    return {
        "status": "FAIL",
        "reason": "No risk disclosure.",
        "risk": "User may not understand consequences.",
        "severity": "MEDIUM",
        "evidence": "missing risk statement"
    }


POLICIES = [
    ("M2_CAPITAL", check_capital),
    ("M2_EXPLANATION", check_explanation),
    ("M2_RISK", check_risk),
]


# --------------------------------------------------
# MAIN ENTRY
# --------------------------------------------------

def validate_policy(payload: Dict[str, Any]):

    controls = []
    failed = []

    for name, fn in POLICIES:
        try:
            result = fn(payload)
        except Exception as e:
            result = {
                "status": "FAIL",
                "reason": "Policy execution failed.",
                "risk": "Policy layer failure.",
                "severity": "HIGH",
                "evidence": str(e)
            }

        if result["status"] == "FAIL":
            failed.append(result)

        controls.append({
            "rule": name,
            "enforced_by": "M2_POLICY",
            "status": result["status"],
            "evidence": result.get("evidence")
        })

    # --------------------------------------------------
    # 🔥 MULTI-VIOLATION SUPPORT (MINIMAL PATCH)
    # --------------------------------------------------
    if failed:
        top = failed[0]

        # 🔥 collect ALL violations
        violations = [f.get("reason") for f in failed if f.get("reason")]

        return {
            "status": "REJECTED",
            "stage": "M2",
            "reason": top["reason"],  # backward compatibility
            "violations": violations,  # 🔥 NEW
            "risk": top["risk"],
            "severity": top["severity"],
            "controls": controls,
            "eu_ai_act": {
                "compliant": False
            }
        }

    return {
        "status": "PASSED",
        "stage": "M2",
        "controls": controls,
        "eu_ai_act": {
            "compliant": True
        }
    }