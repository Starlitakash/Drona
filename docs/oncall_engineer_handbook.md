# NexaTech Solutions - SRE & Platform Engineer On-Call Operational Handbook
**Document ID:** NT-SRE-HDB-062  
**Version:** 3.4  
**Effective Date:** February 1, 2026  
**Owner:** SRE Guild & Production Operations Committee  
**Classification:** Internal - Technical Staff  

---

## 1. On-Call Philosophy: Sustainable Operations
Being on-call at NexaTech is a shared professional responsibility across engineering squads to ensure high system reliability and customer trust. We design our on-call rotations to be humane, sustainable, psychologically safe, and financially compensated.

---

## 2. On-Call Rotations, Rosters & PagerDuty Setup
- **Rotation Structure:** 7-day rotational shifts running from **Tuesday 10:00 AM IST to the following Tuesday 10:00 AM IST**.
- **Two-Tier Coverage:**
  - *Primary On-Call:* First responder for all automated alerts; responsible for triage within 15 minutes.
  - *Secondary (Backup) On-Call:* Escalation contact if Primary fails to acknowledge alert within 15 minutes or during complex SEV-1 incidents.
- **Tooling Configuration:** PagerDuty app must be installed on your mobile phone with "Critical Alerts" permission enabled (allowing audible alarms even in "Do Not Disturb" mode).

---

## 3. On-Call Compensation & Fatigue Management

| On-Call Duty Role | Weekly Readiness Allowance (INR) | Additional Per-Incident Night Payout (10 PM - 6 AM) |
|---|---|---|
| **Primary On-Call Engineer** | **₹12,000 INR** per week | ₹2,500 INR per night engaged |
| **Secondary On-Call Engineer** | **₹6,000 INR** per week | ₹2,500 INR per night engaged (if escalated) |

### 3.1 Sleep Deprivation & Fatigue Recovery
If an on-call engineer is engaged in troubleshooting high-severity incidents between midnight and 6:00 AM IST:
- The engineer is granted mandatory **Fatigue Recovery Time-Off**: They are excused from morning sprint meetings and expected to begin work after 2:00 PM IST or take the following day as Compensatory Off.
- The Secondary On-Call automatically steps up as acting Primary during the rest window.

---

## 4. Alert Triage Playbook
When an alert triggers in PagerDuty:
1. **Acknowledge (Within 10 Minutes):** Tap Acknowledge to prevent escalation to Secondary.
2. **Review Runbook:** Click the runbook link attached to the PagerDuty alarm (e.g., `runbooks.nexatech.internal/pg-pool-exhaustion`).
3. **Assess Blast Radius:** Verify if users are actively experiencing errors on Grafana dashboards.
4. **Escalate Early:** If unable to isolate the issue within 20 minutes, page the Secondary and notify the Practice Delivery Manager.

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
