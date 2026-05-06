import hashlib
import json
from pathlib import Path

import pytest

from runtime.governance import control_candidate_registry as candidates
from runtime.governance import control_promotion_lifecycle as promotions
from runtime.governance import governance_replay_verifier as verifier
from runtime.governance import pattern_memory
from runtime.governance import shadow_validation


def write_jsonl(path: Path, records: list) -> None:
    path.write_text(
        "".join(
            json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n"
            for record in records
        ),
        encoding="utf-8",
    )


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def paths_for(tmp_path: Path) -> dict:
    return {
        "patterns": str(tmp_path / "pattern_memory.jsonl"),
        "candidates": str(tmp_path / "control_candidates.jsonl"),
        "shadows": str(tmp_path / "shadow_validation.jsonl"),
        "promotions": str(tmp_path / "control_promotion_events.jsonl"),
    }


def build_full_chain():
    pattern = pattern_memory.build_pattern_record(
        failure_signature=pattern_memory.build_failure_signature(
            rule="tests_passed",
            status="FAIL",
            stage="M3",
            reason="test execution failed",
        ),
        validation_id="val_123",
        audit_hash="audit_hash",
    )

    candidate = candidates.build_candidate_record(
        candidate_signature=candidates.build_candidate_signature(
            control_name="candidate",
            control_intent="inspect failed tests",
            pattern_signature_hash=pattern["failure_signature"]["signature_hash"],
        ),
        lineage=candidates.build_candidate_lineage(
            pattern_id=pattern["pattern_id"],
            pattern_hash=pattern["pattern_hash"],
            validation_id=pattern["lineage"]["validation_id"],
            audit_hash=pattern["lineage"]["audit_hash"],
        ),
        state="CANDIDATE",
    )

    shadow = shadow_validation.build_shadow_result_record(
        candidate_id=candidate["candidate_id"],
        candidate_hash=candidate["candidate_hash"],
        pattern_id=candidate["lineage"]["pattern_id"],
        pattern_hash=candidate["lineage"]["pattern_hash"],
        validation_id=candidate["lineage"]["validation_id"],
        audit_hash=candidate["lineage"]["audit_hash"],
        production_decision="APPROVED",
        would_block=True,
        would_pass=False,
        envelope_hash="envelope_hash",
    )

    promotion = promotions.build_promotion_event_record(
        candidate_id=candidate["candidate_id"],
        candidate_hash=candidate["candidate_hash"],
        shadow_result_id=shadow["shadow_result_id"],
        shadow_result_hash=shadow["shadow_result_hash"],
        previous_state="DRAFT",
        next_state="CANDIDATE",
        transition_reason="candidate recorded",
    )

    return pattern, candidate, shadow, promotion


def write_histories(tmp_path: Path, *, patterns, candidate_records, shadows, promotion_records):
    paths = paths_for(tmp_path)
    write_jsonl(Path(paths["patterns"]), patterns)
    write_jsonl(Path(paths["candidates"]), candidate_records)
    write_jsonl(Path(paths["shadows"]), shadows)
    write_jsonl(Path(paths["promotions"]), promotion_records)
    return paths


def test_empty_histories_pass(tmp_path):
    report = verifier.verify_governance_replay(paths_for(tmp_path))

    assert list(report.keys()) == ["status", "errors", "counts"]
    assert report == {
        "status": "PASS",
        "errors": [],
        "counts": {
            "patterns": 0,
            "candidates": 0,
            "shadows": 0,
            "promotions": 0,
        },
    }


def test_valid_full_chain_passes(tmp_path):
    pattern, candidate, shadow, promotion = build_full_chain()
    paths = write_histories(
        tmp_path,
        patterns=[pattern],
        candidate_records=[candidate],
        shadows=[shadow],
        promotion_records=[promotion],
    )

    report = verifier.verify_governance_replay(paths)

    assert report == {
        "status": "PASS",
        "errors": [],
        "counts": {
            "patterns": 1,
            "candidates": 1,
            "shadows": 1,
            "promotions": 1,
        },
    }


def test_missing_pattern_fails(tmp_path):
    _, candidate, shadow, promotion = build_full_chain()
    paths = write_histories(
        tmp_path,
        patterns=[],
        candidate_records=[candidate],
        shadows=[shadow],
        promotion_records=[promotion],
    )

    report = verifier.verify_governance_replay(paths)

    assert report["status"] == "FAIL"
    assert report["counts"]["patterns"] == 0
    assert report["errors"] == [
        (
            "candidate[0] missing pattern lineage "
            f"pattern_id={candidate['lineage']['pattern_id']} "
            f"pattern_hash={candidate['lineage']['pattern_hash']}"
        )
    ]


def test_candidate_hash_mismatch_fails(tmp_path):
    pattern, candidate, shadow, promotion = build_full_chain()
    shadow = {
        **shadow,
        "lineage": {
            **shadow["lineage"],
            "candidate_hash": "wrong_candidate_hash",
        },
    }
    paths = write_histories(
        tmp_path,
        patterns=[pattern],
        candidate_records=[candidate],
        shadows=[shadow],
        promotion_records=[promotion],
    )

    report = verifier.verify_governance_replay(paths)

    assert report["status"] == "FAIL"
    assert report["errors"] == [
        (
            "shadow[0] missing candidate lineage "
            f"candidate_id={candidate['candidate_id']} "
            "candidate_hash=wrong_candidate_hash"
        )
    ]


def test_missing_shadow_fails(tmp_path):
    pattern, candidate, _, promotion = build_full_chain()
    paths = write_histories(
        tmp_path,
        patterns=[pattern],
        candidate_records=[candidate],
        shadows=[],
        promotion_records=[promotion],
    )

    report = verifier.verify_governance_replay(paths)

    assert report["status"] == "FAIL"
    assert report["errors"] == [
        (
            "promotion[0] missing shadow lineage "
            f"shadow_result_id={promotion['lineage']['shadow_result_id']} "
            f"shadow_result_hash={promotion['lineage']['shadow_result_hash']}"
        )
    ]


def test_illegal_promotion_transition_fails(tmp_path):
    pattern, candidate, shadow, promotion = build_full_chain()
    promotion = {
        **promotion,
        "previous_state": "DRAFT",
        "next_state": "ACTIVE",
    }
    paths = write_histories(
        tmp_path,
        patterns=[pattern],
        candidate_records=[candidate],
        shadows=[shadow],
        promotion_records=[promotion],
    )

    report = verifier.verify_governance_replay(paths)

    assert report["status"] == "FAIL"
    assert report["errors"] == [
        "promotion[0] illegal transition DRAFT->ACTIVE",
    ]


def test_invalid_json_line_fails_report_and_read_jsonl_raises(tmp_path):
    paths = paths_for(tmp_path)
    Path(paths["patterns"]).write_text('{"ok": true}\nnot-json\n', encoding="utf-8")

    with pytest.raises(ValueError):
        verifier.read_jsonl(paths["patterns"])

    report = verifier.verify_governance_replay(paths)

    assert report["status"] == "FAIL"
    assert report["counts"] == {
        "patterns": 0,
        "candidates": 0,
        "shadows": 0,
        "promotions": 0,
    }
    assert report["errors"] == [
        f"Invalid JSON line 2 in {Path(paths['patterns'])}",
    ]


def test_verifier_does_not_modify_files(tmp_path):
    pattern, candidate, shadow, promotion = build_full_chain()
    paths = write_histories(
        tmp_path,
        patterns=[pattern],
        candidate_records=[candidate],
        shadows=[shadow],
        promotion_records=[promotion],
    )
    before = {
        key: sha256_file(Path(path))
        for key, path in paths.items()
    }

    report = verifier.verify_governance_replay(paths)

    after = {
        key: sha256_file(Path(path))
        for key, path in paths.items()
    }
    assert report["status"] == "PASS"
    assert after == before


def test_repeated_verification_returns_identical_report(tmp_path):
    pattern, candidate, shadow, promotion = build_full_chain()
    paths = write_histories(
        tmp_path,
        patterns=[pattern],
        candidate_records=[candidate],
        shadows=[shadow],
        promotion_records=[promotion],
    )

    first = verifier.verify_governance_replay(paths)
    second = verifier.verify_governance_replay(paths)

    assert first == second
