---
id: "BC-03"
aliases:
  - Station and Deployment
tags:
  - bounded-context
status: proposed
date_created: "2026-10-23"
last_reviewed: "2026-10-23"
sources:
  - "UST-004"
  - "UST-005"
  - "UST-007"
  - "DEC-002"
---

# Station and Deployment

## Purpose

Describe target stations and their equipment, determine whether their
components can satisfy abstract equipment requirements, and govern approved
bindings from sequence requirements to concrete station operations. This
context allows reusable sequences to remain independent of specific hardware
while making deployment choices compatible, traceable, and reviewable.

## Domain responsibility

### Owns

- Station identity, revisions, and Station Descriptions.
- The description of installed Hardware Components and whether each is
  physical or simulated.
- The governed component-type catalog information used to evaluate functional
  compatibility.
- Evaluation of Abstract Equipment Capabilities against station components.
- Candidate selection records and the Deployment Binding lifecycle, including
  validation, approval, staleness, revalidation, revocation, and traceability.
- The explicit identification of simulated components and their bindings.

### Does not own

- Definition of abstract equipment contracts or runtime invocation of concrete
  equipment operations; these belong to Execution Orchestration.
- Position Sequence authoring or the definition of its abstract equipment
  needs; these belong to Sequence and Process Authoring.
- Resource availability, reservation, scheduling, exclusivity, or
  parallel-execution compatibility.
- Simulation fidelity, simulated response behavior, or labeling execution
  evidence as simulated; these are addressed by the simulation and evidence
  capabilities.
- Complete release-coherence validation across executable and configuration
  artifacts; this is handled by the release-validation capability.

## Boundary

This context begins when a station and its installed components are described
or when a Position Sequence's Abstract Equipment Capability must be realized
on a target station. It covers compatibility evaluation and the governed
creation and lifecycle of Deployment Bindings.

It ends by providing an approved, current binding and its validation evidence
to execution consumers. It does not invoke hardware operations or determine
whether equipment is currently available at runtime. A simulated component may
be described and bound through the same functional compatibility and approval
lifecycle as a physical component, while remaining explicitly identified as
simulated.

## Ubiquitous language

- [[CMP-013-SD-station|Station]] - Target for deploying and executing a
  Position Sequence, with connected equipment components.
- [[CMP-014-SD-station-description|Station Description]] - Versioned account of
  station identity, installed components, capabilities, and supported
  operations.
- [[CMP-015-SD-hardware-component|Hardware Component]] - Concrete
  station-specific equipment described by its component type and supported
  operations.
- [[CMP-016-SD-abstract-equipment-capability|Abstract Equipment Capability]]
  - Technology-independent equipment ability required by a sequence.
- [[CMP-017-SD-deployment-binding|Deployment Binding]] - Validated and
  approved mapping from an abstract requirement to a compatible operation and
  component on a selected station.
- [[CMP-018-SD-simulated-station|Simulated Station]] - Software
  representation of a target station and relevant equipment that provides
  defined simulated responses without physical hardware.

## Policies and invariants

- A Position Sequence names abstract equipment requirements, not concrete
  station-specific components or implementation details.
- A Station Description identifies installed components and revisions; the
  governed component-type catalog defines their supported contracts,
  operations, parameter types, units, ranges, and modes.
- Compatibility is functional: every required contract and operation
  attribute must be supported before a binding can be validated.
- A Testing Engineer may propose and select a compatible component. An
  authorized Deployer approves or revokes the binding.
- A binding records the sequence revision, abstract requirement and contract
  version, station and description revision, selected component and catalog
  revision, validation result, creator, approver, timestamps, and lifecycle
  state.
- A binding is usable as an approved current binding only while it is Approved.
  Changes to compatibility-relevant inputs make an Approved binding Stale;
  a Stale binding must be revalidated and approved again.
- A Revoked binding cannot return to use without a new binding proposal.
- Physical and simulated components follow the same functional compatibility
  rules and binding lifecycle, and simulated status must remain explicit.
- Functional compatibility does not assert current equipment availability,
  resource exclusivity, scheduling feasibility, or concurrency safety.

## Collaborations and context map

| Related context | Relationship | Information exchanged | Notes |
| --- | --- | --- | --- |
| [[BC-01-SPA-sequence_and_process_authoring]] | Upstream provider | Position Sequence revision and Abstract Equipment Capabilities | Sequence authoring remains independent of concrete station selection. |
| [[BC-04-EO-execution_orchestration]] | Downstream consumer | Approved current Deployment Binding and validation evidence | Execution checks and consumes bindings; this context does not invoke equipment. |
| [[BC-05-ARD-artifact_and_runtime_data]] | Persistence collaboration | Station Descriptions, component catalog definitions, bindings, approvals, and audit history | Persistence and retrieval are provided by the Data Manager. |
| [[BC-06-RO-runtime_operations]] | Context provider | Target station identity and physical or simulated classification | Runtime Operations identifies the execution target to users. |
| [[BC-07-ET-evidence_and_traceability]] | Traceability collaboration | Station, Station Description, component, and Deployment Binding revisions | Evidence and Traceability can associate the deployed configuration with execution outputs. |
| [[BC-08-QA-quality_assurance]] | Downstream collaboration | Approved binding state and compatibility or staleness findings | Quality and release workflows may consume deployment-readiness information. |
| Simulation and Test Development | Collaboration | Simulated station/component identity and supported capabilities | UST-007 addresses simulation behavior and simulated-result distinction. |
| Release Validation | Downstream collaboration | Station and binding revisions relevant to a test release | UST-016 defines broader executable and configuration coherence checks. |

## Key workflows

1. **Describe a station:** Create or revise a Station Description with a
   unique station identity and revision, recording installed Hardware
   Components and their physical or simulated classification. Resolve each
   component type through the governed catalog. ([[UST-005]])
2. **Find compatible equipment:** Compare a sequence's Abstract Equipment
   Capability with component catalog definitions and return only candidates
   satisfying the required contract versions, operations, parameter types,
   units, ranges, and modes. Report unsatisfied attributes when no candidate
   qualifies. ([[UST-005]], [[DEC-002]])
3. **Propose and validate a binding:** The Testing Engineer selects a
   compatible component, creating a Draft Deployment Binding tied to the
   relevant sequence, station, description, and catalog revisions. Validate
   compatibility before the binding becomes Validated. ([[UST-005]])
4. **Approve a binding:** An authorized Deployer reviews and approves a
   Validated binding. Record approval evidence and make the binding available
   to execution consumers. ([[UST-005]])
5. **Revalidate changed bindings:** When a compatibility-relevant input
   changes, mark the binding Stale. Revalidation returns it to Validated and
   requires new approval before it becomes Approved again. ([[UST-005]])
6. **Bind simulated equipment:** Select and bind a compatible simulated
   component using the same lifecycle, retaining its simulated classification.
   Simulation runs and result fidelity are handled by the simulation
   capability. ([[UST-005]], [[UST-007]])

## Information and lifecycle

| Information or artifact | Authority | Lifecycle or state changes | Consumers |
| --- | --- | --- | --- |
| Station identity and Station Description | Station and Deployment | Created/revised → versioned and retrieved; revisions may invalidate bindings | Compatibility evaluation and deployment |
| Component-type catalog definition | Governed catalog authority; ownership to be confirmed | Defined/revised → selected by revision for compatibility validation | Station description and binding validation |
| Hardware Component inventory | Station and Deployment records component name, type, and physical/simulated classification | Recorded in a Station Description revision → updated or removed in a later revision | Compatibility evaluation, deployment, simulation |
| Abstract Equipment Capability | Sequence and Process Authoring defines the sequence requirement | Authored with a sequence → matched against station components | Binding candidate search and execution |
| Deployment Binding | Station and Deployment | Draft → Validated → Approved; Approved may become Stale or Revoked; Stale requires revalidation and renewed approval | Execution Orchestration and release validation |
| Simulated Station representation | Simulation capability defines simulated responses; Station and Deployment records supported components and classification | Prepared/configured → selected for simulated execution; version association remains to be defined | Sequence development and verification |

## Sources and traceability

- User stories: [[UST-004-hal-in-the-actors]],
  [[UST-005-semantic-station-globals]], [[UST-007-easy-testing]],
  [[UST-016-validating-a-coherent-release-before-execution]]
- Decision records: [[DEC-002-the-abstraction-of-hardware]]
- Glossary entries: [[CMP-013-SD-station]],
  [[CMP-014-SD-station-description]], [[CMP-015-SD-hardware-component]],
  [[CMP-016-SD-abstract-equipment-capability]],
  [[CMP-017-SD-deployment-binding]], [[CMP-018-SD-simulated-station]]
- Related contexts: [[BC-01-SPA-sequence_and_process_authoring]],
  [[BC-04-EO-execution_orchestration]],
  [[BC-05-ARD-artifact_and_runtime_data]],
  [[BC-06-RO-runtime_operations]],
  [[BC-07-ET-evidence_and_traceability]],
  [[BC-08-QA-quality_assurance]]

## Open questions

- [ ] Who owns and approves component-type catalog definitions and revisions?
- [ ] Is Deployer a dedicated stakeholder role, a permission assigned to an
  existing role, or an automated approval responsibility?
- [ ] Which attributes and checks establish that a Station Description matches
  the current physical station configuration?
- [ ] Which unit conversions and range-comparison rules are allowed when
  evaluating compatibility?
- [ ] Can one Abstract Equipment Capability bind to multiple components, or
  can one component satisfy multiple requirements in a deployment?
- [ ] Which change events invalidate an Approved binding, and how are affected
  bindings marked Stale before use?
- [ ] How are simulation fidelity, configurable responses, and simulator
  versions associated with Station Descriptions and sequence revisions?
- [ ] How are simulated execution results distinguished from physical test
  evidence across downstream systems?
- [ ] How do Station Global variables relate to Station Descriptions and
  component deployment, and how are they initialized or migrated?
- [ ] Which station and binding artifacts participate in UST-016
  release-coherence validation?
