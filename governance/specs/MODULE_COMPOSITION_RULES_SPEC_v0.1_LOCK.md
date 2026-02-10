# MODULE COMPOSITION RULES — SPECIFICATION v0.1
## (SAPIANTA · Self-Build Module System)

STATUS: DRAFT → LOCK-READY  
PHASE: Specification — Module Composition Rules  
SCOPE: Artifact-level composition semantics  
NORMATIVE LEVEL: Read-only specification  
COMPATIBILITY: Guard Layer v0.1 (FROZEN)

---

## 1. PURPOSE

This document defines the **canonical rules for composing modules** within the SAPIANTA Self-Build Module System.

Composition governs:
- how modules may reference one another
- how meaning is combined
- how boundaries are preserved

This specification does **not** define execution, orchestration, or runtime behavior.

---

## 2. COMPOSITION PRINCIPLE

Module composition is:
- **explicit**, never implicit
- **referential**, never incorporative
- **acyclic**, by default
- **artifact-safe**, preserving immutability

Composition combines **interpretation contexts**, not executable behaviors.

---

## 3. COMPOSITION UNITS

The basic unit of composition is a **module reference**.

A module reference:
- identifies a released module
- declares the purpose of reference
- specifies the interface used

References do not import internal structure.

---

## 4. COMPOSITION MODES

### 4.1 Interpretive Composition

One module may be **interpreted in light of** another.

Rules:
- No content mutation
- No priority inversion
- Interpretation scope MUST be declared

---

### 4.2 Declarative Dependency

A module may declare reliance on concepts defined in another module.

Rules:
- Dependency MUST be explicit
- No transitive assumption without declaration
- Dependencies do not imply inheritance

---

### 4.3 Aggregative Composition

Multiple modules may be grouped for joint inspection.

Rules:
- Aggregation does not create a new module
- Order does not imply precedence
- Conflicts MUST be surfaced, not resolved implicitly

---

## 5. FORBIDDEN COMPOSITION PATTERNS

The following are explicitly forbidden:

- Implicit dependency
- Cyclic reference (direct or indirect)
- Content override
- Semantic shadowing
- Runtime coupling

Violation invalidates release eligibility.

---

## 6. COMPOSITION BOUNDARY RULES

- Each module retains its own schema identity
- No composed structure may appear as a single artifact
- Composition MUST NOT obscure audit provenance

---

## 7. CONFLICT DECLARATION

If two modules introduce conflicting concepts:
- the conflict MUST be declared
- no automatic resolution is permitted
- resolution occurs outside the composed artifacts

---

## 8. AUDITABILITY REQUIREMENTS

Composed views MUST allow:
- independent inspection of each module
- traceability of references
- clear origin attribution

Composition MUST NOT reduce audit interpretability.

---

## 9. NON-GOALS

This specification excludes:
- execution order
- orchestration logic
- dependency resolution algorithms
- optimization strategies

---

## 10. LOCK READINESS STATEMENT

This document:
- preserves module immutability
- introduces no new authority
- aligns with frozen Guard Layer
- maintains audit transparency

Upon approval, this specification is suitable for **LOCK** and completes the core module composition semantics.

---

END OF SPECIFICATION
