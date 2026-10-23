# NexaTech Solutions - Enterprise RESTful & GraphQL API Design Standards
**Document ID:** NT-ENG-STD-056  
**Version:** 4.2  
**Effective Date:** February 1, 2026  
**Owner:** Architecture Guild & API Center of Excellence (CoE)  
**Classification:** Internal - Technical Staff  

---

## 1. Strategic Principles of API Design
At NexaTech, APIs are first-class software products. Whether building public developer platforms or internal microservices, all APIs must be predictable, resilient, secure, self-documenting, and backwards-compatible.

---

## 2. API Design & Resource Modeling Standards

### 2.1 URI Naming Conventions
- **Nouns, Not Verbs:** Use plural nouns to represent resource collections. Verbs must never appear in URIs:
  - *Correct:* `GET /api/v1/customers`, `POST /api/v1/orders`
  - *Incorrect:* `GET /api/v1/getCustomers`, `POST /api/v1/createOrder`
- **Kebab-Case:** Use lowercase hyphenated naming for multi-word paths:
  - *Correct:* `/api/v1/payment-transactions`
  - *Incorrect:* `/api/v1/paymentTransactions`, `/api/v1/payment_transactions`
- **Sub-Resource Hierarchies:** Model parent-child relationships logically:
  - `GET /api/v1/customers/{customerId}/invoices`

### 2.2 Standard HTTP Verbs & Idempotency
- `GET`: Read resource(s). Must be safe and strictly idempotent.
- `POST`: Create a new resource. Non-idempotent.
- `PUT`: Complete resource replacement. Idempotent.
- `PATCH`: Partial resource mutation. Idempotent where possible.
- `DELETE`: Remove a resource. Idempotent.

### 2.3 API Versioning Strategy
- NexaTech enforces **URI Path Versioning**: `/api/v1/`, `/api/v2/`.
- Breaking changes (field removals, type modifications, mandatory parameter additions) mandate an increment in major version. Minor non-breaking changes (new optional fields) must maintain backwards compatibility.
- Older major versions must be supported for a minimum of **12 months** following public deprecation notices.

---

## 3. Standardized Error Handling (RFC 7807 Problem Details)
All API error responses must adhere strictly to the **RFC 7807 Problem Details** JSON specification:

```json
{
  "type": "https://api.nexatech.com/errors/invalid-resource-state",
  "title": "Invalid Payment State",
  "status": 422,
  "detail": "Invoice INV-9044 cannot be settled because it has already been voided.",
  "instance": "/api/v1/invoices/INV-9044/settlement",
  "code": "ERR_INVOICE_ALREADY_VOIDED",
  "timestamp": "2026-02-15T10:32:00Z",
  "traceId": "77325763-db54-4b4b-8b3c-8aeb1e3cca93"
}
```

---

## 4. Pagination, Filtering, and Sorting
- **Cursor-Based Pagination:** Mandatory for datasets exceeding 1,000 records:
  - `GET /api/v1/audit-logs?cursor=dXNlcl8xMjM=&limit=50`
- **Offset-Based Pagination:** Allowed for small, static datasets:
  - `GET /api/v1/products?page=2&page_size=25`
- Response payloads must include pagination metadata (`has_more`, `next_cursor`, `total_count`).

---

## 5. Security & Rate Limiting Gateways
- All external API traffic must terminate at our Kong / AWS API Gateway layer.
- **Authentication:** OAuth 2.0 with JSON Web Tokens (JWT) signed using RS256 algorithms.
- **Rate Limiting:** Standard consumer tiers enforce 100 requests per minute per IP; authenticated client tiers enforce 1,000 requests per minute with Redis sliding-window token buckets.