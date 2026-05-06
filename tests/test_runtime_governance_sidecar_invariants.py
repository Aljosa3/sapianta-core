import ast
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
GOVERNANCE_DIR = REPO_ROOT / "runtime" / "governance"
DECISION_SPINE_PATH = REPO_ROOT / "runtime" / "engine" / "decision_spine.py"


def load_module(name: str, filename: str):
    module_path = GOVERNANCE_DIR / filename
    spec = importlib.util.spec_from_file_location(name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


PATTERN_MEMORY = load_module("pattern_memory_invariant", "pattern_memory.py")
CONTROL_CANDIDATES = load_module(
    "control_candidate_registry_invariant",
    "control_candidate_registry.py",
)
SHADOW_VALIDATION = load_module("shadow_validation_invariant", "shadow_validation.py")
PROMOTION_LIFECYCLE = load_module(
    "control_promotion_lifecycle_invariant",
    "control_promotion_lifecycle.py",
)

LEGAL_PROMOTION_TRANSITIONS = [
    ("DRAFT", "CANDIDATE"),
    ("CANDIDATE", "SHADOW"),
    ("SHADOW", "REVIEW"),
    ("REVIEW", "APPROVED"),
    ("APPROVED", "ACTIVE"),
    ("ACTIVE", "DEPRECATED"),
    ("DEPRECATED", "REVOKED"),
]


SIDE_CAR_PATHS = [
    GOVERNANCE_DIR / "pattern_memory.py",
    GOVERNANCE_DIR / "control_candidate_registry.py",
    GOVERNANCE_DIR / "shadow_validation.py",
    GOVERNANCE_DIR / "control_promotion_lifecycle.py",
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def jsonl_lines(path: Path):
    return [json.loads(line) for line in path.read_text().splitlines()]


def test_canonical_json_stability_across_sidecars():
    payload_a = {"b": 2, "a": {"z": 3, "c": 1}}
    payload_b = {"a": {"c": 1, "z": 3}, "b": 2}
    expected = '{"a":{"c":1,"z":3},"b":2}'

    assert PATTERN_MEMORY._canonical_json(payload_a) == expected
    assert CONTROL_CANDIDATES._canonical_json(payload_b) == expected
    assert SHADOW_VALIDATION._canonical_json(payload_a) == expected
    assert PROMOTION_LIFECYCLE._canonical_json(payload_b) == expected


def test_deterministic_hashing_stability():
    signature_a = PATTERN_MEMORY.build_failure_signature(
        rule="No Eval",
        status="FAIL",
        stage="M1",
        reason="  Guardian   Failed  ",
        evidence="assert x",
    )
    signature_b = PATTERN_MEMORY.build_failure_signature(
        rule="no eval",
        status="fail",
        stage="m1",
        reason="Guardian Failed",
        evidence="assert x",
    )

    assert signature_a == signature_b
    assert signature_a["signature_hash"] == PATTERN_MEMORY._hash(
        signature_a["normalized"]
    )


def test_replay_safe_payload_generation_is_stable():
    failure_signature = PATTERN_MEMORY.build_failure_signature(
        rule="tests_passed",
        status="FAIL",
        stage="M3",
        reason="test execution failed",
        evidence="assert expected",
    )

    pattern_a = PATTERN_MEMORY.build_pattern_record(
        failure_signature=failure_signature,
        validation_id="val_123",
        audit_hash="audit_hash",
        audit_signature="audit_signature",
        audit_path="runtime/audit_logs/val_123.json",
        observed_at="2026-05-06T00:00:00Z",
    )
    pattern_b = PATTERN_MEMORY.build_pattern_record(
        failure_signature=failure_signature,
        validation_id="val_123",
        audit_hash="audit_hash",
        audit_signature="audit_signature",
        audit_path="runtime/audit_logs/val_123.json",
        observed_at="2026-05-06T00:00:00Z",
    )

    candidate_signature = CONTROL_CANDIDATES.build_candidate_signature(
        control_name="reject failing tests",
        control_intent="Block generated modules with failing tests",
        pattern_signature_hash=failure_signature["signature_hash"],
    )
    lineage = CONTROL_CANDIDATES.build_candidate_lineage(
        pattern_id=pattern_a["pattern_id"],
        pattern_hash=pattern_a["pattern_hash"],
        validation_id="val_123",
        audit_hash="audit_hash",
    )
    candidate_a = CONTROL_CANDIDATES.build_candidate_record(
        candidate_signature=candidate_signature,
        lineage=lineage,
        state="CANDIDATE",
    )
    candidate_b = CONTROL_CANDIDATES.build_candidate_record(
        candidate_signature=candidate_signature,
        lineage=lineage,
        state="CANDIDATE",
    )

    shadow_a = SHADOW_VALIDATION.build_shadow_result_record(
        candidate_id=candidate_a["candidate_id"],
        candidate_hash=candidate_a["candidate_hash"],
        production_decision="APPROVED",
        would_block=True,
        would_pass=False,
        envelope_hash="envelope_hash",
        validation_id="val_123",
        audit_hash="audit_hash",
    )
    shadow_b = SHADOW_VALIDATION.build_shadow_result_record(
        candidate_id=candidate_a["candidate_id"],
        candidate_hash=candidate_a["candidate_hash"],
        production_decision="APPROVED",
        would_block=True,
        would_pass=False,
        envelope_hash="envelope_hash",
        validation_id="val_123",
        audit_hash="audit_hash",
    )

    promotion_a = PROMOTION_LIFECYCLE.build_promotion_event_record(
        candidate_id=candidate_a["candidate_id"],
        candidate_hash=candidate_a["candidate_hash"],
        shadow_result_id=shadow_a["shadow_result_id"],
        shadow_result_hash=shadow_a["shadow_result_hash"],
        approval_id="approval_123",
        approval_hash="approval_hash",
        previous_state="SHADOW",
        next_state="REVIEW",
        transition_reason="shadow evidence ready",
    )
    promotion_b = PROMOTION_LIFECYCLE.build_promotion_event_record(
        candidate_id=candidate_a["candidate_id"],
        candidate_hash=candidate_a["candidate_hash"],
        shadow_result_id=shadow_a["shadow_result_id"],
        shadow_result_hash=shadow_a["shadow_result_hash"],
        approval_id="approval_123",
        approval_hash="approval_hash",
        previous_state="SHADOW",
        next_state="REVIEW",
        transition_reason="shadow evidence ready",
    )

    assert pattern_a == pattern_b
    assert candidate_a == candidate_b
    assert shadow_a == shadow_b
    assert promotion_a == promotion_b


def test_append_only_writes_preserve_existing_records(tmp_path):
    path = tmp_path / "pattern_memory.jsonl"
    signature = PATTERN_MEMORY.build_failure_signature(rule="no_exec", status="FAIL")

    first = PATTERN_MEMORY.build_pattern_record(
        failure_signature=signature,
        validation_id="val_1",
        audit_hash="audit_1",
    )
    second = PATTERN_MEMORY.build_pattern_record(
        failure_signature=signature,
        validation_id="val_2",
        audit_hash="audit_2",
    )

    PATTERN_MEMORY.append_pattern_record(first, path=str(path))
    first_line = path.read_text()
    PATTERN_MEMORY.append_pattern_record(second, path=str(path))

    assert path.read_text().startswith(first_line)
    assert jsonl_lines(path) == [first, second]


def test_append_only_writers_use_temporary_paths(tmp_path):
    candidate_path = tmp_path / "control_candidates.jsonl"
    shadow_path = tmp_path / "shadow_validation.jsonl"
    promotion_path = tmp_path / "control_promotion_events.jsonl"

    candidate = CONTROL_CANDIDATES.build_candidate_record(
        candidate_signature=CONTROL_CANDIDATES.build_candidate_signature(
            control_name="test control",
            control_intent="inspection only",
        ),
        lineage=CONTROL_CANDIDATES.build_candidate_lineage(
            pattern_id="pattern_id",
            pattern_hash="pattern_hash",
            validation_id="val_1",
            audit_hash="audit_1",
        ),
        state="DRAFT",
        governance_metadata={"scope": "test"},
    )
    CONTROL_CANDIDATES.append_candidate_record(candidate, path=str(candidate_path))

    shadow = SHADOW_VALIDATION.build_shadow_result_record(
        candidate_id=candidate["candidate_id"],
        candidate_hash=candidate["candidate_hash"],
        production_decision="APPROVED",
        would_block=False,
        would_pass=True,
        envelope_hash="envelope_hash",
        validation_id="val_1",
        audit_hash="audit_1",
    )
    SHADOW_VALIDATION.append_shadow_result(shadow, path=str(shadow_path))

    promotion = PROMOTION_LIFECYCLE.build_promotion_event_record(
        candidate_id=candidate["candidate_id"],
        candidate_hash=candidate["candidate_hash"],
        shadow_result_id=shadow["shadow_result_id"],
        shadow_result_hash=shadow["shadow_result_hash"],
        previous_state="CANDIDATE",
        next_state="SHADOW",
        transition_reason="begin shadow inspection",
    )
    PROMOTION_LIFECYCLE.append_promotion_event(promotion, path=str(promotion_path))

    assert jsonl_lines(candidate_path) == [candidate]
    assert jsonl_lines(shadow_path) == [shadow]
    assert jsonl_lines(promotion_path) == [promotion]


def test_invalid_state_rejection():
    candidate_signature = CONTROL_CANDIDATES.build_candidate_signature(
        control_name="x",
        control_intent="y",
    )
    lineage = CONTROL_CANDIDATES.build_candidate_lineage()

    with pytest.raises(ValueError):
        CONTROL_CANDIDATES.build_candidate_record(
            candidate_signature=candidate_signature,
            lineage=lineage,
            state="ACTIVE",
        )

    with pytest.raises(ValueError):
        SHADOW_VALIDATION.build_shadow_result_record(state="ACTIVE")

    with pytest.raises(ValueError):
        PROMOTION_LIFECYCLE.build_promotion_event_record(next_state="UNKNOWN")

    with pytest.raises(ValueError):
        PROMOTION_LIFECYCLE.build_promotion_event_record(
            previous_state="UNKNOWN",
            next_state="REVIEW",
        )


@pytest.mark.parametrize("previous_state,next_state", LEGAL_PROMOTION_TRANSITIONS)
def test_legal_promotion_transitions_are_valid(previous_state, next_state):
    assert PROMOTION_LIFECYCLE.is_valid_transition(previous_state, next_state)

    record = PROMOTION_LIFECYCLE.build_promotion_event_record(
        candidate_id="candidate_id",
        candidate_hash="candidate_hash",
        previous_state=previous_state,
        next_state=next_state,
        transition_reason=f"{previous_state} to {next_state}",
    )

    assert record["previous_state"] == previous_state
    assert record["next_state"] == next_state


@pytest.mark.parametrize(
    "previous_state,next_state",
    [
        ("DRAFT", "SHADOW"),
        ("CANDIDATE", "APPROVED"),
        ("SHADOW", "ACTIVE"),
        ("REVIEW", "ACTIVE"),
        ("APPROVED", "DEPRECATED"),
        ("ACTIVE", "REVOKED"),
        ("DEPRECATED", "ACTIVE"),
        ("REVOKED", "ACTIVE"),
        (None, "DRAFT"),
    ],
)
def test_illegal_promotion_transitions_are_rejected(previous_state, next_state):
    assert not PROMOTION_LIFECYCLE.is_valid_transition(previous_state, next_state)

    with pytest.raises(ValueError):
        PROMOTION_LIFECYCLE.build_promotion_event_record(
            candidate_id="candidate_id",
            candidate_hash="candidate_hash",
            previous_state=previous_state,
            next_state=next_state,
        )


def test_transition_validation_is_deterministic():
    first = [
        PROMOTION_LIFECYCLE.is_valid_transition(previous_state, next_state)
        for previous_state, next_state in LEGAL_PROMOTION_TRANSITIONS
    ]
    second = [
        PROMOTION_LIFECYCLE.is_valid_transition(previous_state, next_state)
        for previous_state, next_state in LEGAL_PROMOTION_TRANSITIONS
    ]

    assert first == second
    assert all(first)


def test_promotion_transition_replay_stability():
    first = [
        PROMOTION_LIFECYCLE.build_promotion_event_record(
            candidate_id="candidate_id",
            candidate_hash="candidate_hash",
            previous_state=previous_state,
            next_state=next_state,
            transition_reason="deterministic replay",
        )
        for previous_state, next_state in LEGAL_PROMOTION_TRANSITIONS
    ]
    second = [
        PROMOTION_LIFECYCLE.build_promotion_event_record(
            candidate_id="candidate_id",
            candidate_hash="candidate_hash",
            previous_state=previous_state,
            next_state=next_state,
            transition_reason="deterministic replay",
        )
        for previous_state, next_state in LEGAL_PROMOTION_TRANSITIONS
    ]

    assert first == second


def test_legal_promotion_lifecycle_append_only_guarantee(tmp_path):
    path = tmp_path / "control_promotion_events.jsonl"
    records = [
        PROMOTION_LIFECYCLE.build_promotion_event_record(
            candidate_id="candidate_id",
            candidate_hash="candidate_hash",
            previous_state=previous_state,
            next_state=next_state,
            transition_reason="legal transition",
        )
        for previous_state, next_state in LEGAL_PROMOTION_TRANSITIONS
    ]

    for index, record in enumerate(records):
        before = path.read_text() if path.exists() else ""
        PROMOTION_LIFECYCLE.append_promotion_event(record, path=str(path))
        after = path.read_text()

        assert after.startswith(before)
        assert jsonl_lines(path) == records[: index + 1]


def test_lineage_preservation_across_sidecar_records():
    pattern = PATTERN_MEMORY.build_pattern_record(
        failure_signature=PATTERN_MEMORY.build_failure_signature(
            rule="tests_passed",
            status="FAIL",
            stage="M3",
        ),
        validation_id="val_123",
        audit_hash="audit_hash",
        audit_signature="audit_signature",
        audit_path="runtime/audit_logs/val_123.json",
        observed_at="2026-05-06T00:00:00Z",
    )

    candidate = CONTROL_CANDIDATES.build_candidate_record(
        candidate_signature=CONTROL_CANDIDATES.build_candidate_signature(
            control_name="candidate",
            control_intent="inspect pattern",
            pattern_signature_hash=pattern["failure_signature"]["signature_hash"],
        ),
        lineage=CONTROL_CANDIDATES.build_candidate_lineage(
            pattern_id=pattern["pattern_id"],
            pattern_hash=pattern["pattern_hash"],
            validation_id=pattern["lineage"]["validation_id"],
            audit_hash=pattern["lineage"]["audit_hash"],
        ),
        state="CANDIDATE",
    )

    shadow = SHADOW_VALIDATION.build_shadow_result_record(
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

    promotion = PROMOTION_LIFECYCLE.build_promotion_event_record(
        candidate_id=candidate["candidate_id"],
        candidate_hash=candidate["candidate_hash"],
        shadow_result_id=shadow["shadow_result_id"],
        shadow_result_hash=shadow["shadow_result_hash"],
        pattern_id=shadow["lineage"]["pattern_id"],
        pattern_hash=shadow["lineage"]["pattern_hash"],
        validation_id=shadow["lineage"]["validation_id"],
        audit_hash=shadow["lineage"]["audit_hash"],
        previous_state="SHADOW",
        next_state="REVIEW",
    )

    assert candidate["lineage"]["pattern_id"] == pattern["pattern_id"]
    assert candidate["lineage"]["pattern_hash"] == pattern["pattern_hash"]
    assert shadow["lineage"]["candidate_id"] == candidate["candidate_id"]
    assert shadow["lineage"]["candidate_hash"] == candidate["candidate_hash"]
    assert promotion["lineage"]["shadow_result_id"] == shadow["shadow_result_id"]
    assert promotion["lineage"]["shadow_result_hash"] == shadow["shadow_result_hash"]
    assert promotion["lineage"]["validation_id"] == "val_123"
    assert promotion["lineage"]["audit_hash"] == "audit_hash"


def test_sidecar_modules_do_not_import_runtime_enforcement_paths():
    forbidden_prefixes = {
        "runtime.engine",
        "runtime.orchestrator",
        "runtime.modules",
        "runtime.production",
        "runtime.trading",
    }

    for path in SIDE_CAR_PATHS:
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    assert not any(
                        alias.name == prefix or alias.name.startswith(prefix + ".")
                        for prefix in forbidden_prefixes
                    )
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                assert not any(
                    module == prefix or module.startswith(prefix + ".")
                    for prefix in forbidden_prefixes
                )


def test_decision_spine_file_is_not_mutated_by_sidecar_writers(tmp_path):
    before = sha256_file(DECISION_SPINE_PATH)

    pattern_path = tmp_path / "pattern_memory.jsonl"
    candidate_path = tmp_path / "control_candidates.jsonl"
    shadow_path = tmp_path / "shadow_validation.jsonl"
    promotion_path = tmp_path / "control_promotion_events.jsonl"

    pattern = PATTERN_MEMORY.build_pattern_record(
        failure_signature=PATTERN_MEMORY.build_failure_signature(
            rule="syntax_valid",
            status="FAIL",
        ),
        validation_id="val_1",
        audit_hash="audit_1",
        metadata={"test": "decision_spine_unchanged"},
    )
    PATTERN_MEMORY.append_pattern_record(pattern, path=str(pattern_path))

    candidate = CONTROL_CANDIDATES.build_candidate_record(
        candidate_signature=CONTROL_CANDIDATES.build_candidate_signature(),
        lineage=CONTROL_CANDIDATES.build_candidate_lineage(
            pattern_id=pattern["pattern_id"],
            pattern_hash=pattern["pattern_hash"],
            validation_id="val_1",
            audit_hash="audit_1",
        ),
    )
    CONTROL_CANDIDATES.append_candidate_record(candidate, path=str(candidate_path))

    shadow = SHADOW_VALIDATION.build_shadow_result_record(
        candidate_id=candidate["candidate_id"],
        candidate_hash=candidate["candidate_hash"],
        production_decision="APPROVED",
        would_block=False,
        would_pass=True,
        envelope_hash="envelope_hash",
        validation_id="val_1",
        audit_hash="audit_1",
    )
    SHADOW_VALIDATION.append_shadow_result(shadow, path=str(shadow_path))

    promotion = PROMOTION_LIFECYCLE.build_promotion_event_record(
        candidate_id=candidate["candidate_id"],
        candidate_hash=candidate["candidate_hash"],
        shadow_result_id=shadow["shadow_result_id"],
        shadow_result_hash=shadow["shadow_result_hash"],
        previous_state="DRAFT",
        next_state="CANDIDATE",
    )
    PROMOTION_LIFECYCLE.append_promotion_event(promotion, path=str(promotion_path))

    assert sha256_file(DECISION_SPINE_PATH) == before
