<div align="center">

# Elyria Agent Action Boundary

## Agentic Governance · Tool-Use Boundaries · Action Authority · Production Safety

![License](https://img.shields.io/badge/license-MIT-1f4f5a?style=for-the-badge)
![Agentic AI](https://img.shields.io/badge/Agentic%20AI-Action%20Boundary-1f4f5a?style=for-the-badge)
![Tool Governance](https://img.shields.io/badge/Tool%20Governance-Authority%20Checked-2f6f73?style=for-the-badge)
![Enterprise Ready](https://img.shields.io/badge/Enterprise--Ready-Pilot%20Deployment-c9a66b?style=for-the-badge)
![Auditability](https://img.shields.io/badge/Auditability-Telemetry%20%2B%20Evidence-5f8fa3?style=for-the-badge)
![Deployable Sandbox](https://img.shields.io/badge/Deployable-Sandbox%20Runner-5f8fa3?style=for-the-badge)

### **Govern what an AI agent may access, call, change, escalate, or refuse before tool use becomes enterprise consequence.**

![Actions](https://img.shields.io/badge/Actions-Access%20%7C%20Call%20%7C%20Change%20%7C%20Send-2f6f73?style=flat-square)
![Decisions](https://img.shields.io/badge/Decision-ADMIT%20%7C%20HOLD%20%7C%20REFUSE%20%7C%20REVALIDATE-1f4f5a?style=flat-square)
![Human Approval](https://img.shields.io/badge/Human%20Approval-Required%20Boundaries-c9a66b?style=flat-square)
![Production](https://img.shields.io/badge/Production-Readiness%20Gate-5f8fa3?style=flat-square)

</div>

---

## Deployable Sandbox Quick Start

Run the public-safe sandbox from the repository root:

```bash
python sandbox/run_sandbox.py
```

The sandbox evaluates every scenario in:

```text
examples/
```

It produces decision results at:

```text
sandbox/outputs/sandbox-results.json
```

Expected path:

```text
safe-internal-agent.json           → ADMIT
risky-tool-agent.json              → REFUSE
revalidation-required-agent.json   → REVALIDATE
```

---

## What This Solves

Companies are moving from AI chat into AI agents.

That shift creates a higher-risk enterprise problem: agents can retrieve data, call tools, update records, create tickets, send messages, trigger workflows, recommend actions, and influence operational movement.

The risk is not only that an agent says something wrong. The risk is that an agent performs, triggers, or recommends action before the organization has resolved:

- what tools the agent may call
- what systems it may touch
- what data it may retrieve
- what authority permits action
- what actions require human approval
- what must be refused
- what must escalate
- what telemetry proves what happened
- what changes force revalidation

The **Elyria Agent Action Boundary** provides a public-safe, enterprise-ready reference architecture for governing agentic tool use before action becomes consequence.

---

## Why Enterprises Benefit

Enterprise teams gain a repeatable way to convert agent risk into operational architecture:

- tool inventory
- authority mapping
- action classification
- human approval boundaries
- escalation and refusal states
- telemetry and audit evidence
- production-readiness review
- revalidation after changes to tools, data, model, prompt, policy, or environment

The business value is direct: safer agent deployment, clearer accountability, stronger auditability, reduced uncontrolled automation risk, and a reusable pattern for enterprise AI adoption.

---

## Decision Model

```text
ADMIT      Agent action may proceed under current authority and controls.
HOLD       Required evidence, ownership, or control coverage is incomplete.
REFUSE     Agent action cannot proceed because a critical boundary is missing.
REVALIDATE Prior approval is stale because conditions changed.
```

---

## Enterprise Architecture Flow

```text
Agent request proposed
        ↓
Intent and action classification
        ↓
Tool inventory and system boundary check
        ↓
Data scope and sensitivity review
        ↓
Identity, authority, and approval boundary check
        ↓
Risk, safety, privacy, and operational impact review
        ↓
Telemetry and auditability requirements
        ↓
ADMIT / HOLD / REFUSE / REVALIDATE
        ↓
Tool call only if governed
        ↓
Post-action logging, monitoring, and revalidation
```

---

## End-to-End Coverage

| Layer | Enterprise Question | Repository Asset |
|---|---|---|
| Agent boundary model | What may the agent access, call, change, send, or trigger? | `docs/agent-action-boundary-model.md` |
| Tool authority | Which tools require approval, restriction, escalation, or refusal? | `docs/tool-authority-matrix.md` |
| Human approval | Which actions require review before execution? | `docs/human-approval-boundaries.md` |
| Escalation / refusal | What must stop or escalate instead of executing? | `docs/escalation-and-refusal-model.md` |
| Telemetry | What must be logged to prove agent behavior? | `docs/telemetry-and-auditability.md` |
| Production readiness | What evidence is required before pilot or production movement? | `docs/production-readiness-checklist.md` |
| Enterprise demo | How should this be shown to buyers, hiring panels, or executive stakeholders? | `docs/enterprise-demo-script.md` |
| Deployable sandbox | How can sample scenarios be executed locally? | `docs/deployable-sandbox.md` and `sandbox/run_sandbox.py` |
| Sample report | What does an enterprise-ready review output look like? | `reports/sample-agent-action-boundary-report.md` |

---

## Public-Safe Components

| Asset | Purpose |
|---|---|
| `src/elyria_agent_boundary/engine.py` | Public-safe decision engine for ADMIT / HOLD / REFUSE / REVALIDATE. |
| `src/elyria_agent_boundary/schema.py` | Scenario schema helpers and decision constants. |
| `sandbox/run_sandbox.py` | Local sandbox runner for example scenarios. |
| `docs/deployable-sandbox.md` | Sandbox runbook and pilot usage documentation. |
| `docs/agent-action-boundary-model.md` | Core architecture model for governing agentic action. |
| `docs/tool-authority-matrix.md` | Tool classification and authority matrix. |
| `docs/human-approval-boundaries.md` | Human-in-the-loop and delegated authority rules. |
| `docs/escalation-and-refusal-model.md` | Stop, escalate, refuse, and revalidate states. |
| `docs/telemetry-and-auditability.md` | Evidence requirements for tool calls and agent actions. |
| `docs/production-readiness-checklist.md` | Enterprise deployment readiness checklist. |
| `docs/enterprise-demo-script.md` | 10-minute buyer or hiring-panel demo path. |
| `examples/safe-internal-agent.json` | Lower-risk internal agent scenario. |
| `examples/risky-tool-agent.json` | High-risk agent scenario missing controls. |
| `examples/revalidation-required-agent.json` | Changed-condition revalidation scenario. |
| `sandbox/agent-boundary-playground.md` | Sandbox model for evaluating agent actions. |
| `reports/sample-agent-action-boundary-report.md` | Example enterprise readiness report. |
| `tests/expected-agent-boundary-outcomes.md` | Public-safe test expectations. |
| `NOTICE.md` | Public-safe boundary and attribution notice. |

---

## Relationship to Elyria Enterprise AI Control Plane

```text
Elyria Enterprise AI Control Plane
= governs enterprise AI movement across the organization.

Elyria Agent Action Boundary
= governs the most dangerous production layer: tool-using agents that may touch systems, data, workflows, communications, or operational action.
```

This repository is a focused agentic-governance layer, not a replacement for the broader Elyria architecture.

---

## Public Boundary

This repository is public-safe. It demonstrates the architecture surface, sandbox logic, examples, and enterprise readiness model, not private Elyria Systems runtime machinery, protected validators, customer-specific builds, commercial proof-corridor internals, credentials, keys, or confidential implementation details.

**Show the architecture. Protect the machinery.**
