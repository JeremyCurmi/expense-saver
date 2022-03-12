from pydantic import UUID4, BaseModel
from typing import Optional
from app.schemas.role import Role

class UserRoleBase(BaseModel):
    """
    shared properties
    """
    user_id: Optional[UUID4]
    role_id: Optional[UUID4]

class UserRoleCreate(UserRoleBase):
    pass

class UserRoleUpdate(BaseModel):
    role_id: UUID4


class UserRoleInDBBase(UserRoleBase):
    role: Role

    class Config:
        orm_mode = True

class UserRole(UserRoleInDBBase):
    pass


class UserRoleInDB(UserRoleInDBBase):
    pass