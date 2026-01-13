# ADR 0001: Use S3 for Raw Upload Storage (DOC:ADR-100)

## Context (SEC:ADR-CTX)
- CSV uploads can be large and should not block the API server. (ID:CTX-001)

## Decision (SEC:ADR-DEC)
- Store raw uploads in S3 and process asynchronously via worker jobs. (ID:DEC-001)

## Consequences (SEC:ADR-CONS)
- Requires S3 credentials and lifecycle rules for cleanup. (ID:CONS-001)
