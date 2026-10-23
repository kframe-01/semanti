---
aliases: [Position Execution]
tags: [glossary]
bounded_context: "Execution Orchestration"
status: proposed
source: "UST-008; UST-009"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Position Execution

## Definition

An identifiable run of a manufacturing position with its own current or final state, configured mode, target, and associated results.

## Usage

Two Position Executions of the same Position can be monitored and reviewed separately.

## Boundaries

- Includes: Execution identity and the state of this particular run.
- Does not include: The manufacturing Position definition or a historical log by itself.

## Related terms

- [[CMP-001-SPA-position|Position]] - The manufacturing position being run.
- [[CMP-020-EO-execution-mode|Execution Mode]] - Classifies how this run operates.

## Sources and open questions

- Source notes: [[UST-008-how-it-looks-like-in-runtime]], [[UST-009-executions-have-colours]]
- Open questions: What identifies an execution and which state transitions are valid?
