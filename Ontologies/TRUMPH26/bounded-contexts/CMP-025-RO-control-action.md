---
aliases: [Control Action]
tags: [glossary]
bounded_context: "Runtime Operations"
status: proposed
source: "UST-008"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Control Action

## Definition

An authorized, state-dependent request to influence a running position execution, with an explicit accepted or rejected outcome.

## Usage

The Maintenance Technician requests a Control Action and checks whether the runtime confirms the new execution state.

## Boundaries

- Includes: Permission, availability in the current state, and confirmation of the request's outcome.
- Does not include: An assumption that an unconfirmed request changed a live station.

## Related terms

- [[CMP-024-RO-runtime-view|Runtime View]] - Presents available actions and their outcomes.

## Sources and open questions

- Source note: [[UST-008-how-it-looks-like-in-runtime]]
- Open questions: Are pause, resume, abort, and stop supported, and what are their exact effects?
