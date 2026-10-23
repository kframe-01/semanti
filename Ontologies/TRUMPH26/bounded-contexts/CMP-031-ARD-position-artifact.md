---
aliases: [Position Artifact]
tags: [glossary]
bounded_context: "Artifact and Runtime Data"
status: proposed
source: "UST-003"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Position Artifact

## Definition

An artifact specific to one manufacturing position, such as its generated project, test logic, configuration, deployment bindings, or documentation.

## Usage

The Testing Engineer reviews and releases the Position Artifacts for one Position.

## Boundaries

- Includes: Position-specific material developed, versioned, reviewed, and released for a position.
- Does not include: Shared reusable dependencies or results produced by an execution.

## Related terms

- [[CMP-001-SPA-position|Position]] - The manufacturing position to which the artifact belongs.
- [[CMP-030-ARD-artifact-scope|Artifact Scope]] - The classification governing its lifecycle.

## Sources and open questions

- Source note: [[UST-003-artifactory-and-data]]
- Open questions: Which parts of a generated project are published and independently versioned?
