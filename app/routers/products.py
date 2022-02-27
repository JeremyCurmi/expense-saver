from typing import List

from app.core.db import get_db
from app.services.services import ProductCrud
from app.structs import Product, ProductCreate, Response
from app.utils.utils import response_error, response_success
from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@router.get("/", response_model=List[Product])
async def get_products(db: Session = Depends(get_db)):
    return ProductCrud(db).get_all()


@router.get("/{id}", response_model=Response)
async def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = ProductCrud(db).get_by_id(id)
    if product:
        return response_success(product)
    else:
        return response_error(f"Product with id {id} not found")


@router.get("/{name}", response_model=Response)
async def get_product_by_name(name: str, db: Session = Depends(get_db)):
    product = ProductCrud(db).get_by_name(name)
    if product:
        return response_success(product)
    else:
        return response_error(f"Product with name {name} not found")


@router.post("/", response_model=Response, status_code=201)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        ProductCrud(db).create(**product.dict())
    except IntegrityError as e:
        return response_error(f"Product already exists: {e}", status_code=400)
    return response_success(data="Product has been created", status_code=201)


@router.delete("/{id}", response_model=Response)
async def delete_product_by_id(id: int, db: Session = Depends(get_db)):
    try:
        ProductCrud(db).delete_by_id(id)
    except IntegrityError as e:
        return response_error(f"Product does not exist: {e}", status_code=400)
    return response_success(data="Product has been deleted")


@router.put("/{id}", response_model=Response)
async def update_product_by_id(
    id: int, product: ProductCreate, db: Session = Depends(get_db)
):
    ProductCrud(db).update(id, product)
    return response_success(data="Product has been updated")
