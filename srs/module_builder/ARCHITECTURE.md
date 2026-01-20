# MODULE BUILDER — ARCHITECTURE DRAFT (SRS)

## 0. STATUS & SCOPE

- Component: SAPIANTA MODULE BUILDER  
- Layer: SRS (implementation layer)  
- Normativity: NONE (non-normative, non-decision-making)  
- Bindings: IGL v2 (GR-001–GR-009) — mandatory  
- Exclusions: SCF, policy, interpretation, business logic, defaults  

---

## 1. MINIMAL ARCHITECTURE (STATIC)

srs/
└── module_builder/
    ├── __init__.py
    ├── builder.py
    ├── schema.py
    ├── validator.py
    ├── emitter.py
    └── errors.py

Properties:
- No global state
- No decorators
- No implicit flows
- No cross-layer imports
- Deterministic execution only

---

## 2. COMPONENT ROLES (EXACT)

### builder.py — Orchestrator
- Coordinates call order only
- No logic, no interpretation
- No defaults, no state

### schema.py — Explicit Contract
- Required fields only
- No optional fields
- No inferred values

### validator.py — IGL Structural Validator
- Validates GR-001 … GR-009
- Structural validation only
- No intent or meaning interpretation

### emitter.py — Artifact Emitter
- Deterministic module skeleton emission
- No conditional generation

### errors.py — Explicit Failure Surface
- Typed, terminal errors only
- No recovery, no auto-correction

---

## 3. DATA FLOW (LINEAR, CLOSED)

INPUT (explicit spec)
→ schema.check()
→ validator.check(IGL)
→ emitter.emit()
→ OUTPUT (module artifacts)

No branching  
No retries  
No mutation  

---

## 4. HARD BOUNDARIES

Module Builder may NOT:
- Decide
- Interpret
- Enrich
- Normalize
- Default
- Escalate authority

Module Builder may ONLY:
- Accept explicit input
- Validate structure
- Emit structure

---

## 5. FAILURE MODEL

- Any violation → STOP
- No fallback
- No partial output
- Error must be explicit and terminal

---

## 6. DEPENDENCY RULES

Allowed imports:
- srs.module_builder.*

Forbidden access:
- SCF
- Chat
- Runtime execution
- External helpers

---

## 7. CONFIRMATION GATE

After acceptance:
- Proceed to exact interfaces (function signatures only)

Any ambiguity:
- STOP and ask exactly one question
