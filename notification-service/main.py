from fastapi import FastAPI
from typing import Dict, Optional
from pydantic import BaseModel
import os

app = FastAPI(title="Notification Service")

class NotificationData(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None

class Notification(BaseModel):
    type: str
    data: NotificationData

@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy", "service": "notification-service"}

@app.post("/notifications")
async def handle_notification(notification: Notification) -> Dict[str, str]:
    # In a real app, this would send actual notifications
    print(f"Received notification: {notification.type}")
    print(f"Data: {notification.data}")
    
    return {"status": "notification queued", "type": notification.type}
