import os
from pathlib import Path

DOCS_DIR = Path("docs")
DOCS_DIR.mkdir(parents=True, exist_ok=True)

docs_batch9 = {}

# 81. internship_program_guidelines.md (MEDIUM ~5,100 chars)
docs_batch9["internship_program_guidelines.md"] = """# NexaTech Solutions - University Internship & Apprenticeship Guidelines
**Document ID:** NT-TA-GDE-081  
**Version:** 3.1  
**Effective Date:** January 1, 2026  
**Owner:** University Relations & Emerging Talent Guild  
**Classification:** Internal - All Personnel  

---

## 1. Program Mission & Scope
The NexaTech Emerging Talent Program partners with premier Indian and international engineering institutes (IITs, NITs, BITS, IIITs) to nurture future technology leaders. We provide immersive, real-world engineering apprenticeships where interns contribute directly to production microservices, distributed data pipelines, and generative AI research.

This document details stipend structures, project mentorship, conversion criteria, and working guidelines for interns.

---

## 2. Internship Tracks and Monthly Stipends

NexaTech operates two distinct university internship tracks:
- **Summer Technology Internship (2 to 3 Months):** Targeted at pre-final year engineering students during university summer recesses (May to July).
  - Monthly Stipend: **₹35,000 INR** per month.
- **Semester / Graduate Apprenticeship (6 Months):** Targeted at final-year students completing full-time capstone degree requirements (January to June).
  - Monthly Stipend: **₹45,000 INR** per month.
- **Benefits Issued:** High-performance engineering laptop (Apple MacBook Pro or Dell XPS 15), corporate email and Slack access, subsidized cafeteria meals, and free access to campus wellness and gym centers.

---

## 3. Mentorship and Engineering Deliverables
- **Assigned Mentor:** Every intern is assigned a dedicated Senior SDE (Band 3) who conducts bi-weekly 1-on-1 progress reviews, reviews code pull requests, and unblocks technical challenges.
- **Capstone Project:** Each intern is assigned an end-to-end production-grade user story or internal accelerator module. The intern must demo their completed deliverable at the *Emerging Talent Demo Day* in their final month before Practice Leadership.

---

## 4. Pre-Placement Offer (PPO) Conversion Process
Outstanding interns are extended formal Pre-Placement Offers (PPOs) for full-time employment as Associate Software Engineers (Band 1):
1. **Evaluation Criteria:**
   - Technical execution, code quality, and test coverage on assigned capstone story.
   - Adherence to PRISM core values and proactive team collaboration.
   - Final capstone technical presentation scorecard (minimum 80% passing grade).
2. **PPO Announcement:** PPO letters are issued within **14 calendar days** following the internship conclusion date, guaranteeing a confirmed full-time joining date upon degree completion.
"""

# 82. contractor_and_vendor_staffing.md (MEDIUM ~4,900 chars)
docs_batch9["contractor_and_vendor_staffing.md"] = """# NexaTech Solutions - Contingent Workforce & Staff Augmentation Policy
**Document ID:** NT-HR-POL-082  
**Version:** 3.3  
**Effective Date:** February 1, 2026  
**Owner:** Vendor Management Office (VMO) & Talent Operations  
**Classification:** Internal - Management Personnel  

---

## 1. Purpose and Contingent Labor Governance
To manage fluctuating client sprint capacity, seasonal workload surges, and highly specialized niche skill requirements, NexaTech engages contingent contractors, agency staff, and third-party independent consultants.

This policy governs the requisition, background screening, access control, co-employment risk mitigation, and full-time conversion protocols for contingent personnel.

---

## 2. Requisition and Agency Engagement
- **Engagement Channel:** All contingent staff requisitions must be processed through the central Vendor Management Office (VMO) via email at `contingent@nexatech.com` and logged in the Fieldglass VMS portal.
- **Empaneled Agencies:** Contractors may be sourced exclusively from pre-vetted, empaneled staffing agencies who have executed the NexaTech Master Staffing Agreement.
- **Background Verification Mandate:** 100% of contingent contractors must clear mandatory background screening (education, prior employment, criminal record check) conducted by First Advantage (FADV) prior to being issued physical facility badges or electronic system logins.

---

## 3. Co-Employment Guardrails & Workplace Distinctions
To comply with the Contract Labour (Regulation and Abolition) Act, 1970 and mitigate legal co-employment risks:
- Contractors must not receive corporate performance appraisals, attend internal company all-hands meetings, or receive corporate stock appreciation options.
- Contractor compensation, leave administration, statutory PF/ESI, and payroll deductions are handled exclusively by their third-party agency employer.
- Contractors receive distinctive grey corporate lanyards and email signatures displaying `[Contractor - Agency Name]`.

---

## 4. Conversion to Regular Full-Time Employment
High-performing contractors may be converted to regular full-time NexaTech employees subject to:
1. Completion of at least **6 continuous months** of exemplary performance on NexaTech client deliverables.
2. Formal clearance through standard engineering technical interview panels.
3. Written commercial release from the staffing agency without disputed agency finder fee penalties.
"""

# 83. wellness_employee_assistance_program.md (MEDIUM ~5,200 chars)
docs_batch9["wellness_employee_assistance_program.md"] = """# NexaTech Solutions - Employee Assistance Program (EAP) & Mental Health Guide
**Document ID:** NT-WEL-GDE-083  
**Version:** 3.4  
**Effective Date:** January 1, 2026  
**Owner:** People Operations & Workplace Well-Being Guild  
**Classification:** Internal - All Employees  

---

## 1. Holistic Mental Well-Being Commitment
High-performance engineering and client delivery can be intellectually and emotionally demanding. At NexaTech, mental health is recognized as an integral component of overall human well-being. We partner with India's leading clinical wellness provider, **1to1Help.net**, to provide confidential, professional counseling and psychological support.

---

## 2. Core EAP Service Offerings
All regular full-time employees, contractors, and their immediate dependent family members (spouse, children, parents) have 24/7 access to:
- **Individual Psychological Counseling:** Up to **8 free 1-on-1 clinical sessions** per issue per year with certified clinical psychologists and psychotherapists.
- **Specialized Consultation Pillars:**
  - Stress, anxiety, burnout, and depression management.
  - Marital, relationship, and parenting challenges.
  - Grief, bereavement, and trauma counseling.
  - Personal financial planning, debt management, and legal advisory.
- **Consultation Modalities:** Confidential telephonic hotlines, encrypted video sessions, or in-person clinical consultations across Bengaluru, Hyderabad, Pune, and Gurugram clinics.

---

## 3. Absolute Confidentiality Covenant
- **Zero Visibility to Management:** NexaTech management, HRBPs, and leadership have **zero visibility** into who accesses EAP services, session contents, or psychological notes.
- Inquiries and session history are completely segregated from employee personnel files, performance appraisals, and promotion evaluations.

---

## 4. Mental Wellness Days & Campus Quiet Pods
- **NexaWellness Days:** NexaTech observes two corporate-wide paid *NexaWellness Days* per calendar year (one in Q2, one in Q4) where all client deliveries pause to encourage personal rest and outdoor rejuvenation.
- **Campus Relaxation & Zen Zones:** Each delivery center provides soundproof meditation pods and quiet rooms equipped with massage chairs, dimmable circadian lighting, and guided mindfulness audio stations.
- **Contact:** Call toll-free **1800-270-1790** or download the *1to1Help* app using corporate passkey `NEXATECH-WELLNESS`.
"""

# 84. csr_volunteering_policy.md (MEDIUM ~4,800 chars)
docs_batch9["csr_volunteering_policy.md"] = """# NexaTech Solutions - Corporate Social Responsibility (CSR) & Community Volunteering Policy
**Document ID:** NT-CSR-POL-084  
**Version:** 3.1  
**Effective Date:** January 1, 2026  
**Owner:** NexaCare Foundation & CSR Committee of the Board  
**Classification:** Internal - All Personnel  

---

## 1. Mission of the NexaCare Foundation
In compliance with Section 135 of the Companies Act, 2013, NexaTech Solutions directs at least 2% of average net profits to impactful social initiatives through the **NexaCare Foundation**. Our philanthropic initiatives focus on:
- STEM education and coding literacy for underprivileged rural children.
- Environmental sustainability, urban afforestation, and water body rejuvenation.
- Digital enablement for women self-help groups and differently-abled youth.

---

## 2. Paid Community Volunteering Leave
To encourage active civic engagement, NexaTech grants every confirmed employee:
- **2 Working Days of Paid Volunteering Leave** per calendar year (in addition to standard annual leave entitlements).
- **Eligible Activities:** Participating in verified NexaCare NGO programs, volunteering at municipal schools, participating in urban tree planting drives, or providing technical mentorship to non-profit organizations.
- **Application:** Log volunteering leave on NexaPortal under *NexaCare Volunteering* accompanied by photographic proof or a volunteer certificate from the partner NGO.

---

## 3. Employee Donation Matching Program
- When an employee donates personal funds to an approved Section 80G-certified charitable foundation (e.g., Akshaya Patra, Teach for India, GiveIndia, Pratham):
- NexaTech matches the employee's contribution **rupee-for-rupee up to ₹10,000 INR** per employee per financial year.
- Submit proof of donation via the NexaPortal CSR desk to initiate matching disbursement.
"""

# 85. recreation_clubs_sports_allowance.md (MEDIUM ~4,700 chars)
docs_batch9["recreation_clubs_sports_allowance.md"] = """# NexaTech Solutions - Employee Recreation, Sports Guilds & Fitness Subsidy Policy
**Document ID:** NT-WEL-POL-085  
**Version:** 2.4  
**Effective Date:** January 1, 2026  
**Owner:** People Operations & Employee Culture Council  
**Classification:** Internal - All Employees  

---

## 1. Purpose and Campus Vitality
Physical vitality, camaraderie, and team sports foster creative problem-solving and relieve engineering stress. NexaTech actively sponsors employee sports guilds, recreational clubs, and personal fitness memberships.

---

## 2. Monthly Gym & Fitness Membership Subsidy
- **Subsidy Quantum:** NexaTech reimburses up to **₹1,000 INR per month** toward active gym memberships, yoga studios, swimming pool access, or certified martial arts classes.
- **Claim Process:** Upload quarterly gym tax invoices on NexaPortal Expense Module under *Fitness & Health Subsidy*.
- **On-Campus Fitness Centers:** All delivery centers feature fully equipped, air-conditioned employee gyms featuring certified personal trainers, showers, and steam rooms, accessible free of charge between 6:00 AM and 10:00 PM IST.

---

## 3. NexaSports Guilds & Annual Tournaments
NexaTech funds and supports official employee-run sports clubs:
- **Active Guilds:** Cricket Guild, Football / Futsal League, Badminton Club, Table Tennis Squad, Chess & Esports League, and NexaRunners Marathon Club.
- **Club Budgets:** Each recognized guild receives an annual operating grant of **₹1,50,000 INR** for court rentals, professional coaching, and tournament kits.
- **The NexaOlympics:** Annual inter-office sports championship held every November, where teams from Bengaluru, Hyderabad, Pune, and Gurugram compete for the Chairman's Trophy.
"""

# 86. patent_incentive_and_innovation_awards.md (MEDIUM ~5,200 chars)
docs_batch9["patent_incentive_and_innovation_awards.md"] = """# NexaTech Solutions - Innovation Grants, Hackathons & Technical Awards Policy
**Document ID:** NT-ENG-POL-086  
**Version:** 3.2  
**Effective Date:** February 1, 2026  
**Owner:** Office of the CTO & Engineering Excellence Committee  
**Classification:** Internal - Technical Staff  

---

## 1. Cultivating an Engineering-First Culture
NexaTech was founded by software engineers for software engineers. We celebrate audacious technical experimentation, novel algorithmic research, and transformative engineering breakthroughs that provide competitive moats for our clients.

---

## 2. NexaHack: The Annual 48-Hour Hackathon
Held annually in September, **NexaHack** is our flagship global hackathon:
- Engineers, designers, and product managers form cross-functional squads to build working software prototypes over 48 continuous hours.
- **Prize Pool:**
  - *1st Place (Grand Champion):* **₹3,00,000 INR cash prize** + Guaranteed incubation funding.
  - *2nd Place (Runner-Up):* **₹1,50,000 INR cash prize**.
  - *3rd Place (Innovation Pick):* **₹75,000 INR cash prize**.
- Winning prototypes with strong commercial viability are assigned a dedicated 90-day incubation team to transition the codebase into an enterprise accelerator.

---

## 3. Quarterly CTO Innovation Fellowship & Cash Grants
- Every calendar quarter, the Office of the CTO selects up to three exceptional engineering proposals for the **NexaTech Innovation Fellowship**.
- **Grant Quantum:** Up to **₹1,50,000 INR** in dedicated cloud infrastructure credits (AWS/Azure GPU clusters) and 20% dedicated sprint time for 3 months to develop an approved research prototype.
- Fellows present their findings at the annual *NexaTech Global Tech Summit*.
"""

# 87. environment_health_safety_ehs.md (MEDIUM ~4,900 chars)
docs_batch9["environment_health_safety_ehs.md"] = """# NexaTech Solutions - Environmental Health, Occupational Safety & Campus Emergency SOP
**Document ID:** NT-EHS-SOP-087  
**Version:** 3.3  
**Effective Date:** January 1, 2026  
**Owner:** Workplace Solutions & Environmental Health & Safety (EHS)  
**Classification:** Internal - All Personnel  

---

## 1. Safety Commitment and Environmental Vision
NexaTech Solutions ("NexaTech") is committed to operating safe, hazard-free, and sustainable campuses certified under ISO 45001 (Occupational Health & Safety) and ISO 14001 (Environmental Management). We maintain zero tolerance for unsafe workplace practices.

---

## 2. Emergency Evacuation & Fire Safety Protocols
- **Fire Wardens:** Each wing on every floor has two designated, trained employee Fire Wardens identified by fluorescent vests during emergency alerts.
- **Evacuation Drills:** Mandatory fire and earthquake evacuation drills are conducted **twice per calendar year** at all delivery centers. Full building evacuation must achieve a target evacuation time under **8 minutes**.
- **Assembly Points:** In the event of a continuous alarm siren, evacuate immediately via the nearest fire exit stairs (never use elevators) and assemble at the designated *External Campus Assembly Area*.

---

## 3. Medical First Aid & EMT Stations
- **24/7 Campus Medical Room:** Located on Floor 1 of each delivery center, staffed by a certified Occupational Health Nurse and on-call Emergency Medical Technician (EMT).
- **Automated External Defibrillators (AEDs):** AED units are installed near every central lift lobby, with trained security personnel certified in Cardiopulmonary Resuscitation (CPR).
- **Ambulance Standby:** A fully equipped BLS (Basic Life Support) ambulance is permanently stationed on-site at Bengaluru, Hyderabad, and Pune campuses.
"""

# 88. car_lease_policy.md (MEDIUM ~5,000 chars)
docs_batch9["car_lease_policy.md"] = """# NexaTech Solutions - Corporate Executive Car Lease Policy
**Document ID:** NT-FIN-POL-088  
**Version:** 3.1  
**Effective Date:** January 1, 2026  
**Owner:** Total Rewards, Finance & Taxation Operations  
**Classification:** Internal - Management Staff (Band 4+)  

---

## 1. Purpose and Program Overview
To optimize direct tax liabilities and provide executive mobility benefits, NexaTech offers a tax-efficient Corporate Car Lease Scheme in partnership with premier fleet leasing providers (e.g., LeasePlan, ALD Automotive, ORIX India).

---

## 2. Eligibility & Vehicle Budget Slabs
The scheme is available to confirmed full-time managerial employees in Bands 4 and above:

| Employee Band / Level | Maximum Permissible Ex-Showroom Vehicle Value | Lease Tenure Options |
|---|---|---|
| **Band 4 (Lead SDE / Engineering Manager)** | Up to **₹15,00,000 INR** | 36, 48, or 60 Months |
| **Band 5 (Principal Architect / Director)** | Up to **₹25,00,000 INR** | 36, 48, or 60 Months |
| **Band 6+ (Vice President / Practice Head)** | Up to **₹45,00,000 INR** | 36, 48, or 60 Months |

---

## 3. Tax Optimization and Payroll Restructuring
- The monthly vehicle lease rental is deducted directly from the employee's pre-tax Special Allowance component, reducing taxable gross income.
- **Driver & Fuel Allowances:**
  - Fuel and maintenance reimbursement: Up to **₹8,000 INR per month** (subject to monthly fuel tax invoices).
  - Professional driver salary reimbursement: Up to **₹15,000 INR per month** (subject to driver payment declaration and driving license verification).

---

## 4. Separation or Resignation During Active Lease
If an employee resigns while an active car lease is underway:
1. **Option A (Foreclosure & Purchase):** Settle the outstanding principal balance and foreclosure charges directly with the leasing company to transfer vehicle ownership to their personal name.
2. **Option B (Lease Transfer):** Transfer the active lease to their new employer, subject to the new employer's corporate lease policies and fleet lessor approval.
"""

# 89. telecom_mobile_handset_reimbursement.md (MEDIUM ~4,800 chars)
docs_batch9["telecom_mobile_handset_reimbursement.md"] = """# NexaTech Solutions - Corporate Mobile Handset & Cellular Reimbursement Policy
**Document ID:** NT-IT-POL-089  
**Version:** 3.3  
**Effective Date:** January 1, 2026  
**Owner:** IT Infrastructure, Enterprise Mobility & Procurement  
**Classification:** Internal - Eligible Roles  

---

## 1. Scope and Mobile Enablement
Certain job roles—including 24/7 Incident Commanders, On-Call SRE Leads, Field Sales Executives, and Executive Directors—require reliable, high-grade mobile smartphones to triage high-severity outages and maintain continuous client connectivity.

---

## 2. Handset Procurement Allowance Slabs

Eligible staff may purchase a corporate smartphone and claim reimbursement up to the approved ceiling:

| Job Role / Profile | Handset Reimbursement Ceiling (INR) | Refresh Frequency |
|---|---|---|
| **Incident Commanders & SRE Primary Leads** | Up to **₹35,000 INR** | Every 24 Months |
| **Account Executives & Sales Directors** | Up to **₹50,000 INR** | Every 24 Months |
| **Vice Presidents & Executive Leadership (Band 6+)** | Up to **₹85,000 INR** | Every 24 Months |

*Note: Handsets must be purchased in the employee's personal name with a valid GST invoice; corporate MDM (Microsoft Intune) must be enrolled within 48 hours of purchase.*

---

## 3. Monthly Mobile Bill Reimbursement
- Eligible employees receive a corporate SIM card or claim reimbursement up to **₹1,200 INR per month** against personal postpaid telecom bills (voice and minimum 50GB 5G data).
- Upload postpaid bills on NexaPortal Expense Module under *Mobile Reimbursement* within 30 days of bill generation.
"""

# 90. relocation_deputation_overseas_policy.md (MEDIUM ~5,400 chars)
docs_batch9["relocation_deputation_overseas_policy.md"] = """# NexaTech Solutions - Global Mobility & Overseas Client Deputation Policy
**Document ID:** NT-HR-POL-090  
**Version:** 4.2  
**Effective Date:** February 1, 2026  
**Owner:** Global Mobility Desk, Legal Immigrations & Taxation  
**Classification:** Confidential - International Travel & Deputation  

---

## 1. Overview and International Strategic Presence
To support on-site architectural delivery and client stakeholder management, NexaTech deputes engineering specialists to client locations in North America (San Jose, New York, Seattle), the United Kingdom (London), and the European Union.

This policy governs visa facilitation, overseas allowances, housing stipends, tax equalization, and repatriation protocols.

---

## 2. Deputation Categories and Visa Sponsorship
- **Short-Term Business Travel (Under 90 Days):** Processed on commercial business visitor visas (US B-1, UK Standard Visitor, Schengen Business). Governed by daily per diems specified in `travel_expense_reimbursement.md`.
- **Long-Term Deputation (Over 90 Days):** Sponsored under appropriate work authorizations (e.g., US L-1A/L-1B intra-company transfer, H-1B, UK Senior Specialist Worker visa).
- **Immigration Costs:** 100% of visa filing fees, legal petition drafting fees, premium processing charges, and biometric fees are borne directly by NexaTech.

---

## 3. Overseas Compensation, Per Diems & Housing
Employees on long-term international deputation transition to the **NexaTech International Deputation Pay Structure**:
- **Base Gross Salary:** Adjusted to local geographic market prevailing wages in compliance with US Department of Labor / UK Home Office prevailing wage thresholds.
- **Relocation Transit Allowance:** One-time settling-in allowance of **$3,000 USD** (or £2,500 GBP) disbursed on Day 1 upon arrival.
- **Initial Corporate Lodging:** NexaTech Corporate Travel Desk provides up to **21 calendar days of furnished corporate apartment stay** upon arrival to allow time to secure personal residential leasing.

---

## 4. Tax Equalization Policy
NexaTech enforces strict **Tax Equalization** for long-term international assignees:
- Assignees pay no more and no less total tax (home + host country) than they would have incurred had they remained employed in India.
- NexaTech retains an international accounting consultancy (PwC / EY) to prepare and file both host-country and Indian tax returns at zero cost to the employee.
"""

for filename, content in docs_batch9.items():
    file_path = DOCS_DIR / filename
    file_path.write_text(content.strip(), encoding="utf-8")
    print(f"Written: {filename} ({len(content)} chars)")

print("Batch 9 Complete: 10 files written.")
