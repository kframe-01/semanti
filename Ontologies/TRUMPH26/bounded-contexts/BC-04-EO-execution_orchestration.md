---
id: "BC-04"
aliases:
  - Execution Orchestration
tags:
  - bounded-context
status: proposed
date_created: "2026-10-23"
last_reviewed: "2026-10-23"
sources:
  - "UST-004"
  - "UST-008"
  - "UST-009"
  - "DEC-001"
  - "DEC-002"
---

# Execution Orchestration

## Purpose

Coordinate a Position Execution and its interactions with abstract equipment
operations, so a sequence can run against compatible station equipment without
depending on concrete device details. Preserve execution identity, state,
configured mode, and outcomes so each run can be distinguished and understood.

## Domain responsibility

### Owns

- The runtime identity and state of an individual Position Execution.
- Association of an Execution Mode and Execution Color with a particular run.
- Interpretation and dispatch of abstract equipment operation requests through
  the Hardware Abstraction Layer.
- Runtime validation that each required equipment request has an approved,
  compatible Deployment Binding before hardware operations begin.
- Correlation of equipment requests with their terminal outcomes, including
  success, equipment failure, timeout, and cancellation.
- Actor-based component interaction and the runtime contracts needed to keep
  concrete equipment implementation details out of sequence callers.

### Does not own

- Position Sequence or Process Model authoring; these belong to Sequence and
  Process Authoring.
- Station Description, component catalog, compatibility evaluation, or
  Deployment Binding approval and lifecycle; these belong to Station and
  Deployment.
- Runtime view presentation and operator control workflows; these belong to
  Runtime Operations.
- The internal behavior or recovery implementation of a concrete equipment
  component.
- Resource reservation, exclusivity, scheduling, or parallel-execution
  compatibility.
- The full behavior of station simulation or evidence lifecycle.

## Boundary

This context begins when an execution is configured and started from a
Position Sequence and target or execution environment. It establishes an
identifiable run, tracks its state and mode, and coordinates runtime requests
for abstract equipment operations using approved bindings.

It ends with correlated operation outcomes and the execution's current or
final state available to monitoring and evidence consumers. It does not author
the sequence, select or approve station bindings, determine current resource
availability, or own the user interface for monitoring and controlling a live
execution.

## Ubiquitous language

- [[CMP-019-EO-position-execution|Position Execution]] - Identifiable run of a
  manufacturing position with its own state, configured mode, target, and
  results.
- [[CMP-020-EO-execution-mode|Execution Mode]] - Per-execution configuration
  that distinguishes how the run operates.
- [[CMP-021-EO-white-op|White-op]] - Proposed dry-run Execution Mode for
  runtime testing or debugging; its hardware-actuation semantics remain open.
- [[CMP-022-EO-hardware-abstraction-layer|Hardware Abstraction Layer]] -
  Interpreter-based boundary that routes abstract equipment requests to
  compatible concrete implementations.
- [[CMP-023-EO-actor|Actor]] - Independent component that encapsulates state
  and behavior and communicates by exchanging messages.
- [[CMP-037-EO-execution-color|Execution Color]] - Supplementary per-execution
  visual classification shown with a textual label.

## Policies and invariants

- Each Position Execution has an identity and state independent of other runs
  of the same Position.
- Execution Mode and Execution Color are distinct attributes unless domain
  decisions establish otherwise. Both remain associated with the execution
  they describe.
- Color is supplementary; execution meaning must not be conveyed by color
  alone.
- White-op is a proposed dry-run mode, not an established synonym for
  Simulated Station or a guarantee that physical operations are suppressed.
  Its behavior must be defined before relying on that interpretation.
- Sequences and process-model entry points invoke the same abstract equipment
  contracts and outcome semantics.
- Before hardware operations begin, each required abstract equipment reference
  must have an approved current Deployment Binding that supports the required
  contract.
- Each accepted operation request has one correlated terminal outcome.
  Automatic retries are not performed by the Hardware Abstraction Layer;
  retry decisions belong to the caller and must respect operation safety
  metadata.
- Concrete actor state and driver details are not exposed to sequence callers.
- A simulated or white-op execution must remain distinguishable from normal
  physical operation in runtime and result views.

## Collaborations and context map

| Related context | Relationship | Information exchanged | Notes |
| --- | --- | --- | --- |
| [[BC-01-SPA-sequence_and_process_authoring]] | Upstream provider | Position Sequence, abstract equipment requirements, and process-model invocations | Sequences remain independent of concrete device identities. |
| [[BC-03-SD-station_and_eployment]] | Upstream provider | Approved Deployment Bindings and compatibility evidence | Station and Deployment owns binding selection, approval, and lifecycle. |
| [[BC-05-ARD-artifact_and_runtime_data]] | Upstream consumer / persistence provider | Execution identity, data, logs, measurements, and evidence for storage and retrieval | Artifact and Runtime Data owns storage behavior, not execution outcome production. |
| [[BC-06-RO-runtime_operations]] | Downstream consumer | Execution identity, state, progress, mode, target, outcomes, and available actions | UST-008 covers the Maintenance Technician's runtime view and control workflow. |
| [[BC-07-ET-evidence_and_traceability]] | Downstream consumer | Execution identity, configured mode, target, outcomes, and final state | Execution results must remain distinguishable by run and execution mode. |
| [[BC-08-QA-quality_assurance]] | Collaboration | Test Execution Type rules and execution-produced Test Outcomes | Quality Assurance defines applicable checks and assesses outcomes; execution produces runtime results. |
| Simulation and Test Development | Collaboration | Simulated execution target and simulated operation outcomes | UST-007 covers simulator behavior; White-op is related but not necessarily equivalent. |

## Key workflows

1. **Start a Position Execution:** Select a sequence and target, configure
   execution attributes, establish a distinct run identity, and initialize
   its runtime state. ([[UST-008]], [[UST-009]])
2. **Validate equipment bindings:** Before issuing hardware requests, verify
   that each required abstract equipment reference has an approved current
   binding supporting the required contract. Block execution and report
   missing or incompatible bindings. ([[UST-004]], [[UST-005]], [[DEC-002]])
3. **Orchestrate an equipment operation:** Receive an abstract operation
   request, route it through the Hardware Abstraction Layer to the component
   actor identified by the binding, and return one correlated terminal
   outcome. ([[UST-004]], [[DEC-001]], [[DEC-002]])
4. **Track execution state and completion:** Maintain the run's current and
   final states and make associated outcomes available to runtime monitoring
   and evidence consumers. ([[UST-008]])
5. **Run in a non-standard mode:** Record and expose White-op or other
   configured execution modes without presenting them as normal physical
   operation; exact White-op actuation behavior requires a decision.
   ([[UST-009]])

## Information and lifecycle

| Information or artifact | Authority | Lifecycle or state changes | Consumers |
| --- | --- | --- | --- |
| Position Execution identity and state | Execution Orchestration | Configured → started/active → completed, failed, cancelled, or other defined terminal state | Runtime Operations and Evidence and Traceability |
| Execution Mode | Execution Orchestration records the per-run configuration | Selected before start → associated with run and exposed during and after execution | Runtime Operations and evidence consumers |
| Execution Color | Execution Orchestration records the per-run classification | Assigned/configured → shown with text in runtime and history views | Runtime Operations and history views |
| Abstract operation request and outcome | Execution Orchestration coordinates the request; concrete actor performs the operation | Requested → accepted/in flight → one correlated terminal outcome | Calling sequence or process model; execution history |
| Deployment Binding reference | Station and Deployment owns the binding; Execution Orchestration validates and consumes it | Approved/current at startup → consumed for operation routing; stale or invalid bindings block execution | Hardware Abstraction Layer and execution |
| Simulated or White-op execution designation | Execution Orchestration records configured mode/target; simulator behavior is owned elsewhere | Configured → visible during execution → retained with results | Runtime Operations and Evidence and Traceability |

## Sources and traceability

- User stories: [[UST-004-hal-in-the-actors]],
  [[UST-005-semantic-station-globals]],
  [[UST-007-easy-testing]],
  [[UST-008-how-it-looks-like-in-runtime]],
  [[UST-009-executions-have-colours]]
- Decision records: [[DEC-001-the-actor-framework]],
  [[DEC-002-the-abstraction-of-hardware]]
- Glossary entries: [[CMP-019-EO-position-execution]],
  [[CMP-020-EO-execution-mode]], [[CMP-021-EO-white-op]],
  [[CMP-022-EO-hardware-abstraction-layer]], [[CMP-023-EO-actor]],
  [[CMP-037-EO-execution-color]]
- Related contexts: [[BC-01-SPA-sequence_and_process_authoring]],
  [[BC-03-SD-station_and_eployment]],
  [[BC-05-ARD-artifact_and_runtime_data]],
  [[BC-06-RO-runtime_operations]],
  [[BC-07-ET-evidence_and_traceability]],
  [[BC-08-QA-quality_assurance]]

## Open questions

- [ ] What uniquely identifies a Position Execution, and which state
  transitions are valid?
- [ ] Which Execution Modes exist, and can a mode change after execution
  starts?
- [ ] What does White-op mean operationally: no actuation, simulated
  responses, limited safe operations, or another behavior?
- [ ] How does White-op differ from execution against a Simulated Station?
- [ ] Which colors and textual labels are allowed, what do they mean, and who
  assigns them?
- [ ] Which operation contract fields and metadata define compatibility and
  safe retry behavior?
- [ ] What message delivery, timeout, cancellation, late-response, and
  duplicate-response semantics must Actors support?
- [ ] How are execution state and terminal operation outcomes persisted and
  associated with traceability records?
- [ ] Which control actions can affect a running execution, and which
  operational or safety checks are required before they are accepted?
- [ ] How are resource availability, reservation, scheduling, and parallel
  execution coordinated with this context?
