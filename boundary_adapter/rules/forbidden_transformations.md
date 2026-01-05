# FILE: boundary_adapter/rules/forbidden_transformations.md

## FORBIDDEN TRANSFORMATIONS

### FT-1 — Semantic Transformation
Adapter MUST NOT infer, derive, or modify meaning of any field.

### FT-2 — Field Enrichment
Adapter MUST NOT add new fields beyond those explicitly defined.

### FT-3 — Field Mutation
Adapter MUST NOT alter field values except where fixed assignment is explicitly defined.

### FT-4 — Conditional Transformation
Adapter MUST NOT apply conditional logic based on field values or states.

### FT-5 — Canon Interaction
Adapter MUST NOT reference, interpret, or depend on Canon content.

### FT-6 — Execution Indicators
Adapter MUST NOT introduce flags, markers, or signals that could enable execution.

### FT-7 — State Awareness
Adapter MUST NOT track, infer, or depend on any state (Core, Interaction, or Adapter).

### FT-8 — Temporal Logic
Adapter MUST NOT apply retries, delays, sequencing, or timing-based logic.

### FT-9 — Persistence
Adapter MUST NOT persist, cache, replay, or log transformed data.

### FT-10 — Extension Surface
Adapter MUST NOT expose hooks, plugins, or override mechanisms.
