---
aliases: [Sequence Approval]
tags: [glossary]
bounded_context: "Quality Assurance"
status: proposed
source: "UST-025"
date_created: "2026-10-22"
last_reviewed: "2026-10-22"
---

# Sequence Approval

## Definition

A recorded authorization for a validated sequence that requires explicit
sign-off from both the Product Owner and Testing Engineer before the sequence
is considered approved for project integration.

## Usage

After Continuous Validation passes, the sequence remains pending until both
required approvers have recorded their decisions.

## Boundaries

- Includes: Approver decisions, timestamps, and the transition to an approved state.
- Does not include: Reuse-recommendation decisions or LabVIEW project generation.

## Related terms

- [[CMP-045-QA-continuous-validation|Continuous Validation]] - Establishes validity before approval.
- [[CMP-044-IR-reuse-recommendation|Reuse Recommendation]] - A separate proposal reviewed in the workflow.

## Sources and open questions

- Source note: [[UST-025-continuous-validation-and-approval-workflow]]
- Open questions: How are approvers assigned, decisions retained, and unavailable approvers handled?
