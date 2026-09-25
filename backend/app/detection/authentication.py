from datetime import timedelta
from typing import Any

from app.schemas.event import NormalizedEvent


class AuthenticationDetector:
    """Detect authentication attack patterns across a sequence of events."""

    FAILED_EVENT_TYPES = (
        "ssh authentication failure",
        "authentication failure",
        "login failure",
        "failed authentication",
    )

    SUCCESS_EVENT_TYPES = (
        "successful authentication",
        "login success",
        "authentication success",
        "successful login",
    )

    DEFAULT_WINDOW_MINUTES = 5
    DEFAULT_MIN_FAILED_ATTEMPTS = 5

    @classmethod
    def detect_brute_force(
        cls,
        events: list[NormalizedEvent],
        min_failed_attempts: int = DEFAULT_MIN_FAILED_ATTEMPTS,
        window_minutes: int = DEFAULT_WINDOW_MINUTES,
    ) -> list[dict[str, Any]]:
        """Detect repeated failed authentication attempts."""

        if min_failed_attempts < 2:
            raise ValueError("min_failed_attempts must be at least 2")

        if window_minutes <= 0:
            raise ValueError("window_minutes must be greater than 0")

        findings: list[dict[str, Any]] = []
        failed_events = [
            event for event in events if cls._is_failed_auth(event)
        ]

        failed_events.sort(key=lambda event: event.timestamp)

        for index, start_event in enumerate(failed_events):
            window_end = start_event.timestamp + timedelta(
                minutes=window_minutes
            )

            window_events = [
                event
                for event in failed_events[index:]
                if event.timestamp <= window_end
                and cls._same_context(start_event, event)
            ]

            if len(window_events) >= min_failed_attempts:
                findings.append(
                    {
                        "rule_id": "AUTH-003",
                        "detection_type": "Brute Force Authentication",
                        "description": (
                            "Multiple failed authentication attempts "
                            "detected within a short time window."
                        ),
                        "severity": 8,
                        "mitre_technique": "T1110",
                        "response": (
                            "Investigate the source, affected account, "
                            "authentication pattern, and subsequent login activity."
                        ),
                        "event_count": len(window_events),
                        "first_event": window_events[0],
                        "last_event": window_events[-1],
                    }
                )
                break

        return findings

    @classmethod
    def detect_success_after_failures(
        cls,
        events: list[NormalizedEvent],
        min_failed_attempts: int = 1,
        window_minutes: int = DEFAULT_WINDOW_MINUTES,
    ) -> list[dict[str, Any]]:
        """Detect successful authentication following failed attempts."""

        if min_failed_attempts < 1:
            raise ValueError("min_failed_attempts must be at least 1")

        if window_minutes <= 0:
            raise ValueError("window_minutes must be greater than 0")

        findings: list[dict[str, Any]] = []
        ordered_events = sorted(events, key=lambda event: event.timestamp)

        for index, success_event in enumerate(ordered_events):
            if not cls._is_success_auth(success_event):
                continue

            window_start = success_event.timestamp - timedelta(
                minutes=window_minutes
            )

            preceding_failures = [
                event
                for event in ordered_events[:index]
                if (
                    window_start <= event.timestamp < success_event.timestamp
                    and cls._is_failed_auth(event)
                    and cls._same_context(success_event, event)
                )
            ]

            if len(preceding_failures) >= min_failed_attempts:
                findings.append(
                    {
                        "rule_id": "AUTH-004",
                        "detection_type": "Successful Login After Failures",
                        "description": (
                            "A successful authentication occurred after "
                            "preceding failed authentication attempts."
                        ),
                        "severity": 9,
                        "mitre_technique": "T1078",
                        "response": (
                            "Investigate whether the successful authentication "
                            "represents account compromise or legitimate recovery."
                        ),
                        "failed_event_count": len(preceding_failures),
                        "failed_events": preceding_failures,
                        "successful_event": success_event,
                    }
                )

        return findings

    @classmethod
    def _is_failed_auth(cls, event: NormalizedEvent) -> bool:
        event_type = event.event_type.lower()
        return any(pattern in event_type for pattern in cls.FAILED_EVENT_TYPES)

    @classmethod
    def _is_success_auth(cls, event: NormalizedEvent) -> bool:
        event_type = event.event_type.lower()
        return any(pattern in event_type for pattern in cls.SUCCESS_EVENT_TYPES)

    @staticmethod
    def _same_context(
        first: NormalizedEvent,
        second: NormalizedEvent,
    ) -> bool:
        if first.username and second.username:
            return first.username == second.username

        if first.host and second.host:
            return first.host == second.host

        return True


authentication_detector = AuthenticationDetector()
