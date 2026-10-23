---
aliases: [Execution Evidence]
tags: [glossary]
bounded_context: "Evidence and Traceability"
status: proposed
source: "UST-003; UST-007"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Execution Evidence

## Definition

Recorded results of an execution, such as measurements, logs, reports, and verdicts, kept with the context needed for later diagnosis or verification.

## Usage

After a run, a reviewer retrieves Execution Evidence associated with its Position Execution and input revisions.

## Boundaries

- Includes: Recorded outputs with an identifiable source execution.
- Does not include: Unpromoted temporary development data; simulated results must not be mistaken for physical test evidence.

## Related terms

- [[CMP-028-ET-traceability-record|Traceability Record]] - Connects evidence to its inputs and execution.
- [[CMP-027-ET-execution-log|Execution Log]] - One kind of recorded output.

## Sources and open questions

- Source notes: [[UST-003-artifactory-and-data]], [[UST-007-easy-testing]]
- Open questions: Which outputs qualify as governed quality evidence rather than diagnostic data?
