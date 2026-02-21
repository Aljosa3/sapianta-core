# PATH: runtime/hoi_orchestrator.py

from typing import Optional, Dict, Any, List

from modules.llm_adapter import LLMAdapter, LLMRequest
from runtime.llm_output_guard import guard_llm_output

from modules.facts_extractor import extract_facts
from modules.entities_extractor import extract_entities
from modules.constraints_extractor import extract_constraints
from modules.timeline_extractor import extract_timeline


def _generate_build_proposals(
    facts: List[str],
    entities: Dict[str, Any],
    constraints: List[str],
    timeline: List[str],
) -> List[Dict[str, str]]:
    """
    Passive build proposal generator.
    Descriptive only. No decisions. No execution.
    """

    proposals: List[Dict[str, str]] = []

    proposals.append({
        "description": (
            "Create a new module directory under /modules "
            "with a valid .module_builder_manifest file."
        )
    })

    if facts:
        proposals.append({
            "description": (
                "Implement a facts extraction function that processes raw input "
                "and returns explicit factual statements only."
            )
        })

    if entities:
        proposals.append({
            "description": (
                "Implement an entities extraction function that returns only "
                "explicitly mentioned entities "
                "(dates, actors, locations, amounts, documents)."
            )
        })

    if constraints:
        proposals.append({
            "description": (
                "Implement a constraints extraction function that identifies "
                "explicit limitations, obligations, or prohibitions."
            )
        })

    if timeline:
        proposals.append({
            "description": (
                "Implement a timeline extraction function that lists explicit "
                "time-related information without ordering or prioritization."
            )
        })

    proposals.append({
        "description": (
            "Ensure the module exposes exactly one public function and "
            "does not introduce execution, decisions, or side effects."
        )
    })

    return proposals


def hoi_orchestrator(
    input_payload: Dict[str, Any],
    llm: Optional[LLMAdapter] = None,
    mode: str = "reference",
) -> Dict[str, Any]:
    """
    HOI Orchestrator v0.2

    Modes:
    - reference : analytical, reference-only output
    - proposal  : descriptive build proposal output (no execution)
    """

    base_meta = {
        "scope": "HOI_v0.2",
        "invariants": [
            "reference_only",
            "non_normative",
            "non_decisional",
            "human_in_the_loop",
        ],
    }

    if llm is None:
        return {
            "mode": "REFERENCE_RESPONSE",
            **base_meta,
            "content": {},
        }

    # --------------------------------------------------
    # 1. Guarded LLM reference description
    # --------------------------------------------------

    prompt = (
        "Describe the following situation without recommendations "
        "or decisions:\n\n"
        f"{input_payload}"
    )

    llm_response = llm.generate(LLMRequest(prompt=prompt))
    guard = guard_llm_output(llm_response.text)

    # --------------------------------------------------
    # 2. Analytical modules
    # --------------------------------------------------

    facts = extract_facts(input_payload, llm)["facts"]
    entities = extract_entities(input_payload, llm)["entities"]
    constraints = extract_constraints(input_payload, llm)["constraints"]
    timeline = extract_timeline(input_payload, llm)["timeline"]

    # --------------------------------------------------
    # 3A. BUILD PROPOSALS MODE (NO execution)
    # --------------------------------------------------

    if mode == "proposal":
        proposals = _generate_build_proposals(
            facts=facts,
            entities=entities,
            constraints=constraints,
            timeline=timeline,
        )

        return {
            "mode": "PROPOSAL_ONLY",
            **base_meta,
            "content": {
                "build_proposals": proposals,
            },
        }

    # --------------------------------------------------
    # 3B. REFERENCE MODE (default)
    # --------------------------------------------------

    return {
        "mode": "REFERENCE_RESPONSE",
        **base_meta,
        "content": {
            "llm_reference": guard.text,
            "llm_guard": {
                "status": guard.status,
                "degraded": guard.degraded,
                "reasons": guard.reasons,
                "scope": "LLM_OUTPUT_GUARD_v0.1",
            },
            "facts": facts,
            "entities": entities,
            "constraints": constraints,
            "timeline": timeline,
        },
    }
