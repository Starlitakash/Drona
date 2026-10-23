# NexaTech Solutions - Cloud Infrastructure Governance, FinOps & Architecture Standards
**Document ID:** NT-OPS-POL-014  
**Version:** 3.4  
**Effective Date:** February 1, 2026  
**Owner:** CloudOps, Site Reliability Engineering (SRE) & FinOps Guild  
**Classification:** Confidential - Technical Infrastructure  

---

## 1. Purpose and Strategic Objectives
NexaTech Solutions ("NexaTech") manages enterprise cloud infrastructure spanning thousands of virtual instances, containerized Kubernetes clusters, serverless workloads, and petabytes of structured storage across Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP).

This policy sets enforceable governance standards for multi-account hierarchy, Infrastructure as Code (IaC), cost governance (FinOps), production change approvals, and data security.

---

## 2. Multi-Account Organization Architecture

NexaTech enforces a strict landing zone isolation architecture via AWS Organizations and Control Tower:

```
[NexaTech Master Root Organization]
  ├── Core Infrastructure OU
  │     ├── Security & CDC Account (GuardDuty, SecurityHub, CloudTrail aggregate)
  │     ├── Log Archive Account (WORM-compliant S3 storage)
  │     └── Shared Network Account (Transit Gateway, Direct Connect, Inspection VPC)
  ├── Engineering Practice Sandbox OU (Auto-nuked every 14 days, no prod data)
  ├── Client Development & QA OU (Isolated per client project)
  ├── Client Staging / Pre-Prod OU
  └── Production Workload OU (Strict zero-trust, MFA session tokens)
```

### 2.1 Environment Isolation Rules
- **Cross-Account Traffic:** Direct VPC peering between Sandbox and Production is blocked at the Service Control Policy (SCP) level.
- **Production Data Prohibition:** Production databases, customer PII, or live tokens must NEVER be copied or replicated into Development, QA, or Sandbox accounts. Anonymized synthetic data generators must be used for lower environments.

---

## 3. Infrastructure as Code (IaC) & Deployment Standards

### 3.1 Mandatory Terraform / OpenTofu Standards
- 100% of cloud resources must be provisioned via Infrastructure as Code using Terraform (version 1.7+) or OpenTofu. Manual configuration via cloud web consoles (AWS Console click-ops) is disabled in Staging and Production accounts.
- **State Management:** Terraform state files must reside in centralized remote backends (S3 with AES-256 server-side encryption and DynamoDB state locking). State files must never be committed to Git repositories.
- **Modular Design:** Teams must consume approved, hardened Terraform modules from the *NexaTech Internal Module Registry* (e.g., `terraform-aws-secure-vpc`, `terraform-aws-eks-hardened`).

### 3.2 Mandatory Resource Tagging Standard
Any resource provisioned without the following five mandatory metadata tags will be flagged by automated AWS Config rules and terminated after 48 hours in non-production accounts:
1. `Environment`: `production`, `staging`, `qa`, or `sandbox`
2. `ProjectCode`: Standard Jira billing code (e.g., `NEXA-PROJ-882`)
3. `OwnerEmail`: Tech Lead email alias (e.g., `lead.payments@nexatech.com`)
4. `CostCenter`: Finance allocation code (e.g., `CC-ENG-BLR-402`)
5. `DataClassification`: `public`, `internal`, `confidential`, or `restricted`

---

## 4. FinOps & Cost Governance

### 4.1 Practice Budget Caps and Auto-Alerts
Every business unit and client project is assigned a monthly cloud spending envelope established during contract scoping:
- **70% Threshold:** Automated Slack alert posted to `#finops-alerts` and Tech Lead notified.
- **90% Threshold:** Escalation email sent to Delivery Manager and Practice Head.
- **100% Threshold:** Mandatory architecture review with FinOps Lead. Non-essential sandbox resources (e.g., idle GPU instances, unattached EBS volumes) are paused automatically at 7:00 PM IST daily.

### 4.2 Storage and Compute Optimization Guidelines
- **Compute:** Production workloads must leverage AWS Graviton (ARM64) processors wherever compatible (yielding ~20% cost-performance benefit). Non-production environments must utilize Spot instances for worker nodes.
- **Database Scaling:** PostgreSQL and MySQL workloads must deploy AWS Aurora Serverless v2 with auto-pause enabled on developer QA clusters.
- **S3 Lifecycle Rules:** All non-production S3 buckets must enforce lifecycle rules transitioning objects to *S3 Infrequent Access* after 30 days and *Glacier Flexible Retrieval* or expiration after 90 days.

---

## 5. Production Change Approval Board (CAB) Protocols

Any architectural modification, database migration, or network reconfiguration impacting Production requires formal review:
- **Standard Changes:** Pre-approved low-risk changes (e.g., routine CI/CD container image tag updates) proceed automatically via ArgoCD pipelines.
- **Emergency Changes:** Must be approved live on bridge by the Incident Commander and CISO representative, with retrospective CAB documentation filed within 24 hours.
- **Major Architectural Changes:** Must submit a Request for Change (RFC) in Jira queue `CAB-REQ` by Wednesday 5:00 PM IST for review at the weekly Thursday 2:00 PM CAB meeting.

---

## 6. Access Control and Session Auditing
- Direct public SSH/RDP access (port 22 or 3389 open to `0.0.0.0/0`) is blocked by global SCPs.
- Administrative shell access routes through AWS Systems Manager (SSM) Session Manager or Teleport Bastion with full command keystroke logging stored in encrypted S3 buckets.
- High-privilege IAM roles (`AdministratorAccess`, `IAMFullAccess`) require multi-party approval via Slack bot `#cloud-access-approvals` and expire automatically after 4 hours.