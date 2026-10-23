import os
from pathlib import Path

DOCS_DIR = Path("docs")
DOCS_DIR.mkdir(parents=True, exist_ok=True)

docs_batch7 = {}

# 61. security_incident_classification.md (MEDIUM ~5,200 chars)
docs_batch7["security_incident_classification.md"] = """# NexaTech Solutions - Cyber Security Incident Classification & Containment Guide
**Document ID:** NT-SEC-GDE-061  
**Version:** 4.1  
**Effective Date:** February 1, 2026  
**Owner:** Cyber Defense Center (CDC) & Incident Handling Team  
**Classification:** Confidential - Technical Security  

---

## 1. Purpose and Operational Philosophy
NexaTech Solutions operates a 24/7/365 Cyber Defense Center (CDC). Prompt, standardized incident classification ensures appropriate technical resources, forensic specialists, executive notification chains, and statutory regulatory authorities are engaged without delay.

This guide defines incident severity tiers, containment runbooks, and statutory reporting obligations adhering to NIST SP 800-61 Rev. 2 and Indian Computer Emergency Response Team (CERT-In) guidelines.

---

## 2. Cyber Incident Severity Classification Matrix

| Incident Severity | Operational Definition & Criteria | CDC Initial Response SLA | Mandatory Notification Window | Escalation Authorities |
|---|---|---|---|---|
| **SEV-1 (Critical)** | Active ransomware encryption; exfiltration of customer PII / financial records; root compromise of AWS production master organization; uncontained malware worm spreading across corporate LAN. | **15 Minutes** | **1 Hour Internal / 6 Hours Regulatory** | CISO, CEO, Legal Counsel, Affected Client CISOs, CERT-In |
| **SEV-2 (High)** | Compromise of privileged employee account; malware detected on server endpoint; isolated DDoS attack causing customer degradation; unauthorized production database read query. | **30 Minutes** | **4 Hours** | CISO, Practice Delivery Head, CDC Lead |
| **SEV-3 (Medium)** | Credential phishing campaign targeting multiple staff; multiple failed brute-force attacks; unauthorized software installation on laptop. | **2 Hours** | **12 Hours** | Senior Security Analyst, IT Helpdesk Lead |
| **SEV-4 (Low)** | Isolated spam email report; port scanning from internet without breach; minor security false-positive alert. | **8 Hours** | Next Business Day | Level 1 Security Operations Analyst |

---

## 3. Statutory Regulatory Reporting (CERT-In Mandate)
In compliance with the CERT-In Directions under Section 70B of the Information Technology Act:
- **Mandatory 6-Hour Reporting:** Any cyber incident involving unauthorized access of IT systems, ransomware, identity theft, or data exfiltration must be formally reported to CERT-In (`incident@cert-in.org.in`) within **6 hours** of confirmation.
- The CISO and Legal Counsel coordinate all regulatory filings; individual employees are strictly prohibited from submitting external filings independently.

---

## 4. Immediate Containment & Forensic Runbooks
During an active security breach, investigators must preserve digital evidence for court admissibility:
1. **Endpoint Isolation:** Isolate compromised laptops or virtual machines from the network via CrowdStrike Falcon Sensor Network Containment. Do NOT power off or reboot the machine (preserves volatile RAM).
2. **Volatile Memory Capture:** Capture RAM dumps using approved forensic tools (WinPmem or LiME) before disk imaging.
3. **Credential Invalidation:** Revoke all active Okta sessions, invalidate AWS STS temporary credentials, and force password resets via Active Directory.
4. **Forensic Chain of Custody:** Document every forensic artifact with SHA-256 cryptographic hashes and maintain signed custody transfer forms.
"""

# 62. oncall_engineer_handbook.md (MEDIUM ~5,100 chars)
docs_batch7["oncall_engineer_handbook.md"] = """# NexaTech Solutions - SRE & Platform Engineer On-Call Operational Handbook
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
"""

# 63. testing_and_qa_standards.md (MEDIUM ~5,000 chars)
docs_batch7["testing_and_qa_standards.md"] = """# NexaTech Solutions - Automated Testing Strategy & Code Quality Standards
**Document ID:** NT-ENG-STD-063  
**Version:** 4.0  
**Effective Date:** February 1, 2026  
**Owner:** Quality Engineering Guild & Software Craftsmanship CoE  
**Classification:** Internal - Engineering Staff  

---

## 1. Principles of Testing at NexaTech
Software testing is a core engineering practice aimed at building confidence in continuous delivery. We follow the principle of fast feedback loops: catching defects as close as possible to the developer's local environment through automated test harnesses.

---

## 2. Test Execution Pyramid & Quality Gates

```
       /\
      /  \      E2E Tests (10%) - Playwright, Cypress (Critical flows)
     /----\
    /      \    Integration Tests (20%) - Testcontainers, Postman
   /--------\
  /          \  Unit Tests (70%) - JUnit 5, PyTest, Jest (Fast, in-memory)
 /------------\
```

### 2.1 Unit Testing Standards
- Unit tests must be fast, isolated, and deterministic. No external network or live database calls are permitted in unit test suites.
- **Coverage Mandate:** All pull requests must maintain or increase overall code coverage. SonarQube enforces a strict **80% minimum line coverage threshold** on new code.
- Mocking: Use modern mocking libraries (Mockito, unittest.mock, Vitest). Avoid over-mocking business domain logic.

### 2.2 Integration Testing with Testcontainers
- Real database and message broker interactions must be tested against lightweight, ephemeral Docker containers using **Testcontainers**.
- Tests must validate transaction rollbacks, schema migrations, and cache invalidation behaviors under realistic simulated loads.

---

## 3. Performance & Stress Testing Benchmarks
Before promoting any major service release to Production:
- Execute distributed load tests using **k6** simulating **2x anticipated peak traffic** for 30 minutes.
- **Pass Criteria:** P99 response latency must remain under 250ms with zero HTTP 5xx errors.

---

## 4. Flaky Test Mitigation Policy
Flaky tests destroy developer confidence:
- Any automated test failing intermittently (>2% false-failure rate) is tagged with `@Flaky` and isolated to a quarantine suite.
- The authoring squad must remediate the quarantined test within **5 business days** or permanently remove it.
"""

# 64. ai_tooling_copilot_usage_policy.md (MEDIUM ~5,200 chars)
docs_batch7["ai_tooling_copilot_usage_policy.md"] = """# NexaTech Solutions - Generative AI, LLM Tooling & GitHub Copilot Usage Policy
**Document ID:** NT-ENG-POL-064  
**Version:** 3.2  
**Effective Date:** February 1, 2026  
**Owner:** Office of the CTO, CISO & Legal Compliance  
**Classification:** Internal - Technical Staff  

---

## 1. Context and Objective
Generative AI and Large Language Model (LLM) developer tools dramatically accelerate engineering productivity, code synthesis, documentation authoring, and test generation. However, unvetted AI tools pose critical risks including proprietary code leakage, intellectual property infringement, and hallucinated security vulnerabilities.

This policy establishes binding guardrails for the use of AI development assistants at NexaTech.

---

## 2. Approved Enterprise AI Toolchains
Engineers may utilize exclusively the following enterprise-licensed AI tools:
- **GitHub Copilot Enterprise:** Pre-configured with organizational data boundary protection.
- **NexaTech Internal LLM Gateway (NexaBrain):** Internal proxy providing access to hosted open models (Llama 3, Mistral) with zero-data-retention guarantees.
- **JetBrains AI Assistant Enterprise:** Licensed via corporate JetBrains bundle.

---

## 3. Strict Prohibitions & Data Protection Rules
- **Public Consumer AI Tools:** Employees are strictly prohibited from pasting NexaTech source code, client architecture diagrams, or customer datasets into free or public consumer AI platforms (e.g., public ChatGPT, Claude consumer tiers, unapproved browser AI extensions).
- **Zero Secrets / PII Input:** Prompts must never contain database passwords, API secret keys, personal names, phone numbers, or client proprietary algorithmic formulas.
- **Client Contractual Restrictions:** If a client Master Services Agreement (MSA) explicitly prohibits AI-assisted code generation (common in defense, aerospace, and banking engagements), the assigned engineering squad must disable all Copilot plugins on project repositories.

---

## 4. Code Verification and Human Accountability
- **Human-in-the-Loop:** AI tools are assistants, not software authors. The engineer committing code bears 100% professional and legal accountability for all logic, security posture, and bugs generated by AI.
- **Public Code Match Filter:** All GitHub Copilot Enterprise seats must keep the *Block suggestions matching public code* filter permanently enabled to mitigate copyright and copyleft GPL licensing contamination risks.
- **Security Scrutiny:** AI-generated code must undergo standard peer reviews, SonarQube static analysis, and Snyk vulnerability checks prior to merging.
"""

# 65. client_nda_msa_guidelines.md (MEDIUM ~5,100 chars)
docs_batch7["client_nda_msa_guidelines.md"] = """# NexaTech Solutions - Master Services Agreement (MSA) & Commercial Legal Guidelines
**Document ID:** NT-LGL-GDE-065  
**Version:** 4.0  
**Effective Date:** January 1, 2026  
**Owner:** Legal Department, Commercial Contracts & Risk Committee  
**Classification:** Confidential - Sales & Delivery Management  

---

## 1. Purpose and Commercial Risk Framework
Master Services Agreements (MSAs) and Statements of Work (SOWs) define the legal and financial terms under which NexaTech provides engineering services to enterprise clients. Unfavorable contractual terms can expose NexaTech to unlimited liability, intellectual property forfeiture, and margin erosion.

This playbook provides standard positions, fallback positions, and non-negotiable clauses for commercial contract negotiations.

---

## 2. Key Contractual Clauses and Standard Positions

### 2.1 Limitation of Liability (LoL)
- **Standard Position:** Total aggregate liability under the MSA must be capped at **12 months of fees paid or payable** under the applicable SOW.
- **Fallback Position:** Absolute cap at **2x annual SOW fees** for gross negligence or willful misconduct.
- **Non-Negotiable:** Under no circumstances will NexaTech agree to *unlimited liability* for general breach of contract.

### 2.2 Intellectual Property (IP) Rights
- **Deliverables IP:** Client owns specific custom software deliverables created specifically for them, contingent upon full receipt of contractual fees.
- **NexaTech Background IP:** NexaTech retains perpetual ownership of all pre-existing frameworks, accelerators, reusable libraries, and proprietary architectures developed prior to or independently of the client engagement. Client is granted a non-exclusive, perpetual, royalty-free license to use Background IP integrated into deliverables.

### 2.3 Warranty & Acceptance Testing
- **Warranty Period:** Standard warranty for defect remediation is **30 to 60 calendar days** following formal client user acceptance testing (UAT).
- **Implied Acceptance:** Deliverables are deemed accepted if the client does not provide written, itemized defect notices within **10 business days** of milestone submission.

---

## 3. Non-Solicitation Covenants
All client MSAs must incorporate a bilateral non-solicitation clause prohibiting either party from soliciting, hiring, or contracting employees of the other party during the engagement and for **12 months** following contract termination. In the event of a breach, liquidated damages equal to 100% of the solicited employee's annual CTC must be paid.
"""

# 66. sales_commission_plan.md (MEDIUM ~5,000 chars)
docs_batch7["sales_commission_plan.md"] = """# NexaTech Solutions - Global Sales Incentive & Commission Compensation Plan
**Document ID:** NT-SLS-POL-066  
**Version:** 3.3  
**Effective Date:** April 1, 2026  
**Owner:** Revenue Operations, Finance & Total Rewards  
**Classification:** Confidential - Sales Organization  

---

## 1. Plan Purpose and Philosophy
The NexaTech Sales Incentive Plan aligns individual sales rewards with profitable revenue growth, long-term enterprise client expansion, and healthy gross margin realization.

---

## 2. Quota Attainment & Commission Tier Structure

Commission rates are calculated on **Recognized Billed Revenue** and gross margin thresholds:

| Quota Attainment Tier | Percentage of Annual Target Achieved | Standard Commission Rate | Gross Margin Bonus (>38% GM) |
|---|---|---|---|
| **Tier 1 (Base Band)** | 0% – 79.9% of Quota | **2.5% of Revenue** | Standard Rate |
| **Tier 2 (Target Band)** | 80% – 100% of Quota | **4.5% of Revenue** | +0.5% Booster |
| **Tier 3 (Accelerator 1)** | 100.1% – 125% of Quota | **7.0% of Revenue** | +1.0% Booster |
| **Tier 4 (President's Club)** | > 125% of Quota | **9.5% of Revenue** | +1.5% Booster |

---

## 3. Commission Payout Schedule & Revenue Recognition
- **Quarterly Cycle:** Commissions are evaluated and paid quarterly (in May, August, November, and February payroll cycles).
- **Payment Trigger:** Commissions are released only after:
  1. The client executes the legal SOW and milestone acceptance certificate.
  2. The invoice is formally billed and paid by the client (collected cash basis).
- **Clawbacks:** If a client cancels a contract for convenience or fails to pay invoices (bad debt default) within 90 days, previously disbursed commissions for unpaid invoices are clawed back from future commission cycles.

---

## 4. President's Club Recognition
Account Executives who achieve **>120% of their annual revenue quota** qualify for the prestigious *NexaTech President's Club*, which includes an all-expenses-paid 5-day international luxury retreat with an executive guest and formal recognition by the Board of Directors.
"""

# 67. project_allocation_bench_policy.md (MEDIUM ~4,800 chars)
docs_batch7["project_allocation_bench_policy.md"] = """# NexaTech Solutions - Project Allocation, Bench Governance & Talent Mobility Policy
**Document ID:** NT-OPS-POL-067  
**Version:** 3.2  
**Effective Date:** February 1, 2026  
**Owner:** Resource Management Group (RMG) & Workforce Planning  
**Classification:** Internal - All Employees  

---

## 1. Overview and Talent Redeployment
As a digital engineering services organization, engineers occasionally transition between completed client engagements and upcoming transformation initiatives. The period between billable project engagements is designated as the **Upskilling & Deployment Window (Bench)**.

This policy establishes guidelines for talent readiness, internal interviews, skill enhancement, and deployment timelines.

---

## 2. Roles and Expectations During Bench Tenure
Being on the bench is an active, structured working phase—not paid leave:
- **Daily Hours & Attendance:** Engineers must adhere to standard working hours (09:30 AM to 06:30 PM IST), mark daily check-ins on NexaPortal, and report to their base delivery center on in-office days.
- **Mandatory Upskilling Track:** Within 48 hours of rolling off a project, the engineer, in collaboration with their Practice Lead, creates an *Upskilling Learning Path* in NexaLearn (e.g., AWS Solutions Architect, Kubernetes CKA, LangChain GenAI).
- **Internal Hackathons & Proof-of-Concepts (PoCs):** Bench engineers contribute to internal accelerators, client RFP technical prototypes, and open-source tooling.

---

## 3. Bench Tenure Limits & Career Interventions
NexaTech tracks bench tenure carefully through RMG:
- **Days 1 – 30:** Active internal client shadowing, certification completion, and interview matching with new project accounts.
- **Days 31 – 60:** Expanded matching across cross-functional practices (e.g., Java engineer cross-training to Python Data/AI).
- **Beyond 60 Days:** If an engineer remains unallocated past 60 days despite multiple client opportunities, RMG and HRBP conduct a formal competency review.
- **Unreasonable Rejections:** If an engineer rejects two verified project allocations matching their skillset without documented valid cause, it is considered refusal of work, triggering a performance review.
"""

# 68. customer_data_privacy_gdpr.md (MEDIUM ~5,200 chars)
docs_batch7["customer_data_privacy_gdpr.md"] = """# NexaTech Solutions - Customer Data Privacy, GDPR & DPDP Act Compliance Policy
**Document ID:** NT-LGL-POL-068  
**Version:** 4.2  
**Effective Date:** January 15, 2026  
**Owner:** Data Protection Officer (DPO) & Legal Compliance  
**Classification:** Internal - All Personnel  

---

## 1. Privacy Principles and Regulatory Landscape
NexaTech processes personally identifiable information (PII) of global users on behalf of our enterprise clients. We adhere to the highest global data privacy standards, including the EU General Data Protection Regulation (GDPR), the California Consumer Privacy Act (CCPA/CPRA), and the Indian Digital Personal Data Protection (DPDP) Act, 2023.

---

## 2. Core Privacy Principles
- **Lawfulness, Fairness & Transparency:** Personal data must be processed lawfully and with the explicit consent of data principals.
- **Purpose Limitation:** Data collected for one business purpose (e.g., flight booking) cannot be repurposed for secondary reasons (e.g., marketing profiling).
- **Data Minimization:** Software architectures must collect only the minimum personal data strictly necessary for transaction processing.
- **Storage Limitation:** Personal data must not be stored longer than necessary to satisfy stated business purposes.

---

## 3. Data Subject Access Requests (DSAR) Management
Under GDPR and DPDP regulations, individuals have legal rights regarding their personal data:
- **Right to Access & Portability:** Requesting copies of held personal data.
- **Right to Rectification:** Correcting inaccurate data.
- **Right to Erasure (Right to be Forgotten):** Requesting permanent deletion of data.
- **DSAR Fulfillment SLA:** All DSAR requests received at `privacy@nexatech.com` must be acknowledged within **48 hours** and fulfilled within **30 calendar days**.

---

## 4. Cross-Border Data Transfers & Privacy Impact Assessments (PIA)
- Transferring personal data outside its origin economic area requires approved legal transfer mechanisms (Standard Contractual Clauses - SCCs).
- Any new enterprise engineering project introducing automated profiling, AI decision systems, or large-scale PII ingestion must undergo a formal **Privacy Impact Assessment (PIA)** signed off by the Data Protection Officer (`dpo@nexatech.com`) prior to production deployment.
"""

# 69. service_level_agreements_sla.md (MEDIUM ~4,900 chars)
docs_batch7["service_level_agreements_sla.md"] = """# NexaTech Solutions - Enterprise Service Level Agreement (SLA) & Availability Policy
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
"""

# 70. client_gift_and_hospitality.md (MEDIUM ~4,700 chars)
docs_batch7["client_gift_and_hospitality.md"] = """# NexaTech Solutions - Corporate Gifting, Hospitality & Seasonal Courtesies Policy
**Document ID:** NT-LGL-POL-070  
**Version:** 3.1  
**Effective Date:** January 1, 2026  
**Owner:** Corporate Ethics, Legal Compliance & Marketing  
**Classification:** Internal - All Employees  

---

## 1. Purpose and Anti-Corruption Stance
Exchanging modest corporate courtesies during festive seasons (Diwali, New Year) or following milestone deliveries is a recognized business tradition. However, gifts must never be used to improperly influence commercial decisions, compromise professional objectivity, or circumvent anti-corruption statutes.

---

## 2. Outbound Corporate Gifting Limits (To Clients & Partners)
- **Festive Gift Boxes:** Corporate gift boxes (sweets, dry fruits, branded merchandise) sent during major holidays must be ordered through the Central Marketing Desk (`marketing@nexatech.com`).
- **Monetary Ceiling:** Individual client gifts must not exceed **₹2,500 INR** ($35 USD) per recipient.
- **Prohibited Gifts:** Cash, gold/silver bullion coins, luxury watches, stock shares, and personal travel vouchers are strictly forbidden.
- **Public Officials Ban:** Gifting to government officials or public sector employees of any jurisdiction is strictly capped at **₹500 INR** for modest informational materials (pens/notepads); giving festive gift hampers to government servants is prohibited.

---

## 3. Inbound Gifts Received from Vendors or Clients
- **Gifts Under ₹2,000 INR:** Modest promotional items (diaries, desktop calendars, coffee mugs) may be retained by the employee.
- **Gifts Exceeding ₹2,000 INR:** Must be declared to the Ethics & Compliance Register within 48 hours. The employee must surrender the gift to People Operations for the annual employee raffle or charitable donation.
- **Perishable Hampers:** Large food baskets must be shared with the broader team floor or placed in communal cafeterias.
"""

for filename, content in docs_batch7.items():
    file_path = DOCS_DIR / filename
    file_path.write_text(content.strip(), encoding="utf-8")
    print(f"Written: {filename} ({len(content)} chars)")

print("Batch 7 Complete: 10 files written.")
