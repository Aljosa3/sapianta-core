# SAPIANTA CORE — SYSTEM STATE DECLARATION

Status: ACTIVE — NO-GO  
Version: v1.0  
Date: 2026-01-03  
Authority: Sapianta Core Governance  
Dependency: SAPIANTA_CORE_CANON v1.0

This document declares the operational state of the Sapianta Core.
It does not define meaning.
It defines permission to operate.

---

## 0. Purpose of This Document

This document exists to:

- explicitly declare whether the Sapianta Core may be executed,
- prevent premature or implicit activation,
- provide a formal gate between normative definition and implementation,
- ensure that no code execution occurs by accident or assumption.

This document is binding.

---

## 1. Current System State

The current state of the Sapianta Core is:

**NO-GO**

This means:

- the Core MUST NOT be executed,
- the Core MUST NOT process live requests,
- the Core MUST NOT be embedded in any running system,
- the Core MUST NOT be connected to any interaction layer,
- the Core MUST NOT influence decisions in real or simulated environments.

Any execution of the Core in NO-GO state is a violation.

---

## 2. Meaning of NO-GO State

The NO-GO state signifies that:

- the Canon is defined,
- the Laws are defined,
- the system is structurally prepared,

but:

- implementation is not yet authorized,
- correctness has not yet been proven,
- safety boundaries are not yet enforced in code.

NO-GO is a **protective state**, not an error state.

---

## 3. Prohibited Activities in NO-GO

While the system is in NO-GO state, the following are strictly prohibited:

- executing any Core logic,
- implementing runtime decision pipelines,
- integrating the Core with chat, UI, or LLM systems,
- simulating Core behavior for functional use,
- performing tests that resemble live decision-making,
- collecting data through Core-mediated flows.

Documentation, design, and static analysis are permitted.

---

## 4. Allowed Activities in NO-GO

The following activities are explicitly allowed:

- writing and refining normative documentation,
- implementing static code skeletons without execution,
- preparing test vectors without evaluation,
- defining interfaces without activation,
- reviewing compliance with the Canon and Core Laws.

No activity may produce a decision outcome.

---

## 5. Transition States

The Sapianta Core recognizes three system states:

### 5.1 NO-GO

- No execution permitted.
- No decision logic active.
- Default and safest state.

---

### 5.2 LIMITED

LIMITED state permits:

- controlled execution in isolated environments,
- deterministic test inputs only,
- no user-facing interaction,
- no learning, storage, or feedback loops.

LIMITED is for validation only.

---

### 5.3 GO

GO state permits:

- full Core execution,
- integration with compliant interaction layers,
- live decision processing under Canon constraints.

GO state does not permit learning or self-modification.

---

## 6. Conditions for Transition to LIMITED

A transition from NO-GO to LIMITED is permitted only if all of the following are true:

1. `CANON.md` is complete and locked.
2. `CORE_LAWS.md` is complete and accepted.
3. `sandbox/__concept__.md` is complete.
4. `safety/learning_separation.md` is complete.
5. A formal transition decision is recorded in governance logs.
6. Human authority explicitly authorizes the transition.

Absent any condition, the transition is invalid.

---

## 7. Conditions for Transition to GO

A transition from LIMITED to GO is permitted only if:

- deterministic correctness is demonstrated,
- no invariant violations are observed,
- no execution leaks are detected,
- governance approval is recorded,
- rollback to NO-GO remains possible.

GO is reversible.

---

## 8. Enforcement Principle

System state is authoritative.

No component may:

- infer permission,
- assume readiness,
- bypass declared state.

State must be explicitly checked and respected.

---

## 9. Auditability

All state transitions:

- must be auditable,
- must be logged as events,
- must not expose content or decisions.

State changes are governance actions, not system behavior.

---

## 10. Minimal Conclusion

The Sapianta Core does not become active by being implemented.

It becomes active only by permission.

Until such permission is granted, the system remains:

**NO-GO**
