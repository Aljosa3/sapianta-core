# ADR — Remove Legacy MEP Execution Subsystem

Status: ACCEPTED  
Date: 2026-02-13  
Decision Type: Architectural Cleanup  
Supersedes: GuardLifecycle v0.2 (legacy execution model)

---

## Context

The repository contains a legacy execution subsystem:

    runtime/mep/
    runtime/use_cases/
    tests/mep/
    tests/test_guard_*.py

This subsystem depends on:

    runtime.guard_lifecycle

which no longer exists in the repository.

All imports from runtime.mep fail at import time.

Pytest confirms systematic ModuleNotFoundError during collection.

---

## Architectural Evolution

Timeline:

- 2026-01-23 — GuardLifecycle LOCK v0.2 created
- 2026-01-23 — Module Admission v0.3 supersedes GuardLifecycle
- 2026-02-12 — HOI Kernel v1 freeze
- 2026-02-13 — Kernel Constitution v1.0 activated

The active normative architecture is defined by:

    governance/kernel/KERNEL_CONSTITUTION_v1.0.md
    governance/locks/HOI_KERNEL_v1_LOCK.md

Kernel v1 explicitly defines the runtime surface as:

    sapianta_hoi.*
    sapianta_validation.*
    sapianta_chat.*

The legacy runtime.mep subsystem is not referenced
by any active governance specification.

---

## External Verification

Claude Code architectural audit confirmed:

- runtime.mep is not reachable from active execution graph
- governance references are obsolete or historical
- subsystem is safe to delete
- confidence: high

---

## Decision

The legacy MEP execution subsystem is removed from mainline.

Deleted components:

- runtime/mep/*
- runtime/use_cases/*
- tests/mep/*
- tests/test_guard_*.py

---

## Consequences

Positive:
- Clean pytest baseline
- Single authoritative execution kernel (HOI v1)
- Removal of dead architectural branch
- Clear governance binding

Negative:
- Historical MEP implementation removed from working tree
- Recovery possible only via git history

---

## Rollback Strategy

The pre-removal state is preserved via tag:

    v1.0.0-pre-mep-removal

Any rollback may be performed via:

    git checkout <tag>
    or
    git revert <commit>

---

## Architectural Integrity Statement

Post-removal, the execution model of SAPIANTA is defined exclusively by:

    HOI Kernel v1.0.0

No parallel execution model exists.

Baseline integrity: CLEAN.
