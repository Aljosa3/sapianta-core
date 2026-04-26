# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import json

from sapianta_product.validator_service import validate_code, compute_hash

# ✅ NEW (minimal extension)
from sapianta_product.crypto import verify_signature

app = FastAPI(
    title="SAPIANTA AI Firewall",
    version="0.1"
)

# --------------------------------------------------
# PATH
# --------------------------------------------------

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

AUDIT_DIR = os.path.join(
    PROJECT_ROOT,
    "runtime",
    "audit_logs"
)

# --------------------------------------------------
# REQUEST MODELS
# --------------------------------------------------

class FirewallInput(BaseModel):
    code: str
    tests: str


class VerifyInput(BaseModel):
    id: str
    sha256: str


# ✅ NEW (minimal extension)
class VerifySignatureInput(BaseModel):
    id: str
    sha256: str
    signature: str


# --------------------------------------------------
# VALIDATE ENDPOINT
# --------------------------------------------------

@app.post("/firewall/validate")
def firewall_validate(input_data: FirewallInput):
    try:
        return validate_code(input_data.code, input_data.tests)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --------------------------------------------------
# AUDIT ENDPOINT
# --------------------------------------------------

@app.get("/firewall/audit/{validation_id}")
def get_audit(validation_id: str):
    audit_path = os.path.join(AUDIT_DIR, f"{validation_id}.json")

    if not os.path.exists(audit_path):
        raise HTTPException(status_code=404, detail="Audit not found")

    with open(audit_path, "r") as f:
        return json.load(f)


# --------------------------------------------------
# 🔐 VERIFY ENDPOINT (OBSTOJEČ — NE SPREMINJAJ)
# --------------------------------------------------

@app.post("/firewall/verify")
def verify_execution(input_data: VerifyInput):
    audit_path = os.path.join(AUDIT_DIR, f"{input_data.id}.json")

    if not os.path.exists(audit_path):
        raise HTTPException(status_code=404, detail="Audit not found")

    with open(audit_path, "r") as f:
        audit_data = json.load(f)

    # vzemi hash iz datoteke
    stored_hash = audit_data.pop("sha256", None)

    if stored_hash is None:
        return {
            "valid": False,
            "reason": "missing hash in audit"
        }

    # ponovno izračunaj hash
    recomputed_hash = compute_hash(audit_data)

    is_valid = (recomputed_hash == input_data.sha256)

    return {
        "valid": is_valid,
        "expected": stored_hash,
        "provided": input_data.sha256
    }


# --------------------------------------------------
# 🔐 VERIFY SIGNATURE ENDPOINT (NOVO)
# --------------------------------------------------

@app.post("/firewall/verify_signature")
def verify_signature_endpoint(input_data: VerifySignatureInput):
    audit_path = os.path.join(AUDIT_DIR, f"{input_data.id}.json")

    if not os.path.exists(audit_path):
        raise HTTPException(status_code=404, detail="Audit not found")

    with open(audit_path, "r") as f:
        audit_data = json.load(f)

    # odstranimo polja, ki ne sodijo v hash
    stored_hash = audit_data.pop("sha256", None)
    stored_signature = audit_data.pop("signature", None)

    if stored_hash is None:
        return {
            "hash_valid": False,
            "signature_valid": False,
            "reason": "missing hash in audit"
        }

    # ponovno izračunaj hash
    recomputed_hash = compute_hash(audit_data)

    hash_valid = (recomputed_hash == input_data.sha256)

    # preveri podpis
    signature_valid = verify_signature(
        input_data.sha256,
        input_data.signature
    )

    return {
        "hash_valid": hash_valid,
        "signature_valid": signature_valid
    }