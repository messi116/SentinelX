import os
from typing import Any

import httpx
from dotenv import load_dotenv

load_dotenv()


class WazuhService:
    def __init__(self):
        # Wazuh Manager API
        self.base_url = os.getenv("WAZUH_URL", "").rstrip("/")
        self.username = os.getenv("WAZUH_USERNAME", "")
        self.password = os.getenv("WAZUH_PASSWORD", "")

        # Wazuh Indexer API
        self.indexer_url = os.getenv("WAZUH_INDEXER_URL", "").rstrip("/")
        self.indexer_username = os.getenv("WAZUH_INDEXER_USERNAME", "")
        self.indexer_password = os.getenv("WAZUH_INDEXER_PASSWORD", "")

        self.token: str | None = None

    async def authenticate(self) -> str:
        """Authenticate against the Wazuh Manager API."""

        if not self.base_url:
            raise ValueError("WAZUH_URL is not configured")

        if not self.username or not self.password:
            raise ValueError("Wazuh API credentials are not configured")

        try:
            async with httpx.AsyncClient(
                verify=False,
                timeout=10.0,
            ) as client:
                response = await client.post(
                    f"{self.base_url}/security/user/authenticate",
                    auth=(self.username, self.password),
                )

                response.raise_for_status()

                data = response.json()
                self.token = data.get("data", {}).get("token")

                if not self.token:
                    raise RuntimeError(
                        "Wazuh API did not return a token"
                    )

                return self.token

        except httpx.ConnectTimeout as exc:
            raise ConnectionError(
                "Wazuh API connection timed out"
            ) from exc

        except httpx.ConnectError as exc:
            raise ConnectionError(
                "Unable to connect to Wazuh API"
            ) from exc

        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 401:
                raise PermissionError(
                    "Wazuh API authentication failed"
                ) from exc

            raise RuntimeError(
                f"Wazuh API returned HTTP {exc.response.status_code}"
            ) from exc

    async def get_alerts(self, limit: int = 20) -> Any:
        """Retrieve recent alerts from the Wazuh Indexer."""

        if limit < 1 or limit > 100:
            raise ValueError(
                "limit must be between 1 and 100"
            )

        if not self.indexer_url:
            raise ValueError(
                "WAZUH_INDEXER_URL is not configured"
            )

        if (
            not self.indexer_username
            or not self.indexer_password
        ):
            raise ValueError(
                "Wazuh Indexer credentials are not configured"
            )

        payload = {
            "size": limit,
            "sort": [
                {
                    "timestamp": {
                        "order": "desc"
                    }
                }
            ],
            "query": {
                "match_all": {}
            },
        }

        try:
            async with httpx.AsyncClient(
                verify=False,
                timeout=15.0,
            ) as client:

                response = await client.post(
                    f"{self.indexer_url}/wazuh-alerts-*/_search",
                    auth=(
                        self.indexer_username,
                        self.indexer_password,
                    ),
                    json=payload,
                )

                response.raise_for_status()

                data = response.json()
                hits = data.get("hits", {})

                total = hits.get("total", 0)

                if isinstance(total, dict):
                    total = total.get("value", 0)

                alerts = [
                    hit.get("_source", {})
                    for hit in hits.get("hits", [])
                ]

                return {
                    "total": total,
                    "alerts": alerts,
                }

        except httpx.ConnectTimeout as exc:
            raise ConnectionError(
                "Wazuh Indexer connection timed out"
            ) from exc

        except httpx.ConnectError as exc:
            raise ConnectionError(
                "Unable to connect to Wazuh Indexer"
            ) from exc

        except httpx.HTTPStatusError as exc:
            if exc.response.status_code in (401, 403):
                raise PermissionError(
                    "Wazuh Indexer authentication failed"
                ) from exc

            raise RuntimeError(
                f"Wazuh Indexer returned HTTP "
                f"{exc.response.status_code}"
            ) from exc

        except httpx.RequestError as exc:
            raise ConnectionError(
                "Wazuh Indexer request failed"
            ) from exc


wazuh_service = WazuhService()