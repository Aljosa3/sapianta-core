# MODULE FORMAT — SPECIFICATION v0.1
## (SAPIANTA · Self-Build Module System)

STATUS: DRAFT → LOCK-READY  
PHASE: Specification — Module Format  
SCOPE: Concrete, inspectable artifact structure  
NORMATIVE LEVEL: Read-only specification  
COMPATIBILITY:  
- Module Spec v0.1 (LOCKED)  
- HOI Build Flow v0.1 (LOCKED)  
- Guard Layer v0.1 (FROZEN)

---

## 1. PURPOSE

This document defines the **canonical concrete format** of a SAPIANTA module artifact.

It specifies:
- how a module is physically structured as an artifact
- mandatory sections and ordering
- format constraints ensuring inspectability and auditability

This specification **binds the abstract schema to a concrete artifact form**, without introducing execution semantics.

---

## 2. FORMAT PRINCIPLES

The module format is:

- **static** — no dynamic fields
- **self-contained** — no external dependencies
- **human-readable** — primary inspection by humans
- **machine-parseable** — deterministic structure
- **immutable after release**

The format exists to support **audit, review, and composition**, not execution.

---

## 3. ARTIFACT FORM

A module is represented as a **single artifact unit**, consisting of:

- a primary structured document
- optional attached evidence references (by pointer only)

The artifact MUST be representable as:
- a single canonical document
- or a single directory treated as an atomic unit

Mixed or fragmented representations are forbidden.

---

## 4. CANONICAL SECTIONS (ORDERED)

The following sections MUST appear in the artifact **in this exact order**:

1. Identity  
2. Intent  
3. Specification Core  
4. Assumptions & Limits  
5. Interfaces  
6. Lifecycle Evidence  
7. Audit & Provenance Metadata  

Reordering or omission invalidates the artifact.

---

## 5. SECTION FORMAT RULES

### 5.1 Identity

- Fixed, explicit identifiers
- Version declared once
- No derived or computed fields

---

### 5.2 Intent

- Human-readable normalized intent
- Explicit scope statement
- Explicit constraint acknowledgement reference

---

### 5.3 Specification Core

- Structured, declarative content
- No executable instructions
- No references to runtime behavior

---

### 5.4 Assumptions & Limits

- Explicit assumptions list
- Explicit exclusions
- Explicit non-goals

---

### 5.5 Interfaces

- Interpretive Interface declaration
- Compositional Interface declaration
- Audit Interface declaration

No control or execution interface permitted.

---

### 5.6 Lifecycle Evidence

- Current lifecycle state
- References to prior state evidence
- Transition markers (referential only)

---

### 5.7 Audit & Provenance Metadata

- Build authorization reference
- Integrity reference
- Review posture markers

Metadata MUST be sufficient for independent reconstruction.

---

## 6. FORMAT CONSTRAINTS

The artifact format MUST ensure:

- no hidden sections
- no implicit defaults
- no computed values
- no external file inclusion at read-time

All meaning MUST be explicit in the artifact.

---

## 7. FORMAT STABILITY

- Once released, format is immutable
- Format changes require a new format specification version
- Artifacts bound to v0.1 MUST NOT be reinterpreted under future formats

---

## 8. SEPARATION FROM IMPLEMENTATION

This specification:
- does not define JSON, YAML, or other encodings
- does not define validation logic
- does not define tooling behavior

Encoding choices are deferred to implementation phases.

---

## 9. NON-GOALS

This specification excludes:
- compression
- encryption
- signing mechanisms
- storage backends
- transmission protocols

---

## 10. LOCK READINESS STATEMENT

This document:
- completes the normative definition of the module artifact
- introduces no execution or runtime semantics
- preserves audit primacy and immutability

Upon approval, this specification is suitable for **LOCK** and completes **Module System v0.1** at the format level.

---

END OF SPECIFICATION
