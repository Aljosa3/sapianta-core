# HOI KERNEL — PUBLIC SURFACE SNAPSHOT v1.0

Snapshot Version: v1.0.0  
Status: Frozen  
Linked Constitution: KERNEL_CONSTITUTION_v1.0.md  
Date: 2026-02-13  

---

## 1. Purpose

This document freezes the allowed namespace surface of the HOI Kernel.

It exists to prevent accidental expansion of kernel boundary.

Any namespace outside this whitelist is constitutionally outside the Kernel.

---

## 2. Allowed Kernel Namespaces

The HOI Kernel SHALL consist exclusively of:

- sapianta_hoi.runtime_stub
- sapianta_hoi.execution
- sapianta_hoi.guards
- sapianta_hoi.runtime_contracts

No additional namespaces are permitted.

---

## 3. Prohibited Expansion

The following are explicitly outside Kernel boundary:

- sapianta_validation.*
- sapianta_chat.*
- sapianta_runtime.*
- modules.*
- governance.*
- sandbox.*
- tests.*

Any attempt to:

- Add new sapianta_hoi subpackages
- Introduce new execution layers
- Inject external dependency
- Expand Public Surface

Requires constitutional amendment.

---

## 4. Enforcement Principle

Future enforcement mechanism may include:

- Namespace whitelist validator
- Static boundary scan
- CI freeze check

---

## 5. Freeze Statement

This snapshot freezes the Kernel Public Surface at version 1.x.

Any expansion automatically requires:

- Major version increment (v2.0+)
- Constitution amendment
- Determinism re-certification
- Governance approval
