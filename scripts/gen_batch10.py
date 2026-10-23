import os
from pathlib import Path

DOCS_DIR = Path("docs")
DOCS_DIR.mkdir(parents=True, exist_ok=True)

docs_batch10 = {}

# 91. esop_equity_incentive_plan.md (MEDIUM ~5,200 chars)
docs_batch10["esop_equity_incentive_plan.md"] = """# NexaTech Solutions - Employee Stock Option Plan (ESOP) & Equity Incentive Policy
**Document ID:** NT-FIN-POL-091  
**Version:** 3.4  
**Effective Date:** January 1, 2026  
**Owner:** Board Compensation Committee & Total Rewards  
**Classification:** Confidential - Internal  

---

## 1. Vision and Shared Wealth Creation
NexaTech Solutions ("NexaTech") believes that sustainable enterprise value is created when engineers, technical architects, and business leaders share meaningful equity ownership in the firm. The NexaTech Employee Stock Option Plan (ESOP 2026 Scheme) aligns long-term executive and engineering incentives with shareholder value.

---

## 2. Grant Mechanics and Vesting Schedule
- **Grant Letter:** Issued via the Carta equity management portal upon approval by the Board Nomination and Remuneration Committee (NRC).
- **Vesting Schedule:** Standard **4-year graded vesting with a 1-year cliff**:
  - *Month 12 (1-Year Cliff):* **25%** of granted options vest on the first anniversary of the Grant Date.
  - *Months 13 to 48:* The remaining **75%** vests in equal monthly increments of 2.083% at the end of each completed calendar month.
- **Acceleration Triggers:** Full single-trigger or double-trigger vesting acceleration applies in the event of a change-of-control acquisition or Initial Public Offering (IPO).

---

## 3. Exercise Window and Liquidity Events
- **Exercise Price (Strike Price):** Determined by an independent SEBI/RBI registered merchant banker fair market valuation (FMV) at the time of grant.
- **Liquidity Buyback Windows:** NexaTech organizes bi-annual corporate ESOP liquidity buyback programs, allocating 5% of annual net profit to repurchase vested options from confirmed staff at current FMV.
- **Post-Separation Exercise Window:** Departing employees have **90 calendar days** following their Last Working Day to exercise vested options. Unexercised options return to the corporate ESOP pool.
"""

# 92. vendor_invoice_payment_terms.md (MEDIUM ~4,900 chars)
docs_batch9_or_10 = docs_batch10
docs_batch10["vendor_invoice_payment_terms.md"] = """# NexaTech Solutions - Accounts Payable & Vendor Invoice Processing Policy
**Document ID:** NT-FIN-POL-092  
**Version:** 3.2  
**Effective Date:** February 1, 2026  
**Owner:** Accounts Payable, Treasury & Statutory Tax Desk  
**Classification:** Internal - Finance & Procurement  

---

## 1. Principles of Accounts Payable Governance
NexaTech ensures timely, accurate, and statutory-compliant disbursement of vendor liabilities. This policy defines mandatory invoice verification standards, 3-way matching rules, and payment credit cycles.

---

## 2. Statutory MSME 45-Day Payment Mandate
In strict compliance with the Micro, Small and Medium Enterprises Development (MSMED) Act, 2006 and Section 43B(h) of the Income Tax Act:
- Invoices from verified MSME-registered suppliers must be settled within **45 calendar days** from the date of service acceptance or goods receipt.
- Any delayed MSME payment incurs statutory compound interest at three times the RBI bank rate, payable by NexaTech and non-deductible for corporate income tax.

---

## 3. Three-Way Matching Protocol
Before any commercial invoice is queued for payment in SAP / NetSuite, Accounts Payable verifies:
1. **Purchase Order (PO):** Approved PO issued prior to service delivery with matching unit rates.
2. **Goods Receipt Note (GRN) / Service Entry Sheet (SES):** Written receipt signed by the receiving department lead certifying satisfactory delivery.
3. **Vendor Tax Invoice:** Compliant GST invoice showing NexaTech's correct GSTIN, SAC/HSN codes, and vendor digital signature.

---

## 4. Payment Schedules and Inquiries
- **Standard Credit Period:** Net 30 days for general suppliers; Net 45 days for MSME vendors.
- **Disbursement Batches:** Payments are processed twice weekly (Tuesdays and Thursdays) via NEFT/RTGS banking rails.
- **Vendor Payment Desk:** Inquiries must be directed to `accountspayable@nexatech.com` citing the PO and invoice number.
"""

# 93. software_asset_licensing_audit.md (MEDIUM ~4,800 chars)
docs_batch10["software_asset_licensing_audit.md"] = """# NexaTech Solutions - Software Asset Management & License Compliance Policy
**Document ID:** NT-IT-POL-093  
**Version:** 3.1  
**Effective Date:** January 1, 2026  
**Owner:** IT Asset Management & Software Licensing CoE  
**Classification:** Internal - All Employees  

---

## 1. Purpose and Legal Compliance
NexaTech Solutions relies on hundreds of enterprise software platforms, cloud SDKs, IDEs, and developer utilities. Using unlicensed, cracked, or misconfigured commercial software exposes the enterprise to severe copyright infringement lawsuits, substantial vendor audit fines, and malware infections.

This policy mandates strict compliance with commercial software licensing covenants.

---

## 2. Software Acquisition & Whitelist Mandate
- **Centralized Procurement:** All commercial software licenses must be procured through the IT Asset Management Desk (`itlicensing@nexatech.com`). Employees must not purchase software on personal credit cards without prior written CIO sign-off.
- **Whitelisted Tooling:** Workstations run automated Lansweeper inventory agents. Installing software not on the *NexaTech Approved Software Catalog* is blocked by Intune / Jamf application whitelisting.
- **Prohibition on Piracy:** The possession or installation of cracked software, keygens, torrent clients, or unvetted freeware is gross misconduct resulting in immediate disciplinary review.

---

## 3. Annual Vendor True-Up Audits
- IT Asset Management conducts bi-annual internal reconciliation across JetBrains, Microsoft 365, GitHub Enterprise, and AWS licenses to match deployed seats against active licenses.
- Inactive user accounts (idle > 45 days) have their premium software licenses harvested and returned to the shared corporate pool automatically.
"""

# 94. clean_desk_and_clear_screen_policy.md (MEDIUM ~4,700 chars)
docs_batch10["clean_desk_and_clear_screen_policy.md"] = """# NexaTech Solutions - Clean Desk, Clear Screen & Workspace Hygiene Policy
**Document ID:** NT-SEC-POL-094  
**Version:** 4.0  
**Effective Date:** January 1, 2026  
**Owner:** Physical Security & Cyber Defense Center (CDC)  
**Classification:** Internal - All Personnel  

---

## 1. Purpose and ISO 27001 Alignment
In accordance with ISO/IEC 27001:2022 Control 7.7, NexaTech enforces a strict Clean Desk and Clear Screen policy to protect physical documents, sensitive client data, and workstation access from unauthorized visual snooping, shoulder surfing, or theft.

---

## 2. Clear Screen Mandates
- **Workstation Locking:** Whenever leaving a workstation unattended—even for 1 minute—the employee must lock the screen (`Win + L` on Windows; `Cmd + Ctrl + Q` on macOS).
- **Automated Timeout:** Central MDM enforces an automated screensaver lock after **3 minutes** of inactivity, requiring full password/biometric re-authentication.
- **External Monitor Privacy:** Workstations situated near high-traffic hallways, visitor pathways, or glass perimeter windows must have 3M polarized privacy filters installed.

---

## 3. Clean Desk Mandates
- **Physical Documents:** Paper notes containing passwords, system IP addresses, customer PII, or project architectures must be shredded immediately after use in cross-cut shredders.
- **End-of-Day Clear-Out:** At the end of each workday, all desks must be completely clear of laptops, notebooks, USB peripherals, and access badges. All hardware must be locked inside personal pedestals or lockers.
- **Unannounced Physical Audits:** The Physical Security team conducts nightly sweeps at 10:00 PM IST. Any unattended laptops or confidential papers found unlocked are impounded, and a formal security non-conformance notice is issued to the employee and manager.
"""

# 95. business_email_etiquette_standards.md (MEDIUM ~4,900 chars)
docs_batch9_or_10 = docs_batch10
docs_batch10["business_email_etiquette_standards.md"] = """# NexaTech Solutions - Corporate Communication, Email & Slack Etiquette Standards
**Document ID:** NT-COM-STD-095  
**Version:** 3.2  
**Effective Date:** January 1, 2026  
**Owner:** People Operations & Corporate Communications  
**Classification:** Internal - All Personnel  

---

## 1. Principles of Enterprise Communication
Clear, concise, and courteous communication builds trust with global clients, streamlines sprint execution, and respects colleagues' time across time zones.

---

## 2. Email Formatting and Standardization

### 2.1 Standardized Subject Line Prefixes
To help recipients prioritize high-volume inboxes, subject lines should use standardized action tags:
- `[ACTION REQUIRED] - SOW Review for Cloud Migration by Friday 5 PM`
- `[DECISION] - Database Engine Selection for Payment Microservice`
- `[URGENT] - SEV-1 Outage Notification: Auth Gateway Degraded`
- `[INFO] - Sprint 44 Release Notes Published`

### 2.2 Corporate Signature Block
All outbound business emails must utilize the standardized corporate signature generated via *NexaSignature Tool*:
```text
Firstname Lastname | Senior Software Engineer
NexaTech Solutions Pvt. Ltd. | Bengaluru HQ
Mobile: +91-98XXX-XXXXX | Slack: @firstname.lastname
www.nexatech.com | Digital Transformation & Engineering Excellence
```

---

## 3. Slack Communication Etiquette
- **Public Over Private:** Discuss technical problems in public channel rooms (`#dev-backend`, `#cloud-ops`) rather than 1-on-1 direct messages so the broader team can learn and assist.
- **Threaded Discussions:** Always respond to discussions in Slack threads to keep main channel feeds clean and scannable.
- **Working Hours Respect:** Avoid tagging colleagues outside their registered working hours unless triaging an active SEV-1 incident. Use Slack's *Schedule Send* feature for non-urgent messages.
"""

# 96. offshore_development_center_odc_rules.md (MEDIUM ~5,100 chars)
docs_batch10["offshore_development_center_odc_rules.md"] = """# NexaTech Solutions - Dedicated Offshore Development Center (ODC) Security Regulations
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
"""

# 97. disability_inclusion_accessibility.md (MEDIUM ~4,800 chars)
docs_batch10["disability_inclusion_accessibility.md"] = """# NexaTech Solutions - Workplace Accessibility, Disability Inclusion & Accommodation Policy
**Document ID:** NT-HR-POL-097  
**Version:** 3.1  
**Effective Date:** January 1, 2026  
**Owner:** People Operations & Diversity, Equity & Inclusion (DEI) Guild  
**Classification:** Internal - All Employees  

---

## 1. Commitment to Universal Inclusion
In compliance with the *Rights of Persons with Disabilities (RPwD) Act, 2016*, NexaTech Solutions is dedicated to providing barrier-free, accessible, and empowering workplaces for persons with visible and non-visible disabilities.

---

## 2. Physical Campus Accessibility
All NexaTech delivery centers feature:
- Wheelchair-accessible ramps, motorized entry doors, and wide-aisle turnstiles.
- Tactile paving and Braille signage in all elevator banks and common restrooms.
- Reserved accessible parking bays located immediately adjacent to main reception lobbies.
- Accessible height-adjustable cafeteria dining counters and dedicated emergency evacuation stair-chairs.

---

## 3. Digital Workplace Reasonable Accommodations
Employees requiring specialized technological accommodations may submit a confidential request on NexaPortal under *DEI Support*:
- **Screen Readers & Magnifiers:** Fully sponsored licenses for JAWS, NVDA, and ZoomText.
- **Ergonomic & Assistive Hardware:** Trackball mice, one-handed keyboards, motorized sit-stand desks, and dual-arm monitor mounts.
- **Live Captioning:** Automated CART captioning and sign-language interpretation sponsored for all company-wide town halls and executive keynotes.
- **Support Contact:** Reach out directly to the Accessibility Lead at `accessibility@nexatech.com`.
"""

# 98. corporate_security_surveillance.md (MEDIUM ~4,700 chars)
docs_batch10["corporate_security_surveillance.md"] = """# NexaTech Solutions - Campus Physical Security, CCTV & Electronic Surveillance Policy
**Document ID:** NT-SEC-POL-098  
**Version:** 3.2  
**Effective Date:** January 1, 2026  
**Owner:** Physical Security, Facilities & Legal Compliance  
**Classification:** Internal - All Personnel  

---

## 1. Purpose and Surveillance Scope
NexaTech operates electronic video surveillance systems across all corporate facilities to safeguard personnel physical safety, deter unlawful conduct, prevent theft, and protect enterprise intellectual property.

---

## 2. Camera Placement and Privacy Protections
- **Authorized Surveillance Areas:** Closed-Circuit Television (CCTV) cameras are installed exclusively in communal and high-security zones: main entrances, reception lobbies, cafeteria commons, parking structures, server rooms, emergency exit stairs, and ODC access vestibules.
- **Strict Privacy Zones:** Cameras are strictly prohibited in restrooms, wellness rooms, lactation rooms, changing quarters, and quiet meditation pods.
- **Audio Recording Ban:** Cameras in general office bays operate video capture only; continuous audio eavesdropping of employee conversations is strictly prohibited.

---

## 3. Footage Retention, Access & Chain of Custody
- **Retention Period:** Standard CCTV footage is retained on encrypted Network Video Recorders (NVR) for **60 calendar days**, after which it is automatically overwritten unless preserved under a formal legal hold notice.
- **Access Authorization:** Reviewing recorded CCTV footage requires dual-authorization from the Head of Physical Security and the Legal Counsel. Routine managerial browsing of camera feeds is forbidden.
"""

# 99. intellectual_property_open_innovation.md (MEDIUM ~5,000 chars)
docs_batch10["intellectual_property_open_innovation.md"] = """# NexaTech Solutions - Academic Research Partnerships & Open Innovation Policy
**Document ID:** NT-OCTO-POL-099  
**Version:** 2.4  
**Effective Date:** February 1, 2026  
**Owner:** Office of the CTO & Academic Collaboration Guild  
**Classification:** Internal - Research & Engineering  

---

## 1. Vision: Advancing the Technological Frontier
To remain at the vanguard of distributed systems, quantum computing algorithms, and foundational artificial intelligence, NexaTech collaborates with leading global academic institutions and research consortia.

This policy governs intellectual property allocation, research grants, and joint publication rights for collaborative research.

---

## 2. Research Partnerships & Sponsored Grants
- **Academic Grant Sponsorship:** NexaTech sponsors targeted academic research fellowships and doctoral research grants up to **₹15,00,000 INR** annually per university lab.
- **Sponsored Capstone Projects:** Senior architects co-guide university student capstone projects, providing compute infrastructure on AWS and anonymized benchmark datasets.

---

## 3. Intellectual Property Allocation in Academic Collaborations
- **Joint IP Framework:** Inventions co-developed under formal Joint Research Agreements (JRAs) are co-owned, granting NexaTech an exclusive, perpetual, worldwide commercial license to deploy the resulting technology in enterprise software.
- **Academic Publication Freedom:** Academic partners retain the right to publish scientific findings in peer-reviewed journals (IEEE, ACM), subject to a 30-day review period by NexaTech Legal to file defensive patents or redact proprietary trade secrets.
"""

# 100. enterprise_ai_ethics_governance.md (MEDIUM ~5,300 chars)
docs_batch10["enterprise_ai_ethics_governance.md"] = """# NexaTech Solutions - Responsible Artificial Intelligence (AI) & Algorithmic Ethics Policy
**Document ID:** NT-AI-POL-100  
**Version:** 3.0  
**Effective Date:** February 1, 2026  
**Owner:** AI Ethics Board & Office of the CTO  
**Classification:** Internal - All Technical Staff  

---

## 1. Executive Mandate for Ethical AI
As NexaTech builds enterprise autonomous agents, retrieval-augmented generation (RAG) systems, and machine learning models for mission-critical client operations, we must ensure our AI solutions are fair, explainable, transparent, resilient, and human-centric.

---

## 2. The Five Pillars of NexaTech Responsible AI

1. **Fairness & Bias Mitigation:**
   - Training datasets must be rigorously evaluated for representation bias, historical inequities, and demographic skews.
   - Algorithmic scoring models affecting human credit, employment, or medical diagnosis must achieve parity across demographic cohorts.
2. **Explainability & Transparency:**
   - Black-box AI models cannot be deployed in high-stakes environments without explainability layers (e.g., SHAP, LIME, or chain-of-thought retrieval citation).
   - Users must be explicitly informed whenever they are interacting with an autonomous AI agent or receiving AI-generated recommendations.
3. **Robustness & Hallucination Guardrails:**
   - Generative systems must enforce strict retrieval guardrails (confidence thresholds, source citation constraints). When confidence is below threshold, models must acknowledge uncertainty rather than hallucinating facts.
4. **Data Privacy & IP Protection:**
   - AI models must never be trained on customer proprietary data or confidential code without express contractual authorization.
5. **Human-in-the-Loop Oversight:**
   - Mission-critical actions—such as processing multi-million dollar wire transfers, terminating services, or altering production network rules—must require affirmative human approval before execution.

---

## 3. AI Ethics Review Board (AERB)
All high-risk enterprise AI projects must be approved by the **AI Ethics Review Board** prior to production deployment. The board reviews algorithmic impact assessments, threat models, and bias audit metrics within 10 business days of submission.
"""

for filename, content in docs_batch10.items():
    file_path = DOCS_DIR / filename
    file_path.write_text(content.strip(), encoding="utf-8")
    print(f"Written: {filename} ({len(content)} chars)")

print("Batch 10 Complete: 10 files written.")
