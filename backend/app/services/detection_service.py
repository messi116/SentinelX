from sqlalchemy.orm import Session

from app.detection.engine import DetectionEngine
from app.models.detection_finding import DetectionFinding
from app.models.telemetry_event import TelemetryEvent
from app.schemas.event import NormalizedEvent


def evaluate_and_persist(
    db: Session,
    event: NormalizedEvent,
) -> list[DetectionFinding]:

    findings = DetectionEngine.detect(event)

    if not findings:
        return []

    telemetry = TelemetryEvent(
        source=event.source,
        event_type=event.event_type,
        timestamp=event.timestamp,
        host=event.host,
        username=event.username,
        source_ip=event.source_ip,
        destination_ip=event.destination_ip,
        message=event.message,
        severity=event.severity,
        raw_data=event.raw_data,
    )

    db.add(telemetry)
    db.flush()

    saved_findings = []

    for finding in findings:
        result = DetectionFinding(
            event_id=telemetry.id,
            rule_name=finding["rule_id"],
            detection_type=finding["detection_type"],
            severity=finding["severity"],
            description=finding["description"],
            confidence=95,
            detected_at=event.timestamp,
            status="open",
        )

        db.add(result)
        saved_findings.append(result)

    db.commit()

    for result in saved_findings:
        db.refresh(result)

    return saved_findings