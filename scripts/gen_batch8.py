import os
from pathlib import Path

DOCS_DIR = Path("docs")
DOCS_DIR.mkdir(parents=True, exist_ok=True)

docs_batch8 = {}

# 71. procurement_vendor_selection.md (MEDIUM ~5,100 chars)
docs_batch8["procurement_vendor_selection.md"] = """# NexaTech Solutions - Corporate Procurement & Vendor Selection Policy
**Document ID:** NT-FIN-POL-071  
**Version:** 3.4  
**Effective Date:** January 1, 2026  
**Owner:** Strategic Sourcing, Procurement & Accounts Payable  
**Classification:** Internal - All Employees  

---

## 1. Principles of Enterprise Sourcing
NexaTech Solutions ("NexaTech") procures software, cloud infrastructure, hardware assets, professional consulting, and facilities services to empower high-velocity business delivery. All purchasing decisions must uphold transparency, fiscal prudence, competitive fair bidding, and full anti-corruption compliance.

---

## 2. Competitive Quotation Thresholds
Purchasing thresholds determine mandatory vendor quotation requirements:

| Purchase Order Value (INR) | Minimum Competitive Quotations Required | Mandatory Approval Authorities |
|---|---|---|
| **Tier 1: Up to ₹50,000** | 1 Verified Quotation (Direct Purchase) | Department Head / Practice Manager |
| **Tier 2: ₹50,001 to ₹2,50,000** | **2 Competitive Written Quotations** | Practice Head + Procurement Manager |
| **Tier 3: ₹2,50,001 to ₹10,00,000** | **3 Competitive Written Quotations** | Finance Controller + Strategic Sourcing Head |
| **Tier 4: > ₹10,00,000 (Major Capex)** | Formal RFP Process (3+ Sealed Bids) | Chief Financial Officer (CFO) + CEO |

---

## 3. Purchase Orders (PO) & Contracting
- **No PO, No Pay Mandate:** No commercial engagement may commence without an approved Purchase Order issued by the Procurement Desk (`procurement@nexatech.com`). Invoices submitted without an associated PO number will be rejected by Accounts Payable.
- **Master Vendor Agreement (MVA):** Recurring service providers must execute the standardized NexaTech MVA including confidentiality, anti-bribery covenants, and minimum 45-day payment credit terms.

---

## 4. Vendor Onboarding and Due Diligence
Before any new supplier is issued a PO:
1. Vendor must submit GST Registration Certificate, PAN Card copy, MSME Udyam registration (if applicable), and verified cancelled corporate bank cheque.
2. Global sanctions screening against OFAC, UN, and Indian regulatory watchlists.
3. Information security review for vendors handling electronic data.
"""

# 72. facility_and_seat_booking_policy.md (MEDIUM ~4,800 chars)
docs_batch8["facility_and_seat_booking_policy.md"] = """# NexaTech Solutions - Workplace Facilities & Workspace Seat Reservation Policy
**Document ID:** NT-FAC-POL-072  
**Version:** 3.1  
**Effective Date:** January 1, 2026  
**Owner:** Workplace Solutions & Physical Operations  
**Classification:** Internal - All Employees  

---

## 1. Context and Modern Workplace Design
NexaTech operates activity-based, agile delivery centers across Bengaluru, Hyderabad, Pune, and Gurugram. Our offices feature open collaboration bays, quiet focus pods, agile standup spaces, and ergonomic workstations.

This policy governs desk reservation protocols, hot-desking etiquette, and physical workspace allocations.

---

## 2. Seat Reservation Architecture (NexaSpace App)
- **Advance Booking Window:** Employees may reserve workstations up to **7 calendar days in advance** via the *NexaSpace* mobile app or web portal (`space.nexatech.internal`).
- **Check-In Requirement:** Upon arriving at the assigned workstation, the employee must scan the desk's physical QR code within **45 minutes** of the reserved start time.
- **Auto-Release Policy:** Desks not scanned within 45 minutes of scheduled reservation are automatically released to the shared hot-desk pool, and a reminder notice is sent to the employee.

---

## 3. Dedicated vs. Shared Desks
- **Shared Agile Desks (Default):** 85% of office workstations operate on the shared hot-desk model to support our 3+2 hybrid schedule.
- **Dedicated Seating:** Permanent dedicated desks are assigned exclusively to:
  1. Hardware engineering labs requiring specialized oscilloscopes and soldered test rigs.
  2. Secured Offshore Development Centers (ODCs) with contractual physical isolation requirements.
  3. Physical Security Central Command and IT Helpdesk triage teams.

---

## 4. Clean Desk & Daily Workplace Etiquette
- At the conclusion of each working day, workstations must be cleared of all personal items, coffee cups, food containers, and handwritten project notes.
- Personal items may be stored in assigned biometric lockers located on each floor. Facilities clears unreserved desks nightly at 9:00 PM IST; abandoned personal items are transferred to Lost & Found.
"""

# 73. meeting_room_and_av_equipment.md (MEDIUM ~4,700 chars)
docs_batch8["meeting_room_and_av_equipment.md"] = """# NexaTech Solutions - Meeting Room Governance & Audio-Visual Equipment Policy
**Document ID:** NT-FAC-POL-073  
**Version:** 2.4  
**Effective Date:** January 1, 2026  
**Owner:** Facilities & Collaboration Engineering  
**Classification:** Internal - All Personnel  

---

## 1. Principles of Collaboration Spaces
Meeting rooms, executive boardrooms, and video conference facilities represent high-demand communal resources. Efficient booking practices and mindful room stewardship ensure productive collaboration across distributed time zones.

---

## 2. Meeting Room Reservation Rules
- **Booking Channel:** Meeting rooms must be reserved through Google Calendar by inviting the specific room resource (e.g., `blr-t2-room-aryabhata@nexatech.com`).
- **Maximum Duration:** Single meeting sessions are capped at **2 continuous hours**. All-day workshops or sprint retrospectives exceeding 2 hours require facility coordinator approval (`facilities@nexatech.com`).
- **Ghost Meeting Auto-Release:** If meeting participants do not tap the Cisco/Logitech Touch Controller within **10 minutes** of scheduled start time, the room reservation is automatically canceled by calendar integration and made available to others.

---

## 3. Audio-Visual (AV) Equipment Stewardship
All conference rooms feature standardized collaboration technology:
- Logitech Rally Plus / Poly Studio 4K video conference cameras with auto-framing.
- Dual 65-inch or 75-inch 4K commercial displays.
- High-sensitivity ceiling beamforming microphone arrays.
- **Equipment Care:** Employees must not unplug, reroute, or modify conference room HDMI cables, USB-C adapters, or switch configurations.
- **Technical Faults:** Report any AV faults immediately via Slack bot `#room-av-support` for 5-minute technician dispatch.
"""

# 74. learning_development_certifications.md (MEDIUM ~5,200 chars)
docs_batch8["learning_development_certifications.md"] = """# NexaTech Solutions - Continuous Learning, Upskilling & Certification Sponsorship Policy
**Document ID:** NT-HR-POL-074  
**Version:** 4.1  
**Effective Date:** January 1, 2026  
**Owner:** NexaAcademy & People Operations  
**Classification:** Internal - All Employees  

---

## 1. Philosophy: Relentless Technical Evolution
Technology evolves at exponential velocity. At NexaTech, we invest in our people by actively subsidizing technical certifications, premium learning platforms, and industry credentials across cloud, AI, distributed systems, and cybersecurity domains.

---

## 2. Annual Certification Reimbursement Allowance
- **Annual Budget:** Up to **₹25,000 INR** per employee per financial year (April 1 – March 31).
- **Eligibility:** All confirmed full-time regular employees with at least 3 months post-confirmation tenure.
- **Pre-Approved Technical Certifications:**
  - *Cloud Computing:* AWS Solutions Architect (Associate/Professional), AWS Certified DevOps Engineer, Azure Solutions Architect Expert, Google Cloud Professional Cloud Architect.
  - *Kubernetes & DevOps:* CKA (Certified Kubernetes Administrator), CKAD, HashiCorp Terraform Associate.
  - *Data & AI:* Databricks Certified Data Engineer, Snowflake SnowPro Core, TensorFlow Developer Certificate.
  - *Security & Governance:* CISSP, CISA, CEH, CompTIA Security+.
  - *Agile & Product:* PSM I/II (Professional Scrum Master), PMP.

---

## 3. Reimbursement Workflow
1. Submit Certification Pre-Approval Request via NexaPortal under *NexaAcademy -> Certification Approval*.
2. The Practice Lead confirms alignment with current practice roadmap within 3 business days.
3. Appear for and successfully pass the examination.
4. Upload official exam score sheet, verified credential URL, and payment tax invoice within **30 calendar days** of passing.
5. Reimbursed funds are credited in the following payroll cycle.
*(Note: Exam retake fees for failed attempts are not reimbursable.)*

---

## 4. Premium Learning Subscriptions
All technical staff are provisioned free enterprise access to:
- **O'Reilly Learning Platform:** Complete library of technical textbooks, video courses, and architectural sandboxes.
- **Coursera for Business & Udemy Business:** Unlimited access to curated software engineering curriculums.
"""

# 75. higher_education_sponsorship.md (MEDIUM ~5,000 chars)
docs_batch8["higher_education_sponsorship.md"] = """# NexaTech Solutions - Higher Education Sponsorship & Academic Tuition Assistance Policy
**Document ID:** NT-HR-POL-075  
**Version:** 3.1  
**Effective Date:** February 1, 2026  
**Owner:** People Operations & Executive Leadership Council  
**Classification:** Internal - All Confirmed Staff  

---

## 1. Vision and Academic Partnership
To develop future technical architects and executive delivery leaders, NexaTech sponsors advanced higher education programs—including Executive M.Tech, Master of Science (MS) in Data Science/AI, and Executive MBA degrees—in partnership with premier institutions (e.g., BITS Pilani, IIIT Bangalore, IIM Kozhikode, Great Lakes).

---

## 2. Sponsorship Value and Eligibility Criteria
- **Financial Sponsorship:** Up to **70% of total academic tuition fees**, capped at a maximum of **₹2,50,000 INR** per candidate over the course of the degree program.
- **Eligibility Prerequisites:**
  - Minimum continuous service of **2 continuous years** at NexaTech.
  - Consistent performance appraisal ratings of **4.0 or 5.0** across the previous two cycles.
  - Endorsement from Practice Head and Chief Technology Officer (CTO).

---

## 3. Service Retention Agreement (Bond Covenants)
Academic sponsorship represents a substantial corporate investment. Sponsored employees must execute a formal **Service Retention Agreement**:
- **Commitment Tenure:** The employee commits to serving NexaTech for a minimum of **24 continuous months** following the formal completion/graduation date of the sponsored degree.
- **Pro-Rata Clawback:** If the employee voluntarily resigns or is terminated for cause prior to completing the 24-month retention window, the employee must refund 100% of sponsored tuition fees to NexaTech prior to receiving exit clearance.

---

## 4. Academic Leave Allowance
Sponsored employees are granted up to **10 days of paid Academic Examination Leave** per academic year to attend mandatory on-campus immersions or semester examinations, upon presentation of the university exam hall ticket.
"""

# 76. internal_job_posting_transfer.md (MEDIUM ~4,900 chars)
docs_batch8["internal_job_posting_transfer.md"] = """# NexaTech Solutions - Internal Job Posting (IJP) & Lateral Mobility Policy
**Document ID:** NT-TA-POL-076  
**Version:** 3.3  
**Effective Date:** January 1, 2026  
**Owner:** Talent Acquisition & Career Pathing Guild  
**Classification:** Internal - All Personnel  

---

## 1. Principles of Internal Career Progression
NexaTech prioritizes internal talent discovery before seeking external recruitment. Our Internal Job Posting (IJP) framework empowers employees to explore new technology practices, transition across business units, or relocate across delivery centers to fulfill their long-term career aspirations.

---

## 2. Eligibility Criteria for IJP Applications
To apply for an advertised IJP position on Darwinbox:
- **Tenure in Current Role:** Must have completed at least **12 continuous months** in their current role/project assignment.
- **Performance Threshold:** Performance rating of **3.0 or higher** in the latest appraisal cycle; employee must not be under an active Performance Improvement Plan (PIP).
- **Disciplinary Standing:** Clear compliance record with zero open disciplinary inquiries.

---

## 3. Managerial Intimation & Application Workflow
- **Application Transparency:** Employees may apply directly to IJP listings on Darwinbox. The employee's current Reporting Manager receives an automated notification upon application submission.
- **Manager Endorsement SLA:** The current manager must provide constructive feedback within **5 business days**. Managers may not unreasonably withhold endorsement.
- **Assessment Process:** The receiving hiring manager conducts technical evaluations and scorecards identical to standard interview rubrics.

---

## 4. Release and Transition Timelines
Upon selection for an internal transfer:
- **Standard Transition Window:** The releasing project squad must release the employee within **30 calendar days** of official selection notification.
- **Knowledge Transfer (KT):** The employee must author a comprehensive KT document and train their successor before transitioning to the new practice.
"""

# 77. resignation_and_notice_period.md (MEDIUM ~5,200 chars)
docs_batch8["resignation_and_notice_period.md"] = """# NexaTech Solutions - Employee Resignation, Notice Period & Voluntary Separation Policy
**Document ID:** NT-HR-POL-077  
**Version:** 4.2  
**Effective Date:** January 1, 2026  
**Owner:** People Operations & Employee Relations  
**Classification:** Internal - All Employees  

---

## 1. Scope and Separation Governance
This policy governs voluntary resignations, contractual notice periods, notice buyout calculations, and knowledge transfer obligations for employees departing NexaTech Solutions.

---

## 2. Contractual Notice Period Durations

| Employment Status / Band | Mandatory Notice Period |
|---|---|
| **Probationary Staff (All Bands)** | **30 Calendar Days** |
| **Confirmed Employees (Bands 1 to 3 - Engineers, Leads)** | **90 Calendar Days** |
| **Confirmed Management (Bands 4+ - Managers, Directors, VPs)** | **90 Calendar Days** |

### 2.1 The 90-Day Rationale
NexaTech contracts high-complexity enterprise digital transformations with strict client SLAs. A 90-day notice period ensures adequate time to identify, onboard, and conduct comprehensive knowledge transfer to incoming replacement engineers without risking client software delivery milestones.

---

## 3. Resignation Submission Protocol
- Resignations must be submitted formally via Darwinbox HRMS under *Employee Services -> Resignation*.
- Verbal resignations, text messages, or informal emails do not constitute legal resignation notice.
- The contractual notice period begins on the date of formal Darwinbox submission.

---

## 4. Notice Period Buyout & Early Release
- **Discretionary Approval:** Notice period waivers or early release requests are subject to mutual written agreement between the Practice Head, Delivery Director, and HRBP. Early release is not a unilateral employee right.
- **Buyout Computation:** If early release is approved at the employee's request, the employee must pay a notice buyout calculated on **Basic Salary** for the unserved working days:
  $$\\text{Buyout Amount} = \\left( \\frac{\\text{Monthly Basic Salary}}{30} \\right) \\times \\text{Unserved Notice Days}$$
- **Leave Adjustment During Notice:** Earned Leave (EL) or Casual Leave cannot be used to shorten the contractual notice period unless approved by the Practice Head.

---

## 5. Garden Leave Provisions
For senior leaders (Band 5+) or engineers possessing sensitive competitive architectural knowledge departing to direct competitors, NexaTech reserves the right to place the individual on **Garden Leave** for all or part of their notice period, providing full salary while revoking all system access.
"""

# 78. exit_interview_and_offboarding.md (MEDIUM ~4,900 chars)
docs_batch8["exit_interview_and_offboarding.md"] = """# NexaTech Solutions - Exit Clearance, Knowledge Transfer & Offboarding SOP
**Document ID:** NT-HR-SOP-078  
**Version:** 3.4  
**Effective Date:** January 1, 2026  
**Owner:** People Operations & IT Asset Governance  
**Classification:** Internal - All Personnel  

---

## 1. Purpose of Structured Offboarding
A smooth separation experience honors departing colleagues, protects enterprise intellectual property, and ensures seamless transition of project responsibilities.

---

## 2. Structured Knowledge Transfer (KT) Milestones
During the notice period, the departing employee must complete the following KT deliverables:
1. **KT Plan Formulation (Week 1):** Detail all active Jira tickets, code repositories, scheduled cron jobs, and architectural components under the employee's ownership.
2. **Reverse Shadowing (Weeks 2-6):** The identified successor shadows the departing employee during sprint tasks and code reviews.
3. **Formal KT Sign-Off (Week 7-8):** The Project Delivery Manager must sign the digital *KT Clearance Certificate* on Darwinbox, certifying zero open delivery risks.

---

## 3. Exit Interview Process
- Every resigning employee participates in a confidential **Exit Interview** with an independent People Operations Partner during their final 10 days of service.
- Feedback regarding culture, management quality, tooling, compensation, and reasons for leaving is aggregated anonymously and analyzed quarterly by the Executive Leadership Council.

---

## 4. Final Day Departmental Clearances
On the Last Working Day (LWD), the employee must complete clear-outs across all departments:
- **IT Infrastructure:** Return laptop, charger, YubiKey, and access badges at the Level 1 IT Desk. IT issues a digital *Asset Return Receipt*.
- **Finance & Accounts:** Settle all open travel advances, corporate credit card balances, and petty cash ledgers.
- **Facilities:** Surrender desk locker keys and parking transponders.
- **Account Deactivation:** All Okta SSO, email, Slack, and cloud credentials deactivate automatically at 6:00 PM IST on the LWD.
"""

# 79. full_and_final_settlement_timeline.md (MEDIUM ~4,800 chars)
docs_batch8["full_and_final_settlement_timeline.md"] = """# NexaTech Solutions - Full & Final (F&F) Settlement Timelines & Exit Payroll Policy
**Document ID:** NT-FIN-POL-079  
**Version:** 4.1  
**Effective Date:** January 1, 2026  
**Owner:** Payroll Operations, Finance & Legal Compliance  
**Classification:** Confidential - Internal  

---

## 1. Statutory Settlement Commitments
In compliance with the Code on Wages and state labor enactments, NexaTech Solutions ("NexaTech") ensures that final compensation settlements, leave encashments, and statutory certificates are delivered to separating personnel transparently and within strictly audited statutory timeframes.

---

## 2. Settlement Timeline & Payment SLA
- **Processing Window:** The Full and Final (F&F) settlement is calculated, audited, and disbursed within **30 to 45 calendar days** following the employee's verified Last Working Day (LWD), provided all departmental clearances (IT, Facilities, Finance) are completed.
- **Mode of Payment:** Funds are disbursed via direct NEFT/RTGS bank transfer to the employee's registered corporate salary bank account.

---

## 3. Components of Full and Final Settlement

### 3.1 Credit Items (Earnings)
- Pro-rated monthly salary for active working days in the final month up to LWD.
- Encashment of accumulated, unavailed Earned Leave (EL) balances (up to maximum statutory cap of 45 days) calculated at `Basic Salary / 30 * Days`.
- Statutory Gratuity payout (if eligible with >= 5 continuous years of service).
- Approved pending travel or medical expense reimbursements.

### 3.2 Debit Items (Deductions)
- Statutory Tax Deductions at Source (TDS) calculated on final settlement earnings.
- Unserved notice period buyout deductions (if early release was granted).
- Outstanding corporate travel advances or unsettled corporate credit card charges.
- Penalties for unreturned or damaged corporate hardware assets.

---

## 4. Post-Separation Documentation Release
Within **5 business days** of F&F monetary disbursement, the People Operations Desk generates and delivers via registered personal email:
1. Detailed F&F Settlement Paysheet.
2. Official **Service and Experience Certificate**.
3. Formal **Relieving Letter**.
4. Income Tax Form 16 (Part A & B) released during the statutory quarterly tax cycle.
"""

# 80. alumni_network_policy.md (MEDIUM ~4,600 chars)
docs_batch8["alumni_network_policy.md"] = """# NexaTech Solutions - NexaAlumni Network & Boomerang Talent Rehire Policy
**Document ID:** NT-HR-POL-080  
**Version:** 2.2  
**Effective Date:** January 1, 2026  
**Owner:** People Operations & Talent Brand Guild  
**Classification:** Internal - All Employees  

---

## 1. Philosophy: Lifelong NexaTech Relationships
Separation from NexaTech is not the end of a professional relationship. Our former employees—the **NexaAlumni**—are our greatest brand ambassadors, prospective clients, joint venture partners, and future returning colleagues ("Boomerangs").

---

## 2. NexaAlumni Community Privileges
Former employees separating in good standing automatically receive invitations to join the *NexaAlumni Global Portal*:
- **Alumni Mentorship:** Opportunities to mentor early-career NexaTech apprentices.
- **Tech Talks & Summits:** Complimentary guest invitations to annual NexaTech Tech Summits and hackathons.
- **Alumni Referral Bounties:** Alumni referring talent for open NexaTech engineering roles receive **75% of the standard employee referral bounty** upon candidate confirmation.

---

## 3. "Boomerang" Rehire Guidelines & Perks
NexaTech enthusiastically welcomes high-performing former employees who wish to return:
- **Probation Waiver:** Returning alumni with previously verified 3.0+ performance ratings who return within **24 months** of departure have their standard 90-day probationary period **fully waived**.
- **Tenure Bridging for Gratuity:** If an employee returns within **12 months**, prior continuous service tenure is bridged for statutory gratuity and long-service recognition milestones (subject to prevailing statutory regulations).
- **Fast-Track Selection:** Boomerang candidates bypass initial screening rounds and move directly to final technical architecture discussions.
"""

for filename, content in docs_batch8.items():
    file_path = DOCS_DIR / filename
    file_path.write_text(content.strip(), encoding="utf-8")
    print(f"Written: {filename} ({len(content)} chars)")

print("Batch 8 Complete: 10 files written.")
