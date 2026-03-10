# SAPIANTA Promotion Gate v1.0

## Purpose

Promotion Gate controls the transition of research artifacts
into runtime-eligible strategies.

Research outputs must pass evaluation before being allowed
into the Decision Spine.

This prevents unstable or unsafe models from affecting
runtime decisions.

---

## Promotion Pipeline

experiment_result
↓
artifact_registry
↓
evaluation
↓
promotion_gate
↓
approved_strategy
↓
runtime

---

## Promotion Decision

Promotion decisions must include:

artifact_id
artifact_type
evaluation_result
promotion_result
timestamp
review_context

---

## Promotion Outcomes

Allowed outcomes:

APPROVED
REJECTED
REQUIRES_REVIEW

---

## Governance Rules

Promotion Gate must be:

deterministic
auditable
recorded in artifact registry