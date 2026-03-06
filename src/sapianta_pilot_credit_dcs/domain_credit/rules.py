from decimal import Decimal
from ..core.canonical import decimal_to_float_fixed

def compute_dti(income, debt):
    if income <= 0:
        raise ValueError("Income must be > 0.")
    dti = Decimal(str(debt)) / Decimal(str(income))
    return decimal_to_float_fixed(dti)

def risk_band(dti):
    if dti < 0.30:
        return "LOW"
    if dti <= 0.45:
        return "MEDIUM"
    return "HIGH"

def recommendation(dti):
    return "APPROVE" if dti < 0.40 else "REJECT"
