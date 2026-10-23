---
aliases: [Deployment Binding]
tags: [glossary]
bounded_context: "Station and Deployment"
status: proposed
source: "UST-005; DEC-002"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Deployment Binding

## Definition

An explicit, validated mapping from a sequence's abstract hardware requirement to a compatible concrete operation and component on a selected station.

## Usage

The deployer records a Deployment Binding before the sequence runs on the target Station.

## Boundaries

- Includes: The requirement, selected operation, hardware component, and target station.
- Does not include: Station-specific logic embedded in the reusable sequence.

## Related terms

- [[CMP-016-SD-abstract-equipment-capability|Abstract Equipment Capability]] - The requirement being realized.
- [[CMP-014-SD-station-description|Station Description]] - Describes the available components and operations.

## Sources and open questions

- Source notes: [[UST-005-semantic-station-globals]], [[DEC-002-the-abstraction-of-hardware]]
- Open questions: Who approves bindings, and when must a changed station invalidate them?
