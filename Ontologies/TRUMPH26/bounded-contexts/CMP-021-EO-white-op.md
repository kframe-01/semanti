---
aliases: [White-op, Dry Run]
tags: [glossary]
bounded_context: "Execution Orchestration"
status: proposed
source: "UST-009"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# White-op

## Definition

A proposed dry-run Execution Mode for testing or debugging runtime components, explicitly distinguishable from normal physical operation.

## Usage

A Testing Engineer starts a White-op execution and sees its mode alongside the run's results.

## Boundaries

- Includes: A per-execution dry-run designation and its visibility.
- Does not include: A settled rule for hardware actuation or an assumption that White-op equals station simulation.

## Related terms

- [[CMP-020-EO-execution-mode|Execution Mode]] - Category to which White-op belongs.
- [[CMP-018-SD-simulated-station|Simulated Station]] - Related but not necessarily identical approach.

## Sources and open questions

- Source note: [[UST-009-executions-have-colours]]
- Open questions: Which physical operations, if any, occur in White-op?
