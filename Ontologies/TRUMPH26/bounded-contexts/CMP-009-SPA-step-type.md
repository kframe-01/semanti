---
aliases: [Step Type]
tags: [glossary]
bounded_context: "Sequence and Process Authoring"
status: proposed
source: "UST-011"
date_created: "2026-09-29"
last_reviewed: "2026-10-22"
---

# Step Type

## Definition

A classification of a sequence step that defines the kind of operation or control-flow behavior the step represents. Step Types include Assignment, gRPCCall, Looping, Branching, and custom step types.

## Usage

A Testing Engineer selects a gRPCCall Step Type to configure a remote procedure call in a Position Sequence.

## Boundaries

- Includes: Operation and control-flow categories used to define and configure individual sequence steps, including customized types.
- Does not include: The test-wide functional mode or execution rules that determine whether steps may run.

## Related terms

- [[CMP-010-SPA-test-type|Test Type]] - Applies functional execution rules to a sequence; distinct from the type of an individual step.
- [[CMP-006-SPA-position-sequence|Position Sequence]] - Contains steps classified by Step Type.

## Sources and open questions

- Source note: [[UST-011-step-types-abstraction]]
- Open questions: Which built-in and customized Step Types are supported, and how are their parameters and constraints defined?
