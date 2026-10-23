# NexaTech Solutions - Secure Coding & Application Security Standards
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
