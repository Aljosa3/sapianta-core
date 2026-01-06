from dataclasses import dataclass, field
from typing import Any, Dict, List
from datetime import datetime
import uuid


@dataclass(frozen=True)
class ChatResponse:
    response_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    response_text: str = ""
    response_type: str = "informational"
    explanation_level: str = "normal"
    warnings: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=lambda: {
        "created_at": datetime.utcnow().isoformat()
    })
