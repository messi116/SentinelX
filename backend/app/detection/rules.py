from typing import Any


DETECTION_RULES: list[dict[str, Any]] = [
    {
        "id": "AUTH-001",
        "name": "Authentication Failure",
        "description": "Detects authentication failure events.",
        "severity": 6,
        "conditions": {
            "event_types": [
                "SSH authentication failure",
                "authentication failure",
                "login failure",
            ]
        },
        "mitre_technique": "T1110",
        "response": "Create detection finding and investigate repeated authentication failures.",
    },
    {
        "id": "AUTH-002",
        "name": "Successful Authentication",
        "description": "Detects successful authentication events.",
        "severity": 3,
        "conditions": {
            "event_types": [
                "successful authentication",
                "login success",
                "authentication success",
            ]
        },
        "mitre_technique": "T1078",
        "response": "Record successful authentication and correlate with preceding authentication failures.",
    },
    {
        "id": "PROC-001",
        "name": "Suspicious Process Activity",
        "description": "Detects suspicious process execution events.",
        "severity": 7,
        "conditions": {
            "event_types": [
                "suspicious process",
                "process execution",
                "suspicious process activity",
            ]
        },
        "mitre_technique": "T1059",
        "response": "Create detection finding and preserve process-related evidence for investigation.",
    },
]
