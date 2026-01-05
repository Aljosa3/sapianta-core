# FILE: system_flow/rules/forbidden_skips.md

## FORBIDDEN SKIPS (PAIRWISE)

### FS-1
CLI → Interaction (skipping Invocation) is forbidden.

### FS-2
CLI → Governance Gate is forbidden.

### FS-3
Invocation → Boundary Adapter is forbidden.

### FS-4
Interaction → Boundary Adapter (skipping Governance Gate) is forbidden.

### FS-5
Interaction → Handshake is forbidden.

### FS-6
Governance Gate → Handshake is forbidden.

### FS-7
Boundary Adapter → Core (direct invocation) is forbidden.

### FS-8
Any layer → Core (except reference-only endpoint) is forbidden.

### FS-9
Any layer → Any previous layer is forbidden.

### FS-10
Any layer → Any non-adjacent future layer is forbidden.
