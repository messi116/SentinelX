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
        "id": "AUTH-003",
        "name": "Brute Force Authentication",
        "description": "Detects multiple failed authentication attempts within a short time window.",
        "severity": 8,
        "detection_mode": "sequence",
        "conditions": {
            "event_types": [
                "SSH authentication failure",
                "authentication failure",
                "login failure",
                "failed authentication",
            ],
            "min_events": 5,
            "window_minutes": 5,
        },
        "mitre_technique": "T1110",
        "response": "Investigate repeated authentication failures, source activity, affected account, and subsequent login activity.",
    },
    {
        "id": "AUTH-004",
        "name": "Successful Login After Failures",
        "description": "Detects successful authentication following preceding failed authentication attempts.",
        "severity": 9,
        "detection_mode": "sequence",
        "conditions": {
            "event_types": [
                "successful authentication",
                "login success",
                "authentication success",
                "successful login",
            ],
            "min_failed_events": 1,
            "window_minutes": 5,
        },
        "mitre_technique": "T1078",
        "response": "Investigate whether the successful authentication represents account compromise or legitimate recovery.",
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
