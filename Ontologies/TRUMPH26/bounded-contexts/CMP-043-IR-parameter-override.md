---
aliases: [Parameter Override]
tags: [glossary]
bounded_context: "Intent and Requirements"
status: proposed
source: "UST-001; UST-024; UST-025"
date_created: "2026-10-22"
last_reviewed: "2026-10-22"
---

# Parameter Override

## Definition

A product- or variant-specific exception that supplies a parameter value or
limit different from the applicable baseline profile.

## Usage

During variant comparison, the system records the Parameter Override needed
when a product uses a different test limit from the base profile.

## Boundaries

- Includes: Explicit differences from baseline parameter values or limits.
- Does not include: The inheritance or precedence rules used to apply the difference.

## Related terms

- [[CMP-042-IR-parameter-profile|Parameter Profile]] - Supplies the baseline being overridden.
- [[CMP-040-IR-product-variant|Product Variant]] - Identifies the product configuration to which the exception applies.

## Sources and open questions

- Source notes: [[UST-001-natural-and-formal-description]], [[UST-024-product-variant-management-and-reuse-optimization]], [[UST-025-continuous-validation-and-approval-workflow]]
- Open questions: Which parameter types can be overridden, and how are conflicts and valid ranges handled?
