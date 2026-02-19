# SAPIANTA — CORE PUBLIC INTERFACE CONTRACT
## Version: 1.0
## Status: ACTIVE
## Scope: Layer 2 Public API Boundary

---

# 1. Purpose

This document defines the only supported public interface between:

- sapianta-core (Layers 0–2)
- External domain systems (e.g., Credit, HR, Trading)

It establishes:

- What domains are allowed to call.
- What domains must not access.
- Stability and compatibility guarantees.
- Versioning discipline.

This contract is binding for all domain repositories.

---

# 2. Core Architectural Boundary

The following applies:

- Domains MAY depend on public interfaces explicitly defined in this document.
- Domains MUST NOT import or access internal modules of sapianta-core.
- Domains MUST treat Core as a black-box deterministic runtime.
- Core retains full internal evolution freedom behind this boundary.

Violation of this contract invalidates compatibility guarantees.

---

# 3. Public API Surface (Layer 2)

The following interfaces are officially exposed:

---

## 3.1 ControlLayer

class ControlLayer:
    def validate(event: EventContract) -> ControlResult

### Contract Rules:

- validate MUST be deterministic.
- validate MUST be fail-closed.
- validate MUST NOT mutate input state.
- validate MUST produce a structured audit trace.
- validate MUST enforce Layer 1 registry rules.
- validate MUST enforce Layer 2 invariants.

Domains MUST NOT override or extend ControlLayer.

---

## 3.2 EventContract

class EventContract:
    event_id: str

### Contract Rules:

- Event must be immutable.
- Event must satisfy schema validation.
- Event must belong to registered event domain.
- Event fields must be explicit and typed.
- No dynamic attributes allowed.

Domains MAY define domain-specific events,
but they MUST conform to EventContract interface requirements.

---

## 3.3 ControlResult

class ControlResult:
    is_valid: bool
    event: EventContract
    audit_trace: AuditTrace

### Contract Rules:

- is_valid == False MUST indicate fail-closed behavior.
- audit_trace MUST be deterministic and reproducible.
- No partial validation states allowed.

Domains MUST treat ControlResult as immutable.

---

# 4. Strict Prohibitions

Domains MUST NOT:

- Import internal Layer 0 modules.
- Access registry internals.
- Modify invariant rules.
- Inject runtime hooks into ControlLayer.
- Monkey-patch Core components.
- Rely on undocumented internal behavior.
- Depend on private file structure of Core.

Only documented public interfaces are stable.

---

# 5. Determinism Guarantee

Core guarantees:

- Identical input → identical output.
- Deterministic audit trace generation.
- No hidden side effects.
- No external I/O inside validation.
- No implicit state mutation.

Domains MUST preserve determinism when integrating.

---

# 6. Versioning Discipline

Core follows semantic versioning:

MAJOR.MINOR.PATCH

- PATCH → internal bug fix (no API change)
- MINOR → backward compatible extension
- MAJOR → breaking API change

Domains MUST declare explicit dependency version:

sapianta-core==1.x.y

No floating dependencies allowed.

---

# 7. Compatibility Rules

Core guarantees:

- Backward compatibility within MAJOR version.
- No silent contract expansion.
- No implicit behavior change.

If MAJOR version changes:

- Domains must explicitly upgrade.
- Migration guide must be provided.

---

# 8. Extension Boundary

Future Layers (L3, L4, L5):

- Will extend Core.
- Will NOT alter L2 contract retroactively.
- Will expose new interfaces under new namespaces.

L2 remains stable under v1.x.

---

# 9. Enforcement

Violation of this contract:

- Breaks deterministic guarantees.
- Invalidates certification claims.
- Disqualifies domain system from enterprise compliance.

---

# 10. Effective Date

This contract becomes effective upon tagging:

sapianta-core v1.3.0

---

# End of Contract
