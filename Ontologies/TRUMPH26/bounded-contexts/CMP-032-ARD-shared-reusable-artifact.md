---
aliases: [Shared Reusable Artifact]
tags: [glossary]
bounded_context: "Artifact and Runtime Data"
status: proposed
source: "UST-003"
date_created: "2026-09-29"
last_reviewed: "2026-10-05"
---

# Shared Reusable Artifact

## Definition

A reviewed, versioned artifact intended for use by more than one position, such as a test component, template, library, or equipment abstraction.

## Usage

In the second project phase, the Testing Engineer retrieves an approved Shared Reusable Artifact for a new position project.

## Boundaries

- Includes in phase two: Published dependencies reusable across positions.
- Does not include: The four data scopes handled by the phase-one Data Manager or an unpublished local copy treated as authoritative.

## Related terms

- [[CMP-030-ARD-artifact-scope|Artifact Scope]] - Defines its proposed lifecycle category.
- [[CMP-031-ARD-position-artifact|Position Artifact]] - Material specific to one position.

## Sources and open questions

- Source note: [[UST-003-artifactory-and-data]] identifies this as future phase-two scope.
- Open questions: What approval, compatibility, publication, discovery, deprecation, and immutability rules apply in phase two?
