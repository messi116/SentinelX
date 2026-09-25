from datetime import datetime, timedelta, timezone

from app.detection.authentication import AuthenticationDetector
from app.schemas.event import NormalizedEvent


BASE_TIME = datetime(2026, 9, 25, 14, 0, tzinfo=timezone.utc)


def make_event(
    event_type: str,
    minutes_offset: int = 0,
    username: str = "testuser",
    host: str = "test-host",
) -> NormalizedEvent:
    return NormalizedEvent(
        source="test",
        event_type=event_type,
        timestamp=BASE_TIME + timedelta(minutes=minutes_offset),
        host=host,
        username=username,
        source_ip="192.168.1.50",
        destination_ip="192.168.1.100",
        severity=5,
        message="Authentication test event",
        raw_data={"test": True},
    )


def test_brute_force_detection():
    events = [
        make_event("SSH authentication failure", 0),
        make_event("SSH authentication failure", 1),
        make_event("SSH authentication failure", 2),
        make_event("SSH authentication failure", 3),
        make_event("SSH authentication failure", 4),
    ]

    findings = AuthenticationDetector.detect_brute_force(events)

    assert len(findings) == 1
    assert findings[0]["rule_id"] == "AUTH-003"
    assert findings[0]["detection_type"] == "Brute Force Authentication"
    assert findings[0]["event_count"] == 5
    assert findings[0]["mitre_technique"] == "T1110"


def test_multiple_failed_logins_below_threshold_are_not_brute_force():
    events = [
        make_event("SSH authentication failure", 0),
        make_event("SSH authentication failure", 1),
        make_event("SSH authentication failure", 2),
        make_event("SSH authentication failure", 3),
    ]

    findings = AuthenticationDetector.detect_brute_force(events)

    assert findings == []


def test_successful_login_after_failures():
    events = [
        make_event("SSH authentication failure", 0),
        make_event("SSH authentication failure", 1),
        make_event("SSH authentication failure", 2),
        make_event("Successful authentication", 3),
    ]

    findings = AuthenticationDetector.detect_success_after_failures(events)

    assert len(findings) == 1
    assert findings[0]["rule_id"] == "AUTH-004"
    assert findings[0]["detection_type"] == "Successful Login After Failures"
    assert findings[0]["failed_event_count"] == 3
    assert findings[0]["mitre_technique"] == "T1078"


def test_successful_login_without_previous_failure_is_not_detected():
    events = [
        make_event("Successful authentication", 3),
    ]

    findings = AuthenticationDetector.detect_success_after_failures(events)

    assert findings == []


def test_events_outside_time_window_are_not_correlated():
    events = [
        make_event("SSH authentication failure", 0),
        make_event("SSH authentication failure", 1),
        make_event("SSH authentication failure", 2),
        make_event("SSH authentication failure", 3),
        make_event("SSH authentication failure", 10),
    ]

    findings = AuthenticationDetector.detect_brute_force(
        events,
        min_failed_attempts=5,
        window_minutes=5,
    )

    assert findings == []


def test_different_users_are_not_grouped_for_brute_force():
    events = [
        make_event("SSH authentication failure", 0, username="user1"),
        make_event("SSH authentication failure", 1, username="user2"),
        make_event("SSH authentication failure", 2, username="user1"),
        make_event("SSH authentication failure", 3, username="user2"),
        make_event("SSH authentication failure", 4, username="user1"),
    ]

    findings = AuthenticationDetector.detect_brute_force(events)

    assert findings == []


def test_success_after_failure_requires_same_context():
    events = [
        make_event(
            "SSH authentication failure",
            0,
            username="user1",
        ),
        make_event(
            "SSH authentication failure",
            1,
            username="user1",
        ),
        make_event(
            "Successful authentication",
            2,
            username="user2",
        ),
    ]

    findings = AuthenticationDetector.detect_success_after_failures(events)

    assert findings == []
