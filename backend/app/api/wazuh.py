from fastapi import APIRouter, HTTPException

from app.services.wazuh_service import wazuh_service

router = APIRouter(
    prefix="/api/wazuh",
    tags=["Wazuh"],
)


@router.get("/alerts")
async def get_wazuh_alerts(limit: int = 20):
    """Get recent Wazuh alerts."""

    try:
        return await wazuh_service.get_alerts(limit)

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    except PermissionError as exc:
        raise HTTPException(
            status_code=401,
            detail=str(exc),
        ) from exc

    except ConnectionError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc),
        ) from exc

    except RuntimeError as exc:
        raise HTTPException(
            status_code=502,
            detail=str(exc),
        ) from exc

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unexpected error while retrieving Wazuh alerts",
        )