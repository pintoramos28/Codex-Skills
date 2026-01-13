# Data Model — Example (Gold Standard) (DOC:DATA-100)

## L1 Summary (SEC:DATA-L1)
- Store upload jobs and normalized records keyed by dataset. (ID:SUM-001)

## L2 Design Detail (SEC:DATA-L2)
### Entities (SEC:DATA-ENT)
- **UploadJob** (ID:ENT-001)
  - Fields: id, userId, datasetId, status, createdAt, updatedAt (ID:FIELD-001)
- **Dataset** (ID:ENT-002)
  - Fields: id, name, schema, createdAt (ID:FIELD-002)
- **Record** (ID:ENT-003)
  - Fields: id, datasetId, data (jsonb), createdAt (ID:FIELD-003)

### Migrations (SEC:DATA-MIG)
- Add tables: upload_jobs, datasets, records. (ID:MIG-001)

### Backward Compatibility (SEC:DATA-BC)
- New tables only; no breaking changes. (ID:BC-001)

## L3 Implementation Notes (if needed) (SEC:DATA-L3)
- Index (datasetId, createdAt) for preview pagination. (ID:NOTE-001)

## Design Checklist (SEC:DATA-CHECK)
| Item | Pass/Fail | Notes | ID |
|---|---|---|---|
| Dependencies identified | Pass | Postgres | CHECK-001 |
| Risks identified | Pass | Storage growth | CHECK-002 |
| Observability planned | Pass | DB metrics | CHECK-003 |
| Rollout plan defined | Pass | Migrations | CHECK-004 |
| Migration plan defined | Pass | Initial schema | CHECK-005 |
| Test scope defined | Pass | CRUD ops | CHECK-006 |

## Known Unknowns (SEC:DATA-UNK)
- Final schema per dataset. (ID:UNK-001)
