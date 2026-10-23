# NexaTech Solutions - Enterprise Observability, Logging & Telemetry Standards
**Document ID:** NT-OPS-STD-060  
**Version:** 4.0  
**Effective Date:** February 1, 2026  
**Owner:** SRE Guild & Observability Center of Excellence  
**Classification:** Internal - Technical Staff  

---

## 1. The Three Pillars of Observability
NexaTech systems process millions of critical client transactions every day. Robust observability is vital for fast incident detection, proactive performance optimization, and SLA verification.

We build observability on the three open standards pillars: **Metrics**, **Structured Logs**, and **Distributed Traces**, unified via the OpenTelemetry (OTel) framework.

---

## 2. Structured JSON Logging Standards

All application logs must be emitted as structured single-line JSON to standard output (`stdout`):

```json
{
  "timestamp": "2026-02-15T10:45:12.304Z",
  "level": "INFO",
  "service": "payments-settlement-service",
  "environment": "production",
  "traceId": "4bf92f3577b34da6a3ce929d0e0e4736",
  "spanId": "00f067aa0ba902b7",
  "userId": "usr_99812",
  "message": "Payment transaction processed successfully",
  "http": {
    "method": "POST",
    "route": "/api/v1/payments",
    "status_code": 201,
    "duration_ms": 42.5
  }
}
```

### 2.1 Sensitive Data Masking (Zero-PII Logging Rule)
Application logs must NEVER contain:
- Passwords, API tokens, JWT secrets, or cryptographic keys.
- Credit card PANs, CVV codes, or bank account numbers.
- Aadhaar, SSN, or national identification credentials.
- Protected Health Information (PHI).
*Violations will result in automated SIEM alerts and immediate code revision tickets.*

---

## 3. Metrics Collection & Prometheus Standards
- Services must expose a `/metrics` endpoint formatted for Prometheus scraping.
- Standard Golden Signals must be instrumented for every microservice:
  1. **Latency:** Distribution of request service times (P50, P90, P99).
  2. **Traffic:** Demand placed on the service (Requests per second - RPS).
  3. **Errors:** Rate of failed requests (HTTP 5xx / application exceptions).
  4. **Saturation:** Resource utilization (CPU, memory, database connection pool exhaustion).

---

## 4. Distributed Tracing with OpenTelemetry
- Every inbound HTTP or Kafka event must initialize or propagate a W3C Trace Context header (`traceparent`).
- Spans must capture major database queries, external REST client calls, and cache interactions to enable sub-second latency bottleneck identification across microservices.

---

## Additional Operational Guidelines & Compliance

### Audit Trail & Regulatory Review
All requests, approvals, and dispute resolutions under this policy must be digitally recorded in NexaPortal with immutable audit logs retained for a minimum of 3 calendar years. Periodic internal audits are conducted bi-annually by the Internal Audit and Compliance Guild to verify adherence across all delivery centers.

### Exceptions and Variance Protocol
Any deviation from the standard limits or timelines specified in this document requires prior written concurrence from the Department Head and the Vice President of Operations. Retroactive exception approvals are strictly prohibited.

### Frequently Asked Questions (FAQ)
- **Q: Who do I contact if my ticket is delayed beyond the published SLA?**  
  *A:* Escalate to the department service lead via Slack on `#ops-escalations` or contact your assigned People Operations Business Partner (HRBP).
- **Q: How are policy updates communicated?**  
  *A:* Material revisions are announced during monthly all-hands meetings and updated in the official NexaTech Compliance Repository with change diffs documented.

### Contact Directory & Support Matrix
| Support Function | Primary Email Alias | Emergency Escalation |
|---|---|---|
| Department Service Desk | `servicedesk@nexatech.com` | Slack `#help-servicedesk` |
| Operations Compliance | `compliance@nexatech.com` | Level 2, HR Block |
| Employee Relations | `peopleops@nexatech.com` | Extension 4100 |
