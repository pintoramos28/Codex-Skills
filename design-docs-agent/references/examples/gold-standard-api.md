# API Design — Example (Gold Standard) (DOC:API-100)

## L1 Summary (SEC:API-L1)
- REST endpoints for upload, status, and data preview. (ID:SUM-001)

## L2 Design Detail (SEC:API-L2)
### Endpoints / Operations (SEC:API-ENDPOINTS)
| Method | Path | Auth | Description | ID |
|---|---|---|---|---|
| POST | /uploads | Required | Create upload and return pre‑signed URL | API-001 |
| GET | /uploads/{id} | Required | Get upload status | API-002 |
| GET | /datasets/{id}/preview | Required | Preview normalized data | API-003 |

### Contracts (SEC:API-CONTRACTS)
#### Request (ID:REQ-001)
```json
{ "filename": "data.csv", "schema": "default" }
```

#### Response (ID:RES-001)
```json
{ "id": "upl_123", "uploadUrl": "https://...", "status": "pending" }
```

### Errors (SEC:API-ERRORS)
| Code | Meaning | Recovery | ID |
|---|---|---|---|
| 400 | Invalid schema | Fix CSV columns | ERR-001 |
| 413 | File too large | Upload smaller file | ERR-002 |
| 500 | Processing failed | Retry later | ERR-003 |

### Auth / Rate Limits (SEC:API-AUTH)
- JWT auth required. (ID:AUTH-001)
- 10 uploads/min/user. (ID:AUTH-002)

## L3 Implementation Notes (if needed) (SEC:API-L3)
- Use pre‑signed S3 URLs for direct upload. (ID:NOTE-001)

## Design Checklist (SEC:API-CHECK)
| Item | Pass/Fail | Notes | ID |
|---|---|---|---|
| Dependencies identified | Pass | S3 | CHECK-001 |
| Risks identified | Pass | Large uploads | CHECK-002 |
| Observability planned | Pass | Error counters | CHECK-003 |
| Rollout plan defined | Pass | Feature flag | CHECK-004 |
| Migration plan defined | Pass | N/A | CHECK-005 |
| Test scope defined | Pass | API + auth | CHECK-006 |

## Known Unknowns (SEC:API-UNK)
- Final auth provider selection. (ID:UNK-001)
