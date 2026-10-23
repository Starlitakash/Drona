import os
from pathlib import Path

DOCS_DIR = Path("docs")
DOCS_DIR.mkdir(parents=True, exist_ok=True)

docs_batch1 = {}

# 1. employee_handbook.md (LONG ~14,000 chars)
docs_batch1["employee_handbook.md"] = """# NexaTech Solutions - Comprehensive Employee Handbook
**Document ID:** NT-HR-HB-001  
**Version:** 4.2  
**Effective Date:** January 1, 2026  
**Owner:** People Operations & Human Resources  
**Classification:** Internal - All Employees  

---

## 1. Welcome to NexaTech Solutions

### 1.1 Company Overview & Vision
Founded in 2014, NexaTech Solutions Private Limited ("NexaTech") is a premier mid-sized digital engineering and cloud transformation services enterprise headquartered in Bengaluru, Karnataka, India. With delivery centers in Bengaluru (Global Tech Park), Hyderabad (HITEC City), Pune (Hinjewadi Phase 2), and Gurugram (Cyber City), alongside client partner offices in San Jose, CA (USA) and London (UK), NexaTech powers mission-critical software systems for global Fortune 500 enterprises and hyper-growth innovators.

Our mission is to accelerate sustainable digital evolution through agile engineering, enterprise resilience, and human-centric design. We cultivate an inclusive culture where high ownership, continuous curiosity, technical craftsmanship, and uncompromising ethics define everyday execution.

### 1.2 Core Values: The PRISM Framework
Every team member at NexaTech operates under our PRISM core principles:
- **P - Precision Engineering:** Delivering defect-free, scalable, secure, and production-ready code with pride in craftsmanship.
- **R - Relentless Curiosity:** Investing in continuous learning, experimentation, and upskilling in modern cloud, data, and AI ecosystems.
- **I - Integrity & Transparency:** Holding honesty, psychological safety, client trust, and zero-compromise compliance at the center of all operations.
- **S - Shared Ownership:** Solving challenges cross-functionally, refusing to operate in silos, and owning client outcomes collectively.
- **M - Meritocracy with Empathy:** Recognizing high performance while honoring well-being, work-life balance, and mutual dignity.

---

## 2. Employment Terms and Governance

### 2.1 Employment Categories
NexaTech categorizes personnel under four distinct classifications:
1. **Regular Full-Time Employees:** Staff contracted for standard 40-hour work weeks with full eligibility for corporate benefits, healthcare coverage, annual appraisal bonuses, and statutory retirement schemes.
2. **Fixed-Term Contract Personnel:** Professionals engaged for specific project tenures (6 to 24 months) under bilateral service agreements.
3. **Interns & Apprentices:** Students or early-career learners enrolled in 3-month to 6-month specialized development tracks under technical mentorship.
4. **Retainers & Specialist Advisors:** External subject matter experts contracted for high-level technical advisory or architectural reviews.

### 2.2 Probationary Period and Confirmation
All new regular hires undertake a mandatory 90-day probationary review window:
- **30-Day Check-in:** Informal progress alignment with your assigned buddy and Reporting Manager.
- **60-Day Review:** Milestone assessment against role-specific goals set in NexaPortal.
- **90-Day Formal Evaluation:** Structured evaluation by the Reporting Manager and People Operations Partner (HRBP).
Upon successful evaluation, an official Confirmation Letter is generated within 5 business days via NexaPortal. If performance falls below benchmarks, probation may be extended by up to 60 calendar days with a documented Performance Improvement Plan (PIP).

### 2.3 Working Hours, Shift Rosters, and Overtime
- **Standard Working Week:** Monday through Friday, comprising 40 active work hours.
- **Core Collaboration Hours:** 10:00 AM to 4:00 PM IST, during which team members must be reachable on Slack and attend scheduled standups/ceremonies.
- **Flexible Bands:** Employees may flex their arrival between 8:30 AM and 10:30 AM IST with manager concurrence.
- **Rotational Shifts:** Certain 24/7 client operations (CloudOps, SRE, Network Operations Center) utilize 8-hour rotational shifts. Rotational shifts qualify for monthly Shift Allowances as detailed in `shift_timing_and_night_allowance.md`.

---

## 3. Workplace Culture & Professional Conduct

### 3.1 Diversity, Equity, and Inclusion (DEI)
NexaTech is committed to creating an equitable workplace free of discrimination based on gender identity, sexual orientation, caste, religion, disability, age, veteran status, or marital status. We sponsor employee resource groups including *NexaWomen in Tech*, *Pride@Nexa*, and *NexaNeurodiversity*.

### 3.2 Anti-Harassment and POSH Framework
We maintain zero tolerance toward sexual harassment, intimidation, bullying, or hostile workplace behaviors. NexaTech enforces strict adherence to the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013:
- The Internal Complaints Committee (ICC) is presided over by an external legal expert and senior female leadership.
- Any formal complaint submitted to `posh@nexatech.com` is formally acknowledged within 24 hours and investigated within statutory timelines (completion within 90 days).
- Retaliation against any complainant or witness triggers immediate summary termination of the offender.

### 3.3 Drug, Alcohol, and Smoke-Free Campus Policy
All NexaTech premises are strictly smoke-free, tobacco-free, and substance-free zones. Smoking is restricted solely to designated municipal exterior enclosures away from building air intakes. Possession or consumption of alcoholic beverages or illicit substances on office premises or during client engagements is strictly prohibited and subject to immediate disciplinary termination.

---

## 4. Compensation, Payroll, and Performance

### 4.1 Compensation Architecture
Salaries are paid monthly in arrears on the last banking day of each calendar month directly into employee HDFC, ICICI, or Axis salary accounts. The standard Cost to Company (CTC) structure comprises:
- **Basic Salary:** 40% to 50% of monthly CTC (statutory basis for PF and Gratuity).
- **House Rent Allowance (HRA):** 50% of Basic for metro locations (Bengaluru, Hyderabad, Gurugram) and 40% for non-metro locations (Pune).
- **Special Allowance:** Balancing monthly allowance component.
- **Statutory Retirals:** Provident Fund (12% of Basic employer contribution) and statutory gratuity provisioning.
- **Annual Performance Bonus (Variable Pay):** Evaluated annually against corporate, business unit, and individual milestones.

### 4.2 Performance Management System: NexaGrowth
Appraisals occur bi-annually:
- **Mid-Year Check (H1):** Held in July (qualitative progress review, OKR recalibration).
- **Annual Evaluation (H2):** Held in January (quantitative rating on a 1.0 - 5.0 scale, merit increment cycle, promotion committee).
Rating distribution follows a calibrated curve:
- Rating 5 (Exceptional - Top 10%): 130%-150% target variable bonus payout.
- Rating 4 (Exceeds Expectations - Next 25%): 110%-120% target variable bonus payout.
- Rating 3 (Meets Expectations - Core 50%): 100% target variable bonus payout.
- Rating 2 (Needs Improvement - 10%): PIP initiated, bonus withheld.
- Rating 1 (Unsatisfactory - 5%): Exit proceedings or immediate termination.

---

## 5. Overview of Employee Benefits

### 5.1 Group Health & Term Insurance
- **Group Medical Cover (GMC):** ₹5,00,000 base floater coverage for employee, spouse, up to 2 dependent children, or dependent parents. Super top-up of ₹10,00,000 available at nominal group subsidy.
- **Group Personal Accident (GPA):** ₹25,00,000 capital sum insured against accidental disability or mortality.
- **Group Term Life (GTL):** 3x annual CTC rounded to the nearest lakh, protecting designated nominees.

### 5.2 Wellness and Employee Assistance Program (EAP)
All employees and immediate dependents enjoy 24/7 anonymous counseling support via our wellness partner *1to1Help* covering stress management, financial advisory, and grief counseling. Dial +91-80-6900-5555 or email `support@1to1help.net`.

### 5.3 Continuous Learning & Certification Reimbursement
NexaTech invests ₹25,000 annually per employee for approved cloud (AWS, GCP, Azure), security (CISSP, CISA), and engineering certifications. Upon achieving certification, submit the voucher and completion certificate via NexaPortal under *Learning & Development* within 30 calendar days.

---

## 6. Leave & Time-Off Architecture

NexaTech offers a comprehensive suite of leave entitlements designed to promote physical rest, personal rejuvenation, and family obligations:
- **Casual Leave (CL):** 12 days per calendar year (credited quarterly at 3 days per quarter; maximum 3 consecutive days).
- **Sick / Medical Leave (SL):** 10 days per calendar year. Medical certificate mandatory for sick leaves exceeding 2 consecutive days.
- **Earned Leave / Privilege Leave (EL/PL):** 18 days per calendar year (accrued at 1.5 days per completed month). Up to 45 accumulated days can be carried forward across calendar years.
- **Maternity Leave:** 26 continuous weeks (182 calendar days) fully paid for female employees with at least 80 days of service.
- **Paternity Leave:** 15 working days fully paid, usable in up to two tranches within 6 months of childbirth or legal adoption.
- **Bereavement Leave:** 5 working days in case of the loss of an immediate family member (parents, spouse, siblings, children).

---

## 7. IT Security and Data Stewardship

### 7.1 Acceptable Use & Clean Desk Policy
Employees must protect client proprietary software, source repositories, personal data, and infrastructure credentials.
- Workstations must be locked (`Win + L` or `Cmd + Ctrl + Q`) whenever unattended.
- Printed papers containing confidential or PII data must be shredded before end-of-day.
- USB mass storage devices and unapproved portable media are strictly locked down by central Mobile Device Management (MDM).

### 7.2 Passwords and Authentication
- Passwords must be at least 14 characters long, containing uppercase, lowercase, numbers, and symbols.
- Passwords expire every 90 days and cannot match the previous 5 passwords.
- Multi-Factor Authentication (MFA) via Microsoft Authenticator or Okta Verify is mandatory on all NexaTech accounts.

---

## 8. Facilities and General Administration

### 8.1 Badges and Security Checkpoints
- Access badges must be worn visibly on company-issued lanyards at all times within office premises.
- Lost badges must be reported immediately to `facilities@nexatech.com`. Replacement fee of ₹500 is deducted from the following month's payroll.
- Visitors must be registered at reception, issued visitor badges, and escorted by a NexaTech host throughout their visit.

### 8.2 Travel and Local Commute Support
- Late-night transport: Female employees working on-site beyond 8:00 PM IST or any employee working beyond 9:30 PM IST are entitled to security-escorted cab drops managed through the NexaTransport app.
- Domestic and international travel must follow the expense tiers specified in `travel_expense_reimbursement.md`.

---

## 9. Separation, Notice Periods, and Offboarding

### 9.1 Voluntary Resignation and Notice Periods
- Confirmed full-time staff: 90 calendar days mandatory notice period.
- Probationary staff: 30 calendar days notice period.
- Buyout of notice period requires explicit written approval from the Practice Head and HRBP, calculated at the base gross daily salary rate.

### 9.2 Exit Clearances and Full & Final (F&F) Settlement
Upon submission of resignation via NexaPortal:
- Hardware, access badges, and library materials must be surrendered on the final working day to Facilities and IT.
- Outstanding travel advances or hardware damage penalties must be cleared.
- Full and Final settlement payments and official Relieving & Experience Letters are issued within 30 to 45 calendar days following the Last Working Day (LWD).

---

## 10. Document Governance & Contact Directory

| Department | Contact Alias | SLA / Turnaround |
|---|---|---|
| People Operations (General HR) | `peopleops@nexatech.com` | 24 - 48 Hours |
| Payroll & Tax Queries | `payroll@nexatech.com` | 24 Hours |
| IT Service Desk | `ithelpdesk@nexatech.com` | 4 - 8 Hours |
| Information Security Incident Desk | `infosec@nexatech.com` | 15 Minutes (High Priority) |
| Facilities & Transport | `facilities@nexatech.com` | 12 Hours |
| POSH Internal Complaints Committee | `posh@nexatech.com` | 24 Hours |
| Ethics & Whistleblower Hotline | `ethics@nexatech.com` | 24 Hours |
"""

# 2. it_security_acceptable_use.md (LONG ~14,000 chars)
docs_batch1["it_security_acceptable_use.md"] = """# NexaTech Solutions - Information Technology Security & Acceptable Use Policy
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
"""

# 3. travel_expense_reimbursement.md (LONG ~14,000 chars)
docs_batch1["travel_expense_reimbursement.md"] = """# NexaTech Solutions - Corporate Travel and Expense Reimbursement Policy
**Document ID:** NT-FIN-POL-003  
**Version:** 4.4  
**Effective Date:** January 15, 2026  
**Owner:** Finance, Accounts & Corporate Travel Desk  
**Classification:** Internal - All Employees  

---

## 1. Purpose and Philosophy
NexaTech Solutions ("NexaTech") conducts global client consulting, on-site technical implementation, business development, and cross-office engineering workshops. This policy ensures business travel is conducted safely, comfortably, and economically, establishing clear expense reimbursement ceilings, approval workflows, and audit protocols.

All expenses incurred must be directly business-related, reasonable, necessary, substantiated with valid tax invoices, and pre-approved by appropriate budgetary authorities.

---

## 2. Travel Authorization and Booking Channels

### 2.1 Pre-Travel Authorization (NexaPortal TAR)
Before booking any business travel (domestic or international), the employee must submit a Travel Authorization Request (TAR) via NexaPortal:
- **Domestic Travel:** Must be submitted at least 7 business days prior to intended departure.
- **International Travel:** Must be submitted at least 21 business days prior to departure to accommodate visa facilitation, client invitation letters, and travel insurance coverage.
- **Approval Hierarchy:**
  - TAR Cost < ₹50,000: Reporting Manager approval.
  - TAR Cost ₹50,000 to ₹2,00,000: Reporting Manager + Practice / Business Unit Head approval.
  - TAR Cost > ₹2,00,000 or International Travel: Reporting Manager + BU Head + Chief Financial Officer (CFO) approval.

### 2.2 Centralized Corporate Travel Desk
All air tickets, inter-city rail travel, and hotel accommodations must be booked through the authorized *NexaTech Corporate Travel Desk* (`traveldesk@nexatech.com`) or via our integrated online corporate booking portal (*NexaTravel powered by MakeMyTrip Corporate*). Self-booking through personal retail travel aggregators is prohibited and will not be reimbursed, except during declared emergency evacuations or travel desk system outages.

---

## 3. Domestic Travel Guidelines (Within India)

### 3.1 City Tier Classification
Reimbursement limits for lodging and local expenses are categorized by municipal cost tiers:
- **Tier 1 (Metros):** Bengaluru, Mumbai (MMR), New Delhi & NCR (Gurugram, Noida), Hyderabad, Chennai, Kolkata.
- **Tier 2 (Major Urban Centers):** Pune, Ahmedabad, Kochi, Jaipur, Chandigarh, Lucknow, Indore, Coimbatore, Bhubaneswar.
- **Tier 3 (Other Locations):** All other tier-3 towns, client plant locations, and remote municipalities.

### 3.2 Air Travel Guidelines
- **Economy Class:** All domestic travel across all bands up to Vice President (L7) is strictly Economy Class.
- **Booking Window:** Flights must be booked at least 14 days in advance where possible to leverage corporate discounts.
- **Flight Window:** The Travel Desk books the most cost-effective non-stop or shortest-duration flight departing within 2 hours of the requested travel time.
- **Seat Selection & Baggage:** Standard seat selection and 15kg check-in baggage are covered. Premium extra-legroom seats or lounge passes are personal expenses unless pre-approved for red-eye flights (>4 hours).

### 3.3 Inter-City Rail and Road Travel
- **Rail Travel:** Permitted for overnight travel or routes under 6 hours (e.g., Bengaluru to Chennai, Pune to Mumbai). Eligible classes: AC First Class (1A) or Executive Chair Car for Senior Managers and above; AC 2-Tier (2A) or AC Chair Car (CC) for all other team members.
- **Inter-City Cab / Self-Drive:** Reimbursement for self-drive or outstation app-cabs (Ola/Uber Intercity) is permitted at ₹12 per kilometer for personal four-wheelers or actual commercial cab invoices, provided overall costs are lower than airfare.

### 3.4 Hotel Accommodation Limits (Per Night)
Hotel room rates are capped exclusive of applicable GST/taxes:
| Employee Band / Level | Tier 1 Metros (INR) | Tier 2 Cities (INR) | Tier 3 Cities (INR) |
|---|---|---|---|
| **Band 1 - Band 3 (Engineers, Analysts, Senior SDEs)** | Up to ₹4,500 / night | Up to ₹3,200 / night | Up to ₹2,200 / night |
| **Band 4 - Band 5 (Architects, Managers, Delivery Leads)** | Up to ₹6,500 / night | Up to ₹4,500 / night | Up to ₹3,000 / night |
| **Band 6 - Band 7 (Directors, VPs, Practice Heads)** | Up to ₹9,500 / night | Up to ₹6,500 / night | Up to ₹4,500 / night |

*Note:* Where NexaTech maintains negotiated corporate hotel tie-ups (e.g., Lemon Tree, Ginger, Courtyard by Marriott), employees must book contracted properties via the Travel Desk. If corporate hotels are unavailable due to peak conferences, an exception up to 20% over the ceiling requires Manager written approval.

---

## 4. Daily Allowances and Local Conveyance

### 4.1 Daily Food Allowance (Per Diem / Actuals)
Employees on official outstation travel are entitled to daily meal reimbursements. Employees may select either receipt-based actual reimbursement or a flat daily per diem:
- **Receipt-based Reimbursement Cap:**
  - Tier 1 Metros: Up to ₹1,200 per day.
  - Tier 2 Cities: Up to ₹900 per day.
  - Tier 3 Cities: Up to ₹650 per day.
- **Flat Per Diem (No receipts required, credited via payroll):**
  - Tier 1: ₹750 per day.
  - Tier 2: ₹550 per day.
  - Tier 3: ₹400 per day.
- Meals provided free of charge by hotels (e.g., complimentary breakfast) or hosted by clients must be excluded from daily claims.
- Alcohol, personal mini-bar items, and room service service charges are non-reimbursable.

### 4.2 Local City Conveyance
- Official transit (Airport transfers, hotel to client office, inter-office travel) must prioritize app-based cabs (Uber Business / Ola Corporate) billed directly to the corporate account or reimbursed via receipts.
- Daily local conveyance is capped at ₹1,500 per day in Tier 1 cities, and ₹1,000 in Tier 2/3 cities.
- Auto-rickshaw rides require an itemized digital receipt (e.g., Namma Yatri, Rapido) or manual cash voucher counter-signed by the Reporting Manager for routes where app-cabs are unavailable.

---

## 5. International Travel Policy

### 5.1 Flights and Visas
- All long-haul flights (>6 hours continuous flight time) are booked in Premium Economy for Senior Managers / Architects (Band 4+) and Economy for Bands 1-3. Vice Presidents and above are entitled to Business Class for international flights exceeding 8 hours.
- Visa fees, passport renewal fees required specifically for emergency business travel, biometric appointment fees, and overseas medical travel insurance (minimum $250,000 emergency medical cover) are 100% borne by NexaTech.

### 5.2 International Per Diem & Lodging Caps
International allowances are disbursed via corporate multi-currency Forex cards (Axis Bank / HDFC Bank Forex Card) loaded prior to departure:
| Destination Country / Region | Maximum Hotel Cap (Per Night) | Daily Food & Incidental Per Diem |
|---|---|---|
| **United States (Bay Area, NYC, Boston, Seattle)** | Up to $250 USD / night | $85 USD / day |
| **United States (Other Cities / Suburbs)** | Up to $190 USD / night | $70 USD / day |
| **United Kingdom (Greater London)** | Up to £180 GBP / night | £65 GBP / day |
| **United Kingdom (Regional UK / Manchester)** | Up to £130 GBP / night | £50 GBP / day |
| **European Union (Schengen Zone)** | Up to €170 EUR / night | €65 EUR / day |
| **Asia-Pacific (Singapore, Tokyo, Sydney)** | Up to $200 USD equivalent | $75 USD equivalent |
| **Middle East (Dubai, Riyadh)** | Up to $180 USD equivalent | $65 USD equivalent |

Forex cards must be reconciled within 10 business days of returning to India. Unspent foreign currency must be surrendered back to the Travel Desk for bank credit.

---

## 6. Client Entertainment and Business Meals
When entertaining prospective or existing clients, senior team members (Band 4 and above) may host business meals subject to prior written approval from the BU Head:
- **Spending Ceiling:** Maximum ₹3,000 per person in India; $90 USD per person internationally.
- **Mandatory Documentation:** Expense submission must itemize every attendee (name, organization, title) and state the business objective discussed. Itemized GST/tax bills must be uploaded.

---

## 7. Expense Submission and Settlement Workflow

### 7.1 Submission Timeline and Documentation
- All expense reimbursement claims must be filed via *NexaPortal Expense Module* within **15 calendar days** of completing travel. Claims submitted after 30 days are forfeited and automatically rejected by Finance.
- Original digitized receipts, boarding passes (physical or e-boarding pass PDF), and hotel tax invoices containing NexaTech's GSTIN must be attached.
- Invoices must clearly display the vendor name, date, invoice number, itemized charges, and tax breakdown. Credit card swipe slips without itemized bills are rejected.

### 7.2 Approval Chain & Payroll Settlement Schedule
1. **Level 1 (Reporting Manager):** Reviews business relevance and daily limits within 3 business days.
2. **Level 2 (Finance & Audit Desk):** Verifies GSTIN, tax compliance, receipts, and policy ceilings within 4 business days.
3. Approved expense claims processed by the 20th of the month are disbursed on the 25th in a mid-month reimbursement cycle. Claims approved after the 20th are settled with the month-end salary payout.

---

## 8. Non-Reimbursable Expenses Checklist
The following expenditures will NOT be reimbursed under any circumstances:
- Personal entertainment (in-room pay TV movies, spa treatments, nightclub covers).
- Traffic fines, parking violations, toll speeding penalties, or towing charges.
- Personal grooming (haircuts, cosmetics, laundry on trips shorter than 4 consecutive nights).
- Loss of personal funds, theft of personal laptops, jewelry, or luggage.
- Upgrades to hotel suites, luxury rental vehicles, or first-class rail travel without prior written CFO authorization.
- Expenses for spouses, children, or non-business companions accompanying the employee.
"""

# 4. code_of_conduct_ethics.md (LONG ~13,000 chars)
docs_batch1["code_of_conduct_ethics.md"] = """# NexaTech Solutions - Global Code of Conduct, Business Ethics & Whistleblower Policy
**Document ID:** NT-LGL-POL-004  
**Version:** 4.1  
**Effective Date:** January 1, 2026  
**Owner:** Legal, Corporate Governance & Ethics Committee  
**Classification:** Internal - All Personnel Mandatory  

---

## 1. Executive Message & Commitment
At NexaTech Solutions ("NexaTech"), our business reputation rests on an unyielding commitment to integrity, lawful execution, professional transparency, and fair dealing. As we engineer critical software architectures for global healthcare, financial services, and critical infrastructure clients, ethical behavior is not merely a policy—it is foundational to our enterprise existence.

This Code of Conduct governs all officers, directors, regular employees, contractors, and agency personnel across all global subsidiaries and branch entities.

---

## 2. Workplace Respect, Fairness & Human Rights

### 2.1 Equal Opportunity and Mutual Dignity
NexaTech enforces a strict policy of equal opportunity in all employment decisions including recruitment, promotion, compensation, assignments, and training. We prohibit discrimination, bias, or harassment predicated on race, color, religion, caste, national origin, gender, gender identity, sexual orientation, disability, genetic data, age, or military service.

### 2.2 Psychological Safety and Anti-Bullying
We cultivate psychological safety where every individual feels empowered to raise concerns, propose innovative ideas, voice dissent, or admit engineering errors without fear of humiliation or retribution. Workplace bullying—including verbal abuse, public denigration, intentional exclusion, persistent unconstructive criticism, and weaponized micro-management—is considered gross misconduct.

### 2.3 Prevention of Sexual Harassment (POSH)
In accordance with the Sexual Harassment of Women at Workplace Act (2013) and global human rights treaties:
- NexaTech maintains a legally constituted, independent Internal Complaints Committee (ICC).
- Any unwelcome sexually determined behavior (physical contact, demands for sexual favors, sexually colored remarks, display of pornography, offensive electronic communication) will trigger immediate inquiry.
- Inquiries are completed within 90 days, with protective measures (including immediate transfer or leave for either party) enforced during investigation.
- Reports may be submitted directly to `posh@nexatech.com`.

---

## 3. Conflicts of Interest and Outside Activities

### 3.1 Defining Conflicts of Interest
A conflict of interest arises whenever personal, financial, familial, or outside professional relationships interfere—or appear to interfere—with an employee's objective judgment, loyalty, or fiduciary duty to NexaTech.

### 3.2 Moonlighting and Secondary Employment
- Full-time employees may not hold secondary employment, consult for commercial entities, or operate private businesses that consume work hours, leverage NexaTech hardware, or utilize skills directly competing with NexaTech client engagements.
- Academic teaching, open-source community contributions (non-proprietary), or non-profit board memberships are permitted only after submitting an *Outside Activity Disclosure Form* on NexaPortal and receiving written sign-off from People Operations and the Legal Counsel.

### 3.3 Financial Interests and Familial Relationships
- Employees must disclose any significant financial interest (>1% equity or convertible debt) held by themselves or immediate family in any NexaTech supplier, vendor, partner, or direct competitor.
- Close relatives (spouses, siblings, parents, children) cannot work in a direct reporting line, nor can one relative influence the compensation, promotion, or performance appraisal of another.

---

## 4. Anti-Bribery, Corruption and Fair Dealing

### 4.1 Zero-Tolerance Anti-Bribery Mandate
NexaTech conducts business in strict accordance with the Prevention of Corruption Act (India), the US Foreign Corrupt Practices Act (FCPA), the UK Bribery Act (2010), and international anti-bribery conventions.
- Employees and representatives are strictly forbidden from offering, promising, authorizing, paying, or soliciting bribes, kickbacks, illicit rebates, or improper financial advantages to any commercial partner or government official.
- Facilitation payments ("grease payments" paid to expedite routine, non-discretionary governmental actions such as visa approvals or utility connections) are illegal and expressly prohibited.

### 4.2 Gifts, Hospitality and Entertainment Ceilings
Modest business courtesies are acceptable only when they do not create an obligation or perception of undue influence:
- **Gifts from Vendors / Clients:** Employees may accept occasional promotional tokens (pens, calendars, diaries) or perishable gift baskets valued under **₹2,000 INR** (or $25 USD).
- **Gifts Exceeding ₹2,000:** Must be politely declined or reported to `compliance@nexatech.com`. If declining causes cultural offense, the gift must be surrendered to People Operations for corporate raffles or charitable donation.
- **Cash and Cash Equivalents:** Accepting cash, prepaid debit cards, cryptocurrency, shares, or gift vouchers of any value is strictly prohibited.
- **Client Hospitality:** Business lunches or dinners hosted by vendors must be reasonable, infrequent, and have a clear business agenda. Lavish entertainment, private junkets, sports luxury boxes, or weekend retreats are forbidden without explicit C-suite approval.

---

## 5. Protection of Company Assets, Intellectual Property & Data

### 5.1 Intellectual Property (IP) Ownership
All software programs, algorithms, architectural designs, technical documentation, trade secrets, machine learning models, patents, and inventions authored, conceived, or developed by employees during their employment with NexaTech—whether created on corporate equipment or outside working hours utilizing company knowledge—are the sole, exclusive intellectual property of NexaTech Solutions (or assigned clients under Master Service Agreements).

### 5.2 Confidentiality and Non-Disclosure
Employees are bound by lifelong confidentiality regarding non-public customer architectures, technical roadmaps, financial projections, client contracts, and employee salary data. This obligation survives the termination of employment.

### 5.3 Insider Trading Prevention
NexaTech personnel who possess material non-public information (MNPI) regarding NexaTech, our publicly traded client enterprises, or acquisition targets are legally barred from trading securities of those corporations or tipping external parties. Trading during declared blackout windows is punishable by criminal indictment.

---

## 6. Whistleblower Mechanism and Retaliation Protection

### 6.1 Purpose of the Whistleblower Policy
We provide a secure, confidential, and anonymous mechanism for employees to report suspected accounting irregularities, fraud, embezzlement, insider trading, data theft, sexual harassment, or severe regulatory non-compliance without fear of workplace reprisal.

### 6.2 Reporting Channels
Employees may file reports 24/7 through any of the following independent channels:
- **Ethics Portal:** `https://nexatech.ethicspoint.internal` (permits complete anonymity with encrypted two-way ticketing).
- **Dedicated Ethics Email:** `ethics@nexatech.com` (monitored exclusively by the Ombudsperson and Head of Legal).
- **Postal Mail:** Addressed to:  
  *Chairperson of the Audit Committee,*  
  *NexaTech Solutions Private Limited,*  
  *Tower B, Global Tech Park, Outer Ring Road, Bellandur, Bengaluru 560103, Karnataka, India.*

### 6.3 Absolute Protection Against Retaliation
NexaTech strictly prohibits retaliation, adverse employment action, demotion, subtle harassment, or discriminatory treatment against any whistleblower who in good faith reports an ethical violation.
- Any manager or employee found retaliating against a whistleblower will be subject to immediate termination.
- If a whistleblower feels subjected to subtle retaliation, they must immediately report directly to the Chief People Officer (`cpo@nexatech.com`).

---

## 7. Disciplinary Review and Sanctions
Reports of misconduct are investigated by the Corporate Ethics and Vigilance Committee within 30 business days. Confirmed breaches result in proportional disciplinary sanctions:
1. Formal counseling and written warning placed on official record.
2. Forfeiture of annual performance bonus or stock option vesting.
3. Suspension of duties pending regulatory or forensic investigation.
4. Summary termination of employment for cause without notice or severance pay.
5. Pursuit of criminal prosecution or civil damages for fraud, theft, or intellectual property infringement.
"""

# 5. health_insurance_benefits.md (LONG ~13,000 chars)
docs_batch1["health_insurance_benefits.md"] = """# NexaTech Solutions - Comprehensive Health, Medical & Wellness Benefits Policy
**Document ID:** NT-BEN-POL-005  
**Version:** 4.3  
**Effective Date:** January 1, 2026  
**Owner:** People Operations - Total Rewards & Benefits Team  
**Classification:** Internal - All Employees  

---

## 1. Overview and Philosophy
At NexaTech Solutions ("NexaTech"), the physical, mental, and financial well-being of our workforce and their families is paramount. We sponsor comprehensive medical, accidental, and term life insurance programs, complemented by outpatient allowances, mental health consultations, and preventive healthcare checkups.

This policy outlines coverage tiers, sum insured limits, cashless hospital network procedures, reimbursement claim timelines, and Third-Party Administrator (TPA) escalation pathways.

---

## 2. Group Medical Cover (GMC) - Inpatient Hospitalization

### 2.1 Eligibility and Sum Insured Architecture
All regular full-time employees are automatically enrolled in the Group Medical Insurance scheme from their official date of joining:
- **Base Sum Insured:** **₹5,00,000 INR** per annum on a family floater basis, 100% premium sponsored by NexaTech.
- **Covered Family Composition:** Standard 1+3 or 1+5 structure:
  - Option A: Employee + Spouse + Up to 2 Dependent Children (up to age 25).
  - Option B: Employee + 2 Dependent Parents or Parents-in-Law (subject to payroll co-pay or premium differential).
- **Voluntary Super Top-Up Coverage:**
  Employees can elect to enhance their coverage during the annual benefits enrollment window (January 1-15) or within 30 days of joining:
  - Top-Up Option 1: Additional ₹5,00,000 (Total ₹10,00,000 cover) at ₹3,200/year employee contribution.
  - Top-Up Option 2: Additional ₹10,00,000 (Total ₹15,00,000 cover) at ₹5,800/year employee contribution.
  Deductions are spread equally across 12 monthly payroll cycles.

### 2.2 Coverage Highlights and Key Features
- **Pre-Existing Disease (PED) Waiver:** Covered from Day 1 of enrollment with zero waiting period.
- **First 30-Day Exemption Waiver:** Waived. Coverage applies immediately upon joining.
- **Specific Ailment 1-Year / 2-Year Waiting Period:** Waived for standard corporate policy.
- **Room Rent Capping:**
  - Normal Room: Capped at 1% of Sum Insured per day (e.g., ₹5,000/day for ₹5L base cover). Single private AC room permitted without proportionate deduction if within limit.
  - ICU / CCU Room: Capped at 2% of Sum Insured per day (₹10,000/day for ₹5L base cover).
- **Daycare Procedures:** Over 400 modern daycare procedures (chemotherapy, dialysis, cataract surgery, appendectomy, radiotherapy, angiography) requiring less than 24 hours hospitalization are fully covered.
- **Pre & Post Hospitalization:** Medical expenses incurred 30 days prior to hospital admission and 60 days following formal discharge are reimbursable.

### 2.3 Maternity and Newborn Care Benefits
- **Maternity Normal Delivery Limit:** Up to **₹75,000 INR**.
- **Maternity Caesarean (C-Section) Limit:** Up to **₹1,00,000 INR**.
- **9-Month Waiting Period:** Waived from Day 1.
- **Newborn Baby Cover:** Covered from birth within the family floater sum insured up to the end of the policy period without requiring separate underwriting approval. Mandatory notification to `benefits@nexatech.com` within 30 days of birth with birth certificate.
- **Pre-Natal and Post-Natal Expenses:** Covered up to ₹10,000 within the overall maternity sub-limit.

---

## 3. Outpatient Department (OPD) & Wellness Wallet

### 3.1 Annual OPD & Tele-Consultation Allowance
To encourage preventive care, NexaTech provides an annual OPD and Dental/Vision reimbursement allowance of **₹10,000 INR** per financial year per employee:
- **Eligible Expenses:** Specialist doctor consultations, prescribed diagnostic tests (blood panels, MRIs, ultrasounds), prescription eyeglasses/contact lenses, and preventive dental cleanings/fillings.
- **Ineligible Items:** Cosmetic treatments, teeth whitening, over-the-counter dietary supplements, vitamins without deficiency diagnosis.
- **Claim Process:** Upload GST medical bills and prescription copies via the MediBuddy app under the *NexaWellness OPD Wallet*.

### 3.2 Annual Comprehensive Health Checkup
Employees aged 30 and above are entitled to one fully sponsored executive health checkup annually at partnered diagnostic chains (Apollo Clinics, Manipal Hospitals, SRL Diagnostics, Suburban Diagnostics):
- Includes complete hemogram, lipid profile, HbA1c, liver & renal function panels, thyroid stimulating hormone (TSH), ECG, chest X-ray, and physician consultation.
- Booking is initiated directly through the MediBuddy corporate portal with zero out-of-pocket payment.

---

## 4. Group Personal Accident (GPA) Insurance

NexaTech provides 24/7 global accidental injury and disability insurance:
- **Sum Insured:** **₹25,00,000 INR** (or 2x annual CTC, whichever is higher).
- **Accidental Death:** 100% of Sum Insured paid to designated statutory nominees.
- **Permanent Total Disability (PTD):** 100% to 150% of Sum Insured according to statutory medical injury tables.
- **Permanent Partial Disability (PPD):** Scaled percentage of Sum Insured based on disability percentage certified by a government medical board.
- **Temporary Total Disability (TTD):** Weekly stipend of 1% of Sum Insured (up to ₹15,000/week) for up to 26 weeks if incapacitated from performing work duties.

---

## 5. Group Term Life (GTL) Insurance

To provide robust long-term financial security for employees' families:
- **Coverage:** **3x Annual CTC** (rounded up to the nearest ₹1,00,000), minimum cover of ₹30,00,000 INR.
- **Coverage Scope:** Worldwide, 24 hours a day, covering death due to natural causes, critical illnesses, or accidents.
- **Terminal Illness Advance:** 50% accelerated payout upon diagnosis of a certified terminal condition with life expectancy under 12 months.
- **Nomination:** Employees must keep nominee records updated in NexaPortal under *Profile -> Insurance Nominees*.

---

## 6. Hospitalization and Claims Administration

### 6.1 Cashless Hospitalization Workflow (Network Hospitals)
NexaTech partners with **MediBuddy TPA** (Third-Party Administrator) covering over 10,000 empaneled hospitals across India:
1. **Planned Hospitalization:** Submit pre-authorization request via the MediBuddy Mobile App at least 72 hours prior to admission.
2. **Emergency Hospitalization:** Present the digital MediBuddy e-card and government ID at the hospital's TPA / Insurance desk within 24 hours of admission.
3. The hospital desk coordinates directly with MediBuddy for initial authorization and final discharge claim clearance. The employee pays only non-medical consumable items.

### 6.2 Reimbursement Claim Workflow (Non-Network Hospitals)
If treatment occurs at an unempaneled medical facility:
1. Pay all bills directly upon discharge and collect all original documentation.
2. Mandatory documentation required:
   - Duly signed MediBuddy Reimbursement Claim Form.
   - Original hospital discharge summary detailing clinical history, diagnosis, and treatment.
   - Original itemized hospital final bill with break-up of charges and receipt with revenue stamp.
   - Doctor prescriptions, pharmacy cash memos, and diagnostic test reports with films.
3. **Submission Deadline:** Submit digital claim on MediBuddy app within **15 calendar days** of discharge; physical documents must reach the NexaTech Benefits Desk within **30 calendar days**.

---

## 7. Employee Assistance Program (EAP) & Mental Health
NexaTech believes mental health is as important as physical health. Through our corporate partnership with *1to1Help.net*:
- **Free Confidential Counseling:** Up to 8 free 1-on-1 sessions per year per issue with certified clinical psychologists for employees and immediate family members.
- **Modality:** Video sessions, telephonic consultations, or in-person visits across Bengaluru, Hyderabad, Pune, and Gurugram.
- **Complete Privacy:** NexaTech management has zero visibility into individual session contents, diagnostic notes, or identities.
- **Contact:** Call toll-free 1800-270-1790 or write to `eap@nexatech.com`.

---

## 8. Escalation Matrix and Support Contacts

| Level / Entity | Contact Details | Operating Hours |
|---|---|---|
| **MediBuddy Corporate Helpdesk** | Dedicated Toll-Free: 1800-425-9449 <br> Email: `nexatech.helpdesk@medibuddy.in` | 24/7/365 |
| **NexaTech On-Site Insurance Coordinator** | Mobile: +91-98801-44332 <br> Desk: Level 2, HR Block | Mon-Fri: 9:30 AM - 6:30 PM IST |
| **People Operations Benefits Lead** | Email: `benefits@nexatech.com` | Mon-Fri: 10:00 AM - 5:00 PM IST |
| **Emergency Hospital Escalation** | +91-80-6922-0999 (24/7 Emergency Line) | Immediate 15-Minute Response |
"""

# 6. wfh_quick_reference.md (SHORT ~1,600 chars)
docs_batch1["wfh_quick_reference.md"] = """# NexaTech Solutions - Work From Home (WFH) Quick Reference Cheat-Sheet
**Document ID:** NT-OPS-SOP-006  
**Version:** 3.0  
**Effective Date:** January 1, 2026  
**Owner:** Workplace Solutions & People Operations  
**Classification:** Internal - All Employees  

---

## 1. Core Hybrid Framework at a Glance
NexaTech operates a structured **3+2 Hybrid Model**:
- **In-Office Days:** 3 days per week (Core team days: Tuesday & Thursday; 3rd day chosen with your Delivery Manager).
- **Remote Days:** Up to 2 days per week from your approved registered home location.
- **Core Collaboration Window:** 10:00 AM to 4:00 PM IST. You must be available on Slack and responsive within 30 minutes.

---

## 2. Daily Check-in & Presence Requirements
- **Slack Status:** Set your Slack status to 💻 *Working Remotely* or 🏢 *In Office - [City]* upon starting your workday.
- **Standups:** Attend daily standup calls with camera enabled unless bandwidth restrictions occur.
- **Calendar Visibility:** Keep your Google Calendar updated with working hours, focus blocks, and lunch breaks.

---

## 3. Remote Work Allowances & Claims
- **Monthly Broadband Allowance:** Up to **₹1,500 INR** per month reimbursable via NexaPortal Expense Module under *Internet Reimbursement* with monthly provider tax invoice.
- **One-time Ergonomic Setup Allowance:** Up to **₹15,000 INR** for confirmed employees (desk, ergonomic chair, monitor stand). Reimbursable within first 90 days of confirmation.

---

## 4. Emergency WFH Escalation
If you face sudden illness, family emergencies, or civic transit disruptions:
1. Notify your Reporting Manager via Slack or email by 9:00 AM IST.
2. Mark your status in NexaPortal as *Ad-hoc Remote Work*.
3. For medical or prolonged WFH requests (>3 consecutive days outside the 3+2 schedule), email `peopleops@nexatech.com` with manager sign-off.
"""

# 7. emergency_contacts.md (SHORT ~1,600 chars)
docs_batch1["emergency_contacts.md"] = """# NexaTech Solutions - 24/7 Corporate Emergency Contacts & Escalation Directory
**Document ID:** NT-SEC-REF-007  
**Version:** 4.0  
**Effective Date:** January 1, 2026  
**Owner:** Physical Security, Facilities & Cyber Defense Center  
**Classification:** Public Internal  

---

## 1. Central Emergency Hotlines (24/7/365)
In the event of medical emergencies, fire, physical threats, or severe facility incidents, immediately dial:
- **Central Security Operations Center (CSOC):** **+91-80-6922-0001** (Direct Extension: 1111)
- **Medical Emergency Ambulance Dispatch:** **+91-80-6922-0999** (Direct Extension: 9999)
- **Cyber Defense Incident Response Desk:** **+91-80-6922-0911** (Direct Extension: 9110)
- **Anonymous Whistleblower / Crisis Line:** **+91-80-6900-5555**

---

## 2. Campus Facilities & Security Leads
| Campus Location | Facility Head | Direct Contact | Email Address |
|---|---|---|---|
| **Bengaluru (HQ - Global Tech Park)** | Rajesh Kumar Nair | +91-98450-11223 | `blr.facilities@nexatech.com` |
| **Hyderabad (HITEC City - Cyber Pearl)** | Suresh Konduru | +91-99890-44556 | `hyd.facilities@nexatech.com` |
| **Pune (Hinjewadi Phase 2)** | Amit Deshmukh | +91-97640-77889 | `pune.facilities@nexatech.com` |
| **Gurugram (Cyber City Building 10)** | Vikram Chaudhary | +91-98110-33221 | `ggn.facilities@nexatech.com` |

---

## 3. Municipal Emergency Services (India)
- **National Police Emergency Helpline:** 112
- **Fire & Rescue Services:** 101
- **Ambulance Services:** 108 / 102
- **Women's Safety Helpline:** 1091 / 181
- **Cyber Crime National Reporting Portal:** 1930 / `cybercrime.gov.in`
"""

# 8. dress_code_guidelines.md (SHORT ~1,500 chars)
docs_batch1["dress_code_guidelines.md"] = """# NexaTech Solutions - Workplace Attire & Professional Presentation Guidelines
**Document ID:** NT-HR-GDE-008  
**Version:** 2.1  
**Effective Date:** January 1, 2026  
**Owner:** People Operations  
**Classification:** Internal - All Employees  

---

## 1. Purpose & General Principles
NexaTech embraces a modern, comfortable, and productive work culture while projecting professional credibility to enterprise clients and international visitors. Our dress code is grounded in common sense, neatness, and mutual respect.

---

## 2. Daily Dress Code Standards
- **Monday through Thursday (Business Casual):**
  - Collared shirts, polo shirts, tailored blouses, knit sweaters, kurtas, formal dresses, slacks, chinos, dark well-fitted denim jeans (free of rips or distressing).
  - Footwear: Leather shoes, loafers, dress flats, smart ankle boots, clean tailored sneakers.
- **Casual Fridays (Smart Casual):**
  - Solid or tasteful graphic t-shirts (free of political, offensive, or controversial slogans), hoodies, jeans, stylish sneakers, and comfortable footwear.
- **Client Engagements & Executive Board Meetings:**
  - Business Formal: Tailored suits, blazers, dress shirts with trousers, formal Indian ethnic wear (sarees, formal suits). Always match the client's corporate culture when visiting client sites.

---

## 3. Unacceptable Workplace Attire
The following items are not permitted on campus:
- Beachwear, rubber flip-flops, torn/ripped distressed jeans, workout gym tank tops, athletic sweatpants, midriff-baring clothing, and slippers.
- Any attire containing derogatory, profane, discriminatory, or politically partisan prints.

---

## 4. Technical Labs & Data Centers
Personnel working in server rooms, hardware testing labs, or network switch rooms must wear closed-toe flat shoes with rubber soles and avoid loose hanging jewelry or lanyards that could pose snagging hazards around electrical racks.
"""

# 9. visitor_policy.md (SHORT ~1,500 chars)
docs_batch1["visitor_policy.md"] = """# NexaTech Solutions - Corporate Campus Visitor and Guest Access Policy
**Document ID:** NT-FAC-POL-009  
**Version:** 3.1  
**Effective Date:** January 1, 2026  
**Owner:** Workplace Solutions & Physical Security  
**Classification:** Internal - All Employees  

---

## 1. Purpose and Protocol
To protect enterprise assets, intellectual property, and client confidentiality, all visitors to NexaTech Solutions campuses—including client delegations, interview candidates, vendors, contractors, and personal guests—must adhere to strict access protocols.

---

## 2. Visitor Registration and Verification
1. **Host Pre-Registration:** Hosts should pre-register visitors on the *NexaVisitor Portal* at least 24 hours prior to arrival to expedite security clearances.
2. **Reception Check-In:** Visitors must present a valid government-issued photo ID (Aadhaar, Passport, Driving License, Voter ID) at the security reception desk.
3. **Visitor Badge Issuance:** Visitors receive a color-coded physical visitor badge that must be worn visibly on their upper torso at all times.
4. **Non-Disclosure Agreement (NDA):** Client representatives, audit teams, and technical contractors must sign the digital visitor NDA on the reception iPad before entry.

---

## 3. Escort and Movement Rules
- **Continuous Escort:** Visitors must be escorted by their NexaTech host or a designated delegate at all times. Visitors must never be left unchaperoned in work bays or corridors.
- **Restricted Areas:** Visitors are strictly barred from entering server rooms, secure ODC (Offshore Development Center) bays, finance archives, and executive switch rooms without specific CISO approval.
- **Photography Ban:** Photography, video recording, or audio capture is strictly prohibited across all office premises.

---

## 4. Departure and Badge Surrender
Upon concluding the visit, the host must escort the guest to reception. The visitor badge must be surrendered to the security desk. Security logs the official checkout timestamp.
"""

# 10. lost_and_found_policy.md (SHORT ~1,400 chars)
docs_batch1["lost_and_found_policy.md"] = """# NexaTech Solutions - Lost, Found and Unattended Property Policy
**Document ID:** NT-FAC-SOP-010  
**Version:** 2.0  
**Effective Date:** January 1, 2026  
**Owner:** Facilities & Workplace Solutions  
**Classification:** Internal - All Employees  

---

## 1. Purpose and Custody Protocols
This policy establishes standard handling procedures for personal or corporate property discovered unattended or reported missing within NexaTech office buildings, cafeterias, parking structures, and transit shuttles.

---

## 2. Reporting and Turning in Found Items
- Any employee finding an unattended or lost item must surrender it to the **Central Facilities Desk** (Ground Floor Security Office) within **2 hours** of discovery.
- Facilities logs the item in the *Lost & Found Asset Ledger* documenting: date, exact location found, item description, serial numbers (if applicable), and finder details.
- High-value electronic assets (laptops, phones, smartwatches, jewelry, wallets, identity cards) are placed in a secure fireproof safe under dual-custody combination locks.

---

## 3. Claiming Lost Property
- Owners seeking to retrieve lost property must visit the Facilities Desk between 10:00 AM and 5:00 PM IST on business days.
- Claimants must provide proof of ownership: unlocking passcode for electronic devices, matching serial numbers, or detailed description of contents.
- Claimants must sign the property release ledger with employee ID and date.

---

## 4. Retention and Disposal Timelines
- **Government IDs & Bank Cards:** Held for 14 calendar days; if unclaimed, bank cards are destroyed and IDs forwarded to municipal police lost property cells.
- **High-Value Electronics:** Held for 60 calendar days. If unclaimed, company property is re-imaged by IT; personal electronics are surrendered to local authorities.
- **Clothing & General Articles:** Held for 30 calendar days, after which they are donated to verified charitable partner NGOs.
"""

for filename, content in docs_batch1.items():
    file_path = DOCS_DIR / filename
    file_path.write_text(content.strip(), encoding="utf-8")
    print(f"Written: {filename} ({len(content)} chars)")

print("Batch 1 Complete: 10 files written.")
