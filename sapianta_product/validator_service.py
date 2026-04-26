# validator_service.py

import os
import uuid
import subprocess
import json
import hashlib
from datetime import datetime

from runtime.development.architecture_guardian import ArchitectureGuardian

# ✅ NEW (minimal extension)
from sapianta_product.crypto import sign_hash

# --------------------------------------------------
# BASE PATH
# --------------------------------------------------

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

TEST_TIMEOUT = 30

AUDIT_DIR = os.path.abspath(
    os.path.join(PROJECT_ROOT, "runtime", "audit_logs")
)


# --------------------------------------------------
# UTILS
# --------------------------------------------------

def generate_id():
    return f"val_{uuid.uuid4().hex[:8]}"


def create_execution_dir(validation_id: str):
    execution_dir = os.path.join(
        PROJECT_ROOT,
        "runtime",
        "development",
        "generated",
        validation_id
    )

    if os.path.exists(execution_dir):
        raise RuntimeError(f"Execution directory already exists: {execution_dir}")

    os.makedirs(execution_dir)
    return execution_dir


def write_files(execution_dir: str, code: str, tests: str):
    module_file = os.path.join(execution_dir, "ai_firewall_module.py")
    test_file = os.path.join(execution_dir, "test_ai_firewall_module.py")

    with open(module_file, "w") as f:
        f.write(code)

    with open(test_file, "w") as f:
        f.write(tests)

    return module_file, test_file


# --------------------------------------------------
# HASH (CRITICAL)
# --------------------------------------------------

def compute_hash(payload: dict) -> str:
    """
    IMPORTANT:
    - deterministic JSON
    - NO sha256 field inside payload
    """
    canonical = json.dumps(
        payload,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":")
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


# --------------------------------------------------
# AUDIT SAVE (IMMUTABLE)
# --------------------------------------------------

def save_audit(
    validation_id: str,
    code: str,
    tests: str,
    status: str,
    stage: str,
    reason: str,
    execution_dir: str,
    stdout: str = "",
    stderr: str = "",
    return_code=None,
    guardian_result=None,
):
    os.makedirs(AUDIT_DIR, exist_ok=True)

    # 🔒 payload WITHOUT hash (important)
    audit_payload = {
        "id": validation_id,
        "status": status,
        "stage": stage,
        "reason": reason,
        "code": code,
        "tests": tests,
        "stdout": stdout,
        "stderr": stderr,
        "return_code": return_code,
        "guardian_result": guardian_result,
        "execution_dir": execution_dir,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }

    # 🔐 compute hash
    audit_hash = compute_hash(audit_payload)

    # ✅ NEW — SIGNATURE (minimal extension)
    signature = sign_hash(audit_hash)

    # final data (hash appended AFTER computation)
    audit_payload["sha256"] = audit_hash
    audit_payload["signature"] = signature

    file_path = os.path.join(AUDIT_DIR, f"{validation_id}.json")

    # 🔒 IMMUTABILITY (critical)
    if os.path.exists(file_path):
        raise RuntimeError(f"Audit file already exists: {file_path}")

    with open(file_path, "x") as f:
        json.dump(audit_payload, f, indent=2, ensure_ascii=False)

    # ✅ UPDATED RETURN
    return audit_hash, signature


# --------------------------------------------------
# MAIN VALIDATOR
# --------------------------------------------------

def validate_code(code: str, tests: str):
    validation_id = generate_id()

    execution_dir = create_execution_dir(validation_id)
    module_file, test_file = write_files(execution_dir, code, tests)

    # -------------------
    # M1 — ARCHITECTURE GUARDIAN
    # -------------------
    guardian = ArchitectureGuardian()
    guardian_result = guardian.validate(module_file, code)

    if not guardian_result.get("success", False):
        reason = guardian_result.get("error", "guardian validation failed")

        audit_hash, signature = save_audit(
            validation_id=validation_id,
            code=code,
            tests=tests,
            status="REJECTED",
            stage="M1",
            reason=reason,
            execution_dir=execution_dir,
            guardian_result=guardian_result,
        )

        return {
            "status": "REJECTED",
            "stage": "M1",
            "reason": reason,
            "id": validation_id,
            "sha256": audit_hash,
            "signature": signature,  # ✅ NEW
        }

    # -------------------
    # M3 — TEST EXECUTION
    # -------------------
    try:
        result = subprocess.run(
            ["pytest", "-q"],
            cwd=execution_dir,
            capture_output=True,
            text=True,
            timeout=TEST_TIMEOUT
        )

        stdout = result.stdout
        stderr = result.stderr
        return_code = result.returncode

        if return_code != 0:
            reason = "test execution failed"

            audit_hash, signature = save_audit(
                validation_id=validation_id,
                code=code,
                tests=tests,
                status="REJECTED",
                stage="M3",
                reason=reason,
                execution_dir=execution_dir,
                stdout=stdout,
                stderr=stderr,
                return_code=return_code,
                guardian_result=guardian_result,
            )

            return {
                "status": "REJECTED",
                "stage": "M3",
                "reason": reason,
                "details": {
                    "stdout": stdout,
                    "stderr": stderr,
                    "return_code": return_code,
                },
                "id": validation_id,
                "sha256": audit_hash,
                "signature": signature,  # ✅ NEW
            }

    except Exception as e:
        reason = "execution error"

        audit_hash, signature = save_audit(
            validation_id=validation_id,
            code=code,
            tests=tests,
            status="REJECTED",
            stage="M3",
            reason=reason,
            execution_dir=execution_dir,
            stderr=str(e),
            return_code=None,
            guardian_result=guardian_result,
        )

        return {
            "status": "REJECTED",
            "stage": "M3",
            "reason": reason,
            "details": str(e),
            "id": validation_id,
            "sha256": audit_hash,
            "signature": signature,  # ✅ NEW
        }

    # -------------------
    # SUCCESS
    # -------------------
    reason = "all checks passed"

    audit_hash, signature = save_audit(
        validation_id=validation_id,
        code=code,
        tests=tests,
        status="CERTIFIED",
        stage="M3",
        reason=reason,
        execution_dir=execution_dir,
        stdout=stdout,
        stderr=stderr,
        return_code=return_code,
        guardian_result=guardian_result,
    )

    return {
        "status": "CERTIFIED",
        "stage": "M3",
        "reason": reason,
        "id": validation_id,
        "sha256": audit_hash,
        "signature": signature,  # ✅ NEW
    }