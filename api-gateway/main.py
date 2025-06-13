from fastapi import FastAPI, HTTPException, Request
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

@app.api_route("/users/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def user_service_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        try:
            # Forward the request with the same method and body
            response = await client.request(
                method=request.method,
                url=f"{USER_SERVICE_URL}/{path}",
                headers={key: value for key, value in request.headers.items() if key.lower() != "host"},
                content=await request.body() if request.method in ["POST", "PUT", "PATCH"] else None
            )
            return response.json()
        except httpx.RequestError as exc:
            raise HTTPException(status_code=503, detail=f"User service unavailable: {str(exc)}")

@app.api_route("/products/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def product_service_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method=request.method,
                url=f"{PRODUCT_SERVICE_URL}/{path}",
                headers={key: value for key, value in request.headers.items() if key.lower() != "host"},
                content=await request.body() if request.method in ["POST", "PUT", "PATCH"] else None
            )
            return response.json()
        except httpx.RequestError as exc:
            raise HTTPException(status_code=503, detail=f"Product service unavailable: {str(exc)}")

@app.api_route("/orders/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def order_service_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method=request.method,
                url=f"{ORDER_SERVICE_URL}/{path}",
                headers={key: value for key, value in request.headers.items() if key.lower() != "host"},
                content=await request.body() if request.method in ["POST", "PUT", "PATCH"] else None
            )
            return response.json()
        except httpx.RequestError as exc:
            raise HTTPException(status_code=503, detail=f"Order service unavailable: {str(exc)}")
