"""Scenario schema helpers for the public-safe boundary engine."""

REQUIRED_FIELDS = [
    "scenario",
    "stage",
    "action_class",
    "tool_type",
    "data_classification",
    "business_owner",
    "technical_owner",
    "tool_owner",
    "authority_resolved",
    "tool_scope_defined",
    "human_approval_required",
    "approval_present",
    "telemetry_required",
    "telemetry_present",
    "revalidation_required",
]

DECISIONS = ["ADMIT", "HOLD", "REFUSE", "REVALIDATE"]

ACTION_CLASSES = ["observe", "recommend", "draft", "execute", "escalate", "refuse"]

TOOL_TYPES = [
    "read_only_knowledge",
    "internal_drafting",
    "record_update",
    "external_communication",
    "workflow_trigger",
    "financial_movement",
    "access_change",
    "production_change",
    "legal_privacy_action",
]
