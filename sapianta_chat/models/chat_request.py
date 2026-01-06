from dataclasses import dataclass, field
from typing import Any, Dict, Optional
from datetime import datetime
import uuid


@dataclass(frozen=True)
class ChatRequest:
    request_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    original_input: str = ""
    normalized_input: str = ""
    interaction_type: str = "unknown"
    context: Optional[Dict[str, Any]] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=lambda: {
        "created_at": datetime.utcnow().isoformat()
    })
