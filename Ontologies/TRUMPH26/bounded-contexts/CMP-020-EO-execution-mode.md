---
aliases: [Execution Mode]
tags: [glossary]
bounded_context: "Execution Orchestration"
status: proposed
source: "UST-009"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Execution Mode

## Definition

A configuration associated with an individual execution that distinguishes how it runs, such as white-op, from normal physical operation.

## Usage

The Testing Engineer selects an Execution Mode before starting a Position Execution.

## Boundaries

- Includes: Mode recorded and displayed for a particular execution.
- Does not include: Execution color, which may represent a separate classification.

## Related terms

- [[CMP-021-EO-white-op|White-op]] - Proposed dry-run mode.
- [[CMP-019-EO-position-execution|Position Execution]] - Run to which the mode applies.

## Sources and open questions

- Source note: [[UST-009-executions-have-colours]]
- Open questions: Which modes exist, and can the mode change after a run starts?
