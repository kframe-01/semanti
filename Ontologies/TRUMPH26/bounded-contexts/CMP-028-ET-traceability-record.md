---
aliases: [Traceability Record]
tags: [glossary]
bounded_context: "Evidence and Traceability"
status: proposed
source: "UST-003; UST-013"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Traceability Record

## Definition

An association that lets reviewers identify the intent version, position, execution, artifact versions, configuration, and inputs behind resulting evidence.

## Usage

The reviewer uses a Traceability Record to find which Test Intent version and artifacts were used for an Execution Log.

## Boundaries

- Includes: Identifiable relationships between inputs, a run, and its outputs.
- Does not include: Proof that the resulting test or product passed.

## Related terms

- [[CMP-019-EO-position-execution|Position Execution]] - The run being linked.
- [[CMP-027-ET-execution-log|Execution Log]] - One linked output.

## Sources and open questions

- Source notes: [[UST-003-artifactory-and-data]], [[UST-013-worker-is-a-complice]]
- Open questions: Which identifiers and version metadata must each link retain?
