# IGL-GR-004 — No Hidden Control Flow

Status: DRAFT  
Scope: SRS (Implementation Guard Layer)

## Rule
Implementation code MUST NOT introduce hidden or implicit control flow
mechanisms that alter execution paths outside of explicit function calls
and conditionals.

## Rationale
Hidden control flow makes execution behavior non-obvious, non-reviewable,
and prone to semantic drift. In a governed system, all execution paths must
be explicit and statically inspectable.

## Enforcement
The following are DISALLOWED in SRS implementation code:
- decorators that alter runtime behavior (except explicitly allowed ones)
- implicit execution via metaprogramming
- control flow introduced through side effects at definition time

The following are ALLOWED:
- explicit function calls
- explicit conditional statements
- explicitly whitelisted decorators (defined by IGL)

This rule does NOT regulate business logic correctness.

## Examples (Non-exhaustive)

### ALLOWED
- Explicit function calls
- Explicit `if / else` branching
- `@abstractmethod` for interface definition

### DISALLOWED
- Decorators that inject execution logic
- Implicit invocation through class or function definition
- Control flow hidden behind import-time execution
