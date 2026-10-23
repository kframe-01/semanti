---
aliases: [Test Type]
tags: [glossary]
bounded_context: "Sequence and Process Authoring"
status: proposed
source: "UST-011; UST-025"
date_created: "2026-09-29"
last_reviewed: "2026-10-22"
---

# Test Type

## Definition

A functional mode applied to a test sequence that determines which operations are permitted during that test. Test Types include GoldenSample, SystemVerification, SerialTest, SerialAfterReparation, and customized types. For example, GoldenSample and SystemVerification exclude operations that alter the product.

## Usage

A Testing Engineer applies the GoldenSample Test Type to a sequence so that product-altering operations are not executed during that test.

## Boundaries

- Includes: A sequence-level functional classification and the execution rules associated with it, including rules that exclude certain operations.
- Does not include: The kind or structure of an individual step, which is represented by its Step Type.

## Related terms

- [[CMP-009-SPA-step-type|Step Type]] - Classifies an individual operation or control-flow step; Test Type rules govern its eligibility during a test.
- [[CMP-006-SPA-position-sequence|Position Sequence]] - A Test Type is applied to a sequence.

## Sources and open questions

- Source notes: [[UST-011-step-types-abstraction]], [[UST-025-continuous-validation-and-approval-workflow]]
- Open questions: What execution rules apply to each built-in and customized Test Type, and how are conflicting or unsupported step configurations handled?
