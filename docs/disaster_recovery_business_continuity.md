# NexaTech Solutions - Disaster Recovery (DR) & Business Continuity Plan (BCP)
**Document ID:** NT-OPS-POL-050  
**Version:** 4.0  
**Effective Date:** February 1, 2026  
**Owner:** SRE Guild, Cloud Infrastructure & Enterprise Risk  
**Classification:** Confidential - Technical Operations  

---

## 1. Overview and Enterprise Resilience
NexaTech Solutions ("NexaTech") maintains enterprise business continuity plans to ensure vital business operations, software delivery pipelines, and client production systems recover seamlessly from natural disasters, civic unrest, cyber attacks, or primary data center outages.

---

## 2. Recovery Objectives (RTO & RPO)

Systems are classified into three operational resilience tiers:

| Tier | System Classification | Recovery Point Objective (RPO) | Recovery Time Objective (RTO) |
|---|---|---|---|
| **Tier 1 (Mission-Critical)** | Client production transactional databases, payment gateways, active authentication directories. | **< 15 Minutes** | **< 1 Hour** |
| **Tier 2 (Core Business)** | Production CI/CD pipelines, internal Git repositories, customer support ticketing desks. | **< 1 Hour** | **< 4 Hours** |
| **Tier 3 (Operational Support)** | Corporate intranet wikis, LMS portals, historical analytics archives. | **< 24 Hours** | **< 24 Hours** |

---

## 3. Multi-Region Cloud Replication Architecture
- **AWS Primary / Secondary Topology:** Workloads deployed in AWS primary region (e.g., `ap-south-1` Mumbai) maintain continuous asynchronous database cross-region replication to secondary region (`ap-southeast-1` Singapore).
- **Automated DNS Failover:** Amazon Route 53 latency-based routing paired with health checks automates traffic redirection to hot-standby clusters during regional disruptions.
- **Immutable Backups:** Database snapshots and critical S3 storage buckets enforce WORM (Write Once, Read Many) Object Lock protection against ransomware alteration.

---

## 4. Bi-Annual DR Simulation Drills
- The SRE Guild conducts full-scale disaster recovery simulation drills **twice per year** (May and November).
- The exercise tests complete database failover, DNS traffic shifting, and team failover between delivery centers (e.g., Bengaluru engineering handing over support to Hyderabad teams).
- Drill post-mortems and verified recovery times are submitted to the Board Audit Committee.

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
