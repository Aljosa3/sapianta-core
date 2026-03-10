# SAPIANTA_DECISION_ENVELOPE_SCHEMA_v1.0

Status: CANONICAL SPECIFICATION
Layer: L2 Decision Spine
Scope: Decision Artifact Output
Version: 1.0

---

# 1. Purpose

This document defines the canonical schema for the Decision Envelope Artifact used within the SAPIANTA Decision Spine architecture.

The Decision Envelope represents the final, validated, governance-approved output of the Decision Spine after policy evaluation.

The Decision Envelope ensures:

- deterministic decision output
- policy traceability
- audit-ready decisions
- replay-verifiable governance
- tamper-resistant decision recording

The Decision Envelope is the canonical artifact recorded in the system ledger.

---

# 2. Architectural Position

The Decision Envelope exists after policy validation in the Decision Spine.

Architecture flow:

domain_logic
↓
proposal_artifact
↓
policy_validation
↓
advisory_evaluation
↓
decision_envelope
↓
ledger_record
↓
execution_intent

The Decision Envelope represents the final decision artifact produced by the system.

---

# 3. Canonical Decision Envelope Structure

All decision envelopes must follow the canonical schema.

Example decision envelope:

decision_envelope:

  decision_id: "uuid"

  domain_id: "trading"
  domain_version: "1.0"

  proposal_reference:
    proposal_id: "uuid"
    proposal_hash: "sha256"

  input_state_hash: "sha256"

  decision_result: "APPROVED"

  decision_timestamp: "ISO-8601"

  policy_trace:
    - policy_module: "max_position_size"
      result: "PASS"

    - policy_module: "exposure_limit"
      result: "PASS"

  advisory:
    summary: "policy validated momentum breakout signal"
    explanation_source: "policy_engine"

  action:
    type: "BUY"
    asset: "BTC"
    quantity: 0.5

  risk_context:
    exposure_before: 0.12
    exposure_after: 0.18
    volatility_regime: "medium"

  envelope_hash: "sha256"

  authority_signature:
    authority_id: "decision_spine"
    signature: "hash_signature"

  metadata:
    environment: "production"
    execution_mode: "live"

---

# 4. Required Fields

The following fields are mandatory:

decision_id
domain_id
domain_version
proposal_reference
input_state_hash
decision_result
decision_timestamp
policy_trace
action
envelope_hash
authority_signature

These fields ensure that the decision is:

- deterministic
- auditable
- replay-verifiable
- governance compliant

---

# 5. Decision Result

The decision_result field represents the governance outcome.

Allowed values:

APPROVED
REJECTED
DEFERRED
CONDITIONAL

Example:

decision_result: APPROVED

If the decision is rejected, the envelope must still be recorded in the ledger.

---

# 6. Proposal Reference

Each Decision Envelope must reference the originating proposal artifact.

proposal_reference:

  proposal_id: uuid
  proposal_hash: sha256

This ensures traceability between:

proposal → decision.

---

# 7. Policy Trace

Policy Trace records the evaluation performed by the Policy Engine.

Example:

policy_trace:

  - policy_module: max_position_size
    result: PASS

  - policy_module: exposure_limit
    result: PASS

  - policy_module: volatility_limit
    result: PASS

Policy Trace enables:

- governance transparency
- regulatory audit
- deterministic replay validation

---

# 8. Advisory Section

The advisory section contains the system explanation context.

Example:

advisory:

  summary: "policy validated signal"
  explanation_source: "policy_engine"

Advisory must remain deterministic and must not include stochastic or non-deterministic information.

---

# 9. Action Structure

The action section represents the approved domain-specific operation.

Example (Trading):

action:
  type: BUY
  asset: BTC
  quantity: 0.5

Example (Credit):

action:
  type: APPROVE_LOAN
  loan_amount: 100000
  duration_months: 60

Example (Insurance):

action:
  type: ISSUE_POLICY
  policy_type: LIABILITY
  coverage: 500000

The action structure is domain extensible but must remain deterministic.

---

# 10. Risk Context

Risk Context provides decision-relevant state used during evaluation.

Example:

risk_context:

  exposure_before: 0.12
  exposure_after: 0.18
  volatility_regime: medium

Risk context enables:

- risk monitoring
- replay verification
- policy analysis

---

# 11. Hash Binding

Each Decision Envelope must include a cryptographic hash.

envelope_hash = sha256(serialized_envelope_without_hash)

Hash binding ensures:

- tamper detection
- deterministic replay
- audit verification

---

# 12. Authority Signature

Each Decision Envelope must include an authority signature.

Example:

authority_signature:

  authority_id: decision_spine
  signature: hash_signature

This ensures the envelope is:

- governance validated
- authorized by the decision system
- cryptographically verifiable

---

# 13. Deterministic Serialization

Decision envelopes must be serialized deterministically.

Requirements:

- sorted keys
- stable encoding
- no runtime randomness
- canonical serialization

Allowed formats:

JSON
canonical JSON
YAML (deterministic)

---

# 14. Ledger Recording

Each Decision Envelope must be recorded in the system ledger.

ledger_entry:

decision_id
envelope_hash
timestamp
previous_hash

The ledger must be:

- append-only
- immutable
- tamper-evident

---

# 15. Replay Requirements

The system must support deterministic replay of all decisions.

Replay must reconstruct:

input_state
proposal
policy_validation
decision_envelope

Replay verification must produce:

identical decision result
identical envelope hash

---

# 16. Artifact Lifecycle

The Decision Envelope participates in the following lifecycle:

proposal_generation
proposal_submission
policy_validation
advisory_evaluation
decision_envelope_creation
ledger_recording
execution_intent

Decision Envelopes must be:

immutable
hash-bound
replay-verifiable
audit traceable

---

# 17. Governance Constraints

Decision Envelopes must not:

- contain non-deterministic fields
- contain runtime randomness
- bypass policy validation
- modify proposal artifacts

All envelopes must be generated exclusively by the Decision Spine.

---

# 18. Cross-Domain Interoperability

Decision Envelopes must support multi-domain operation.

Supported domains include:

trading
credit
insurance
macro_policy
risk_monitoring
energy_systems
supply_chain

The canonical schema ensures consistent decision governance across domains.

---

# 19. System Invariants

The following invariants must always hold.

INVARIANT_ENVELOPE_IMMUTABILITY
Decision envelopes must never be modified after creation.

INVARIANT_HASH_BINDING
Each envelope must include a verifiable cryptographic hash.

INVARIANT_POLICY_VALIDATION
No envelope may be created without policy evaluation.

INVARIANT_LEDGER_RECORDING
Every decision envelope must be recorded in the ledger.

INVARIANT_DETERMINISM
Replay of the same input must produce the same envelope hash.

---

END OF SPECIFICATION