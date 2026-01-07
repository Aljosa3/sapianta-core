# Planning Anchor Binding

## Status
- Phase: FAZA 23B
- Type: Governance / Design-only
- Applies to: Planning Layer
- Execution: Forbidden
- Binding state: Mandatory

---

## 1. Purpose

This document defines how **Knowledge Anchors are bound to planning outputs**
within the SAPIANTA system.

It answers the question:

> On what authority is this plan allowed to exist?

A plan without anchors is:
- speculative
- non-binding
- ineligible for execution

---

## 2. Mandatory Binding Rule

Every **plan** produced by the system MUST declare
one or more **Anchor Bindings**.

This applies to:
- conceptual plans
- structural plans
- execution preparation plans
- boundary plans

There are **no exceptions**.

---

## 3. Binding Scope in Planning

Anchors MAY be attached to:

- the entire plan
- individual plan steps
- execution eligibility boundaries

At least one anchor MUST apply to the **entire plan**.

---

## 4. Anchor Binding Structure (Planning)

Each plan MUST include:

- anchor_id
- anchor_version
- enforcement_level
- binding_scope
- justification

Bindings MUST conform to:
- Anchor Binding Model
- Knowledge Anchor Enforcement Levels

---

## 5. Planning Without Execution

Plans MAY describe execution conceptually.

Plans MUST NOT:
- trigger execution
- imply permission
- bypass execution gates

Execution eligibility is evaluated elsewhere.

---

## 6. Missing or Invalid Binding

If a plan:
- lacks anchor bindings
- references non-existent anchors
- uses inferred or implicit anchors

Then:

→ **E2 Refusal MUST be issued**

The system MUST NOT:
- generate a valid plan
- downgrade refusal to explanation
- auto-correct bindings

---

## 7. Multiple Anchors in Planning

A plan MAY reference multiple anchors.

Rules:
- All anchors apply
- Highest enforcement level dominates
- Conflicts MUST be explicitly surfaced

Silent conflict resolution is forbidden.

---

## 8. Design-Time Constraint

This document:
- defines planning legitimacy only
- performs no execution
- introduces no permissions
- enforces no runtime behavior

---

## 9. Why This Matters

Planning is the bridge between thought and action.

Unanchored planning is dangerous fiction.

Anchored planning is controlled intent.

---

## 10. Closing Statement

No plan is neutral.

Every plan must declare:
- **what law allows it**
- **why it is permitted**

No anchor → no plan.
