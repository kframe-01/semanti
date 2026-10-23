---
aliases: [Continuous Validation]
tags: [glossary]
bounded_context: "Quality Assurance"
status: proposed
source: "UST-025"
date_created: "2026-10-22"
last_reviewed: "2026-10-22"
---

# Continuous Validation

## Definition

Repeated validation of a sequence during authoring or modification, checking
its structure, required steps, variant-specific parameters and limits, and
step-specific execution rules.

## Usage

As a Testing Engineer changes a sequence, Continuous Validation reports an
actionable error for a missing required step or an out-of-range parameter.

## Boundaries

- Includes: Authoring-time checks and feedback about sequence validity.
- Does not include: Human approval or runtime selection of product-specific test limits.

## Related terms

- [[CMP-006-SPA-position-sequence|Position Sequence]] - The authored artifact being validated.
- [[CMP-046-QA-sequence-approval|Sequence Approval]] - Follows validation before integration.

## Sources and open questions

- Source note: [[UST-025-continuous-validation-and-approval-workflow]]
- Open questions: Which rules run on every edit, and which are deferred until a sequence is submitted?
