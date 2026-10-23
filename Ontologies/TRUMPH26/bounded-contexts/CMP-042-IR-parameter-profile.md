---
aliases: [Parameter Profile, Base Profile]
tags: [glossary]
bounded_context: "Intent and Requirements"
status: proposed
source: "UST-001; UST-024; UST-025"
date_created: "2026-10-22"
last_reviewed: "2026-10-22"
---

# Parameter Profile

## Definition

A named set of default parameter values associated with a product or product
family, used as a baseline when describing test behavior for its variants.

## Usage

A test intent refers to a base Parameter Profile and records a product-specific
exception where a variant needs a different parameter value.

## Boundaries

- Includes: Baseline parameter values used to describe variant differences.
- Does not include: The rules for inheriting, validating, or applying those values.

## Related terms

- [[CMP-040-IR-product-variant|Product Variant]] - May use baseline values with product-specific differences.
- [[CMP-043-IR-parameter-override|Parameter Override]] - Records an exception to a profile value.

## Sources and open questions

- Source notes: [[UST-001-natural-and-formal-description]], [[UST-024-product-variant-management-and-reuse-optimization]], [[UST-025-continuous-validation-and-approval-workflow]]
- Open questions: How are profiles selected, versioned, inherited, and validated?
