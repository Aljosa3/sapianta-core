# Knowledge Anchor — Definition

## Status
- Phase: FAZA 23A
- Type: Design-only
- Execution: Forbidden
- Stability: Canon-adjacent

---

## 1. Purpose

A **Knowledge Anchor** is a declarative, external, versioned source of truth
that SAPIANTA may reference during reasoning.

Knowledge Anchors exist to:
- prevent hallucination
- prevent free interpretation of system rules
- enforce architectural and governance constraints
- ground reasoning in explicit documents, not model memory

SAPIANTA does not "know" — it **references**.

---

## 2. Core Principle

> If a claim cannot be traced to a Knowledge Anchor,  
> it has **no normative authority** inside the system.

---

## 3. What a Knowledge Anchor Is

A Knowledge Anchor is:

- external to the model
- human-authored
- versioned
- readable
- immutable once locked
- normatively binding for reasoning

It may:
- describe rules
- define boundaries
- specify architecture
- impose locks
- constrain execution

---

## 4. What a Knowledge Anchor Is NOT

A Knowledge Anchor is NOT:

- executable code
- dynamic memory
- inferred knowledge
- learned behavior
- probabilistic output
- implicit system state

Anchors are **declared**, never discovered.

---

## 5. Anchor Metadata (Conceptual)

Each Knowledge Anchor MUST conceptually expose:

- Anchor ID
- Document path
- Version or tag
- Status (draft / active / locked)
- Scope (what it governs)
- Normative strength (informative / binding)

No anchor is valid without explicit declaration.

---

## 6. Anchor Authority Levels

Knowledge Anchors may have different authority levels:

1. **Binding**
   - MUST be obeyed
   - Overrides model suggestions
   - Example: locks, execution boundaries

2. **Guiding**
   - SHOULD be followed
   - Allows interpretation within bounds
   - Example: specs, architectural principles

3. **Informative**
   - MAY inform reasoning
   - Has no restrictive power
   - Example: notes, explanations

---

## 7. Anchor Usage Rules

SAPIANTA reasoning MUST:

- explicitly reference anchors when applicable
- resolve conflicts by anchor authority
- refuse actions that violate binding anchors
- state when no anchor applies

If no relevant anchor exists:
- SAPIANTA MUST respond in exploratory / non-authoritative mode

---

## 8. Immutability & Locking

Once a Knowledge Anchor is locked:
- its content is immutable
- reinterpretation is forbidden
- overrides are forbidden
- only supersession via new anchor version is allowed

---

## 9. Relation to Other Layers

Knowledge Anchors sit between:

- Governance / Canon (source of authority)
- Reasoning Layer (consumer of authority)

They do NOT belong to:
- Execution Layer
- Memory Layer
- Learning Layer

---

## 10. Design Constraint

Knowledge Anchors are a **hard requirement** for:

- execution permission
- autonomous behavior
- system self-modification
- trust escalation

Without anchors, execution is structurally unsafe.

---

## 11. Closing Statement

Knowledge Anchors are the **spine of SAPIANTA**.

They ensure that:
- reasoning is accountable
- power is bounded
- evolution is traceable
- control remains human-legible

No execution shall ever outrun its anchors.
