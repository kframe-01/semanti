---
id: "BC-05"
aliases:
  - Artifact and Runtime Data
tags:
  - bounded-context
status: proposed
date_created: "2026-10-23"
last_reviewed: "2026-10-23"
sources:
  - "UST-003"
---

# Artifact and Runtime Data

## Purpose

Provide consistent storage and retrieval for position artifacts, test inputs
and fixtures, execution data and evidence, and temporary development data.
Associate each item with an unambiguous identity and relevant position or
execution so that users and services can develop, run, diagnose, and verify
manufacturing positions without confusing data of different purposes.

## Domain responsibility

### Owns

- The logical Data Manager capability and its storage and retrieval semantics,
  independently of the physical storage backend.
- Classification of phase-one stored items by Artifact Scope.
- Resolution and persistence of each item's identity, associated Position,
  and Execution association when applicable.
- Phase-one per-scope storage authorization and the retrieval behavior defined
  by UST-003.
- Local fallback, pending-synchronization state, later synchronization, and
  conflict reporting when a required backend is unavailable.
- Distinction between phase-one data scopes and the planned phase-two
  Artifact Repository capability for Shared Reusable Artifacts.

### Does not own

- The domain meaning or authoring of a Position Sequence, Test Intent, or
  Station Description.
- Execution orchestration or the production of runtime measurements, logs,
  and verdicts.
- The assessment of whether stored evidence proves that a test or product
  passed.
- Phase-two publication, compatibility governance, discovery, deprecation, and
  lifecycle management of Shared Reusable Artifacts as phase-one scope.
- The choice of a specific storage product or the requirement that all scopes
  use one physical backend.

## Boundary

This context begins when a user or service requests storage or retrieval of an
artifact or data item for development, execution, diagnosis, or verification.
It classifies the item, resolves its scope and associations, checks storage
authorization, and applies the scope's defined persistence behavior.

In phase one, the Data Manager stores and retrieves four scopes: Position
Artifacts, Test Inputs and Fixtures, Execution Data and Evidence, and
Temporary Development Data. If a required backend is unavailable, it can
store locally, report pending synchronization, and later synchronize according
to the defined conflict rules. It does not own the production or domain
assessment of the content. Shared Reusable Artifact governance is planned for
phase two.

## Ubiquitous language

- [[CMP-030-ARD-artifact-scope|Artifact Scope]] - Classification of an item by
  purpose and association, independent of storage backend.
- [[CMP-031-ARD-position-artifact|Position Artifact]] - Position-specific
  project, test logic, configuration, deployment binding, or documentation.
- [[CMP-032-ARD-shared-reusable-artifact|Shared Reusable Artifact]] -
  Reviewed, versioned artifact intended for use by more than one position;
  governed repository lifecycle is future phase-two scope.
- [[CMP-033-ARD-test-input-and-fixture|Test Input and Fixture]] - Controlled
  input material needed to run a test, such as reference values, calibration
  fixtures, or datasets.
- [[CMP-038-ARD-temporary-development-data|Temporary Development Data]] -
  Disposable intermediate development or debugging material unless promoted
  into a governed scope.
- [[CMP-039-ARD-artifact-repository|Artifact Repository]] - Proposed
  phase-two capability for publishing, discovering, retrieving, and
  versioning Shared Reusable Artifacts.

## Policies and invariants

- Every stored item has a scope and unique identity within that scope, an
  associated Position, and an Execution association when applicable.
- If association context is ambiguous or conflicting, storage is rejected
  with actionable validation information; the Data Manager does not guess.
- Phase-one Position Artifacts, Test Inputs and Fixtures, and Temporary
  Development Data may be overwritten by an authorized store request using
  the same scope and identity.
- Existing Execution Data and Evidence cannot be overwritten by an item with
  the same identity.
- Retrieval in phase one is unrestricted and does not require authentication;
  storage requires authentication and an explicit grant for the scope.
- When a required backend is unavailable, local storage is marked pending
  synchronization and is not reported as having reached the intended backend.
- During synchronization, an existing backend item with the same scope and
  identity remains authoritative. The conflict is reported and the conflicting
  local item is deleted; it is not silently represented as synchronized.
- Temporary Development Data is not treated as retained Execution Evidence
  or as a published Position Artifact unless explicitly promoted under defined
  governance.
- Shared Reusable Artifact publication and lifecycle governance are outside
  phase-one Data Manager scope.

## Collaborations and context map

| Related context | Relationship | Information exchanged | Notes |
| --- | --- | --- | --- |
| [[BC-01-SPA-sequence_and_process_authoring]] | Upstream provider / consumer | Position identity and authored Position Artifacts | Sequence meaning and authoring remain owned by Sequence and Process Authoring. |
| [[BC-02-IR-intent_and_requirements]] | Upstream provider / consumer | Test Intent and Requirement artifacts, where persisted | This context stores data; semantic ownership remains with Intent and Requirements. |
| [[BC-03-SD-station_and_eployment]] | Upstream provider / consumer | Station Descriptions and Deployment Binding artifacts | Station and Deployment owns their compatibility and lifecycle semantics. |
| [[BC-04-EO-execution_orchestration]] | Upstream producer | Execution identity, data, logs, measurements, and evidence for storage | Execution Orchestration produces runtime outcomes; this context stores and retrieves associated items. |
| [[BC-06-RO-runtime_operations]] | Consumer | Retrieved position, execution, and supporting data for runtime users | Runtime Operations presents data; it does not own storage semantics. |
| [[BC-07-ET-evidence_and_traceability]] | Storage provider / consumer | Execution Logs, Execution Evidence, Traceability Records, identities, and associations | Evidence and Traceability owns evidence meaning; this context owns persistence and retrieval. |
| [[BC-08-QA-quality_assurance]] | Storage provider / consumer | Prüflisten, sequence descriptions, approval records, and assessments | Quality Assurance owns validation and assessment semantics. |

## Key workflows

1. **Store a phase-one item:** An authorized user or service chooses a scope
   and supplies content and identity. The Data Manager resolves the Position
   and optional Execution association, rejects ambiguous context, and stores
   according to the scope's overwrite rules. ([[UST-003]])
2. **Retrieve an item:** A caller requests an item by scope and identity. The
   Data Manager returns its content and persisted Position and Execution
   associations; phase-one retrieval does not require authentication.
   ([[UST-003]])
3. **Handle unavailable backends:** When the intended backend is unavailable,
   store locally, mark the item pending synchronization, and report that the
   backend write is incomplete. Synchronize when available. ([[UST-003]])
4. **Resolve a synchronization conflict:** If the backend already contains an
   item with the same scope and identity, retain the backend item, report the
   conflict, and delete the conflicting local item. ([[UST-003]])
5. **Defer shared reuse governance:** In phase two, use an Artifact Repository
   to govern publication, discovery, compatibility, retrieval, and lifecycle
   of Shared Reusable Artifacts. These capabilities are not implied by
   phase-one storage and retrieval. ([[UST-003]])

## Information and lifecycle

| Information or artifact | Authority | Lifecycle or state changes | Consumers |
| --- | --- | --- | --- |
| Position Artifact | Producing/authoring context owns content; Data Manager owns phase-one storage behavior | Stored/retrieved by scope and identity; a same-identity store overwrites | Position development, project generation, and deployment |
| Test Input and Fixture | Test or configuration owner defines content; Data Manager owns phase-one storage behavior | Stored/retrieved by scope and identity; a same-identity store overwrites | Execution Orchestration and verification |
| Execution Data and Evidence | Execution capability produces content; Data Manager owns phase-one storage behavior | Stored once or retrieved by identity and associations; same-identity overwrite is rejected | Runtime Operations, diagnosis, verification, and quality review |
| Temporary Development Data | Creating user or service produces content; Data Manager owns its phase-one scope and association behavior | Stored/retrieved by scope and identity; same-identity store overwrites; may be explicitly promoted under future governance | Development and debugging workflows |
| Local pending item | Data Manager | Locally stored and marked pending → synchronized, or conflict reported and local conflicting item deleted | Original caller and intended backend |
| Shared Reusable Artifact | Artifact Repository capability is proposed as future authority; detailed ownership is open | Future phase: reviewed/versioned → published/retrievable → deprecated or retired under rules to be defined | Multiple positions and their development workflows |

## Sources and traceability

- User stories: [[UST-003-artifactory-and-data]]
- Glossary entries: [[CMP-030-ARD-artifact-scope]],
  [[CMP-031-ARD-position-artifact]],
  [[CMP-032-ARD-shared-reusable-artifact]],
  [[CMP-033-ARD-test-input-and-fixture]],
  [[CMP-038-ARD-temporary-development-data]],
  [[CMP-039-ARD-artifact-repository]]
- Related contexts: [[BC-01-SPA-sequence_and_process_authoring]],
  [[BC-02-IR-intent_and_requirements]],
  [[BC-03-SD-station_and_eployment]],
  [[BC-04-EO-execution_orchestration]],
  [[BC-06-RO-runtime_operations]],
  [[BC-07-ET-evidence_and_traceability]],
  [[BC-08-QA-quality_assurance]]

## Open questions

- [ ] Which metadata, retention, deletion, and promotion rules apply to each
  phase-one scope?
- [ ] Which outputs qualify as governed Execution Evidence rather than
  diagnostic or temporary data?
- [ ] What mechanisms resolve Position and Execution associations from caller
  context, storage path, or session, and how are conflicting sources handled?
- [ ] How are pending local items surfaced and monitored before synchronization
  completes?
- [ ] Which storage backends are used for each scope, and what consistency
  guarantees do they provide?
- [ ] How are backend conflicts audited and communicated to affected callers?
- [ ] Which phase-two approval, compatibility, publication, discovery,
  deprecation, and immutability rules apply to Shared Reusable Artifacts?
- [ ] Is Artifactory a product requirement or shorthand for the Artifact
  Repository capability?
- [ ] Which version-history capabilities, if any, are needed beyond the
  explicitly defined phase-one overwrite and no-overwrite rules?
