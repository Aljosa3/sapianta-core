# SAPIANTA CORE CANON v1.0

## Canonical and Normative Definition of the Sapianta Core

Status: CANONICAL — LOCKED  
Version: v1.0  
Date of Canonization: 2026-01-03  
Authority: Sapianta Core  
Scope: System-defining  

This document is implementation-independent and repository-independent.

---

## 0. Canonical Status

This document is the canonical and normative source of truth for the Sapianta Core.

If any implementation, module, interaction layer, explanation, or behavior
contradicts this document, the implementation is wrong.

This document does not describe how the system is implemented.  
It defines what the system is.

---

## 1. Purpose of the Core

The Sapianta Core is a normative system kernel whose sole purpose is to:

- deterministically assess the meaning of a request,
- return a single, typed decision output,
- provide a non-influential explanation of that decision,
- provide a minimal, content-free audit trace.

The Core does not execute actions.  
The Core does not converse.  
The Core does not interact.

---

## 2. Boundaries of Responsibility

The Core is responsible only for:

- semantic evaluation (meaning),
- formal decision output (ACCEPTED / REJECTED),
- read-only explanation of decisions,
- proof that a decision occurred.

The Core is not responsible for:

- user interfaces,
- dialogue or conversation,
- interaction management,
- selection or use of LLMs,
- execution of commands or actions,
- learning, optimization, or adaptation.

---

## 3. Core Structure

The Sapianta Core consists of three independent and isolatable domains.

### 3.1 Decision / Meaning Kernel

This domain:

- receives an abstract request representation,
- evaluates meaning only,
- operates deterministically,
- uses no heuristics,
- performs no inference beyond defined semantics.

Its output is the ChatResponse.

---

### 3.2 Explain Domain (Read-only)

The Explain Domain:

- reads only the final ChatResponse,
- never reads the original request,
- never participates in decision-making,
- never asks questions,
- never proposes actions.

It produces an ExplainResponse, which is:

- a direct projection of ChatResponse,
- declarative,
- neutral,
- non-influential,
- without feedback into the Core.

---

### 3.3 Audit Domain (Read-only)

The Audit Domain:

- records the existence of a decision,
- records metadata only,
- never records content,
- never enables replay, debugging, or reconstruction.

It produces an AuditRecord, which is evidence — not a log.

---

## 4. Core Outputs

### 4.1 ChatResponse

ChatResponse is the only authoritative output of the Core.

It contains:

- decision status (ACCEPTED or REJECTED),
- a typed reason (if applicable),
- immutable system markers.

It is:

- deterministic,
- immutable,
- side-effect free.

---

### 4.2 ExplainResponse

ExplainResponse is a secondary semantic description of ChatResponse.

It introduces:

- no new decisions,
- no new reasons,
- no reinterpretation.

If explanation is not applicable, a neutral formulation is used.

---

### 4.3 AuditRecord

AuditRecord is a minimal proof artifact.

It may contain:

- timestamp,
- decision outcome,
- reason category,
- core identity marker.

It never contains:

- input data,
- request content,
- explanation text,
- user or session identifiers.

---

## 5. Core Invariants

The following statements must always hold:

- The Core is deterministic.
- The Core performs no execution.
- The Core contains no dialogue.
- The Core has no feedback loops.
- The Core does not learn.
- The Core is immutable by design.
- The Core is replaceable by implementation, not by meaning.

If any invariant is violated, the system is not Sapianta Core.

---

## 6. Relationship to External Layers

All external layers (interaction, chat, LLMs, UX, modules):

- are subordinate to this Canon,
- must not alter Core outputs,
- must not emulate Core decision-making,
- must not extend or reinterpret decision meaning.

The Core has no knowledge of external layers.

---

## 7. Removability

Each Core domain may be removed:

- without affecting the remaining domains,
- without affecting decision correctness.

If Explain or Audit domains are absent,
the Decision / Meaning Kernel remains valid and correct.

---

## 8. Canon Lock

This document defines Sapianta Core v1.0.

Changes are permitted only by:

- issuing a new Canon version (v1.1, v2.0, …),
- publishing a new canonical document,
- explicitly declaring a Core change.

This version is locked.

---

## 9. Minimal Conclusion

Sapianta Core is not an application.  
It is not a chatbot.  
It is not an LLM system.

Sapianta Core is a normative operating kernel for meaning-based decisions.

Everything else is an extension.
