# SRS — Module Builder: Purpose and Boundaries

## Purpose

The SAPIANTA Module Builder is an SRS-layer infrastructural component.
Its sole purpose is to deterministically generate module artifacts
that conform to the SAPIANTA module structure and governance entry conditions.

The Module Builder exists exclusively to:
- accept an explicit ModuleSpec
- validate its structure
- apply mandatory IGL gating
- emit a minimal, provenance-marked module artifact

The Module Builder does not participate in runtime execution.


## Non-Goals

The Module Builder SHALL NOT:
- act as a runtime module
- appear inside /modules as a loadable unit
- define, interpret, or infer semantics
- execute business logic
- assign permissions or authority
- inject defaults or inferred values
- perform cross-layer imports
- mutate global or shared state
- interpret IGL rules beyond explicit gating
- create executable code

Any functionality beyond deterministic artifact emission is explicitly out of scope.


## Layer Position

The Module Builder resides strictly in the SRS (System Runtime Support) layer.

It operates:
- before runtime
- outside the module system
- outside execution flow

Runtime components MUST NOT depend on, reference, or invoke the Module Builder.
The existence of the Module Builder is opaque to runtime.


## Authority Limits

The Module Builder has no decision authority.

It SHALL:
- refuse incomplete or malformed specifications
- halt on validation failure
- produce artifacts only on explicit success

It SHALL NOT:
- override governance
- escalate privileges
- create implicit interfaces
- infer intent or meaning
- authorize behavior

All authority remains external to the Module Builder.
