from fastapi import FastAPI
from typing import Dict

app = FastAPI(title="Notification Service")

@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy", "service": "notification-service"}
