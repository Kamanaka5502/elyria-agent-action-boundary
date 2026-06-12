# Human Approval Boundaries

## Purpose

Human approval boundaries define when an AI agent may act autonomously, when it may only draft or recommend, and when a human must approve before execution.

---

## Approval Tiers

| Tier | Agent Permission | Human Role |
|---|---|---|
| Tier 0 | Observe only | No approval required if access is already authorized. |
| Tier 1 | Recommend | Human decides whether to act. |
| Tier 2 | Draft | Human reviews before send, update, or workflow movement. |
| Tier 3 | Prepare action | Human approves before tool execution. |
| Tier 4 | Execute protected action | Requires explicit delegated authority and audit evidence. |
| Tier 5 | Critical action | Refuse or escalate; agent must not execute directly. |

---

## Human Approval Required When

- action affects a customer, employee, vendor, account, payment, legal status, access permission, production environment, or compliance position
- action changes a system of record
- action sends external communication
- action uses sensitive or regulated data
- action triggers downstream workflow movement
- action cannot be fully reversed
- authority or ownership is unclear

---

## Approval Evidence

Every approval should preserve:

- approver identity
- time of approval
- action requested
- tool involved
- data scope
- reason for approval
- conditions or limitations
- post-action telemetry link

---

## Operating Principle

Human approval is not a cosmetic checkpoint. It is the authority boundary that determines whether an AI-generated proposal may become enterprise action.
