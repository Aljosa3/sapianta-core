# runtime/mep/sp6_audit_export.py

import json
from datetime import datetime
from context import ExecutionContext


def sp6_audit_export(ctx: ExecutionContext, target: str = "stdout"):
    """
    SP-6: External Audit Export

    Best-effort izvoz audit artefakta.
    Ne vpliva na execution tok.
    """

    try:
        record = {
            "context_id": ctx.context_id,
            "timestamp": datetime.utcnow().isoformat(),
            "status": ctx.status.name,
            "phase": ctx.phase.name,
            "source": ctx.source,
            "decisions": ctx.decisions,
            "violations": ctx.violations,
            "policy": getattr(ctx, "policy", None),
            "policy_ok": getattr(ctx, "policy_ok", None),
            "result": ctx.result,
            "explain": getattr(ctx, "explain", None),
        }

        if target == "stdout":
            print("\n=== AUDIT EXPORT (SP-6) ===")
            print(json.dumps(record, indent=2, ensure_ascii=False))

        elif target == "file":
            path = f"runtime/audit/{ctx.context_id}.json"
            with open(path, "w", encoding="utf-8") as f:
                json.dump(record, f, indent=2, ensure_ascii=False)

        ctx.add_decision("SP-6 audit export completed")
        return True

    except Exception as e:
        # SP-6 nikoli ne sme sesuti sistema
        ctx.add_violation(f"SP-6 export failed: {str(e)}")
        return False
