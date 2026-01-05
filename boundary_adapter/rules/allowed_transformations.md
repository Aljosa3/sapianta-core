# FILE: boundary_adapter/rules/allowed_transformations.md

## ALLOWED TRANSFORMATIONS

### AT-1 — Structural Mapping
Adapter MAY perform structural field-to-field mapping as explicitly defined
in the mapping specifications.

### AT-2 — Field Dropping
Adapter MAY drop fields that have no explicit target in the destination type.

### AT-3 — Fixed Value Assignment
Adapter MAY assign fixed, pre-declared constant values where explicitly required
by a mapping rule.

### AT-4 — Opaque Forwarding
Adapter MAY forward fields without inspecting or interpreting their contents.

### AT-5 — Deterministic Output
For identical input structures, Adapter MUST emit identical output structures.

### AT-6 — Idempotency
Applying the same transformation multiple times MUST yield the same result.
