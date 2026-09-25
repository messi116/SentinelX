from app.detection.rules import DETECTION_RULES
from app.schemas.event import NormalizedEvent


class DetectionEngine:
    """Evaluate normalized telemetry against deterministic single-event rules."""

    @staticmethod
    def detect(event: NormalizedEvent) -> list[dict]:
        findings: list[dict] = []

        event_type = event.event_type.lower()

        for rule in DETECTION_RULES:
            if rule.get("detection_mode") == "sequence":
                continue

            conditions = rule.get("conditions", {})
            event_types = conditions.get("event_types", [])

            for pattern in event_types:
                if pattern.lower() in event_type:
                    findings.append(
                        {
                            "rule_id": rule["id"],
                            "detection_type": rule["name"],
                            "description": rule["description"],
                            "severity": max(
                                event.severity or 0,
                                rule["severity"],
                            ),
                            "mitre_technique": rule.get("mitre_technique"),
                            "response": rule.get("response"),
                            "event": event,
                        }
                    )
                    break

        return findings
