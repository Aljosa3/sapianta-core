# CLAIM_CLASSIFICATION_MODEL

## Status
- Phase: FAZA 24A
- Type: Governance / Design-only
- Execution: Forbidden
- Classification state: Mandatory
- Lock state: NOT LOCKED

---

## 1. Purpose

This document defines the **Claim Classification Model**.

It answers the question:

> What kind of statement is the user making — before any reasoning,
> planning, or execution is attempted?

Claim Classification exists to:
- prevent premature reasoning
- prevent accidental execution
- route inputs into lawful system paths
- explain refusals deterministically

Classification is **non-evaluative**.
Classification is **non-executing**.
Classification is **non-authoritative**.

---

## 2. Core Principle

Every user input MUST be classified
**before** it can enter:
- reasoning
- planning
- execution eligibility

No classification → no processing.

---

## 3. Claim Types

The system recognizes exactly **five** claim types.

No other claim types may be inferred.

| Code | Claim Type            | Description |
|-----:|----------------------|-------------|
| C0   | Informational        | Requests for descriptive information |
| C1   | Advisory             | Requests for suggestions or opinions |
| C2   | Binding              | Claims that assert system state, legality, or readiness |
| C3   | Planning             | Requests to construct plans or structures |
| C4   | Execution Attempt    | Attempts to cause execution or state change |

---

## 4. Claim Type Definitions

### 4.1 C0 — Informational

**Meaning:**
- Descriptive questions
- No authority implied
- No legality implied

**Examples:**
- “Kako je zasnovana arhitektura sistema?”
- “Kaj je Knowledge Anchor?”

**Allowed flow:**
→ Informational response  
→ No anchor required

---

### 4.2 C1 — Advisory

**Meaning:**
- Requests for recommendations
- Hypothetical or opinion-based

**Examples:**
- “Kaj bi bilo smiselno narediti naprej?”
- “Kako bi lahko izboljšali ta del?”

**Allowed flow:**
→ Advisory response  
→ Anchors optional (E0/E1 only)

---

### 4.3 C2 — Binding

**Meaning:**
- Asserts or queries legality, validity, readiness, or permission
- Implies authority

**Examples:**
- “Ali je sistem pripravljen na execution?”
- “Ali je ta faza zaključena?”
- “Kateri deli so stabilni?”

**Required:**
- Explicit Knowledge Anchor binding

**Default behavior if missing anchor:**
→ **E2 Refusal**

---

### 4.4 C3 — Planning

**Meaning:**
- Requests construction of structured plans
- No execution implied

**Examples:**
- “Kako bi bil strukturiran execution modul?”
- “Pripravi fazni načrt.”

**Required:**
- Planning Anchor Binding

**Execution:**
- Forbidden (design-only)

---

### 4.5 C4 — Execution Attempt

**Meaning:**
- Attempts to trigger execution or system change
- Explicit or implicit

**Examples:**
- “Izvedi to.”
- “Aktiviraj modul.”
- “Zapiši v sistem.”

**Behavior:**
→ Immediate **E3 Fail**  
→ No reasoning  
→ No explanation beyond failure notice

---

## 5. Classification Output

Classification produces a **Claim Classification Record**.

Canonical fields:

ClaimClassification
├── claim_type: C0 | C1 | C2 | C3 | C4
├── detected_scope: reasoning | planning | execution
├── binding_required: true | false
├── execution_allowed: false (always in FAZA 24A)
├── notes: string (optional)

---

## 6. Prohibited Behavior

The system MUST NOT:
- answer before classification
- downgrade a claim type
- infer missing anchors
- reinterpret execution attempts as planning
- classify ambiguously

If classification is ambiguous:
→ Default to **C2 (Binding)**

---

## 7. Design-Time Constraint

This model:
- performs no reasoning
- performs no planning
- performs no execution
- emits no answers

It only labels the input.

---

## 8. Closing Statement

Classification is the **first gate of law**.

If intent is unclear:
- authority is assumed
- safeguards activate
- silence is replaced by refusal

No classification → no legitimacy.
