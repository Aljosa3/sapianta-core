from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import sys
import os

# ensure repo root on path
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from modules.hds_json_output_v0_3.schema import hds_json_schema

app = FastAPI(title="SAPIANTA HDS API v0.1")

@app.post("/hds/preview")
async def hds_preview(request: Request):
    # accept but do not interpret payload
    _ = await request.body()

    options = [
        {
            "id": "opt-1",
            "title": "Proceed conservatively",
            "rationale": "Maintains system stability under uncertainty.",
            "consequences": [
                "Lower short-term gain",
                "Reduced risk exposure"
            ],
            "uncertainty": "Medium"
        },
        {
            "id": "opt-2",
            "title": "Delay decision",
            "rationale": "Allows additional human assessment.",
            "consequences": [
                "Opportunity cost",
                "Improved contextual clarity"
            ],
            "uncertainty": "Low"
        }
    ]

    output = hds_json_schema(
        options,
        meta_extra={
            "source": "api",
            "execution_context": "http",
            "audit_hint": "stdout-only"
        }
    )

    # stdout audit (passive)
    print(output)

    return JSONResponse(content=output)
