---
aliases: [Abstract Equipment Capability]
tags: [glossary]
bounded_context: "Station and Deployment"
status: proposed
source: "UST-004; UST-005; DEC-002"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Abstract Equipment Capability

## Definition

A hardware ability required by a position sequence without naming a specific station, device model, or driver; deployment must find a compatible concrete operation.

## Usage

The sequence requests an Abstract Equipment Capability that two different Stations can each satisfy.

## Boundaries

- Includes: Technology-independent equipment requirements and operations.
- Does not include: The chosen concrete component or station-specific binding.

## Related terms

- [[CMP-017-SD-deployment-binding|Deployment Binding]] - Selects a compatible concrete realization.
- [[CMP-006-SPA-position-sequence|Position Sequence]] - Expresses the abstract requirement.

## Sources and open questions

- Source notes: [[UST-004-hal-in-the-actors]], [[UST-005-semantic-station-globals]], [[DEC-002-the-abstraction-of-hardware]]
- Open questions: How are capability limits, modes, and contract versions represented?
