# PATH: governance/phases/PHASE_v0.17_OUTPUT_PROTOCOL_LOCK.md

# PHASE v0.17 — OUTPUT PROTOCOL STABILIZATION
## Status: LOCKED

---

## What is locked

1. **RAW LLM output protocol is FILE-based only**

   The only allowed output format from any execution backend is:

   FILE: <relative/path>
   <file content>

   Repeated for each generated file.

2. **Output must be fully machine-readable**

   - No markdown fences
   - No explanations
   - No comments outside FILE blocks
   - No mixed formats (JSON, prose, etc.)

3. **Materialization is strictly protocol-driven**

   Files are created **only** from FILE blocks.
   No inference, guessing, or recovery is allowed.

---

## What is forbidden

- Any fallback parsing strategy
- Any attempt to “repair” malformed output
- Accepting partial or ambiguous output
- Allowing content outside FILE blocks
- Introducing alternative output formats

---

## Failure semantics

Any deviation from the FILE output protocol results in
**immediate build failure (HARD FAIL)**.

No retries.  
No auto-correction.  
No silent degradation.

---

## Phase completion statement

PHASE v0.17 locks the RAW OUTPUT TRANSPORT PROTOCOL
between execution backends and the SAPIANTA runtime.

From this phase onward, reliable module construction
depends exclusively on strict FILE-based output.

LOCK CONFIRMED.
