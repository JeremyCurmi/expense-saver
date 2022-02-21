from typing import List

from app.core.db import get_db
from app.services.services import ProductCrud
from app.structs import Product
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@router.get("/", response_model=List[Product])
async def get_products(db: Session = Depends(get_db)):
    return ProductCrud(db).get_all()
