# NexaTech Solutions - Open Source Software (OSS) Governance & Compliance Policy
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