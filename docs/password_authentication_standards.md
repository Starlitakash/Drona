# NexaTech Solutions - Enterprise Password & Multi-Factor Authentication Standards
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
