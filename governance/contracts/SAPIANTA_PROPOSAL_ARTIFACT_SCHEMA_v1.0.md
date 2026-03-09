# SAPIANTA_PROPOSAL_ARTIFACT_SCHEMA_v1.0

Status: CANONICAL SPECIFICATION  
Layer: L3 Governance  
Scope: Decision Spine Input Artifact  
Version: 1.0

---

# 1. Purpose

This document defines the canonical schema for the Proposal Artifact used within the SAPIANTA Decision Spine architecture.

The Proposal Artifact represents the deterministic output of a domain module submitted to the Decision Spine for policy evaluation and decision processing.

The proposal artifact ensures:

- deterministic proposal generation
- replay-verifiable decision input
- policy validation compatibility
- cross-domain interoperability
- governance traceability

This schema is required for all domains integrating through the SAPIANTA Domain Contract.

---

# 2. Architectural Position

The Proposal Artifact exists between domain logic and the Decision Spine.

Architecture flow:

domain_logic  
↓  
proposal_artifact  
↓  
policy_validation  
↓  
decision_envelope  
↓  
ledger_record  

The Proposal Artifact therefore represents the formal input boundary of the Decision Spine.

---

# 3. Canonical Proposal Structure

All proposals must follow the canonical schema.

Example proposal artifact:

proposal:
  proposal_id: "uuid"
  domain_id: "trading"
  domain_version: "1.0"

  timestamp: "ISO-8601"

  input_state_hash: "sha256"
  proposal_hash: "sha256"

  action:
    type: "BUY"
    asset: "BTC"
    quantity: 0.5

  rationale:
    description: "momentum breakout"
    signal_source: "strategy_momentum_v2"

  risk_context:
    exposure_before: 0.12
    exposure_after: 0.18
    volatility_regime: "medium"

  metadata:
    strategy_id: "momentum_v2"
    environment: "simulation"

---

# 4. Required Fields

The following fields are mandatory:

proposal_id  
domain_id  
domain_version  
timestamp  
input_state_hash  
proposal_hash  
action  
rationale  
risk_context  

These fields ensure the proposal can be:

- validated
- replayed
- audited
- traced through the decision pipeline

---

# 5. Action Structure

The action section describes the domain-specific operation proposed to the Decision Spine.

Example structures:

Trading example:

action:
  type: BUY
  asset: BTC
  quantity: 0.5

Credit example:

action:
  type: APPROVE_LOAN
  loan_amount: 100000
  duration_months: 60

Insurance example:

action:
  type: ISSUE_POLICY
  policy_type: LIABILITY
  coverage: 500000

The action structure is domain extensible but must remain deterministic.

---

# 6. Rationale Structure

The rationale provides the explanation context for the proposal.

Example:

rationale:
  description: "trend breakout detected"
  signal_source: "strategy_momentum_v2"

The rationale must:

- explain the proposal
- reference the signal or model
- remain deterministic

---

# 7. Risk Context

Risk context provides decision-relevant context for policy evaluation.

Example:

risk_context:
  exposure_before: 0.12
  exposure_after: 0.18
  volatility_regime: medium

Risk context enables:

- policy evaluation
- risk monitoring
- replay verification

---

# 8. Hash Binding

Each proposal artifact must include cryptographic hashes.

input_state_hash  
proposal_hash  

Hash binding guarantees:

- deterministic replay
- tamper resistance
- audit verification

Hash calculation rules:

input_state_hash = sha256(serialized_input_state)

proposal_hash = sha256(serialized_proposal_without_hash_field)

---

# 9. Deterministic Serialization

All proposal artifacts must be serialized deterministically.

Requirements:

- sorted keys
- stable encoding
- no implicit defaults
- no runtime randomness

Serialization formats allowed:

- YAML
- JSON
- canonical JSON

The serialization format must support exact replay reproduction.

---

# 10. Replay Requirements

The proposal artifact must allow deterministic replay of the decision process.

Replay must reconstruct:

input_state  
proposal  
policy_validation  
decision_result  

Replay verification must yield:

identical decision outcome  
identical decision envelope hash  

---

# 11. Artifact Lifecycle

The proposal artifact participates in the following lifecycle:

generate_proposal  
validate_schema  
submit_to_decision_spine  
policy_evaluation  
decision_envelope_creation  
ledger_recording  

Proposal artifacts must be:

- immutable
- hash-bound
- audit traceable

---

# 12. Governance Constraints

Proposal artifacts must not:

- contain non-deterministic fields
- contain runtime randomness
- contain mutable references
- bypass policy evaluation

Domains must submit proposals exclusively through the Domain Contract interface.

---

# 13. Cross-Domain Interoperability

Proposal artifacts must support multi-domain operation.

Examples of domains:

trading  
credit  
insurance  
macro_policy  
risk_monitoring  

The canonical proposal structure ensures that the Decision Spine can evaluate proposals across domains consistently.

---

# 14. System Invariants

The following invariants must always hold.

INVARIANT_PROPOSAL_IMMUTABILITY  
Proposal artifacts must never be modified after creation.

INVARIANT_HASH_BINDING  
Each proposal artifact must include verifiable hash references.

INVARIANT_DETERMINISTIC_STRUCTURE  
Proposal artifacts must serialize deterministically.

INVARIANT_POLICY_GATE  
All proposals must pass through policy validation.

INVARIANT_DECISION_SPINE_INPUT  
Only proposal artifacts may enter the Decision Spine.

These invariants guarantee system safety and auditability.

---

# 15. Relationship to Domain Contract

The Proposal Artifact Schema complements the SAPIANTA Domain Contract.

Domain contract defines:

- domain integration rules
- proposal submission interface
- execution boundaries

Proposal schema defines:

- proposal structure
- deterministic serialization
- hash binding
- replay guarantees

Together they form the formal interface between domains and the Decision Spine.

---

# 16. Architectural Principle

SAPIANTA enforces the following invariant:

DOMAINS_GENERATE_PROPOSALS  
DECISION_SPINE_MAKES_DECISIONS  

Domains provide:

analysis  
signals  
domain logic  

The Decision Spine provides:

proposal intake  
policy evaluation  
decision governance  
decision envelope  
ledger recording  

This architecture guarantees:

- deterministic decisions
- policy enforcement
- system-wide auditability
- cross-domain governance

---

# End of Document