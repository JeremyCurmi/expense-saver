from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel


class Response(BaseModel):
    data: Optional[Any] = None
    status_code: int = 200


class ProductBase(BaseModel):
    name: str
    description: Optional[str]
    updated_at: Optional[datetime] = datetime.now()


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
