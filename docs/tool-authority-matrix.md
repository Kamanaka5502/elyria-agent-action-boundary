# Tool Authority Matrix

## Purpose

The Tool Authority Matrix classifies agent-accessible tools by impact, authority requirement, approval need, telemetry requirement, and default decision posture.

---

| Tool Type | Example | Risk | Required Boundary | Default Decision |
|---|---|---:|---|---|
| Read-only knowledge | Search approved docs | Low | Access scope and source authority | ADMIT |
| Internal drafting | Draft ticket or email | Medium | Human review before send | ADMIT / HOLD |
| Record update | Update CRM, ERP, HRIS, case system | High | Explicit authority and approval | HOLD |
| External communication | Send email, message customer, post update | High | Human approval and audit log | HOLD / REFUSE |
| Financial movement | Payment, refund, invoice, purchase | Critical | Strong approval and segregation | REFUSE unless separately governed |
| Access change | Permissions, roles, credentials | Critical | Privileged process only | REFUSE |
| Production change | Deploy, restart, modify config | Critical | Change-management authority | REFUSE unless governed |
| Legal/privacy action | Data subject response, legal notice | Critical | Legal/privacy authority | REFUSE / ESCALATE |

---

## Authority Questions

- Who owns the tool?
- What action can the tool perform?
- What systems or records can it affect?
- What data can it expose or change?
- What approval is required?
- What must be logged?
- What conditions force revalidation?

---

## Operating Rule

Tool access is not the same as action authority.

An agent may be allowed to see a tool but still be refused permission to execute a protected action through that tool.
