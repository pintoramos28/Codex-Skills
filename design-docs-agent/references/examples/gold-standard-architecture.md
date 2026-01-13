# Architecture Overview — Example (Gold Standard) (DOC:ARCH-100)

## L1 Summary (SEC:ARCH-L1)
- Build a web app that ingests CSV uploads, normalizes data, and exposes it via a REST API and UI. (ID:SUM-001)
- Split into ingestion, processing, storage, and API layers with clear contracts. (ID:SUM-002)
- Use Postgres for canonical storage; S3 for raw files; background jobs for normalization. (ID:SUM-003)

## Goals / Non‑Goals (SEC:ARCH-GOALS)
**Goals**
- Reliable CSV ingestion with schema validation and normalization. (ID:GOAL-001)
- Queryable data via REST endpoints with pagination and filters. (ID:GOAL-002)
- Basic UI for upload, status, and data preview. (ID:GOAL-003)

**Non‑Goals**
- Real‑time ingestion. (ID:NONGOAL-001)
- Complex analytics/BI. (ID:NONGOAL-002)

## L2 Design Detail (SEC:ARCH-L2)
### Components (SEC:ARCH-COMP)
- **Web UI**: Upload CSV, track status, preview normalized data. (ID:COMP-001)
- **API Service**: Auth, ingestion initiation, query endpoints. (ID:COMP-002)
- **Worker Service**: Parse CSV, validate schema, normalize data. (ID:COMP-003)
- **Storage**: S3 for raw uploads; Postgres for normalized records. (ID:COMP-004)

### Data Flow (SEC:ARCH-FLOW)
1) User uploads CSV → API stores raw file in S3. (ID:FLOW-001)
2) API enqueues job with S3 key. (ID:FLOW-002)
3) Worker downloads CSV, validates schema, normalizes records. (ID:FLOW-003)
4) Worker writes to Postgres; updates job status. (ID:FLOW-004)
5) UI queries API for status and data preview. (ID:FLOW-005)

### Integrations (SEC:ARCH-INT)
- S3 for raw uploads. (ID:INT-001)
- Job queue (e.g., Redis/Sidekiq/BullMQ). (ID:INT-002)

## L3 Implementation Notes (if needed) (SEC:ARCH-L3)
- Use multipart upload for >50MB files. (ID:NOTE-001)
- Enforce CSV max row count to prevent resource exhaustion. (ID:NOTE-002)

## Design Checklist (SEC:ARCH-CHECK)
| Item | Pass/Fail | Notes | ID |
|---|---|---|---|
| Dependencies identified | Pass | S3, queue, Postgres | CHECK-001 |
| Risks identified | Pass | Large files, invalid schemas | CHECK-002 |
| Observability planned | Pass | Job metrics, error logs | CHECK-003 |
| Rollout plan defined | Pass | Feature flag for uploads | CHECK-004 |
| Migration plan defined | Pass | Initial schema + backfill | CHECK-005 |
| Test scope defined | Pass | Parsing, validation, API | CHECK-006 |

## Known Unknowns (SEC:ARCH-UNK)
- Final CSV schema(s) per tenant. (ID:UNK-001)
