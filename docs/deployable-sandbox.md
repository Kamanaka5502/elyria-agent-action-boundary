# Deployable Sandbox

## Purpose

The deployable sandbox gives reviewers a simple way to run the public-safe agent boundary engine against sample enterprise scenarios.

It demonstrates the operating model without exposing private runtime machinery.

---

## Run Locally

From the repository root:

```bash
python sandbox/run_sandbox.py
```

The sandbox evaluates every JSON scenario in:

```text
examples/
```

It writes results to:

```text
sandbox/outputs/sandbox-results.json
```

---

## What the Sandbox Produces

Each result includes:

- scenario file
- scenario name
- expected outcome
- actual outcome
- reason codes
- required remediation

---

## Sample Decision Path

```text
safe-internal-agent.json           → ADMIT
risky-tool-agent.json              → REFUSE
revalidation-required-agent.json   → REVALIDATE
```

---

## Pilot Use

The sandbox can be used for:

- enterprise buyer demos
- AI governance pilot reviews
- agentic workflow discovery
- production-readiness conversations
- architecture interviews
- security and privacy review workshops

---

## Deployment Boundary

This sandbox is a reference implementation. Production deployment requires environment-specific security, identity, logging, privacy, legal, infrastructure, and policy review.
