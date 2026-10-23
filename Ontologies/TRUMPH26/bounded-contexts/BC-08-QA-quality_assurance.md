---
id: "BC-08"
aliases:
  - Quality Assurance
tags:
  - bounded-context
status: proposed
date_created: "2026-10-23"
last_reviewed: "2026-10-23"
sources:
  - "UST-012"
  - "UST-013"
  - "UST-021"
  - "UST-025"
---

# Quality Assurance

## Purpose

Help ensure that authored test sequences are valid and explicitly approved
before integration, and that execution outcomes and logs can be reviewed
against their intended behavior. Provide quality-focused validation,
authorization, synchronization, and assessment without conflating automated
checks, execution-produced outcomes, or human judgment.

## Domain responsibility

### Owns

- Continuous validation of sequence structure, required steps, variant
  parameters and limits, and Test Execution Type-specific step rules.
- Actionable validation feedback identifying affected steps and violated
  rules.
- The joint Sequence Approval workflow requiring explicit Product Owner and
  Testing Engineer sign-off before approved integration.
- Approval decision records, approver identities, timestamps, and the
  sequence's approval state, including re-approval after relevant changes.
- Synchronization-state checks between a Prüfliste and its paired Robot
  Framework sequence description, including conflict visibility and
  reconciliation workflow.
- The meaning and recording of Test Outcomes as distinct results of the test
  body and lifecycle cleanup.
- Human Log Assessments that judge whether an Execution Log is consistent
  with its Test Intent and sufficiently complete for assessment.

### Does not own

- Authoring or persistence of Position Sequences; these belong to Sequence
  and Process Authoring and Artifact and Runtime Data, respectively.
- The semantic definition of Test Intents, Requirements, and Verification
  Criteria; these belong to Intent and Requirements.
- Execution orchestration or production of runtime events and outcomes;
  these belong to Execution Orchestration.
- Execution Evidence storage, retrieval, and traceability record semantics;
  these are handled by Artifact and Runtime Data and Evidence and Traceability.
- LabVIEW project generation itself; approval may trigger the UST-002
  capability, but does not implement it.
- Product-serialization mapping or runtime test-limit selection.
- Reuse Recommendation generation, editing, or approval, which UST-024
  identifies as outside UST-025 and whose decision ownership needs
  clarification.

## Boundary

This context begins when a sequence is authored or modified and requires
validation, when a validated sequence is submitted for approval, or when an
execution log or outcome is presented for quality assessment. It covers
authoring-time checks, joint approval, checklist-description synchronization,
and review of execution outcomes and logs.

It ends when a sequence is approved and eligible for downstream integration,
when validation or synchronization issues are reported for correction, or
when an assessment is recorded or escalated. Project generation and machine
execution remain downstream capabilities. Automated validation and human
assessment are separate processes; neither should silently replace the other's
result.

## Ubiquitous language

- [[CMP-034-QA-log-assessment|Log Assessment]] - Recorded human judgment about
  whether an Execution Log is consistent with a specific Test Intent version
  and contains enough relevant information.
- [[CMP-035-QA-test-outcome|Test Outcome]] - Reported result of the test body,
  distinguished from setup and teardown failures and from later human
  assessment.
- [[CMP-045-QA-continuous-validation|Continuous Validation]] - Repeated
  authoring-time checks of sequence structure, required steps, variant
  parameters and limits, and step-specific execution rules.
- [[CMP-046-QA-sequence-approval|Sequence Approval]] - Recorded joint
  authorization by the Product Owner and Testing Engineer before sequence
  integration.
- [[CMP-047-QA-test-execution-type|Test Execution Type]] - Classification of
  a test run, such as Serial, Validation, or GoldenSample, that may determine
  applicable step rules.
- [[CMP-048-QA-pruefliste|Prüfliste]] - Excel or CSV checklist paired with a
  Robot Framework sequence description and subject to synchronization checks.

## Policies and invariants

- Continuous Validation reports structural, required-step, variant-parameter,
  limit, and Test Execution Type rule issues with actionable context.
- A sequence is not marked Approved until both the Product Owner and Testing
  Engineer have explicitly signed off.
- Each approval decision and timestamp is recorded. A sequence whose
  dependencies change after approval becomes Stale and requires revalidation
  and new approval before machine integration.
- A Test Execution Type is a classification of a run with associated
  step-specific rules; it is not the type of an individual step.
- A Test Outcome remains distinguishable from setup and teardown failures.
  Cleanup failures must not conceal or replace the test body's outcome.
- A Log Assessment is a human judgment associated with the applicable Test
  Intent version, execution, and log; it is not an automatically produced log
  event or a certification of product conformity.
- Missing, incomplete, ambiguous, or unverifiable intent or log information
  prevents a definitive assessment and must be made visible.
- Changes to either a Prüfliste or paired Robot Framework description mark
  their synchronization state out of sync until conflicts are addressed and
  both are reconciled.
- Sequence approval may trigger project generation, but Quality Assurance
  does not own the generation capability.

## Collaborations and context map

| Related context | Relationship | Information exchanged | Notes |
| --- | --- | --- | --- |
| [[BC-01-SPA-sequence_and_process_authoring]] | Upstream provider | Authored sequence, steps, variables, and configuration | Sequence authoring owns sequence content; Quality Assurance validates it and manages approval. |
| [[BC-02-IR-intent_and_requirements]] | Upstream provider | Test Intent semantics, Requirements, parameter/variant descriptions, and expected behavior | Intent and Requirements owns the meaning used by validation and log assessment. |
| [[BC-03-SD-station_and_eployment]] | Collaboration | Deployment readiness and binding compatibility or staleness findings | Quality and release workflows may consume station configuration status without owning binding lifecycle. |
| [[BC-04-EO-execution_orchestration]] | Upstream provider / downstream consumer | Test Execution Type configuration and execution-produced Test Outcomes | Execution Orchestration runs the test; Quality Assurance defines applicable checks and assesses outcomes. |
| [[BC-05-ARD-artifact_and_runtime_data]] | Storage collaboration | Prüflisten, sequence descriptions, approval records, assessments, and related artifacts | Artifact and Runtime Data owns storage and retrieval behavior. |
| [[BC-06-RO-runtime_operations]] | Collaboration | Validation status, approval state, execution result, and operator-visible issues | Runtime Operations presents information and permitted actions; this context owns quality rules and assessment semantics. |
| [[BC-07-ET-evidence_and_traceability]] | Upstream evidence provider / downstream assessment consumer | Execution Logs, evidence, Test Intent version, execution, and traceability links | Evidence and Traceability owns evidence context; Quality Assurance performs Log Assessment. |
| LabVIEW project generation | Downstream consumer | Approved sequence and variant-specific configuration | UST-002 generates or updates the project after approval. |

## Key workflows

1. **Validate an authored sequence:** As steps or configuration change, check
   sequence structure, required steps, variant-specific parameters and limits,
   and Test Execution Type rules. Report actionable findings at the affected
   step. ([[UST-025]])
2. **Approve a sequence:** After validation passes, collect Product Owner
   approval of intent and semantics and Testing Engineer approval of technical
   feasibility. Record decisions and timestamps; mark Approved only after both
   approvals are present. ([[UST-025]])
3. **Revalidate changed dependencies:** When a dependent requirement, parameter
   definition, variant rule, or step type changes after approval, mark the
   sequence Stale and require new validation and approval before integration.
   ([[UST-025]])
4. **Synchronize checklist and sequence description:** Detect edits to either
   the Prüfliste or Robot Framework description, flag out-of-sync state, and
   provide a workflow to merge changes and resolve conflicts. ([[UST-025]])
5. **Report test and lifecycle outcomes distinctly:** Preserve the test-body
   outcome alongside setup and teardown failures and report cleanup failure
   separately. ([[UST-012]])
6. **Assess an Execution Log:** Compare the log with the Test Intent version
   used for its execution, record whether it appears consistent, incomplete,
   or inconsistent, and escalate unresolved or unverifiable discrepancies.
   ([[UST-013]])
7. **Trigger downstream integration:** Once joint approval is complete,
   provide the approved sequence and configuration to the LabVIEW project
   generation capability. ([[UST-025]], [[UST-002]])

## Information and lifecycle

| Information or artifact | Authority | Lifecycle or state changes | Consumers |
| --- | --- | --- | --- |
| Validation findings and status | Quality Assurance | Authoring change → validation result and actionable findings → corrected and revalidated | Sequence authoring and review |
| Sequence Approval | Quality Assurance records the workflow; Product Owner and Testing Engineer provide decisions | Ready for approval → one or both approvals pending → Approved or returned for changes; dependency changes make it Stale | Project generation, Runtime Operations, audit and traceability |
| Test Execution Type rules | Quality Assurance defines or governs validation rules; exact governance remains open | Type and rules defined → applied during sequence validation → revised rules may require revalidation | Sequence authoring and execution preparation |
| Prüfliste synchronization state | Quality Assurance owns synchronization assessment; source formats remain separately authored | In sync → edit detected/out of sync → conflicts merged and synchronized | Sequence authors, reviewers, project generation |
| Test Outcome | Execution runtime produces the result; Quality Assurance defines its distinction from lifecycle outcomes | Test body runs → outcome reported alongside setup/teardown results → retained with execution | Runtime Operations, Evidence and Traceability, quality review |
| Log Assessment | Quality Assurance records the human assessment | Log and intent version reviewed → consistent, incomplete, inconsistent, or otherwise defined assessment → escalated or closed | Maintenance, Verification, Quality Assurance |

## Sources and traceability

- User stories: [[UST-012-teardowning]],
  [[UST-013-worker-is-a-complice]],
  [[UST-021-managing-golden-samples-across-test-types]],
  [[UST-025-continuous-validation-and-approval-workflow]]
- Glossary entries: [[CMP-034-QA-log-assessment]],
  [[CMP-035-QA-test-outcome]],
  [[CMP-045-QA-continuous-validation]],
  [[CMP-046-QA-sequence-approval]],
  [[CMP-047-QA-test-execution-type]],
  [[CMP-048-QA-pruefliste]]
- Related contexts: [[BC-01-SPA-sequence_and_process_authoring]],
  [[BC-02-IR-intent_and_requirements]],
[[BC-03-SD-station_and_eployment]],
[[BC-04-EO-execution_orchestration]],
  [[BC-05-ARD-artifact_and_runtime_data]],
  [[BC-06-RO-runtime_operations]],
  [[BC-07-ET-evidence_and_traceability]]
- Related source notes: [[UST-002-dsl-to-poject]],
  [[UST-024-product-variant-management-and-reuse-optimization]]

## Open questions

- [ ] What is the complete set of Test Execution Types and the step-specific
  rules for each type?
- [ ] Which validation checks run on every authoring change and which run
  before approval?
- [ ] How are Product Owner and Testing Engineer approvers assigned, and
  what escalation applies when either is unavailable?
- [ ] How are approval decisions retained, revoked, or audited?
- [ ] Is the Prüfliste or Robot Framework description authoritative when
  changes conflict, and is synchronization one-way or two-way?
- [ ] Which states and categories are required for Test Outcomes, especially
  beyond success, failure, and interruption?
- [ ] May a Maintenance Technician approve a Log Assessment or only assess
  and escalate it?
- [ ] Which information is required before a Log Assessment can be definitive,
  and when must the result be marked incomplete or unverifiable?
- [ ] Which context owns approval or rejection of Reuse Recommendations, given
  UST-024 and UST-025 describe that responsibility differently?
- [ ] How do GoldenSample procedures and reference-sample lifecycle relate to
  Test Execution Types and this context's validation rules?
