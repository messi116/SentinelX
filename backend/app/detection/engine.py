from app.detection.rules import DETECTION_RULES
from app.schemas.event import NormalizedEvent


class DetectionEngine:
    """Evaluate normalized telemetry against deterministic detection rules."""

    @staticmethod
    def detect(event: NormalizedEvent) -> list[dict]:
        findings: list[dict] = []

        event_type = event.event_type.lower()

        for rule in DETECTION_RULES:
            for pattern in rule["event_types"]:
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
                            "event": event,
                        }
                    )
                    break

        return findings