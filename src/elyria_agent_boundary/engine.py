"""Public-safe reference engine for agent action boundary evaluation.

This module is intentionally simple and transparent. It is not private Elyria
runtime machinery. It demonstrates how enterprise agent actions can be
classified into ADMIT, HOLD, REFUSE, or REVALIDATE outcomes using explicit
boundary evidence.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple


CRITICAL_TOOL_TYPES = {
    "financial_movement",
    "access_change",
    "production_change",
    "legal_privacy_action",
}

HIGH_RISK_ACTIONS = {"execute", "record_update", "external_send", "workflow_trigger"}


@dataclass
class BoundaryDecision:
    """Decision returned by the public-safe boundary evaluator."""

    outcome: str
    reason_codes: List[str] = field(default_factory=list)
    required_remediation: List[str] = field(default_factory=list)
    evidence: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "outcome": self.outcome,
            "reason_codes": self.reason_codes,
            "required_remediation": self.required_remediation,
            "evidence": self.evidence,
        }


def _present(value: Any) -> bool:
    return value is not None and value != "" and value is not False


def evaluate_agent_action(scenario: Dict[str, Any]) -> Dict[str, Any]:
    """Evaluate an agent action scenario.

    Expected output:
    - ADMIT: required authority and controls are present.
    - HOLD: missing non-critical evidence or ownership must be completed.
    - REFUSE: critical boundary is missing.
    - REVALIDATE: prior approval is stale because conditions changed.
    """

    reason_codes: List[str] = []
    remediation: List[str] = []

    if scenario.get("revalidation_required") is True:
        return BoundaryDecision(
            outcome="REVALIDATE",
            reason_codes=["REVALIDATION_REQUIRED"],
            required_remediation=["Re-run boundary review before action proceeds."],
            evidence=scenario,
        ).to_dict()

    required_owners: List[Tuple[str, str]] = [
        ("business_owner", "Assign a business owner."),
        ("technical_owner", "Assign a technical owner."),
        ("tool_owner", "Assign a tool owner."),
    ]

    for field_name, fix in required_owners:
        if not _present(scenario.get(field_name)):
            reason_codes.append(f"MISSING_{field_name.upper()}")
            remediation.append(fix)

    if reason_codes:
        return BoundaryDecision("HOLD", reason_codes, remediation, scenario).to_dict()

    tool_type = str(scenario.get("tool_type", "")).lower()
    action_class = str(scenario.get("action_class", "")).lower()

    if tool_type in CRITICAL_TOOL_TYPES:
        return BoundaryDecision(
            outcome="REFUSE",
            reason_codes=["CRITICAL_TOOL_REQUIRES_SEPARATE_GOVERNANCE"],
            required_remediation=[
                "Route critical tool action through privileged governance and explicit executive authority."
            ],
            evidence=scenario,
        ).to_dict()

    if scenario.get("authority_resolved") is not True:
        reason_codes.append("AUTHORITY_UNRESOLVED")
        remediation.append("Resolve agent, user, and business authority before action.")

    if scenario.get("tool_scope_defined") is not True:
        reason_codes.append("TOOL_SCOPE_UNDEFINED")
        remediation.append("Define allowed and prohibited tool actions.")

    if scenario.get("human_approval_required") is True and scenario.get("approval_present") is not True:
        reason_codes.append("APPROVAL_REQUIRED_BUT_MISSING")
        remediation.append("Capture required human approval before action.")

    if reason_codes:
        return BoundaryDecision("REFUSE", reason_codes, remediation, scenario).to_dict()

    if scenario.get("telemetry_required") is True and scenario.get("telemetry_present") is not True:
        return BoundaryDecision(
            outcome="HOLD",
            reason_codes=["TELEMETRY_REQUIRED_BUT_MISSING"],
            required_remediation=["Implement action telemetry before execution."],
            evidence=scenario,
        ).to_dict()

    if action_class in HIGH_RISK_ACTIONS and scenario.get("human_approval_required") is not True:
        return BoundaryDecision(
            outcome="HOLD",
            reason_codes=["HIGH_RISK_ACTION_NEEDS_APPROVAL_BOUNDARY"],
            required_remediation=["Define approval boundary for high-risk action class."],
            evidence=scenario,
        ).to_dict()

    return BoundaryDecision(
        outcome="ADMIT",
        reason_codes=["BOUNDARY_RESOLVED"],
        required_remediation=[],
        evidence=scenario,
    ).to_dict()
