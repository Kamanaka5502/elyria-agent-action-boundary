# Enterprise Demo Script

## Purpose

This script supports a concise buyer, hiring-panel, or executive walkthrough of the Elyria Agent Action Boundary.

---

## Opening

```text
This repository addresses the production risk created when AI agents move beyond chat and begin calling tools, retrieving data, updating systems, sending communications, or triggering workflows.

The question is not only whether the agent can complete the task. The question is whether the agent has authority to act, whether the tool is in scope, whether the data is permitted, whether human approval is required, and whether telemetry can prove what happened.
```

---

## Walkthrough Path

1. Start with `README.md` and explain the enterprise problem.
2. Open `docs/agent-action-boundary-model.md` and show the action classes.
3. Open `docs/tool-authority-matrix.md` and explain tool risk tiers.
4. Open `docs/human-approval-boundaries.md` and show approval tiers.
5. Open `docs/escalation-and-refusal-model.md` and show refusal conditions.
6. Open `sandbox/agent-boundary-playground.md` and walk through sample scenarios.
7. Open `reports/sample-agent-action-boundary-report.md` and show the enterprise output.

---

## Close

```text
The value is controlled agent deployment. This gives enterprises a repeatable pattern for deciding which agent actions can proceed, which must pause, which must be refused, and which must be revalidated before tool use becomes operational consequence.
```
