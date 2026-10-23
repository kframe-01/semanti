---
aliases: [Entry Point]
tags: [glossary]
bounded_context: "Sequence and Process Authoring"
status: proposed
source: "UST-006"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Entry Point

## Definition

A named way for a position sequence to invoke a Process Model through an explicit contract covering required inputs, preconditions, outputs, and failures.

## Usage

The sequence invokes an Entry Point and receives an observable outcome or actionable error.

## Boundaries

- Includes: The invocation contract visible to the sequence.
- Does not include: The Process Model's internal steps.

## Related terms

- [[CMP-007-SPA-process-model|Process Model]] - Exposes the Entry Point.

## Sources and open questions

- Source note: [[UST-006-process-model-entry-points]]
- Open questions: Is an Entry Point a callable operation, named process, actor message, or another construct?
