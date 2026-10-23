# NexaTech Solutions - Enterprise Service Level Agreement (SLA) & Availability Policy
**Document ID:** NT-OPS-POL-069  
**Version:** 3.4  
**Effective Date:** February 1, 2026  
**Owner:** Service Operations, Client Delivery Office & SRE  
**Classification:** Internal - Delivery Leadership  

---

## 1. Purpose and Contractual Commitments
NexaTech guarantees robust availability, latency thresholds, and incident resolution times for managed cloud environments and mission-critical applications. This policy establishes standardized enterprise SLAs and service credit calculations.

---

## 2. Uptime Commitment Tiers & Exclusions

| SLA Commitment Level | Maximum Permissible Unscheduled Monthly Downtime | Target Availability | Service Credit Trigger |
|---|---|---|---|
| **Tier 1 (Mission-Critical / Financial)** | **43.8 Minutes per month** | **99.9% Availability** | Downtime > 45 mins: 10% credit; > 2 hrs: 25% credit |
| **Tier 2 (Business-Critical)** | **3.65 Hours per month** | **99.5% Availability** | Downtime > 4 hrs: 10% credit |
| **Tier 3 (Standard Corporate)** | **7.3 Hours per month** | **99.0% Availability** | Downtime > 8 hrs: 5% credit |

### 2.1 SLA Exclusions
Unavailability resulting from the following is contractually excluded from uptime calculations:
- Pre-scheduled emergency maintenance notified at least 48 hours in advance.
- Client-caused infrastructure faults, unapproved DNS alterations, or third-party cloud provider outages (e.g., AWS global region disruption).
- Force majeure events (earthquakes, war, national telecom cable severance).

---

## 3. Incident Notification and RCA Delivery SLAs
- **Outage Notification:** Client technical leads must be notified via automated incident webhooks and SMS within **15 minutes** of declaring a SEV-1 incident.
- **Root Cause Analysis (RCA):** A formal, signed Post-Mortem RCA document must be delivered to the client within **72 business hours** of incident resolution.

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
