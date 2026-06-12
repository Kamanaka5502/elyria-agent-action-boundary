# Architecture Diagram

## Agent Action Boundary Flow

```mermaid
flowchart TD
    A[Agent Request] --> B[Intent Classification]
    B --> C[Tool Inventory Check]
    C --> D[Data Scope Review]
    D --> E[Authority Boundary]
    E --> F[Human Approval Check]
    F --> G[Telemetry Requirement]
    G --> H[Revalidation Check]
    H --> I{Decision}
    I -->|ADMIT| J[Tool Call May Proceed]
    I -->|HOLD| K[Complete Evidence or Ownership]
    I -->|REFUSE| L[Stop Action]
    I -->|REVALIDATE| M[Run Boundary Review Again]
    J --> N[Post-Action Log]
    N --> O[Monitoring and Revalidation]
```

---

## Boundary Principle

```text
Tool access is not action authority.
```

An enterprise agent may be allowed to observe or draft without being allowed to execute, send, update, approve, or trigger protected workflow movement.
