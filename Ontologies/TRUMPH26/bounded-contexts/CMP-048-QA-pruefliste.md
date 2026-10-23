---
aliases: [Prüfliste, Test Checklist]
tags: [glossary]
bounded_context: "Quality Assurance"
status: proposed
source: "UST-025"
date_created: "2026-10-22"
last_reviewed: "2026-10-22"
---

# Prüfliste

## Definition

A test checklist maintained as an Excel or CSV list alongside a Robot Framework
sequence description, with which it must remain synchronized.

## Usage

When a Prüfliste changes, the system checks whether its paired Robot Framework
description is out of sync and flags the discrepancy.

## Boundaries

- Includes: The checklist artifact and its synchronization relationship to a sequence description.
- Does not include: The Robot Framework description itself or an agreed source-of-truth policy.

## Related terms

- [[CMP-036-IR-domain-specific-language|Domain-Specific Language]] - Describes test intent and sequence behavior in the paired format.
- [[CMP-045-QA-continuous-validation|Continuous Validation]] - Validates sequence content, not checklist synchronization by itself.

## Sources and open questions

- Source note: [[UST-025-continuous-validation-and-approval-workflow]]
- Open questions: Is synchronization one-way or two-way, and which format is authoritative when changes conflict?
