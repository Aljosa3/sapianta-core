# validator_service.py

import os
import uuid
import subprocess
import json
import hashlib
from datetime import datetime

from runtime.development.architecture_guardian import ArchitectureGuardian
from sapianta_product.policy_engine import validate_policy

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

TEST_TIMEOUT = 30

AUDIT_DIR = os.path.abspath(
    os.path.join(PROJECT_ROOT, "runtime", "audit_logs")
)

BASE_URL = "http://178.105.26.164:8000"


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


def detect_weak_tests(tests: str):
    return "assert" not in tests


def detect_message(stage: str, guardian_passed: bool, test_passed, stdout: str, stderr: str) -> str:
    combined = (stdout or "") + "\n" + (stderr or "")

    if stage == "M1":
        if "os.system" in combined:
            return "System command execution is not allowed."
        if "exec" in combined or "eval" in combined:
            return "Dynamic execution is not allowed."
        if "subprocess" in combined:
            return "External process execution is blocked."
        if "SyntaxError" in combined or "syntax" in combined.lower():
            return "Code contains a syntax error."
        return "Code is blocked before execution due to security policy."

    if test_passed is False:
        if "NameError" in combined:
            return "Function is not defined."
        if "ImportError" in combined or "ModuleNotFoundError" in combined:
            return "Import failed — module or dependency is missing."
        if "assert" in combined:
            return "Test failed — logic is incorrect."
        if "SyntaxError" in combined:
            return "Code contains a syntax error."
        return "Tests failed."

    if test_passed is True:
        if "collected 0 items" in combined:
            return "No tests were executed."
        return "Execution approved. All validation checks passed."

    return "Validation completed."


# --------------------------------------------------
# 🔥 RISK LAYER (FINAL - DETERMINISTIC + SMART)
# --------------------------------------------------

def detect_risk(stage: str, guardian_passed: bool, stdout: str, stderr: str, status: str) -> str:

    combined = f"{stage}\n{stdout or ''}\n{stderr or ''}".lower()

    # --------------------------------------------------
    # 🔴 POLICY RISK (M2)
    # --------------------------------------------------
    if stage == "M2":
        return "This decision violates policy or regulatory constraints."

    # --------------------------------------------------
    # ✅ SUCCESS → NO RISK (DETERMINISTIC)
    # --------------------------------------------------
    if status == "CERTIFIED":
        return ""

    # --------------------------------------------------
    # ⚠️ WEAK / NO TESTS
    # --------------------------------------------------
    if "collected 0 items" in combined:
        return "Tests may be insufficient to guarantee correctness."

    # --------------------------------------------------
    # 🔴 SECURITY RISKS
    # --------------------------------------------------
    if "os.system" in combined:
        return "This code could delete files, modify the system, or execute destructive commands on the host machine."

    if "subprocess" in combined:
        return "This code could run external programs, potentially bypassing application-level controls."

    if "eval" in combined or "exec" in combined:
        return "This code could execute arbitrary or dynamically generated instructions, including malicious payloads."

    # --------------------------------------------------
    # 🔴 LOGIC RISK
    # --------------------------------------------------
    if "assert" in combined or "assertionerror" in combined:
        return "This code produces incorrect results, which can lead to wrong decisions or system behavior."

    # --------------------------------------------------
    # 🔴 GUARDIAN BLOCK
    # --------------------------------------------------
    if stage == "M1" and not guardian_passed:
        return "This code violates a security policy and was blocked before execution."

    # --------------------------------------------------
    # 🔴 EXECUTION / VALIDATION FAILURE
    # --------------------------------------------------
    if stage == "M3":
        return "This code failed validation and may be unsafe or unreliable."

    return ""

def extract_test_evidence(stdout: str, stderr: str) -> str:
    combined = (stdout or "") + "\n" + (stderr or "")

    if "NameError" in combined:
        for line in combined.splitlines():
            if "NameError" in line:
                return f"NameError → {line.strip()}"

    if "ModuleNotFoundError" in combined or "ImportError" in combined:
        for line in combined.splitlines():
            if "ModuleNotFoundError" in line or "ImportError" in line:
                return f"Import error → {line.strip()}"

    for line in combined.splitlines():
        if "assert" in line:
            return f"Assertion failed → {line.strip()}"

    if "SyntaxError" in combined:
        return "SyntaxError → invalid code"

    if stderr:
        return stderr.strip().splitlines()[-1]

    return "test execution failed"


def build_controls(guardian_passed: bool, test_passed=None, stdout="", stderr=""):
    guardian_status = "PASS" if guardian_passed else "FAIL"

    if test_passed is None:
        test_status = "NOT_RUN"

        if not guardian_passed:
            evidence = "execution prevented by security policy"
        else:
            evidence = "blocked before execution"
    else:
        test_status = "PASS" if test_passed else "FAIL"

        if not guardian_passed:
            evidence = "blocked by execution control layer"
        elif test_passed is False:
            evidence = extract_test_evidence(stdout, stderr) or "test failed"
        else:
            evidence = "all tests passed"

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
    message: str = None,
    severity: str = None,
    risk: str = None,
    eu_ai_act: dict = None,   # 🔥 NEW
):
    os.makedirs(AUDIT_DIR, exist_ok=True)

    audit_payload = {
        "id": validation_id,
        "status": status,
        "stage": stage,
        "severity": severity,
        "reason": reason,
        "message": message,
        "risk": risk,
        "eu_ai_act": eu_ai_act,   # 🔥 NEW
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
    signature = None

    audit_payload["sha256"] = audit_hash
    audit_payload["signature"] = signature

    file_path = os.path.join(AUDIT_DIR, f"{validation_id}.json")

    if os.path.exists(file_path):
        raise RuntimeError(f"Audit file already exists: {file_path}")

    with open(file_path, "x") as f:
        json.dump(audit_payload, f, indent=2, ensure_ascii=False)

    return audit_hash, signature


# --------------------------------------------------
# SEVERITY LAYER
# --------------------------------------------------

def detect_severity(stage: str, guardian_passed: bool, test_passed):
    """
    Returns severity level based on validation stage.
    Minimal extension: adds M2 support without breaking existing logic.
    """

    if stage == "M1":
        return "CRITICAL"

    if stage == "M2":
        # policy violations are serious but below hard security failure
        return "HIGH"

    if stage == "M3":
        if test_passed is False:
            return "HIGH"
        if test_passed is True:
            return "NONE"

    return "UNKNOWN"


# --------------------------------------------------
# EU AI ACT STATUS LAYER
# --------------------------------------------------

def build_eu_ai_act_status(stage: str):
    """
    Minimal deterministic EU AI Act status mapping.
    """

    if stage in ["M1", "M2", "M3"]:
        return {"compliant": False}

    return {"compliant": True}


def validate_code(code: str, tests: str):
    validation_id = generate_id()
    audit_url = f"{BASE_URL}/audit-viewer/{validation_id}"

    execution_dir = create_execution_dir(validation_id)
    module_file, test_file = write_files(execution_dir, code, tests)

    guardian = ArchitectureGuardian()
    guardian_result = guardian.validate(module_file, code)

    # --------------------------------------------------
    # M1 — ARCHITECTURE GUARDIAN (FAIL-CLOSED)
    # --------------------------------------------------
    if not guardian_result.get("success", False):
        controls = build_controls(False)

        guardian_error = guardian_result.get(
            "error",
            "guardian validation failed"
        )

        message = detect_message(
            "M1",
            False,
            None,
            code,
            guardian_error
        )

        severity = detect_severity("M1", False, None)

        risk = detect_risk(
            "M1",
            False,
            code + "\n" + guardian_error,
            "",
            "REJECTED"
        )

        audit_hash, signature = save_audit(
            validation_id,
            code,
            tests,
            "REJECTED",
            "M1",
            guardian_error,
            execution_dir,
            controls,
            guardian_result=guardian_result,
            message=message,
            severity=severity,
            risk=risk,
            eu_ai_act=build_eu_ai_act_status("M1")
        )

        return {
            "status": "REJECTED",
            "stage": "M1",
            "severity": severity,
            "reason": guardian_error,
            "message": message,
            "risk": risk,
            "id": validation_id,
            "sha256": audit_hash,
            "signature": signature,
            "controls": controls,
            "control_version": "v1",
            "audit_url": audit_url
        }

    # --------------------------------------------------
    # M2 — POLICY LAYER (DECISION COMPLIANCE)
    # --------------------------------------------------
    policy_payload = {
        "code": code,
        "text": code   # 🔥 NEW
    }

    try:
        m2 = validate_policy(policy_payload)
    except Exception as e:
        # fail-closed policy layer
        m2 = {
            "status": "REJECTED",
            "stage": "M2",
            "reason": "Policy validation failed.",
            "risk": "Policy layer error.",
            "severity": "HIGH",
            "controls": [],
            "eu_ai_act": {"compliant": False}
        }

    if m2["status"] == "REJECTED":

        controls = build_controls(True)
        controls.extend(m2.get("controls", []))

        message = f"Policy violation: {m2['reason']}"

        risk = detect_risk("M2", True, "", "", "REJECTED")

        audit_hash, signature = save_audit(
            validation_id,
            code,
            tests,
            "REJECTED",
            "M2",
            m2["reason"],
            execution_dir,
            controls,
            stdout="",                     # 🔥 ADD
            stderr="",                     # 🔥 ADD
            return_code=None,              # 🔥 ADD
            guardian_result=guardian_result,
            message=message,
            severity=m2.get("severity", "HIGH"),
            risk=risk,
            eu_ai_act=build_eu_ai_act_status("M2")
        )

        return {
            "status": "REJECTED",
            "stage": "M2",
            "severity": m2.get("severity", "HIGH"),
            "reason": m2["reason"],
            "message": message,
            "risk": risk,
            "id": validation_id,
            "sha256": audit_hash,
            "signature": signature,
            "controls": controls,
            "control_version": "v1",
            "audit_url": audit_url,
            "eu_ai_act": build_eu_ai_act_status("M2")
        }

    # --------------------------------------------------
    # EXECUTION
    # --------------------------------------------------
    try:
        import sys

        result_exec = subprocess.run(
            [sys.executable, "-m", "pytest", "-q"],
            cwd=execution_dir,
            capture_output=True,
            text=True,
            timeout=TEST_TIMEOUT
        )

        stdout = result_exec.stdout
        stderr = result_exec.stderr
        return_code = result_exec.returncode

    except Exception as e:
        message = "Execution error occurred."
        controls = build_controls(True, False, "", str(e))
        severity = detect_severity("M3", True, False)
        risk = detect_risk("M3", True, "", str(e), "REJECTED")

        audit_hash, signature = save_audit(
            validation_id,
            code,
            tests,
            "REJECTED",
            "M3",
            "execution_error",
            execution_dir,
            controls,
            stdout="",                      # dodano za konsistentnost
            stderr=str(e),
            return_code=None,               # dodano za konsistentnost
            guardian_result=guardian_result,
            message=message,
            severity=severity,
            risk=risk,
            eu_ai_act=build_eu_ai_act_status("M3")
        )

        return {
            "status": "REJECTED",
            "stage": "M3",
            "severity": severity,
            "reason": "execution_error",
            "message": message,
            "risk": risk,
            "details": str(e),
            "id": validation_id,
            "sha256": audit_hash,
            "signature": signature,
            "controls": controls,
            "control_version": "v1",
            "audit_url": audit_url
        }

    # --------------------------------------------------
    # TEST FAIL
    # --------------------------------------------------
    if return_code != 0:
        controls = build_controls(True, False, stdout, stderr)
        message = detect_message("M3", True, False, stdout, stderr)
        severity = detect_severity("M3", True, False)
        risk = detect_risk("M3", True, stdout, stderr, "REJECTED")

        audit_hash, signature = save_audit(
            validation_id,
            code,
            tests,
            "REJECTED",
            "M3",
            "test execution failed",
            execution_dir,
            controls,
            stdout,
            stderr,
            return_code,
            guardian_result,
            message,
            severity,
            risk,
            eu_ai_act=build_eu_ai_act_status("M3")
        )

        return {
            "status": "REJECTED",
            "stage": "M3",
            "severity": severity,
            "reason": "test execution failed",
            "message": message,
            "risk": risk,
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
            "audit_url": audit_url
        }

    # --------------------------------------------------
    # SUCCESS (M1 + M2 + M3 PASSED)
    # --------------------------------------------------
    controls = build_controls(True, True, stdout, stderr)

    # 🔹 vključimo tudi M2 kontrole (če obstajajo)
    if 'm2' in locals() and m2.get("controls"):
        controls.extend(m2["controls"])

    message = detect_message("M3", True, True, stdout, stderr)
    severity = detect_severity("M3", True, True)
    risk = detect_risk("M3", True, stdout, stderr, "CERTIFIED")

    if detect_weak_tests(tests):
        message = "Tests passed, but they may be too weak to ensure correctness."

    audit_hash, signature = save_audit(
        validation_id,
        code,
        tests,
        "CERTIFIED",
        "M3",
        "all checks passed",
        execution_dir,
        controls,
        stdout,
        stderr,
        return_code,
        guardian_result,
        message,
        severity,
        risk,
        eu_ai_act={"compliant": True}
    )

    result = {
        "status": "CERTIFIED",
        "stage": "M3",
        "severity": severity,
        "reason": "all checks passed",
        "message": message,
        "risk": risk,
        "id": validation_id,
        "sha256": audit_hash,
        "signature": signature,
        "controls": controls,
        "control_version": "v1",
        "audit_url": audit_url,

        # 🔥 NOVO — EU AI ACT LAYER
        "eu_ai_act": {"compliant": True}
    }

    if detect_weak_tests(tests):
        result["warning"] = "Weak tests produce unreliable results."

    return result