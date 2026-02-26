# SAPIANTA
# Trading Decision Envelope Contract v1.0
# Development Module – Trading Validation

---

## 1. Purpose

The Trading Decision Envelope represents a complete, structured, and deterministic
snapshot of a trading decision proposal subject to validation.

This document is a development artifact and does not introduce new governance domains.

---

## 2. Structural Principles

A Trading Decision Envelope MUST be:

- Complete (no missing required fields)
- Schema-valid
- Free of implicit fields
- Deterministically serializable
- Hashable prior to validation

Failure to meet these conditions results in STRUCTURAL_INVALID.

---

## 3. Required Fields (v1.0)

### 3.1 Identification

- decision_id (string, unique, deterministic identifier provided by caller)
- timestamp_utc (ISO-8601 string)
- venue (string, e.g., "IBKR", "Bybit", "Paper")

---

### 3.2 Trade Parameters

- asset (string, symbol identifier)
- side (enumeration: "BUY" | "SELL")
- entry_price (numeric > 0)
- stop_loss_price (numeric > 0)
- position_size (numeric > 0)

All values represent the proposed trade at decision time.

---

### 3.3 Risk Parameters

- leverage_ratio (numeric >= 0)

Leverage must be provided as a snapshot value at decision time.

---

### 3.4 Portfolio Snapshot

- account_balance (numeric >= 0)
- current_open_positions (integer >= 0)
- total_exposure (numeric >= 0)
- daily_pnl (numeric, can be negative)

All values represent snapshot state at decision time.

- **account_balance**: Current account equity
- **current_open_positions**: Number of open positions before this decision
- **total_exposure**: Notional exposure after applying this decision, or provided snapshot
- **daily_pnl**: Profit/loss for current trading day

No implicit calculation allowed in v1.0.

---

## 4. Optional Fields

### 4.1 Policy Hint

- policy_hint (string, optional)

Optional field for runtime policy selection.
This field is NOT enforced by the validator and serves as metadata only.

---

## 5. Prohibited Fields

The Trading Decision Envelope MUST NOT contain:

- Strategy signal metadata
- Technical indicators
- ML model outputs or feature vectors
- Free-text justification
- AI interpretation fields
- Document references
- Override flags

---

## 6. Deterministic Integrity

The Trading Decision Envelope MUST:

- Be deterministically serialized
- Be hashed before validation
- Include the hash in the validation output

---

## 7. Structural Failure Conditions

STRUCTURAL_INVALID occurs if:

- Required fields are missing
- Field types are invalid
- side is outside allowed enumeration ("BUY" | "SELL")
- Numeric fields violate domain constraints (e.g., entry_price <= 0)
- Integer fields are not integers (e.g., current_open_positions)

If STRUCTURAL_INVALID, policy validation MUST NOT start.

---

## 8. Validation Scope

This envelope structure is sufficient to validate:

1. Max risk per trade (derived from position_size, entry_price, stop_loss_price)
2. Max open positions (current_open_positions constraint)
3. Max total exposure (total_exposure constraint)
4. Daily loss kill switch (daily_pnl threshold)
5. Leverage cap (leverage_ratio constraint)

---

## 9. Versioning

Changes to this structure require:

- New contract version
- No retroactive impact
- Explicit version bump
