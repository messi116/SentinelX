from datetime import datetime, timezone
from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def valid_event():
    return {
        "source": "test",
        "event_type": "SSH authentication failure",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "host": "test-host",
        "username": "testuser",
        "source_ip": "192.168.1.50",
        "destination_ip": "192.168.1.100",
        "severity": 6,
        "message": "Automated API test event",
        "raw_data": {
            "test": True,
            "source": "pytest",
        },
    }


def test_detection_api_valid_event():
    fake_finding = type(
        "FakeFinding",
        (),
        {
            "id": 1,
            "rule_name": "AUTH-001",
            "detection_type": "Authentication Failure",
            "description": "Detects authentication failure events.",
            "severity": 6,
            "confidence": 95,
            "status": "open",
        },
    )()

    with patch(
        "app.api.detection.evaluate_and_persist",
        return_value=[fake_finding],
    ):
        response = client.post(
            "/api/detection/evaluate",
            json=valid_event(),
        )

    assert response.status_code == 200

    data = response.json()

    assert data["event_type"] == "SSH authentication failure"
    assert data["finding_count"] == 1
    assert len(data["findings"]) == 1
    assert data["findings"][0]["rule_id"] == "AUTH-001"
    assert data["findings"][0]["status"] == "open"


def test_detection_api_no_finding():
    with patch(
        "app.api.detection.evaluate_and_persist",
        return_value=[],
    ):
        event = valid_event()
        event["event_type"] = "Normal system information"

        response = client.post(
            "/api/detection/evaluate",
            json=event,
        )

    assert response.status_code == 200

    data = response.json()

    assert data["event_type"] == "Normal system information"
    assert data["finding_count"] == 0
    assert data["findings"] == []


def test_detection_api_invalid_severity():
    event = valid_event()
    event["severity"] = 11

    response = client.post(
        "/api/detection/evaluate",
        json=event,
    )

    assert response.status_code == 422


def test_detection_api_missing_required_field():
    event = valid_event()
    del event["event_type"]

    response = client.post(
        "/api/detection/evaluate",
        json=event,
    )

    assert response.status_code == 422


def test_detection_api_response_structure():
    with patch(
        "app.api.detection.evaluate_and_persist",
        return_value=[],
    ):
        response = client.post(
            "/api/detection/evaluate",
            json=valid_event(),
        )

    assert response.status_code == 200

    data = response.json()

    assert "event_type" in data
    assert "finding_count" in data
    assert "findings" in data
    assert isinstance(data["finding_count"], int)
    assert isinstance(data["findings"], list)