---
aliases: [Station Description]
tags: [glossary]
bounded_context: "Station and Deployment"
status: proposed
source: "UST-005"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Station Description

## Definition

A structured account of a station's identity, connected hardware components, their capabilities, and supported concrete operations, used to assess deployment compatibility.

## Usage

Before deployment, the system compares a Position Sequence's requirements against the Station Description.

## Boundaries

- Includes: Described station configuration and available operations.
- Does not include: The sequence's test procedure or a guarantee that currently connected hardware matches the description.

## Related terms

- [[CMP-013-SD-station|Station]] - The described target.
- [[CMP-017-SD-deployment-binding|Deployment Binding]] - Mapping validated against the description.

## Sources and open questions

- Source note: [[UST-005-semantic-station-globals]]
- Open questions: How are descriptions versioned and checked against physical hardware?
