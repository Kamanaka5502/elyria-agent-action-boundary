# Escalation and Refusal Model

## Purpose

Escalation and refusal are required safety states for production agentic systems.

A governed agent must be able to stop or route a request instead of attempting to complete an action when authority, data scope, approval, tool boundary, or risk conditions are unresolved.

---

## Escalation Conditions

Escalate when:

- authority is unclear
- data classification is unknown
- requested action affects a regulated or sensitive process
- action would change a system of record
- user intent is ambiguous
- tool result conflicts with policy
- safety, privacy, legal, or security review is required
- production impact cannot be assessed

---

## Refusal Conditions

Refuse when:

- the agent lacks authority to act
- the tool is out of approved scope
- the requested action is prohibited
- approval is required but missing
- the data source is unauthorized
- required telemetry is unavailable
- the action could create irreversible or high-impact consequence
- revalidation is required before action

---

## Safe Fallback Pattern

```text
Do not execute.
Explain the boundary.
Preserve the reason.
Escalate to the correct owner.
Request required evidence or approval.
```

---

## Operating Principle

A mature agentic system is not measured only by what it can do.

It is measured by what it can correctly refuse, route, or hold before unsafe action occurs.
