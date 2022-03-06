from typing import List

from app.core.db import get_db
from app.services.services import CategoryCrud
from app.structs import Category, Response
from app.structs.schemas import CategoryCreate
from app.utils.utils import response_error, response_success
from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/categories",
    tags=["category"],
)


@router.get("/", response_model=List[Category])
async def get_categories(db: Session = Depends(get_db)):
    return CategoryCrud(db).get_all()


@router.get("/{id}", response_model=Response)
async def get_category_by_id(id: int, db: Session = Depends(get_db)):
    category = CategoryCrud(db).get_by_id(id)
    if category:
        return response_success(category)
    else:
        return response_error(f"Category with id {id} not found")


@router.post("/", response_model=Response, status_code=201)
async def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    try:
        CategoryCrud(db).create(**category.dict())
    except IntegrityError as e:
        return response_error(f"Category already exists: {e}", status_code=400)
    return response_success(data="Category has been created", status_code=201)
