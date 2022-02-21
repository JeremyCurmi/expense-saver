from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: Optional[str]


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    updated_at: datetime

    class Config:
        orm_mode = True
