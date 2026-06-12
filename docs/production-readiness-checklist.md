# Production Readiness Checklist

## Purpose

This checklist defines what must be resolved before an AI agent is allowed to operate in a pilot, production-candidate, or production environment.

---

## Ownership

- [ ] Business owner assigned
- [ ] Technical owner assigned
- [ ] Tool owner assigned
- [ ] Data owner assigned where required
- [ ] Security reviewer assigned
- [ ] Production support owner assigned

---

## Tool Boundary

- [ ] Tool inventory completed
- [ ] Tool purpose documented
- [ ] Tool owner identified
- [ ] Tool action scope defined
- [ ] Allowed actions documented
- [ ] Prohibited actions documented
- [ ] Approval requirements mapped
- [ ] Revalidation triggers defined

---

## Data Boundary

- [ ] Data sources identified
- [ ] Data classification documented
- [ ] Sensitive data status confirmed
- [ ] Retrieval and access permissions mapped
- [ ] Data minimization reviewed
- [ ] Retention expectations documented

---

## Authority and Approval

- [ ] User authority model defined
- [ ] Agent authority model defined
- [ ] Delegated authority documented where applicable
- [ ] Human approval requirements defined
- [ ] Escalation path defined
- [ ] Refusal conditions defined

---

## Telemetry

- [ ] Request ID captured
- [ ] Agent identity captured
- [ ] Tool call captured
- [ ] Action class captured
- [ ] Data scope captured
- [ ] Approval record captured
- [ ] Decision outcome captured
- [ ] Reason codes captured
- [ ] Post-action status captured

---

## Final Production Decision

```text
ADMIT      Agent action boundary is resolved.
HOLD       Missing evidence or control coverage remains.
REFUSE     Critical action boundary is missing.
REVALIDATE Conditions changed; prior approval is stale.
```
