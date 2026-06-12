# Telemetry and Auditability

## Purpose

Agentic systems require durable telemetry because tool use can create operational consequence.

The purpose of telemetry is to prove what the agent attempted, what it accessed, what tool was called, what decision was made, what approval existed, and what happened after action.

---

## Required Evidence

| Evidence | Purpose |
|---|---|
| Request ID | Tie action to a specific event. |
| User / initiator | Identify who or what initiated the request. |
| Agent identity | Identify the agent, model, workflow, or service. |
| Tool requested | Identify the tool or integration path. |
| Action class | Observe, recommend, draft, execute, escalate, refuse. |
| Data scope | Identify what data was accessed or affected. |
| Authority check | Preserve whether authority existed. |
| Approval record | Preserve required human or delegated approval. |
| Decision outcome | ADMIT / HOLD / REFUSE / REVALIDATE. |
| Reason codes | Explain why the decision occurred. |
| Post-action status | Show result, error, escalation, or refusal. |

---

## Audit Questions

- What did the agent attempt?
- What tool was involved?
- What data was accessed?
- What authority permitted or blocked the action?
- Was human approval required?
- Was approval present?
- What decision was made?
- What evidence supports the decision?
- What changed after the action?
- Does the action require revalidation?

---

## Operating Principle

If the enterprise cannot reconstruct the agent action path, it cannot prove governance.
