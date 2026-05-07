# SAPIANTA Product System State

## Purpose

This document is product-facing architectural memory for the server/demo branch. It exists to preserve continuity for UI work, demo preparation, enterprise messaging, EU AI Act messaging, and AI assistant collaboration.

This document is documentation-only. It does not define runtime behavior, activate governance, change enforcement, or modify the Decision Spine.

## Current Product State

SAPIANTA is currently presented as an AI Decision Validator demo experience for enterprise audiences. The product story emphasizes deterministic validation, auditability, explainability, and clear limits on what the demo currently implements.

The active product surface is presentation-oriented. It is intended to help viewers understand how decision validation, audit traces, and regulatory narratives can be made visible without claiming a complete compliance product.

## Current Demo State

The demo branch is optimized for credible presentation. The main demo emphasis is:

- cinematic first impression
- enterprise-readable dark UI
- audit-first walkthrough
- explainability flow
- Swagger/API exposure for technical audiences
- EU AI Act narrative support with careful non-claim language

The demo is not a runtime governance activation. It should be described as a product and architecture demonstration.

## Current UI State

The UI direction is cinematic, dark, enterprise-oriented, and audit-forward. The interface should make the product feel serious, inspectable, and boardroom-ready while avoiding exaggerated claims.

The UI should keep validation outcomes, explanations, audit records, and regulatory framing visible enough for a short demo without requiring deep technical setup.

## Enterprise Positioning Status

The current enterprise position is:

SAPIANTA helps organizations inspect AI-assisted decisions through deterministic validation, audit-friendly presentation, and explainability-oriented records.

Current positioning should avoid claims of legal compliance, autonomous enforcement, certified governance, or fully implemented production controls unless those capabilities are separately implemented and verified.

## Current Architecture Separation

The product memory layer is separate from runtime architecture.

- Product memory lives in `docs/`.
- Product ADRs live in `docs/ADR/`.
- Product milestone categories live in `docs/MILESTONES/`.
- Runtime code remains unchanged.
- Governance documents remain separate from this product memory layer.

Governance remains dormant in the server/demo branch. Runtime governance activation is not active. The demo branch is presentation-oriented and does not activate governed enforcement.

## Known Limitations

The current branch has important limits:

- governance remains dormant
- runtime governance activation is not active
- governed enforcement is not active
- the demo does not prove regulatory compliance
- the demo does not provide autonomous decision control
- product UI may show concepts that require careful explanation as demo surfaces

See `docs/KNOWN_LIMITATIONS.md` for the full product-facing limitation list.

## Current Focus

The current focus is demo clarity:

- cinematic demo
- audit viewer
- enterprise UI
- AI Decision Validator messaging
- EU AI Act narrative
- demo credibility
- explainability flow

## Demo Readiness State

The demo is suitable for product storytelling when presented with explicit limitations. It is not suitable for claims of certified compliance, runtime governance activation, or production enforcement.

Demo readiness depends on keeping the story deterministic, explainable, and honest about implemented versus conceptual capabilities.
