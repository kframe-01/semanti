---
aliases: [Operator Interface]
tags: [glossary]
bounded_context: "Runtime Operations"
status: proposed
source: "UST-010"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Operator Interface

## Definition

The shop-floor worker's task-focused interface to a position, showing needed instructions, current state, permitted actions, and access to relevant supporting information.

## Usage

The worker uses the Operator Interface to provide required input and respond to an interruption during production.

## Boundaries

- Includes: Role-appropriate position guidance and interaction.
- Does not include: Unrestricted maintenance controls or engineering details unrelated to the worker's task.

## Related terms

- [[CMP-024-RO-runtime-view|Runtime View]] - Related live view for maintenance monitoring and control.

## Sources and open questions

- Source note: [[UST-010-simple-user-experience]]
- Open questions: Which tasks and additional information should be available to each shop-floor role?
