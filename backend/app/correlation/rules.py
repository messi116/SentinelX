from typing import Any


CORRELATION_RULES: list[dict[str, Any]] = [
    {
        "id": "CORR-001",
        "name": "Same Host Correlation",
        "description": "Correlates findings originating from the same host.",
        "window_minutes": 10,
        "fields": ["host"],
        "minimum_findings": 2,
    },
    {
        "id": "CORR-002",
        "name": "Same User Correlation",
        "description": "Correlates findings associated with the same user.",
        "window_minutes": 10,
        "fields": ["username"],
        "minimum_findings": 2,
    },
    {
        "id": "CORR-003",
        "name": "Multi-Stage Activity",
        "description": "Correlates multiple findings occurring close together.",
        "window_minutes": 15,
        "fields": ["host", "username"],
        "minimum_findings": 3,
    },
]
