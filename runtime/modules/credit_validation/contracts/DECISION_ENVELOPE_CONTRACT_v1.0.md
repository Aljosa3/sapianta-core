# SAPIANTA
# Decision Envelope Contract v1.0
# Development Module – Credit Validation

---

## 1. Purpose

The Decision Envelope represents a complete, structured, and deterministic
snapshot of a credit decision proposal subject to validation.

This document is a development artifact and does not introduce new governance domains.

---

## 2. Structural Principles

A Decision Envelope MUST be:

- Complete (no missing required fields)
- Schema-valid
- Free of implicit fields
- Deterministically serializable
- Hashable prior to validation

Failure to meet these conditions results in STRUCTURAL_INVALID.

---

## 3. Required Fields (v1.0)

### 3.1 Identification

- decision_id (string, unique)
- timestamp (ISO-8601)
- policy_version (string)
- currency (ISO 4217)

---

### 3.2 Client Snapshot

- client_id (string)
- rating (enumeration: A, B, C, D)
- sector_code (string)
- group_id (string | null)

This is a frozen snapshot. No external lookup is performed.

---

### 3.3 Credit Parameters

- requested_exposure (positive numeric)
- tenor_months (positive integer)
- collateral_value (numeric >= 0)
- collateral_type (string)
- collateral_coverage_ratio (numeric >= 0)

No implicit calculation allowed in v1.0.

---

### 3.4 Portfolio Snapshot (Light-B)

- current_client_exposure (numeric >= 0)
- current_group_exposure (numeric >= 0)
- current_sector_exposure (numeric >= 0)
- total_portfolio_exposure (numeric > 0)

All values represent snapshot state at decision time.

---

## 4. Prohibited Fields

The Decision Envelope MUST NOT contain:

- Free-text justification
- AI interpretation fields
- Document references
- Override flags

---

## 5. Deterministic Integrity

The Decision Envelope MUST:

- Be deterministically serialized
- Be hashed before validation
- Include the hash in the validation output

---

## 6. Structural Failure Conditions

STRUCTURAL_INVALID occurs if:

- Required fields are missing
- Field types are invalid
- rating is outside allowed enumeration
- Numeric fields violate domain constraints

If STRUCTURAL_INVALID, policy validation MUST NOT start.

---

## 7. Versioning

Changes to this structure require:

- New contract version
- No retroactive impact
- Explicit version bump