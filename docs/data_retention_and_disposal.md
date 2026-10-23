# NexaTech Solutions - Corporate Data Retention, Archival & Disposal Policy
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