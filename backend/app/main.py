from fastapi import FastAPI
from app.api.alerts import router as alerts_router
from app.api.auth import router as auth_router

from app.api.wazuh import router as wazuh_router
from app.api.incidents import router as incidents_router
from app.api.detection import router as detection_router
from app.api.events import router as events_router
from app.api.hosts import router as hosts_router
from app.api.users import router as users_router
app = FastAPI(
    title="SentinelX API",
    description="Evidence-first SOC investigation platform",
    version="0.1.0",
)


app.include_router(wazuh_router)
app.include_router(detection_router)
app.include_router(events_router)
app.include_router(alerts_router)
app.include_router(incidents_router)
app.include_router(hosts_router)
app.include_router(users_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "name": "SentinelX",
        "status": "online",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }