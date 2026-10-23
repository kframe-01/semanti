---
aliases: [Test Execution Type]
tags: [glossary]
bounded_context: "Quality Assurance"
status: proposed
source: "UST-025"
date_created: "2026-10-22"
last_reviewed: "2026-10-22"
---

# Test Execution Type

## Definition

A classification of a test run, such as Serial, Validation, or GoldenSample,
that can determine which step-specific rules apply during sequence validation.

## Usage

Validation checks that a step configured for a GoldenSample run follows the
rules defined for that Test Execution Type.

## Boundaries

- Includes: The execution classification and its associated step-specific validation rules.
- Does not include: Runtime product-serialization mapping or a complete execution lifecycle model.

## Related terms

- [[CMP-045-QA-continuous-validation|Continuous Validation]] - Checks configured steps against the applicable rules.
- [[CMP-006-SPA-position-sequence|Position Sequence]] - Contains steps whose configuration may depend on the type.

## Sources and open questions

- Source note: [[UST-025-continuous-validation-and-approval-workflow]]
- Open questions: What are the complete set of types, their definitions, and their step-specific rules?
