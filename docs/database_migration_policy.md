# NexaTech Solutions - Database Schema Evolution & Zero-Downtime Migration Policy
**Document ID:** NT-DAT-POL-059  
**Version:** 3.2  
**Effective Date:** February 1, 2026  
**Owner:** Database Administration (DBA) & Platform Engineering  
**Classification:** Internal - Technical Staff  

---

## 1. Purpose and Reliability Mandate
Database schema migrations represent significant operational risk. Uncoordinated table locks or destructive column drops can cause cascading application outages. This policy mandates zero-downtime database schema evolution across all relational (PostgreSQL, MySQL) and NoSQL (MongoDB, DynamoDB) systems.

---

## 2. Schema Evolution Tooling & Version Control
- All database mutations must be defined as versioned code using approved migration frameworks: **Flyway**, **Liquibase**, or **Alembic** (for Python services).
- Migration scripts must be version-controlled in the application repository under `/migrations/` and executed automatically during CI/CD deployment phases.
- Manual execution of DDL statements (`CREATE`, `ALTER`, `DROP`) directly against production databases is strictly prohibited.

---

## 3. The Expand-and-Contract Migration Pattern
All breaking schema migrations must follow the multi-phase **Expand-and-Contract (Parallel Run) Pattern**:
1. **Phase 1 (Expand):** Add the new column/table alongside the old column. Application code writes to both old and new columns, reading from the old.
2. **Phase 2 (Backfill):** Asynchronous background batch jobs populate historical data from old column to new column.
3. **Phase 3 (Switch):** Deploy updated application reading and writing exclusively from the new column.
4. **Phase 4 (Contract):** After verifying stability for at least one full sprint, drop the obsolete old column via a dedicated migration script.

---

## 4. Guardrails for Production Relational Migrations
- **Table Lock Avoidance:** In PostgreSQL, adding an index must always specify `CONCURRENTLY`. Modifying default values or adding constraints must be done without table rewrite locks.
- **Pre-Migration Backups:** Automated snapshot backups must be verified immediately prior to executing any DDL script on production databases.
- **Rollback Script Mandate:** Every migration script `V{N}__description.sql` must have a corresponding, fully tested rollback script `U{N}__undo_description.sql`.

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
