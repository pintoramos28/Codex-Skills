# Test Plan — Example (Gold Standard) (DOC:TEST-100)

## L1 Summary (SEC:TEST-L1)
- Cover upload flow, processing, and preview. (ID:SUM-001)

## L2 Design Detail (SEC:TEST-L2)
### Unit Tests (SEC:TEST-UNIT)
- CSV parser validation and error mapping. (ID:UNIT-001)
- Status transitions. (ID:UNIT-002)

### Integration Tests (SEC:TEST-INT)
- Upload → process → preview pipeline. (ID:INT-001)
- Auth + rate limits. (ID:INT-002)

### E2E Tests (SEC:TEST-E2E)
- UI upload + status + preview. (ID:E2E-001)

### Test Data / Fixtures (SEC:TEST-DATA)
- Valid CSV, invalid schema CSV, large CSV. (ID:DATA-001)

### Observability / Rollback Testing (SEC:TEST-OBS)
- Verify metrics emitted on failure. (ID:OBS-001)
- Simulate rollback by disabling feature flag. (ID:OBS-002)

## L3 Implementation Notes (if needed) (SEC:TEST-L3)
- Use test S3 bucket with lifecycle cleanup. (ID:NOTE-001)

## Design Checklist (SEC:TEST-CHECK)
| Item | Pass/Fail | Notes | ID |
|---|---|---|---|
| Dependencies identified | Pass | Queue, S3 | CHECK-001 |
| Risks identified | Pass | Flaky jobs | CHECK-002 |
| Observability planned | Pass | Alerts | CHECK-003 |
| Rollout plan defined | Pass | Feature flag | CHECK-004 |
| Migration plan defined | Pass | N/A | CHECK-005 |
| Test scope defined | Pass | Full pipeline | CHECK-006 |

## Known Unknowns (SEC:TEST-UNK)
- Final CI test time budget. (ID:UNK-001)
