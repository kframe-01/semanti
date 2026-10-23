---
id: "BC-01"
aliases:
  - Sequence and Process Authoring
tags:
  - bounded-context
status: proposed
date_created: "2026-10-22"
last_reviewed: "2026-10-22"
sources:
  - "UST-001"
  - "UST-002"
  - "UST-004"
  - "UST-006"
  - "UST-011"
  - "UST-012"
  - "UST-023"
---

# Sequence and Process Authoring

## Purpose

Provide the domain concepts and authoring capabilities for defining
position-specific test flows and reusable process behavior. This context enables
Testing Engineers and domain users to describe, compose, and validate sequence
steps and lifecycle behavior while keeping position-specific decisions distinct
from reusable behavior.

## Domain responsibility

### Owns

- The domain model and authoring of Position Sequences, including their
  position-specific flow, ordering, and decisions.
- Reusable Process Models and the Entry Points through which sequences invoke
  them.
- Step Type classification and sequence-level Test Type selection.
- Setup and Teardown behavior associated with test lifecycles.
- Variable declarations and scopes used while authoring sequences.
- Position and Workplane concepts as currently represented in the glossary;
  ownership of these concepts remains to be confirmed.

### Does not own

- The meaning and approval of upstream Test Intents or formal Requirements.
- Sequence persistence and retrieval, identified as the responsibility of
  UST-003.
- LabVIEW project generation, which is handled by UST-002.
- Concrete station hardware, deployment bindings, or runtime execution.
- Continuous validation and joint approval workflows owned by UST-025.

## Boundary

This context begins when a Test Intent or position-related information is used
to author or refine a Position Sequence. It covers sequence and reusable
process definitions, their step and variable configuration, and lifecycle
behavior. It ends when an authored sequence is ready for storage, validation
and approval, project generation, deployment, or execution by collaborating
capabilities.

The sequence expresses position-specific intent and ordering. Reusable behavior
is defined separately in a Process Model and invoked through an Entry Point.
Concrete station-specific hardware selection and runtime behavior are outside
this context.

## Ubiquitous language

- [[CMP-001-SPA-position|Position]] - Manufacturing position for which a
  sequence is authored; its distinction from a physical station remains open.
- [[CMP-002-SPA-workplane|Workplane]] - ERP-downloaded information identifying
  manufacturing positions and providing position data.
- [[CMP-006-SPA-position-sequence|Position Sequence]] - Authored
  position-specific test behavior, ordering, decisions, and abstract hardware
  needs.
- [[CMP-007-SPA-process-model|Process Model]] - Reusable process behavior
  maintained separately from a Position Sequence.
- [[CMP-008-SPA-entry-point|Entry Point]] - Named, contract-based way for a
  sequence to invoke a Process Model.
- [[CMP-009-SPA-step-type|Step Type]] - Classification of an individual step,
  such as Assignment, gRPCCall, Looping, Branching, or a custom type.
- [[CMP-010-SPA-test-type|Test Type]] - Functional mode applied to a sequence
  that governs which operations are permitted during a test.
- [[CMP-011-SPA-setup|Setup]] - Reusable preparation behavior before a test
  body.
- [[CMP-012-SPA-teardown|Teardown]] - Reusable cleanup behavior attempted
  after a test body when applicable and safe.
- [[CMP-041-SPA-variable-scope|Variable Scope]] - Level at which a variable is
  available and initialized: Local, Sequence Global, or Station Global.

## Policies and invariants

- A Position Sequence retains position-specific flow, ordering, and decisions;
  reusable process internals belong to the Process Model.
- A sequence invokes a Process Model through a named Entry Point with an
  explicit contract for inputs, preconditions, outputs, and failures.
- Step Type describes an individual step; Test Type describes functional rules
  applied to the sequence. They are distinct concepts.
- Setup precedes the test body. Teardown follows it when applicable and safe;
  setup, test, and teardown outcomes must remain distinguishable.
- Variable declarations identify their scope. Initialization and availability
  follow that scope's rules.
- Abstract equipment needs in a sequence do not identify concrete,
  station-specific hardware bindings.

## Collaborations and context map

| Related context                         | Relationship               | Information exchanged                                                    | Notes                                                                                                |
| --------------------------------------- | -------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| [[BC-02-IR-intent_and_requirements]]    | Upstream provider          | Accepted Test Intent, Requirements, and variable or step metadata        | Authoring refines intent without silently changing its meaning.                                      |
| [[BC-03-SD-station_and_eployment]]      | Downstream collaboration   | Abstract equipment needs and position-related information                | Concrete station hardware and deployment bindings are outside this context.                          |
| [[BC-04-EO-execution_orchestration]]    | Downstream consumer        | An authored sequence and reusable process behavior for execution         | Runtime orchestration and hardware execution are outside this context.                               |
| [[BC-05-ARD-artifact_and_runtime_data]] | Persistence collaboration  | Authored sequence and related artifacts                                  | UST-003 is identified as owning sequence persistence and retrieval.                                  |
| [[BC-06-RO-runtime_operations]]         | Upstream provider          | Position identity, authored instructions, and step/process context       | Runtime Operations presents authored information; it does not edit sequences or process definitions. |
| [[BC-07-ET-evidence_and_traceability]]  | Traceability collaboration | Position and sequence identity or revision used for an execution         | Evidence and Traceability associates execution output with the sequence revision.                    |
| [[BC-08-QA-quality_assurance]]          | Downstream collaboration   | Sequence structure, step configuration, and variant-specific information | Quality Assurance validates sequence changes and manages approval.                                   |

## Key workflows

1. **Author a Position Sequence:** A Testing Engineer or domain user creates or
   modifies a sequence, selects Step Types, configures steps and variables,
   and validates the authored structure. ([[UST-023]])
2. **Compose reusable behavior:** A sequence identifies common behavior and
   invokes a Process Model through an Entry Point with the required inputs.
   ([[UST-006]], [[UST-011]])
3. **Apply test lifecycle behavior:** A test declares reusable Setup and
   Teardown, which run around the test body according to applicable lifecycle
   and safety rules. ([[UST-012]])
4. **Prepare position project input:** Position and Workplane data are used
   with an accepted Test Intent as input to the downstream project-generation
   capability. ([[UST-002]])

## Information and lifecycle

| Information or artifact | Authority | Lifecycle or state changes | Consumers |
| --- | --- | --- | --- |
| Position Sequence | Sequence and Process Authoring defines its authored meaning; persistence is owned by UST-003 | Authored or modified → validated and ready for downstream processing | Quality Assurance, project generation, execution capabilities |
| Process Model and Entry Point contract | Sequence and Process Authoring | Defined and maintained → referenced by consuming sequences | Position Sequences and execution capabilities |
| Step and variable declarations | Sequence and Process Authoring | Declared or modified → checked during authoring and downstream validation | Project generation and execution capabilities |
| Position and Workplane data | Current glossary placement is Sequence and Process Authoring; ownership is unresolved | ERP-downloaded Workplane identifies Positions used in project generation | Project generation and related authoring capabilities |
| Setup and Teardown definitions | Sequence and Process Authoring | Defined and associated with test lifecycle points | Sequence execution capabilities |

## Sources and traceability

- User stories: [[UST-001-natural-and-formal-description]],
  [[UST-002-dsl-to-poject]], [[UST-004-hal-in-the-actors]],
  [[UST-006-process-model-entry-points]],
  [[UST-011-step-types-abstraction]], [[UST-012-teardowning]],
  [[UST-023-accessible-sequence-authoring-with-typed-steps]]
- Glossary entries: [[CMP-001-SPA-position]], [[CMP-002-SPA-workplane]],
  [[CMP-006-SPA-position-sequence]], [[CMP-007-SPA-process-model]],
  [[CMP-008-SPA-entry-point]], [[CMP-009-SPA-step-type]],
  [[CMP-010-SPA-test-type]], [[CMP-011-SPA-setup]], [[CMP-012-SPA-teardown]],
  [[CMP-041-SPA-variable-scope]]
- Other source notes: [[UST-025-continuous-validation-and-approval-workflow]]
- Related contexts: [[BC-02-IR-intent_and_requirements]],
  [[BC-03-SD-station_and_eployment]],
  [[BC-04-EO-execution_orchestration]],
  [[BC-05-ARD-artifact_and_runtime_data]],
  [[BC-06-RO-runtime_operations]],
  [[BC-07-ET-evidence_and_traceability]],
  [[BC-08-QA-quality_assurance]]

## Open questions

- [ ] Is Position owned by this context, Station and Deployment, or another
  context, and how does it relate to a physical station?
- [ ] Which ERP system and Workplane format are supported, and which context
  owns the Workplane data?
- [ ] Which sequence constructs and authoring technologies must be supported?
- [ ] Which responsibilities belong in a Process Model rather than directly
  in a Position Sequence?
- [ ] How are Process Models and Entry Points discovered, versioned, approved,
  and kept compatible with consuming sequences?
- [ ] What execution rules are defined for each built-in and customized Test
  Type?
- [ ] Which Setup and Teardown scopes and interruption paths are required?
- [ ] How are Station Global variables initialized, persisted, and resolved
  across stations or sequences?
