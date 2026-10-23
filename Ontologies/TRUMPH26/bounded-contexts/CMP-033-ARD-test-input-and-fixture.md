---
aliases: [Test Input and Fixture]
tags: [glossary]
bounded_context: "Artifact and Runtime Data"
status: proposed
source: "UST-003"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Test Input and Fixture

## Definition

Controlled input material needed to run a test, including input files, reference values, calibration or simulation fixtures, and datasets.

## Usage

The runtime resolves the exact Test Input and Fixture version required by the Position Execution.

## Boundaries

- Includes: Inputs associated with the consuming position or test revision.
- Does not include: Measurements or logs produced by that execution.

## Related terms

- [[CMP-029-ET-execution-evidence|Execution Evidence]] - Output produced using these inputs.
- [[CMP-030-ARD-artifact-scope|Artifact Scope]] - Classifies inputs separately from evidence.

## Sources and open questions

- Source note: [[UST-003-artifactory-and-data]]
- Open questions: Which fixtures need calibration status or retention metadata?
