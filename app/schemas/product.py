from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    """
    shared properties
    """
    name: Optional[str]

class ProductName(ProductBase):
    pass