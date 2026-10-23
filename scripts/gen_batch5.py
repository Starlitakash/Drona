import os
from pathlib import Path

DOCS_DIR = Path("docs")
DOCS_DIR.mkdir(parents=True, exist_ok=True)

docs_batch5 = {}

# 41. relocation_assistance_policy.md (MEDIUM ~5,000 chars)
docs_batch5["relocation_assistance_policy.md"] = """# NexaTech Solutions - Employee Relocation Assistance & Settlement Policy
**Document ID:** NT-HR-POL-041  
**Version:** 3.3  
**Effective Date:** January 1, 2026  
**Owner:** Talent Acquisition, Mobility & People Operations  
**Classification:** Internal - All Employees  

---

## 1. Scope and Relocation Assistance Principles
NexaTech Solutions ("NexaTech") provides structured financial, logistical, and settlement assistance to newly hired employees or existing employees transferring laterally across corporate delivery centers (Bengaluru, Hyderabad, Pune, Gurugram) at the company's request.

---

## 2. Relocation Financial Assistance Packages

Reimbursement ceilings are categorized based on employee professional bands:

| Band / Level | Packers & Movers Logistics Cap (INR) | Initial Corporate Hotel Stay | House Brokerage Allowance (INR) | One-Time Settling-In Allowance |
|---|---|---|---|---|
| **Bands 1 - 2 (Associate / SDE-1)** | Up to ₹40,000 | 10 Calendar Days (Breakfast included) | Up to ₹25,000 (or actuals) | ₹15,000 (Taxable) |
| **Bands 3 - 4 (Senior SDE / Architect)** | Up to ₹65,000 | 14 Calendar Days (Breakfast included) | Up to ₹40,000 (or actuals) | ₹25,000 (Taxable) |
| **Bands 5+ (Principal / Director / VP)** | Up to ₹1,00,000 | 21 Calendar Days (Breakfast included) | Up to ₹60,000 (or actuals) | ₹50,000 (Taxable) |

---

## 3. Travel and Transit Flights
- **One-Way Transit Airfare:** NexaTech Corporate Travel Desk books economy class airfare for the employee, legal spouse, and up to two dependent children from their origin city to the new destination city.
- **Airport Transfer:** Corporate cab booked by the Travel Desk picks up the family from origin residence to airport, and from destination airport to the corporate hotel.

---

## 4. Packing, Moving & Vehicle Transportation
- Logistics must be executed through NexaTech empaneled moving partners (**Agarwal Packers & Movers / Allied Pickfords**). Direct billing to NexaTech is coordinated by the Mobility Desk (`mobility@nexatech.com`).
- If using an unempaneled vendor, the employee must obtain at least three competitive quotations and obtain written pre-approval from the Mobility Lead.
- Transportation of one personal vehicle (car or two-wheeler) is covered within the overall logistics cap.

---

## 5. Clawback & Repayment Covenant
Relocation benefits represent a substantial corporate investment. If an employee voluntarily resigns or is terminated for cause within **12 continuous months** of the relocation date:
- **100% of the total relocation expenses** (including hotel costs, packing/moving invoices, brokerage, airfare, and settling-in allowance) must be refunded to NexaTech.
- The amount is recovered directly from the employee's Full and Final (F&F) settlement.
"""

# 42. referral_bonus_policy.md (MEDIUM ~4,800 chars)
docs_batch5["referral_bonus_policy.md"] = """# NexaTech Solutions - Employee Referral Program & Bounty Policy
**Document ID:** NT-TA-POL-042  
**Version:** 4.1  
**Effective Date:** January 1, 2026  
**Owner:** Talent Acquisition & Total Rewards  
**Classification:** Internal - All Employees  

---

## 1. Overview and Program Philosophy
Top engineering talent thrives among top engineering talent. The NexaTech Referral Bounty Program encourages employees to recommend skilled colleagues, former teammates, and industry contacts for active job openings across our delivery centers.

---

## 2. Referral Bounty Payout Matrix

Referral bounties are awarded based on the professional band of the hired role:

| Position / Band Hired | Standard Referral Bounty (INR) | Niche Skill / Diversity Candidate Bounty (INR) |
|---|---|---|
| **Band 1 (Associate SDE / Analyst)** | **₹25,000** | **₹35,000** |
| **Band 2 (SDE-1 / Consultant)** | **₹35,000** | **₹50,000** |
| **Band 3 (Senior SDE / Technical Lead)** | **₹50,000** | **₹75,000** |
| **Band 4 (Lead Architect / Engineering Manager)** | **₹75,000** | **₹1,00,000** |
| **Band 5+ (Principal Architect / Director / VP)** | **₹1,00,000** | **₹1,50,000** |

*Note: Diversity candidates (female, non-binary, or differently-abled hires) and niche skill roles (GenAI Architects, Rust Systems Engineers, SRE Principal Leads) qualify for the higher bounty tier.*

---

## 3. Payout Schedule & Tranches
To encourage long-term retention, referral bounties are disbursed in two equal installments:
- **Tranche 1 (50% of Bounty):** Paid in the payroll cycle immediately following the candidate's formal joining date.
- **Tranche 2 (Remaining 50%):** Paid in the payroll cycle following the candidate's successful 90-day probationary confirmation.
- The referring employee must be on active payroll on the date of payout.

---

## 4. Eligibility and Submission Rules
- **Submission Portal:** Referrals must be submitted via Greenhouse ATS (`https://nexatech.greenhouse.io`) prior to the candidate applying directly or through a recruitment agency.
- **Referral Validity:** A candidate referral remains valid in the ATS for **6 calendar months** from submission date.
- **Ineligible Roles:** Members of Talent Acquisition, HRBPs, and hiring managers evaluating candidates for their own direct reporting line are ineligible for referral bounties.
"""

# 43. password_authentication_standards.md (MEDIUM ~4,700 chars)
docs_batch5["password_authentication_standards.md"] = """# NexaTech Solutions - Enterprise Password & Multi-Factor Authentication Standards
**Document ID:** NT-SEC-STD-043  
**Version:** 4.2  
**Effective Date:** February 1, 2026  
**Owner:** Cyber Defense Center & Identity Governance Guild  
**Classification:** Confidential - Technical Security Standard  

---

## 1. Scope and Authentication Principles
Compromised credentials represent the primary attack vector for enterprise breaches. This standard defines technical parameters for passwords, passphrases, multi-factor authentication (MFA), hardware tokens, and service accounts across Active Directory, Okta SSO, AWS IAM, GitHub, and production Kubernetes clusters.

---

## 2. Password Complexity Requirements

All interactive user accounts must enforce the following cryptographic policies:
- **Minimum Length:** **14 alphanumeric characters** (passphrases of 18+ characters encouraged).
- **Complexity Enforcements:** Must contain at least one uppercase letter (`A-Z`), one lowercase letter (`a-z`), one numerical digit (`0-9`), and one special symbol (`!@#$%^&*()-_+=`).
- **Rotation Frequency:** Mandatory expiration and password change every **90 calendar days**.
- **History Enforcement:** Systems prevent reuse of the previous **6 passwords**.
- **Lockout Threshold:** Automated account lockout after **5 consecutive failed attempts**. Lockout duration is 30 minutes unless unlocked manually by IT Service Desk.

---

## 3. Multi-Factor Authentication (MFA) Mandate
- MFA is universally required for all logins to corporate SSO, VPN, email, and cloud consoles.
- **Approved Authenticators:**
  1. Okta Verify with Number Matching (Push Notification).
  2. Microsoft Authenticator with Number Matching.
  3. FIPS 140-2 Level 3 Hardware Security Keys (YubiKey 5 Series).
- **Prohibited Methods:** SMS-based OTP and voice-call OTP are strictly disabled due to SIM-swapping and SS7 interception vulnerabilities.

---

## 4. Privileged Access & Hardware Security Keys
- Engineers with production write permissions, AWS Organization root access, or GitHub Organization Owner roles must utilize **hardware YubiKeys** as their primary second-factor credential.
- Keys must be enrolled in presence of IT Security personnel on Floor 3 CDC Kiosk.

---

## 5. Machine Credentials and API Keys
- API keys, service principal secrets, and database credentials must never be hard-coded into source code repositories.
- All secrets must be fetched at runtime via HashiCorp Vault or AWS Secrets Manager with automated 30-day credential rotation enabled.
"""

# 44. data_classification_handling.md (MEDIUM ~4,900 chars)
docs_batch5["data_classification_handling.md"] = """# NexaTech Solutions - Enterprise Data Classification & Handling Standard
**Document ID:** NT-SEC-STD-044  
**Version:** 4.0  
**Effective Date:** January 15, 2026  
**Owner:** Information Security & Data Protection Officer (DPO)  
**Classification:** Internal - All Personnel  

---

## 1. Purpose and Data Protection Framework
NexaTech manages critical data assets on behalf of healthcare, banking, and government clients. This standard defines our four-tier classification taxonomy and specifies security controls for storage, transmission, encryption, and disposal in compliance with ISO 27001, SOC 2, GDPR, and India's DPDP Act 2023.

---

## 2. Four-Tier Data Classification Taxonomy

| Classification Tier | Definition & Examples | Encryption Mandates | Egress & Sharing Restrictions |
|---|---|---|---|
| **Tier 1: Public** | Marketing collateral, public press releases, published whitepapers, careers page job descriptions. | None mandated | Freely shareable externally |
| **Tier 2: Internal** | Employee handbook, internal engineering wikis, generic Slack conversations, org charts. | TLS 1.3 in transit | Restricted to NexaTech employees and contractors under NDA |
| **Tier 3: Confidential** | Customer source code, architectural blueprints, financial reports, employee salary structures, commercial proposals. | AES-256 at rest; TLS 1.3 in transit | Restricted to project team members; watermarked on export |
| **Tier 4: Restricted (Highly Sensitive)** | Customer production PII, PHI (medical records), payment card PANs, database master credentials, encryption private keys. | Field-level AES-GCM 256; Hardware Security Module (HSM) | Strictly zero egress; multi-party approval required |

---

## 3. Data Loss Prevention (DLP) Controls
- Endpoint DLP (CrowdStrike / Microsoft Purview) scans all outbound email attachments and web uploads for patterns matching Aadhaar numbers, Social Security numbers, credit card sequences, and private cryptographic keys.
- Detected unauthorized transmissions are blocked in real-time and trigger an immediate SEV-2 security alert to the Cyber Defense Center (`infosec@nexatech.com`).

---

## 4. Secure Disposal and Media Sanitization
- Digital files classified as Confidential or Restricted must be wiped using cryptographic erasure or multi-pass overwrite (NIST SP 800-88 Rev 1 guidelines).
- Physical hard drives and SSDs decommissioned from servers or laptops are destroyed using industrial on-site degaussing and shredding with certificates of destruction issued by certified e-waste partners.
"""

# 45. access_control_rbac_policy.md (MEDIUM ~4,600 chars)
docs_batch5["access_control_rbac_policy.md"] = """# NexaTech Solutions - Role-Based Access Control (RBAC) & Privilege Governance Policy
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
"""

# 46. byod_mobile_device_management.md (MEDIUM ~4,500 chars)
docs_batch5["byod_mobile_device_management.md"] = """# NexaTech Solutions - Bring Your Own Device (BYOD) & Mobile Security Policy
**Document ID:** NT-IT-POL-046  
**Version:** 3.2  
**Effective Date:** January 1, 2026  
**Owner:** Enterprise Mobility, IT Infrastructure & Security  
**Classification:** Internal - All Personnel  

---

## 1. Scope and Objective
To support workplace mobility, NexaTech allows employees to access corporate email, Slack, and calendars on personal mobile smartphones and tablets under our Bring Your Own Device (BYOD) framework.

To safeguard corporate data, personal devices accessing NexaTech corporate resources must enroll in enterprise Mobile Device Management (MDM).

---

## 2. Device Enrollment & Containerization (Microsoft Intune)
- Personal devices (iOS 17+ or Android 13+) must install the **Microsoft Intune Company Portal**.
- **Enterprise Sandbox / Work Profile:** Corporate applications (Outlook, Slack, Teams, Authenticator) run inside an encrypted, isolated container.
- **Personal Privacy Guarantee:** NexaTech IT cannot see, access, or monitor personal photos, personal WhatsApp chats, browsing history, or personal apps.

---

## 3. Mandatory Security Standards for BYOD Endpoints
- **Device Passcode:** Minimum 6-digit PIN or biometric unlock (Face ID / Fingerprint) required. Simple PINs (e.g., `123456`, `000000`) are blocked.
- **OS Updates:** Operating systems must be updated within 14 days of security patch releases.
- **Jailbreak / Rooting Prohibition:** Jailbroken iOS devices or rooted Android devices are blocked from corporate access automatically.
- **Screen Lock Timeout:** Device must lock automatically after 3 minutes of inactivity.

---

## 4. Selective Remote Wipe Protocol
In the event a BYOD device is lost, stolen, or an employee separates from NexaTech:
- The IT Helpdesk executes a **Selective Enterprise Wipe**.
- This wipes all corporate emails, Slack caches, and work tokens, leaving personal photos, personal apps, and private data 100% untouched.
"""

# 47. secure_coding_standards.md (MEDIUM ~4,900 chars)
docs_batch5["secure_coding_standards.md"] = """# NexaTech Solutions - Secure Coding & Application Security Standards
**Document ID:** NT-ENG-STD-047  
**Version:** 4.1  
**Effective Date:** February 1, 2026  
**Owner:** Application Security Guild & Engineering Excellence  
**Classification:** Internal - Technical Staff  

---

## 1. Philosophy: Shift-Left Security
At NexaTech, security is integrated from the initial architectural design phase rather than audited at deployment. All software applications engineered for clients or internal operations must resist modern threat vectors, complying with OWASP Top 10 (Web), OWASP Top 10 (API), and SANS Top 25 standards.

---

## 2. Core Application Security Requirements

### 2.1 Injection & Input Sanitization
- All database queries must utilize parameterized queries, prepared statements, or modern Object-Relational Mappers (ORMs). Raw SQL string concatenation is strictly blocked by SonarQube quality gates.
- All external user inputs must undergo strict schema validation (using Pydantic, Zod, or Bean Validation) and output encoding to eliminate Cross-Site Scripting (XSS).

### 2.2 Authentication & Cryptography
- Passwords must be hashed using modern memory-hard cryptographic algorithms: **Argon2id** (recommended) or **bcrypt** with a minimum work factor of 12. Deprecated algorithms (MD5, SHA-1, DES) are banned.
- All external and inter-service HTTP communications must enforce TLS 1.3 with forward secrecy.

### 2.3 Secret Management & Hardcoded Credentials
- Source code repositories must never contain API keys, private certificates, or database passwords.
- GitGuardian pre-commit hooks block any commit containing secret signatures. Violations trigger automated notifications to the AppSec team.

---

## 3. Automated CI/CD Security Gating
Every GitHub Actions pull request pipeline executes automated security analysis:
- **Static Application Security Testing (SAST):** SonarQube Enterprise gates fail any PR introducing new Security Hotspots or high-severity vulnerabilities.
- **Software Composition Analysis (SCA):** Snyk Developer scans open-source dependencies and blocks PRs introducing packages with known Critical CVEs.
- **Dynamic Application Security Testing (DAST):** OWASP ZAP automated baseline scans run nightly against staging environments.
"""

# 48. vulnerability_management_patching.md (MEDIUM ~4,700 chars)
docs_batch5["vulnerability_management_patching.md"] = """# NexaTech Solutions - Enterprise Vulnerability Management & Patching Policy
**Document ID:** NT-SEC-POL-048  
**Version:** 3.5  
**Effective Date:** February 1, 2026  
**Owner:** Cyber Defense Center & Infrastructure Operations  
**Classification:** Internal - Technical Operations  

---

## 1. Objective and Scanning Scope
This policy mandates continuous identification, risk assessment, and systematic patching of security vulnerabilities across corporate laptops, cloud infrastructure, container registries, and serverless architectures.

---

## 2. Vulnerability Severity Tiers & Remediation SLAs

Vulnerability remediation timelines are strictly governed by Common Vulnerability Scoring System (CVSS v3.1) scores:

| Severity Level | CVSS Score Range | Mandatory Remediation SLA | Example Scenarios |
|---|---|---|---|
| **Critical** | 9.0 – 10.0 | **48 Hours** | Remote Code Execution (RCE), unauthenticated privilege escalation, zero-day exploits. |
| **High** | 7.0 – 8.9 | **14 Calendar Days** | SQL injection, authentication bypass, high-impact denial of service. |
| **Medium** | 4.0 – 6.9 | **30 Calendar Days** | Cross-Site Scripting (XSS), information disclosure of internal paths. |
| **Low** | 0.1 – 3.9 | **90 Calendar Days** | Minor version banner disclosures, weak cipher warnings. |

---

## 3. Regular Patching Windows
- **Monthly Maintenance Window:** Scheduled server and container base image patching occurs on the third Saturday of each calendar month between 01:00 AM and 05:00 AM IST.
- **Zero-Day Emergency Patching:** For actively exploited zero-day vulnerabilities affecting production workloads (e.g., Log4Shell-scale exploits), the CISO authorizes immediate emergency out-of-band patching without waiting for scheduled maintenance windows.

---

## 4. Exception Management
If patching a vulnerability breaks legacy client software dependencies:
- A formal Security Exception Request must be logged in Jira under queue `SEC-EXCEPT`.
- The exception requires compensatory security controls (e.g., WAF virtual patching, network isolation) and must be countersigned by the CISO and Delivery Head. Exceptions expire after 60 days.
"""

# 49. third_party_vendor_security.md (MEDIUM ~4,500 chars)
docs_batch5["third_party_vendor_security.md"] = """# NexaTech Solutions - Third-Party Vendor & Supplier Risk Management Policy
**Document ID:** NT-SEC-POL-049  
**Version:** 3.1  
**Effective Date:** January 1, 2026  
**Owner:** Vendor Management Office (VMO) & InfoSec Compliance  
**Classification:** Internal - Procurement & Management  

---

## 1. Purpose and Supply Chain Integrity
Third-party software vendors, SaaS providers, and contractors can introduce serious supply chain vulnerabilities. NexaTech enforces rigorous pre-procurement security vetting and ongoing compliance auditing for all external technology partners.

---

## 2. Vendor Risk Categorization
- **Tier 1 (High Risk / Critical):** Vendors hosting, storing, or processing NexaTech customer data, production source code, or PII (e.g., AWS, GitHub, Databricks, Salesforce).
- **Tier 2 (Moderate Risk):** Vendors with indirect access to internal networks or operational workflows (e.g., Jira, Slack, Zoom).
- **Tier 3 (Low Risk):** Vendors providing generic non-technical goods, office supplies, or catering services.

---

## 3. Pre-Procurement Security Vetting
Before contracting any Tier 1 or Tier 2 technology vendor:
1. The vendor must provide current independent audit certifications: **SOC 2 Type II Report** (within last 12 months) and/or **ISO/IEC 27001:2022 Certificate**.
2. The vendor must complete the *NexaTech Standard Vendor Security Questionnaire (VSQ)* covering data encryption, incident notification SLAs (<24 hours for breaches), and employee background checks.
3. The Cyber Defense Center issues a formal Vendor Security Assessment Report with an approved risk rating before Procurement can execute agreements.

---

## 4. Continuous Monitoring & Annual Re-Assessment
- Tier 1 vendor security postures are re-audited annually.
- In the event of a reported security breach at a vendor, the NexaTech Incident Commander activates immediate supply-chain response protocols within 4 hours.
"""

# 50. disaster_recovery_business_continuity.md (MEDIUM ~4,900 chars)
docs_batch5["disaster_recovery_business_continuity.md"] = """# NexaTech Solutions - Disaster Recovery (DR) & Business Continuity Plan (BCP)
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
"""

for filename, content in docs_batch5.items():
    file_path = DOCS_DIR / filename
    file_path.write_text(content.strip(), encoding="utf-8")
    print(f"Written: {filename} ({len(content)} chars)")

print("Batch 5 Complete: 10 files written.")
