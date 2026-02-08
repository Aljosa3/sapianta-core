# WRITE-INTENT — v1.0 (LOCK)

## Status
LOCKED — canonical intent declaration

## Purpose
WRITE-INTENT defines the mandatory, explicit declaration
required before any promotion or write operation
from staging (`out/`) into a canonical repository domain.

WRITE-INTENT exists to make intent:
- explicit
- human-visible
- auditable
- non-implicit

---

## 1. Definition

WRITE-INTENT is a declarative artifact.
It expresses a request to perform a controlled write
across a governance boundary.

WRITE-INTENT is NOT:
- a command
- an execution instruction
- a permission by itself

It is a prerequisite for WRITE-GATE evaluation.

---

## 2. Mandatory Properties

A valid WRITE-INTENT MUST explicitly specify:

1. Artifact identifier  
   (logical name of the module or artifact)

2. Source path  
   (exact path under `out/`)

3. Target canonical domain  
   (e.g. `modules/`)

4. Intended operation  
   (promotion, not mutation)

5. Actor  
   (human or governed system initiating the intent)

Omission of any property invalidates the intent.

---

## 3. Scope of Authority

WRITE-INTENT:
- authorizes evaluation
- does NOT authorize execution

Only WRITE-GATE may decide execution legitimacy.

WRITE-INTENT has no effect without WRITE-GATE.

---

## 4. Explicitness Requirement

WRITE-INTENT MUST be:
- explicit
- unambiguous
- human-readable
- single-purpose

Implicit, inferred, or contextual intent is forbidden.

---

## 5. Immutability

Once issued:
- a WRITE-INTENT MUST NOT be modified
- changes require a new WRITE-INTENT
- supersession MUST be explicit

Intent mutation is forbidden.

---

## 6. One-to-One Mapping

Each WRITE-INTENT:
- refers to exactly one artifact
- refers to exactly one operation
- results in at most one WRITE-GATE decision

Batch or wildcard intents are forbidden.

---

## 7. Auditability

WRITE-INTENT MUST be traceable through:
- explicit declaration
- WRITE-GATE decision
- resulting commit (if ALLOW)

WRITE-INTENT is part of the audit chain.

---

## 8. Failure Semantics

Invalid WRITE-INTENT:
- MUST NOT be evaluated
- MUST result in immediate DENY
- MUST NOT trigger recovery logic

Silence is forbidden.

---

## 9. Governance Boundary

WRITE-INTENT defines the formal boundary
between intention and legitimacy.

No system component may bypass this boundary.

---

## END OF DOCUMENT
