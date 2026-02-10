# HOI BUILD FLOW — SPECIFICATION v0.1
## (SAPIANTA · Human Orientation Interface)

STATUS: DRAFT → LOCK-READY  
PHASE: Specification — HOI Build Flow  
SCOPE: Normative flow for module self-build via HOI  
NORMATIVE LEVEL: Read-only specification  
COMPATIBILITY: Module Spec v0.1 (LOCKED), Guard Layer v0.1 (FROZEN)

---

## 1. PURPOSE

This document defines the **canonical build flow** through which the Human Orientation Interface (HOI)
mediates the construction of a SAPIANTA module.

The build flow specifies:
- sequential stages of interaction
- decision and rejection points
- responsibility boundaries
- transition conditions toward artifact existence

This specification defines **how a module is built**, not what it contains.

---

## 2. HOI BUILD FLOW PRINCIPLE

HOI build flow is:
- **guided**, not free-form
- **constraint-driven**, not generative-first
- **stage-gated**, not continuous
- **terminable**, not forced to completion

HOI may refuse to proceed at any stage.

---

## 3. BUILD FLOW STAGES (CANONICAL)

HOI-mediated module construction progresses through the following stages:

1. Entry  
2. Intent Articulation  
3. Scope Delimitation  
4. Constraint Acknowledgement  
5. Structural Confirmation  
6. Construction Authorization  
7. Artifact Construction  
8. HOI Exit

Stages are **strictly ordered**.

---

## 4. STAGE DEFINITIONS

### 4.1 Entry

Purpose:
- Establish build intent
- Confirm non-execution expectations

HOI responsibilities:
- Clarify that output is an artifact
- Confirm absence of runtime intent

Exit conditions:
- User confirms artifact-only goal

Failure conditions:
- User requests execution, automation, or control

---

### 4.2 Intent Articulation

Purpose:
- Capture human purpose in natural language

HOI responsibilities:
- Elicit explicit intent
- Normalize ambiguous language
- Reject over-broad goals

Exit conditions:
- Intent is explicit and bounded

Failure conditions:
- Vague, conflicting, or implicit intent

---

### 4.3 Scope Delimitation

Purpose:
- Define boundaries of the intended module

HOI responsibilities:
- Surface inclusions and exclusions
- Prevent scope creep
- Align with Module Architecture

Exit conditions:
- Clear scope boundaries acknowledged

Failure conditions:
- Unlimited or shifting scope

---

### 4.4 Constraint Acknowledgement

Purpose:
- Bind user intent to system invariants

HOI responsibilities:
- Present non-negotiable invariants
- Require explicit acknowledgement

Exit conditions:
- Constraints accepted without exception

Failure conditions:
- Attempts to bypass or weaken invariants

---

### 4.5 Structural Confirmation

Purpose:
- Confirm schema-level structure

HOI responsibilities:
- Present required schema sections
- Validate user understanding

Exit conditions:
- Structural completeness confirmed

Failure conditions:
- Missing or rejected required sections

---

### 4.6 Construction Authorization

Purpose:
- Gate transition from intent to artifact

HOI responsibilities:
- Request build authorization
- Record authorization reference

Exit conditions:
- Authorization granted

Failure conditions:
- Authorization withheld or unclear

---

### 4.7 Artifact Construction

Purpose:
- Produce the module artifact

HOI responsibilities:
- Ensure conformance to locked specs
- Bind intent trace to artifact

Exit conditions:
- Artifact reaches Constructed state

Failure conditions:
- Non-conformant structure or evidence gaps

---

### 4.8 HOI Exit

Purpose:
- Terminate HOI responsibility

HOI responsibilities:
- Declare end of mediation
- Hand off artifact to lifecycle governance

Exit conditions:
- Artifact exists independently of HOI

---

## 5. REJECTION & TERMINATION RULES

- HOI may terminate at any stage
- Termination MUST preserve trace
- No partial artifact may be released

Termination is a valid outcome.

---

## 6. RESPONSIBILITY BOUNDARIES

HOI is responsible for:
- intent normalization
- scope enforcement
- invariant acknowledgement
- trace completeness

HOI is not responsible for:
- approval decisions
- enforcement actions
- lifecycle transitions beyond construction

---

## 7. SEPARATION FROM RUNTIME & GUARDS

HOI build flow:
- does not invoke runtime behavior
- does not modify guard logic
- produces artifacts consumable by guards

---

## 8. NON-GOALS

This specification excludes:
- UI/UX design
- prompts or phrasing
- CLI or API definition
- automation logic

---

## 9. LOCK READINESS STATEMENT

This document:
- defines a complete, bounded HOI build flow
- introduces no execution semantics
- preserves all module invariants

Upon approval, this specification is suitable for **LOCK** and completes the normative definition of module self-build.

---

END OF SPECIFICATION
