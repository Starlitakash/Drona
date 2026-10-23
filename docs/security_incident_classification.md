# NexaTech Solutions - Cyber Security Incident Classification & Containment Guide
**Document ID:** NT-SEC-GDE-061  
**Version:** 4.1  
**Effective Date:** February 1, 2026  
**Owner:** Cyber Defense Center (CDC) & Incident Handling Team  
**Classification:** Confidential - Technical Security  

---

## 1. Purpose and Operational Philosophy
NexaTech Solutions operates a 24/7/365 Cyber Defense Center (CDC). Prompt, standardized incident classification ensures appropriate technical resources, forensic specialists, executive notification chains, and statutory regulatory authorities are engaged without delay.

This guide defines incident severity tiers, containment runbooks, and statutory reporting obligations adhering to NIST SP 800-61 Rev. 2 and Indian Computer Emergency Response Team (CERT-In) guidelines.

---

## 2. Cyber Incident Severity Classification Matrix

| Incident Severity | Operational Definition & Criteria | CDC Initial Response SLA | Mandatory Notification Window | Escalation Authorities |
|---|---|---|---|---|
| **SEV-1 (Critical)** | Active ransomware encryption; exfiltration of customer PII / financial records; root compromise of AWS production master organization; uncontained malware worm spreading across corporate LAN. | **15 Minutes** | **1 Hour Internal / 6 Hours Regulatory** | CISO, CEO, Legal Counsel, Affected Client CISOs, CERT-In |
| **SEV-2 (High)** | Compromise of privileged employee account; malware detected on server endpoint; isolated DDoS attack causing customer degradation; unauthorized production database read query. | **30 Minutes** | **4 Hours** | CISO, Practice Delivery Head, CDC Lead |
| **SEV-3 (Medium)** | Credential phishing campaign targeting multiple staff; multiple failed brute-force attacks; unauthorized software installation on laptop. | **2 Hours** | **12 Hours** | Senior Security Analyst, IT Helpdesk Lead |
| **SEV-4 (Low)** | Isolated spam email report; port scanning from internet without breach; minor security false-positive alert. | **8 Hours** | Next Business Day | Level 1 Security Operations Analyst |

---

## 3. Statutory Regulatory Reporting (CERT-In Mandate)
In compliance with the CERT-In Directions under Section 70B of the Information Technology Act:
- **Mandatory 6-Hour Reporting:** Any cyber incident involving unauthorized access of IT systems, ransomware, identity theft, or data exfiltration must be formally reported to CERT-In (`incident@cert-in.org.in`) within **6 hours** of confirmation.
- The CISO and Legal Counsel coordinate all regulatory filings; individual employees are strictly prohibited from submitting external filings independently.

---

## 4. Immediate Containment & Forensic Runbooks
During an active security breach, investigators must preserve digital evidence for court admissibility:
1. **Endpoint Isolation:** Isolate compromised laptops or virtual machines from the network via CrowdStrike Falcon Sensor Network Containment. Do NOT power off or reboot the machine (preserves volatile RAM).
2. **Volatile Memory Capture:** Capture RAM dumps using approved forensic tools (WinPmem or LiME) before disk imaging.
3. **Credential Invalidation:** Revoke all active Okta sessions, invalidate AWS STS temporary credentials, and force password resets via Active Directory.
4. **Forensic Chain of Custody:** Document every forensic artifact with SHA-256 cryptographic hashes and maintain signed custody transfer forms.