# IGL-GR-009 — No Cross-Layer Imports

Status: DRAFT  
Scope: SRS (Implementation Guard Layer)

## Rule
No SRS module may directly import code from another architectural layer.

## Defined Layers
The SAPIANTA system defines the following layers:
- SCF / Core
- Governance
- SRS (Chat, Modules, Adapters)
- Execution / Runtime

Each layer has a strictly defined responsibility.

## Constraints
The following import patterns are DISALLOWED:
- SRS importing Core internals
- SRS importing Governance implementation code
- Chat importing Execution logic
- Any upward or sideways import across layers

## Allowed Direction
Only the following are permitted:
- Higher layers depending on lower layers via interfaces
- Imports of interface definitions (not implementations)
- Dependency injection across layers

## Rationale
Cross-layer imports:
- collapse architectural boundaries
- introduce hidden authority escalation
- make audits unreliable
- allow semantic drift across layers

Strict layering ensures:
- governance enforcement
- system replaceability
- controlled evolution of the system

## Enforcement
IGL MUST flag:
- imports crossing defined layer boundaries
- references to implementation paths outside the current layer
- direct imports of concrete classes from foreign layers

## Notes
This rule applies regardless of convenience or code reuse.
Architectural integrity has priority over implementation simplicity.
