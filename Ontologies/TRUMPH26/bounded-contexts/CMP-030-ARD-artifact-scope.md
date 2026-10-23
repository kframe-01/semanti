---
aliases: [Artifact Scope]
tags: [glossary]
bounded_context: "Artifact and Runtime Data"
status: proposed
source: "UST-003"
date_created: "2026-09-29"
last_reviewed: "2026-10-05"
---

# Artifact Scope

## Definition

A classification of an artifact or data item by its purpose and association, independently of the storage backend used to access it.

## Usage

A Testing Engineer stores a generated project as a Position Artifact through the phase-one Data Manager.

## Boundaries

- Includes in phase one: Position-specific artifacts, test inputs and fixtures, execution data and evidence, and temporary development data.
- Does not include in phase one: Shared reusable artifacts, which are deferred to the second project phase, or the choice of storage backend.

## Related terms

- [[CMP-031-ARD-position-artifact|Position Artifact]] - One proposed scope.
- [[CMP-029-ET-execution-evidence|Execution Evidence]] - Another proposed scope of stored outputs.

## Sources and open questions

- Source note: [[UST-003-artifactory-and-data]]
- Open questions: Which lifecycle rules should be added to the phase-one scopes, and how should shared reusable artifacts be governed in phase two?
