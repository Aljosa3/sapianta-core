# TRADING_DECISION_TO_INTENT_SPEC_v0.1

## Purpose

Define a deterministic, governance-controlled transformation from:

    TRADING_DECISION_PROPOSED
to:
    TRADING_INTENT_CREATED

No side effects. No enrichment. No external data.

---

## Deterministic Mapping Rules

### 1. Field Mapping (1:1)

| Decision Field | Intent Field |
|---------------|--------------|
| decision_id  | decision_id |
| action       | action |
| symbol       | symbol |
| timeframe    | timeframe |

All mapped fields must be preserved without modification.

---

### 2. Intent ID Derivation Rule

intent_id MUST be deterministically derived as:

    intent_id = "INTENT_" + decision_id

No randomness.
No hashing.
No timestamp usage.

---

### 3. Optional Fields

If decision contains:
- rationale

Intent MAY include:
- notes = rationale

No other enrichment allowed.

---

### 4. Prohibited Transformations

The following are forbidden:

- Changing action value
- Normalizing symbol case
- Modifying timeframe
- Injecting portfolio logic
- Injecting position sizing
- Injecting execution metadata

---

### 5. Version Binding

This spec is valid only with:

- TRADING_DECISION_CONTRACT_v0.1
- TRADING_INTENT_CONTRACT_v0.1

Any contract version change invalidates this spec version.

---

## Determinism Guarantee

Given identical Decision input,
the resulting Intent output MUST be identical.
