from fastapi import FastAPI, HTTPException
from typing import Dict
import httpx
import os

app = FastAPI(title="API Gateway")

# Service URLs from environment variables
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user-service:8000")
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://product-service:8001")
ORDER_SERVICE_URL = os.getenv("ORDER_SERVICE_URL", "http://order-service:8002")

@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy", "service": "api-gateway"}

@app.get("/users/{path:path}")
async def user_service_proxy(path: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{USER_SERVICE_URL}/{path}")
            return response.json()
        except httpx.RequestError as exc:
            raise HTTPException(status_code=503, detail=f"User service unavailable: {str(exc)}")

@app.get("/products/{path:path}")
async def product_service_proxy(path: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{PRODUCT_SERVICE_URL}/{path}")
            return response.json()
        except httpx.RequestError as exc:
            raise HTTPException(status_code=503, detail=f"Product service unavailable: {str(exc)}")

@app.get("/orders/{path:path}")
async def order_service_proxy(path: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{ORDER_SERVICE_URL}/{path}")
            return response.json()
        except httpx.RequestError as exc:
            raise HTTPException(status_code=503, detail=f"Order service unavailable: {str(exc)}")
