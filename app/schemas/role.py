from pydantic import UUID4, BaseModel
from typing import Optional

class RoleBase(BaseModel):
    """
    shared properties
    """
    name: Optional[str]
    description: Optional[str]

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class RoleInDBBase(RoleBase):
    id: UUID4

    class Config:
        orm_mode = True

class Role(RoleInDBBase):
    """
    Additional properties to return in API
    """
    pass

class RoleInDB(RoleInDBBase):
    pass