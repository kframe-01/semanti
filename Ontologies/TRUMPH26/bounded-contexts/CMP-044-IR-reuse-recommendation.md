---
aliases: [Reuse Recommendation]
tags: [glossary]
bounded_context: "Intent and Requirements"
status: proposed
source: "UST-024; UST-025"
date_created: "2026-10-22"
last_reviewed: "2026-10-22"
---

# Reuse Recommendation

## Definition

A reviewable proposal to share an identified subset of test logic across
products, supported by the matching products, shared steps, parameter
differences, and rationale.

## Usage

The Product Owner and Testing Engineer review a Reuse Recommendation before
deciding whether to adopt the shared sequence logic.

## Boundaries

- Includes: Analysis evidence and a proposed reusable subset.
- Does not include: Approval, implementation, or project generation.

## Related terms

- [[CMP-032-ARD-shared-reusable-artifact|Shared Reusable Artifact]] - May result from an accepted recommendation.
- [[CMP-040-IR-product-variant|Product Variant]] - The products whose test logic is compared.

## Sources and open questions

- Source notes: [[UST-024-product-variant-management-and-reuse-optimization]], [[UST-025-continuous-validation-and-approval-workflow]]
- Open questions: Are recommendations reviewed individually or in batches, and how are they ranked and versioned?
