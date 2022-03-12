from pydantic import UUID4, BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from app.schemas.user_role import UserRole

class UserBase(BaseModel):
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    account_id: Optional[UUID4] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserInDBBase(UserBase):
    id: UUID4
    user_role: Optional[UserRole]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class User(UserInDBBase):
    """Additional properties to return via API"""
    pass

class UserInDB(UserInDBBase):
    """Additional properties saved in db"""
    hashed_password: str