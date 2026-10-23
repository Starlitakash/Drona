# NexaTech Solutions - Git Branching, Code Review & Pull Request Policy
**Document ID:** NT-ENG-POL-057  
**Version:** 3.5  
**Effective Date:** February 1, 2026  
**Owner:** Engineering Excellence Guild & DevOps Office  
**Classification:** Internal - Technical Staff  

---

## 1. Philosophy: Clean Version Control
Source code history is an immutable technical audit log. A disciplined Git workflow ensures code traceability, seamless rollbacks, and psychological safety for developers deploying to production.

---

## 2. Trunk-Based Development with Short-Lived Branches
NexaTech mandates **Trunk-Based Development**:
- **Trunk (`main` branch):** Always deployable and protected. Direct commits and history rewrites (`git push --force`) are disabled by GitHub branch protection rules.
- **Branch Lifespan:** Feature branches must live no longer than **48 to 72 hours**. Long-lived branches spanning multiple weeks are forbidden; complex features must be broken into incremental sub-tasks guarded by Feature Flags (LaunchDarkly).

---

## 3. Branch Naming Standards
Branches must reference an active Jira ticket identifier:
- `feat/NEXA-3401-add-sso-saml-login`
- `fix/NEXA-4120-null-pointer-invoice-calc`
- `refactor/NEXA-2209-migrate-orm-to-sqlalchemy2`
- `chore/NEXA-5501-upgrade-spring-boot-3-4`

---

## 4. Pull Request (PR) Requirements & Quality Gates
Before any PR can be merged into `main`, it must satisfy four mandatory criteria:
1. **Peer Review Approvals:** At least **two approving reviews** from engineering peers, including at least one Senior SDE or Technical Lead.
2. **Automated CI Checks:** GitHub Actions pipeline must complete 100% green:
   - Unit test code coverage >= 80% on new code.
   - SonarQube quality gate passing with zero new security hotspots.
   - Snyk dependency vulnerability check clean.
3. **Conventional Commits:** Pull request titles and squash commit messages must follow the Conventional Commits specification (`feat:`, `fix:`, `docs:`, `perf:`).
4. **Merge Method:** Repositories enforce **Squash and Merge** by default to ensure clean, atomic commit histories on the trunk branch.

---

## 5. Code Review Etiquette & SLAs
- **Review Turnaround SLA:** Reviewers must review assigned PRs within **24 business hours**.
- **Constructive Tone:** Code reviews must be empathetic and objective. Distinguish between blockers (*"This causes a race condition under concurrency"*) and non-blocking nitpicks (*"Nit: Could consider extracting this helper"*).

---

## Additional Operational Guidelines & Compliance

### Audit Trail & Regulatory Review
All requests, approvals, and dispute resolutions under this policy must be digitally recorded in NexaPortal with immutable audit logs retained for a minimum of 3 calendar years. Periodic internal audits are conducted bi-annually by the Internal Audit and Compliance Guild to verify adherence across all delivery centers.

### Exceptions and Variance Protocol
Any deviation from the standard limits or timelines specified in this document requires prior written concurrence from the Department Head and the Vice President of Operations. Retroactive exception approvals are strictly prohibited.

### Frequently Asked Questions (FAQ)
- **Q: Who do I contact if my ticket is delayed beyond the published SLA?**  
  *A:* Escalate to the department service lead via Slack on `#ops-escalations` or contact your assigned People Operations Business Partner (HRBP).
- **Q: How are policy updates communicated?**  
  *A:* Material revisions are announced during monthly all-hands meetings and updated in the official NexaTech Compliance Repository with change diffs documented.

### Contact Directory & Support Matrix
| Support Function | Primary Email Alias | Emergency Escalation |
|---|---|---|
| Department Service Desk | `servicedesk@nexatech.com` | Slack `#help-servicedesk` |
| Operations Compliance | `compliance@nexatech.com` | Level 2, HR Block |
| Employee Relations | `peopleops@nexatech.com` | Extension 4100 |
