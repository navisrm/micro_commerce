from fastapi import FastAPI
from typing import Dict

app = FastAPI(title="User Service")

@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy", "service": "user-service"}
