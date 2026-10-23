---
aliases: [Simulated Station]
tags: [glossary]
bounded_context: "Station and Deployment"
status: proposed
source: "UST-007"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Simulated Station

## Definition

A software representation of a target station and its relevant equipment that provides defined simulated responses to a position sequence without requiring physical hardware.

## Usage

A Testing Engineer runs a sequence on a computer against a Simulated Station while the physical station is unavailable.

## Boundaries

- Includes: Simulated capabilities and operation results for sequence development and verification.
- Does not include: Physical hardware operation or evidence of a physical test.

## Related terms

- [[CMP-013-SD-station|Station]] - Physical target represented by the simulation.
- [[CMP-016-SD-abstract-equipment-capability|Abstract Equipment Capability]] - Contract a simulator may satisfy.

## Sources and open questions

- Source note: [[UST-007-easy-testing]]
- Open questions: What fidelity and device-fault behavior must the simulator support?
