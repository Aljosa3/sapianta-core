from typing import List, Dict, Any
from datetime import datetime
import uuid


def hds_json_schema(options: List[Dict[str, Any]], *, meta_extra: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """
    Deterministic JSON-safe envelope.
    v0.4: meta-only additive extension.
    """
    base_meta = {
        "version": "hds-json-output-v0.3",
        "disclaimer": "Decision authority rests solely with the human operator."
    }

    # v0.4 meta-only additions (additive, non-semantic)
    v0_4_meta = {
        "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "trace_id": str(uuid.uuid4()),
        "source": "cli",
    }

    if meta_extra:
        v0_4_meta.update(meta_extra)

    return {
        "options": options,
        "meta": {
            **base_meta,
            **v0_4_meta,
        }
    }
