# SAPIANTA_DOMAIN_CONTRACT_v1.0

Status: CANONICAL SPECIFICATION
Layer: L3 Governance
Scope: Domain Integration
Version: 1.0

---

# 1. Purpose

This document defines the formal contract between a domain module and the SAPIANTA Decision Spine.

A domain may implement specialized logic (trading, credit, insurance, macro policy, etc.),
but it must not implement its own decision engine.

Instead, domains interact with the core system through a standardized interface:

domain_logic → proposal → Decision Spine

This contract ensures:

- deterministic decision processing
- consistent governance enforcement
- replay-verifiable decisions
- cross-domain interoperability

---

# 2. Domain Identification

Each domain must define a unique identifier.

Example:

domain:
  domain_id: trading
  domain_version: 1.0
  domain_owner: sapianta-domain-trading

Domain identification is required for:

- artifact traceability
- policy routing
- ledger classification

---

# 3. Input State Schema

Each domain must define the structure of the input state used to generate proposals.

Example: Trading domain

input_state:
  market_state: object
  signal: object
  risk_context: object
  timestamp: datetime

Example: Credit domain

input_state:
  customer_profile: object
  financial_data: object
  credit_score: float
  loan_request: object
  timestamp: datetime

The input state must satisfy:

- deterministic serialization
- schema validation
- reproducibility for replay

---

# 4. Proposal Structure

All domains must produce a Proposal Artifact that conforms to the standard structure.

Example proposal:

proposal:
  domain: trading
  action: BUY
  asset: BTC
  quantity: 0.5
  rationale: momentum_breakout
  risk_context: object
  timestamp: datetime

Requirements:

- proposal must be deterministic
- proposal must contain domain identifier
- proposal must include sufficient context for replay

---

# 5. Policy Integration

Domain proposals must be validated through the Policy Engine before execution.

Example policy modules for Trading:

policy_modules:
  - max_position_size
  - max_drawdown
  - market_hours
  - exposure_limit

Example policy modules for Credit:

policy_modules:
  - max_default_probability
  - regulatory_limits
  - customer_risk_classification
  - loan_exposure_rules

Policy validation must be fail-closed.

If validation fails:

decision_result: REJECTED

---

# 6. Decision Output Format

The Decision Spine returns a Decision Artifact.

Example:

decision:
  decision_id: uuid
  result: APPROVED
  policy_trace: list
  envelope_hash: hash
  timestamp: datetime

The decision artifact must be:

- hash-bound
- signed
- replay-verifiable

---

# 7. Execution Interface

The domain must define how the decision result is interpreted.

Example: Trading

execution_mapping:
  APPROVED: place_order
  REJECTED: ignore_signal

Example: Credit

execution_mapping:
  APPROVED: approve_loan
  REJECTED: decline_loan

Execution must be performed outside the Decision Spine,
based on the approved decision artifact.

---

# 8. Artifact Requirements

All domain interactions with the Decision Spine must produce artifacts.

artifact_types:
  - proposal_artifact
  - decision_envelope
  - ledger_entry

These artifacts must be:

- immutable
- hash-bound
- stored in append-only ledger

---

# 9. Replay Requirements

The system must support deterministic replay.

Replay must reproduce:

replay_scope:
  - input_state
  - proposal
  - policy_validation
  - decision_envelope

Replay must yield the same decision result.

---

# 10. Governance Constraints

Domains must not:

- modify the Decision Spine
- bypass policy validation
- write directly to the ledger
- alter governance artifacts

All domain interactions must occur via the Domain Contract interface.

---

# 11. Versioning

Domain contracts must be versioned.

contract_version:
  name: SAPIANTA_DOMAIN_CONTRACT
  version: 1.0

Future revisions should maintain backward compatibility where possible.

---

# 12. Architectural Principle

system_invariant:
  decision_spine: single
  domains: multiple

This invariant means:

- one deterministic decision pipeline
- multiple domain modules connected to the same governance system

Domains provide specialized logic.

The Decision Spine provides:

decision_pipeline:
  - proposal
  - policy
  - advisory
  - envelope
  - ledger

This guarantees:

- deterministic decisions
- cross-domain governance
- system-wide auditability

---

# 13. Domain Responsibilities

Domains must:

- generate deterministic proposals
- maintain domain input schema
- implement execution adapters
- preserve replay compatibility
- respect governance constraints

Domains must not:

- implement their own decision pipeline
- bypass policy validation
- mutate governance artifacts

---

# End of Document