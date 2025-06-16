from sqlalchemy import Boolean, Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from pydantic import BaseModel, EmailStr, constr
from typing import Optional
import enum

Base = declarative_base()

# Define UserRole values as a list for both Enum and SQLAlchemy
USER_ROLES = ['admin', 'customer', 'seller']

class UserRole(str, enum.Enum):
    ADMIN = USER_ROLES[0]
    CUSTOMER = USER_ROLES[1]
    SELLER = USER_ROLES[2]

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=False)
    phone = Column(String(20), unique=True, index=True, nullable=True)
    role = Column(Enum('admin', 'customer', 'seller', name='userrole', create_type=False), nullable=False, server_default='customer')
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    last_login = Column(DateTime, nullable=True)

# Pydantic models for request/response
class UserBase(BaseModel):
    email: EmailStr
    full_name: constr(min_length=2, max_length=100)
    phone: Optional[constr(min_length=10, max_length=20)] = None
    role: Optional[UserRole] = UserRole.CUSTOMER

class UserCreate(UserBase):
    password: constr(min_length=8)

class UserUpdate(BaseModel):
    full_name: Optional[constr(min_length=2, max_length=100)] = None
    phone: Optional[constr(min_length=10, max_length=20)] = None
    password: Optional[constr(min_length=8)] = None

class UserResponse(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    created_at: datetime
    last_login: Optional[datetime]
    
    class Config:
        from_attributes = True  # new name for orm_mode in Pydantic v2
