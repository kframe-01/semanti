---
aliases: [Hardware Component]
tags: [glossary]
bounded_context: "Station and Deployment"
status: proposed
source: "UST-005"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Hardware Component

## Definition

A concrete piece of equipment connected to a station, described by the capabilities and operations it supports.

## Usage

A Deployment Binding selects a Hardware Component on the target Station for an abstract equipment requirement.

## Boundaries

- Includes: Station-specific equipment identity and supported operations.
- Does not include: The abstract requirement written in the reusable sequence.

## Related terms

- [[CMP-013-SD-station|Station]] - Hosts the component.
- [[CMP-016-SD-abstract-equipment-capability|Abstract Equipment Capability]] - What the sequence requests independently of a device.

## Sources and open questions

- Source note: [[UST-005-semantic-station-globals]]
- Open questions: Which component attributes, connections, and availability checks are required?
