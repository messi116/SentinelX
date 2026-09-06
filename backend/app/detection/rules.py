from typing import Any


DETECTION_RULES: list[dict[str, Any]] = [
    {
        "id": "AUTH-001",
        "name": "Authentication Failure",
        "description": "Detects authentication failure events.",
        "event_types": [
            "SSH authentication failure",
            "authentication failure",
            "login failure",
        ],
        "severity": 6,
    },
    {
        "id": "AUTH-002",
        "name": "Successful Authentication",
        "description": "Detects successful authentication events.",
        "event_types": [
            "successful authentication",
            "login success",
            "authentication success",
        ],
        "severity": 3,
    },
    {
        "id": "PROC-001",
        "name": "Suspicious Process Activity",
        "description": "Detects suspicious process execution events.",
        "event_types": [
            "suspicious process",
            "process execution",
            "suspicious process activity",
        ],
        "severity": 7,
    },
]