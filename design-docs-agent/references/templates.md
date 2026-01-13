# Design Docs Templates

These templates are intended to be copied into project docs (under a `design/` folder) and then filled in.
Keep sections tight and prefer bullets/tables. Use L1/L2/L3 depth model.

---

## 1) Overall Plan (`design/plan.md`)

```markdown
# Plan (DOC:PLAN-001)

## Status Legend (SEC:PLAN-LEGEND)
- [N] = Not Started
- [I] = In Progress
- [B] = Blocked
- [D] = Done

## Phase 0 — Discovery & Alignment (SEC:PLAN-P0)
- [N] Task: … (ID:TASK-P0-001)
- [N] Task: … (ID:TASK-P0-002)

## Phase 1 — Core Build (SEC:PLAN-P1)
- [N] Task: … (ID:TASK-P1-001)
- [N] Task: … (ID:TASK-P1-002)

## Phase 2 — Hardening & Launch (SEC:PLAN-P2)
- [N] Task: … (ID:TASK-P2-001)

## Dependencies (SEC:PLAN-DEPS)
- … (ID:DEP-001) depends on … (ID:TASK-…)

## Risks & Mitigations (SEC:PLAN-RISKS)
- Risk: … (ID:RISK-001) → Mitigation: … (ID:MIT-001)

## Next Steps (SEC:PLAN-NEXT)
- … (ID:NEXT-001)
```

---

## 2) Architecture Overview (`design/architecture.md`)

```markdown
# Architecture Overview (DOC:ARCH-001)

## L1 Summary (SEC:ARCH-L1)
- … (ID:SUM-001)

## Goals / Non‑Goals (SEC:ARCH-GOALS)
**Goals**
- … (ID:GOAL-001)
**Non‑Goals**
- … (ID:NONGOAL-001)

## L2 Design Detail (SEC:ARCH-L2)
### Components (SEC:ARCH-COMP)
- Component A: … (ID:COMP-001)
- Component B: … (ID:COMP-002)

### Data Flow (SEC:ARCH-FLOW)
- … (ID:FLOW-001)

### Integrations (SEC:ARCH-INT)
- … (ID:INT-001)

## L3 Implementation Notes (if needed) (SEC:ARCH-L3)
- … (ID:NOTE-001)

## Design Checklist (SEC:ARCH-CHECK)
| Item | Pass/Fail | Notes | ID |
|---|---|---|---|
| Dependencies identified |  |  | CHECK-001 |
| Risks identified |  |  | CHECK-002 |
| Observability planned |  |  | CHECK-003 |
| Rollout plan defined |  |  | CHECK-004 |
| Migration plan defined |  |  | CHECK-005 |
| Test scope defined |  |  | CHECK-006 |

## Known Unknowns (SEC:ARCH-UNK)
- … (ID:UNK-001)
```

---

## 3) Feature Design Spec (`design/feature-spec.md`)

```markdown
# Feature Design Spec (DOC:FEAT-001)

## L1 Summary (SEC:FEAT-L1)
- … (ID:SUM-001)

## Problem Statement (SEC:FEAT-PROB)
- … (ID:PROB-001)

## User Stories (SEC:FEAT-STORIES)
- As a … I want … so that … (ID:STORY-001)

## Acceptance Criteria (SEC:FEAT-AC)
- … (ID:AC-001)

## L2 Design Detail (SEC:FEAT-L2)
### UX / Flow (SEC:FEAT-FLOW)
- … (ID:FLOW-001)

### Edge Cases (SEC:FEAT-EDGE)
- … (ID:EDGE-001)

### Open Questions (SEC:FEAT-OPEN)
- … (ID:Q-001)

## L3 Implementation Notes (if needed) (SEC:FEAT-L3)
- … (ID:NOTE-001)

## Design Checklist (SEC:FEAT-CHECK)
| Item | Pass/Fail | Notes | ID |
|---|---|---|---|
| Dependencies identified |  |  | CHECK-001 |
| Risks identified |  |  | CHECK-002 |
| Observability planned |  |  | CHECK-003 |
| Rollout plan defined |  |  | CHECK-004 |
| Migration plan defined |  |  | CHECK-005 |
| Test scope defined |  |  | CHECK-006 |

## Known Unknowns (SEC:FEAT-UNK)
- … (ID:UNK-001)
```

---

## 4) API Design (`design/api.md`)

```markdown
# API Design (DOC:API-001)

## L1 Summary (SEC:API-L1)
- … (ID:SUM-001)

## L2 Design Detail (SEC:API-L2)
### Endpoints / Operations (SEC:API-ENDPOINTS)
| Method | Path | Auth | Description | ID |
|---|---|---|---|---|
|  |  |  |  | API-001 |

### Contracts (SEC:API-CONTRACTS)
#### Request (ID:REQ-001)
```json
{}
```

#### Response (ID:RES-001)
```json
{}
```

### Errors (SEC:API-ERRORS)
| Code | Meaning | Recovery | ID |
|---|---|---|---|
|  |  |  | ERR-001 |

### Auth / Rate Limits (SEC:API-AUTH)
- … (ID:AUTH-001)

## L3 Implementation Notes (if needed) (SEC:API-L3)
- … (ID:NOTE-001)

## Design Checklist (SEC:API-CHECK)
| Item | Pass/Fail | Notes | ID |
|---|---|---|---|
| Dependencies identified |  |  | CHECK-001 |
| Risks identified |  |  | CHECK-002 |
| Observability planned |  |  | CHECK-003 |
| Rollout plan defined |  |  | CHECK-004 |
| Migration plan defined |  |  | CHECK-005 |
| Test scope defined |  |  | CHECK-006 |

## Known Unknowns (SEC:API-UNK)
- … (ID:UNK-001)
```

---

## 5) Data Model (`design/data-model.md`)

```markdown
# Data Model (DOC:DATA-001)

## L1 Summary (SEC:DATA-L1)
- … (ID:SUM-001)

## L2 Design Detail (SEC:DATA-L2)
### Entities (SEC:DATA-ENT)
- Entity A (ID:ENT-001)
  - Fields: … (ID:FIELD-001)
  - Relationships: … (ID:REL-001)

### Migrations (SEC:DATA-MIG)
- … (ID:MIG-001)

### Backward Compatibility (SEC:DATA-BC)
- … (ID:BC-001)

## L3 Implementation Notes (if needed) (SEC:DATA-L3)
- … (ID:NOTE-001)

## Design Checklist (SEC:DATA-CHECK)
| Item | Pass/Fail | Notes | ID |
|---|---|---|---|
| Dependencies identified |  |  | CHECK-001 |
| Risks identified |  |  | CHECK-002 |
| Observability planned |  |  | CHECK-003 |
| Rollout plan defined |  |  | CHECK-004 |
| Migration plan defined |  |  | CHECK-005 |
| Test scope defined |  |  | CHECK-006 |

## Known Unknowns (SEC:DATA-UNK)
- … (ID:UNK-001)
```

---

## 6) Non‑Functional Requirements (`design/non-functional.md`)

```markdown
# Non‑Functional Requirements (DOC:NFR-001)

## L1 Summary (SEC:NFR-L1)
- … (ID:SUM-001)

## L2 Design Detail (SEC:NFR-L2)
### Security (SEC:NFR-SEC)
- AuthN/AuthZ: … (ID:SEC-001)
- PII handling: … (ID:SEC-002)

### Compliance (SEC:NFR-COMP)
- SOC2/GDPR: … (ID:COMP-001)

### Performance & Scalability (SEC:NFR-PERF)
- Latency budget: … (ID:PERF-001)
- Throughput: … (ID:PERF-002)

### Cost (SEC:NFR-COST)
- Cost ceiling: … (ID:COST-001)

## L3 Implementation Notes (if needed) (SEC:NFR-L3)
- … (ID:NOTE-001)

## Design Checklist (SEC:NFR-CHECK)
| Item | Pass/Fail | Notes | ID |
|---|---|---|---|
| Dependencies identified |  |  | CHECK-001 |
| Risks identified |  |  | CHECK-002 |
| Observability planned |  |  | CHECK-003 |
| Rollout plan defined |  |  | CHECK-004 |
| Migration plan defined |  |  | CHECK-005 |
| Test scope defined |  |  | CHECK-006 |

## Known Unknowns (SEC:NFR-UNK)
- … (ID:UNK-001)
```

---

## 7) Test Plan (`design/test-plan.md`)

```markdown
# Test Plan (DOC:TEST-001)

## L1 Summary (SEC:TEST-L1)
- … (ID:SUM-001)

## L2 Design Detail (SEC:TEST-L2)
### Unit Tests (SEC:TEST-UNIT)
- … (ID:UNIT-001)

### Integration Tests (SEC:TEST-INT)
- … (ID:INT-001)

### E2E Tests (SEC:TEST-E2E)
- … (ID:E2E-001)

### Test Data / Fixtures (SEC:TEST-DATA)
- … (ID:DATA-001)

### Observability / Rollback Testing (SEC:TEST-OBS)
- … (ID:OBS-001)

## L3 Implementation Notes (if needed) (SEC:TEST-L3)
- … (ID:NOTE-001)

## Design Checklist (SEC:TEST-CHECK)
| Item | Pass/Fail | Notes | ID |
|---|---|---|---|
| Dependencies identified |  |  | CHECK-001 |
| Risks identified |  |  | CHECK-002 |
| Observability planned |  |  | CHECK-003 |
| Rollout plan defined |  |  | CHECK-004 |
| Migration plan defined |  |  | CHECK-005 |
| Test scope defined |  |  | CHECK-006 |

## Known Unknowns (SEC:TEST-UNK)
- … (ID:UNK-001)
```

---

## 8) ADR (`design/adrs/0001-title.md`)

```markdown
# ADR 0001: Title (DOC:ADR-0001)

## Context (SEC:ADR-CTX)
- … (ID:CTX-001)

## Decision (SEC:ADR-DEC)
- … (ID:DEC-001)

## Consequences (SEC:ADR-CONS)
- … (ID:CONS-001)
```
