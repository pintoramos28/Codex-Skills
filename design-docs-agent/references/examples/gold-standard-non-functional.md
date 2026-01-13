# Non‑Functional Requirements — Example (Gold Standard) (DOC:NFR-100)

## L1 Summary (SEC:NFR-L1)
- Secure uploads, PII‑safe storage, and predictable performance. (ID:SUM-001)

## L2 Design Detail (SEC:NFR-L2)
### Security (SEC:NFR-SEC)
- AuthN/AuthZ: JWT required for all endpoints. (ID:SEC-001)
- PII handling: Encrypt data at rest; access logged. (ID:SEC-002)

### Compliance (SEC:NFR-COMP)
- SOC2: Audit logging for data access. (ID:COMP-001)
- GDPR: Support deletion requests. (ID:COMP-002)

### Performance & Scalability (SEC:NFR-PERF)
- Latency budget: <300ms for preview requests. (ID:PERF-001)
- Throughput: 100 concurrent uploads. (ID:PERF-002)

### Cost (SEC:NFR-COST)
- Cost ceiling: $500/month for storage + compute. (ID:COST-001)

## L3 Implementation Notes (if needed) (SEC:NFR-L3)
- Use S3 lifecycle rules to prune raw uploads after 30 days. (ID:NOTE-001)

## Design Checklist (SEC:NFR-CHECK)
| Item | Pass/Fail | Notes | ID |
|---|---|---|---|
| Dependencies identified | Pass | S3, Postgres | CHECK-001 |
| Risks identified | Pass | PII exposure | CHECK-002 |
| Observability planned | Pass | Access logs | CHECK-003 |
| Rollout plan defined | Pass | Feature flag | CHECK-004 |
| Migration plan defined | Pass | N/A | CHECK-005 |
| Test scope defined | Pass | Security tests | CHECK-006 |

## Known Unknowns (SEC:NFR-UNK)
- Final compliance requirements. (ID:UNK-001)
