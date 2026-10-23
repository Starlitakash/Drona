# NexaTech Solutions - SRE & Enterprise Incident Management Runbook
**Document ID:** NT-SRE-SOP-015  
**Version:** 4.2  
**Effective Date:** February 1, 2026  
**Owner:** Site Reliability Engineering (SRE) & Incident Management Office  
**Classification:** Internal - Technical Operations  

---

## 1. Overview and Operational Principles
NexaTech Solutions ("NexaTech") maintains 99.99% service availability agreements for mission-critical client systems. Rapid, coordinated, and blameless incident management ensures operational disruptions are swiftly mitigated, root causes remediated, and stakeholder communications maintained transparently.

This runbook establishes severity definitions, on-call expectations, bridge protocols, escalation SLAs, and Root Cause Analysis (RCA) requirements.

---

## 2. Severity Classification and Response Matrix

Incidents are classified into four severity tiers based on business impact, data integrity, and customer degradation:

| Severity | Impact Definition | Initial Response SLA | Escalation Target | War Room Mandate |
|---|---|---|---|---|
| **SEV-1 (Critical Outage)** | Complete service unavailability affecting >25% of users; data loss or corruption; security breach; complete payment gateway failure. | **10 Minutes** | Executive Leadership, BU Head, CISO, Lead SRE | Mandatory 24/7 video bridge + Slack `#incident-sev1` |
| **SEV-2 (Major Degradation)** | Core customer journeys degraded; partial system failure with workaround; transaction processing latency >5x baseline. | **20 Minutes** | Service Owner, SRE Primary, Delivery Manager | Dedicated Slack `#incident-sev2` + Google Meet bridge |
| **SEV-3 (Moderate Issue)** | Minor feature malfunction; internal developer tooling failure; non-critical batch job delay. | **1 Hour** | Assigned Feature Squad On-Call | Handled within squad Slack channel |
| **SEV-4 (Low / Minor)** | Minor cosmetic defect; documentation discrepancy; non-impacting telemetry failure. | **4 Hours** | Next business day triage | Jira backlog item |

---

## 3. Incident Command System (ICS) Roles

During SEV-1 and SEV-2 incidents, clear operational roles prevent chaos:
1. **Incident Commander (IC):** Holds single-point operational authority over the incident. Directs troubleshooting, assigns investigation paths, enforces timeboxes, and authorizes failover actions. Does NOT write code or execute terminal commands directly.
2. **Operations Lead (SRE / Subject Matter Expert):** Executes technical diagnostics, logs, database queries, and deployment rollbacks. Reports findings directly to the IC.
3. **Communications Lead:** Manages internal executive briefings and external client notifications. Posts structured updates to the public status page (`status.nexatech.com`) and client Slack channels every 30 minutes during SEV-1 events.
4. **Scribe:** Documents real-time timeline, diagnostic findings, hypotheses, and configuration changes in the shared Google Docs incident scratchpad.

---

## 4. Immediate Incident Response Protocols

```
[Alarm Fires / PagerDuty Pages]
       │
       ▼ (10 Min SLA)
[SRE Acknowledges Page & Joins War Room]
       │
       ▼
[Designate Incident Commander (IC)]
       │
       ▼
[Assess Impact & Declare Severity]
       │
       ├─────────────────────────────────┐
       ▼ (If SEV-1)                      ▼ (If SEV-2)
[Open War Room Bridge + Slack]   [Open Triage Thread]
       │                                 │
       ▼                                 ▼
[Mitigate First: Rollback / Scale / Divert Traffic]
       │
       ▼
[Verify Recovery & Monitor Service Telemetry (30 Mins)]
       │
       ▼
[Declare All-Clear & Schedule Post-Mortem]
```

### 4.1 Mitigation First, RCA Later
The primary mandate during an active outage is **restoring service availability**, NOT debugging root cause. If an outage follows a deployment:
- Execute immediate deployment rollback via ArgoCD or Helm.
- Scale replica sets horizontally or reboot unresponsive pods.
- Divert traffic via Cloudflare / Route53 DNS health checks to secondary region.
- Collect thread dumps, heap dumps, and system logs before recycling containers.

---

## 5. On-Call Rotations and Compensation

- **Rotation Schedule:** SRE and platform engineering teams operate 7-day primary and secondary on-call rotations beginning Tuesdays at 10:00 AM IST.
- **On-Call Pager Allowance:** Engineers rostered as primary on-call receive an on-call readiness allowance of **₹12,000 INR per week**. Secondary on-call receives **₹6,000 INR per week**.
- **Incident Engagement Stipend:** If called after-hours (10:00 PM to 6:00 AM IST), engineers receive compensatory off (Comp-Off) of 1 day plus ₹2,500 INR incident allowance per night engaged.

---

## 6. Blameless Post-Mortem and Root Cause Analysis (RCA)

NexaTech strictly practices blameless post-mortems. System failures are results of flawed design, insufficient guardrails, or tooling gaps—not individual negligence.
- **Timeline:** A draft RCA must be published within **48 hours** of incident resolution for SEV-1 incidents, and **72 hours** for SEV-2 incidents.
- **RCA Structure (Confluence Template):**
  1. Executive Summary & Customer Impact (minutes of downtime, transactions lost).
  2. Detailed chronological event timeline (all times in IST and UTC).
  3. "5 Whys" root-cause derivation.
  4. What went well vs. what went wrong.
  5. Corrective and Preventive Actions (CAPA) with assigned Jira ticket owners and strict completion deadlines (within 30 days).
- **RCA Review Meeting:** Chaired by the Lead SRE every Tuesday at 3:00 PM IST.