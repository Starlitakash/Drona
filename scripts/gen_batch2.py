import os
from pathlib import Path

DOCS_DIR = Path("docs")
DOCS_DIR.mkdir(parents=True, exist_ok=True)

docs_batch2 = {}

# 11. onboarding_sde.md (LONG ~12,500 chars)
docs_batch2["onboarding_sde.md"] = """# NexaTech Solutions - Software Development Engineer (SDE) Onboarding & Technical Ramp-Up Guide
**Document ID:** NT-ENG-GDE-011  
**Version:** 4.2  
**Effective Date:** February 1, 2026  
**Owner:** Engineering Excellence & Developer Experience Guild  
**Classification:** Internal - Technical Staff  

---

## 1. Welcome to NexaTech Engineering
Congratulations on joining the NexaTech Solutions Engineering team! Our engineering organization comprises over 900 software engineers, distributed systems architects, cloud specialists, and QA automation professionals building high-resilience systems for global Fortune 500 enterprises.

This guide provides a structured technical blueprint for your first 90 days, covering hardware provisioning, local development environments, architectural standards, code review protocols, CI/CD pipelines, and key milestones.

---

## 2. Hardware and Standard Developer Tooling

### 2.1 Hardware Provisioning Baseline
All software engineers are issued standardized high-performance hardware configured by IT Services on Day 1:
- **Default SDE Hardware Tier:** Apple MacBook Pro 16-inch (Apple Silicon M3 Pro, 36GB Unified Memory, 1TB NVMe SSD) OR Dell XPS 15 (Intel Core i7 14th Gen, 32GB DDR5 RAM, 1TB NVMe SSD, Ubuntu LTS 24.04 or Windows 11 Enterprise).
- **Peripherals Issued:** Dual 27-inch 4K Dell UltraSharp monitors (issued at base office desks), NexaTech-branded USB-C multiport docking station, and Jabra Evolve 65 noise-canceling headset.
- **Home Setup Support:** Confirmed engineers can claim up to ₹15,000 INR under the Ergonomic Workstation Reimbursement Policy.

### 2.2 Standard Developer Tooling & Licenses
Your Okta SSO account provides automated license provisioning for the following toolchains:
- **Version Control & Collaboration:** GitHub Enterprise (`github.com/nexatech-solutions`), Jira Software Cloud, Confluence, Slack Enterprise Grid.
- **IDEs & Productivity:** JetBrains All Products Pack (IntelliJ IDEA Ultimate, PyCharm Professional, GoLand, WebStorm) or Visual Studio Code Enterprise with GitHub Copilot Enterprise extension enabled.
- **API Development & Testing:** Postman Enterprise Workspace, Insomnia Pro.
- **Containers & Virtualization:** Docker Desktop Enterprise (licensed via NexaTech Business Agreement) or Rancher Desktop.
- **Static Analysis & Security:** SonarQube Enterprise, Snyk Developer CLI, GitGuardian secret scanning.

---

## 3. Account Provisioning and Security Clearance

### 3.1 Core Account Check-in Checklist
Complete the following access verifications on Day 1:
1. **Active Directory & Okta Single Sign-On:** Verify login at `https://nexatech.okta.com` using credentials received via SMS from IT Helpdesk.
2. **Multi-Factor Authentication (MFA):** Pair Okta Verify on your smartphone with Number Matching enabled. Hardware YubiKey enrollment can be completed at the IT Support Kiosk on Floor 3.
3. **GitHub Enterprise Organization:** Accept the automated email invitation to `github.com/orgs/nexatech-solutions`. Ensure your hardware SSH key is generated using `ed25519` algorithms and registered with GPG commit signing:
   ```bash
   ssh-keygen -t ed25519 -C "your.name@nexatech.com"
   git config --global user.signingkey <GPG-KEY-ID>
   git config --global commit.gpgsign true
   ```
4. **AWS Developer Sandbox Access:** Access the AWS IAM Identity Center portal (`https://nexatech.awsapps.com/start`) to obtain temporary CLI credentials for your assigned Practice sandbox account.

### 3.2 Required Compliance Modules (Day 1 - 3)
Before production codebase read access is granted, you must complete four mandatory training modules on the NexaLearn LMS:
- *Secure Coding & OWASP Top 10 (2026 Edition)* - 90 minutes.
- *Information Security & SOC 2 Developer Responsibilities* - 45 minutes.
- *Open Source Software & Licensing Governance* - 30 minutes.
- *Data Privacy & GDPR / DPDP Act Developer Essentials* - 45 minutes.

---

## 4. Git Workflows, Branching & Pull Request Standards

### 4.1 Git Branching Architecture
NexaTech enforces a trunk-based branching strategy with short-lived feature branches:
- **Main / Trunk Branch:** Always kept deployable and protected. Direct commits and force-pushes are disabled at the GitHub branch protection level.
- **Branch Naming Standard:**
  - Feature: `feat/NEXA-<JIRA-ID>-short-description` (e.g., `feat/NEXA-1240-user-profile-api`)
  - Bugfix: `fix/NEXA-<JIRA-ID>-short-description`
  - Hotfix: `hotfix/NEXA-<JIRA-ID>-short-description`
  - Refactoring: `refactor/NEXA-<JIRA-ID>-short-description`

### 4.2 Pull Request (PR) Requirements
Every Pull Request must satisfy the following strict gating criteria before merging:
1. **Mandatory Peer Reviews:** At least two approving reviews: one from a designated peer SDE and one from the Module Lead / Senior SDE.
2. **Automated CI Checks:**
   - GitHub Actions pipeline must pass 100% green.
   - Unit test code coverage must meet or exceed **80%** on new lines of code (enforced by SonarQube quality gates).
   - Zero critical or high vulnerabilities flagged by Snyk dependency analysis and GitGuardian secret scans.
3. **Conventional Commits:** Commit messages must follow the Conventional Commits specification:
   ```text
   feat(auth): implement token refresh rotation for oauth2 client
   
   Closes: NEXA-1240
   Signed-off-by: Your Name <your.name@nexatech.com>
   ```

---

## 5. Architecture Standards and Technology Stacks

NexaTech follows strict technology radar tiers: *Adopt*, *Trial*, *Assess*, and *Hold*:
- **Backend Languages & Frameworks:** Java 21 LTS (Spring Boot 3.x), Python 3.11+ (FastAPI), Go 1.22+, TypeScript / Node.js 20 LTS (NestJS).
- **Frontend & Mobile:** React 18+, Next.js 14+, TypeScript, Tailwind CSS, Flutter for cross-platform mobile.
- **Databases & Messaging:** PostgreSQL 16+ (AWS Aurora Serverless v2), MongoDB 7+, Redis Enterprise Cluster, Apache Kafka (Confluent Cloud), RabbitMQ.
- **Cloud & Orchestration:** Amazon Web Services (AWS), Microsoft Azure, Kubernetes (EKS / AKS), Terraform for Infrastructure as Code (IaC), ArgoCD for GitOps deployments.

---

## 6. SDE 30-60-90 Day Success Milestones

```
[Day 1-30: Foundation & First Commit]
  ├── Set up local IDE and security tooling
  ├── Complete mandatory LMS compliance certifications
  ├── Shadow sprint planning, daily standup, and grooming
  ├── Resolve 2 "good-first-issue" bug tickets in sprint
  └── Ship your first pull request to staging environment

[Day 31-60: Independence & Delivery]
  ├── Own an end-to-end user story from grooming to production release
  ├── Write automated integration tests and documentation in Confluence
  ├── Perform peer code reviews for teammates
  └── Participate in on-call shadowing rotation alongside senior SDE

[Day 61-90: Mastery & Production Readiness]
  ├── Drive technical design for a feature sub-module
  ├── Conduct an architecture review with the Technical Lead
  ├── Participate fully in primary/secondary on-call rotation
  └── Present a 30-minute tech talk at the Engineering Guild Lunch & Learn
```

---

## 7. Mentorship and Buddy Program
Every incoming engineer is assigned two dedicated support contacts:
- **Technical Mentor (Senior SDE / Lead):** Guides your architectural understanding, reviews complex PRs, and conducts weekly 45-minute technical 1-on-1s.
- **Onboarding Buddy (Peer SDE):** Your informal go-to guide for day-to-day questions: navigating office perks, local team norms, cafeteria timings, and Slack channels.

---

## 8. Key Engineering Slack Channels & Contacts

| Slack Channel | Purpose | Key Contact |
|---|---|---|
| `#eng-announcements` | Organization-wide technical updates & releases | VP of Engineering |
| `#dev-support` | Peer troubleshooting, toolchain issues, environment help | DevEx Guild Leads |
| `#cloud-access-approvals` | AWS/Azure IAM privilege elevation requests | CloudOps On-Call |
| `#github-admin` | Repository creation, CI runner issues, branch access | DevOps Admin Team |
| `#security-champions` | Application security guidance, threat modeling | Application Security Lead |
| `#guild-python` / `#guild-java` | Language-specific best practices and tech talks | Guild Moderators |
"""

# 12. performance_review_promotion.md (LONG ~12,500 chars)
docs_batch2["performance_review_promotion.md"] = """# NexaTech Solutions - Comprehensive Performance Management, Appraisal & Promotion Policy
**Document ID:** NT-HR-POL-012  
**Version:** 4.0  
**Effective Date:** January 1, 2026  
**Owner:** People Operations & Total Rewards Committee  
**Classification:** Internal - All Employees  

---

## 1. Philosophy and Framework: NexaGrowth
NexaTech Solutions ("NexaTech") believes high-performance cultures flourish when evaluation is transparent, continuous, objective, and deeply rooted in measurable outcomes. Our performance framework, **NexaGrowth**, combines Objectives and Key Results (OKRs), continuous feedback check-ins, and bi-annual calibrated evaluations.

This policy applies to all confirmed full-time employees across all delivery centers and functional bands.

---

## 2. Appraisal Cycles and Calendar

NexaTech operates on a two-cycle evaluation model per financial year:
```
  [April 1 - 15]        [July 1 - 31]         [Oct 1 - 15]          [Jan 1 - Feb 28]
  OKR Goal Setting  ->  H1 Mid-Year Review -> Q3 OKR Tuning  ->  H2 Annual Appraisal &
  (Annual Targets)      (Qualitative Check)   (Milestone Recal)      Promotion Calibration
```

### 2.1 Cycle Breakdown
- **Goal Setting (April):** Employees define 3 to 5 OKRs in NexaPortal in collaboration with their Reporting Manager. Every goal must have verifiable quantitative metrics.
- **H1 Mid-Year Review (July):** Formal checkpoint. Progress is reviewed, blockers removed, and developmental feedback documented. No salary changes occur in H1 unless driven by critical off-cycle promotions.
- **H2 Annual Appraisal (January - February):** Comprehensive annual performance assessment covering self-evaluations, 360-degree peer feedback, manager assessments, committee calibration, and annual compensation revisions effective April 1.

---

## 3. The 5-Point Rating Scale & Distribution Curve

Employee contributions are evaluated against both *What* was achieved (goal delivery, code quality, revenue impact) and *How* it was achieved (adherence to core PRISM values, collaboration, mentorship):

| Rating | Classification | Performance Definition | Target Bell Curve Distribution | Variable Bonus Multiplier |
|---|---|---|---|---|
| **5.0** | **Exceptional (Role Model)** | Consistently exceeds ambitious targets; drives significant organizational impact; recognized company-wide as a domain expert and culture multiplier. | 10% | 130% - 150% |
| **4.0** | **Exceeds Expectations** | Frequently delivers above baseline expectations; high technical autonomy; proactive problem solver; models values consistently. | 25% | 110% - 120% |
| **3.0** | **Meets Expectations (Core Performer)** | Reliably meets all sprint and project commitments; solid engineering quality; solid collaborative team player. | 50% | 100% |
| **2.0** | **Needs Improvement** | Inconsistent delivery; misses deadlines or quality benchmarks; requires frequent supervision; enrolled in Performance Improvement Plan. | 10% | 0% (Withheld) |
| **1.0** | **Unsatisfactory** | Fails to meet minimum job criteria; demonstrates unwillingness to adapt; triggers separation proceedings. | 5% | 0% |

---

## 4. Promotion Criteria and Career Bands

### 4.1 Engineering & Professional Banding Hierarchy
- **Band 1 (Associate SDE / Analyst):** Entry-level graduates and early-career associates (0 - 2 years experience). Focus: Task execution, learning toolchains, delivering well-defined modules.
- **Band 2 (SDE-1 / Consultant):** Autonomous contributors (2 - 4 years experience). Focus: End-to-end feature ownership, robust code quality, automated test coverage.
- **Band 3 (Senior SDE / Senior Consultant):** Technical anchors (4 - 7 years experience). Focus: Architectural design, cross-functional collaboration, unblocking junior engineers, high complexity delivery.
- **Band 4 (Lead SDE / Engineering Manager):** Team leadership & system ownership (7 - 10 years experience). Focus: System scalability, technical debt reduction, people management or deep domain specialization.
- **Band 5 (Principal Architect / Director):** Strategic technical leadership (10 - 14 years experience). Focus: Enterprise architecture, client executive engagement, multi-team roadmaps.
- **Band 6 - Band 7 (VP / Practice Head / Fellow):** Executive leadership (14+ years experience). Focus: Business unit P&L, global practice strategy, executive client partnerships.

### 4.2 Eligibility for Promotion
To be considered for promotion to the subsequent band, an employee must satisfy:
1. **Tenure in Current Role:** Minimum **18 months** in current band (exceptions for extraordinary talent require Practice Head sign-off).
2. **Performance Track Record:** Minimum two consecutive rating cycles with a rating of **4.0 or 5.0**.
3. **Demonstrated Band-Next Capability:** Proven track record of operating at the next band's responsibilities for at least 6 months prior to nomination.
4. **Promotion Dossier Submission:** Manager submits a detailed business case containing:
   - Quantified project accomplishments, system architectural contributions, and customer accolades.
   - 360-degree peer feedback from at least 3 senior stakeholders.
   - Independent review and endorsement by the *Engineering Promotion Calibration Panel*.

---

## 5. Calibration Committees and Bias Mitigation

To ensure fairness and prevent managerial favoritism:
- Departmental calibration sessions are chaired jointly by the Practice Head, Head of People Operations, and an external HRBP facilitator.
- All proposed ratings of 5.0, 2.0, and 1.0, alongside all promotion nominations, are scrutinized against standardized competency rubrics.
- Calibration committees cross-reference ratings against diversity metrics, ensuring parity across gender, tenure, and project allocations.

---

## 6. Performance Improvement Plan (PIP) Guidelines

When an employee receives a 2.0 rating or exhibits prolonged delivery slippage:
1. **Initiation:** The Reporting Manager and HRBP draft a formal 60-calendar-day Performance Improvement Plan detailing specific, measurable milestones and weekly check-ins.
2. **Support Structure:** The employee is assigned a senior mentor, relieved of secondary administrative duties, and provided targeted training resources.
3. **Outcomes:**
   - **Successful Completion:** If all PIP milestones are met at the 60-day mark, the employee resumes standard standing (bonus remains prorated for the cycle).
   - **Unsuccessful Completion:** If milestones are unmet, the employee is either offered a mutually agreed voluntary separation package or employment is terminated with 30 days statutory notice.

---

## 7. Appeals and Grievance Process
If an employee believes their appraisal rating was tainted by personal bias, discrimination, or procedural irregularity:
- The employee may file an appraisal appeal via NexaPortal within **10 business days** of receiving final appraisal notification.
- The *Appeals Review Panel* (comprising an independent Practice Head and the Chief People Officer) investigates the claim, reviews artifacts, interviews both parties, and issues a final, binding determination within 15 business days.
"""

# 13. hardware_asset_management.md (LONG ~12,000 chars)
docs_batch2["hardware_asset_management.md"] = """# NexaTech Solutions - Hardware Procurement, Asset Allocation & IT Lifecycle Policy
**Document ID:** NT-IT-POL-013  
**Version:** 4.0  
**Effective Date:** January 15, 2026  
**Owner:** IT Infrastructure, Enterprise Asset Management & Procurement  
**Classification:** Internal - All Employees  

---

## 1. Purpose and Scope
NexaTech Solutions ("NexaTech") equips employees with modern, high-grade computing workstations, peripheral displays, and mobile testing devices to ensure optimal developer productivity, client delivery, and data security.

This policy governs the procurement, allocation, acceptable maintenance, peripheral allowances, refresh cycles, and return procedures for all IT hardware assets owned or leased by NexaTech.

---

## 2. Hardware Allocation Matrix by Role

Hardware configurations are strictly aligned with job profiles, computational requirements, and client security standards:

| Role / Job Family | Hardware Specification Tier | Standard Device Models | Budget Ceiling (INR) |
|---|---|---|---|
| **Software Engineers, Data Engineers, DevOps, CloudOps (Band 1 - Band 3)** | High-Performance Engineering Workstation | Apple MacBook Pro 16" (M3 Pro, 36GB RAM, 1TB SSD) OR Dell XPS 15 (i7 14th Gen, 32GB RAM, 1TB SSD, Ubuntu/Win11) | Up to ₹2,20,000 |
| **Principal Architects, Technical Directors, AI/ML Specialists (Band 4+)** | Advanced Compute / AI Workstation | Apple MacBook Pro 16" (M3 Max, 64GB RAM, 2TB SSD) OR ThinkPad P1 Gen 7 (i9, 64GB RAM, RTX 4070 8GB) | Up to ₹3,20,000 |
| **UI/UX Designers, Creative Leads** | Creative Design Workstation | Apple MacBook Pro 16" (M3 Pro, 36GB RAM, 1TB SSD) + Apple Magic Trackpad | Up to ₹2,30,000 |
| **Sales, People Ops, Finance, Legal, Project Coordinators** | Standard Business Ultrabook | Lenovo ThinkPad T14s (i5 14th Gen, 16GB RAM, 512GB SSD) OR Dell Latitude 7450 (i5, 16GB RAM) | Up to ₹1,10,000 |

*Note:* Deviation from standard specifications requires written justification from the Practice Head and approval from the Chief Information Officer (CIO) via Jira queue `IT-CAPEX`.

---

## 3. Peripheral Allowance and Home Office Equipment

### 3.1 Office-Based Peripherals
At all physical NexaTech delivery centers (Bengaluru, Hyderabad, Pune, Gurugram), hot-desks and dedicated bays are equipped with:
- Dual 27-inch 4K USB-C Dell UltraSharp hub monitors (delivering 90W power passthrough).
- Ergonomic wireless keyboard and optical mouse.
- Cat6 Gigabit Ethernet patch cables and universal power strips.

### 3.2 Remote Ergonomic Setup Allowance
Confirmed full-time employees are entitled to a one-time reimbursement of up to **₹15,000 INR** to equip their home workspace:
- **Eligible Items:** Ergonomic task chair, height-adjustable desk or desk riser, external monitor stand, wrist rests, and uninterruptible power supply (UPS) for home Wi-Fi routers.
- **Submission:** Submit tax invoices via NexaPortal Expense Module under *Remote Ergonomic Allowance* within 90 days of confirmation.
- **Ownership:** Equipment purchased under this allowance remains the personal property of the employee; receipts must show the employee's personal name.

---

## 4. Asset Care, Maintenance, and Refresh Lifecycle

### 4.1 Asset Lifecycle and Refresh Policy
- **Standard Refresh Cycle:** Laptops are refreshed every **36 months** (3 years) from original deployment date.
- **Buy-Back Option:** Upon completing 36 months, employees may purchase their decommissioned laptop at fair depreciated market salvage value (typically 10% to 15% of original invoice value). The laptop is sanitized of all corporate data, BitLocker/FileVault keys, and MDM profiles before transfer of ownership.

### 4.2 Maintenance and Repairs
- All corporate laptops carry manufacturer premier on-site warranties (AppleCare+ Enterprise or Dell ProSupport Plus with Next Business Day On-Site Service).
- For hardware faults (faulty battery, keyboard failure, display anomalies), raise a ticket on NexaDesk under queue `IT-SERV`.
- Loaner laptops of equivalent specifications are issued by the IT Helpdesk within **2 hours** at physical delivery centers while repairs are underway.

---

## 5. Loss, Theft, and Accidental Damage Protocols

### 5.1 Immediate Reporting Obligation
In the event an asset is lost, stolen, or damaged:
1. **Immediate SLA (Within 2 Hours):** Contact the Cyber Defense Center (`infosec@nexatech.com` or +91-80-6922-0911) so the device can be remotely locked and wiped via Microsoft Intune or Jamf Pro.
2. **Police Complaint:** For stolen or lost devices, file a police complaint (e-FIR) with local municipal police within 24 hours and forward the FIR copy to `ithelpdesk@nexatech.com`.

### 5.2 Financial Liability Matrix
- **Manufacturer Defect or Normal Wear:** 100% covered by corporate maintenance contracts.
- **First Accidental Damage Event (e.g., liquid spill, accidental screen crack):** Covered under corporate damage insurance; zero employee liability.
- **Subsequent Negligent Damage (within 12 months of first incident):** Employee pays 25% of certified repair cost, capped at ₹15,000 INR, deducted via payroll.
- **Gross Negligence / Unreported Loss / Non-Filing of FIR:** If an employee fails to report a lost laptop within 24 hours or demonstrates gross negligence (e.g., leaving a laptop in an unlocked vehicle overnight), the employee is liable for 50% of the depreciated asset book value, deducted across 3 subsequent payroll cycles.

---

## 6. Asset Return and Offboarding Clearance

Upon separation or resignation from NexaTech:
- All assigned IT assets—including laptop, charging brick, power cables, hardware YubiKeys, and any mobile test devices—must be returned to the IT Helpdesk on or before the Last Working Day (LWD).
- Remote employees are shipped a prepaid, insured courier shipping crate by the Logistics Desk.
- Failure to return corporate hardware assets within 7 business days of LWD will delay the issuance of the Full and Final settlement and Relieving Certificate, and may trigger civil recovery proceedings under Indian Penal Code provisions governing criminal breach of trust.
"""

# 14. cloud_infrastructure_governance.md (LONG ~12,500 chars)
docs_batch2["cloud_infrastructure_governance.md"] = """# NexaTech Solutions - Cloud Infrastructure Governance, FinOps & Architecture Standards
**Document ID:** NT-OPS-POL-014  
**Version:** 3.4  
**Effective Date:** February 1, 2026  
**Owner:** CloudOps, Site Reliability Engineering (SRE) & FinOps Guild  
**Classification:** Confidential - Technical Infrastructure  

---

## 1. Purpose and Strategic Objectives
NexaTech Solutions ("NexaTech") manages enterprise cloud infrastructure spanning thousands of virtual instances, containerized Kubernetes clusters, serverless workloads, and petabytes of structured storage across Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP).

This policy sets enforceable governance standards for multi-account hierarchy, Infrastructure as Code (IaC), cost governance (FinOps), production change approvals, and data security.

---

## 2. Multi-Account Organization Architecture

NexaTech enforces a strict landing zone isolation architecture via AWS Organizations and Control Tower:

```
[NexaTech Master Root Organization]
  ├── Core Infrastructure OU
  │     ├── Security & CDC Account (GuardDuty, SecurityHub, CloudTrail aggregate)
  │     ├── Log Archive Account (WORM-compliant S3 storage)
  │     └── Shared Network Account (Transit Gateway, Direct Connect, Inspection VPC)
  ├── Engineering Practice Sandbox OU (Auto-nuked every 14 days, no prod data)
  ├── Client Development & QA OU (Isolated per client project)
  ├── Client Staging / Pre-Prod OU
  └── Production Workload OU (Strict zero-trust, MFA session tokens)
```

### 2.1 Environment Isolation Rules
- **Cross-Account Traffic:** Direct VPC peering between Sandbox and Production is blocked at the Service Control Policy (SCP) level.
- **Production Data Prohibition:** Production databases, customer PII, or live tokens must NEVER be copied or replicated into Development, QA, or Sandbox accounts. Anonymized synthetic data generators must be used for lower environments.

---

## 3. Infrastructure as Code (IaC) & Deployment Standards

### 3.1 Mandatory Terraform / OpenTofu Standards
- 100% of cloud resources must be provisioned via Infrastructure as Code using Terraform (version 1.7+) or OpenTofu. Manual configuration via cloud web consoles (AWS Console click-ops) is disabled in Staging and Production accounts.
- **State Management:** Terraform state files must reside in centralized remote backends (S3 with AES-256 server-side encryption and DynamoDB state locking). State files must never be committed to Git repositories.
- **Modular Design:** Teams must consume approved, hardened Terraform modules from the *NexaTech Internal Module Registry* (e.g., `terraform-aws-secure-vpc`, `terraform-aws-eks-hardened`).

### 3.2 Mandatory Resource Tagging Standard
Any resource provisioned without the following five mandatory metadata tags will be flagged by automated AWS Config rules and terminated after 48 hours in non-production accounts:
1. `Environment`: `production`, `staging`, `qa`, or `sandbox`
2. `ProjectCode`: Standard Jira billing code (e.g., `NEXA-PROJ-882`)
3. `OwnerEmail`: Tech Lead email alias (e.g., `lead.payments@nexatech.com`)
4. `CostCenter`: Finance allocation code (e.g., `CC-ENG-BLR-402`)
5. `DataClassification`: `public`, `internal`, `confidential`, or `restricted`

---

## 4. FinOps & Cost Governance

### 4.1 Practice Budget Caps and Auto-Alerts
Every business unit and client project is assigned a monthly cloud spending envelope established during contract scoping:
- **70% Threshold:** Automated Slack alert posted to `#finops-alerts` and Tech Lead notified.
- **90% Threshold:** Escalation email sent to Delivery Manager and Practice Head.
- **100% Threshold:** Mandatory architecture review with FinOps Lead. Non-essential sandbox resources (e.g., idle GPU instances, unattached EBS volumes) are paused automatically at 7:00 PM IST daily.

### 4.2 Storage and Compute Optimization Guidelines
- **Compute:** Production workloads must leverage AWS Graviton (ARM64) processors wherever compatible (yielding ~20% cost-performance benefit). Non-production environments must utilize Spot instances for worker nodes.
- **Database Scaling:** PostgreSQL and MySQL workloads must deploy AWS Aurora Serverless v2 with auto-pause enabled on developer QA clusters.
- **S3 Lifecycle Rules:** All non-production S3 buckets must enforce lifecycle rules transitioning objects to *S3 Infrequent Access* after 30 days and *Glacier Flexible Retrieval* or expiration after 90 days.

---

## 5. Production Change Approval Board (CAB) Protocols

Any architectural modification, database migration, or network reconfiguration impacting Production requires formal review:
- **Standard Changes:** Pre-approved low-risk changes (e.g., routine CI/CD container image tag updates) proceed automatically via ArgoCD pipelines.
- **Emergency Changes:** Must be approved live on bridge by the Incident Commander and CISO representative, with retrospective CAB documentation filed within 24 hours.
- **Major Architectural Changes:** Must submit a Request for Change (RFC) in Jira queue `CAB-REQ` by Wednesday 5:00 PM IST for review at the weekly Thursday 2:00 PM CAB meeting.

---

## 6. Access Control and Session Auditing
- Direct public SSH/RDP access (port 22 or 3389 open to `0.0.0.0/0`) is blocked by global SCPs.
- Administrative shell access routes through AWS Systems Manager (SSM) Session Manager or Teleport Bastion with full command keystroke logging stored in encrypted S3 buckets.
- High-privilege IAM roles (`AdministratorAccess`, `IAMFullAccess`) require multi-party approval via Slack bot `#cloud-access-approvals` and expire automatically after 4 hours.
"""

# 15. incident_response_sre_runbook.md (LONG ~13,000 chars)
docs_batch2["incident_response_sre_runbook.md"] = """# NexaTech Solutions - SRE & Enterprise Incident Management Runbook
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
"""

# 16. leave_policy_casual_sick.md (MEDIUM ~4,500 chars)
docs_batch2["leave_policy_casual_sick.md"] = """# NexaTech Solutions - Casual and Sick Leave Policy
**Document ID:** NT-HR-POL-016  
**Version:** 3.5  
**Effective Date:** January 1, 2026  
**Owner:** People Operations  
**Classification:** Internal - All Employees  

---

## 1. Overview & Annual Entitlement
NexaTech Solutions provides paid Casual Leave (CL) and Sick Leave (SL) to allow employees to address personal affairs, attend to unforeseen family commitments, and recover from personal illnesses without financial penalty.

- **Casual Leave (CL):** **12 calendar days** per calendar year (accrued quarterly at 3 days per quarter: Jan 1, Apr 1, Jul 1, Oct 1).
- **Sick / Medical Leave (SL):** **10 calendar days** per calendar year (credited in full on January 1 of each calendar year, or prorated for new joiners based on joining month).

---

## 2. Casual Leave (CL) Guidelines
- **Purpose:** Intended for short personal errands, family social functions, religious observances, or urgent personal business.
- **Maximum Duration:** CL can be taken for a maximum of **3 consecutive business days** at a time. Requests for 4 or more consecutive days must be applied under *Earned Leave (EL)*.
- **Notice Period:** Except in emergencies, CL should be applied on NexaPortal at least 48 hours in advance and requires Reporting Manager approval.
- **Half-Day Option:** CL can be utilized as half-day leave (First Half: 9:30 AM - 1:30 PM; Second Half: 1:30 PM - 6:00 PM).
- **Lapse & Non-Encashment:** Unavailed CL lapses entirely at the end of each calendar year (December 31) and cannot be carried forward or encashed.

---

## 3. Sick / Medical Leave (SL) Guidelines
- **Purpose:** Reserved strictly for employee medical recovery, illness, injury, outpatient medical procedures, or medical quarantine.
- **Intimation:** In case of sudden illness, the employee must notify their Reporting Manager via Slack or email by 9:30 AM IST on the day of absence.
- **Medical Certificate Requirement:**
  - For SL of 1 or 2 consecutive days: Self-declaration on NexaPortal suffices.
  - For SL exceeding **2 consecutive business days** (3 or more days): A valid medical fitness certificate and prescription from a registered medical practitioner (MBBS or equivalent) must be uploaded on NexaPortal upon resumption of duty.
- **Lapse & Non-Encashment:** Unavailed Sick Leave lapses at the end of the calendar year and cannot be carried forward or encashed.

---

## 4. Clubbing and Combination Rules
- **Prohibited Clubbing:** Casual Leave (CL) CANNOT be combined with Sick Leave (SL), Earned Leave (EL), or Maternity/Paternity Leave in a single continuous leave stretch.
- **Sandwich Rule Exception:** NexaTech does NOT enforce the "sandwich rule" for CL or SL. Intervening weekend days (Saturday and Sunday) or gazetted public holidays falling between approved leave dates are NOT deducted from the leave balance.
"""

# 17. leave_policy_earned_vacation.md (MEDIUM ~4,500 chars)
docs_batch2["leave_policy_earned_vacation.md"] = """# NexaTech Solutions - Earned Leave & Vacation Policy
**Document ID:** NT-HR-POL-017  
**Version:** 3.3  
**Effective Date:** January 1, 2026  
**Owner:** People Operations  
**Classification:** Internal - All Employees  

---

## 1. Purpose and Entitlement
NexaTech recognizes that extended rest and vacation are essential for long-term creativity, engineering excellence, and sustained well-being. Earned Leave (EL), also known as Privilege Leave (PL), provides planned vacation time for all confirmed full-time staff.

- **Annual Entitlement:** **18 working days** per calendar year.
- **Accrual Rate:** Accrues at the rate of **1.5 working days** for every completed calendar month of active service.
- **Probationary Staff:** Accrues during probation, but may only be availed after successful confirmation, unless approved by Practice Head under exceptional personal circumstances.

---

## 2. Planning, Advance Notice, and Approval Workflows
- **Notice Period Requirements:**
  - Leave duration of 1 to 3 days: Apply at least 5 business days in advance.
  - Leave duration of 4 to 9 days: Apply at least 15 calendar days in advance.
  - Extended vacation (10 or more consecutive days): Apply at least **30 calendar days** in advance to allow client sprint planning and team coverage coordination.
- **Approval Chain:**
  - Up to 5 days: Reporting Manager approval.
  - 6 to 10 days: Reporting Manager + Delivery Lead approval.
  - Greater than 10 days: Reporting Manager + Practice Head approval.

---

## 3. Accumulation, Carry-Forward & Encashment
- **Maximum Accumulation Limit:** An employee can accumulate up to a maximum of **45 working days** of Earned Leave in their leave account.
- **Year-End Carry Forward:** At the end of each calendar year (December 31), any accrued EL balance up to 45 days is automatically carried forward to the subsequent year. Any excess days beyond 45 days lapse automatically on December 31 without compensation.
- **Encashment Upon Separation:** Upon resignation, retirement, or termination, accumulated unavailed Earned Leave (up to the maximum ceiling of 45 days) is encashed as part of the Full & Final (F&F) settlement calculated based on the employee's `Basic Salary / 30 * Accumulated Days`. Active in-service encashment is not permitted.
"""

# 18. parental_maternity_paternity_leave.md (MEDIUM ~4,500 chars)
docs_batch2["parental_maternity_paternity_leave.md"] = """# NexaTech Solutions - Parental, Maternity, Paternity & Adoption Leave Policy
**Document ID:** NT-HR-POL-018  
**Version:** 4.1  
**Effective Date:** January 1, 2026  
**Owner:** People Operations & Total Rewards  
**Classification:** Internal - All Employees  

---

## 1. Philosophy and Commitment
NexaTech is dedicated to supporting growing families and empowering working parents. Our parental benefits align with the Maternity Benefit (Amendment) Act, 2017, and extend market-leading provisions for biological, adoptive, and commissioning parents.

---

## 2. Maternity Leave (Biological Mothers)
- **Entitlement:** **26 continuous calendar weeks (182 calendar days)** of fully paid maternity leave for female employees expecting up to two surviving children. For third child onwards, statutory leave is 12 weeks.
- **Commencement Window:** Leave may commence up to 8 weeks prior to the expected delivery date, with the remaining balance availed postpartum.
- **Eligibility:** Female employees who have worked at NexaTech for at least 80 working days in the 12 months preceding expected delivery.
- **Miscarriage / Medical Termination:** In the unfortunate event of a miscarriage or medical termination of pregnancy, 6 weeks (42 calendar days) of paid medical leave is granted immediately upon submission of a certified doctor's certificate.

---

## 3. Paternity Leave (Fathers & Secondary Caregivers)
- **Entitlement:** **15 working days** of fully paid paternity leave for male employees upon the birth of their child or legal adoption of a child under 1 year of age.
- **Utilization Window:** May be availed in up to two separate tranches within **6 months** of childbirth.
- **Advance Notice:** Must be applied on NexaPortal at least 14 days prior to intended commencement.

---

## 4. Adoption and Surrogacy Leave
- **Primary Adoptive / Commissioning Mother:** **12 continuous calendar weeks (84 calendar days)** of fully paid leave for legally adopting a child under 1 year of age, or commissioning a surrogate mother, effective from the date custody is formally awarded.
- **Adoptive Father:** Entitled to 15 working days of paid leave within 6 months of adoption.

---

## 5. Phased Return-to-Work and Creche Amenities
- **Gradual Ramp-Back:** Returning mothers may work 50% hours on full salary for the first 4 weeks post-maternity leave upon agreement with their Delivery Manager.
- **Corporate Creche Tie-ups:** NexaTech delivery centers maintain partnerships with verified on-site or near-site daycare centers (e.g., Klay Prep Schools, WeCare) within a 5km radius, subsidized 50% by NexaTech for children up to 4 years old.
"""

# 19. bereavement_sabbatical_leave.md (MEDIUM ~4,200 chars)
docs_batch2["bereavement_sabbatical_leave.md"] = """# NexaTech Solutions - Bereavement Leave & Career Sabbatical Policy
**Document ID:** NT-HR-POL-019  
**Version:** 3.0  
**Effective Date:** January 1, 2026  
**Owner:** People Operations  
**Classification:** Internal - All Employees  

---

## 1. Bereavement Leave
NexaTech recognizes that the loss of a loved one is an emotionally challenging time requiring personal mourning, funeral observances, and estate administration.

### 1.1 Entitlement and Eligible Relations
- **Immediate Family Loss:** **5 consecutive working days** of fully paid leave granted upon the passing of: spouse, child, parent, parent-in-law, brother, sister, or legal guardian.
- **Extended Family Loss:** **2 working days** of paid leave granted upon the passing of: grandparent, grandchild, uncle, aunt, or first cousin.
- **Travel Accommodation:** If interstate or international travel (>500 km) is required to attend funeral rites, an additional 2 days of unpaid or Earned Leave may be tagged without advance notice penalties.
- **Notice & Intimation:** Verbal or Slack intimation to the manager on Day 1 is accepted, with formal logging on NexaPortal within 10 days of return.

---

## 2. Career Sabbatical Policy
NexaTech supports career longevity and life enrichment by offering unpaid sabbaticals for higher education, critical health recuperation, or public service.

### 2.1 Sabbatical Eligibility Criteria
- **Minimum Service Tenure:** Continuous confirmed employment of at least **3 continuous years** at NexaTech.
- **Performance Threshold:** Performance ratings of 3.0 or higher across the preceding two appraisal cycles.
- **Duration:** Minimum duration of **3 months** up to a maximum of **12 calendar months**.

### 2.2 Terms During Sabbatical
- **Compensation:** The sabbatical is strictly unpaid; salary, bonuses, and retirement contributions pause during the sabbatical tenure.
- **Health Insurance:** Corporate health insurance (GMC) may be continued at the employee's personal expense by paying the monthly group premium in advance.
- **Equipment & System Access:** Corporate laptops, badges, and cloud access credentials must be surrendered to IT prior to commencing the sabbatical.
- **Re-Employment Guarantee:** Upon successful completion of an approved sabbatical, NexaTech guarantees reinstatement in an equivalent role and band, subject to a 60-day advance notice of return.
"""

# 20. public_holidays_comp_off.md (MEDIUM ~4,000 chars)
docs_batch2["public_holidays_comp_off.md"] = """# NexaTech Solutions - Gazetted Public Holidays & Compensatory Off (Comp-Off) Policy
**Document ID:** NT-HR-POL-020  
**Version:** 3.2  
**Effective Date:** January 1, 2026  
**Owner:** People Operations & Workforce Management  
**Classification:** Internal - All Employees  

---

## 1. Annual Public Holiday Framework
NexaTech recognizes **12 paid public holidays** per calendar year across its Indian offices:
- **Mandatory National Holidays (3 Days):**
  1. Republic Day (January 26)
  2. Independence Day (August 15)
  3. Mahatma Gandhi Jayanti (October 2)
- **Regional & Cultural Holidays (9 Days):** Published annually in December for the upcoming calendar year, customized by delivery center location (e.g., Kannada Rajyotsava in Bengaluru, Bathukamma in Hyderabad, Ganeshotsav in Pune).

---

## 2. Compensatory Off (Comp-Off) Framework

### 2.1 Eligibility for Comp-Off
Engineers, support analysts, and operations personnel required by business needs to work on a designated public holiday or weekend (Saturday/Sunday) are eligible for Compensatory Off:
- **Minimum Work Duration:** The employee must log a minimum of **4 active hours** (for half-day comp-off) or **7 active hours** (for full-day comp-off).
- **Mandatory Pre-Approval:** Weekend/holiday work must be pre-authorized in writing by the Project Delivery Manager via NexaPortal at least 24 hours prior to the date. Spontaneous unapproved weekend work does not qualify.

### 2.2 Validity and Claim Workflow
- **Application Deadline:** Comp-Off must be claimed in NexaPortal within **7 calendar days** of the weekend or holiday worked.
- **Validity Window:** Approved Comp-Off credits must be availed as time-off within **60 calendar days** of being credited.
- **Lapse & Non-Encashment:** Unavailed Comp-Off balances expire automatically after 60 days. Comp-off credits cannot be encashed for monetary compensation or accumulated toward separation payouts.
"""

for filename, content in docs_batch2.items():
    file_path = DOCS_DIR / filename
    file_path.write_text(content.strip(), encoding="utf-8")
    print(f"Written: {filename} ({len(content)} chars)")

print("Batch 2 Complete: 10 files written.")
