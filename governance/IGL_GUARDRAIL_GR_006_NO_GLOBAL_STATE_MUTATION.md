# IGL-GR-006 — No Global State Mutation (Top-Level Only)

Status: DRAFT  
Scope: SRS (Implementation Guard Layer)

## Rule
SRS implementation code MUST NOT mutate global or module-level state
at top-level execution time.

## Definition
Top-level code is any code executed during module import, including:
- assignments at module scope
- mutation of module-level objects
- registration, caching, or state initialization outside functions or classes

## Rationale
Top-level mutations create implicit execution order, hidden dependencies,
and non-deterministic behavior across imports.
In a governed system, module import MUST be side-effect free.

## Enforcement
The following are DISALLOWED at module top-level:
- mutable global variables
- appending to lists or dicts
- modifying class registries
- calling functions that mutate state
- implicit initialization logic

The following are ALLOWED:
- constant definitions
- class and function definitions
- type declarations
- imports
- immutable literals

State mutation is ONLY permitted:
- inside functions
- inside class methods
- during explicit runtime execution

## Examples (Non-exhaustive)

### ALLOWED
- `CONST_VALUE = 10`
- class definitions
- function definitions

### DISALLOWED
- `registry.append(x)` at module scope
- `CONFIG["x"] = y` at import time
- implicit initialization logic outside functions
