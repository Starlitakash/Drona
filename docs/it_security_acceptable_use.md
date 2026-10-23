# NexaTech Solutions - Information Technology Security & Acceptable Use Policy
**Document ID:** NT-SEC-POL-002  
**Version:** 5.1  
**Effective Date:** February 15, 2026  
**Owner:** Chief Information Security Officer (CISO) & Cyber Defense Center  
**Classification:** Confidential - Internal Compliance Mandatory  

---

## 1. Purpose and Scope
NexaTech Solutions ("NexaTech") handles proprietary source code, intellectual property, enterprise customer architectures, and protected data governed by SOC 2 Type II, ISO/IEC 27001:2022, and GDPR. This policy establishes binding standards for computing assets, identity management, peripheral usage, cloud governance, and network security.

This policy applies to all full-time employees, contractors, interns, vendors, and third-party partners accessing NexaTech corporate networks, AWS/Azure production environments, hardware endpoints, email domains, and Slack workspaces.

---

## 2. Identity and Access Management (IAM)

### 2.1 Password Complexity Standards
All user credentials across Active Directory, Okta SSO, Google Workspace, GitHub Enterprise, and AWS IAM must conform to strict complexity rules:
- **Minimum Length:** 14 characters.
- **Character Composition:** Must include at least 1 uppercase letter, 1 lowercase letter, 1 numerical digit, and 1 non-alphanumeric special character (`!@#$%^&*()-_+=`).
- **Rotation Interval:** Mandatory rotation every 90 days. Systems enforce a history constraint preventing reuse of the last 6 previous passwords.
- **Lockout Mechanism:** Accounts lock automatically after 5 consecutive failed login attempts. Unlocking requires administrator verification via IT Service Desk (`ithelpdesk@nexatech.com` or extension 4357).
- **Prohibited Patterns:** Passwords cannot contain personal names, company names ("NexaTech", "Bengaluru"), sequential digits ("123456"), or standard dictionary terms.

### 2.2 Multi-Factor Authentication (MFA)
- MFA is universally mandatory across all corporate accounts, VPN gateways, Slack, and cloud management consoles.
- Approved MFA Authenticators: Okta Verify (Push with Number Matching), Microsoft Authenticator, and hardware YubiKeys (Series 5 FIPS).
- SMS-based or voice-call MFA is strictly deprecated and disabled due to SIM-swapping vulnerabilities.
- Biometric authentication (TouchID, Windows Hello for Business) is enabled as an approved secondary credential for local device unlocks.

---

## 3. Endpoint Security and Hardware Protection

### 3.1 Device Encryption and MDM Enrollment
- Every laptop supplied by NexaTech must run enterprise Mobile Device Management (Microsoft Intune for Windows; Jamf Pro for macOS).
- Full Disk Encryption (BitLocker with XTS-AES 256-bit on Windows; FileVault 2 on macOS) is configured at hardware provisioning. Recovery escrow keys are centrally stored within secure Azure Key Vaults.
- Disabling, modifying, or bypassing MDM profiles, local firewalls, or disk encryption constitutes a critical security infraction resulting in immediate disciplinary review.

### 3.2 Endpoint Detection & Response (EDR)
- All endpoints must continuously execute CrowdStrike Falcon Sensor.
- Real-time telemetry is ingested into our Cyber Defense Center (CDC) SIEM.
- Endpoints showing disabled EDR agents or out-of-date signatures (>48 hours offline) are quarantined automatically from the corporate Wi-Fi and VPN.

### 3.3 Peripheral Storage and Removable Media Lockdown
- All external USB mass storage devices (flash drives, external hard drives, SD cards) are blocked at the kernel level by endpoint policies.
- If legitimate business needs require external storage (e.g., forensic disk imaging, hardware firmware flashes), a formal exemption request must be submitted via Jira ticket queue `SEC-OPS` and approved by the CISO.
- Approved USB devices must be company-procured, hardware-encrypted (Apricorn Aegis or Kingston IronKey), and scanned by the CDC prior to insertion.

---

## 4. Network and Cloud Environment Security

### 4.1 Corporate Wi-Fi Networks
NexaTech facilities host three distinct wireless SSIDs:
1. `NexaCorp-Secure`: 802.1X certificate-based WPA3 Enterprise network for corporate-managed laptops.
2. `Nexa-BYOD`: Isolated wireless subnet for employee personal smartphones. Bandwidth-throttled with zero access to internal subnets or source repositories.
3. `Nexa-Guest`: Captive-portal network for registered clients and visitors. Valid for 12 hours with client escort confirmation.

### 4.2 Remote Access VPN
- All remote work connections to internal corporate networks, staging clusters, and database read-replicas must traverse NexaTech GlobalProtect / WireGuard Zero-Trust Network Access (ZTNA) gateways.
- Split-tunneling is disabled on production bastion gateways.
- Remote connections terminate after 8 hours of continuous session time, or 30 minutes of idle time, requiring re-authentication via MFA.

### 4.3 Cloud Production Access & Principle of Least Privilege
- Direct SSH/RDP to production AWS EC2 or Azure VMs is prohibited. All administrative shell sessions must route through AWS Systems Manager (SSM) Session Manager or Teleport Bastion with session recording.
- Permanent root or administrative cloud credentials are strictly prohibited. Production privilege elevation requires just-in-time (JIT) access requests approved by the Engineering Lead and CloudOps via Slack `#cloud-access-approvals`. Maximum session lease is 4 hours.

---

## 5. Software Usage and Shadow IT

### 5.1 Approved vs. Unapproved Software
- Users may install software exclusively from the pre-approved *NexaTech Self-Service Portal* (Intune Company Portal / Jamf Self Service).
- Freeware, torrent clients, peer-to-peer utilities, commercial IDE plugins without license vetting, or unvetted browser extensions are blocked.
- Software requests for developer productivity (e.g., specific Docker extensions, JetBrains plugins) require approval via Jira queue `IT-SERV`.

### 5.2 Generative AI and Public LLM Usage
- Employees may not upload proprietary NexaTech source code, customer datasets, unannounced architecture diagrams, API keys, or personally identifiable information (PII) to public generative AI platforms (e.g., public ChatGPT, Claude, Gemini, Copilot).
- Use of enterprise-licensed tools (NexaTech GitHub Copilot Enterprise and internal enterprise LLM gateways) is governed by `ai_tooling_copilot_usage_policy.md`. All prompts must adhere to enterprise data boundary covenants.

---

## 6. Email, Phishing, and Social Engineering

### 6.1 Email Security Guidelines
- Be vigilant of spear-phishing, credential harvesting, and CEO fraud attempts. NexaTech executives will never request gift card purchases, immediate fund wire transfers, or sensitive password disclosures via email or Slack.
- Suspicious emails must be reported immediately using the *Report Phishing (PhishER)* button in Outlook or forwarded to `phishing@nexatech.com`.

### 6.2 Simulated Phishing Exercises
The Cyber Defense Center conducts unannounced monthly simulated phishing campaigns across all departments.
- Failure 1 (Entering credentials): Mandatory 30-minute interactive Security Awareness refresher module completed within 7 calendar days.
- Failure 2 within 6 months: Notification sent to Reporting Manager and Practice Head; mandatory 1-on-1 coaching with a CDC Security Analyst.
- Failure 3 within 12 months: Escalation to Department Head, formal written reprimand, and temporary suspension of remote access privileges.

---

## 7. Clean Desk and Physical Workspace Security
- Unattended workstations must be locked instantly. Set screensavers to lock automatically after 3 minutes of inactivity.
- Physical documents, customer contracts, design sketches, or authentication tokens must be locked in personal credenzas or pedestals when departing desks.
- Whiteboards in meeting rooms and collaborative spaces must be thoroughly erased following strategic, architecture, or customer-facing sessions.
- Tailgating at facility turnstiles or biometric access doors is strictly prohibited. Every employee must tap their individual badge upon entry and exit.

---

## 8. Incident Reporting and Escalation SLA

Any suspected security anomaly—including lost laptops, stolen access badges, ransomware alerts, accidental credential commits to public GitHub, or abnormal data egress—must be reported immediately.

### Severity Levels and Notification Matrix:
| Severity Level | Definition | Mandatory SLA | Escalation Target |
|---|---|---|---|
| **SEV-1 (Critical)** | Active data exfiltration, production ransomware, exposed root credentials, verified breach of customer PII | 15 Minutes | CISO, CDC Incident Commander, Legal Counsel (`infosec@nexatech.com`, +91-80-6922-0911) |
| **SEV-2 (High)** | Lost/stolen corporate laptop, compromised employee credentials, malware on corporate subnet | 1 Hour | CDC Lead, IT Service Desk (`infosec@nexatech.com`) |
| **SEV-3 (Medium)** | Phishing campaign detected internally, suspicious login alerts from unauthorized geographies | 4 Hours | CDC Security Analysts |
| **SEV-4 (Low)** | General policy query, unapproved software request, minor false-positive alert | 24 Hours | IT Helpdesk (`ithelpdesk@nexatech.com`) |

---

## 9. Compliance Enforcement and Disciplinary Actions
Non-compliance with this policy threatens the security accreditation, customer trust, and regulatory compliance of NexaTech Solutions. Violations are investigated by the Disciplinary Action Committee (comprising InfoSec, Legal, and People Operations) and may result in:
1. Written reprimand placed in employee permanent personnel file.
2. Immediate revocation of network, cloud, and building access credentials.
3. Suspension without pay pending inquiry.
4. Summary termination of employment for gross misconduct.
5. Criminal referral or civil litigation under the Information Technology Act, 2000 and the Digital Personal Data Protection (DPDP) Act, 2023.