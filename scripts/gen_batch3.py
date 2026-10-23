import os
from pathlib import Path

DOCS_DIR = Path("docs")
DOCS_DIR.mkdir(parents=True, exist_ok=True)

docs_batch3 = {}

# 21. work_from_home_hybrid_policy.md (MEDIUM ~5,200 chars)
docs_batch3["work_from_home_hybrid_policy.md"] = """# NexaTech Solutions - Hybrid Workplace & Remote Operations Policy
**Document ID:** NT-OPS-POL-021  
**Version:** 4.0  
**Effective Date:** January 1, 2026  
**Owner:** Workplace Solutions & People Operations  
**Classification:** Internal - All Employees  

---

## 1. Context and Operational Philosophy
NexaTech Solutions ("NexaTech") operates under a structured hybrid model balancing the agility of remote work with the undeniable creative and collaborative advantages of co-located engineering and client design sprints. This policy governs eligibility, attendance cadences, communication standards, and compliance rules for all employees.

---

## 2. The 3+2 Hybrid Model Architecture

### 2.1 Standard Office Roster
All regular full-time and contract personnel assigned to delivery centers (Bengaluru, Hyderabad, Pune, Gurugram) must adhere to the **3+2 working rhythm**:
- **3 Days In-Office:** Two mandatory organization/business unit anchor days (Tuesdays and Thursdays) and one floating team anchor day determined by your Delivery Lead or Project Manager.
- **2 Days Remote:** Up to two days per week working from your registered domestic home address.
- **Client Project Overrides:** Specific client Master Service Agreements (MSAs)—such as defense, banking, or healthcare compliance engagements operating inside dedicated Offshore Development Centers (ODCs)—may mandate 100% on-site presence. Project contracts supersede standard corporate hybrid permissions.

### 2.2 Core Hours & Real-Time Availability
Regardless of physical work location, team members must maintain active availability during **Core Business Hours (10:00 AM to 4:00 PM IST)**:
- Respond to direct Slack inquiries and mentions within a reasonable window (maximum 45 minutes).
- Attend scheduled sprint ceremonies, retrospectives, and client syncs with audio and video enabled unless technical constraints prevent it.
- Calendar blocks: Document focus work, client meetings, and meal breaks transparently on Google Calendar.

---

## 3. Remote Work Infrastructure & Security Prerequisites
To maintain eligibility for remote days, employees must maintain:
- **Broadband Connectivity:** Stable home broadband internet connection with a minimum download and upload speed of **50 Mbps**. Mobile hotspot tethering is permissible only as an emergency backup.
- **Power Backup:** Uninterruptible Power Supply (UPS) or home inverter ensuring continuous workstation and router power during local municipal power disruptions.
- **Physical Security:** Workstations must be located in private, secure residential environments. Working from public coffee shops, airport lobbies, or communal spaces without privacy screens is prohibited when handling client source code or PII.

---

## 4. Exceptions and Extended Remote Work (Work from Anywhere)
- **Medical / Temporary Hardship:** An employee requiring temporary 100% remote work due to post-operative recovery, pregnancy, or family medical emergencies must submit a formal medical exception request on NexaPortal backed by medical certification. Requires joint sign-off from Reporting Manager and HRBP (maximum approval 60 calendar days per request).
- **Relocation Across States:** Employees may not relocate to another state or city without formal People Operations approval, as state-level tax filings (Professional Tax) and labor compliance must be restructured.
- **Working from Outside India:** Working remotely from outside India is strictly prohibited due to international permanent establishment tax liabilities, export control laws, and cross-border data transfer regulations.

---

## 5. Compliance Monitoring and Non-Adherence
- Attendance is recorded via electronic turnstile badge swipes on campus and correlated with NexaPortal hybrid logs.
- Consistent failure to satisfy the 3-day in-office requirement without prior written approval triggers:
  1. *First Month:* Formal automated notification to employee and Reporting Manager.
  2. *Second Consecutive Month:* Meeting with HRBP; forfeiture of remote work privileges for 90 days.
  3. *Continued Non-Adherence:* Formal disciplinary warning impacting the H2 performance appraisal rating.
"""

# 22. remote_work_ergonomics_stipend.md (MEDIUM ~4,600 chars)
docs_batch3["remote_work_ergonomics_stipend.md"] = """# NexaTech Solutions - Remote Workspace Ergonomics & Internet Subsidy Policy
**Document ID:** NT-FIN-POL-022  
**Version:** 3.1  
**Effective Date:** January 1, 2026  
**Owner:** Total Rewards, Finance & Environmental Health and Safety (EHS)  
**Classification:** Internal - All Confirmed Staff  

---

## 1. Overview and Employee Well-Being
Prolonged remote engineering work requires proper posture, lumbar support, and adequate lighting to prevent repetitive strain injuries (RSI), musculoskeletal disorders, and eye fatigue. NexaTech provides financial subsidies to ensure home workstations meet certified ergonomic standards.

---

## 2. One-Time Home Ergonomic Setup Allowance

### 2.1 Benefit Amount & Eligibility
- **Ceiling:** Up to **₹15,000 INR** (inclusive of applicable GST).
- **Eligibility:** All confirmed regular full-time employees upon passing their 90-day probationary period.
- **Claim Window:** Must be claimed within **90 calendar days** from the date of formal employment confirmation.

### 2.2 Eligible Equipment Categories
Reimbursements are approved exclusively for the following items:
- Certified ergonomic office chairs featuring adjustable lumbar support, 3D armrests, and pneumatic height adjustment (e.g., Featherlite, Transteel, Green Soul, Herman Miller).
- Height-adjustable desks or motorized sit-stand desk convertors.
- Dual-monitor aluminum desk mounts or VESA gas-spring monitor arms.
- External ergonomic keyboards and vertical ergonomic mice.
- Home Wi-Fi router UPS backup systems (e.g., APC, Resonate).
*Ineligible:* Gaming consoles, decorative lighting, beanbags, sofas, headphones, or soundbars.

### 2.3 Vendor Corporate Discount Partnerships
NexaTech maintains negotiated corporate discount codes offering 15% to 25% off retail list prices:
- **Featherlite:** Use code `NEXA-FEATHER-25` on `featherlitefurniture.com`.
- **Transteel:** Use code `TRANSTEEL-NEXA20` on corporate portal.

---

## 3. Monthly Broadband & Connectivity Reimbursement

### 3.1 Monthly Allowance Limit
- NexaTech reimburses up to **₹1,500 INR per month** (inclusive of GST) toward home broadband internet bills.
- If the monthly bill is less than ₹1,500, reimbursement is for actual invoice amount. If the bill exceeds ₹1,500, the employee absorbs the differential.

### 3.2 Submission Workflow and Deadlines
- Claims must be filed via *NexaPortal Expense Module* under category *Internet Reimbursement*.
- Attach a clear PDF of the monthly telecom invoice (Airtel, Jio Fiber, ACT Fibernet, Tata Play Fiber, etc.). The invoice must clearly show:
  1. Service address matching the employee's registered residential address.
  2. Employee's name or immediate family member's name.
  3. Tax invoice number, billing period, and GSTIN of the telecom provider.
- **Deadline:** Claims must be filed within **30 calendar days** of invoice generation. Backdated claims spanning multiple expired quarters will not be honored.
"""

# 23. shift_timing_and_night_allowance.md (MEDIUM ~4,800 chars)
docs_batch3["shift_timing_and_night_allowance.md"] = """# NexaTech Solutions - Shift Rotations, Operational Timings & Shift Allowances Policy
**Document ID:** NT-OPS-POL-023  
**Version:** 3.4  
**Effective Date:** February 1, 2026  
**Owner:** Workforce Management, Delivery Operations & People Ops  
**Classification:** Internal - Technical Operations  

---

## 1. Purpose and Operational Context
To support mission-critical cloud workloads, 24/7 SRE coverage, and round-the-clock enterprise clients across the United States, Europe, and Asia-Pacific, NexaTech operates structured rotational shifts. This policy defines shift windows, allowance schedules, safety protocols, and health safeguards.

---

## 2. Shift Windows and Allowance Structure

All shifts are 8.5 hours in duration, including a 45-minute meal break and two 15-minute rest intervals:

| Shift Name | Operational Hours (IST) | Applicable Allowance (Per Active Shift Worked) | Transport Support |
|---|---|---|---|
| **General Shift** | 09:30 AM – 06:30 PM | Baseline salary (No additional allowance) | Public / Personal / Nexa Commute Bus |
| **Morning / Early Shift** | 06:00 AM – 02:30 PM | **₹350 INR** per shift | Morning pickup cab provided for home pickups before 6:00 AM |
| **Afternoon / Mid Shift** | 02:00 PM – 10:30 PM | **₹500 INR** per shift | Night drop cab provided for all staff departing after 8:00 PM |
| **Night Shift (US Hours)** | 10:00 PM – 06:30 AM | **₹800 INR** per shift | Dedicated door-to-door escort cab with security personnel |

---

## 3. Shift Allowance Payment and Eligibility Rules
- Allowances are credited directly into monthly payroll based on verified attendance biometric turnstile logs and manager roster submissions.
- Allowances are payable only for active working shifts; paid leave, public holidays, or comp-offs taken while assigned to a shift roster do not earn shift allowances.
- Shift allowance is treated as a taxable special allowance under Indian Income Tax regulations.

---

## 4. Night Shift Safety Protocols & Women Employee Safeguards
NexaTech enforces the highest safety and security standards in accordance with the Karnataka, Telangana, and Maharashtra Shops and Establishments Acts:
- **Mandatory Cab Escort:** All female employees departing after 8:00 PM or arriving before 6:00 AM must be provided with company-contracted GPS-tracked cabs with an armed security guard on board.
- **Driver Verification:** All transport drivers undergo background verification, police verification, and quarterly breathalyzer screening.
- **First-Pick / Last-Drop Rule:** Female employees are never picked first in the morning or dropped last at night without a security guard in the vehicle. The security guard must confirm the employee safely enters her residential premises before the cab departs.
- **Emergency Telematics:** All corporate transport cabs feature automated SOS panic buttons monitored live by the Central Security Operations Center (CSOC: +91-80-6922-0001).

---

## 5. Health Safeguards and Fatigue Management
- **Maximum Consecutive Night Shifts:** No employee may be scheduled for more than **5 consecutive night shifts**. After 5 consecutive night shifts, a mandatory rest window of at least 48 continuous hours is enforced before transitioning to another shift.
- **Shift Swaps:** Shift swaps between colleagues must be submitted on NexaPortal at least 24 hours in advance and approved by the Roster Delivery Manager.
- **Quarterly Health Checks:** Night-shift staff are entitled to free quarterly vitals and sleep-health screenings at our campus wellness centers.
"""

# 24. anti_harassment_posh_policy.md (MEDIUM ~5,400 chars)
docs_batch3["anti_harassment_posh_policy.md"] = """# NexaTech Solutions - Prevention of Sexual Harassment (POSH) & Anti-Harassment Policy
**Document ID:** NT-LGL-POL-024  
**Version:** 5.0  
**Effective Date:** January 1, 2026  
**Owner:** Internal Complaints Committee (ICC) & Legal Counsel  
**Classification:** Internal - All Personnel  

---

## 1. Zero-Tolerance Policy Statement
NexaTech Solutions ("NexaTech") is committed to fostering a safe, respectful, and dignified work environment free from sexual harassment, gender discrimination, and hostile work conditions. Sexual harassment is an infringement of the fundamental right to gender equality, life, and personal liberty guaranteed by the Constitution of India.

NexaTech enforces a strict zero-tolerance mandate toward any form of sexual harassment in strict compliance with the *Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013*.

---

## 2. Definitions and Workplace Scope

### 2.1 Defining Sexual Harassment
Sexual harassment includes any one or more of the following unwelcome acts or behaviors (whether directly or by implication):
- Unwelcome physical contact, advances, or inappropriate proximity.
- Demand or request for sexual favors (quid pro quo harassment).
- Making sexually colored remarks, jokes, or innuendos.
- Showing or distributing pornography, sexually explicit videos, images, memes, or cartoons via email, Slack, or WhatsApp.
- Any other unwelcome physical, verbal, visual, or non-verbal conduct of a sexual nature.
- Implied or explicit promise of preferential treatment or threat of detrimental employment action tied to sexual cooperation.

### 2.2 Expanded Definition of Workplace
The "workplace" extends beyond physical NexaTech offices to include:
- Client offices, data centers, and project sites.
- Business travel, airport lounges, hotel accommodations, and company-sponsored transit cabs.
- Corporate retreats, team dinners, off-sites, and industry conferences.
- Virtual digital workspaces: Slack channels, Zoom / Google Meet calls, email communications, and direct messaging applications.

---

## 3. Constitution of the Internal Complaints Committee (ICC)
NexaTech has constituted an independent Internal Complaints Committee across each operating region:
- **Presiding Officer:** A senior woman leader from within the enterprise.
- **Employee Members:** At least two employees committed to gender justice and legal integrity.
- **External Member:** An independent external legal expert or NGO representative specializing in women's rights and POSH compliance.
- **Gender Ratio:** At least 50% of the total committee members are women.

---

## 4. Complaint Redressal Process and Timelines

```
[Incident Occurs]
       │
       ▼ (Within 3 Months)
[Written Complaint to posh@nexatech.com]
       │
       ▼ (Within 7 Days)
[ICC Sends Notice & Copy of Complaint to Respondent]
       │
       ▼ (Within 10 Days)
[Respondent Files Formal Written Response]
       │
       ├─────────────────────────────────┐
       ▼ (Optional)                      ▼ (Default)
[Conciliation Requested]          [Formal Inquiry Initiated]
       │                                 │
       ▼                                 ▼ (Within 90 Days)
[Mutual Settlement Reached]       [Inquiry Completed & Findings Report]
                                         │
                                         ▼ (Within 10 Days)
                                  [Management Executes Recommendations]
```

### 4.1 Filing a Complaint
- Any aggrieved employee may submit a formal written complaint within **3 months** of the incident date to `posh@nexatech.com`. In cases of incapacitation, legal heirs or trusted colleagues may file on their behalf.
- If conciliation is requested by the complainant, the ICC facilitates amicable settlement without monetary compensation. If conciliation fails or is declined, a formal inquiry commences.

### 4.2 Interim Measures
During the pendency of the inquiry, the ICC may recommend immediate protective relief:
- Transferring the complainant or respondent to another project squad or floor.
- Granting paid leave up to 3 months to the complainant (in addition to standard leave balances).
- Restraining the respondent from supervising or assessing the complainant's performance.

---

## 5. Penalties for Proven Harassment
If allegations are substantiated, the ICC recommends disciplinary sanctions to Executive Management:
- Written apology and mandatory psychological sensitivity counseling.
- Withholding promotion, salary increments, or annual bonus payouts.
- Termination of employment for gross misconduct without notice or severance pay.
- Monetary deductions from respondent's salary paid as compensatory damages to the victim.

---

## 6. Protection Against Retaliation and Confidentiality
- **Confidentiality:** The identity of the complainant, respondent, and witnesses is strictly protected. Leaking inquiry details is an offense subject to ₹5,000 statutory penalties and disciplinary action.
- **Retaliation:** Retaliation against any party or witness will result in summary dismissal.
"""

# 25. grievance_redressal_escalation.md (MEDIUM ~4,900 chars)
docs_batch3["grievance_redressal_escalation.md"] = """# NexaTech Solutions - Workplace Grievance Redressal & Escalation Framework
**Document ID:** NT-HR-POL-025  
**Version:** 3.3  
**Effective Date:** January 1, 2026  
**Owner:** People Operations & Employee Relations Guild  
**Classification:** Internal - All Employees  

---

## 1. Objective and Guiding Principles
NexaTech Solutions ("NexaTech") is committed to ensuring prompt, fair, and objective resolution of employee grievances relating to working conditions, compensation disputes, team dynamics, managerial conflicts, or unfair treatment. Every employee has the right to be heard without fear of bias or professional prejudice.

*(Note: Inquiries relating to sexual harassment are governed exclusively by `anti_harassment_posh_policy.md`; matters of financial fraud or criminal illegality fall under `whistleblower_protection_policy.md`.)*

---

## 2. Multi-Tier Grievance Escalation Matrix

```
[Level 1: Informal Dialogue & HRBP Mediation]  --> SLA: 5 Business Days
                    │ (If Unresolved)
                    ▼
[Level 2: Formal Grievance Committee Inquiry]   --> SLA: 14 Business Days
                    │ (If Unresolved)
                    ▼
[Level 3: Executive Grievance Council Review]   --> SLA: 10 Business Days (Final & Binding)
```

### 2.1 Level 1: Direct Resolution & HRBP Mediation
- The employee discusses the concern informally with their direct Reporting Manager or assigned Human Resources Business Partner (HRBP).
- The manager/HRBP conducts informal discussions and attempts to resolve the issue within **5 business days**.
- If the grievance directly involves the Reporting Manager, the employee may bypass the manager and approach the HRBP directly.

### 2.2 Level 2: Formal Grievance Committee
If the matter remains unresolved or the employee is dissatisfied with Level 1 mediation:
- The employee submits a formal Grievance Ticket via NexaPortal under *Employee Relations -> Formal Grievance* or emails `grievance@nexatech.com`.
- The **Grievance Redressal Committee** (comprising an independent Practice Head, Head of Employee Relations, and a peer council member) reviews the petition.
- The committee reviews documentation, interviews relevant parties, and issues a written finding within **14 business days**.

### 2.3 Level 3: Executive Grievance Council
- If either party disputes the Level 2 findings, a final appeal may be submitted within 7 business days of the Level 2 ruling.
- The **Executive Grievance Council** (comprising the Chief People Officer, Chief Operating Officer, and General Counsel) convenes to review the full investigative record.
- The Council renders a final, legally binding decision within **10 business days**. No further internal appeals are entertained.

---

## 3. Scope of Grievances
Employees may invoke this redressal mechanism for issues including:
- Arbitrary performance appraisal scoring or uncalibrated PIP placements.
- Denial of statutory leave entitlements or unapproved shift transitions.
- Workplace interpersonal hostility, micro-inequities, or managerial favoritism.
- Unfair project bench allocation or denial of lateral transfer requests.
- Payroll discrepancies, expense claim rejections, or incentive calculation errors.

---

## 4. Protection from Victimization and Documentation Integrity
- NexaTech strictly prohibits any form of victimization, harassment, negative appraisal retribution, or adverse project reallocation against an employee who exercises their right to file a grievance.
- Any manager found retaliating against a grieving employee will face formal disciplinary action up to termination of employment.
- All grievance records, interview recordings, and deliberation logs are archived in encrypted HR archives with access restricted strictly to Employee Relations legal custodians.
"""

# 26. whistleblower_protection_policy.md (MEDIUM ~4,700 chars)
docs_batch3["whistleblower_protection_policy.md"] = """# NexaTech Solutions - Whistleblower Protection & Vigil Mechanism Policy
**Document ID:** NT-LGL-POL-026  
**Version:** 4.1  
**Effective Date:** January 1, 2026  
**Owner:** Audit Committee of the Board & Legal Compliance  
**Classification:** Internal - All Employees  

---

## 1. Statutory Context & Enterprise Scope
In compliance with Section 177 of the Companies Act, 2013, and global anti-fraud standards, NexaTech Solutions ("NexaTech") maintains a robust Vigil Mechanism empowering employees, contractors, and vendors to report genuine concerns regarding unethical behavior, fraud, financial misconduct, or regulatory non-compliance.

This policy guarantees confidential, independent investigations and absolute immunity from organizational retaliation for disclosures made in good faith.

---

## 2. Reportable Malpractices
Protected disclosures under this policy encompass:
- Financial fraud, accounting irregularities, falsification of client billing timesheets, or tax evasion.
- Offering, paying, or soliciting commercial bribes, kickbacks, or facilitation payments.
- Insider trading or unauthorized disclosure of non-public customer financial data.
- Intentional violation of export control sanctions or data privacy statutes (GDPR, DPDP Act).
- Serious compromise of enterprise cyber infrastructure, unauthorized backdoor deployments, or concealment of data breaches.
- Environmental health and physical safety violations placing personnel in immediate danger.

---

## 3. Reporting Channels & Anonymity

Whistleblowers may report disclosures 24/7/365 through the following secure channels:
- **Independent Web Hotline:** `https://nexatech.ethicspoint.internal` (Permits complete digital anonymity via randomized alphanumeric PIN).
- **Confidential Email Alias:** `ethics@nexatech.com` (Directly routed to the Corporate Ombudsperson and Chief Legal Officer).
- **Direct Access to Board Audit Committee:** In critical cases involving Senior Executive Leadership or C-Suite officers, reports may be mailed directly to:  
  *Chairperson, Audit Committee of the Board*  
  *NexaTech Solutions Private Limited*  
  *Tower B, Global Tech Park, Outer Ring Road, Bellandur, Bengaluru 560103, India.*

---

## 4. Investigation Methodology and Timelines
1. **Initial Screening (Within 48 Hours):** The Corporate Ombudsperson screens the disclosure for prima facie evidence. Frivolous or malicious grievances are dismissed.
2. **Investigation Mandate (Within 10 Days):** A dedicated Special Investigation Team (SIT) comprising internal audit, digital forensics, and legal specialists is mobilized.
3. **Investigation Completion (Within 45 Days):** The SIT examines forensic artifacts, bank transactions, code commits, and interview transcripts, submitting a formal Investigation Report to the Audit Committee.
4. **Action & Remediation (Within 15 Days of Report):** The Audit Committee executes binding corrective measures including executive termination, criminal referral, recovery of misappropriated funds, and strengthening of internal financial controls.

---

## 5. Absolute Whistleblower Protection (Zero Retaliation)
- **Legal Immunity:** No whistleblower reporting in good faith will suffer termination, demotion, transfer, denial of promotion, salary reduction, or subtle intimidation.
- **Burden of Proof:** Any adverse employment action taken against a whistleblower within 12 months of filing a report will be presumed retaliatory unless management demonstrates compelling, documented non-related cause beyond reasonable doubt.
- **Penalties for Retaliation:** Anyone attempting to identify, threaten, or retaliate against a whistleblower will be subject to summary dismissal.
"""

# 27. substance_free_workplace.md (MEDIUM ~4,100 chars)
docs_batch3["substance_free_workplace.md"] = """# NexaTech Solutions - Drug-Free, Alcohol-Free & Substance Policy
**Document ID:** NT-HR-POL-027  
**Version:** 3.1  
**Effective Date:** January 1, 2026  
**Owner:** Workplace Safety, Physical Security & People Operations  
**Classification:** Internal - All Personnel  

---

## 1. Policy Statement and Core Objectives
NexaTech Solutions ("NexaTech") is dedicated to providing a safe, healthy, and productive working environment. The use, possession, manufacture, or distribution of illicit narcotics, unprescribed controlled substances, or alcohol impairs cognitive judgment, endangers coworker physical safety, and compromises intellectual property security.

This policy applies on all corporate premises, customer project sites, transit vehicles, business travel journeys, and client-sponsored social events.

---

## 2. Prohibited Conduct
- **Illicit Narcotics:** The possession, sale, purchase, consumption, or distribution of any illicit narcotic or psychotropic substance (as classified under the Narcotic Drugs and Psychotropic Substances Act, 1985) is strictly prohibited.
- **Alcohol on Campus:** Possession or consumption of alcoholic beverages on office premises, cafeterias, parking decks, or client facilities is forbidden, except during designated corporate celebrations formally sanctioned by the Chief Executive Officer (CEO).
- **Impaired Operation:** Reporting to work, operating company hardware, or driving company-provided vehicles while under the influence of intoxicating substances or alcohol is strictly banned.

---

## 3. Prescription Medications
Employees legally using prescribed medications that may cause drowsiness, motor impairment, or cognitive deficits (e.g., strong pain medications, sedatives) must inform their Reporting Manager if their duties involve server rack maintenance, hardware testing, or on-site client operations.

---

## 4. Testing Protocols and Reasonable Suspicion
NexaTech reserves the right to conduct certified toxicological screenings under specific conditions:
- **Reasonable Suspicion:** Triggered when an employee displays overt signs of intoxication, severe slurred speech, acute motor disorientation, or erratic aggressive behavior. Testing requires concurrence between the Practice Head and HRBP.
- **Post-Incident Testing:** Mandatory for any personnel involved in a major workplace safety incident, vehicular accident, or critical security breach causing physical harm or property damage.

---

## 5. Employee Assistance Program (EAP) & Disciplinary Outcomes
- **Self-Disclosed Dependency Support:** Employees struggling with substance abuse who voluntarily seek assistance prior to being identified by security or performance failures are provided up to **30 days of medical leave** and confidential clinical rehabilitation support through the *1to1Help* EAP network.
- **Disciplinary Sanctions:** Confirmed unauthorized possession, sale, or refusal to undergo reasonable-suspicion testing results in immediate termination of employment for gross misconduct without notice.
"""

# 28. onboarding_sales_account_exec.md (MEDIUM ~5,000 chars)
docs_batch3["onboarding_sales_account_exec.md"] = """# NexaTech Solutions - Sales & Account Executive (AE) Onboarding Playbook
**Document ID:** NT-SLS-GDE-028  
**Version:** 3.2  
**Effective Date:** February 1, 2026  
**Owner:** Global Sales Enablement & Revenue Operations  
**Classification:** Internal - Sales Organization  

---

## 1. Welcome to NexaTech Global Sales
As an Account Executive (AE) or Sales Director at NexaTech Solutions, you lead customer relationships, digital transformation scoping, and multi-year IT services contracts across North America, Europe, and Asia-Pacific.

This guide outlines your 90-day onboarding trajectory, sales toolchains, Master Services Agreement (MSA) frameworks, and revenue enablement resources.

---

## 2. Sales Tech Stack & CRM Provisioning
Your Okta SSO credentials provide immediate access to the following revenue tools:
- **Salesforce Enterprise CRM:** Central system of record. Every deal, contact, opportunity stage, and customer interaction must be logged within 24 hours.
- **ZoomInfo Enterprise:** Prospecting, contact discovery, and org-chart mapping.
- **Gong.io:** AI-powered conversational intelligence for client discovery calls, demos, and pipeline reviews.
- **LinkedIn Sales Navigator Team Edition:** Account outreach and executive relationship mapping.
- **Highspot:** Sales enablement content, case studies, client pitch decks, and technical capability one-pagers.

---

## 3. Deal Governance & Pricing Approval Chains
All client proposals, Statements of Work (SOWs), and rate-card discount requests must navigate standardized governance workflows before client submission:

| Annual Contract Value (ACV) | Gross Margin Floor | Mandatory Approval Hierarchy |
|---|---|---|
| **Tier 1: < $250,000 USD** | Minimum 38% Gross Margin | Sales Director + Delivery Lead |
| **Tier 2: $250,000 to $1,000,000 USD** | Minimum 35% Gross Margin | VP of Sales + Practice Head + Finance Controller |
| **Tier 3: > $1,000,000 USD** | Minimum 32% Gross Margin | Chief Commercial Officer (CCO) + CFO + CEO |

*Note:* Standard Master Service Agreements (MSAs) must use standard NexaTech legal templates. Any client-proposed deviations regarding indemnification caps, liability ceilings, or intellectual property assignment require explicit written clearance from Legal Counsel (`legal@nexatech.com`).

---

## 4. Sales 30-60-90 Day Ramp Milestones

```
[Month 1: Enablement & Pitch Certification]
  ├── Complete NexaTech Capability Certifications on Highspot
  ├── Master our 4 core service lines: CloudOps, Data/AI, App Mod, SRE
  ├── Shadow 10 live sales calls with senior Account Directors on Gong
  └── Deliver formal 45-minute mock client pitch to the Sales VP

[Month 2: Pipeline Generation & Account Scoping]
  ├── Build account plan for 20 Tier-1 enterprise target accounts
  ├── Generate $500,000 USD in qualified pipeline opportunities (Stage 2+)
  ├── Co-author first technical RFP response with Engineering Solution Architects
  └── Conduct first 5 customer discovery calls independently

[Month 3: Deal Acceleration & Closing]
  ├── Advance at least 2 opportunities to Stage 4 (Contract Scoping / MSA Review)
  ├── Deliver $1,000,000+ USD active pipeline in Salesforce
  └── Close first commercial SOW or pilot engagement
```

---

## 5. Sales Commission Structure Overview
Commission payouts are governed by the Global Incentive Compensation Plan:
- Sales targets are designated on an Annual Quota basis, evaluated and disbursed quarterly.
- Baseline commission pays out at 4% to 6% of Recognized Revenue upon milestone sign-off by client and invoice collection. Full details in `sales_commission_plan.md`.
"""

# 29. onboarding_hr_people_ops.md (MEDIUM ~4,900 chars)
docs_batch3["onboarding_hr_people_ops.md"] = """# NexaTech Solutions - People Operations & HRBP Onboarding Playbook
**Document ID:** NT-HR-GDE-029  
**Version:** 3.1  
**Effective Date:** February 1, 2026  
**Owner:** People Operations Excellence & HR Shared Services  
**Classification:** Internal - HR Personnel  

---

## 1. Mission of People Operations at NexaTech
People Operations at NexaTech Solutions is designed not as a bureaucratic administrative unit, but as a strategic business partner championing employee growth, organizational effectiveness, diversity, and operational compliance across our global delivery centers.

This playbook establishes the operational foundation for incoming Human Resources Business Partners (HRBPs), Talent Acquisition specialists, and Total Rewards analysts.

---

## 2. Core Human Resources Information Systems (HRIS)
HR team members are provisioned privileged access to the following enterprise portals:
- **Darwinbox HRMS:** Core system of record for employee demographic profiles, leave management, confirmation tracking, and appraisal rating workflows.
- **Greenhouse ATS:** End-to-end recruitment pipeline, candidate interview scorecards, job requisitions, and offer letter generation.
- **Keka Payroll & Tax Portal:** Monthly payroll cut-off registers, investment proof verification, and Form 16 generation.
- **First Advantage (FADV):** Automated background verification (BGV) portal tracking criminal records, employment history, and education degree verifications.

---

## 3. Background Verification (BGV) SLAs and Protocols
NexaTech enforces 100% background verification for all joiners prior to full employment confirmation:
- **Components Screened:** Highest educational degree, previous 7 years employment history, permanent address physical check, national criminal database search, and global watchlists.
- **BGV Results Categorization:**
  - *Green (Clear):* Verified without discrepancies; confirmation proceeds.
  - *Amber (Minor Discrepancy):* Minor date mismatch (<30 days) or tenure overlap during college; resolved via candidate affidavit.
  - *Red (Major Fraud / Fake Experience):* Fabricated experience letters, fraudulent degree certificates, or concealed criminal history. Triggers immediate termination with zero notice under gross misconduct clauses.

---

## 4. Key HR Operations Calendar and Deadlines
- **Monthly Payroll Cut-Off:** 20th of every month. All new joiners, unpaid leave (LWP), salary revisions, and exit clearances must be approved in Darwinbox by 5:00 PM IST on the 20th.
- **Confirmation Tracker:** Run on the 1st of every month to identify employees approaching the 90-day probation milestone. Review forms must reach managers by Day 75.
- **Exit Processing & F&F Clearances:** Initiated upon employee resignation submission; assets retrieved and F&F settlement packet approved within 30 days of LWD.
"""

# 30. onboarding_operations_support.md (MEDIUM ~4,800 chars)
docs_batch3["onboarding_operations_support.md"] = """# NexaTech Solutions - IT Service Desk & Operations Support Onboarding Guide
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
"""

for filename, content in docs_batch3.items():
    file_path = DOCS_DIR / filename
    file_path.write_text(content.strip(), encoding="utf-8")
    print(f"Written: {filename} ({len(content)} chars)")

print("Batch 3 Complete: 10 files written.")
