# NexaTech Solutions - Software Development Engineer (SDE) Onboarding & Technical Ramp-Up Guide
**Document ID:** NT-ENG-GDE-011  
**Version:** 4.2  
**Effective Date:** February 1, 2026  
**Owner:** Engineering Excellence & Developer Experience Guild  
**Classification:** Internal - Technical Staff  

---

## 1. Welcome to NexaTech Engineering
Congratulations on joining the NexaTech Solutions Engineering team! Our engineering organization comprises over 900 software engineers, distributed systems architects, cloud specialists, and QA automation professionals building high-resilience systems for global Fortune 500 enterprises.

This guide provides a structured technical blueprint for your first 90 days, covering hardware provisioning, local development environments, architectural standards, code review protocols, CI/CD pipelines, and key milestones.

---

## 2. Hardware and Standard Developer Tooling

### 2.1 Hardware Provisioning Baseline
All software engineers are issued standardized high-performance hardware configured by IT Services on Day 1:
- **Default SDE Hardware Tier:** Apple MacBook Pro 16-inch (Apple Silicon M3 Pro, 36GB Unified Memory, 1TB NVMe SSD) OR Dell XPS 15 (Intel Core i7 14th Gen, 32GB DDR5 RAM, 1TB NVMe SSD, Ubuntu LTS 24.04 or Windows 11 Enterprise).
- **Peripherals Issued:** Dual 27-inch 4K Dell UltraSharp monitors (issued at base office desks), NexaTech-branded USB-C multiport docking station, and Jabra Evolve 65 noise-canceling headset.
- **Home Setup Support:** Confirmed engineers can claim up to ₹15,000 INR under the Ergonomic Workstation Reimbursement Policy.

### 2.2 Standard Developer Tooling & Licenses
Your Okta SSO account provides automated license provisioning for the following toolchains:
- **Version Control & Collaboration:** GitHub Enterprise (`github.com/nexatech-solutions`), Jira Software Cloud, Confluence, Slack Enterprise Grid.
- **IDEs & Productivity:** JetBrains All Products Pack (IntelliJ IDEA Ultimate, PyCharm Professional, GoLand, WebStorm) or Visual Studio Code Enterprise with GitHub Copilot Enterprise extension enabled.
- **API Development & Testing:** Postman Enterprise Workspace, Insomnia Pro.
- **Containers & Virtualization:** Docker Desktop Enterprise (licensed via NexaTech Business Agreement) or Rancher Desktop.
- **Static Analysis & Security:** SonarQube Enterprise, Snyk Developer CLI, GitGuardian secret scanning.

---

## 3. Account Provisioning and Security Clearance

### 3.1 Core Account Check-in Checklist
Complete the following access verifications on Day 1:
1. **Active Directory & Okta Single Sign-On:** Verify login at `https://nexatech.okta.com` using credentials received via SMS from IT Helpdesk.
2. **Multi-Factor Authentication (MFA):** Pair Okta Verify on your smartphone with Number Matching enabled. Hardware YubiKey enrollment can be completed at the IT Support Kiosk on Floor 3.
3. **GitHub Enterprise Organization:** Accept the automated email invitation to `github.com/orgs/nexatech-solutions`. Ensure your hardware SSH key is generated using `ed25519` algorithms and registered with GPG commit signing:
   ```bash
   ssh-keygen -t ed25519 -C "your.name@nexatech.com"
   git config --global user.signingkey <GPG-KEY-ID>
   git config --global commit.gpgsign true
   ```
4. **AWS Developer Sandbox Access:** Access the AWS IAM Identity Center portal (`https://nexatech.awsapps.com/start`) to obtain temporary CLI credentials for your assigned Practice sandbox account.

### 3.2 Required Compliance Modules (Day 1 - 3)
Before production codebase read access is granted, you must complete four mandatory training modules on the NexaLearn LMS:
- *Secure Coding & OWASP Top 10 (2026 Edition)* - 90 minutes.
- *Information Security & SOC 2 Developer Responsibilities* - 45 minutes.
- *Open Source Software & Licensing Governance* - 30 minutes.
- *Data Privacy & GDPR / DPDP Act Developer Essentials* - 45 minutes.

---

## 4. Git Workflows, Branching & Pull Request Standards

### 4.1 Git Branching Architecture
NexaTech enforces a trunk-based branching strategy with short-lived feature branches:
- **Main / Trunk Branch:** Always kept deployable and protected. Direct commits and force-pushes are disabled at the GitHub branch protection level.
- **Branch Naming Standard:**
  - Feature: `feat/NEXA-<JIRA-ID>-short-description` (e.g., `feat/NEXA-1240-user-profile-api`)
  - Bugfix: `fix/NEXA-<JIRA-ID>-short-description`
  - Hotfix: `hotfix/NEXA-<JIRA-ID>-short-description`
  - Refactoring: `refactor/NEXA-<JIRA-ID>-short-description`

### 4.2 Pull Request (PR) Requirements
Every Pull Request must satisfy the following strict gating criteria before merging:
1. **Mandatory Peer Reviews:** At least two approving reviews: one from a designated peer SDE and one from the Module Lead / Senior SDE.
2. **Automated CI Checks:**
   - GitHub Actions pipeline must pass 100% green.
   - Unit test code coverage must meet or exceed **80%** on new lines of code (enforced by SonarQube quality gates).
   - Zero critical or high vulnerabilities flagged by Snyk dependency analysis and GitGuardian secret scans.
3. **Conventional Commits:** Commit messages must follow the Conventional Commits specification:
   ```text
   feat(auth): implement token refresh rotation for oauth2 client
   
   Closes: NEXA-1240
   Signed-off-by: Your Name <your.name@nexatech.com>
   ```

---

## 5. Architecture Standards and Technology Stacks

NexaTech follows strict technology radar tiers: *Adopt*, *Trial*, *Assess*, and *Hold*:
- **Backend Languages & Frameworks:** Java 21 LTS (Spring Boot 3.x), Python 3.11+ (FastAPI), Go 1.22+, TypeScript / Node.js 20 LTS (NestJS).
- **Frontend & Mobile:** React 18+, Next.js 14+, TypeScript, Tailwind CSS, Flutter for cross-platform mobile.
- **Databases & Messaging:** PostgreSQL 16+ (AWS Aurora Serverless v2), MongoDB 7+, Redis Enterprise Cluster, Apache Kafka (Confluent Cloud), RabbitMQ.
- **Cloud & Orchestration:** Amazon Web Services (AWS), Microsoft Azure, Kubernetes (EKS / AKS), Terraform for Infrastructure as Code (IaC), ArgoCD for GitOps deployments.

---

## 6. SDE 30-60-90 Day Success Milestones

```
[Day 1-30: Foundation & First Commit]
  ├── Set up local IDE and security tooling
  ├── Complete mandatory LMS compliance certifications
  ├── Shadow sprint planning, daily standup, and grooming
  ├── Resolve 2 "good-first-issue" bug tickets in sprint
  └── Ship your first pull request to staging environment

[Day 31-60: Independence & Delivery]
  ├── Own an end-to-end user story from grooming to production release
  ├── Write automated integration tests and documentation in Confluence
  ├── Perform peer code reviews for teammates
  └── Participate in on-call shadowing rotation alongside senior SDE

[Day 61-90: Mastery & Production Readiness]
  ├── Drive technical design for a feature sub-module
  ├── Conduct an architecture review with the Technical Lead
  ├── Participate fully in primary/secondary on-call rotation
  └── Present a 30-minute tech talk at the Engineering Guild Lunch & Learn
```

---

## 7. Mentorship and Buddy Program
Every incoming engineer is assigned two dedicated support contacts:
- **Technical Mentor (Senior SDE / Lead):** Guides your architectural understanding, reviews complex PRs, and conducts weekly 45-minute technical 1-on-1s.
- **Onboarding Buddy (Peer SDE):** Your informal go-to guide for day-to-day questions: navigating office perks, local team norms, cafeteria timings, and Slack channels.

---

## 8. Key Engineering Slack Channels & Contacts

| Slack Channel | Purpose | Key Contact |
|---|---|---|
| `#eng-announcements` | Organization-wide technical updates & releases | VP of Engineering |
| `#dev-support` | Peer troubleshooting, toolchain issues, environment help | DevEx Guild Leads |
| `#cloud-access-approvals` | AWS/Azure IAM privilege elevation requests | CloudOps On-Call |
| `#github-admin` | Repository creation, CI runner issues, branch access | DevOps Admin Team |
| `#security-champions` | Application security guidance, threat modeling | Application Security Lead |
| `#guild-python` / `#guild-java` | Language-specific best practices and tech talks | Guild Moderators |