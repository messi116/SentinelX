from datetime import timedelta

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.correlation.engine import CorrelationEngine
from app.models.detection_finding import DetectionFinding
from app.models.incident import Incident
from app.models.telemetry_event import TelemetryEvent


class CorrelationService:
    """Build incidents from related detection findings."""

    @staticmethod
    def correlate_open_findings(db: Session) -> list[Incident]:
        findings = db.scalars(
            select(DetectionFinding)
            .where(DetectionFinding.status == "open")
            .order_by(DetectionFinding.detected_at)
        ).all()

        if len(findings) < 2:
            return []

        finding_data = []

        for finding in findings:
            event = db.get(TelemetryEvent, finding.event_id)

            if event is None:
                continue

            finding_data.append(
                {
                    "finding_id": finding.id,
                    "rule_name": finding.rule_name,
                    "detection_type": finding.detection_type,
                    "severity": finding.severity,
                    "confidence": finding.confidence,
                    "description": finding.description,
                    "detected_at": finding.detected_at,
                    "host": event.host,
                    "username": event.username,
                    "source_ip": event.source_ip,
                }
            )

        correlated = CorrelationEngine.correlate(finding_data)

        incidents: list[Incident] = []

        for group in correlated:
            related_findings = group["findings"]

            max_severity = max(
                finding["severity"]
                for finding in related_findings
            )

            confidence_values = [
                finding["confidence"]
                for finding in related_findings
                if finding["confidence"] is not None
            ]

            confidence = (
                max(confidence_values)
                if confidence_values
                else None
            )

            risk_score = min(
                100,
                (max_severity * 10) + (len(related_findings) * 5),
            )

            incident = Incident(
                title=group["title"],
                description=(
                    f"SentinelX correlated {len(related_findings)} "
                    f"detection findings involving "
                    f"host={group.get('host')} "
                    f"and username={group.get('username')}."
                ),
                severity=max_severity,
                risk_score=risk_score,
                status="open",
                confidence=confidence,
                first_seen=group["first_seen"],
                last_seen=group["last_seen"],
            )

            db.add(incident)
            incidents.append(incident)

        if incidents:
            db.commit()

            for incident in incidents:
                db.refresh(incident)

        return incidents