# NexaTech Solutions - Role-Based Access Control (RBAC) & Privilege Governance Policy
**Document ID:** NT-SEC-POL-045  
**Version:** 3.4  
**Effective Date:** February 1, 2026  
**Owner:** Chief Information Security Officer (CISO) & Cloud Identity Guild  
**Classification:** Internal - Technical Operations  

---

## 1. Principles of Least Privilege & Need-to-Know
NexaTech enforces the **Principle of Least Privilege (PoLP)**. Every employee, system service, and API client is granted only the minimum technical access rights necessary to perform their immediate job duties.

Access permissions are bound strictly to assigned organizational roles rather than personal individuals.

---

## 2. Role-Based Access Control (RBAC) Hierarchy
- **Standard Contributor:** Access restricted to development and testing sandboxes, project Jira boards, and assigned GitHub repositories.
- **Module Lead / Senior SDE:** Read-only access to staging telemetry, merge permissions on protected branches with peer reviews, and ability to request temporary staging bastions.
- **CloudOps / SRE Lead:** Management access to production infrastructure via Just-In-Time (JIT) short-lived tokens.
- **Enterprise Administrator:** Restricted strictly to designated IT & Security directors; requires multi-party authorization for changes.

---

## 3. Just-In-Time (JIT) Temporary Privilege Elevation
Permanent administrative rights on production databases, AWS/Azure production subscriptions, or production Kubernetes clusters are strictly forbidden:
- Engineers requiring emergency break-glass production access must submit an elevation request via the Slack `#cloud-access-approvals` bot.
- The request requires real-time approval from both the Delivery Manager and On-Call SRE Lead.
- Elevated sessions are leased for a maximum of **4 hours**, after which tokens automatically expire and session logs are archived for security audit.

---

## 4. Quarterly User Access Reviews (UAR)
Every calendar quarter (March, June, September, December), the Cyber Defense Center conducts mandatory User Access Reviews across GitHub, AWS, Jira, and VPN directories:
- Delivery Managers must review and re-certify access lists for all direct reports within 10 business days.
- Any access permission not formally re-certified is automatically revoked by identity workflows.

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
