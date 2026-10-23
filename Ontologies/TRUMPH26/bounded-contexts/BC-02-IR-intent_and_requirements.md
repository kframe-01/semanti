---
id: "BC-02"
aliases:
  - Intent and Requirements
tags:
  - bounded-context
status: proposed
date_created: "2026-10-23"
last_reviewed: "2026-10-23"
sources:
  - "UST-001"
  - "UST-002"
  - "UST-023"
  - "UST-024"
  - "UST-025"
  - "DEC-003"
---

# Intent and Requirements

## Purpose

Capture what a test is intended to accomplish, refine that intent into
structured and verifiable requirements, and preserve the meaning of the test
across downstream sequence authoring and variant analysis. This context gives
Product Owners and Testing Engineers a shared, domain-readable basis for
describing expected behavior and product-specific differences.

## Domain responsibility

### Owns

- The meaning and domain content of Test Intents, including purpose, subject
  under test, relevant conditions, and intended outcomes.
- Refinement of Test Intents into structured Requirements and measurable
  Verification Criteria.
- The controlled domain language and representation used to express and
  exchange Test Intents.
- Domain descriptions of Product Variants, Parameter Profiles, and Parameter
  Overrides.
- The meaning and reviewable content of Reuse Recommendations, including
  identified shared test logic, variant differences, and rationale.
- Traceability between intents, refined requirements, verification criteria,
  and variant-specific descriptions.

### Does not own

- Position Sequence authoring, Step Types, Test Types, or reusable process
  definitions; these belong to Sequence and Process Authoring.
- The portfolio-wide RDF transformation, product comparison, and generation
  of Reuse Recommendations, which are performed by the UST-024 reuse-analysis
  capability.
- Approval or rejection of Reuse Recommendations, continuous sequence
  validation, or joint sequence approval; these belong to the relevant
  downstream workflow.
- Parameter inheritance and base-profile application rules, which remain
  unresolved and are outside the ownership defined by UST-024.
- LabVIEW project generation, machine integration, or runtime selection of
  product serialization and test limits.

## Boundary

This context begins when a Product Owner or Testing Engineer expresses a test
need and its intended result. It covers domain-readable Test Intent
descriptions, their formal representation, refinement into Requirements and
Verification Criteria, and product-variant parameter information used to
describe differences.

It provides meaning-preserving inputs to sequence authoring and downstream
analysis. It does not define the position-specific order or implementation of
steps, perform portfolio comparison itself, approve resulting recommendations,
or generate executable projects.

## Ubiquitous language

- [[CMP-003-IR-test-intent|Test Intent]] - Domain description of a test's
  purpose, subject under test, conditions, and intended outcome.
- [[CMP-004-IR-requirement|Requirement]] - Structured need or expected behavior
  refined from a Test Intent so it can be reviewed and verified.
- [[CMP-005-IR-verification-criterion|Verification Criterion]] - Observable
  or measurable condition for checking whether intended behavior was met.
- [[CMP-036-IR-domain-specific-language|Domain-Specific Language]] - Controlled
  Robot Framework `.robot` representation for stakeholder-readable Test
  Intents and downstream interpretation.
- [[CMP-040-IR-product-variant|Product Variant]] - Product configuration that
  may differ in test parameters, limits, or steps.
- [[CMP-042-IR-parameter-profile|Parameter Profile]] - Baseline set of
  parameter values for a product or product family.
- [[CMP-043-IR-parameter-override|Parameter Override]] - Product- or
  variant-specific difference from a baseline parameter value or limit.
- [[CMP-044-IR-reuse-recommendation|Reuse Recommendation]] - Reviewable
  proposal to share test logic across products, with supporting differences
  and rationale.

## Policies and invariants

- A Test Intent states intended behavior, not the implementation of a runnable
  Position Sequence or station-specific hardware configuration.
- Refinement into Requirements and Verification Criteria must preserve the
  intended meaning; ambiguity and missing information are recorded rather
  than silently resolved.
- Expected outcomes should be observable or measurable enough to support
  verification.
- Variant descriptions make product-specific parameters, limits, and
  step-inclusion differences explicit relative to an identified baseline
  where one is defined.
- A Parameter Override records a difference from a Parameter Profile; it does
  not itself define inheritance, precedence, or validation rules.
- A Reuse Recommendation is evidence-backed guidance, not approval or an
  implementation decision.
- A formal representation supports both stakeholder review and structured
  downstream processing. Robot Framework representation does not require the
  manufacturing runtime to execute Robot Framework directly.

## Collaborations and context map

| Related context | Relationship | Information exchanged | Notes |
| --- | --- | --- | --- |
| [[BC-01-SPA-sequence_and_process_authoring]] | Downstream consumer | Accepted Test Intent, refined Requirements, Verification Criteria, and variant/parameter descriptions | Sequence authoring preserves intent while defining position-specific flow and steps. |
| [[BC-05-ARD-artifact_and_runtime_data]] | Persistence collaboration | Structured intent and requirement artifacts, where persistence is provided | Storage behavior is separate from semantic ownership. |
| [[BC-07-ET-evidence_and_traceability]] | Upstream provider | Test Intent version and expected behavior for the execution | Evidence and Traceability records the version associated with execution outputs. |
| [[BC-08-QA-quality_assurance]] | Downstream consumer | Requirements and Verification Criteria; variant rules and expected behavior | Quality Assurance uses these definitions for sequence validation and log assessment. |
| LabVIEW project generation | Downstream consumer | Accepted formal Test Intent and position/variant information | UST-002 owns project generation, not the meaning of the intent. |
| Product portfolio reuse analysis | Analytical collaboration | Formal Test Intents, product/variant descriptions, profiles, and overrides; comparison results and Reuse Recommendations | UST-024 transforms descriptions to RDF and generates portfolio comparisons and recommendations. |

## Key workflows

1. **Describe a Test Intent:** A Product Owner or Testing Engineer records the
   test purpose, subject, conditions, expected behavior, and measurable
   outcome using the controlled domain language. Ambiguities are captured for
   clarification. ([[UST-001]], [[DEC-003]])
2. **Refine and verify intent:** Reviewers refine an accepted Test Intent into
   structured Requirements and Verification Criteria without changing its
   meaning. ([[UST-001]])
3. **Describe product-variant differences:** Authors identify Product
   Variants, baseline Parameter Profiles, and explicit Parameter Overrides,
   including variant-specific test-step inclusion or omission where applicable.
   ([[UST-001]], [[UST-024]])
4. **Analyze reuse across a portfolio:** The reuse-analysis capability
   transforms accepted formal descriptions, compares products, and returns
   Reuse Recommendations with shared subsets, differences, and rationale for
   human review. ([[UST-024]])
5. **Pass intent downstream:** The accepted formal description and its
   traceability information are made available for sequence authoring and
   project generation. ([[UST-002]], [[UST-023]])

## Information and lifecycle

| Information or artifact | Authority | Lifecycle or state changes | Consumers |
| --- | --- | --- | --- |
| Test Intent | Intent and Requirements owns its domain meaning | Draft → clarified/reviewed → accepted → refined or superseded | Sequence authoring, requirements refinement, reuse analysis, project generation |
| Requirement | Intent and Requirements owns the refined statement | Draft/refined → reviewed and ready for verification; exact states remain to be defined | Sequence authoring and Quality Assurance |
| Verification Criterion | Intent and Requirements owns the criterion definition | Derived → reviewed/accepted; execution results are recorded elsewhere | Verification and Quality Assurance |
| Domain-Specific Language description | Intent and Requirements owns the domain convention; the storage format owner is to be determined | Authored → validated/reviewed → accepted and consumed downstream | Reuse analysis, sequence authoring, project generation |
| Product Variant and Parameter Profile | Intent and Requirements owns their domain descriptions; product master-data authority is to be determined | Defined or updated → compared and validated downstream | Reuse analysis and sequence validation |
| Parameter Override | Intent and Requirements owns the described exception; application and precedence rules are unresolved | Declared → checked against baseline and applicable limits | Reuse analysis and sequence validation |
| Reuse Recommendation | UST-024 analysis capability generates the recommendation; reviewers decide whether to adopt it | Generated → reviewed, accepted/rejected/modified; persistence and versioning remain open | Product Owner, Testing Engineer, sequence authoring |

## Sources and traceability

- User stories: [[UST-001-natural-and-formal-description]],
  [[UST-002-dsl-to-poject]],
  [[UST-023-accessible-sequence-authoring-with-typed-steps]],
  [[UST-024-product-variant-management-and-reuse-optimization]],
  [[UST-025-continuous-validation-and-approval-workflow]]
- Decision records: [[DEC-003-use-robot-language-for-test-intents]]
- Glossary entries: [[CMP-003-IR-test-intent]],
  [[CMP-004-IR-requirement]], [[CMP-005-IR-verification-criterion]],
  [[CMP-036-IR-domain-specific-language]],
  [[CMP-040-IR-product-variant]], [[CMP-042-IR-parameter-profile]],
  [[CMP-043-IR-parameter-override]],
  [[CMP-044-IR-reuse-recommendation]]
- Related context: [[BC-01-SPA-sequence_and_process_authoring]]
- Related contexts: [[BC-05-ARD-artifact_and_runtime_data]],
  [[BC-07-ET-evidence_and_traceability]],
  [[BC-08-QA-quality_assurance]]

## Open questions

- [ ] Which Test Intent fields and review states are mandatory for acceptance?
- [ ] Which `.robot` sections, metadata, keywords, and semantic validation
  rules are required by the controlled Domain-Specific Language?
- [ ] What structure and agreement state make a Requirement ready for use?
- [ ] Which Verification Criteria must be quantitative, and who accepts them?
- [ ] How are domain vocabulary and ambiguous terms governed and versioned?
- [ ] Which RDF schema and matching rules are used for portfolio analysis, and
  how are generated recommendations persisted and versioned?
- [ ] How are Product Variants identified and related to product families and
  authoritative product master data?
- [ ] How are Parameter Profiles selected, inherited, versioned, and applied?
- [ ] Which Parameter Override precedence and validation rules apply?
- [ ] Which context owns approval or rejection of Reuse Recommendations, given
  the ownership references in UST-024 and UST-025?
- [ ] Which capability owns persistence and version history for Test Intents,
  Requirements, Verification Criteria, and formal descriptions?
