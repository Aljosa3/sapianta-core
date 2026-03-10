FILE PATH:
sapianta_system/governance/contracts/SAPIANTA_LEDGER_SCHEMA_v1.0.md


# SAPIANTA_LEDGER_SCHEMA_v1.0

Status: CANONICAL SPECIFICATION
Layer: L2 Decision Spine
Scope: Decision Ledger Recording
Version: 1.0


------------------------------------------------------------
1. PURPOSE
------------------------------------------------------------

This document defines the canonical schema for the Decision Ledger used within the SAPIANTA architecture.

The ledger is an append-only record that stores all Decision Envelopes produced by the Decision Spine.

The ledger ensures:

- tamper-evident decision history
- deterministic replay capability
- audit-ready governance traceability
- chronological ordering of decisions
- cryptographic integrity of decision chains

The ledger forms the final artifact layer of the Decision Spine pipeline.

Architecture flow:

domain_logic
↓
proposal_artifact
↓
policy_validation
↓
advisory
↓
decision_envelope
↓
ledger_record
↓
execution


------------------------------------------------------------
2. ARCHITECTURAL POSITION
------------------------------------------------------------

The ledger is the final persistence layer of the Decision Spine.

It records the output of the Decision Envelope artifact.

The ledger connects decisions into a cryptographically verifiable chain.

Decision chain structure:

decision_envelope_1
↓
ledger_entry_1
↓
ledger_entry_2
↓
ledger_entry_3
↓
...


------------------------------------------------------------
3. LEDGER STRUCTURE
------------------------------------------------------------

Each decision recorded in the ledger must follow the canonical ledger entry structure.

Example ledger entry:

ledger_entry:

  ledger_version: "1.0"

  decision_reference:
    decision_id: "uuid"
    envelope_hash: "sha256"

  domain:
    domain_id: "trading"
    domain_version: "1.0"

  timestamp: "ISO-8601"

  previous_hash: "sha256"

  entry_hash: "sha256"

  environment: "production"

  metadata:
    execution_mode: "live"
    system_version: "decision_spine_v1.0"


------------------------------------------------------------
4. REQUIRED FIELDS
------------------------------------------------------------

The following fields are mandatory:

ledger_version
decision_reference
domain
timestamp
previous_hash
entry_hash

These fields ensure that:

- ledger entries can be verified
- the decision chain is cryptographically secured
- replay validation is possible


------------------------------------------------------------
5. DECISION REFERENCE
------------------------------------------------------------

Each ledger entry must reference the originating Decision Envelope.

decision_reference:

  decision_id: uuid
  envelope_hash: sha256

This ensures that the ledger links directly to the canonical decision artifact.

Traceability chain:

proposal
↓
decision_envelope
↓
ledger_entry


------------------------------------------------------------
6. HASH CHAIN STRUCTURE
------------------------------------------------------------

The ledger implements a cryptographic hash chain.

Each entry references the previous entry.

previous_hash = sha256(previous_ledger_entry)

entry_hash = sha256(serialized_current_entry_without_entry_hash)

Example chain:

entry_1
previous_hash = GENESIS_HASH

entry_2
previous_hash = hash(entry_1)

entry_3
previous_hash = hash(entry_2)


------------------------------------------------------------
7. GENESIS ENTRY
------------------------------------------------------------

The ledger must begin with a genesis entry.

Example:

ledger_entry:

  ledger_version: "1.0"

  decision_reference:
    decision_id: "GENESIS"
    envelope_hash: "GENESIS"

  domain:
    domain_id: "system"
    domain_version: "1.0"

  timestamp: "system_initialization"

  previous_hash: "NONE"

  entry_hash: sha256(genesis_entry)


The genesis entry anchors the decision chain.


------------------------------------------------------------
8. APPEND ONLY CONSTRAINT
------------------------------------------------------------

The ledger must be append-only.

Allowed operations:

append_entry

Forbidden operations:

update_entry
delete_entry
reorder_entries

Any violation of append-only rules invalidates the ledger.


------------------------------------------------------------
9. DETERMINISTIC SERIALIZATION
------------------------------------------------------------

Ledger entries must be serialized deterministically.

Requirements:

- sorted keys
- stable encoding
- canonical representation
- no runtime randomness

Allowed serialization formats:

JSON
canonical JSON
YAML (deterministic)


------------------------------------------------------------
10. REPLAY REQUIREMENTS
------------------------------------------------------------

The ledger must support deterministic replay of all decisions.

Replay process:

replay_scope:

- input_state
- proposal
- policy_validation
- decision_envelope
- ledger_entry

Replay verification must produce:

- identical envelope hash
- identical ledger entry hash
- identical decision result


------------------------------------------------------------
11. LEDGER STORAGE MODEL
------------------------------------------------------------

Ledger entries must be stored sequentially.

Example storage format:

decision_ledger.jsonl

Each line represents one ledger entry.

Example:

{ledger_entry_1}
{ledger_entry_2}
{ledger_entry_3}

This format ensures:

- append-only behavior
- efficient streaming
- replay capability


------------------------------------------------------------
12. GOVERNANCE CONSTRAINTS
------------------------------------------------------------

The ledger must obey the following governance rules.

The ledger must not:

- allow mutation of previous entries
- accept unsigned decision envelopes
- accept envelopes without policy trace
- allow bypass of Decision Spine

All ledger writes must originate from the Decision Spine.


------------------------------------------------------------
13. CROSS-DOMAIN COMPATIBILITY
------------------------------------------------------------

The ledger must support decisions from multiple domains.

Example domains:

trading
credit
insurance
macro_policy
risk_monitoring

Domain identification must always be present in the ledger entry.


------------------------------------------------------------
14. SYSTEM INVARIANTS
------------------------------------------------------------

The following invariants must always hold.

INVARIANT_LEDGER_APPEND_ONLY

Ledger entries must never be modified once written.


INVARIANT_LEDGER_HASH_CHAIN

Each ledger entry must reference the previous entry hash.


INVARIANT_LEDGER_DECISION_TRACEABILITY

Each ledger entry must reference a valid Decision Envelope.


INVARIANT_LEDGER_DETERMINISM

Ledger serialization must be deterministic.


INVARIANT_LEDGER_REPLAY_VALIDATION

Replaying the ledger must reconstruct identical decisions.


------------------------------------------------------------
15. CANONICAL YAML EXAMPLE
------------------------------------------------------------

ledger_entry:

  ledger_version: "1.0"

  decision_reference:
    decision_id: "b91b3e5e-3c3c-4d3c-9b9e-93a8d2d4f0b2"
    envelope_hash: "7a3d9c1f..."

  domain:
    domain_id: "trading"
    domain_version: "1.0"

  timestamp: "2026-03-09T12:45:00Z"

  previous_hash: "c39a21c0..."

  entry_hash: "a9d83e21..."

  environment: "production"

  metadata:
    execution_mode: "live"
    system_version: "decision_spine_v1.0"


------------------------------------------------------------
END OF DOCUMENT
------------------------------------------------------------