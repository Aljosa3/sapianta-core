# main.py

from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import json

API_KEY = "demo-secret-123"

from sapianta_product.validator_service import validate_code, compute_hash

app = FastAPI(
    title="SAPIANTA AI Firewall",
    version="0.1"
)

# --------------------------------------------------
# 🔥 CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# PATH
# --------------------------------------------------

PROJECT_ROOT = "/root/sapianta-core"
FRONTEND_DIR = "/root/sapianta-core/sapianta-product/frontend"

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
    tests: str | None = None


class VerifyInput(BaseModel):
    id: str
    sha256: str


# --------------------------------------------------
# RESPONSE MODEL
# --------------------------------------------------

class FirewallResponse(BaseModel):
    status: str
    stage: str
    reason: str
    message: str | None = None
    risk: str | None = None
    severity: str | None = None
    id: str
    sha256: str
    signature: str | None = None
    controls: list
    control_version: str
    audit_url: str


# --------------------------------------------------
# VALIDATE
# --------------------------------------------------

@app.post("/firewall/validate", response_model=FirewallResponse)
def firewall_validate(input_data: FirewallInput, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        tests = input_data.tests or "def test_placeholder(): assert True"
        result = validate_code(input_data.code, tests)

        result["audit_url"] = f"http://178.105.26.164:8000/audit-viewer/{result['id']}"

        if "risk" not in result:
            result["risk"] = ""

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --------------------------------------------------
# RAW AUDIT
# --------------------------------------------------

@app.get("/firewall/audit/{validation_id}")
def get_audit(validation_id: str):
    audit_path = os.path.join(AUDIT_DIR, f"{validation_id}.json")

    if not os.path.exists(audit_path):
        raise HTTPException(status_code=404, detail="Audit not found")

    with open(audit_path, "r") as f:
        return json.load(f)


# --------------------------------------------------
# 🔥 AUDIT VIEWER
# --------------------------------------------------

@app.get("/audit-viewer/{validation_id}", response_class=HTMLResponse)
def audit_viewer(validation_id: str):

    audit_path = os.path.join(AUDIT_DIR, f"{validation_id}.json")

    if not os.path.exists(audit_path):
        return HTMLResponse(f"<h2>Audit not found: {validation_id}</h2>", status_code=404)

    with open(audit_path, "r") as f:
        data = json.load(f)

    status = data.get("status", "UNKNOWN")
    status_color = "#16a34a" if status == "CERTIFIED" else "#dc2626"

    severity = data.get("severity", "UNKNOWN")

    severity_color = {
        "CRITICAL": "#dc2626",
        "HIGH": "#f97316",
        "NONE": "#16a34a",
    }.get(severity, "#6b7280")

    severity_bg = {
        "CRITICAL": "#fee2e2",
        "HIGH": "#ffedd5",
        "NONE": "#dcfce7",
    }.get(severity, "#f3f4f6")

    message = data.get("message")
    risk = data.get("risk")

    # --------------------------------------------------
    # 🔥 RISK BLOCK
    # --------------------------------------------------

    risk_block = ""
    if risk:
        risk_block = f"""
        <div class="message" style="border-left:6px solid #f97316;">
            <strong>Risk:</strong><br>
            {risk}
        </div>
        """

    controls = data.get("controls", [])

    controls_rows = ""
    for control in controls:
        control_status = control.get("status", "")
        control_color = "#16a34a" if control_status == "PASS" else "#dc2626"

        enforced_by = control.get("enforced_by", "")
        if enforced_by == "ArchitectureGuardian":
            enforced_by = "Execution Control Layer (ArchitectureGuardian)"

        controls_rows += f"""
        <tr>
            <td>{control.get("rule", "")}</td>
            <td>{enforced_by}</td>
            <td style="color:{control_color}; font-weight:bold;">{control_status}</td>
            <td>{control.get("evidence", "")}</td>
        </tr>
        """

    # --------------------------------------------------
    # 🔥 DECISION BANNER (FIXED)
    # --------------------------------------------------

    decision_banner = ""

    if status == "CERTIFIED":
        decision_banner = f"""
        <div style="
            background:#ecfdf5;
            border-left:8px solid #16a34a;
            padding:20px;
            border-radius:12px;
            margin-bottom:20px;
        ">
            <div style="font-size:20px; font-weight:bold; color:#16a34a;">
                ✅ DECISION CERTIFIED
            </div>
            <div style="margin-top:6px;">
                All validation checks passed. Execution approved.
            </div>
        </div>
        """
    else:
        first_fail = None

        for c in controls:
            if c.get("status") == "FAIL":
                first_fail = c
                break

        if first_fail:
            rule_name = first_fail.get("rule", "unknown")

            # 🔥 PREVOD PRAVIL (ključni fix)
            rule_map = {
                "no_eval": "eval() execution",
                "no_exec": "exec() execution",
                "no_subprocess": "subprocess execution",
                "syntax_valid": "invalid syntax",
                "tests_passed": "failed logic tests"
            }

            readable_rule = rule_map.get(rule_name, rule_name)

            decision_banner = f"""
            <div style="
                background:#fee2e2;
                border-left:8px solid #dc2626;
                padding:20px;
                border-radius:12px;
                margin-bottom:20px;
            ">
                <div style="font-size:20px; font-weight:bold; color:#dc2626;">
                    🚫 DECISION BLOCKED
                </div>
                <div style="margin-top:6px;">
                    Blocked by rule: {readable_rule}
                </div>
            </div>
            """

    raw_json = json.dumps(data, indent=2, ensure_ascii=False)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SAPIANTA Audit Viewer</title>
        <style>
            body {{
                font-family: Arial;
                background: #f8fafc;
                padding: 30px;
            }}
            .card {{
                background: white;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            }}
            .status {{
                font-size: 28px;
                font-weight: bold;
                color: {status_color};
            }}
            .message {{
                margin-top: 20px;
                padding: 16px;
                border-radius: 8px;
                background-color: #f9fafb;
                border-left: 6px solid {status_color};
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
            }}
            th {{
                background: #f1f5f9;
            }}
            pre {{
                background: #0f172a;
                color: #e5e7eb;
                padding: 15px;
                border-radius: 8px;
                overflow-x: auto;
            }}
        </style>
    </head>

    <body>

        <div class="card">
            <h1>SAPIANTA AI Firewall</h1>

            {decision_banner}

            <p>ID: <b>{data.get("id")}</b></p>
            <p class="status">{status}</p>

            <div style="margin-top:10px; font-weight:bold;">
                Severity
                <span style="
                    margin-left:8px;
                    padding:6px 12px;
                    border-radius:999px;
                    font-size:14px;
                    color:{severity_color};
                    background:{severity_bg};
                ">
                    {severity}
                </span>
            </div>

            <p>Stage: {data.get("stage")}</p>
            <p>Reason: {data.get("reason")}</p>

            {"<div class='message'><strong>Why it was blocked:</strong><br>" + message + "</div>" if message else ""}
            {risk_block}
        </div>

        <div class="card">
            <h2>Controls</h2>
            <table>
                <tr>
                    <th>Rule</th>
                    <th>Enforced by</th>
                    <th>Status</th>
                    <th>Evidence</th>
                </tr>
                {controls_rows}
            </table>
        </div>

        <div class="card">
            <h2>Raw Audit</h2>
            <pre>{raw_json}</pre>
        </div>

    </body>
    </html>
    """


# --------------------------------------------------
# VERIFY
# --------------------------------------------------

@app.post("/firewall/verify")
def verify_execution(input_data: VerifyInput):
    audit_path = os.path.join(AUDIT_DIR, f"{input_data.id}.json")

    if not os.path.exists(audit_path):
        raise HTTPException(status_code=404, detail="Audit not found")

    with open(audit_path, "r") as f:
        audit_data = json.load(f)

    stored_hash = audit_data.pop("sha256", None)

    if stored_hash is None:
        return {"valid": False, "reason": "missing hash in audit"}

    recomputed_hash = compute_hash(audit_data)

    return {
        "valid": (recomputed_hash == input_data.sha256),
        "expected": stored_hash,
        "provided": input_data.sha256
    }


# --------------------------------------------------
# FRONTEND
# --------------------------------------------------

app.mount(
    "/",
    StaticFiles(directory=FRONTEND_DIR, html=True),
    name="frontend"
)