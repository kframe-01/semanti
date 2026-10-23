---
aliases: [Domain-Specific Language, DSL]
tags: [glossary]
bounded_context: "Intent and Requirements"
status: proposed
source: "UST-001; UST-002"
date_created: "2026-09-29"
last_reviewed: "2026-10-05"
---

# Domain-Specific Language

## Definition

Robot Framework's plain-text `.robot` format, using the project convention `Given that ...`, `When ...`, and `Then ...`, for expressing Test Intents that remain understandable to stakeholders and can be interpreted for downstream refinement and project generation.

## Usage

A Testing Engineer supplies an accepted `.robot` Test Intent to the LabVIEW project generator.

## Boundaries

- Includes: The `.robot` representation, BDD-style scenario structure, and a controlled domain keyword vocabulary governed by DEC-003.
- Does not include: The generated project, concrete equipment bindings, or a requirement for the manufacturing runtime to execute Robot Framework directly.

## Related terms

- [[CMP-003-IR-test-intent|Test Intent]] - Meaning that the language must preserve.

## Sources and open questions

- Source notes: [[UST-001-natural-and-formal-description]], [[UST-002-dsl-to-poject]]
- Decision record: [[DEC-003-use-robot-language-for-test-intents]]
- Open questions: Which `.robot` sections, metadata, keywords, arguments, and semantic validation rules are required for project generation?
