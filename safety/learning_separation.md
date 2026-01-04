# SAPIANTA LEARNING SEPARATION POLICY

Status: NORMATIVE — LOCKED  
Version: v1.0  
Date: 2026-01-03  
Authority: Sapianta System Governance  
Dependency:
- SAPIANTA_CORE_CANON v1.0
- CORE_LAWS.md

This document defines the mandatory separation between
normative decision-making and learning mechanisms
within the Sapianta System.

---

## 0. Purpose of This Document

This document exists to:

- formally prohibit learning within the Sapianta Core,
- define where learning may exist in the system,
- prevent implicit or accidental feedback loops,
- ensure long-term determinism and safety.

Learning separation is a foundational safety invariant.

---

## 1. Fundamental Principle

**The Sapianta Core MUST NOT learn.**

This prohibition is absolute.

Learning is defined as any process that:

- modifies behavior based on past inputs or outcomes,
- adjusts decision logic through experience,
- optimizes responses over time,
- incorporates feedback into future decisions.

If any such process affects the Core,
the system is non-compliant.

---

## 2. Core Learning Prohibition

The following are strictly forbidden within the Core:

- parameter updates,
- weight adjustments,
- heuristic tuning,
- adaptive thresholds,
- feedback-based optimization,
- memory of past decisions,
- statistical aggregation of outcomes.

The Core must behave identically for identical inputs,
regardless of history.

---

## 3. Permitted Learning Domains

Learning MAY exist only outside the Core,
in explicitly designated system layers.

Permitted learning domains include:

- interaction layers (language adaptation, UX),
- recommendation or guidance modules,
- optimization of non-decisional workflows,
- analytics and monitoring components,
- external models not involved in Core decisions.

All learning must be:

- clearly scoped,
- explicitly declared,
- isolated from the Core.

---

## 4. No Feedback Into the Core

Under no circumstances may learning outputs:

- influence Core inputs,
- modify request representations,
- bias meaning evaluation,
- alter decision semantics,
- pre-filter or pre-judge requests.

The Core must receive inputs
without learned distortion.

---

## 5. Interaction Layer Constraints

The Interaction Layer:

- may learn conversational preferences,
- may adapt phrasing or explanations,
- may improve clarity or usability,

but MUST NOT:

- infer acceptability,
- predict Core outcomes,
- adjust behavior based on past Core decisions,
- simulate approval or rejection.

Learning in the Interaction Layer
must remain epistemically separate.

---

## 6. Builder and Self-Improvement Constraints

Builder mechanisms may:

- detect missing components,
- identify structural gaps,
- propose improvements,

but MUST NOT:

- autonomously modify the Core,
- update decision logic,
- optimize acceptance criteria,
- learn what “works” in decision terms.

Builder learning, if any,
is advisory only.

---

## 7. Prohibition of Shadow Learning

The following are explicitly forbidden system-wide:

- caching past decisions for inference,
- training models on Core outcomes,
- statistical pattern extraction from accept/reject ratios,
- reinforcement signals derived from Core behavior,
- indirect learning via sandbox simulations.

This includes implicit and emergent learning paths.

---

## 8. Detection and Enforcement

Any evidence of learning influence on the Core
constitutes a critical system violation.

The system must support:

- inspection of Core determinism,
- verification of stateless behavior,
- auditability of learning boundaries.

Violations require immediate rollback to NO-GO state.

---

## 9. Relationship to System State

Learning separation is a prerequisite for:

- transition from NO-GO to LIMITED,
- validation in LIMITED state,
- authorization of GO state.

If learning separation is compromised,
all higher system states are invalid.

---

## 10. Canonical Constraint

This policy is subordinate to:

- SAPIANTA_CORE_CANON v1.0
- CORE_LAWS.md

If any learning mechanism conflicts with the Canon,
the learning mechanism is invalid.

---

## 11. Minimal Conclusion

The Sapianta System may learn.

The Sapianta Core must never learn.

This separation preserves meaning,
prevents drift,
and protects authority.
