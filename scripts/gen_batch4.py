import os
from pathlib import Path

DOCS_DIR = Path("docs")
DOCS_DIR.mkdir(parents=True, exist_ok=True)

docs_batch4 = {}

# 31. onboarding_product_manager.md (MEDIUM ~5,200 chars)
docs_batch4["onboarding_product_manager.md"] = """# NexaTech Solutions - Technical Product Manager (TPM) Onboarding Playbook
**Document ID:** NT-PRD-GDE-031  
**Version:** 3.1  
**Effective Date:** February 1, 2026  
**Owner:** Product Management Guild & Agile Program Office  
**Classification:** Internal - Product Organization  

---

## 1. Role and Strategic Context
Technical Product Managers (TPMs) at NexaTech bridge client business strategy, human-centered UI/UX design, and complex cloud engineering execution. As a TPM, you define the "Why" and "What" of our software deliverables while empowering engineering squads to solve the "How."

This playbook outlines your 90-day ramp journey, product artifact standards, backlog management, and client workshop frameworks.

---

## 2. Product Tooling Stack
Your Okta SSO credentials provide immediate access to our product management suite:
- **Jira Software Enterprise:** Backlog prioritization, epics, sprint planning, and release burndown tracking.
- **Productboard:** Product roadmap visualization, feature prioritization (RICE scoring), and client feedback aggregation.
- **Figma Enterprise:** Reviewing UI/UX wireframes, design systems, and component libraries.
- **Miro Enterprise:** Collaborative whiteboarding, story mapping, and design thinking workshops.
- **Amplitude & Mixpanel:** Product analytics, user funnel drop-offs, and feature adoption telemetry.

---

## 3. Product Requirements Document (PRD) Standard
Every feature epic at NexaTech requires a standardized PRD in Confluence before sprint grooming:
1. **Problem Statement & Executive Context:** What customer pain point or market opportunity is being addressed?
2. **Success Metrics (North Star & Guardrail KPIs):** Quantifiable outcomes (e.g., reduce checkout latency by 35%, increase conversion by 4%).
3. **User Personas & Journey Maps:** Step-by-step user flows across web, mobile, and API interfaces.
4. **Functional Requirements & Out-of-Scope:** Explicit itemization of MVP vs. future-phase capabilities.
5. **Non-Functional Requirements (NFRs):** P99 response latency (<200ms), concurrency (10,000 TPS), data retention, and security compliance (SOC 2, HIPAA).
6. **Release Milestones & Phased Rollout:** Feature flag strategy (LaunchDarkly) and canary rollout stages.

---

## 4. Product 30-60-90 Day Milestones

```
[Day 1-30: Discovery & Domain Immersion]
  ├── Review existing architectural diagrams and product roadmaps
  ├── Shadow client weekly syncs and sprint retrospectives
  ├── Conduct 1-on-1 discovery sessions with Engineering Leads and UX Designers
  └── Author first minor PRD for an upcoming sprint maintenance release

[Day 31-60: Squad Leadership & Sprint Ownership]
  ├── Facilitate backlog grooming and sprint planning for assigned squad
  ├── Lead customer journey mapping workshop with client stakeholders
  ├── Define telemetry tracking events in Amplitude for new feature releases
  └── Manage sprint scope changes and communicate tradeoffs transparently

[Day 61-90: Roadmap Strategy & Value Realization]
  ├── Author quarterly product roadmap (Q+1 / Q+2) with RICE prioritization
  ├── Present product roadmap to Client Executive Steering Committee
  └── Analyze post-launch adoption metrics and present retro findings
```
"""

# 32. onboarding_qa_automation.md (MEDIUM ~5,000 chars)
docs_batch4["onboarding_qa_automation.md"] = """# NexaTech Solutions - Quality Engineering & QA Automation Onboarding Guide
**Document ID:** NT-ENG-GDE-032  
**Version:** 3.4  
**Effective Date:** February 1, 2026  
**Owner:** Quality Engineering Excellence & Automation Guild  
**Classification:** Internal - Technical Staff  

---

## 1. Quality Engineering Philosophy at NexaTech
Quality is not an inspection phase tacked onto the end of a sprint; it is an intrinsic engineering discipline embedded throughout the software development lifecycle (SDLC). At NexaTech, Quality Engineers write scalable automated test suites, build CI/CD test gates, conduct performance load simulations, and ensure zero defect slippage into production.

---

## 2. Standard Quality Engineering Toolchain
- **E2E Automation:** Playwright (TypeScript/Python) and Cypress for modern web applications; Appium for mobile (iOS/Android).
- **API Testing:** RestAssured (Java), Karate Framework, and Postman Newman CLI.
- **Performance & Load Testing:** k6 Cloud, Apache JMeter, and Gatling for distributed high-concurrency simulation.
- **Test Management & CI Integration:** Zephyr Scale for Jira, GitHub Actions, and Allure Reporting.

---

## 3. Test Automation Pyramid and Coverage Gates
NexaTech mandates strict adherence to the test pyramid:
- **Unit Tests (70% of total tests):** Authored primarily by SDEs; minimum 80% line coverage enforced by SonarQube quality gates.
- **API / Integration Tests (20% of total tests):** Co-authored by QA and SDEs; validate contract compliance, database mutations, and external webhooks.
- **End-to-End UI Tests (10% of total tests):** Maintained by Quality Engineers; focused on critical business transaction paths.

---

## 4. Defect Severity Matrix & Resolution SLAs
When logging defects in Jira Software under project issue type `Bug`:

| Severity Level | Definition | Investigation SLA | Resolution Target |
|---|---|---|---|
| **Blocker (P1)** | Complete system crash; data loss; critical security vulnerability; payment flow halted. | **15 Minutes** | **4 Hours** |
| **Critical (P2)** | Core feature broken with no available workaround; significant customer impact. | **1 Hour** | **24 Hours** |
| **Major (P3)** | Secondary feature broken; viable business workaround exists. | **4 Hours** | Current Sprint |
| **Minor (P4)** | Cosmetic UI layout defect; minor typographical error; non-blocking issue. | **24 Hours** | Next Sprint Backlog |

---

## 5. QA 30-60-90 Day Success Milestones
- **Month 1:** Set up local test runner; automate 5 manual regression test cases in Playwright; execute test runs in staging.
- **Month 2:** Integrate automated test suite into GitHub Actions CI pipeline; establish Allure test dashboards; write API performance script in k6.
- **Month 3:** Take full ownership of squad sprint QA sign-off; conduct cross-browser and accessibility (WCAG 2.1 AA) compliance audit.
"""

# 33. onboarding_data_ai_engineer.md (MEDIUM ~5,100 chars)
docs_batch4["onboarding_data_ai_engineer.md"] = """# NexaTech Solutions - Data, Analytics & AI Engineer Onboarding Guide
**Document ID:** NT-ENG-GDE-033  
**Version:** 3.1  
**Effective Date:** February 1, 2026  
**Owner:** Data Engineering & Enterprise AI Practice  
**Classification:** Internal - Technical Staff  

---

## 1. Overview and Practice Vision
The Data & AI Practice at NexaTech designs petabyte-scale data lakehouses, real-time streaming architectures, generative AI agent workflows, and enterprise MLOps pipelines. We transform raw enterprise telemetry into actionable intelligence for global banking, retail, and healthcare clients.

This guide details our reference architectures, security boundaries, compute clusters, and 90-day ramp objectives.

---

## 2. Core Data & AI Technology Stack
- **Lakehouse & Data Warehousing:** Databricks (Delta Lake on AWS/Azure), Snowflake Enterprise, Google BigQuery.
- **Data Transformation & Orchestration:** dbt Core / dbt Cloud, Apache Airflow (Astronomer), Prefect.
- **Streaming & Event Streaming:** Apache Kafka (Confluent Cloud), Apache Flink, AWS Kinesis.
- **Machine Learning & MLOps:** MLflow for model registry and tracking, Kubeflow, Weights & Biases, Ray on Kubernetes.
- **Generative AI & LLM Frameworks:** LangChain, LangGraph, LlamaIndex, vLLM, Hugging Face Enterprise, Qdrant Vector Search.

---

## 3. Data Governance, Synthetic Data & Privacy Rules
- **Prohibition on Production Data:** Under no circumstances may raw production customer data containing PII (names, emails, phone numbers, Aadhaar/SSN, credit card PAN) be exported to local developer machines or unapproved sandbox buckets.
- **Synthetic Data Generation:** Engineers must use approved synthetic data generators (e.g., Faker, Synthetic Data Vault - SDV) for local development and unit testing.
- **Model Training Data Cleanliness:** AI models developed for enterprise clients must not be trained on confidential or copyrighted intellectual property unless explicit contractual data rights are established in the MSA.

---

## 4. Data Engineer 30-60-90 Day Ramp Milestones
- **Month 1:** Configure local Python 3.11 / Poetry environment; obtain Databricks and Snowflake developer credentials; complete mandatory Data Privacy and HIPAA/GDPR certifications.
- **Month 2:** Build and deploy a dbt model transformation pipeline with automated Great Expectations data quality tests; shadow senior data architect on streaming Kafka pipeline.
- **Month 3:** Deploy an end-to-end RAG or analytics pipeline into staging environment; establish automated data drift monitoring and Grafana alerting.
"""

# 34. buddy_program_guidelines.md (MEDIUM ~4,500 chars)
docs_batch4["buddy_program_guidelines.md"] = """# NexaTech Solutions - Workplace Buddy Program Guidelines
**Document ID:** NT-HR-GDE-034  
**Version:** 2.3  
**Effective Date:** January 1, 2026  
**Owner:** People Operations & Culture Experience  
**Classification:** Internal - All Employees  

---

## 1. Purpose of the Buddy Program
Joining a new company can feel daunting. The NexaTech Buddy Program pairs every incoming team member with an experienced, friendly peer colleague (a "Buddy") to ensure a warm, smooth, and welcoming transition into our community during their first 90 days.

While a Technical Mentor guides code reviews and architecture, your Buddy is your informal partner for day-to-day cultural nuances, social connections, and navigating campus life.

---

## 2. Role and Responsibilities of a Buddy
A NexaTech Buddy agrees to:
- **Pre-Joining Outreach:** Send a friendly welcome email or LinkedIn message 2 days before Day 1 introducing themselves.
- **Day 1 Welcome:** Meet the new joiner at reception after HR induction, give a campus tour (cafeteria, wellness room, gym, coffee bars), and host a welcome lunch.
- **Weekly Check-Ins:** Schedule a recurring 30-minute informal coffee chat once a week for the first 4 weeks, transitioning to bi-weekly in Month 2 and 3.
- **Cultural Guide:** Help the new joiner navigate Slack channels (`#random`, `#tech-banter`, `#bangalore-foodies`), explain internal acronyms, and share tips for booking desks.
- **Psychological Safety:** Provide a confidential, judgment-free space for informal questions that the new joiner might hesitate to ask their direct manager.

---

## 3. Buddy Welcome Lunch Expense Allowance
- NexaTech sponsors a **Welcome Lunch Allowance of up to ₹2,000 INR** for the Buddy and new hire.
- The Buddy pays for the lunch and claims reimbursement via NexaPortal Expense Module under category *Buddy Welcome Lunch* by attaching the restaurant tax invoice within 14 days of Day 1.

---

## 4. Buddy Selection and Recognition
- **Eligibility:** Full-time confirmed employees with at least 9 months tenure at NexaTech and consistent performance ratings of 3.0 or higher.
- **Recognition:** Serving as an onboarding buddy is recognized during annual performance appraisals under *Culture and Mentorship*. Buddies receive a ₹2,500 Amazon voucher upon the new hire's successful 90-day confirmation.
"""

# 35. payroll_salary_structure.md (MEDIUM ~5,200 chars)
docs_batch4["payroll_salary_structure.md"] = """# NexaTech Solutions - Payroll, Compensation Architecture & Salary Structure Policy
**Document ID:** NT-FIN-POL-035  
**Version:** 4.1  
**Effective Date:** January 1, 2026  
**Owner:** Finance, Payroll Operations & Total Rewards  
**Classification:** Confidential - Internal  

---

## 1. Compensation Framework: Cost to Company (CTC)
NexaTech Solutions ("NexaTech") provides transparent, competitive, and legally compliant compensation packages. An employee's annual total compensation is represented as Cost to Company (CTC), comprising Fixed Compensation, Statutory Retirals, Tax-Friendly Flexible Benefits, and Annual Variable Pay.

---

## 2. Salary Components and Breakup

The standard monthly salary breakup is structured as follows:

| Salary Component | Percentage / Quantum of CTC | Tax Treatment | Description |
|---|---|---|---|
| **Basic Salary** | 40% to 50% of Fixed CTC | 100% Taxable | Base compensation; statutory foundation for Provident Fund and Gratuity calculations. |
| **House Rent Allowance (HRA)** | 50% of Basic (Metros) / 40% (Non-Metros) | Tax-exempt under Sec 10(13A) subject to rent receipts | Assistance toward residential rental accommodation. |
| **Leave Travel Allowance (LTA)** | Up to ₹50,000 per annum | Tax-exempt twice in a 4-year block under Sec 10(5) | Domestic travel with family during approved earned leave. |
| **Food & Meal Allowance** | ₹2,200 per month (₹26,400/year) | Non-taxable benefit | Disbursed via Pluxee / Sodexo digital meal card. |
| **Special Allowance** | Balancing residual monthly amount | 100% Taxable | Floating monthly allowance component. |
| **Employer Provident Fund (PF)** | 12% of Basic Salary | Exempt up to statutory caps | Employer's statutory contribution to EPFO. |
| **Gratuity Provision** | 4.81% of Basic Salary | Tax-exempt up to statutory limits upon payout | Statutory benefit accrued under Payment of Gratuity Act. |

---

## 3. Payroll Disbursement Timelines and Accounts
- **Disbursement Date:** Salaries are credited on the **last banking day** of each calendar month.
- **Bank Partnerships:** NexaTech maintains premier corporate salary account partnerships with **HDFC Bank, ICICI Bank, and Axis Bank**. Employees enjoy zero-balance salary accounts, free platinum debit cards, and preferential home loan interest rates.
- **Payslip Access:** Electronic monthly payslips and tax projection sheets are published on the Keka Payroll Portal by the 1st of every month.

---

## 4. Income Tax Deductions (TDS) and Investment Proofs
- **Tax Regimes:** Employees may elect either the *New Tax Regime (Section 115BAC)* or the *Old Tax Regime* at the start of each financial year (April) on Keka.
- **Investment Declarations (April):** Employees submit planned investments under 80C, 80D, HRA rent, and home loan interest.
- **Investment Proof Verification (January 1 - 20):** Actual tax-saving receipts (rent agreements with landlord PAN, insurance premium receipts, PPF passbooks) must be uploaded. Failure to submit verified proofs results in recalculation of TDS across January, February, and March payrolls.
"""

# 36. provident_fund_gratuity_guide.md (MEDIUM ~4,600 chars)
docs_batch4["provident_fund_gratuity_guide.md"] = """# NexaTech Solutions - Employees' Provident Fund (EPF) & Gratuity Guide
**Document ID:** NT-FIN-GDE-036  
**Version:** 3.2  
**Effective Date:** January 1, 2026  
**Owner:** Payroll Operations & Statutory Compliance Desk  
**Classification:** Internal - All Personnel  

---

## 1. Overview of Statutory Retirement Schemes
NexaTech complies fully with the *Employees' Provident Funds and Miscellaneous Provisions Act, 1952* and the *Payment of Gratuity Act, 1972*. These retirement safety nets ensure long-term wealth creation, social security, and post-service financial stability for all employees.

---

## 2. Employees' Provident Fund (EPF) Framework

### 2.1 Contributions and Universal Account Number (UAN)
- **Employee Contribution:** 12% of Basic Salary deducted monthly from payroll.
- **Employer Contribution:** 12% of Basic Salary contributed by NexaTech, split statutory between:
  - 3.67% credited to the Employee's EPF Account.
  - 8.33% (capped at ₹1,250/month statutory ceiling or actual basic) credited to the Employees' Pension Scheme (EPS).
- **Universal Account Number (UAN):** All joiners must provide their existing 12-digit UAN on Day 1 in Darwinbox. New joiners entering the formal workforce are assigned a fresh UAN within 15 days of joining.
- **Voluntary Provident Fund (VPF):** Employees can elect to contribute additional funds beyond 12% (up to 100% of Basic) to their EPF account to earn government-declared interest (currently ~8.25% p.a.). VPF enrollment opens annually in April.

---

## 3. Gratuity Scheme and Eligibility

### 3.1 Eligibility Threshold
Under the Payment of Gratuity Act, 1972, gratuity becomes payable to an employee upon:
- Separation from NexaTech after rendering **minimum 5 continuous years of service**.
- Retirement, superannuation, or total permanent disablement/mortality (for death or disability, the 5-year tenure condition is waived).

### 3.2 Calculation Formula
Gratuity is computed in accordance with the statutory formula:
$$\\text{Gratuity} = \\frac{15 \\times \\text{Last Drawn Basic Salary} \\times \\text{Completed Years of Service}}{26}$$
*(Service exceeding 6 months in the final year is rounded up to a full year.)*
- **Statutory Tax Exemption:** Gratuity payouts up to **₹20,00,000 INR** are 100% tax-exempt under Section 10(10) of the Income Tax Act.
- **Disbursement:** Gratuity is processed and disbursed within **30 calendar days** following the employee's Last Working Day (LWD).
"""

# 37. annual_bonus_incentive_plan.md (MEDIUM ~4,700 chars)
docs_batch4["annual_bonus_incentive_plan.md"] = """# NexaTech Solutions - Annual Performance Bonus & Variable Incentive Policy
**Document ID:** NT-HR-POL-037  
**Version:** 3.4  
**Effective Date:** January 1, 2026  
**Owner:** Total Rewards, Executive Compensation & Finance  
**Classification:** Confidential - Internal  

---

## 1. Philosophy and Plan Objectives
The NexaTech Variable Incentive Plan is designed to reward high-performing individuals and teams who directly drive client success, software delivery excellence, and enterprise profitability. The plan ties individual rewards to organizational performance.

---

## 2. Bonus Computation Formula
Variable pay is computed using a balanced tripartite formula:
$$\\text{Final Bonus Payout} = \\text{Target Variable Bonus} \\times C_M \\times B_M \\times I_M$$
Where:
1. **Target Variable Bonus:** The contractual variable component stipulated in the employee's offer letter (typically 10% to 25% of annual CTC depending on band).
2. **$C_M$ (Company Performance Multiplier - 40% Weightage):** Determined by overall NexaTech annual revenue and EBITDA targets (ranges from 0.0x to 1.3x).
3. **$B_M$ (Business Unit / Practice Multiplier - 30% Weightage):** Evaluates practice-level delivery margins, customer CSAT scores (>90%), and billable utilization (ranges from 0.0x to 1.2x).
4. **$I_M$ (Individual Performance Multiplier - 30% Weightage):** Derived directly from the employee's H2 performance appraisal rating:
   - Rating 5.0 (Exceptional): 1.4x multiplier.
   - Rating 4.0 (Exceeds Expectations): 1.15x multiplier.
   - Rating 3.0 (Meets Expectations): 1.0x multiplier.
   - Rating 2.0 (Needs Improvement): 0.0x (Forfeited).
   - Rating 1.0 (Unsatisfactory): 0.0x (Forfeited).

---

## 3. Payout Schedule and Eligibility Criteria
- **Evaluation Period:** Evaluated over the Financial Year (April 1 to March 31).
- **Payout Timing:** Disbursed annually with the **April payroll cycle** (credited on April 30).
- **Eligibility Window:** Employees must have completed at least **6 months of active service** during the financial year to be eligible for prorated bonus. Joiners after October 1 become eligible in the subsequent financial year.
- **Active Employment Condition:** An employee must be on the active payroll of NexaTech on the date of payout. Employees who have tendered their resignation or are serving notice on the date of disbursement are not eligible for bonus payouts.
"""

# 38. overtime_and_weekend_work_payout.md (MEDIUM ~4,300 chars)
docs_batch4["overtime_and_weekend_work_payout.md"] = """# NexaTech Solutions - Overtime, Weekend Work & Standby Compensation Policy
**Document ID:** NT-OPS-POL-038  
**Version:** 3.1  
**Effective Date:** January 1, 2026  
**Owner:** Workforce Management & Employee Relations  
**Classification:** Internal - Technical Operations  

---

## 1. Context and General Principles
NexaTech values work-life balance and designs engineering sprint plans to fit within standard 40-hour work weeks. However, critical production deployments, unexpected emergency outages, and major data migrations may occasionally require after-hours or weekend engagements.

This policy defines compensation, pre-approval requirements, and health protections for non-exempt overtime.

---

## 2. Eligibility & Exemption Status
- **Exempt Personnel (Bands 4 and above):** Lead Engineers, Engineering Managers, Architects, and Directors are classified as managerial/supervisory personnel and are not eligible for hourly overtime payouts; they receive compensatory off (Comp-Off) for emergency weekend work.
- **Non-Exempt Personnel (Bands 1 to 3):** Associate Engineers, QA Analysts, and Operations Associates working in formal 24/7 client support rosters qualify for monetary overtime compensation.

---

## 3. Overtime Rates and Calculation
- **Weekday Overtime (beyond 9 daily hours):** Paid at **1.5x of base hourly wage** (`[Basic Salary / 160] * 1.5 * Overtime Hours`).
- **Weekend / Declared Holiday Overtime:** Paid at **2.0x of base hourly wage** OR the employee may opt for 1 day of Compensatory Off (Comp-Off) plus 1.0x hourly pay.
- **Mandatory Pre-Approval:** All overtime work must be pre-authorized on NexaPortal by the Project Delivery Manager at least 24 hours in advance. Unapproved overtime logged post-facto will be rejected.
- **Maximum Cap:** To prevent developer burnout, overtime is strictly capped at a maximum of **16 hours per month** per employee.

---

## 4. Standby / On-Call Readiness Allowance
- When an engineer is required to remain on standby on call during a weekend (within 30 minutes of laptop response):
  - Weekend Standby Allowance: **₹2,000 INR per day** (Saturday or Sunday).
  - Public Holiday Standby: **₹3,000 INR per day**.
  - If an active incident occurs during standby, hourly overtime applies in addition to the standby allowance.
"""

# 39. corporate_credit_card_policy.md (MEDIUM ~4,600 chars)
docs_batch4["corporate_credit_card_policy.md"] = """# NexaTech Solutions - Corporate Credit Card Issuance & Management Policy
**Document ID:** NT-FIN-POL-039  
**Version:** 3.3  
**Effective Date:** February 1, 2026  
**Owner:** Corporate Finance, Accounts & Treasury  
**Classification:** Internal - Management Personnel  

---

## 1. Objective and Card Program Overview
To facilitate seamless international business travel, client hospitality, and essential enterprise cloud procurement, NexaTech Solutions issues corporate credit cards (NexaTech HDFC / American Express Corporate Cards) to eligible managerial and business development staff.

The corporate card is an enterprise financial instrument backed by corporate liability; cardholders must handle it with fiduciary responsibility.

---

## 2. Eligibility and Credit Limits
Corporate cards are allocated strictly based on organizational role, international travel frequency, and budgetary authority:

| Role / Band | Standard Monthly Credit Limit (INR) | Primary Card Purpose |
|---|---|---|
| **Account Executives & Sales Directors** | ₹2,50,000 | Client entertainment, domestic/foreign sales travel |
| **Delivery Leads & Practice Heads (Band 4-5)** | ₹2,00,000 | Project team dinners, software subscriptions, travel |
| **Vice Presidents & C-Suite Executives (Band 6+)** | ₹5,00,000 | Strategic customer engagements, international summits |

---

## 3. Permissible vs. Prohibited Card Usage
- **Permissible Expenses:** Business travel lodging, client business meals, taxi transport, approved developer cloud SaaS tool renewals, and urgent hardware replacement accessories during client on-site visits.
- **Strictly Prohibited:**
  1. Personal or family expenditures of any nature.
  2. Cash advances or ATM cash withdrawals (blocked at card network level).
  3. Gambling, lottery tickets, digital assets, or personal retail purchases.
  4. Personal hotel spa treatments, mini-bar snacks, or in-room movies.

---

## 4. Reconciliation Workflow and Expense Settlement
- **Monthly Statement Cycle:** Card statements generate on the 15th of each month.
- **Reconciliation SLA:** Cardholders must submit an expense report on NexaPortal matching all card transactions against itemized tax invoices within **10 calendar days** of statement generation.
- **Recovery of Unreconciled / Personal Charges:** Any transaction remaining unsubstantiated or deemed personal after 30 days will be flagged by Finance and deducted automatically from the cardholder's next payroll cycle, along with a 2% administrative fee. Continued default results in card cancellation.
"""

# 40. client_entertainment_expense_policy.md (MEDIUM ~4,400 chars)
docs_batch4["client_entertainment_expense_policy.md"] = """# NexaTech Solutions - Client Entertainment & Business Hospitality Policy
**Document ID:** NT-FIN-POL-040  
**Version:** 3.1  
**Effective Date:** January 1, 2026  
**Owner:** Legal, Corporate Governance & Finance  
**Classification:** Internal - Sales & Delivery Leadership  

---

## 1. Purpose and Guiding Ethics
NexaTech Solutions fosters authentic, professional relationships with prospective and current enterprise clients. Modest hospitality is a recognized element of business relationship building; however, entertainment must always be reasonable, proportionate, directly tied to clear business discussions, and compliant with global anti-bribery standards (FCPA, UK Bribery Act).

---

## 2. Entertainment Spending Ceilings
Business entertainment is permitted only for senior team members (Band 4 and above) hosting active or prospective clients:

| Location / Geography | Maximum Meal Ceiling (Per Person) | Approval Authority |
|---|---|---|
| **Domestic India (Tier 1 Metros)** | Up to **₹3,000 INR** per person | Practice / BU Head |
| **Domestic India (Tier 2/3 Cities)** | Up to **₹2,000 INR** per person | Practice / BU Head |
| **International (United States)** | Up to **$100 USD** per person | VP of Sales / BU Head |
| **International (United Kingdom / Europe)** | Up to **£80 GBP / €90 EUR** per person | VP of Sales / BU Head |

*Ceilings are inclusive of food, moderate alcoholic beverages, taxes, and gratuities.*

---

## 3. Strict Prohibitions
- **Government Officials:** Entertainment of public sector enterprise employees or government officials of any country is strictly capped at **₹1,000 INR** ($15 USD) for working box lunches; offering lavish dinners, golf retreats, or gifts to public servants is illegal and forbidden.
- **Adult / Inappropriate Venues:** Hosting clients at adult entertainment venues, nightclubs, gambling casinos, or luxury sporting events without prior written CEO approval is strictly prohibited.
- **Cash Gifting:** Cash, gift cards, or luxury items cannot be provided to clients under the guise of entertainment.

---

## 4. Documentation and Expense Claim Requirements
To claim reimbursement for business entertainment:
1. Submit claim within **14 calendar days** via NexaPortal Expense Module.
2. Provide an itemized official tax bill (credit card summary slips are rejected).
3. Itemize the **Full Name, Title, and Organization** of every guest present.
4. Provide a 2-to-3 sentence executive summary of the business topics discussed (e.g., "Explored Q3 cloud modernization architecture and SOW scoping with VP of Engineering, Acme Health").
"""

for filename, content in docs_batch4.items():
    file_path = DOCS_DIR / filename
    file_path.write_text(content.strip(), encoding="utf-8")
    print(f"Written: {filename} ({len(content)} chars)")

print("Batch 4 Complete: 10 files written.")
