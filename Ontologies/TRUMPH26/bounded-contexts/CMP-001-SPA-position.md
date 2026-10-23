---
aliases:
  - Position
tags:
  - glossary
bounded_context: "Sequence and Process Authoring"
status: proposed
source: "UST-002"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Position

## Definition

A manufacturing position in the workplane downloaded from the ERP system.

## Usage

A Testing Engineer identifies a Position in the ERP-downloaded workplane when generating a LabVIEW project from a test intent.

## Boundaries

- Includes: The manufacturing position referenced by the workplane and the generated project.
- Does not include: To be clarified; whether a Position is distinct from a physical station is not yet defined.

## Related terms

- [[CMP-002-SPA-workplane|Workplane]] - Contains the manufacturing Position.

## Sources and open questions

- Source note: [[UST-002-dsl-to-poject]]
- Open questions: Is Position owned by Sequence and Process Authoring, or by another bounded context? How does it relate to a physical station?
