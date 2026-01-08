# Execution Dry-Run & Eligibility Evaluation Model

## Status
- Phase: FAZA 27B
- Type: Governance / Design-only
- Execution: Forbidden
- Evaluation mode: Read-only
- Lock state: NOT LOCKED

---

## 1. Purpose

This document defines how SAPIANTA evaluates **whether execution would be allowed**
*without performing execution*.

It answers the question:

> If this were to be executed, would it be permitted — and why?

The goal is to:
- enable safe pre-execution analysis
- expose blockers early
- prevent accidental execution
- make execution eligibility explainable

Dry-run evaluation is **mandatory** before any execution attempt.

---

## 2. Core Principle

A Dry-Run is a **simulation of execution eligibility**, not execution itself.

During dry-run:
- no side effects are allowed
- no state changes are allowed
- no external calls are allowed
- no permissions are consumed

Dry-run produces **an evaluation result**, never an action.

---

## 3. What Dry-Run Evaluates

Dry-run evaluation MUST check all normative layers:

1. Claim classification
2. Knowledge Anchor bindings
3. Anchor enforcement levels
4. Authority validity
5. Execution eligibility rules
6. Execution gate state

Failure at any layer stops evaluation immediately.

---

## 4. Dry-Run Input

Dry-run operates on an **Execution Intent**.

Required input:
- intent_id
- intent_type
- originating_claim
- bound anchors
- requesting authority
- target execution scope

If any required input is missing:
→ **R1 Refusal**

---

## 5. Evaluation Stages

Dry-run evaluation proceeds strictly in order:

### Stage 1 — Structural Validity
Checks:
- intent is well-formed
- intent type is known
- no forbidden fields present

Failure → R1 Refusal

---

### Stage 2 — Anchor Enforcement
Checks:
- all binding claims have anchors
- anchor versions match registry
- no E2 / E3 violations

Failure:
- E2 → R1 Refusal
- E3 → F1 Failure

---

### Stage 3 — Authority Verification
Checks:
- authority exists
- authority is valid
- authority scope matches intent

Failure → R2 Denial

---

### Stage 4 — Eligibility Rules
Checks:
- execution eligibility rules satisfied
- phase allows execution
- required gates exist

Failure → R1 Refusal or R2 Denial (depending on rule)

---

### Stage 5 — Gate Readiness
Checks:
- execution gate is defined
- gate is not locked
- gate preconditions satisfied

Failure → R2 Denial

---

## 6. Dry-Run Result

Dry-run MUST return exactly one result.

### Allowed results

- ELIGIBLE
- REFUSED
- DENIED
- FAILED

---

## 7. Dry-Run Result Structure

DryRunResult
├── result: ELIGIBLE | REFUSED | DENIED | FAILED
├── blocking_stage: stage identifier
├── reason_code: string
├── human_message: string
├── required_fixes: list (optional)
├── escalation_required: boolean

---

## 8. Prohibited Behavior

During dry-run the system MUST NOT:
- execute actions
- mutate state
- consume permissions
- bypass enforcement
- downgrade failures

Dry-run MUST be deterministic and repeatable.

---

## 9. Relationship to Execution

Dry-run:
- is mandatory before execution
- does not guarantee execution success
- only certifies *eligibility at this moment*

Execution without a successful dry-run is forbidden.

---

## 10. Closing Statement

Dry-run is the **last safe checkpoint**.

If execution will fail,
it must fail here — visibly, explainably, and harmlessly.

No dry-run → no execution.
