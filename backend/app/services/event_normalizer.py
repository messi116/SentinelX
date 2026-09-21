from datetime import datetime, timezone
from typing import Any

from app.schemas.event import NormalizedEvent


class EventNormalizer:
    """Convert raw security telemetry into SentinelX's standard event format."""

    @staticmethod
    def _parse_timestamp(alert: dict[str, Any]) -> datetime:
        timestamp_value = (
            alert.get("@timestamp")
            or alert.get("timestamp")
        )

        if isinstance(timestamp_value, str):
            try:
                timestamp = datetime.fromisoformat(
                    timestamp_value.replace("Z", "+00:00")
                )

                if timestamp.tzinfo is None:
                    timestamp = timestamp.replace(
                        tzinfo=timezone.utc
                    )

                return timestamp

            except ValueError:
                pass

        return datetime.now(timezone.utc)

    @staticmethod
    def normalize_wazuh_alert(
        alert: dict[str, Any],
    ) -> NormalizedEvent:
        data = alert.get("data") or {}
        agent = alert.get("agent") or {}
        rule = alert.get("rule") or {}
        decoder = alert.get("decoder") or {}

        win = data.get("win") or {}
        win_system = win.get("system") or {}

        timestamp = EventNormalizer._parse_timestamp(alert)

        host = (
            agent.get("name")
            or win_system.get("computer")
        )

        username = (
            data.get("srcuser")
            or data.get("dstuser")
            or data.get("user")
        )

        source_ip = (
            data.get("srcip")
            or data.get("src_ip")
        )

        destination_ip = (
            data.get("dstip")
            or data.get("dst_ip")
        )

        source_port = (
            data.get("srcport")
            or data.get("src_port")
        )

        destination_port = (
            data.get("dstport")
            or data.get("dst_port")
        )

        process_name = (
            data.get("process_name")
            or data.get("process")
        )

        process_id = (
            data.get("process_id")
            or data.get("pid")
        )

        event_type = (
            decoder.get("name")
            or rule.get("groups", [None])[0]
            or "wazuh_alert"
        )

        message = (
            rule.get("description")
            or win_system.get("message")
            or alert.get("full_log")
            or alert.get("message")
        )

        severity = rule.get("level")

        return NormalizedEvent(
            source="wazuh",
            event_type=str(event_type),
            timestamp=timestamp,
            host=host,
            username=username,
            source_ip=source_ip,
            destination_ip=destination_ip,
            source_port=source_port,
            destination_port=destination_port,
            process_name=process_name,
            process_id=process_id,
            severity=severity,
            message=message,
            raw_data=alert,
        )

    @staticmethod
    def normalize_suricata_event(
        event: dict[str, Any],
    ) -> NormalizedEvent:
        timestamp = EventNormalizer._parse_timestamp(event)

        event_type = event.get("event_type") or "suricata_event"

        source_ip = event.get("src_ip")
        destination_ip = event.get("dest_ip")

        source_port = event.get("src_port")
        destination_port = event.get("dest_port")

        interface = event.get("in_iface")

        protocol = event.get("proto")

        message = (
            f"Suricata {event_type} event"
            + (f" over {protocol}" if protocol else "")
        )

        return NormalizedEvent(
            source="suricata",
            event_type=str(event_type),
            timestamp=timestamp,
            host=interface,
            source_ip=source_ip,
            destination_ip=destination_ip,
            source_port=source_port,
            destination_port=destination_port,
            message=message,
            raw_data=event,
        )
