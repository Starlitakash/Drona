# ACME CORP ENGINEERING & INCIDENT RUNBOOK

## 1. Incident Severity Definitions
- **SEV-1 (Critical Outage):** Production outage affecting >25% of active users, data loss risk, or payment processing failure. PagerDuty escalates to the Primary On-Call Engineer and Engineering Director within 5 minutes.
- **SEV-2 (Major Degradation):** Core functionality degraded (e.g., search slow, notification delays), no data loss. Response time SLA is 30 minutes.
- **SEV-3 (Minor Bug):** Non-critical bug, cosmetic issue, or internal tool failure. Tracked in Jira under project "ENG" during normal business hours.

## 2. Database Connection Pool Exhaustion (Error Code: PG-ERR-53300)
**Symptoms:** API returns HTTP 500/504 errors. CloudWatch logs show "FATAL: remaining connection slots are reserved for non-replication superuser connections".
**Immediate Action Steps:**
1. Check active connections via PgBouncer: `SHOW POOLS;`
2. Identify long-running idle transactions: `SELECT pid, now() - query_start AS duration, query FROM pg_stat_activity WHERE state != 'idle' ORDER BY duration DESC LIMIT 5;`
3. Terminate stuck query safely: `SELECT pg_terminate_backend(<pid>);`
4. If connections do not drain within 3 minutes, restart the read-replica pods: `kubectl rollout restart deployment/read-replica -n prod`

## 3. Production Deployment & Rollback Procedures
- All deployments are managed through GitHub Actions and Kubernetes.
- Merging to `main` triggers a canary deployment (10% traffic for 15 minutes).
- **Rollback Procedure:** If error rates exceed 1% on Datadog, trigger an emergency rollback immediately:
  `kubectl rollout undo deployment/api-gateway -n prod`
- Post-incident, a post-mortem document must be filed in Confluence within 48 hours for all SEV-1 and SEV-2 incidents.