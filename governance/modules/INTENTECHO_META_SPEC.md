# INTENTECHO+META — REFERENCE MODULE SPECIFICATION (IE-META v0.1)
## Read-only · Non-interpreting · Non-executing · EXT-2 Reference

This document defines **IntentEcho+Meta** as the **first formally allowed extension**
over the IntentEcho baseline.

It exists solely to prove **architectural extensibility without semantic escalation**.

This is:
- not an implementation
- not an executable module
- not an operational capability

---

## 1. Module Identity

- **Name:** IntentEcho+Meta
- **Extends:** IntentEcho (IE-SPEC v0.1)
- **Type:** Reference / Meta-extension
- **Class:** Informational (read-only)
- **Execution:** None
- **Persistence:** None
- **Autonomy:** None

---

## 2. Purpose

> **IntentEcho+Meta augments pure intent reflection with
> strictly non-semantic, technical metadata describing the input string itself.**

Its purpose is to:
- demonstrate controlled horizontal extension
- preserve full semantic neutrality
- provide a test boundary for EXT-2 classification

---

## 3. Input Contract

- **Input:** Raw human-provided text
- **Processing:**
  - identical to IntentEcho
  - no filtering
  - no validation
  - no interpretation

The module does not assess meaning, safety, or correctness.

---

## 4. Output Contract

The output consists of **two strictly isolated sections**:

### 4.1 Echo Section
- Exact structural echo of the input
- Informationally equivalent to IntentEcho

### 4.2 Meta Section (EXT-2 Addition)

Only the following metadata fields are permitted:

- **`char_count`**  
  Total number of characters in the input

- **`contains_digits`**  
  Boolean indicator (true/false)

- **`contains_letters`**  
  Boolean indicator (true/false)

- **`contains_whitespace`**  
  Boolean indicator (true/false)

- **`hash`**  
  Deterministic, non-reversible technical hash of the input string

All fields describe **physical properties of the string**, not its meaning.

---

## 5. Strict Negative Specification

IntentEcho+Meta MUST NOT:

- infer intent, meaning, or purpose
- label language, topic, or sentiment
- classify or categorize content
- identify questions, commands, or requests
- summarize or paraphrase
- normalize, correct, or transform text
- explain metadata
- provide commentary
- ask follow-up questions
- propose next steps
- influence phases or WRITE-GATE
- generate or modify artifacts
- execute or simulate execution

If ambiguity exists → behavior is **forbidden**.

---

## 6. Relationship to IntentEcho

- Echo output must remain **unchanged**
- Meta output must be:
  - removable without semantic loss
  - non-influential to echo
  - strictly additive

IntentEcho+Meta does not replace IntentEcho.

---

## 7. Responsibility Model

- **Human:**  
  - owns intent, meaning, and consequences

- **System:**  
  - reflects input
  - reports string-level properties
  - holds no responsibility or judgment

---

## 8. Governance Alignment

This module is explicitly aligned with:

- **MMC-EXT-1 NO-GO ZONE**
- **Formal Phase Model (FPM)**
- **Chat Phase Signal Protocol (CPSP)**

It does **not** require:
- WRITE-GATE
- Build Scope Declaration
- BUILD phase

---

## 9. Role in the Architecture

IntentEcho+Meta serves as:

- the **canonical EXT-2 example**
- proof of safe extensibility
- boundary test between structure and semantics

Any further extension must justify divergence from this model.

---

## 10. Status

- Reference-only
- Spec-only
- EXT-2 certified
- No implementation
- No execution
- No autonomy
