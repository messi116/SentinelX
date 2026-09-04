from fastapi import FastAPI

from app.api.wazuh import router as wazuh_router

app = FastAPI(
    title="SentinelX API",
    description="Evidence-first SOC investigation platform",
    version="0.1.0",
)

app.include_router(wazuh_router)


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