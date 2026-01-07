# Reasoning Anchor Binding

## Status
- Phase: FAZA 23B
- Type: Governance / Design-only
- Applies to: Reasoning Layer
- Execution: Forbidden
- Binding state: Mandatory

---

## 1. Purpose

This document defines how **Knowledge Anchors are bound to reasoning outputs**
within the SAPIANTA system.

It answers the question:

> On what authority did the system reach this conclusion?

Reasoning without anchors is considered:
- non-binding
- unverifiable
- illegitimate

---

## 2. Mandatory Binding Rule

Every **reasoning conclusion** produced by the system MUST declare
at least one **Anchor Binding**.

This applies to:
- explanatory answers
- structural explanations
- boundary reasoning
- eligibility statements

There are **no exceptions**.

---

## 3. Binding Scope in Reasoning

Anchors MAY be attached to:

- the entire reasoning conclusion
- individual reasoning steps
- specific claims within the explanation

At least one anchor MUST apply to the **final conclusion**.

---

## 4. Anchor Binding Structure (Reasoning)

Each reasoning output MUST include:

- anchor_id
- anchor_version
- enforcement_level
- binding_scope
- justification

Bindings MUST conform to:
- Anchor Binding Model
- Knowledge Anchor Enforcement Levels

---

## 5. Missing or Invalid Binding

If a reasoning output:
- lacks anchor bindings
- references non-existent anchors
- uses implicit or inferred anchors

Then:

→ **E2 Refusal MUST be issued**

The system MUST NOT:
- generate a normal answer
- downgrade the refusal
- replace refusal with explanation

---

## 6. Multiple Anchors in Reasoning

A reasoning output MAY reference multiple anchors.

Rules:
- All anchors apply
- Highest enforcement level dominates
- Conflicts MUST be explicitly surfaced

Silent conflict resolution is forbidden.

---

## 7. Design-Time Constraint

This document:
- defines binding requirements only
- performs no evaluation
- triggers no execution
- introduces no permissions

Runtime enforcement is defined elsewhere.

---

## 8. Why This Matters

Reasoning without anchors is opinion.

Anchored reasoning is law-bound logic.

This distinction is fundamental.

---

## 9. Closing Statement

The system is not allowed to think anonymously.

Every conclusion must declare:
- **what rule it follows**
- **why that rule applies**

No anchor → no authority.
