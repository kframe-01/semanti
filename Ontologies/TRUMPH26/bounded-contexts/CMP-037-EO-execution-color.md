---
aliases: [Execution Color]
tags: [glossary]
bounded_context: "Execution Orchestration"
status: proposed
source: "UST-009"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Execution Color

## Definition

A per-execution visual classification proposed to help distinguish runs, displayed together with a textual label.

## Usage

The runtime view shows the assigned Execution Color and a label for a selected run.

## Boundaries

- Includes: An assigned color retained with the execution and visible in runtime and history views.
- Does not include: The Execution Mode or a color-only indication of meaning.

## Related terms

- [[CMP-019-EO-position-execution|Position Execution]] - Run that carries the assigned color.
- [[CMP-020-EO-execution-mode|Execution Mode]] - Separate configuration unless discovery decides otherwise.

## Sources and open questions

- Source note: [[UST-009-executions-have-colours]]
- Open questions: Which colors are allowed, what do they mean, and who assigns them?
