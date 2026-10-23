# NexaTech Solutions - Hardware Procurement, Asset Allocation & IT Lifecycle Policy
**Document ID:** NT-IT-POL-013  
**Version:** 4.0  
**Effective Date:** January 15, 2026  
**Owner:** IT Infrastructure, Enterprise Asset Management & Procurement  
**Classification:** Internal - All Employees  

---

## 1. Purpose and Scope
NexaTech Solutions ("NexaTech") equips employees with modern, high-grade computing workstations, peripheral displays, and mobile testing devices to ensure optimal developer productivity, client delivery, and data security.

This policy governs the procurement, allocation, acceptable maintenance, peripheral allowances, refresh cycles, and return procedures for all IT hardware assets owned or leased by NexaTech.

---

## 2. Hardware Allocation Matrix by Role

Hardware configurations are strictly aligned with job profiles, computational requirements, and client security standards:

| Role / Job Family | Hardware Specification Tier | Standard Device Models | Budget Ceiling (INR) |
|---|---|---|---|
| **Software Engineers, Data Engineers, DevOps, CloudOps (Band 1 - Band 3)** | High-Performance Engineering Workstation | Apple MacBook Pro 16" (M3 Pro, 36GB RAM, 1TB SSD) OR Dell XPS 15 (i7 14th Gen, 32GB RAM, 1TB SSD, Ubuntu/Win11) | Up to ₹2,20,000 |
| **Principal Architects, Technical Directors, AI/ML Specialists (Band 4+)** | Advanced Compute / AI Workstation | Apple MacBook Pro 16" (M3 Max, 64GB RAM, 2TB SSD) OR ThinkPad P1 Gen 7 (i9, 64GB RAM, RTX 4070 8GB) | Up to ₹3,20,000 |
| **UI/UX Designers, Creative Leads** | Creative Design Workstation | Apple MacBook Pro 16" (M3 Pro, 36GB RAM, 1TB SSD) + Apple Magic Trackpad | Up to ₹2,30,000 |
| **Sales, People Ops, Finance, Legal, Project Coordinators** | Standard Business Ultrabook | Lenovo ThinkPad T14s (i5 14th Gen, 16GB RAM, 512GB SSD) OR Dell Latitude 7450 (i5, 16GB RAM) | Up to ₹1,10,000 |

*Note:* Deviation from standard specifications requires written justification from the Practice Head and approval from the Chief Information Officer (CIO) via Jira queue `IT-CAPEX`.

---

## 3. Peripheral Allowance and Home Office Equipment

### 3.1 Office-Based Peripherals
At all physical NexaTech delivery centers (Bengaluru, Hyderabad, Pune, Gurugram), hot-desks and dedicated bays are equipped with:
- Dual 27-inch 4K USB-C Dell UltraSharp hub monitors (delivering 90W power passthrough).
- Ergonomic wireless keyboard and optical mouse.
- Cat6 Gigabit Ethernet patch cables and universal power strips.

### 3.2 Remote Ergonomic Setup Allowance
Confirmed full-time employees are entitled to a one-time reimbursement of up to **₹15,000 INR** to equip their home workspace:
- **Eligible Items:** Ergonomic task chair, height-adjustable desk or desk riser, external monitor stand, wrist rests, and uninterruptible power supply (UPS) for home Wi-Fi routers.
- **Submission:** Submit tax invoices via NexaPortal Expense Module under *Remote Ergonomic Allowance* within 90 days of confirmation.
- **Ownership:** Equipment purchased under this allowance remains the personal property of the employee; receipts must show the employee's personal name.

---

## 4. Asset Care, Maintenance, and Refresh Lifecycle

### 4.1 Asset Lifecycle and Refresh Policy
- **Standard Refresh Cycle:** Laptops are refreshed every **36 months** (3 years) from original deployment date.
- **Buy-Back Option:** Upon completing 36 months, employees may purchase their decommissioned laptop at fair depreciated market salvage value (typically 10% to 15% of original invoice value). The laptop is sanitized of all corporate data, BitLocker/FileVault keys, and MDM profiles before transfer of ownership.

### 4.2 Maintenance and Repairs
- All corporate laptops carry manufacturer premier on-site warranties (AppleCare+ Enterprise or Dell ProSupport Plus with Next Business Day On-Site Service).
- For hardware faults (faulty battery, keyboard failure, display anomalies), raise a ticket on NexaDesk under queue `IT-SERV`.
- Loaner laptops of equivalent specifications are issued by the IT Helpdesk within **2 hours** at physical delivery centers while repairs are underway.

---

## 5. Loss, Theft, and Accidental Damage Protocols

### 5.1 Immediate Reporting Obligation
In the event an asset is lost, stolen, or damaged:
1. **Immediate SLA (Within 2 Hours):** Contact the Cyber Defense Center (`infosec@nexatech.com` or +91-80-6922-0911) so the device can be remotely locked and wiped via Microsoft Intune or Jamf Pro.
2. **Police Complaint:** For stolen or lost devices, file a police complaint (e-FIR) with local municipal police within 24 hours and forward the FIR copy to `ithelpdesk@nexatech.com`.

### 5.2 Financial Liability Matrix
- **Manufacturer Defect or Normal Wear:** 100% covered by corporate maintenance contracts.
- **First Accidental Damage Event (e.g., liquid spill, accidental screen crack):** Covered under corporate damage insurance; zero employee liability.
- **Subsequent Negligent Damage (within 12 months of first incident):** Employee pays 25% of certified repair cost, capped at ₹15,000 INR, deducted via payroll.
- **Gross Negligence / Unreported Loss / Non-Filing of FIR:** If an employee fails to report a lost laptop within 24 hours or demonstrates gross negligence (e.g., leaving a laptop in an unlocked vehicle overnight), the employee is liable for 50% of the depreciated asset book value, deducted across 3 subsequent payroll cycles.

---

## 6. Asset Return and Offboarding Clearance

Upon separation or resignation from NexaTech:
- All assigned IT assets—including laptop, charging brick, power cables, hardware YubiKeys, and any mobile test devices—must be returned to the IT Helpdesk on or before the Last Working Day (LWD).
- Remote employees are shipped a prepaid, insured courier shipping crate by the Logistics Desk.
- Failure to return corporate hardware assets within 7 business days of LWD will delay the issuance of the Full and Final settlement and Relieving Certificate, and may trigger civil recovery proceedings under Indian Penal Code provisions governing criminal breach of trust.