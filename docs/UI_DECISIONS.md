# UI Decisions

## Purpose

This document records why current UI choices were made for the server/demo branch. It is product-facing architectural memory, not runtime instruction.

## Why Cinematic UI Was Selected

Cinematic UI was selected to make the product legible quickly in a demo setting.

Enterprise audiences often need to understand a complex technical product in a short presentation. A cinematic first impression helps establish seriousness, narrative clarity, and product identity before the deeper audit and API surfaces appear.

The cinematic layer must remain grounded. It should support inspection and explanation, not imply hidden autonomous control.

## Why Dark Enterprise UI Was Selected

Dark enterprise UI was selected because the demo should feel like an operational control surface rather than a marketing page.

The dark theme supports:

- boardroom presentation
- clear focus on validation status
- audit viewer contrast
- technical credibility
- reduced visual distraction

The dark theme should remain restrained and readable. It should not become decorative at the expense of clarity.

## Why Audit-First Presentation Matters

Audit-first presentation matters because SAPIANTA's strongest current product value is inspectability.

The demo should make it easy to answer:

- what decision was inspected
- what validation result was shown
- what explanation is available
- what evidence can be reviewed
- what is not currently implemented

Audit-first presentation helps prevent overclaiming because it keeps attention on visible evidence.

## Why Explainability Visibility Matters

Explainability visibility matters because enterprise viewers need to understand why a validation result appears.

The UI should show explanations in a way that is clear, concise, and linked to the decision scenario. Explanation should be presented as product transparency, not as a guarantee of correctness or legal sufficiency.

## Why Governance Visibility Matters

Governance visibility matters as a product narrative because regulated AI buyers care about boundaries, responsibility, and traceability.

In the demo branch, governance visibility must remain presentation-oriented. It should help explain structure and future direction without activating runtime governance, enforcement, or policy engine behavior.
