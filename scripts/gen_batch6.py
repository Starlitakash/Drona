import os
from pathlib import Path

DOCS_DIR = Path("docs")
DOCS_DIR.mkdir(parents=True, exist_ok=True)

docs_batch6 = {}

# 51. data_retention_and_disposal.md (MEDIUM ~5,200 chars)
docs_batch6["data_retention_and_disposal.md"] = """# NexaTech Solutions - Corporate Data Retention, Archival & Disposal Policy
**Document ID:** NT-LGL-POL-051  
**Version:** 3.4  
**Effective Date:** January 15, 2026  
**Owner:** Legal, Corporate Governance & Data Protection Office  
**Classification:** Internal - All Personnel  

---

## 1. Purpose and Statutory Scope
NexaTech Solutions ("NexaTech") creates, processes, and maintains large volumes of business records, financial filings, software intellectual property, and client data. This policy defines statutory retention timelines, archival standards, and secure disposal protocols in accordance with the Companies Act, 2013, the Income Tax Act, 1961, the Digital Personal Data Protection (DPDP) Act, 2023, GDPR, and SOC 2 Type II audit requirements.

---

## 2. Statutory Data Retention Schedule

All corporate records must be retained in accordance with the following mandatory schedule:

| Category of Records | Specific Document Types | Mandatory Retention Period | Primary Custodian | Storage Location |
|---|---|---|---|---|
| **Financial & Accounting** | Books of account, audit balance sheets, tax filings, invoices, bank statements, statutory audit working papers | **8 Financial Years** (from end of relevant FY) | Finance Controller | Encrypted Cold Storage (AWS S3 Glacier WORM) |
| **Corporate Legal & Board** | Articles of Association, Board Minutes, shareholder registers, regulatory licenses | **Permanent (Perpetual)** | Company Secretary | Fireproof Safe & Azure Archive Vault |
| **Employee Personnel Records** | Offer letters, employment agreements, confirmation letters, disciplinary inquiries, BGV reports | **7 Years Post-Separation** | People Operations | Darwinbox HRMS Cloud Archive |
| **Payroll & Statutory Retirals** | Monthly payroll registers, EPF returns, ESI filings, Form 16s, Gratuity ledgers | **10 Years Post-Payment** | Payroll Desk | Keka Payroll Historical Vault |
| **Customer Project Deliverables** | Client code repositories, architectural designs, Master Services Agreements (MSAs), Statements of Work (SOWs) | **7 Years Post-Contract Completion** | Delivery Management Office | GitHub Enterprise & Client Secure Archive |
| **Cybersecurity & Audit Telemetry** | Active Directory authentication logs, firewall traffic, VPN session records, SIEM events | **1 Calendar Year Active, 3 Years Archived** | Cyber Defense Center | AWS S3 Log Archive (Encrypted) |

---

## 3. Data Archival and Cold Storage
- **Automated Lifecycle Transitions:** Data older than 90 days must be transitioned from high-performance production storage to cost-effective cold tiers (e.g., AWS S3 Standard to S3 Glacier Flexible Retrieval).
- **Immutability (WORM Compliance):** Financial archives and legal hold datasets must be stored with Object Lock enabled in Compliance Mode to prevent accidental or malicious deletion.
- **Encryption:** All archived data must be encrypted with AWS KMS customer-managed keys (CMK) enforcing AES-256 bit encryption.

---

## 4. Secure Disposal and Media Sanitization Protocols

Upon the expiration of the mandatory retention window, data must be permanently purged:
1. **Digital Purging:** Digital records must be destroyed using certified cryptographic erasure or multi-pass data shredding in compliance with NIST SP 800-88 Revision 1 guidelines.
2. **Physical Asset Destruction:** Decommissioned hard drives, magnetic tapes, and solid-state disks must undergo mechanical degaussing followed by industrial physical shredding.
3. **Certificate of Destruction:** E-waste disposal contractors must issue a formal *Certificate of Destruction* documenting asset serial numbers, date, and witnessed destruction signatures. Certificates are retained perpetually by Facilities.

---

## 5. Legal Hold Overrides
In the event of active litigation, tax investigations, or regulatory subpoenas, the Legal Department issues an official **Legal Hold Notice**:
- All automated deletion routines and document shredding schedules for relevant custodians are suspended immediately.
- Destroying or altering documents subject to an active Legal Hold constitutes a criminal offense resulting in summary termination and civil prosecution.
"""

# 52. confidentiality_nda_guidelines.md (MEDIUM ~5,400 chars)
docs_batch6["confidentiality_nda_guidelines.md"] = """# NexaTech Solutions - Confidentiality, Trade Secrets & Non-Disclosure Guidelines
**Document ID:** NT-LGL-POL-052  
**Version:** 4.1  
**Effective Date:** January 1, 2026  
**Owner:** Legal Department & Intellectual Property Office  
**Classification:** Internal - All Employees & Contractors  

---

## 1. Executive Summary and Fiduciary Duty
In the course of technical consulting and software engineering, NexaTech personnel routinely access proprietary source code, algorithmic designs, unannounced product roadmaps, pricing models, and sensitive client architectures. The unauthorized disclosure of such confidential assets jeopardizes client relationships, exposes NexaTech to multi-million-dollar liabilities, and breaches criminal trade secret protections.

Every employee signs the NexaTech Proprietary Information and Inventions Agreement (PIIA) upon joining. This document provides practical guidance on executing your confidentiality obligations.

---

## 2. Defining Confidential Information
Confidential Information encompasses all non-public technical, business, and operational data, including:
- **Technical Assets:** Source code, architectural blueprints, database schemas, cryptographic private keys, internal API endpoints, ML training datasets, and benchmarks.
- **Commercial Assets:** Master Services Agreements (MSAs), Statements of Work (SOWs), profit margins, hourly billing rate cards, sales pipeline data, and pricing formulas.
- **Client Assets:** Any data, customer databases, personal healthcare information (PHI), or financial transactions belonging to NexaTech clients.
- **Human Resources Data:** Employee salary structures, performance ratings, internal investigation reports, and personnel medical records.

---

## 3. Practical Safeguards for Daily Operations
Employees must practice rigorous information hygiene:
1. **Clean Screen & Clean Desk:** Never display confidential client diagrams in public transit, coffee shops, or shared co-working spaces without a 3M privacy filter attached.
2. **Authorized Repositories Only:** Never export, forward, or copy confidential source code or datasets to personal Gmail, Google Drive, personal GitHub, or external USB storage.
3. **Public Discussion Ban:** Never discuss client names, technical challenges, or project code-names in public elevators, cafeterias, or on public transit shuttles.
4. **Third-Party AI Gateways:** Never paste client source code or proprietary schemas into unapproved commercial AI models (e.g., public ChatGPT or Claude). Only use internal enterprise AI gateways configured with zero data retention guarantees.

---

## 4. Third-Party Non-Disclosure Agreements (NDAs)
- **Standard Corporate Template:** NexaTech maintains standard bilateral and unilateral NDA templates approved by Legal (`legal@nexatech.com`).
- **Review of Client NDAs:** If a client or vendor requires NexaTech to execute their customized NDA template, the agreement must be submitted to the Legal Desk in Jira (`LGL-CONTRACTS`) for redline review.
- **Signing Authority:** Only authorized corporate officers (Vice President and above) hold legal power of attorney to sign NDAs on behalf of NexaTech Solutions.

---

## 5. Post-Employment Confidentiality Survival
Your legal obligation to safeguard NexaTech and client trade secrets **survives indefinitely** following your separation from the company:
- You may not use confidential methodologies, client contact lists, or proprietary source code in subsequent employment.
- Upon departure, all physical notes, design sketches, and corporate files must be surrendered on or before your Last Working Day (LWD).

---

## 6. Penalties for Breach of Confidentiality
Breach of confidentiality represents gross misconduct triggering:
1. Immediate summary termination of employment without notice or severance pay.
2. Forfeiture of all unvested employee stock appreciation rights (SARs) and performance bonuses.
3. Pursuit of emergent civil injunctive relief and monetary damages in high court jurisdictions.
4. Criminal referral under Section 66 and 72 of the Information Technology Act, 2000.
"""

# 53. intellectual_property_patents.md (MEDIUM ~5,100 chars)
docs_batch6["intellectual_property_patents.md"] = """# NexaTech Solutions - Intellectual Property Assignment & Patent Incentive Policy
**Document ID:** NT-IP-POL-053  
**Version:** 3.2  
**Effective Date:** February 1, 2026  
**Owner:** Office of the Chief Technology Officer (OCTO) & Legal IP Cell  
**Classification:** Internal - Technical Staff  

---

## 1. Vision: Fostering Enterprise Innovation
NexaTech Solutions ("NexaTech") is dedicated to advancing cutting-edge distributed computing, generative AI systems, high-throughput cloud networking, and enterprise security architectures. We encourage engineers, architects, and researchers to invent novel technologies and actively reward intellectual property creation.

---

## 2. Intellectual Property Ownership and Assignment
- **Work Made for Hire:** In accordance with the Indian Copyright Act, 1957, and global patent conventions, all inventions, software code, algorithms, trade secrets, design patents, and utility patents conceived, developed, or reduced to practice by employees during their tenure—using company resources, time, or knowledge—are the exclusive intellectual property of NexaTech Solutions.
- **Client IP carve-outs:** Where software is developed specifically under client Master Service Agreements (MSAs) with "Work Made for Hire" ownership transfer clauses, IP rights are transferred to the client upon full payment of contractual fees.

---

## 3. Invention Disclosure & Patent Evaluation Workflow

```
[Engineer Conceives Novel Architecture/Algorithm]
                      │
                      ▼
[Submit Invention Disclosure Form (IDF) via NexaPortal]
                      │
                      ▼ (Within 14 Days)
[Patent Review Committee (PRC) Technical Evaluation]
                      │
                      ├─────────────────────────────────┐
                      ▼ (Approved for Filing)           ▼ (Rejected / Defensive Publication)
[External Patent Attorneys Draft Application]     [Feedback Shared / Published as Tech Blog]
                      │
                      ▼
[Filing with Indian Patent Office (IPO) & USPTO]
```

### 3.1 Invention Disclosure Form (IDF)
Engineers must document the novelty of their system, prior art differentiators, system flowcharts, and commercial applications on the IDF template available in Confluence.

### 3.2 Patent Review Committee (PRC)
The PRC comprises the Chief Technology Officer, two Principal Architects, and external IP legal counsel. The committee evaluates submissions bi-monthly based on patentability, market defensibility, and strategic relevance.

---

## 4. Inventor Recognition and Financial Incentive Schedule

To reward technical innovation, NexaTech provides substantial monetary bonuses to inventors:

| Patent Milestone | Monetary Incentive (Per Approved Patent) | Additional Recognition |
|---|---|---|
| **Milestone 1: PRC Acceptance & Attorney Drafting** | **₹15,000 INR** (shared equally among co-inventors) | Certificate of Invention from CTO |
| **Milestone 2: Official Filing with USPTO / IPO** | **₹35,000 INR** (shared equally among co-inventors) | Custom Engraved Crystal Patent Plaque |
| **Milestone 3: Official Patent Grant / Issuance** | **₹1,00,000 INR** (shared equally among co-inventors) | Annual CTO Innovation Award & Board Commendation |

---

## 5. Defensive Publications and Whitepapers
Inventions that offer competitive value but do not warrant multi-year patent prosecution may be selected for defensive publication on *NexaTech Technical Annals* or open-access research repositories (e.g., arXiv), with inventors awarded a **₹10,000 INR publication honorarium**.
"""

# 54. social_media_and_pr_policy.md (MEDIUM ~4,800 chars)
docs_batch6["social_media_and_pr_policy.md"] = """# NexaTech Solutions - Social Media, Public Relations & External Communications Policy
**Document ID:** NT-COM-POL-054  
**Version:** 3.3  
**Effective Date:** January 1, 2026  
**Owner:** Corporate Communications, Public Relations & Legal  
**Classification:** Internal - All Personnel  

---

## 1. Context and Objective
Digital professional networks like LinkedIn, X (Twitter), GitHub, and YouTube offer powerful opportunities for thought leadership and recruitment branding. However, unguarded commentary, inadvertent client data leaks, or uncoordinated media statements can inflict severe reputational damage.

This policy establishes guidelines for professional social media participation and governs official communications with press and media outlets.

---

## 2. Personal Social Media Guidelines

When posting on personal social media platforms:
- **Mandatory Personal Disclaimer:** If your profile identifies you as an employee of NexaTech Solutions, your bio or posts must state: *"Views and opinions expressed are solely my own and do not represent the official stance of my employer."*
- **Absolute Client Anonymity:** Never disclose client names, project codenames, client screenshots, or details of customer engagements unless the client has formally authorized a public joint case study. Saying *"Engineering a high-throughput payments engine for a tier-1 US retail bank"* is permissible; naming the specific bank without approval is a contractual violation.
- **Zero Hate Speech or Defamation:** Do not post defamatory, discriminatory, sexually explicit, politically inflammatory, or harassing content. Online misconduct reflecting poorly on the enterprise will trigger HR disciplinary inquiry.
- **Stock & Financial Speculation:** Never speculate publicly regarding NexaTech financial revenues, client stock fluctuations, acquisition rumors, or executive leadership transitions.

---

## 3. Official Public Relations & Media Inquiries
- **Designated Spokespersons Only:** No employee may speak to journalists, issue press statements, or accept broadcast interview invitations on behalf of NexaTech Solutions unless formally designated in writing as an Official Spokesperson by the Chief Executive Officer (CEO) or Head of Communications.
- **Routing Inbound Inquiries:** If contacted by a journalist, trade analyst, or news agency, politely decline immediate comment and forward the inquiry within 2 hours to `press@nexatech.com`.

---

## 4. Technical Blogging, Public Speaking & Conferences
NexaTech actively encourages engineers to speak at conferences (e.g., AWS re:Invent, KubeCon, PyCon) and author technical tutorials:
- **Pre-Publication Review:** Slides, whitepapers, or technical blog posts must be submitted to the Developer Relations Guild (`devrel@nexatech.com`) at least **5 business days** prior to presentation to ensure no proprietary source code or client confidential data is exposed.
- **Sponsorship:** NexaTech sponsors conference delegate passes and travel expenses for accepted speakers under the *Learning and Development Policy*.
"""

# 55. open_source_software_compliance.md (MEDIUM ~5,200 chars)
docs_batch6["open_source_software_compliance.md"] = """# NexaTech Solutions - Open Source Software (OSS) Governance & Compliance Policy
**Document ID:** NT-ENG-POL-055  
**Version:** 3.4  
**Effective Date:** February 1, 2026  
**Owner:** Open Source Review Board (OSRB) & Legal IP Team  
**Classification:** Internal - Engineering Staff  

---

## 1. Philosophy: Responsible Open Source Stewardship
Open source software powers modern digital engineering. NexaTech actively leverages, champions, and contributes to the global open-source ecosystem. However, unvetted open-source components carry severe legal risks—including copyleft contamination (viral GPL licenses forcing proprietary code disclosure), patent infringement, and software supply chain vulnerabilities.

---

## 2. Open Source License Categorization & Permissibility

NexaTech categorizes open-source software licenses into three distinct compliance tiers:

| License Tier | Representative Licenses | Corporate Stance | Conditions & Governance |
|---|---|---|---|
| **Tier 1: Permissive** | MIT, Apache 2.0, BSD 2-Clause / 3-Clause, ISC | **Pre-Approved (Adopt)** | Permitted in all client and internal software builds. Attribution notices and copyright headers must be preserved. |
| **Tier 2: Weak Copyleft** | LGPL 2.1 / 3.0, MPL 2.0, EPL 2.0, CDDL | **Conditional Approval** | Permitted ONLY if consumed as dynamically linked libraries (`.so`, `.dll`, or standalone packages). Must NOT be statically compiled with proprietary core code. |
| **Tier 3: Strong Copyleft / Viral** | GPL v2 / v3, AGPL v3, SSPL | **Strictly Prohibited** in client proprietary deliverables | Forbidden in client software unless the client explicitly mandates GPL in writing. Consuming AGPL or GPL in proprietary SaaS solutions risks forced open-sourcing of all surrounding code. |

---

## 3. Automated Dependency Scanning in CI/CD
- **Snyk & Mend (WhiteSource) Scans:** Every repository must execute automated dependency license audits on each GitHub pull request.
- **Build Gating:** Any pull request introducing a package with an unauthorized copyleft license (AGPL, GPL, SSPL) or an unclassified license is automatically blocked from merging.

---

## 4. Open Source Review Board (OSRB) Exemption Workflow
If an engineering team requires a library governed by a conditional or restricted license:
1. Submit an OSRB Requisition Ticket on Jira (`OSRB-REQ`) detailing: package name, version, intended architecture linkage (dynamic vs. static), and commercial alternative analysis.
2. The OSRB (comprising the Lead Architect and IP Legal Counsel) reviews the petition within **5 business days**.

---

## 5. Contributing Back to Open Source
NexaTech encourages contributions to community projects:
- **Bugfixes & Minor Patches:** Engineers may submit bug fixes, documentation updates, or minor performance patches to public OSS projects using their corporate email.
- **Releasing New NexaTech Open Source Projects:** Releasing a new standalone framework, library, or tool under the `github.com/nexatech-solutions` open-source organization requires formal clearance from the CTO and OSRB.
"""

# 56. api_design_standards.md (MEDIUM ~5,400 chars)
docs_batch6["api_design_standards.md"] = """# NexaTech Solutions - Enterprise RESTful & GraphQL API Design Standards
**Document ID:** NT-ENG-STD-056  
**Version:** 4.2  
**Effective Date:** February 1, 2026  
**Owner:** Architecture Guild & API Center of Excellence (CoE)  
**Classification:** Internal - Technical Staff  

---

## 1. Strategic Principles of API Design
At NexaTech, APIs are first-class software products. Whether building public developer platforms or internal microservices, all APIs must be predictable, resilient, secure, self-documenting, and backwards-compatible.

---

## 2. API Design & Resource Modeling Standards

### 2.1 URI Naming Conventions
- **Nouns, Not Verbs:** Use plural nouns to represent resource collections. Verbs must never appear in URIs:
  - *Correct:* `GET /api/v1/customers`, `POST /api/v1/orders`
  - *Incorrect:* `GET /api/v1/getCustomers`, `POST /api/v1/createOrder`
- **Kebab-Case:** Use lowercase hyphenated naming for multi-word paths:
  - *Correct:* `/api/v1/payment-transactions`
  - *Incorrect:* `/api/v1/paymentTransactions`, `/api/v1/payment_transactions`
- **Sub-Resource Hierarchies:** Model parent-child relationships logically:
  - `GET /api/v1/customers/{customerId}/invoices`

### 2.2 Standard HTTP Verbs & Idempotency
- `GET`: Read resource(s). Must be safe and strictly idempotent.
- `POST`: Create a new resource. Non-idempotent.
- `PUT`: Complete resource replacement. Idempotent.
- `PATCH`: Partial resource mutation. Idempotent where possible.
- `DELETE`: Remove a resource. Idempotent.

### 2.3 API Versioning Strategy
- NexaTech enforces **URI Path Versioning**: `/api/v1/`, `/api/v2/`.
- Breaking changes (field removals, type modifications, mandatory parameter additions) mandate an increment in major version. Minor non-breaking changes (new optional fields) must maintain backwards compatibility.
- Older major versions must be supported for a minimum of **12 months** following public deprecation notices.

---

## 3. Standardized Error Handling (RFC 7807 Problem Details)
All API error responses must adhere strictly to the **RFC 7807 Problem Details** JSON specification:

```json
{
  "type": "https://api.nexatech.com/errors/invalid-resource-state",
  "title": "Invalid Payment State",
  "status": 422,
  "detail": "Invoice INV-9044 cannot be settled because it has already been voided.",
  "instance": "/api/v1/invoices/INV-9044/settlement",
  "code": "ERR_INVOICE_ALREADY_VOIDED",
  "timestamp": "2026-02-15T10:32:00Z",
  "traceId": "77325763-db54-4b4b-8b3c-8aeb1e3cca93"
}
```

---

## 4. Pagination, Filtering, and Sorting
- **Cursor-Based Pagination:** Mandatory for datasets exceeding 1,000 records:
  - `GET /api/v1/audit-logs?cursor=dXNlcl8xMjM=&limit=50`
- **Offset-Based Pagination:** Allowed for small, static datasets:
  - `GET /api/v1/products?page=2&page_size=25`
- Response payloads must include pagination metadata (`has_more`, `next_cursor`, `total_count`).

---

## 5. Security & Rate Limiting Gateways
- All external API traffic must terminate at our Kong / AWS API Gateway layer.
- **Authentication:** OAuth 2.0 with JSON Web Tokens (JWT) signed using RS256 algorithms.
- **Rate Limiting:** Standard consumer tiers enforce 100 requests per minute per IP; authenticated client tiers enforce 1,000 requests per minute with Redis sliding-window token buckets.
"""

# 57. git_branching_pull_request_policy.md (MEDIUM ~5,000 chars)
docs_batch6["git_branching_pull_request_policy.md"] = """# NexaTech Solutions - Git Branching, Code Review & Pull Request Policy
**Document ID:** NT-ENG-POL-057  
**Version:** 3.5  
**Effective Date:** February 1, 2026  
**Owner:** Engineering Excellence Guild & DevOps Office  
**Classification:** Internal - Technical Staff  

---

## 1. Philosophy: Clean Version Control
Source code history is an immutable technical audit log. A disciplined Git workflow ensures code traceability, seamless rollbacks, and psychological safety for developers deploying to production.

---

## 2. Trunk-Based Development with Short-Lived Branches
NexaTech mandates **Trunk-Based Development**:
- **Trunk (`main` branch):** Always deployable and protected. Direct commits and history rewrites (`git push --force`) are disabled by GitHub branch protection rules.
- **Branch Lifespan:** Feature branches must live no longer than **48 to 72 hours**. Long-lived branches spanning multiple weeks are forbidden; complex features must be broken into incremental sub-tasks guarded by Feature Flags (LaunchDarkly).

---

## 3. Branch Naming Standards
Branches must reference an active Jira ticket identifier:
- `feat/NEXA-3401-add-sso-saml-login`
- `fix/NEXA-4120-null-pointer-invoice-calc`
- `refactor/NEXA-2209-migrate-orm-to-sqlalchemy2`
- `chore/NEXA-5501-upgrade-spring-boot-3-4`

---

## 4. Pull Request (PR) Requirements & Quality Gates
Before any PR can be merged into `main`, it must satisfy four mandatory criteria:
1. **Peer Review Approvals:** At least **two approving reviews** from engineering peers, including at least one Senior SDE or Technical Lead.
2. **Automated CI Checks:** GitHub Actions pipeline must complete 100% green:
   - Unit test code coverage >= 80% on new code.
   - SonarQube quality gate passing with zero new security hotspots.
   - Snyk dependency vulnerability check clean.
3. **Conventional Commits:** Pull request titles and squash commit messages must follow the Conventional Commits specification (`feat:`, `fix:`, `docs:`, `perf:`).
4. **Merge Method:** Repositories enforce **Squash and Merge** by default to ensure clean, atomic commit histories on the trunk branch.

---

## 5. Code Review Etiquette & SLAs
- **Review Turnaround SLA:** Reviewers must review assigned PRs within **24 business hours**.
- **Constructive Tone:** Code reviews must be empathetic and objective. Distinguish between blockers (*"This causes a race condition under concurrency"*) and non-blocking nitpicks (*"Nit: Could consider extracting this helper"*).
"""

# 58. ci_cd_deployment_pipeline.md (MEDIUM ~5,100 chars)
docs_batch6["ci_cd_deployment_pipeline.md"] = """# NexaTech Solutions - Continuous Integration & Continuous Delivery (CI/CD) Standards
**Document ID:** NT-OPS-STD-058  
**Version:** 4.1  
**Effective Date:** February 1, 2026  
**Owner:** DevOps & Platform Engineering Guild  
**Classification:** Internal - Technical Operations  

---

## 1. Overview and Core Objectives
Continuous Delivery enables rapid, safe, and automated software delivery. At NexaTech, every code commit to `main` triggers automated testing, container packaging, security validation, and progressive deployment without manual human bottlenecks.

---

## 2. Standard CI/CD Architecture

```
[Git Commit to Feature Branch]
               │
               ▼ (GitHub Actions CI)
[Build, Unit Tests, SonarQube, Snyk Scan, Container Image Build]
               │
               ▼ (PR Approved & Merged into Main)
[Image Tagged, Signed with Cosign, Pushed to ECR]
               │
               ▼ (ArgoCD GitOps Synchronizer)
[Staging Deployment & Automated Smoke Tests]
               │
               ▼ (Automated Canary Analysis)
[Production Progressive Canary Rollout (10% -> 25% -> 50% -> 100%)]
```

---

## 3. Progressive Delivery & Canary Deployments
- Production deployments must leverage **Argo Rollouts** for canary releases.
- **Canary Steps:** 10% traffic for 15 minutes $\rightarrow$ 25% for 30 minutes $\rightarrow$ 50% for 30 minutes $\rightarrow$ 100% full promotion.
- **Automated Rollback Criteria:** If HTTP 5xx error rate exceeds **1.0%** or P95 latency spikes by more than **25%** over baseline during any canary phase, Argo Rollouts aborts immediately and reverts traffic to stable replica sets within 30 seconds.

---

## 4. Container Security & Supply Chain Integrity
- **Base Images:** All container images must inherit from certified *NexaTech Golden Base Images* maintained by Platform Engineering (e.g., `distroless` or `alpine` hardened images).
- **Non-Root Execution:** Containers must run as an unprivileged non-root user (`USER 1001`).
- **Image Signing:** Container images must be cryptographically signed using **Cosign / Sigstore**; Kubernetes Kyverno admission controllers reject any pod image lacking a valid cryptographic signature.
"""

# 59. database_migration_policy.md (MEDIUM ~4,900 chars)
docs_batch6["database_migration_policy.md"] = """# NexaTech Solutions - Database Schema Evolution & Zero-Downtime Migration Policy
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
"""

# 60. observability_logging_monitoring.md (MEDIUM ~5,300 chars)
docs_batch6["observability_logging_monitoring.md"] = """# NexaTech Solutions - Enterprise Observability, Logging & Telemetry Standards
**Document ID:** NT-OPS-STD-060  
**Version:** 4.0  
**Effective Date:** February 1, 2026  
**Owner:** SRE Guild & Observability Center of Excellence  
**Classification:** Internal - Technical Staff  

---

## 1. The Three Pillars of Observability
NexaTech systems process millions of critical client transactions every day. Robust observability is vital for fast incident detection, proactive performance optimization, and SLA verification.

We build observability on the three open standards pillars: **Metrics**, **Structured Logs**, and **Distributed Traces**, unified via the OpenTelemetry (OTel) framework.

---

## 2. Structured JSON Logging Standards

All application logs must be emitted as structured single-line JSON to standard output (`stdout`):

```json
{
  "timestamp": "2026-02-15T10:45:12.304Z",
  "level": "INFO",
  "service": "payments-settlement-service",
  "environment": "production",
  "traceId": "4bf92f3577b34da6a3ce929d0e0e4736",
  "spanId": "00f067aa0ba902b7",
  "userId": "usr_99812",
  "message": "Payment transaction processed successfully",
  "http": {
    "method": "POST",
    "route": "/api/v1/payments",
    "status_code": 201,
    "duration_ms": 42.5
  }
}
```

### 2.1 Sensitive Data Masking (Zero-PII Logging Rule)
Application logs must NEVER contain:
- Passwords, API tokens, JWT secrets, or cryptographic keys.
- Credit card PANs, CVV codes, or bank account numbers.
- Aadhaar, SSN, or national identification credentials.
- Protected Health Information (PHI).
*Violations will result in automated SIEM alerts and immediate code revision tickets.*

---

## 3. Metrics Collection & Prometheus Standards
- Services must expose a `/metrics` endpoint formatted for Prometheus scraping.
- Standard Golden Signals must be instrumented for every microservice:
  1. **Latency:** Distribution of request service times (P50, P90, P99).
  2. **Traffic:** Demand placed on the service (Requests per second - RPS).
  3. **Errors:** Rate of failed requests (HTTP 5xx / application exceptions).
  4. **Saturation:** Resource utilization (CPU, memory, database connection pool exhaustion).

---

## 4. Distributed Tracing with OpenTelemetry
- Every inbound HTTP or Kafka event must initialize or propagate a W3C Trace Context header (`traceparent`).
- Spans must capture major database queries, external REST client calls, and cache interactions to enable sub-second latency bottleneck identification across microservices.
"""

for filename, content in docs_batch6.items():
    file_path = DOCS_DIR / filename
    file_path.write_text(content.strip(), encoding="utf-8")
    print(f"Written: {filename} ({len(content)} chars)")

print("Batch 6 Complete: 10 files written.")
