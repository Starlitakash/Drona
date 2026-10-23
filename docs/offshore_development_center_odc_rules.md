# NexaTech Solutions - Dedicated Offshore Development Center (ODC) Security Regulations
**Document ID:** NT-SEC-POL-096  
**Version:** 4.1  
**Effective Date:** February 1, 2026  
**Owner:** Cyber Defense Center & Enterprise Facility Security  
**Classification:** Confidential - Restricted Operations  

---

## 1. Purpose and Contractual Context
Certain enterprise clients in banking, capital markets, defense, and healthcare mandate physically and logically isolated workspaces known as Offshore Development Centers (ODCs). This policy establishes strict security perimeters governing dedicated client ODCs.

---

## 2. Physical Security Perimeters
- **Biometric Turnstiles:** Access to ODC bays is restricted strictly to assigned, client-cleared project personnel via dual-factor biometric access (fingerprint/facial recognition + RFID badge).
- **Prohibited Devices:** Personal mobile phones, smartwatches, digital cameras, recording devices, USB flash drives, and personal laptops are strictly prohibited inside the ODC bay. All personal electronics must be deposited in assigned biometric lockers outside the bay entrance.
- **CCTV Surveillance:** 100% of ODC workspaces are monitored by 4K high-definition CCTV cameras with footage securely archived for **90 calendar days** for client compliance audits.

---

## 3. Logical Network & Infrastructure Isolation
- **Dedicated VLANs & Firewalls:** ODC networks operate on air-gapped or dedicated VLANs with zero route to other NexaTech internal networks.
- **Zero Internet Access:** Workstations within high-security ODCs are restricted to whitelisted client IP subnets via dedicated AWS DirectConnect or Azure ExpressRoute circuits. Public internet browsing is completely disabled.
- **Client Security Audits:** ODC facilities undergo quarterly unannounced physical and logical audits by client security delegations.

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
