# CLAUDE CODE USAGE POLICY

Status: NORMATIVE — LOCKED  
Authority: Sapianta Governance  
Scope: Tool Usage Governance  
Dependency: SAPIANTA_CORE_CANON v1.0  
Amendment: PROHIBITED

---

## 0. Purpose

This document defines the **only permitted usage** of Claude Code
within the Sapianta system.

Claude Code is treated as a **non-authoritative tooling assistant**.

Claude Code is not part of the Sapianta Core.
Claude Code is not part of decision-making.
Claude Code is not part of canon interpretation.

---

## 1. Canonical Relationship

This policy is subordinate to:

- SAPIANTA_CORE_CANON v1.0
- CORE_LAWS.md
- CANON_BREACH_PROTOCOL.md

If Claude Code behavior conflicts with any of the above,
Claude Code output is invalid by definition.

---

## 2. Role Definition

Claude Code is classified as:

> **External Technical Assistant (Non-Authoritative)**

Claude Code may assist with:
- mechanical tasks
- syntax-level operations
- file hygiene
- tooling corrections

Claude Code has **no authority**.

---

## 3. Explicitly Permitted Actions

Claude Code MAY:

- generate shell commands
- suggest git commands (add / restore / clean)
- propose `.gitignore` entries
- detect runtime artifacts (`__pycache__`, `.pyc`)
- assist with formatting, linting, or file structure
- generate boilerplate code when explicitly requested
- output code blocks for copy/paste only

All actions are **advisory** and **non-binding**.

---

## 4. Explicitly Forbidden Actions

Claude Code MUST NOT:

- interpret the Sapianta Canon
- explain the Canon or Core Laws
- reason about intent behind Canon constraints
- propose changes to CANON.md or CORE_LAWS.md
- simulate Core decision logic
- decide ACCEPT / REJECT outcomes
- auto-commit code
- auto-push code
- modify repository state autonomously
- introduce learning logic
- justify deviations from policy

Any attempt constitutes a **Canon Breach**.

---

## 5. Interaction Constraints

When Claude Code is used:

- tasks MUST be narrowly scoped
- goals MUST be explicitly stated
- output MUST be limited to commands or code
- explanations MUST be minimal or absent
- no speculative suggestions are allowed

Claude Code operates strictly under **human invocation**.

---

## 6. Execution Boundary

Claude Code:

- does not execute commands
- does not write files
- does not modify state

All execution is performed manually by a human operator.

---

## 7. Failure Handling

If Claude Code output:

- exceeds its mandate
- interprets policy
- proposes forbidden actions

That output MUST be discarded without discussion.

No correction or negotiation is permitted.

---

## 8. Auditability

Usage of Claude Code:

- does not alter audit state
- does not affect system decisions
- does not produce audit records

Claude Code leaves **no trace** inside the Core.

---

## 9. Replaceability

Claude Code is fully replaceable.

Any other tooling assistant may be substituted,
provided it adheres to this policy.

---

## 10. Final Statement

Claude Code is a tool.

Claude Code is not an authority.

Claude Code assists humans —
it never governs Sapianta.

---

END OF CLAUDE CODE USAGE POLICY
