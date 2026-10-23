---
aliases: [Artifact Repository]
tags: [glossary]
bounded_context: "Artifact and Runtime Data"
status: proposed
source: "UST-003"
date_created: "2026-09-29"
last_reviewed: "2026-10-05"
---

# Artifact Repository

## Definition

A proposed phase-two governed capability for searching, publishing, retrieving, and versioning shared reusable artifacts, distinct from the phase-one Data Manager and its storage backends.

## Usage

In the second project phase, a Testing Engineer retrieves an approved reusable artifact from the Artifact Repository before releasing a position.

## Boundaries

- Includes in phase two: Authoritative lifecycle and traceability for shared reusable artifacts.
- Does not include: Phase-one storage and retrieval of position artifacts, test inputs and fixtures, execution data and evidence, or temporary development data; a decision to use a particular product called Artifactory; or an assumption that a local copy is authoritative.

## Related terms

- [[CMP-032-ARD-shared-reusable-artifact|Shared Reusable Artifact]] - One kind of governed content.
- [[CMP-030-ARD-artifact-scope|Artifact Scope]] - Ownership and lifecycle classification independent of access mode.

## Sources and open questions

- Source note: [[UST-003-artifactory-and-data]] identifies repository governance for shared reusable artifacts as future phase-two scope.
- Open questions: Is Artifactory a product requirement or shorthand for this repository capability, and which phase-two lifecycle operations must it support?
