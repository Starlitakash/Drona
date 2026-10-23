# NexaTech Solutions - Quality Engineering & QA Automation Onboarding Guide
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