from datetime import datetime, timezone

from app.detection.engine import DetectionEngine
from app.schemas.event import NormalizedEvent


def make_event(event_type: str, severity: int = 5) -> NormalizedEvent:
    return NormalizedEvent(
        source="test",
        event_type=event_type,
        timestamp=datetime.now(timezone.utc),
        host="test-host",
        username="testuser",
        source_ip="192.168.1.50",
        destination_ip="192.168.1.100",
        severity=severity,
        message="Automated test event",
        raw_data={"test": True},
    )


def test_authentication_failure_detection():
    event = make_event("SSH authentication failure")

    findings = DetectionEngine.detect(event)

    assert len(findings) == 1
    assert findings[0]["rule_id"] == "AUTH-001"
    assert findings[0]["detection_type"] == "Authentication Failure"


def test_successful_authentication_detection():
    event = make_event("Successful authentication")

    findings = DetectionEngine.detect(event)

    assert len(findings) == 1
    assert findings[0]["rule_id"] == "AUTH-002"


def test_suspicious_process_detection():
    event = make_event("Suspicious process activity")

    findings = DetectionEngine.detect(event)

    assert len(findings) == 1
    assert findings[0]["rule_id"] == "PROC-001"


def test_unmatched_event_returns_no_findings():
    event = make_event("Normal system information")

    findings = DetectionEngine.detect(event)

    assert findings == []


def test_rule_severity_is_preserved():
    event = make_event("Suspicious process activity", severity=3)

    findings = DetectionEngine.detect(event)

    assert len(findings) == 1
    assert findings[0]["severity"] == 7


def test_event_severity_higher_than_rule_is_used():
    event = make_event("Suspicious process activity", severity=9)

    findings = DetectionEngine.detect(event)

    assert len(findings) == 1
    assert findings[0]["severity"] == 9