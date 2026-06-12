# Sample Agent Action Boundary Report

## Scenario

**Risky Tool-Using Agent**

An AI agent is being evaluated for production-candidate use. The agent can update customer records through an internal tool while confidential data is in scope.

---

## Decision

```text
REFUSE
```

---

## Rationale

The agent action cannot advance because authority is unresolved, tool scope is undefined, required approval is missing, and telemetry is not present.

---

## Evidence Summary

| Area | Status | Finding |
|---|---|---|
| Business owner | Present | Operations |
| Technical owner | Present | Automation Team |
| Tool owner | Present | Customer Records System |
| Action class | High risk | Execute / record update |
| Data classification | Confidential | Sensitive enterprise data in scope |
| Authority | Missing | Authority not resolved |
| Tool scope | Missing | Allowed and prohibited actions not defined |
| Human approval | Missing | Approval required but not present |
| Telemetry | Missing | Required audit trail not present |
| Revalidation | Not current issue | Refusal occurs before revalidation analysis |

---

## Required Remediation

- Define tool action scope.
- Resolve authority model.
- Require human approval for protected record updates.
- Implement telemetry for request, tool, action, data scope, approval, decision, and result.
- Re-run boundary review before pilot or production movement.

---

## Executive Summary

This agent should not advance to production-candidate execution. It may return for review after authority, tool scope, approval, and telemetry controls are implemented.
