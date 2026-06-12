from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from elyria_agent_boundary import evaluate_agent_action

EXAMPLES = ROOT / "examples"
REPORTS = ROOT / "sandbox" / "outputs"


def main():
    REPORTS.mkdir(parents=True, exist_ok=True)
    results = []

    for scenario_file in sorted(EXAMPLES.glob("*.json")):
        scenario = json.loads(scenario_file.read_text(encoding="utf-8"))
        decision = evaluate_agent_action(scenario)
        result = {
            "scenario_file": scenario_file.name,
            "scenario": scenario.get("scenario"),
            "expected_outcome": scenario.get("expected_outcome"),
            "actual_outcome": decision["outcome"],
            "reason_codes": decision["reason_codes"],
            "required_remediation": decision["required_remediation"],
        }
        results.append(result)

    output_path = REPORTS / "sandbox-results.json"
    output_path.write_text(json.dumps(results, indent=2), encoding="utf-8")

    print(json.dumps(results, indent=2))
    print(f"\nSandbox results written to {output_path}")


if __name__ == "__main__":
    main()
