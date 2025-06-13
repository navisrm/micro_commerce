from fastapi import FastAPI, HTTPException
from typing import Dict
from pydantic import BaseModel
import httpx
import os

app = FastAPI(title="User Service")

# Service URLs
NOTIFICATION_SERVICE_URL = os.getenv("NOTIFICATION_SERVICE_URL", "http://notification-service:8004")

class UserCreate(BaseModel):
    username: str
    email: str

@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy", "service": "user-service"}

@app.post("/users")
async def create_user(user: UserCreate) -> Dict[str, str]:
    # Simulate user creation
    # In a real app, this would save to the database
    
    # Send notification about new user
    async with httpx.AsyncClient() as client:
        try:
            notification_data = {
                "type": "user_created",
                "data": {"username": user.username, "email": user.email}
            }
            response = await client.post(
                f"{NOTIFICATION_SERVICE_URL}/notifications",
                json=notification_data
            )
            if response.status_code != 200:
                print(f"Warning: Notification failed: {response.text}")
        except httpx.RequestError as exc:
            print(f"Warning: Could not send notification: {str(exc)}")
    
    return {"message": f"User {user.username} created successfully"}
