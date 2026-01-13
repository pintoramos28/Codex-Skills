---
name: design-docs-agent
description: Create and maintain software design documentation for web applications. Use when Codex must produce structured design docs (architecture overview, feature design spec, API design, data model, non-functional requirements, test plan, ADRs) plus a phased implementation plan with progress tracking and AI-agent-ready detail.
---

# Design Docs Agent

## Workflow

1) **Identify scope + doc set**
- Confirm the feature or project scope.
- Produce the core doc set:
  - Architecture Overview
  - Feature Design Spec
  - API Design
  - Data Model
  - Non‑Functional Requirements
  - Test Plan
  - ADRs (as needed)
- **Always** produce an overall Plan doc with tasks grouped into phases and explicit progress tracking.

2) **Read repository context (if available)**
- Scan: README, existing architecture docs, API schemas, folder conventions, CI/CD notes.
- If repo context is missing or ambiguous, ask 2–3 clarifying questions before drafting.

3) **Depth model**
- Use tiered depth in each doc:
  - L1 Summary (short)
  - L2 Design detail (required)
  - L3 Implementation notes (only if non‑trivial or risky)
- Prefer structured artifacts (tables, contracts, pseudocode) over long narrative.

4) **Constraints**
- Always include constraints checklist: security (authN/authZ), privacy/PII handling, compliance (SOC2/GDPR), scalability, latency budgets, cost ceilings.
- Make trade‑offs explicit if any constraints conflict.

5) **Validation + quality**
- Include a “Design Checklist” with pass/fail items: dependencies, risks, observability, rollout, migration, test scope.
- Include a “Known Unknowns” section for missing inputs.

6) **Brevity vs completeness**
- Target length per doc; default to concise but implementation‑ready.
- Avoid redundant context; reference a single canonical section instead.
- Use appendices for deep details.

## Output structure

Produce the following markdown files (or sections if a single doc is required):

1) `design/plan.md`
- Phased implementation plan (e.g., Phase 0/1/2)
- Task list with status markers (Not Started / In Progress / Blocked / Done)
- Dependencies between tasks
- Next steps section

2) `design/architecture.md`
- Context, goals, non‑goals
- System diagram (ASCII or mermaid if allowed)
- Major components and responsibilities
- Data flow and integrations

3) `design/feature-spec.md`
- Problem statement, user stories, acceptance criteria
- Flows / UX notes
- Edge cases

4) `design/api.md`
- Endpoint list or GraphQL schema
- Request/response contracts
- Error model
- Auth and rate‑limits

5) `design/data-model.md`
- Entities, fields, relationships
- Migrations and backward compatibility

6) `design/non-functional.md`
- Security, privacy, compliance
- Performance and scalability targets
- Cost considerations

7) `design/test-plan.md`
- Unit/integration/e2e scope
- Test data and fixtures
- Observability and rollback testing

8) `design/adrs/` (if needed)
- ADR template: Context → Decision → Consequences

## Style
- Primary audience: engineers, secondarily AI agents.
- Write to be actionable by a fresh AI developer with minimal back‑and‑forth.
- Keep sections tight; use bullets and tables.
- **Traceability**: Every doc, section, and actionable item must include a unique ID. Use IDs to cross‑reference related items across docs.

## When to ask questions
- Missing stack profile or repo context
- Unclear API style or data store
- Unspecified compliance or security constraints

## References
- `references/templates.md` for doc templates
- `references/stack-profiles.md` for stack defaults
- `references/checklists.md` for validation and repo scan
- `references/output-guidelines.md` for length and style guidance

## Example docs
- `references/examples/gold-standard-plan.md`
- `references/examples/gold-standard-architecture.md`
- `references/examples/gold-standard-feature-spec.md`
- `references/examples/gold-standard-api.md`
- `references/examples/gold-standard-data-model.md`
- `references/examples/gold-standard-non-functional.md`
- `references/examples/gold-standard-test-plan.md`
- `references/examples/gold-standard-adr.md`
- `references/examples/bad-example.md` (contrast example)
