# SAPIANTA – AI Development Operating Constitution
# CLAUDE.md

This repository follows strict deterministic and governance-driven development principles.

Claude Code MUST adhere to the following rules in ALL tasks unless explicitly overridden by the human operator.

---

## 1. Stability Over Speed

SAPIANTA prioritizes stability over feature expansion.

Claude MUST:
- Prefer minimal changes over broad refactors
- Avoid architectural drift
- Avoid speculative improvements
- Avoid “nice to have” modifications

No implicit redesign.

---

## 2. File Creation Discipline

Claude MUST:

- Create ONLY the files explicitly requested.
- Modify ONLY the files explicitly authorized.
- Never modify unrelated files.
- Never auto-create __init__.py unless explicitly instructed.
- Never restructure directories unless explicitly instructed.

After each task, Claude MUST provide:
- `git status --short`
- `git diff --stat`

No silent edits.

---

## 3. Determinism Mandate

All runtime code MUST be deterministic.

Forbidden:
- Randomness
- datetime.now()
- Environment-based branching
- Filesystem calls (unless explicitly required)
- Git calls
- Network calls
- Non-deterministic ordering
- Reflection-based behavior

All hashes MUST use:
- json.dumps(sort_keys=True, separators=(",", ":"), ensure_ascii=False)
- SHA256
- Stable field ordering

All outputs MUST have deterministic ordering:
- Sorted errors
- Sorted constraint failures
- Sorted lists by stable keys

---

## 4. Domain Isolation

SAPIANTA enforces strict domain boundaries.

Claude MUST:

- Never import across domains unless explicitly allowed.
- trading_validation MUST NOT import credit_validation.
- credit domain MUST NOT depend on trading domain.
- Shared components must live in core or runtime substrate only.

No cross-domain coupling.

---

## 5. Validator Pattern Consistency

All domain validators MUST follow this pattern:

1. deterministic_hash()
2. structural_validate()
3. evaluate_constraint()
4. validate_<domain>_decision()

No shortcuts.
No early optimization.
No hidden logic.

Structural validation MUST precede policy validation.

---

## 6. Governance Integrity

Claude MUST respect:

- Promotion Gate classifications
- Freeze manifests
- Layer dependency checks
- Kernel determinism checks
- Boundary validators

If a change impacts governance artifacts, Claude MUST:
- Explicitly declare it
- Not proceed silently

---

## 7. No Implicit Intelligence

Validators are enforcement engines.

Forbidden inside validation logic:
- Strategy logic
- Trading signals
- ML metadata
- AI interpretation fields
- Advisory reasoning
- Free-text justification fields

Decision envelope is a snapshot, not a model explanation.

---

## 8. Minimalism Rule

Claude MUST:

- Implement only what is requested.
- Avoid adding helper abstractions unless explicitly required.
- Avoid generic frameworks.
- Avoid meta-programming.
- Avoid unnecessary configuration layers.

Simple > Abstract.

---

## 9. Test-Ready Code

All modules must:
- Import successfully
- Avoid circular imports
- Avoid global mutable state
- Be replay-safe

---

## 10. Human Authority

Claude operates under human authority.

If a requested change:
- Violates determinism
- Breaks domain isolation
- Breaks governance freeze
- Introduces architectural ambiguity

Claude MUST:
- Stop
- Explain risk
- Request confirmation

No silent architectural shifts.

---

# Operational Principle

SAPIANTA is an industrial deterministic validation engine.

Expansion must never compromise:

- Replayability
- Determinism
- Governance traceability
- Domain separation
- Constitutional stability

Stability is the highest rule.