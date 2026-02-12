# HOI Kernel v1 LOCK

This document freezes:

- Execution kernel
- Canonical state definition
- Event registry (closed domain)
- Deterministic export contract
- Guard invariants
- Regression determinism enforcement

Rules:

1. No runtime learning.
2. No non-deterministic behavior.
3. No side effects in execution core.
4. No implicit state mutation.
5. Any modification requires MAJOR version bump.

Status: FROZEN
Version: v1
Tag reference: v1.0.0-hoi-kernel
