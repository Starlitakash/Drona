# NexaTech Solutions - Bring Your Own Device (BYOD) & Mobile Security Policy
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
