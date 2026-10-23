---
aliases: [Hardware Abstraction Layer, HAL]
tags: [glossary]
bounded_context: "Execution Orchestration"
status: proposed
source: "UST-004; DEC-002"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Hardware Abstraction Layer

## Definition

The interpreter-based boundary through which sequences request abstract equipment operations and those requests are handled by compatible concrete hardware implementations.

## Usage

During execution, the Hardware Abstraction Layer directs an abstract operation to the appropriate hardware actor and returns its outcome.

## Boundaries

- Includes: Interpreting hardware requests and exposing observable results or errors.
- Does not include: Station-specific device identifiers in the sequence or the choice of a specific actor framework product.

## Related terms

- [[CMP-016-SD-abstract-equipment-capability|Abstract Equipment Capability]] - Requirement exposed to sequence authors.
- [[CMP-017-SD-deployment-binding|Deployment Binding]] - Connects the request to station equipment.

## Sources and open questions

- Source notes: [[UST-004-hal-in-the-actors]], [[DEC-002-the-abstraction-of-hardware]]
- Open questions: What result, error, and timeout contracts must every hardware operation support?
