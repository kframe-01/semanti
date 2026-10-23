---
aliases: [Setup]
tags: [glossary]
bounded_context: "Sequence and Process Authoring"
status: proposed
source: "UST-012"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Setup

## Definition

Reusable preparation behavior performed before a test body so that required resources or conditions are ready.

## Usage

A test declares Setup that prepares equipment before its test body runs.

## Boundaries

- Includes: Preparation with a defined place in the test lifecycle.
- Does not include: The test body or post-test cleanup.

## Related terms

- [[CMP-012-SPA-teardown|Teardown]] - Cleanup attempted after the test body.

## Sources and open questions

- Source note: [[UST-012-teardowning]]
- Open questions: Which setup scopes, such as per test or per sequence, are needed?
