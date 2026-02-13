# HOI KERNEL — PUBLIC SURFACE v1.0

Kernel Version: v1.0.0  
Freeze Status: API Frozen  
Determinism Status: Production Sealed (v0.51)  
Date: 2026-02-13  

---

## 1. Purpose

This document defines the officially supported and allowed public interface of the HOI Kernel.

Any usage outside of this defined surface is considered a boundary violation.

The kernel is defined as a deterministic execution substrate and must remain semantically isolated from business, policy, and industrial logic.

This document governs API-level interaction only.  
Architectural constitution and amendment rules are defined separately in `KERNEL_CONSTITUTION_v1.0.md`.

---

## 2. Kernel Scope Definition

The HOI Kernel consists exclusively of the following namespaces:

- `sapianta_hoi.runtime_stub`
- `sapianta_hoi.execution`
- `sapianta_hoi.guards`
- `sapianta_hoi.runtime_contracts`

All other namespaces are considered higher layers and are not part of the kernel.

This Public Surface applies only to the defined Kernel Scope.

---

## 3. Official Execution Entry

### Allowed Import

```python
from sapianta_hoi.execution.session_controller import SessionController
```

### Allowed Public Methods

- `dispatch(event: Event) -> CanonicalState`
- `current_state() -> CanonicalState`

This is the only allowed mechanism for:

- Triggering events
- Executing transitions
- Mutating state
- Retrieving canonical state

Direct access to `execution_loop` or any internal transition mechanism is strictly forbidden.

Execution semantics must never be bypassed.

---

## 4. Event Surface

### Allowed Imports

```python
from sapianta_hoi.execution.event_dispatcher import create
from sapianta_hoi.runtime_stub.event import Event
```

Event objects must remain immutable and free of business semantics.

Modification of Event payload after creation is forbidden.

Event interpretation is not part of the kernel responsibility.

---

## 5. Canonical State Surface

### Allowed Import

```python
from sapianta_hoi.runtime_stub.canonical_state import CanonicalState
```

Allowed:

- Reading state values
- Passing state across higher layers

Forbidden:

- Direct mutation
- Accessing private `SessionController` state
- Injecting external state directly into kernel

State mutation is only permitted through `dispatch()`.

---

## 6. Export Surface

### Allowed Import

```python
from sapianta_hoi.runtime_contracts.exporter import *
```

Exporter is the only official mechanism for extracting kernel state for external layers.

Kernel must not expose internal structures directly.

Export output must remain deterministic and version-stable.

---

## 7. Registry Surface

Registry exposure is limited to read-level introspection.

### Allowed Import

```python
from sapianta_hoi.runtime_contracts.event_registry import EventRegistry
```

Forbidden:

- Runtime override of transition mapping
- Direct manipulation of transitions
- Dynamic mutation of registry mappings from higher layers

Registry mutation is internal-only.

---

## 8. Strictly Internal (Forbidden for Higher Layers)

The following modules are strictly internal and must not be imported outside kernel:

- `runtime_stub.execution_loop`
- `runtime_stub.transitions`
- `runtime_stub.validation`
- `guards.*`
- Private attributes of `SessionController`
- Any module explicitly marked as internal

Violation of this rule constitutes an architectural boundary breach.

---

## 9. Boundary Violation Definition

A boundary violation occurs if:

- Higher-layer code imports internal kernel modules
- Higher-layer code mutates kernel state directly
- Higher-layer code bypasses `SessionController`
- Higher-layer code manipulates transitions
- Higher-layer code introduces non-deterministic behavior into kernel scope

Boundary violations require immediate architectural review.

---

## 10. Determinism & Isolation Guarantee

The HOI Kernel guarantees:

- Deterministic execution
- No external I/O within kernel scope
- No dependency on time, randomness, environment variables, or network
- No business or policy interpretation within kernel

Any modification that compromises these guarantees invalidates this freeze status.

---

## 11. Change Policy

Changes to this Public Surface require:

- Major version increment of Kernel
- Governance review
- Re-certification of determinism
- Updated freeze documentation

Minor implementation changes inside kernel that do not alter this surface do not require version change.

---

## 12. Status

HOI Kernel v1.0.0 is certified as:

**Level A — Pure Execution Substrate**

This Public Surface is frozen under constitution-grade protection.
