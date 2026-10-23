# NexaTech Solutions - IT Service Desk & Operations Support Onboarding Guide
**Document ID:** NT-OPS-GDE-030  
**Version:** 3.2  
**Effective Date:** February 1, 2026  
**Owner:** IT Infrastructure, Service Operations & Facilities  
**Classification:** Internal - IT Operations Staff  

---

## 1. Welcome to IT Service Operations
The IT Operations and Service Desk team maintains the digital backbone of NexaTech Solutions. We support over 2,200 active workstations, corporate networks, cloud access privileges, and unified communication systems across our delivery centers.

This playbook outlines ticket management queues, Service Level Agreements (SLAs), device imaging workflows, and escalation paths.

---

## 2. IT Service Management (ITSM) Tooling
- **Jira Service Management (JSM):** Central ticketing platform. All employee requests must have an associated ticket number under projects `IT-SERV` (General IT), `IT-CAPEX` (Hardware Procurement), or `SEC-OPS` (Security Access).
- **Microsoft Intune & Jamf Pro:** Enterprise device management suites used for automated zero-touch workstation deployment, BitLocker/FileVault key escrow, and remote wipe.
- **Active Directory & Azure AD (Entra ID):** User identity management, security group memberships, and distribution list maintenance.
- **Lansweeper:** Real-time IT asset discovery, software inventory scanning, and warranty tracking.

---

## 3. Service Level Agreements (SLAs) Matrix
All IT support personnel must manage incoming queues to achieve strict contractual SLAs:

| Priority | Ticket Classification | Response SLA | Resolution SLA | Escalation Target |
|---|---|---|---|---|
| **P1 - Urgent** | Whole floor network outage; video conference failure in Executive Boardroom during client pitch; CEO/C-suite hardware failure. | **15 Minutes** | **2 Hours** | IT Operations Director (+91-98450-99887) |
| **P2 - High** | Developer workstation boot failure; lost access badge; primary Slack/Email SSO failure for multiple users. | **30 Minutes** | **4 Hours** | Senior Systems Engineer |
| **P3 - Medium** | Software license provisioning (JetBrains, Postman); external monitor requisition; password reset unlock. | **2 Hours** | **8 Hours** | Level 2 Service Desk Specialist |
| **P4 - Low** | General IT query; peripheral replacement cable request; ergonomic equipment setup assistance. | **4 Hours** | **24 Hours** | Level 1 Service Desk Associate |

---

## 4. Standard Workstation Imaging & Deployment SOP
When staging a new MacBook Pro or Dell XPS workstation for incoming joiners:
1. Ensure the device serial number is enrolled in Apple Business Manager (ABM) or Windows Autopilot.
2. Power on the device and initiate corporate zero-touch enrollment connected to `NexaCorp-Secure` staging VLAN.
3. Verify mandatory base agents:
   - CrowdStrike Falcon Sensor (confirm sensor connected in CDC console).
   - Microsoft Intune / Jamf Pro MDM profile verified and active.
   - BitLocker / FileVault 2 encryption enabled (AES-256 bit) with recovery key escrowed.
   - Pre-installed productivity suite: Chrome, Slack, Zoom, Office 365.
4. Affix tamper-evident asset barcode tag on device chassis and register barcode in Lansweeper.