# validator_service.py

import os
import uuid
import subprocess
import json
import hashlib
from datetime import datetime

from runtime.development.architecture_guardian import ArchitectureGuardian
from sapianta_product.crypto import sign_hash

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

TEST_TIMEOUT = 30

AUDIT_DIR = os.path.abspath(
    os.path.join(PROJECT_ROOT, "runtime", "audit_logs")
)


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
# NEW: TEST EVIDENCE EXTRACTION
# --------------------------------------------------

def extract_test_evidence(stdout: str) -> str:
    if not stdout:
        return ""

    lines = stdout.splitlines()

    for i, line in enumerate(lines):
        if "assert" in line:
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            return f"{line.strip()} | {next_line.strip()}"

    return "test failed (no detailed assertion found)"


# --------------------------------------------------
# CONTROL LAYER (PROOF OF CONTROL)
# --------------------------------------------------

def build_controls(guardian_passed: bool, test_passed=None, test_stdout: str = ""):
    guardian_status = "PASS" if guardian_passed else "FAIL"

    if test_passed is None:
        test_status = "NOT_RUN"
        evidence = ""
    else:
        test_status = "PASS" if test_passed else "FAIL"
        evidence = extract_test_evidence(test_stdout) if not test_passed else "all tests passed"

    return [
        {"rule": "no_eval", "enforced_by": "ArchitectureGuardian", "status": guardian_status},
        {"rule": "no_exec", "enforced_by": "ArchitectureGuardian", "status": guardian_status},
        {"rule": "no_subprocess", "enforced_by": "ArchitectureGuardian", "status": guardian_status},
        {"rule": "syntax_valid", "enforced_by": "ArchitectureGuardian", "status": guardian_status},
        {
            "rule": "tests_passed",
            "enforced_by": "pytest",
            "status": test_status,
            "evidence": evidence
        },
    ]


def compute_hash(payload: dict) -> str:
    canonical = json.dumps(
        payload,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":")
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def save_audit(
    validation_id: str,
    code: str,
    tests: str,
    status: str,
    stage: str,
    reason: str,
    execution_dir: str,
    controls: list,
    stdout: str = "",
    stderr: str = "",
    return_code=None,
    guardian_result=None,
):
    os.makedirs(AUDIT_DIR, exist_ok=True)

    audit_payload = {
        "id": validation_id,
        "status": status,
        "stage": stage,
        "reason": reason,
        "code": code,
        "tests": tests,
        "controls": controls,
        "control_version": "v1",
        "stdout": stdout,
        "stderr": stderr,
        "return_code": return_code,
        "guardian_result": guardian_result,
        "execution_dir": execution_dir,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }

    audit_hash = compute_hash(audit_payload)
    signature = sign_hash(audit_hash)

    audit_payload["sha256"] = audit_hash
    audit_payload["signature"] = signature

    file_path = os.path.join(AUDIT_DIR, f"{validation_id}.json")

    if os.path.exists(file_path):
        raise RuntimeError(f"Audit file already exists: {file_path}")

    with open(file_path, "x") as f:
        json.dump(audit_payload, f, indent=2, ensure_ascii=False)

    return audit_hash, signature


def validate_code(code: str, tests: str):
    validation_id = generate_id()

    execution_dir = create_execution_dir(validation_id)
    module_file, test_file = write_files(execution_dir, code, tests)

    guardian = ArchitectureGuardian()
    guardian_result = guardian.validate(module_file, code)

    # M1 FAIL
    if not guardian_result.get("success", False):
        controls = build_controls(guardian_passed=False, test_passed=None, test_stdout="")
        reason = guardian_result.get("error", "guardian validation failed")

        audit_hash, signature = save_audit(
            validation_id=validation_id,
            code=code,
            tests=tests,
            status="REJECTED",
            stage="M1",
            reason=reason,
            execution_dir=execution_dir,
            controls=controls,
            guardian_result=guardian_result,
        )

        return {
            "status": "REJECTED",
            "stage": "M1",
            "reason": reason,
            "id": validation_id,
            "sha256": audit_hash,
            "signature": signature,
            "controls": controls,
            "control_version": "v1",
        }

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

        # M3 FAIL
        if return_code != 0:
            controls = build_controls(guardian_passed=True, test_passed=False, test_stdout=stdout)
            reason = "test execution failed"

            audit_hash, signature = save_audit(
                validation_id=validation_id,
                code=code,
                tests=tests,
                status="REJECTED",
                stage="M3",
                reason=reason,
                execution_dir=execution_dir,
                controls=controls,
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
                "signature": signature,
                "controls": controls,
                "control_version": "v1",
            }

    except Exception as e:
        controls = build_controls(guardian_passed=True, test_passed=False, test_stdout="")
        reason = "execution error"

        audit_hash, signature = save_audit(
            validation_id=validation_id,
            code=code,
            tests=tests,
            status="REJECTED",
            stage="M3",
            reason=reason,
            execution_dir=execution_dir,
            controls=controls,
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
            "signature": signature,
            "controls": controls,
            "control_version": "v1",
        }

    # SUCCESS
    controls = build_controls(guardian_passed=True, test_passed=True, test_stdout=stdout)
    reason = "all checks passed"

    audit_hash, signature = save_audit(
        validation_id=validation_id,
        code=code,
        tests=tests,
        status="CERTIFIED",
        stage="M3",
        reason=reason,
        execution_dir=execution_dir,
        controls=controls,
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
        "signature": signature,
        "controls": controls,
        "control_version": "v1",
    }