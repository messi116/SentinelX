from datetime import datetime, timezone

from app.services.event_normalizer import EventNormalizer


def test_normalize_windows_wazuh_alert():
    alert = {
        "@timestamp": "2026-09-18T10:00:00.000Z",
        "agent": {
            "name": "windows-test",
            "ip": "192.168.18.161",
        },
        "decoder": {
            "name": "windows_eventchannel",
        },
        "rule": {
            "level": 7,
            "description": "Windows authentication event",
        },
        "data": {
            "win": {
                "system": {
                    "computer": "windows-test",
                    "message": "Authentication event",
                }
            },
            "srcuser": "testuser",
            "srcip": "192.168.18.50",
        },
        "full_log": "Windows authentication event",
    }

    normalized = EventNormalizer.normalize_wazuh_alert(alert)

    assert normalized.source == "wazuh"
    assert normalized.event_type == "windows_eventchannel"
    assert normalized.timestamp == datetime(
        2026, 9, 18, 10, 0, tzinfo=timezone.utc
    )
    assert normalized.host == "windows-test"
    assert normalized.username == "testuser"
    assert normalized.source_ip == "192.168.18.50"
    assert normalized.severity == 7
    assert normalized.message == "Windows authentication event"
    assert normalized.raw_data == alert


def test_normalize_ssh_wazuh_alert():
    alert = {
        "timestamp": "2026-09-18T10:05:00.000Z",
        "agent": {
            "name": "ubuntu-virtual-machine",
            "ip": "192.168.18.203",
        },
        "decoder": {
            "name": "sshd",
        },
        "rule": {
            "level": 5,
            "description": "sshd authentication failure",
        },
        "data": {
            "srcuser": "admin",
            "srcip": "192.168.18.50",
            "dstip": "192.168.18.203",
            "srcport": 54321,
            "dstport": 22,
        },
        "full_log": "Failed SSH authentication",
    }

    normalized = EventNormalizer.normalize_wazuh_alert(alert)

    assert normalized.source == "wazuh"
    assert normalized.event_type == "sshd"
    assert normalized.host == "ubuntu-virtual-machine"
    assert normalized.username == "admin"
    assert normalized.source_ip == "192.168.18.50"
    assert normalized.destination_ip == "192.168.18.203"
    assert normalized.source_port == 54321
    assert normalized.destination_port == 22
    assert normalized.severity == 5
    assert normalized.raw_data == alert


def test_normalize_auditd_process_event():
    alert = {
        "timestamp": "2026-09-18T10:10:00.000Z",
        "agent": {
            "name": "ubuntu-virtual-machine",
        },
        "decoder": {
            "name": "auditd",
        },
        "rule": {
            "level": 7,
            "description": "Process execution detected",
        },
        "data": {
            "user": "root",
            "process_name": "bash",
            "process_id": 1234,
            "pid": 1234,
        },
        "message": "Process execution detected",
    }

    normalized = EventNormalizer.normalize_wazuh_alert(alert)

    assert normalized.source == "wazuh"
    assert normalized.event_type == "auditd"
    assert normalized.host == "ubuntu-virtual-machine"
    assert normalized.username == "root"
    assert normalized.process_name == "bash"
    assert normalized.process_id == 1234
    assert normalized.severity == 7
    assert normalized.message == "Process execution detected"
    assert normalized.raw_data == alert


def test_normalize_missing_optional_fields():
    alert = {
        "timestamp": "2026-09-18T10:15:00Z",
        "agent": {
            "name": "minimal-host",
        },
        "rule": {
            "level": 3,
        },
    }

    normalized = EventNormalizer.normalize_wazuh_alert(alert)

    assert normalized.source == "wazuh"
    assert normalized.event_type == "wazuh_alert"
    assert normalized.host == "minimal-host"
    assert normalized.severity == 3
    assert normalized.raw_data == alert
