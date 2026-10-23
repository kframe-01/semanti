---
aliases: [Runtime View]
tags: [glossary]
bounded_context: "Runtime Operations"
status: proposed
source: "UST-008"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Runtime View

## Definition

The live view of a selected position execution used to inspect its identity, mode, target, state, progress, and available control actions.

## Usage

A Maintenance Technician opens the Runtime View to see the current step and respond to an execution warning.

## Boundaries

- Includes: Current execution information and feedback on requested actions.
- Does not include: Editing the sequence or silently treating stale status as current.

## Related terms

- [[CMP-019-EO-position-execution|Position Execution]] - Run shown by the view.
- [[CMP-025-RO-control-action|Control Action]] - State-dependent operation requested from the view.

## Sources and open questions

- Source note: [[UST-008-how-it-looks-like-in-runtime]]
- Open questions: Which progress data and update frequency are required?
