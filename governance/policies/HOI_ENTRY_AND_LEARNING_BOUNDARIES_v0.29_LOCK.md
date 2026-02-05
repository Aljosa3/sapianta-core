# 🔒 HOI Entry & Learning Boundaries — v0.29 (LOCK)

## Status
LOCKED — normative specification  
No runtime behavior defined  
No implementation implied

---

## Purpose

This document establishes the **Human Orientation Interface (HOI)** as the mandatory
entry layer for module self-construction in SAPIANTA and defines **strict boundaries
for learning and language refinement**.

HOI exists to **protect human attention and responsibility**, not to optimize speed,
comfort, or decision outcomes.

Learning is allowed **only** where it improves orientation and understanding,
never where it replaces or predicts decisions.

---

## Scope

### Included
- HOI Entry Flow
- Criteria for the first Canonical Decision Record (CDR)
- HOI stop conditions (when the system must stop asking questions)
- Learning boundaries
- HOI language refinement boundaries

### Explicitly Excluded
- No chat / UI design
- No runtime logic
- No validator logic
- No WRITE-GATE or WRITE-INTENT changes
- No UX or engagement optimization
- No silent prompt replacement

---

## A. HOI Entry Flow

### A1. Activation
HOI is activated for **every request** to build or modify a module.

### A2. Initial Conditional Question
The first HOI question MUST be conditional:

> “Do you already have a well-defined idea of this module,  
> or is the idea still open and something you want to develop?”

### A3. Path Split
- **Defined idea** → user describes intent in own words; questions are asked only
  where consequences are likely understood.
- **Open idea** → system offers paths:
  - common patterns
  - joint clarification
  - iterative minimal start  
  No path is recommended as superior.

### A4. Non-Locking Principle
HOI MUST NOT force narrowing of intent while all decisions remain reversible.

---

## B. Criteria for First CDR

A first Canonical Decision Record is legitimate only when ALL are true:
1. Intent is stable (what is to be achieved, not how)
2. Consequences are understood at least at a coarse level
3. Responsibility is explicit

HOI MUST NOT generate CDRs.  
HOI MAY ONLY recognize when a CDR becomes legitimate.

---

## C. Stop Conditions (HOI Silence)

HOI MUST stop asking questions when:
- further questions reduce clarity rather than increase it
- Attention Budget is exhausted (~10 consecutive orientation questions)
- the user remains legitimately uncertain with no irreversible risk

Upon stopping:
- safest default constraints apply
- no implicit decisions are made
- return to HOI remains possible at any time

---

## D. Learning Boundaries

### D1. When Learning Is Allowed
- Only **after** a CDR exists
- Never during orientation
- Never in real time

### D2. What May Be Learned
- which questions or sequences led to more stable CDRs
- where fewer REPLACE / DEPRECATE actions occurred due to misunderstanding
- which explanations reduced later regret

### D3. What Is Forbidden
- optimization for speed or comfort
- skipping or suppressing questions
- predicting user decisions
- reducing signal strength

### D4. Core Rule
Learning may improve **questions**, never **answers**.
Learning may improve **orientation**, never **decisions**.

---

## E. HOI Language Refinement Boundaries

### E1. Purpose
To improve **clarity and understandability** of HOI questions when evidence shows
frequent misunderstanding — without altering meaning or decision weight.

### E2. Allowed
- reformulation for clarity
- added explanations or examples
- improved explanatory ordering

### E3. Forbidden
- semantic change
- narrowing or expanding decision space
- suggesting a correct answer
- reducing cognitive friction
- silent replacement of questions

### E4. Versioning
- HOI questions are **versioned normative artifacts**
- old versions remain accessible
- new versions require explicit introduction (LOCK)
- no silent migration

### E5. Timing
Language refinement is post-hoc only.
Never during an active user dialogue.

### E6. Guarantee
SAPIANTA does not replace questions.
It introduces new versions while preserving responsibility.

---

## F. Non-Conflict Guarantees

- No interaction with WRITE-GATE or WRITE-INTENT
- No impact on validator or state machine
- No implicit transitions
- No normalization of risk

---

## G. Success Metrics (Anti-UX)

Success is measured over time, not per session:
- fewer misunderstood initial CDRs
- fewer silent desires to “just fix it”
- more explicit REPLACE instead of edits
- higher user trust in their own decisions

---

## Lock Statement

HOI in v0.29 is an **orientation layer**.
Learning is **retrospective and constrained**.
Language refinement is **versioned, explicit, and non-silent**.

This document defines permanent constraints.
