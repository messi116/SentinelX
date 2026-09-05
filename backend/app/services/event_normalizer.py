from datetime import datetime, timezone
from typing import Any

from app.schemas.event import NormalizedEvent


class EventNormalizer:
    """Convert raw security telemetry into SentinelX's standard event format."""

    @staticmethod
    def normalize_wazuh_alert(alert: dict[str, Any]) -> NormalizedEvent:
        data = alert.get("data") or {}
        agent = alert.get("agent") or {}
        rule = alert.get("rule") or {}

        timestamp_value = alert.get("timestamp")

        if isinstance(timestamp_value, str):
            timestamp = datetime.fromisoformat(
                timestamp_value.replace("Z", "+00:00")
            )
        else:
            timestamp = datetime.now(timezone.utc)

        severity = rule.get("level")

        return NormalizedEvent(
            source="wazuh",
            event_type=rule.get("description", "wazuh_alert"),
            timestamp=timestamp,
            host=agent.get("name"),
            username=data.get("srcuser") or data.get("dstuser"),
            source_ip=data.get("srcip"),
            destination_ip=data.get("dstip"),
            source_port=data.get("srcport"),
            destination_port=data.get("dstport"),
            process_name=data.get("process_name"),
            process_id=data.get("process_id"),
            severity=severity,
            message=alert.get("full_log") or alert.get("message"),
            raw_data=alert,
        )