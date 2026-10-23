---
aliases: [Temporary Development Data]
tags: [glossary]
bounded_context: "Artifact and Runtime Data"
status: proposed
source: "UST-003"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Temporary Development Data

## Definition

Disposable intermediate material from development or debugging, such as local caches, debug captures, or incomplete experiments, unless explicitly promoted to a governed artifact scope.

## Usage

A Testing Engineer keeps a debug capture as Temporary Development Data rather than treating it as released evidence.

## Boundaries

- Includes: Intermediate or local artifacts not yet governed for reuse or retention.
- Does not include: Published Position Artifacts or retained Execution Evidence.

## Related terms

- [[CMP-030-ARD-artifact-scope|Artifact Scope]] - Classifies temporary data separately from governed artifacts.
- [[CMP-029-ET-execution-evidence|Execution Evidence]] - Retained output that must not be confused with temporary data.

## Sources and open questions

- Source note: [[UST-003-artifactory-and-data]]
- Open questions: When and how can a temporary item be promoted into a governed scope?
