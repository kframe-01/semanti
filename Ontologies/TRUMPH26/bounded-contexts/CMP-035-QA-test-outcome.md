---
aliases: [Test Outcome]
tags: [glossary]
bounded_context: "Quality and Assessment"
status: proposed
source: "UST-012"
date_created: "2026-09-29"
last_reviewed: "2026-09-29"
---

# Test Outcome

## Definition

The reported result of the test body, kept distinguishable from setup and teardown failures when an execution completes or is interrupted.

## Usage

When Teardown fails after a test-body failure, the Test Outcome remains visible alongside the cleanup failure.

## Boundaries

- Includes: What happened during the test body and its reported result.
- Does not include: A cleanup result silently replacing the test result or a later human Log Assessment.

## Related terms

- [[CMP-012-SPA-teardown|Teardown]] - Its outcome must be reported separately.
- [[CMP-034-QA-log-assessment|Log Assessment]] - Later human evaluation of the log.

## Sources and open questions

- Source note: [[UST-012-teardowning]]
- Open questions: Which result states are required beyond success, failure, and interruption?
