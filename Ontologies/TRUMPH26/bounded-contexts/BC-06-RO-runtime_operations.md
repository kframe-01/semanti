---
id: "BC-06"
aliases:
  - Runtime Operations
tags:
  - bounded-context
status: proposed
date_created: "2026-10-23"
last_reviewed: "2026-10-23"
sources:
  - "UST-008"
  - "UST-010"
---

# Runtime Operations

## Purpose

Provide role-appropriate interfaces for people interacting with an active
position: a Runtime View for monitoring and authorized intervention, and an
Operator Interface for guided shop-floor work. Help users understand the
selected execution, its current state, the next relevant action, and any
warnings or outcomes without exposing unnecessary complexity or implying an
unconfirmed state change.

## Domain responsibility

### Owns

- Presentation of live and final Position Execution information in a
  Runtime View.
- Presentation of task-focused position instructions, inputs, state, and
  permitted actions through an Operator Interface.
- Role- and permission-appropriate visibility of information and available
  actions.
- Presentation of available Control Actions and their accepted, rejected, or
  unconfirmed outcomes.
- Clear communication of stale, disconnected, incomplete, or unavailable
  runtime information.
- Clear distinction between active and completed executions, and between
  physical and simulated or otherwise non-physical runs.

### Does not own

- Position Execution identity, lifecycle state transitions, or equipment
  operation dispatch; these belong to Execution Orchestration.
- Sequence, process, or instruction authoring.
- Station Description, equipment selection, or Deployment Binding approval.
- Operational safety rules themselves; interfaces must respect the
  applicable rules and only offer permitted actions.
- Definition of the complete set of Control Actions or their underlying
  execution semantics, which remain to be agreed with runtime stakeholders.

## Boundary

This context begins when a user opens a position or a specific Position
Execution in a Runtime View or Operator Interface. It presents the runtime
state, progress, instructions, messages, and actions appropriate to that
user's role and task. It accepts user inputs or Control Action requests and
communicates their confirmed outcomes.

It ends at the interaction boundary with the execution runtime: this context
does not itself change execution state or actuate equipment. Requests are
forwarded to the execution capability, and the interface reports the resulting
state only when confirmed. Stale or unavailable data must be shown as such.

## Ubiquitous language

- [[CMP-024-RO-runtime-view|Runtime View]] - Live view for inspecting a
  selected Position Execution, including its identity, mode, target, state,
  progress, and available Control Actions.
- [[CMP-025-RO-control-action|Control Action]] - Authorized, state-dependent
  request to influence a running Position Execution, with an explicit
  accepted or rejected outcome.
- [[CMP-026-RO-operator-interface|Operator Interface]] - Shop-floor worker's
  task-focused interface to position instructions, current state, permitted
  actions, and supporting information.

## Policies and invariants

- Runtime information is associated with the selected Position Execution and
  must not be confused with another run, historical state, or simulated
  execution.
- When updates are stale or unavailable, the interface makes that condition
  explicit and does not present stale information as current.
- A Control Action is shown as executable only when it is available for the
  current state and the user is authorized to request it.
- A request is not presented as successful, nor as having changed execution
  state, until its outcome is confirmed.
- Any action affecting a live position or equipment follows applicable
  operational and safety procedures.
- The Operator Interface prioritizes the instructions and inputs needed for
  the operator's current task while making authorized supporting information
  accessible without obscuring the primary workflow.
- Role-appropriate interfaces do not expose technical controls or information
  without a task-related need and the user's authorization.
- Color is not the sole means of communicating execution state, warnings, or
  required action.
- Errors, warnings, and interruptions explain their impact and present the
  next permitted action or a clear escalation path where known.

## Collaborations and context map

| Related context | Relationship | Information exchanged | Notes |
| --- | --- | --- | --- |
| [[BC-04-EO-execution_orchestration]] | Upstream provider | Execution identity, state, progress, mode, target, messages, and action outcomes | Execution Orchestration owns execution state and hardware-operation coordination; this context presents that information and forwards user requests. |
| [[BC-01-SPA-sequence_and_process_authoring]] | Upstream provider | Position identity, authored instructions, and step/process context | Runtime Operations presents authored information; it does not edit sequences or process definitions. |
| [[BC-03-SD-station_and_eployment]] | Context provider | Target station identity and physical or simulated classification | Used to make execution target understandable; station configuration and binding lifecycle remain external. |
| [[BC-05-ARD-artifact_and_runtime_data]] | Upstream provider | Retrieved position, execution, and supporting data | Artifact and Runtime Data owns storage semantics. |
| [[BC-07-ET-evidence_and_traceability]] | Downstream consumer | Final execution state, user interaction context, and links to available results | Evidence retention and traceability records are owned outside this context. |
| [[BC-08-QA-quality_assurance]] | Collaboration | Validation status, approval state, test outcome, and operator-visible quality issues | Quality Assurance owns validation and assessment; Runtime Operations presents relevant information. |

## Key workflows

1. **Monitor a Position Execution:** A Maintenance Technician selects a run
   and inspects its identity, target, mode, current state, progress, and
   relevant messages. The view distinguishes active and completed state.
   ([[UST-008]])
2. **Request a Control Action:** The interface shows actions available to the
   user's role and the execution's current state. The user submits a request,
   and the interface reports acceptance, rejection, or an unconfirmed outcome
   alongside any confirmed resulting state. ([[UST-008]])
3. **Guide a shop-floor task:** A Worker on the Machine opens the assigned
   position, follows contextual instructions, supplies requested input or
   confirmation, and receives clear guidance when attention or escalation is
   needed. ([[UST-010]])
4. **Access supporting information:** An authorized user reaches additional
   task-relevant or diagnostic information without losing the current runtime
   or operator workflow context. ([[UST-008]], [[UST-010]])
5. **Handle loss of runtime updates:** When disconnected or receiving stale
   information, the interface identifies the limitation and does not report a
   requested action as successful without confirmation. ([[UST-008]],
   [[UST-010]])

## Information and lifecycle

| Information or artifact | Authority | Lifecycle or state changes | Consumers |
| --- | --- | --- | --- |
| Runtime View state and progress presentation | Runtime Operations presents data supplied by Execution Orchestration | Connected/current → updated as execution changes → final state; may become stale or unavailable | Maintenance Technician and other authorized runtime viewers |
| Operator instructions and task prompts | Position or sequence source owns the instruction meaning; Runtime Operations presents them | Available for assigned task → displayed at the applicable step → completed or superseded | Worker on the Machine / Shop-Floor Operator |
| Control Action request and user feedback | Runtime Operations owns presentation and request interaction; Execution Orchestration owns execution result | Available → requested → accepted, rejected, or unconfirmed; confirmed state is displayed when received | Requesting user and execution history |
| Role- and permission-filtered information/actions | Authorization policy owner is to be determined; Runtime Operations enforces presentation | Evaluated for user, task, and current execution state → shown or withheld | Maintenance Technician, Testing Engineer, shop-floor operator |
| Runtime warning, error, or interruption presentation | Execution Orchestration supplies runtime event; Runtime Operations contextualizes it for the user's task | Received → associated with run and presented → resolved, escalated, or retained for review | Operator, Maintenance Technician, and evidence/quality consumers |

## Sources and traceability

- User stories: [[UST-008-how-it-looks-like-in-runtime]],
  [[UST-010-simple-user-experience]]
- Glossary entries: [[CMP-024-RO-runtime-view]],
  [[CMP-025-RO-control-action]], [[CMP-026-RO-operator-interface]]
- Related contexts: [[BC-01-SPA-sequence_and_process_authoring]],
  [[BC-03-SD-station_and_eployment]],
  [[BC-04-EO-execution_orchestration]],
  [[BC-05-ARD-artifact_and_runtime_data]],
  [[BC-07-ET-evidence_and_traceability]],
  [[BC-08-QA-quality_assurance]]
- Related source notes: [[UST-009-executions-have-colours]]

## Open questions

- [ ] Which execution state, progress, measurements, device state, messages,
  and elapsed-time information must be visible in the Runtime View?
- [ ] Which Control Actions are supported, what state transitions do they
  request, and which require confirmation or safe-state checks?
- [ ] Which roles may view, control, or access supporting information, and
  can permissions vary by station or execution mode?
- [ ] What runtime update frequency and response times are required?
- [ ] How should concurrent viewers and simultaneous Control Action requests
  be handled?
- [ ] Which instructions, inputs, and controls are essential to each
  shop-floor task, and what does “open as necessary” mean?
- [ ] Which shop-floor language, accessibility, environmental, and usability
  needs must the Operator Interface support?
- [ ] What should the interface display when an action times out and its
  outcome cannot be confirmed?
- [ ] Which runtime interactions or outcomes must be retained as execution
  evidence?
- [ ] How should physical, simulated, and White-op executions be distinguished
  consistently across Runtime View and Operator Interface?
