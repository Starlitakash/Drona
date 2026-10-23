# NexaTech Solutions - Data, Analytics & AI Engineer Onboarding Guide
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
