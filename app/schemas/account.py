from pydantic import UUID4, BaseModel
from typing import Optional
from datetime import datetime

class AccountBase(BaseModel):
    """
    shared properties
    """
    name: Optional[str]
    description: Optional[str]
    # current_subscription_ends: Optional[datetime]
    # plan_id: Optional[UUID4]
    is_active: Optional[bool] = True

class AccountCreate(AccountBase):
    pass

class AccountUpdate(AccountBase):
    pass

class AccountInDBBase(AccountBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Account(AccountInDBBase):
    """
    Additional properties to return in API
    """
    pass

class AccountInDB(AccountInDBBase):
    pass