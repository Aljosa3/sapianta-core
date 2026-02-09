# MMC-EXT-1 — ABSOLUTE NO-GO ZONE
## Semantic Boundary Introduction (Prohibition Specification)

This document defines the **absolute, non-negotiable boundary** for all SAPIANTA modules operating under **MMC-EXT-1**.

Crossing any rule in this document means the module is **no longer EXT-1 compliant**, regardless of intent or implementation quality.

---

## 1. Semantic Prohibitions

### 1.1 No Interpretation
A module MUST NOT:
- interpret meaning
- infer intent
- select between possible meanings
- summarize content

If the output reveals *what the input means*, this boundary is violated.

---

### 1.2 No Semantic Categorization
A module MUST NOT:
- classify input as request / command / question / problem
- assign semantic types
- group inputs by meaning

Only the **existence** of semantic ambiguity may be declared — never its nature.

---

## 2. Decision Prohibitions

### 2.1 No Selection
A module MUST NOT:
- choose an interpretation
- suggest a preferred meaning
- imply correctness of any option

Where multiple meanings exist, the module must remain silent.

---

### 2.2 No Preference
A module MUST NOT:
- evaluate correctness or quality
- use normative language
- imply error, risk, or validity

Words implying judgment are forbidden.

---

## 3. Action Prohibitions

### 3.1 No Action Suggestion
A module MUST NOT:
- suggest next steps
- advise human action
- present options as actions

Even soft suggestions constitute a violation.

---

### 3.2 No Flow Triggering
A module MUST NOT:
- trigger subsequent modules
- create continuation conditions
- implicitly request a response

An EXT-1 module is terminal.

---

## 4. Responsibility Prohibitions

### 4.1 No Semantic Authority
A module MUST NOT:
- act as arbiter of meaning
- confirm or reject interpretations
- resolve ambiguity

Semantic authority remains exclusively human.

---

### 4.2 No Responsibility Transfer
A module MUST NOT:
- reduce human responsibility
- imply system understanding
- create the impression of system-level decision-making

If the human does not decide, nothing happens.

---

## 5. Structural Prohibitions

### 5.1 No State
A module MUST NOT:
- store semantic boundaries
- remember previous inputs
- compare with past cases

Each interaction is isolated.

---

### 5.2 No Composition
A module MUST NOT:
- participate in pipelines
- produce machine-consumable outputs
- serve as an intermediate processing step

EXT-1 modules are non-composable.

---

## 6. Language Prohibitions

### 6.1 No Normative Language
Outputs MUST NOT:
- suggest correctness
- imply intent
- create expectations

Only description, marking, and boundary indication are allowed.

---

### 6.2 No Questions
A module MUST NOT:
- ask questions
- request clarification
- prompt explanation

Questions imply action and are forbidden.

---

## 7. Forward-Boundary Prohibition

### 7.1 No Implicit EXT-2
A module MUST NOT:
- prepare interpretation
- partially explain meaning
- hint at future processing

EXT-1 has no knowledge of what comes next.

---

## 8. Compliance Litmus Test

A module is **NOT EXT-1 compliant** if any of the following are true:
- meaning can be inferred from output
- action can be derived from output
- a decision is implied
- continuation is possible without human intervention

If any answer is YES — the module is outside EXT-1.

---

## 9. Boundary Statement

> EXT-1 is the point where the system may state:  
> “Meaning begins here — and my authority ends here.”

---

Status:
- Absolute boundary
- No implementation permission
- No production implication
- Governance-enforced
