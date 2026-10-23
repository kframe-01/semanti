---
aliases: [Variable Scope]
tags: [glossary]
bounded_context: "Sequence and Process Authoring"
status: proposed
source: "UST-001; UST-002; UST-023"
date_created: "2026-10-22"
last_reviewed: "2026-10-22"
---

# Variable Scope

## Definition

The declared level at which a variable is available and initialized, defining
whether it belongs to a step instance, a sequence instance, or a station.

## Usage

When authoring a sequence, the user declares whether a variable is Local,
Sequence Global, or Station Global.

## Boundaries

- Includes: Local, Sequence Global, and Station Global availability and initialization levels.
- Does not include: The variable's data type, value, or persistence policy.

## Related terms

- [[CMP-006-SPA-position-sequence|Position Sequence]] - A scope for Sequence Global variables.
- In another context: [[CMP-003-IR-test-intent|Test Intent]] - Declares variable scopes for downstream use.

## Sources and open questions

- Source notes: [[UST-001-natural-and-formal-description]], [[UST-002-dsl-to-poject]], [[UST-023-accessible-sequence-authoring-with-typed-steps]]
- Open questions: How do Station Global initialization, persistence, and name conflicts work?
