---
aliases: [Execution Log]
tags: [glossary]
bounded_context: "Evidence and Traceability"
status: proposed
source: "UST-013"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Execution Log

## Definition

The log produced by a particular execution, containing recorded behavior and outcomes that can be compared with the version of the Test Intent used for that run.

## Usage

A Maintenance Technician reviews the Execution Log against the expected behavior in the associated Test Intent.

## Boundaries

- Includes: Recorded events, outcomes, and relevant execution context.
- Does not include: The technician's assessment of whether the log is complete or consistent.

## Related terms

- [[CMP-003-IR-test-intent|Test Intent]] - States the expected behavior for comparison.
- [[CMP-034-QA-log-assessment|Log Assessment]] - Records the reviewer's judgment.

## Sources and open questions

- Source note: [[UST-013-worker-is-a-complice]]
- Open questions: Which events and measurements are required to assess a log?
