# FILE: modules/ipv_v1_1/semantic_mapper.py
# IPV-1.1 — deterministic semantic mapper
# Contract: IPV-1.1 Semantic Role Contract v0.1 (LOCKED)

from typing import Dict, Any


class SemanticMapperV1_1:
    """
    Deterministični semantic mapper.
    - brez LLM
    - brez zgodovine
    - brez inferenc
    - čisti if/else
    """

    def map(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Vhod: surov IPV dogodek (dict)
        Izhod: JSON shape natančno po contractu
        """

        # privzeti izhod (contract-safe)
        output = {
            "ipv_version": "1.1",
            "semantic_role": "UNRESOLVED",
            "confidence": 1.0,
            "flags": [],
            "audit": {
                "deterministic": True,
                "rule_id": None
            }
        }

        # --- DETERMINISTIČNA LOGIKA ---

        if not isinstance(event, dict):
            output["semantic_role"] = "INVALID_INPUT"
            output["flags"].append("input_not_dict")
            output["audit"]["rule_id"] = "R0"
            return output

        role = event.get("role")
        intent = event.get("intent")

        if role == "HOI" and intent == "ORCHESTRATION":
            output["semantic_role"] = "HOI_ORCHESTRATOR"
            output["audit"]["rule_id"] = "R1"

        elif role == "LLM" and intent == "RESPONSE":
            output["semantic_role"] = "LLM_RESPONSE"
            output["audit"]["rule_id"] = "R2"

        elif role == "SYSTEM" and intent == "AUDIT":
            output["semantic_role"] = "AUDIT_EVENT"
            output["audit"]["rule_id"] = "R3"

        else:
            output["semantic_role"] = "UNKNOWN"
            output["flags"].append("no_matching_rule")
            output["audit"]["rule_id"] = "R9"

        return output
