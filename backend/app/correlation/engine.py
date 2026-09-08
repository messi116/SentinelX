from datetime import datetime, timedelta
from typing import Any


class CorrelationEngine:
    """Correlate detection findings into potential incidents."""

    @staticmethod
    def correlate(findings: list[dict[str, Any]]) -> list[dict[str, Any]]:
        if len(findings) < 2:
            return []

        sorted_findings = sorted(
            findings,
            key=lambda finding: finding["detected_at"],
        )

        incidents: list[dict[str, Any]] = []

        for index, base_finding in enumerate(sorted_findings):
            related: list[dict[str, Any]] = [base_finding]

            base_time = base_finding["detected_at"]
            base_host = base_finding.get("host")
            base_username = base_finding.get("username")

            for candidate in sorted_findings[index + 1:]:
                candidate_time = candidate["detected_at"]

                if candidate_time - base_time > timedelta(minutes=15):
                    break

                same_host = (
                    base_host is not None
                    and candidate.get("host") == base_host
                )

                same_user = (
                    base_username is not None
                    and candidate.get("username") == base_username
                )

                if same_host or same_user:
                    related.append(candidate)

            if len(related) >= 2:
                incidents.append(
                    {
                        "title": "Correlated Security Activity",
                        "finding_count": len(related),
                        "findings": related,
                        "host": base_host,
                        "username": base_username,
                        "first_seen": related[0]["detected_at"],
                        "last_seen": related[-1]["detected_at"],
                    }
                )

        return incidents