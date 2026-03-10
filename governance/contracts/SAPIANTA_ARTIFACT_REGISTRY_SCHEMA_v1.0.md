# SAPIANTA Artifact Registry Schema v1.0

## Purpose

The Artifact Registry stores canonical references to all artifacts
produced by the SAPIANTA ecosystem.

Artifacts include:

- proposals
- decision envelopes
- experiment outputs
- strategies
- models
- research artifacts

The registry enables:

- traceability
- reproducibility
- artifact discovery
- governance compliance


---

# Artifact Structure

Each artifact entry must contain:

artifact_id
artifact_type
domain_id
timestamp
artifact_hash
artifact_location
producer
metadata


---

# Artifact Entry Example

artifact_entry:

artifact_id: artifact-123
artifact_type: decision_envelope
domain_id: trading
timestamp: 2026-03-10T10:15:22

artifact_hash: 8d84c2bd2aff776837568e6b3e4efbef68f0656661beb6d8c67b37dabfd669e0

artifact_location:
runtime/history/decision_ledger.jsonl

producer:
decision_spine

metadata:

proposal_id: test-001
policy_result: APPROVED


---

# Artifact Types

Allowed artifact types:

proposal
decision_envelope
ledger_entry
experiment_result
strategy
model


---

# Registry Requirements

The artifact registry must be:

append-only

deterministic

hash-bound

auditable


---

# Registry Storage

Default registry location:

runtime/history/artifact_registry.jsonl


Each entry must be stored as JSON.


---

# Governance Constraints

Artifacts cannot be modified after registration.

Any change must produce a new artifact entry.

