# CLI_OUTPUT_ADAPTER

## Status
- Phase: FAZA 24C.2
- Type: Governance / Design-only
- Execution: Forbidden
- Adapter state: Mandatory
- Lock state: NOT LOCKED

---

## 1. Purpose

This document defines the **CLI Output Adapter** as a strict
implementation boundary between:

- routed Message Objects
- terminal output rendered to the user

It answers the question:

> How does a lawful message become visible — without changing its meaning?

The goal is to:
- prevent the CLI from interpreting decisions
- isolate presentation from governance
- ensure deterministic and auditable output
- make refusal and failure behavior predictable

The adapter renders.
It does not decide.

---

## 2. Core Principle

The CLI Output Adapter MUST act as a **pure renderer**.

It MUST:
- accept a finalized Message Object
- transform it into terminal-safe output
- preserve semantic content exactly

It MUST NOT:
- evaluate meaning
- alter intent
- add advice
- suppress information
- trigger execution or logic

No transformation of authority is permitted.

---

## 3. Adapter Boundary

The adapter sits **after Message Routing** and **before terminal output**.

Upstream:
- Message Routing Contract
- Refusal / Denial / Failure semantics

Downstream:
- CLI stdout / stderr only

No upstream calls are allowed.

---

## 4. Accepted Inputs

The adapter MAY receive **only one** of the following:

- Success Output (non-governed)
- R1 — Refusal Message
- R2 — Denial Message
- F1 — Failure Message

Any other input MUST result in an immediate adapter error
(which itself MUST be converted to F1 by upstream logic).

The adapter never emits errors directly.

---

## 5. Rendering Rules

The adapter MUST:

- render all required fields
- preserve wording verbatim
- preserve ordering of fields
- maintain explicit labels
- render exactly one message per invocation

Whitespace and formatting MAY vary,
but **content MUST NOT**.

---

## 6. Output Channels

The adapter MUST use channels consistently:

- stdout:
  - R1 (Refusal)
  - R2 (Denial)
  - Success output

- stderr:
  - F1 (Failure) only

No mixing is allowed.

---

## 7. Exit Codes

The adapter MUST return deterministic exit codes:

| Condition | Exit Code |
|---------:|----------:|
| Success  | 0 |
| R1      | 10 |
| R2      | 20 |
| F1      | 99 |

Exit codes are part of the contract
and MUST NOT change without governance approval.

---

## 8. Formatting Policy

Formatting is allowed **only** to improve readability.

Allowed:
- headings
- indentation
- line breaks
- monospace blocks

Forbidden:
- summarization
- rewording
- interpretation
- emoji
- natural-language explanations

The adapter formats.
It does not explain.

---

## 9. Prohibited Behavior

The CLI Output Adapter MUST NOT:

- generate messages
- merge multiple messages
- retry rendering
- downgrade message severity
- convert failures into refusals
- swallow messages
- print stack traces
- print debug information

Any violation is a system integrity breach.

---

## 10. Design-Time Constraint

This document:
- defines an implementation boundary only
- contains no code
- performs no routing
- performs no execution
- performs no evaluation

It is enforced by:
- Message Routing Contract (FAZA 24C.1)
- Refusal & Failure Messages (FAZA 24B)
- Governance Lock System

---

## 11. Closing Statement

The CLI Output Adapter is the **mouth of the system**.

If it lies:
- the law is corrupted
- refusal becomes opinion
- failure becomes noise

Render exactly.
Or do not render at all.
