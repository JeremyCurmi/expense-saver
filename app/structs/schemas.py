from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    last_modified: str

    class Config:
        orm_mode = True
