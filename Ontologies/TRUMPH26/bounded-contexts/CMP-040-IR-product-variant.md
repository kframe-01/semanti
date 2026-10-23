---
aliases: [Product Variant]
tags: [glossary]
bounded_context: "Intent and Requirements"
status: proposed
source: "UST-001; UST-024; UST-025"
date_created: "2026-10-22"
last_reviewed: "2026-10-22"
---

# Product Variant

## Definition

A product configuration in a product portfolio that may share test logic with
other configurations while having its own parameter values, limits, or
variant-specific steps.

## Usage

A Product Owner compares two Product Variants to identify shared sequence logic
and the differences that require product-specific handling.

## Boundaries

- Includes: Differences relevant to test intent, sequence steps, parameters, and limits.
- Does not include: Runtime product-serialization mapping or test-limit selection.

## Related terms

- [[CMP-003-IR-test-intent|Test Intent]] - Describes the intended test behavior for a product.
- [[CMP-041-IR-variable-scope|Variable Scope]] - Determines where declared variables are available.

## Sources and open questions

- Source notes: [[UST-001-natural-and-formal-description]], [[UST-024-product-variant-management-and-reuse-optimization]], [[UST-025-continuous-validation-and-approval-workflow]]
- Open questions: How are product variants identified, grouped, and related to product families?
