# Expected Agent Boundary Outcomes

## Purpose

This file documents expected public-safe outcomes for sample agent scenarios.

---

## Scenario 1: Safe Internal Knowledge Agent

Input:

```text
examples/safe-internal-agent.json
```

Expected outcome:

```text
ADMIT
```

Reason:

```text
Ownership, tool scope, authority, approval, telemetry, and data boundary are present.
```

---

## Scenario 2: Risky Tool-Using Agent

Input:

```text
examples/risky-tool-agent.json
```

Expected outcome:

```text
REFUSE
```

Reason:

```text
The scenario lacks resolved authority, defined tool scope, required approval, and telemetry.
```

---

## Scenario 3: Agent With Changed Tool Permission

Input:

```text
examples/revalidation-required-agent.json
```

Expected outcome:

```text
REVALIDATE
```

Reason:

```text
Prior approval cannot be relied on because tool permission conditions changed.
```
