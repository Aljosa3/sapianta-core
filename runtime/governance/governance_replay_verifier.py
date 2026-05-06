"""
SAPIANTA Governance Replay Verifier

Read-only verifier for dormant governance sidecar history.

This module is intentionally observational:
- no enforcement activation
- no active control loading
- no Decision Spine activation
- no policy participation
- no history mutation
"""

import json
from pathlib import Path

from runtime.governance.control_promotion_lifecycle import is_valid_transition


DEFAULT_PATHS = {
    "patterns": "runtime/history/pattern_memory.jsonl",
    "candidates": "runtime/history/control_candidates.jsonl",
    "shadows": "runtime/history/shadow_validation.jsonl",
    "promotions": "runtime/history/control_promotion_events.jsonl",
}


def read_jsonl(path) -> list:
    """
    Read JSONL records deterministically without writing to disk.
    """
    file_path = Path(path)

    if not file_path.exists():
        return []

    if file_path.stat().st_size == 0:
        return []

    records = []

    with file_path.open("r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            stripped = line.strip()

            if not stripped:
                continue

            try:
                records.append(json.loads(stripped))
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"Invalid JSON line {line_number} in {file_path}"
                ) from exc

    return records


def _record_pair(record: dict, id_key: str, hash_key: str) -> tuple:
    return (record.get(id_key), record.get(hash_key))


def _lineage_pair(lineage: dict, id_key: str, hash_key: str) -> tuple:
    return (lineage.get(id_key), lineage.get(hash_key))


def _status(errors: list) -> str:
    return "FAIL" if errors else "PASS"


def _report(errors: list, counts: dict) -> dict:
    return {
        "status": _status(errors),
        "errors": errors,
        "counts": counts,
    }


def verify_governance_replay(paths: dict | None = None) -> dict:
    """
    Reconstruct and validate dormant governance sidecar lineage.
    """
    resolved_paths = {**DEFAULT_PATHS, **(paths or {})}

    try:
        patterns = read_jsonl(resolved_paths["patterns"])
        candidates = read_jsonl(resolved_paths["candidates"])
        shadows = read_jsonl(resolved_paths["shadows"])
        promotions = read_jsonl(resolved_paths["promotions"])
    except ValueError as exc:
        return _report(
            errors=[str(exc)],
            counts={
                "patterns": 0,
                "candidates": 0,
                "shadows": 0,
                "promotions": 0,
            },
        )

    counts = {
        "patterns": len(patterns),
        "candidates": len(candidates),
        "shadows": len(shadows),
        "promotions": len(promotions),
    }
    errors = []

    pattern_pairs = {
        _record_pair(record, "pattern_id", "pattern_hash")
        for record in patterns
    }
    candidate_pairs = {
        _record_pair(record, "candidate_id", "candidate_hash")
        for record in candidates
    }
    shadow_pairs = {
        _record_pair(record, "shadow_result_id", "shadow_result_hash")
        for record in shadows
    }

    for index, candidate in enumerate(candidates):
        lineage = candidate.get("lineage") or {}
        pair = _lineage_pair(lineage, "pattern_id", "pattern_hash")

        if pair not in pattern_pairs:
            errors.append(
                "candidate[{index}] missing pattern lineage "
                "pattern_id={pattern_id} pattern_hash={pattern_hash}".format(
                    index=index,
                    pattern_id=pair[0],
                    pattern_hash=pair[1],
                )
            )

    for index, shadow in enumerate(shadows):
        lineage = shadow.get("lineage") or {}
        pair = _lineage_pair(lineage, "candidate_id", "candidate_hash")

        if pair not in candidate_pairs:
            errors.append(
                "shadow[{index}] missing candidate lineage "
                "candidate_id={candidate_id} candidate_hash={candidate_hash}".format(
                    index=index,
                    candidate_id=pair[0],
                    candidate_hash=pair[1],
                )
            )

    for index, promotion in enumerate(promotions):
        lineage = promotion.get("lineage") or {}
        pair = _lineage_pair(lineage, "shadow_result_id", "shadow_result_hash")

        if pair not in shadow_pairs:
            errors.append(
                "promotion[{index}] missing shadow lineage "
                "shadow_result_id={shadow_id} shadow_result_hash={shadow_hash}".format(
                    index=index,
                    shadow_id=pair[0],
                    shadow_hash=pair[1],
                )
            )

        previous_state = promotion.get("previous_state")
        next_state = promotion.get("next_state")

        try:
            valid_transition = is_valid_transition(previous_state, next_state)
        except ValueError:
            valid_transition = False

        if not valid_transition:
            errors.append(
                "promotion[{index}] illegal transition "
                "{previous_state}->{next_state}".format(
                    index=index,
                    previous_state=previous_state,
                    next_state=next_state,
                )
            )

    return _report(errors=errors, counts=counts)
