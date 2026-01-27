# LLM ROLE CONTRACT v0.1 — SAPIANTA

STATUS: ACTIVE
VERSION: v0.1
DATE: 2026-01-27

---

## 1. PURPOSE

This document defines the permitted and prohibited roles of Large Language Models (LLMs)
within the SAPIANTA system.

The objective is to ensure:
- human legitimacy at all times,
- deterministic system behavior,
- auditability,
- prevention of implicit or emergent AI authority.

LLMs are treated strictly as subordinate tools, never as decision-makers or agents.

---

## 2. AUTHORITY MODEL

- Human Operator Interface (HOI) is the sole source of legitimacy.
- LLMs possess **no authority**, explicit or implicit.
- LLM outputs are non-binding and non-executable by default.

No system component may delegate authority to an LLM.

---

## 3. PERMITTED LLM ROLES

LLMs may only be used in the following roles:

### 3.1 Explain-on-Demand

LLMs may generate natural language explanations of:
- existing `options[]`,
- existing `meta` fields,
- already-produced system outputs.

Constraints:
- No creation of new options
- No ranking or recommendation
- No introduction of new semantics

Explain-on-Demand is strictly post-hoc and read-only.

---

### 3.2 Assistive Generation Within Modules (UC-x)

LLMs may be used inside domain modules as assistive generators, under the following conditions:
- Output is treated as a suggestion, not a decision
- Output is filtered through deterministic rules
- Output is validated against module constraints
- Output requires explicit HOI confirmation

If an LLM fails or produces invalid output, the module must remain functional.

---

### 3.3 Preprocessing / Postprocessing

LLMs may be used for:
- summarization of human-provided input
- language normalization
- translation
- formatting

These uses must not alter decision semantics or introduce new intent.

---

## 4. PROHIBITED LLM ROLES

LLMs must **never** be used as:

- decision-makers
- goal setters
- optimizers
- ranking engines
- autonomous agents
- system orchestrators
- state holders
- memory stores
- long-term planners

LLMs must not:
- trigger actions
- escalate privileges
- modify system state
- bypass HOI
- interact directly with audit mechanisms

---

## 5. ARCHITECTURAL CONSTRAINTS

- LLMs must not be directly accessible from Chat UI components.
- LLMs must not produce canonical system outputs.
- All LLM interaction points must be explicitly declared in module boundaries.
- LLMs must be replaceable without affecting system correctness.

---

## 6. AUDIT AND TRACEABILITY

- LLM outputs are not considered canonical records.
- Any LLM usage must be traceable via surrounding module or explain-on-demand context.
- The audit system records system outputs, not LLM reasoning.

---

## 7. FAILURE MODE REQUIREMENTS

In the event of:
- LLM unavailability
- malformed output
- unexpected behavior

The system must:
- degrade gracefully
- preserve HOI authority
- continue operating without LLM dependency

---

## 8. CHANGE POLICY

Any change to this contract requires:
- new contract version (v0.2+)
- explicit INIT / LOCK / COMPLETE governance cycle

This contract is binding for all current and future SAPIANTA modules.

---

CONTRACT CONFIRMED.
