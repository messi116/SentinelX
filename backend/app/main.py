from fastapi import FastAPI

app = FastAPI(
    title="SentinelX API",
    description="Evidence-first SOC investigation platform",
    version="0.1.0",
)


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