---
aliases: [Process Model]
tags: [glossary]
bounded_context: "Sequence and Process Authoring"
status: proposed
source: "UST-006"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Process Model

## Definition

A reusable unit of process behavior maintained separately from a position sequence and exposed through named entry points with defined contracts.

## Usage

Two Position Sequences invoke the same Process Model without duplicating its internal steps.

## Boundaries

- Includes: Reusable process behavior and its entry-point contracts.
- Does not include: Position-specific ordering and decisions retained by the consuming sequence.

## Related terms

- [[CMP-006-SPA-position-sequence|Position Sequence]] - Invokes reusable behavior.
- [[CMP-008-SPA-entry-point|Entry Point]] - Named interface exposed to a sequence.

## Sources and open questions

- Source note: [[UST-006-process-model-entry-points]]
- Open questions: Which responsibilities belong in a Process Model rather than a sequence?
