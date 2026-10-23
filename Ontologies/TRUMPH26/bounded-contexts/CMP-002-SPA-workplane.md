---
aliases:
  - Workplane
tags:
  - glossary
bounded_context: "Sequence and Process Authoring"
status: proposed
source: "UST-002"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Workplane

## Definition

A workplane downloaded from the ERP system that identifies manufacturing positions and provides position data used when generating a LabVIEW project from a test intent.

## Usage

The system loads the ERP-downloaded Workplane and checks that it contains the Position referenced by the test intent before generating a project.

## Boundaries

- Includes: ERP-provided information needed to identify the manufacturing Position for project generation.
- Does not include: The generated LabVIEW project; the full scope of workplane data is not yet defined.

## Related terms

- [[CMP-001-SPA-position|Position]] - A manufacturing position identified in the Workplane.

## Sources and open questions

- Source note: [[UST-002-dsl-to-poject]]
- Open questions: Which ERP system and workplane format are supported? What other data does a Workplane contain, and which bounded context owns it?
