# Agent Action Boundary Model

## Purpose

The Agent Action Boundary defines what an AI agent may access, call, change, send, trigger, escalate, or refuse before tool use becomes enterprise consequence.

It is designed for enterprise environments where agents interact with business systems, internal tools, customer data, workflow engines, ticketing systems, messaging channels, retrieval systems, or production automation.

---

## Core Boundary Question

```text
What action is the agent attempting, under what authority, against what system or data, with what approval, telemetry, and revalidation requirements?
```

---

## Action Classes

| Class | Description | Default Posture |
|---|---|---|
| Observe | Read or summarize allowed information. | ADMIT if access is scoped. |
| Recommend | Produce advisory output for human review. | ADMIT or HOLD depending on risk. |
| Draft | Prepare a message, ticket, or workflow update without sending. | ADMIT with review. |
| Execute | Change a system, send communication, update record, or trigger workflow. | HOLD or REFUSE unless authority is resolved. |
| Escalate | Route to human, security, privacy, legal, or owner review. | ADMIT as safe fallback. |
| Refuse | Stop action because required boundary is missing. | Required for high-risk gaps. |

---

## Boundary Layers

1. Intent classification
2. Tool inventory
3. Data scope
4. Identity and authority
5. Human approval requirement
6. Action impact tier
7. Security and privacy review
8. Telemetry and auditability
9. Revalidation trigger check
10. Final decision

---

## Production Rule

```text
No agentic tool call should bind enterprise consequence unless tool scope, authority, approval, data boundary, telemetry, and revalidation conditions are resolved.
```

---

## Decision Outcomes

```text
ADMIT      Agent action may proceed under current controls.
HOLD       More evidence or ownership is required.
REFUSE     Required boundary is missing; action cannot proceed.
REVALIDATE Prior approval is stale because conditions changed.
```
