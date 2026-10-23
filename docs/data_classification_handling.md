# NexaTech Solutions - Enterprise Data Classification & Handling Standard
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
