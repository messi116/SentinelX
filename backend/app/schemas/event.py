from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class NormalizedEvent(BaseModel):
    source: str = Field(..., min_length=1)
    event_type: str = Field(..., min_length=1)

    timestamp: datetime

    host: str | None = None
    username: str | None = None

    source_ip: str | None = None
    destination_ip: str | None = None

    source_port: int | None = None
    destination_port: int | None = None

    process_name: str | None = None
    process_id: int | None = None

    severity: int | None = Field(default=None, ge=0, le=10)

    message: str | None = None

    raw_data: dict[str, Any] | None = None