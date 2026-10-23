---
aliases: [Station]
tags: [glossary]
bounded_context: "Station and Deployment"
status: proposed
source: "UST-005"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Station

## Definition

A target for deploying and executing a position sequence, with connected hardware components that provide concrete operations and capabilities.

## Usage

The Testing Engineer selects a Station whose components can satisfy a sequence's abstract hardware requirements.

## Boundaries

- Includes: Station identity and its connected equipment.
- Does not include: The reusable Position Sequence or a manufacturing Position in an ERP workplane.

## Related terms

- [[CMP-014-SD-station-description|Station Description]] - Records the station's components and capabilities.
- [[CMP-001-SPA-position|Position]] - A different, manufacturing concept.

## Sources and open questions

- Source note: [[UST-005-semantic-station-globals]]
- Open questions: Which station attributes and physical checks establish current configuration?
