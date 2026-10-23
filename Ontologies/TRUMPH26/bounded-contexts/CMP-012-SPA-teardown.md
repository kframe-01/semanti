---
aliases: [Teardown]
tags: [glossary]
bounded_context: "Sequence and Process Authoring"
status: proposed
source: "UST-012"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Teardown

## Definition

Reusable cleanup behavior attempted after a test body, including applicable failure or interruption paths, to release resources or leave equipment in an appropriate state.

## Usage

After a test fails, Teardown is attempted and its failure, if any, is reported separately from the test failure.

## Boundaries

- Includes: Defined cleanup actions and their lifecycle ordering.
- Does not include: The test outcome itself; not every cleanup action is safe to automate.

## Related terms

- [[CMP-011-SPA-setup|Setup]] - Prepares resources before the test body.

## Sources and open questions

- Source note: [[UST-012-teardowning]]
- Open questions: At which scopes and after which interruption modes must cleanup be attempted?
