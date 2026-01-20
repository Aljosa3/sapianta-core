# IGL-GR-008 — Explicit Interfaces Only

Status: DRAFT  
Scope: SRS (Implementation Guard Layer)

## Rule
All SRS modules MUST communicate exclusively through explicitly defined interfaces.

## Definition
An explicit interface is:
- a named contract (class, protocol, or documented interface)
- with a defined method signature
- and clearly defined input/output semantics

Implicit communication is NOT allowed.

## Rationale
Implicit coupling creates hidden dependencies, makes governance unenforceable,
and prevents reliable auditing and replacement of modules.

Explicit interfaces ensure:
- composability
- auditability
- replaceability
- deterministic integration

## Enforcement
The following are DISALLOWED in SRS code:
- accessing attributes of foreign modules directly
- relying on undocumented side effects
- calling functions or methods not declared in an interface
- importing implementation details instead of interfaces

The following are ALLOWED:
- communication via interface classes
- dependency injection via explicit interface parameters
- usage of abstract base classes or protocols

## Examples (Non-exhaustive)

### ALLOWED
- `class DecisionInterface`
- `handler: DecisionInterface`
- `module.receive(payload)`

### DISALLOWED
- `other_module._internal_state`
- `from module.impl import concrete_function`
- relying on global registries or hidden singletons
