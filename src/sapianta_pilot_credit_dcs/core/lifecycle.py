from dataclasses import dataclass
import hashlib
import json


def _canonical_hash(data: dict) -> str:
    canonical = json.dumps(data, sort_keys=True)
    return hashlib.sha256(canonical.encode()).hexdigest()


@dataclass(frozen=True)
class Proposal:
    payload: dict
    hash: str


@dataclass(frozen=True)
class Advisory:
    proposal_hash: str
    payload: dict
    hash: str


@dataclass(frozen=True)
class Decision:
    advisory_hash: str
    outcome: dict
    hash: str


def create_proposal(payload: dict) -> Proposal:
    h = _canonical_hash(payload)
    return Proposal(payload=payload, hash=h)


def create_advisory(proposal: Proposal, payload: dict) -> Advisory:
    combined = {
        "proposal_hash": proposal.hash,
        "payload": payload,
    }
    h = _canonical_hash(combined)
    return Advisory(
        proposal_hash=proposal.hash,
        payload=payload,
        hash=h,
    )


def create_decision(advisory: Advisory) -> Decision:
    combined = {
        "advisory_hash": advisory.hash,
        "outcome": advisory.payload,
    }
    h = _canonical_hash(combined)
    return Decision(
        advisory_hash=advisory.hash,
        outcome=advisory.payload,
        hash=h,
    )


def replay_decision(decision: Decision) -> Decision:
    combined = {
        "advisory_hash": decision.advisory_hash,
        "outcome": decision.outcome,
    }
    recalculated = _canonical_hash(combined)

    if recalculated != decision.hash:
        raise ValueError("Replay hash mismatch")

    return decision