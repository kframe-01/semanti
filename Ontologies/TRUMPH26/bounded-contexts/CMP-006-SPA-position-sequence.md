---
aliases: [Position Sequence]
tags: [glossary]
bounded_context: "Sequence and Process Authoring"
status: proposed
source: "UST-004; UST-006"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Position Sequence

## Definition

An authored description of position-specific test behavior and ordering that can invoke reusable processes and refer to abstract equipment rather than station-specific devices.

## Usage

A Testing Engineer authors a Position Sequence and later deploys it to a compatible station.

## Boundaries

- Includes: Position-specific flow, decisions, and abstract hardware needs.
- Does not include: Concrete station bindings or the internals of reusable process behavior.

## Related terms

- [[CMP-001-SPA-position|Position]] - Manufacturing position for which the sequence is authored.
- [[CMP-007-SPA-process-model|Process Model]] - Supplies reusable behavior called from the sequence.

## Sources and open questions

- Source notes: [[UST-004-hal-in-the-actors]], [[UST-006-process-model-entry-points]]
- Open questions: Which sequencing technologies and sequence constructs must be supported?
