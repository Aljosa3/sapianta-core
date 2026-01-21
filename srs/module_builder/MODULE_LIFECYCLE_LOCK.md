# SRS — Module Lifecycle Lock

## Scope

This document defines the mandatory lifecycle constraints for all SAPIANTA modules.
It applies to all current and future modules, regardless of layer or purpose.

These constraints are normative for the SRS layer and enforceable via CI.


## Creation

All modules SHALL be created exclusively via the SAPIANTA Module Builder.

Manual creation of module directories, files, or artifacts inside `/modules`
is explicitly forbidden.

A valid module MUST contain a provenance marker emitted by the Module Builder.


## Provenance

Each module SHALL include a builder-emitted manifest that proves its origin.

Modules lacking a valid provenance marker:
- are considered invalid
- MUST NOT be loaded
- MUST fail CI checks

Provenance is binary and non-inferable.


## Mutation

Modules SHALL NOT be mutated retroactively.

Any structural or interface change to a module:
- requires re-generation via the Module Builder
- results in a new module instance

In-place modification of existing modules is forbidden.


## Enforcement

The Module Builder is the sole authorized creation mechanism.

CI tooling SHALL:
- reject modules without valid provenance
- reject manual or retroactive mutations
- enforce the exclusivity of the Module Builder

No runtime component may bypass or override these constraints.
