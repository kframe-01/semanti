---
aliases: [Actor]
tags: [glossary]
bounded_context: "Execution Orchestration"
status: proposed
source: "DEC-001; UST-004"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Actor

## Definition

An independent system component that encapsulates its own state and behavior and communicates with other components by exchanging messages.

## Usage

A hardware Actor handles an operation request without exposing its driver or internal state to the sequence.

## Boundaries

- Includes: Component responsibility and message-based interaction.
- Does not include: A specific actor-framework product, transport, or delivery guarantee.

## Related terms

- [[CMP-022-EO-hardware-abstraction-layer|Hardware Abstraction Layer]] - Uses actors for hardware interactions.

## Sources and open questions

- Source notes: [[DEC-001-the-actor-framework]], [[UST-004-hal-in-the-actors]]
- Open questions: What message, retry, and failure semantics will the runtime use?
