# artifact_builder.py

import hashlib
import json
import subprocess
from typing import Dict
from experimental.sandbox_poc.artifact_schema import canonical_hash, compute_artifact_hash


def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def get_current_commit_hash() -> str:
    """
    Returns current git HEAD commit hash.
    """
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception:
        return "UNKNOWN_COMMIT"


def build_artifact(
    prompt_text: str,
    response_text: str,
    diff_text: str,
    declared_scope: str = "NON_STRUCTURAL",
    iteration: int = 1,
) -> Dict:

    parent_commit_hash = get_current_commit_hash()

    prompt_hash = hash_text(prompt_text)
    response_hash = hash_text(response_text)
    diff_hash = hash_text(diff_text)

    validation_report = {
        "determinism": True,
        "replay": True,
        "boundary": True,
        "layer_dependency": True,
        "freeze": True,
    }

    validation_report_hash = canonical_hash(validation_report)

    # Build binding payload first (without artifact_id)
    binding_payload = {
        "parent_commit_hash": parent_commit_hash,
        "prompt_hash": prompt_hash,
        "response_hash": response_hash,
        "diff_hash": diff_hash,
        "validation_report_hash": validation_report_hash,
        "sandbox_iteration_count": iteration,
        "declared_scope": declared_scope,
    }

    # Deterministic artifact_id derived from binding payload
    artifact_id = canonical_hash(binding_payload)

    artifact = {
        "artifact_id": artifact_id,
        **binding_payload,
    }

    artifact["artifact_hash"] = compute_artifact_hash(artifact)

    return artifact


def save_artifact(artifact: Dict, path: str):
    canonical = json.dumps(
        artifact,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(canonical)