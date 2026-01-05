# FILE: system_flow/rules/forbidden_flow.md

## FORBIDDEN FLOWS AND SKIPS

### FF-1 — Layer Skipping
No flow may skip any declared layer in the canonical order.

### FF-2 — Reordering
No flow may reorder declared layers.

### FF-3 — Backward Traversal
No flow may traverse backward to a previous layer.

### FF-4 — Parallel Paths
No parallel, forked, or concurrent flows are permitted.

### FF-5 — Direct Core Access
No layer may access Core directly, except via declared handshake reference.

### FF-6 — Adapter Bypass
No flow may bypass the Boundary Adapter.

### FF-7 — Governance Gate Bypass
No flow may bypass the Interaction Governance Gate.

### FF-8 — Invocation Bypass
No flow may bypass the Invocation layer.

### FF-9 — CLI Re-entry
No flow may re-enter CLI after leaving it.

### FF-10 — Handshake Re-entry
No flow may re-enter the Handshake after completion.

### FF-11 — Conditional Routing
No flow may branch conditionally based on decisions or statuses.

### FF-12 — Implicit Paths
No implicit, inferred, or undocumented paths are permitted.
